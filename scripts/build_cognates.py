"""Build data/cognates.json from the curated source list.

For each curated entry, if `saadia_key` is set, look it up in
corpus-index.json and attach count + first occurrence. Modern slang
entries skip the corpus lookup (Saadia doesn't say 'yallah').

Output shape per entry:
  {
    "rank":            1,
    "modern_he":       "ראש",
    "modern_translit": "rosh",
    "modern_en":       "head",
    "arabic":          "رأس",
    "arabic_translit": "raʾs",
    "ja_form":         "ראס",
    "story":           "...",
    "group":           "body_parts",
    "count":           42,                     # 0 if not in Saadia
    "n_verses":        38,
    "first":           { "book_slug": "bereshit", "book": "Bereshit", "ch": 3, "v": 15 } | null
  }
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "data-source" / "cognates.curated.json"
CORPUS = REPO / "public" / "corpus-index.json"
OUT = REPO / "data" / "cognates.json"
BOOK_DISPLAY = {
    "bereshit": "Bereshit",
    "shemot": "Shemot",
    "vayikra": "Vayikra",
    "bamidbar": "Bamidbar",
    "devarim": "Devarim",
}
BOOK_ORDER = ["bereshit", "shemot", "vayikra", "bamidbar", "devarim"]


def build_verse_to_book_map() -> dict[tuple[int, int], list[str]]:
    DATA = REPO / "data"
    out: dict[tuple[int, int], list[str]] = defaultdict(list)
    for path in sorted(DATA.glob("tafsir-*.json")):
        if "-english" in path.stem:
            continue
        parts = path.stem.split("-")
        if len(parts) < 3:
            continue
        book_slug = parts[1]
        d = json.loads(path.read_text(encoding="utf-8"))
        for v in d.get("verses", []):
            out[(v["ch"], v["v"])].append(book_slug)
    return out


def main() -> None:
    curated = json.loads(SRC.read_text(encoding="utf-8"))
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    verse_to_book = build_verse_to_book_map()

    out_entries = []
    missing_keys = []
    for rank, src in enumerate(curated["entries"], start=1):
        key = src.get("saadia_key")
        count = 0
        n_verses = 0
        first = None
        if key:
            bucket = corpus["tokens"].get(key)
            if bucket:
                count = bucket["count"]
                verses_seen: set[tuple[int, int]] = set()
                for o in bucket["occurrences"]:
                    verses_seen.add((o[0], o[1]))
                n_verses = len(verses_seen)
                ch0, v0 = bucket["occurrences"][0][0], bucket["occurrences"][0][1]
                book_slugs = verse_to_book.get((ch0, v0), [])
                book_slugs.sort(
                    key=lambda s: BOOK_ORDER.index(s) if s in BOOK_ORDER else 99
                )
                book_slug = book_slugs[0] if book_slugs else "bereshit"
                first = {
                    "book_slug": book_slug,
                    "book": BOOK_DISPLAY.get(book_slug, book_slug.title()),
                    "ch": ch0,
                    "v": v0,
                }
            else:
                missing_keys.append((src["modern_he"], key))

        out_entries.append({
            "rank": rank,
            "modern_he": src["modern_he"],
            "modern_translit": src["modern_translit"],
            "modern_en": src["modern_en"],
            "arabic": src["arabic"],
            "arabic_translit": src["arabic_translit"],
            "ja_form": src.get("ja_form"),
            "story": src["story"],
            "group": src["group"],
            "count": count,
            "n_verses": n_verses,
            "first": first,
        })

    payload = {
        "_generated": "scripts/build_cognates.py",
        "_total": len(out_entries),
        "entries": out_entries,
    }
    OUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    size_kb = OUT.stat().st_size / 1024
    print(f"wrote {OUT.relative_to(REPO)} ({size_kb:.1f} KB, {len(out_entries)} entries)")
    with_saadia = sum(1 for e in out_entries if e["count"] > 0)
    print(f"  with Saadia hits: {with_saadia}/{len(out_entries)}")
    if missing_keys:
        print(f"  WARN: {len(missing_keys)} saadia_keys not in corpus:")
        for he, k in missing_keys:
            print(f"    {he!r} -> {k!r}")


if __name__ == "__main__":
    main()

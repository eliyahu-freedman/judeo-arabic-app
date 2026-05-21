"""Build public/first-50-ja-words.json from the curated source list.

Joins each curated entry to:
  - corpus-index.json    -> count, n_verses, first occurrence (ch, v)
  - dictionary-starter   -> optional root + extra note
  - dictionary-auto      -> fallback root if starter missed it

Output shape per entry:
  {
    "key":      "כ'לק",
    "rank":     1,                 # 1..50, position in curated order
    "lemma_ja": "כ'לק",
    "arabic":   "خَلَق",
    "en":       "created",
    "he_echo":  "ברא",
    "group":    "verbs",
    "note":     "...",
    "root":     "خ-ل-ق",           # if known
    "count":    87,                # occurrences in the Tafsir
    "n_verses": 64,                # unique verses
    "first":    { "book": "Bereshit", "ch": 1, "v": 1 }
  }
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "data-source" / "first-50-ja-words.curated.json"
CORPUS = REPO / "public" / "corpus-index.json"
DICT_STARTER = REPO / "data" / "dictionary-starter.json"
DICT_AUTO = REPO / "data" / "dictionary-auto.json"
# Output goes to data/ because at 20 KB it's small enough to static-import
# into the Next.js bundle. (Corpus-index lives in public/ because at 1.6 MB
# it would balloon first paint if bundled.)
OUT = REPO / "data" / "first-50-ja-words.json"
BOOK_SLUG_TO_DISPLAY = {
    "bereshit": "Bereshit",
    "shemot": "Shemot",
    "vayikra": "Vayikra",
    "bamidbar": "Bamidbar",
    "devarim": "Devarim",
}


def find_first_book(ch_v_pairs: list[tuple[int, int]]) -> tuple[str, int, int]:
    """Map the corpus-index's (ch, v) — which is global per book per file —
    back to a specific book. We do this by inspecting data/tafsir-*.json
    to figure out which book a (ch, v) belongs to. Since the corpus index
    stores ch as the within-book chapter number, we need to look up which
    book file contains that (ch, v)."""
    # The corpus index already stored ch as the book-local chapter, so we
    # don't know the book from the index alone. To resolve: scan all
    # data/tafsir-*.json once and build a (book, ch, v) -> True set.
    raise NotImplementedError("Use lookup table built once")


def build_verse_to_book_map() -> dict[tuple[int, int], list[str]]:
    """(ch, v) -> [list of book slugs that contain that pair]."""
    DATA = REPO / "data"
    out: dict[tuple[int, int], list[str]] = defaultdict(list)
    for path in sorted(DATA.glob("tafsir-*.json")):
        if "-english" in path.stem:
            continue
        # Filename like "tafsir-bereshit-1.json"
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
    starter = json.loads(DICT_STARTER.read_text(encoding="utf-8"))
    auto = json.loads(DICT_AUTO.read_text(encoding="utf-8"))

    starter_by_lemma: dict[str, dict] = {}
    for e in starter["entries"]:
        starter_by_lemma.setdefault(e["lemma_ja"], e)
    auto_by_lemma: dict[str, dict] = {}
    for e in auto["entries"]:
        auto_by_lemma.setdefault(e["lemma_ja"], e)

    verse_to_book = build_verse_to_book_map()

    out_entries = []
    missing = []
    for rank, src in enumerate(curated["entries"], start=1):
        key = src["key"]
        bucket = corpus["tokens"].get(key)
        count = bucket["count"] if bucket else 0
        n_verses = 0
        first = None
        if bucket:
            verses_seen: set[tuple[int, int]] = set()
            for o in bucket["occurrences"]:
                ch, v = o[0], o[1]
                verses_seen.add((ch, v))
            n_verses = len(verses_seen)
            # First occurrence in document order
            ch0, v0 = bucket["occurrences"][0][0], bucket["occurrences"][0][1]
            book_slugs = verse_to_book.get((ch0, v0), [])
            # If multiple books share that (ch, v), prefer canonical Pentateuch order
            book_order = ["bereshit", "shemot", "vayikra", "bamidbar", "devarim"]
            book_slugs.sort(key=lambda s: book_order.index(s) if s in book_order else 99)
            book_slug = book_slugs[0] if book_slugs else "bereshit"
            first = {
                "book_slug": book_slug,
                "book": BOOK_SLUG_TO_DISPLAY.get(book_slug, book_slug.title()),
                "ch": ch0,
                "v": v0,
            }
        else:
            missing.append(key)

        root = ""
        s_entry = starter_by_lemma.get(src["lemma_ja"]) or starter_by_lemma.get(key)
        a_entry = auto_by_lemma.get(src["lemma_ja"]) or auto_by_lemma.get(key)
        if s_entry and s_entry.get("root") and s_entry["root"] not in ("—", "-"):
            root = s_entry["root"]
        elif a_entry and a_entry.get("root"):
            root = a_entry["root"]

        out_entries.append({
            "rank": rank,
            "key": key,
            "lemma_ja": src["lemma_ja"],
            "arabic": src["arabic"],
            "en": src["en"],
            "he_echo": src.get("he_echo", ""),
            "group": src["group"],
            "note": src.get("note", ""),
            "root": root,
            "count": count,
            "n_verses": n_verses,
            "first": first,
        })

    payload = {
        "_generated": "scripts/build_first_50.py",
        "_total": len(out_entries),
        "entries": out_entries,
    }
    OUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    size_kb = OUT.stat().st_size / 1024
    print(f"wrote {OUT.relative_to(REPO)} ({size_kb:.1f} KB, {len(out_entries)} entries)")
    if missing:
        print(f"  WARN: {len(missing)} keys not found in corpus: {missing}")


if __name__ == "__main__":
    main()

"""Generic offline driver for hand-authored tafsir alignments.

Loads scripts/align_data/{book}_{chapter}.py (which must export an
ALIGNMENTS dict mapping verse-number → list of (he|None, ja, en) triples),
validates each triple against data/tafsir-{book}-{chapter}.json +
-english.json with a per-side sequential cursor (tolerant of non-canonical
Hebrew niqqud order via NFC matching), and writes
data/tafsir-{book}-{chapter}-alignment.json with source-exact HE substrings.

Run:
    python3 scripts/handalign_chapter.py --book shemot --chapter 2
    python3 scripts/handalign_chapter.py --book shemot --chapter 2 --write

Without --write, validates only and reports.
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def load_alignments(book: str, chapter: int) -> dict[int, list[tuple]]:
    mod = importlib.import_module(f"align_data.{book}_{chapter}")
    return mod.ALIGNMENTS


def load_sources(book: str, chapter: int) -> tuple[dict, dict[str, str]]:
    src = json.loads(
        (DATA_DIR / f"tafsir-{book}-{chapter}.json").read_text(encoding="utf-8"),
    )
    en = json.loads(
        (DATA_DIR / f"tafsir-{book}-{chapter}-english.json").read_text(
            encoding="utf-8",
        ),
    )["translations"]
    return src, en


def find_he(needle: str, haystack: str, start: int) -> tuple[int, str | None]:
    """Locate Hebrew needle tolerant of canonical-combining-mark reorder.

    Sefaria sometimes stores marks non-canonically (e.g. SHIN-DOT before
    HIRIQ). NFC of either form is identical and length-preserving for
    Hebrew (no precomposition), so we locate via NFC and slice from the
    untouched source — the written JSON then round-trips against the raw
    source for the runtime resolver.
    """
    n_needle = unicodedata.normalize("NFC", needle)
    n_hay = unicodedata.normalize("NFC", haystack)
    idx = n_hay.find(n_needle, start)
    if idx == -1:
        return -1, None
    return idx, haystack[idx : idx + len(n_needle)]


def validate(
    book: str,
    chapter: int,
) -> tuple[list[str], int, dict[int, list[tuple[str | None, str, str]]]]:
    alignments = load_alignments(book, chapter)
    src, en = load_sources(book, chapter)

    problems: list[str] = []
    total = 0
    resolved: dict[int, list[tuple[str | None, str, str]]] = {}
    by_v = {v["v"]: v for v in src["verses"]}

    for vnum, triples in alignments.items():
        if vnum not in by_v:
            problems.append(f"v{vnum}: not in source")
            continue
        he_full = by_v[vnum]["hebrew"]
        ja_full = by_v[vnum]["ja"]
        en_full = en.get(str(vnum), "")
        he_cur = ja_cur = en_cur = 0
        resolved_v: list[tuple[str | None, str, str]] = []
        for i, (he, ja, en_phrase) in enumerate(triples):
            ji = ja_full.find(ja, ja_cur)
            if ji == -1:
                problems.append(
                    f"v{vnum} pair {i}: JA {ja!r} not at/after cursor "
                    f"{ja_cur} in {ja_full!r}",
                )
                continue
            ei = en_full.find(en_phrase, en_cur)
            if ei == -1:
                problems.append(
                    f"v{vnum} pair {i}: EN {en_phrase!r} not at/after cursor "
                    f"{en_cur} in {en_full!r}",
                )
                continue
            he_exact: str | None = None
            if he:
                hi, sliced = find_he(he, he_full, he_cur)
                if hi == -1:
                    problems.append(
                        f"v{vnum} pair {i}: HE {he!r} not at/after cursor "
                        f"{he_cur} in {he_full!r}",
                    )
                    continue
                he_exact = sliced
                he_cur = hi + len(he)
            resolved_v.append((he_exact, ja, en_phrase))
            ja_cur = ji + len(ja)
            en_cur = ei + len(en_phrase)
            total += 1
        resolved[vnum] = resolved_v
    return problems, total, resolved


def write_sidecar(
    book: str,
    chapter: int,
    resolved: dict[int, list[tuple[str | None, str, str]]],
) -> Path:
    out_path = DATA_DIR / f"tafsir-{book}-{chapter}-alignment.json"
    alignments_json: dict[str, list[dict]] = {}
    for vnum, triples in resolved.items():
        rows = []
        for he, ja, en in triples:
            row: dict[str, str] = {"ja": ja, "en": en}
            if he:
                row["he"] = he
            rows.append(row)
        alignments_json[str(vnum)] = rows
    payload = {
        "_note": (
            f"Hebrew↔JA↔EN phrase-triple alignment for {book.title()} "
            f"{chapter}. Hand-authored (no API) via "
            "scripts/handalign_chapter.py + "
            f"scripts/align_data/{book}_{chapter}.py; validated against the "
            "source with a sequential per-side cursor."
        ),
        "_status": "draft",
        "_model": "hand-authored",
        "alignments": alignments_json,
    }
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    # Ensure align_data/ is importable when invoked from any cwd.
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    problems, total, resolved = validate(args.book, args.chapter)
    for p in problems:
        print("  ! " + p, file=sys.stderr)
    print(
        f"[{args.book} {args.chapter}] {total} pairs valid; "
        f"{len(problems)} problem(s)",
    )
    if problems:
        return 2
    if args.write:
        out = write_sidecar(args.book, args.chapter, resolved)
        print(f"wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

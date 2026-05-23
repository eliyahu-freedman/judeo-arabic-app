"""Validate a hand-written tafsir alignment sidecar against the source verses.

Loads data/tafsir-{book}-{chapter}-alignment.json and re-runs the same checks
the API path applies in scripts/align_tafsir_english.py:

  - Every triple's `ja` and `en` must appear verbatim in the verse on each
    side; `he` is optional but, when present, must appear verbatim in the
    Hebrew.
  - Triples must be in left-to-right order on every side (cursor walk).

Read-only: prints a report (kept / dropped / would-drop), does NOT rewrite
the file. Useful while hand-authoring — fix the JSON, re-run, repeat.

Usage:
    python3 scripts/validate_alignment.py --book shemot --chapter 1
    python3 scripts/validate_alignment.py --book shemot --all
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def validate_verse(
    he: str,
    ja: str,
    en: str,
    pairs: list[dict],
) -> tuple[int, list[str]]:
    """Return (kept_count, list_of_problem_descriptions)."""
    problems: list[str] = []
    he_cur = ja_cur = en_cur = 0
    kept = 0
    for i, p in enumerate(pairs):
        if not isinstance(p, dict) or "ja" not in p or "en" not in p:
            problems.append(f"pair {i}: malformed {p!r}")
            continue
        ja_phrase = p["ja"]
        en_phrase = p["en"]
        ji = ja.find(ja_phrase, ja_cur)
        if ji == -1:
            problems.append(
                f"pair {i}: JA {ja_phrase!r} not found at/after cursor {ja_cur}",
            )
            continue
        ei = en.find(en_phrase, en_cur)
        if ei == -1:
            problems.append(
                f"pair {i}: EN {en_phrase!r} not found at/after cursor {en_cur}",
            )
            continue
        he_phrase = p.get("he")
        if isinstance(he_phrase, str) and he_phrase:
            hi = he.find(he_phrase, he_cur)
            if hi == -1:
                problems.append(
                    f"pair {i}: HE {he_phrase!r} not found at/after cursor {he_cur} "
                    "(would be kept without he anchor)",
                )
            else:
                he_cur = hi + len(he_phrase)
        kept += 1
        ja_cur = ji + len(ja_phrase)
        en_cur = ei + len(en_phrase)
    return kept, problems


def validate_chapter(book: str, chapter: int) -> int:
    src_path = DATA_DIR / f"tafsir-{book}-{chapter}.json"
    en_path = DATA_DIR / f"tafsir-{book}-{chapter}-english.json"
    al_path = DATA_DIR / f"tafsir-{book}-{chapter}-alignment.json"
    for p in (src_path, en_path, al_path):
        if not p.exists():
            print(f"missing: {p}", file=sys.stderr)
            return 1

    src = json.loads(src_path.read_text(encoding="utf-8"))
    en = json.loads(en_path.read_text(encoding="utf-8"))["translations"]
    al = json.loads(al_path.read_text(encoding="utf-8"))["alignments"]

    total_kept = total_issues = 0
    bad_verses = 0
    for v in src["verses"]:
        vnum = str(v["v"])
        pairs = al.get(vnum, [])
        kept, problems = validate_verse(
            v["hebrew"], v["ja"], en.get(vnum, ""), pairs,
        )
        total_kept += kept
        total_issues += len(problems)
        if problems:
            bad_verses += 1
            print(f"  v{vnum}: kept {kept}/{len(pairs)}")
            for prob in problems:
                print(f"    - {prob}")

    status = "OK" if total_issues == 0 else f"{total_issues} issue(s) in {bad_verses} verse(s)"
    print(
        f"[{book} {chapter}] {total_kept} pairs kept; {status}",
    )
    return 0 if total_issues == 0 else 2


def discover_aligned_chapters(book: str) -> list[int]:
    prefix = f"tafsir-{book}-"
    suffix = "-alignment.json"
    chs = []
    for p in DATA_DIR.iterdir():
        name = p.name
        if not name.startswith(prefix) or not name.endswith(suffix):
            continue
        stem = name[len(prefix) : -len(suffix)]
        if stem.isdigit():
            chs.append(int(stem))
    return sorted(chs)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--book", required=True)
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    if not args.all and args.chapter is None:
        ap.error("either --chapter N or --all is required")

    if args.all:
        chapters = discover_aligned_chapters(args.book)
        if not chapters:
            print(f"no alignment files for book={args.book}", file=sys.stderr)
            return 1
        rc_any = 0
        for ch in chapters:
            rc = validate_chapter(args.book, ch)
            if rc != 0:
                rc_any = rc
        return rc_any

    return validate_chapter(args.book, args.chapter)


if __name__ == "__main__":
    raise SystemExit(main())

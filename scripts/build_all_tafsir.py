"""Ingest every parsha file in ~/Desktop/Rasag-Parshiot and write one
JSON per (book, chapter), aggregating across files so cross-parsha
chapters (e.g. Bereshit 6, which is split between 01-Bereshit.txt and
02-Noach.txt) merge cleanly.

Run:  python3 scripts/build_all_tafsir.py
      python3 scripts/build_all_tafsir.py --clean   # delete existing files first
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from build_tafsir import (  # noqa: E402
    OUT_DIR,
    PARSHA_TO_BOOK,
    clean_arabic,
    clean_hebrew_translation,
    clean_ja,
    parse_file,
)

SRC_DIR = Path.home() / "Desktop" / "Rasag-Parshiot"


def infer_book(source: Path) -> str:
    m = re.match(r"(\d+)-", source.name)
    if not m:
        return "Bereshit"
    return PARSHA_TO_BOOK.get(int(m.group(1)), "Bereshit")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=SRC_DIR)
    ap.add_argument(
        "--clean", action="store_true",
        help="Delete existing tafsir-*.json files (except *-english.json) before writing",
    )
    args = ap.parse_args()

    if not args.src.exists():
        print(f"missing source dir: {args.src}", file=sys.stderr)
        return 1

    if args.clean:
        for p in OUT_DIR.glob("tafsir-*.json"):
            if "-english" in p.stem:
                continue
            p.unlink()
            print(f"  rm {p.name}")

    sources = sorted(args.src.glob("[0-9][0-9]-*.txt"))
    if not sources:
        print(f"no parsha files in {args.src}", file=sys.stderr)
        return 2

    # (book, ch) -> dict(v -> verse)
    bucket: dict[tuple[str, int], dict[int, dict]] = {}

    for src in sources:
        book = infer_book(src)
        verses = parse_file(src)
        for v in verses:
            ch = v["ch"]
            vn = v["v"]
            v["ja"] = clean_ja(v["ja"])
            v["hebrew_translation"] = clean_hebrew_translation(v["hebrew_translation"])
            v["hebrew"] = re.sub(r"\s+", " ", v["hebrew"]).strip()
            v["arabic"] = re.sub(r"\s+", " ", v["arabic"]).strip()
            bucket.setdefault((book, ch), {})[vn] = v
        print(f"  read {src.name}: {len(verses):>4} verses")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    total_chapters = 0
    total_verses = 0
    by_book: dict[str, int] = {}
    for (book, ch), verses in sorted(bucket.items()):
        ordered = [verses[v] for v in sorted(verses)]
        out = OUT_DIR / f"tafsir-{book.lower()}-{ch}.json"
        out.write_text(
            json.dumps(
                {"book": book, "chapter": ch, "verses": ordered},
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        total_chapters += 1
        total_verses += len(ordered)
        by_book[book] = by_book.get(book, 0) + len(ordered)

    print()
    print(f"wrote {total_chapters} chapter files, {total_verses} verses total")
    for book in ["Bereshit", "Shemot", "Vayikra", "Bamidbar", "Devarim"]:
        if book in by_book:
            chs = sum(1 for k in bucket if k[0] == book)
            print(f"  {book:<10} {chs:>3} chapters · {by_book[book]:>5} verses")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Convert Eli's <slug>.md (English translation) into bahya-<slug>-english.json.

Usage:
  md_to_english_json.py bab7        # → data/bahya-bab7-english.json
  md_to_english_json.py hakdamah    # → data/bahya-hakdamah-english.json
  md_to_english_json.py bab8 bab9   # multiple slugs at once

Generalised from parse_bahya_bab1_english.py; handles any slug, including
non-integer ones like "hakdamah".

Strategy:
  - Read edition/translation/<slug>.md
  - Drop everything from "## Notes" / "## Footnotes" onward.
  - Strip superscript footnote markers (¹²³…).
  - Skip lines starting with # or bare horizontal-rule separators.
  - Treat blank lines as paragraph separators.
  - Join wrapped lines within a block with a space.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TRANSLATION_DIR = (
    Path.home()
    / "Downloads"
    / "genizah-research"
    / "bahya-hovot"
    / "edition"
    / "translation"
)
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

SUPERS_RE = re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+")


def process_slug(slug: str) -> None:
    src = TRANSLATION_DIR / f"{slug}.md"
    out = DATA_DIR / f"bahya-{slug}-english.json"

    if not src.exists():
        print(f"[{slug}] ERROR: {src} not found — write the translation first.")
        return

    text = src.read_text(encoding="utf-8")

    # Cut footnote definitions section.
    m = re.search(r"\n#+\s*(?:Notes|Footnotes)\b", text)
    if m:
        text = text[: m.start()]

    text = SUPERS_RE.sub("", text)

    paragraphs: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        keep = [
            line
            for line in block.splitlines()
            if not line.lstrip().startswith("#") and line.strip() != "---"
        ]
        joined = " ".join(l.strip() for l in keep if l.strip())
        if joined:
            paragraphs.append(joined)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(
            {
                "source_file": str(src),
                "translator": "Eliyahu Freedman (working draft)",
                "paragraphs": paragraphs,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"[{slug}] wrote {len(paragraphs)} paragraphs → {out.name}")


def main() -> None:
    slugs = sys.argv[1:]
    if not slugs:
        sys.exit("usage: md_to_english_json.py <slug> [<slug> ...]   e.g. bab7 bab8 hakdamah")
    for slug in slugs:
        process_slug(slug)


if __name__ == "__main__":
    main()

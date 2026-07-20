#!/usr/bin/env python3
"""
Convert Qirqisani Maqala markdown translation files to app JSON format.

Usage:
  python3 scripts/convert-maqala-md.py --maqala 1 --lang en
  python3 scripts/convert-maqala-md.py --maqala 1 --lang he
  python3 scripts/convert-maqala-md.py --maqala 2 --lang he

Produces qirqisani-m{N}-bab{NN}-{lang}.json in data/
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ── Source directories ──────────────────────────────────────────────────────
SOURCES = {
    (1, "en"): Path.home() / "Downloads/genizah-research/qirqisani-maqala1-english",
    (1, "he"): Path.home() / "Downloads/genizah-research/qirqisani-maqala1-hebrew",
    (2, "he"): Path.home() / "Downloads/genizah-research/qirqisani-maqala2-hebrew",
}

TRANSLATOR = {
    "en": "Eliyahu Freedman (working draft, 2026)",
    "he": "Eliyahu Freedman (תרגום עברי-טברנידי, 2026)",
}

LANG_SUFFIX = {
    "en": "english",
    "he": "hebrew",
}

OUT_DIR = Path(__file__).parent.parent / "data"


def clean_paragraph(text: str) -> str:
    # Strip inline footnote refs like [^1], [^12]
    text = re.sub(r'\[\^[\w\d]+\]', '', text)
    # Strip inline links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Strip emphasis markers (bold/italic) but keep content
    text = re.sub(r'\*{1,3}([^\*]+)\*{1,3}', r'\1', text)
    # Normalise whitespace
    text = ' '.join(text.split())
    return text.strip()


def parse_md(path: Path) -> list[str]:
    """Return list of prose paragraphs from a translation markdown file."""
    paragraphs = []
    current: list[str] = []

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()

        # Skip: H1, H2, H3-italic transliteration lines, blockquote preamble, --- dividers
        if line.startswith("# ") or line.startswith("## "):
            continue
        if line.startswith("> "):
            continue
        if line == "---":
            if current:
                para = clean_paragraph(" ".join(current))
                if para:
                    paragraphs.append(para)
                current = []
            continue

        # ### lines: either a transliteration subtitle (### *text*) → skip,
        # or a section marker (### §N — / ### פסקה N —) → keep as text
        if line.startswith("### "):
            content = line[4:].strip()
            # H3-italic subtitle: starts with * and ends with * → skip
            if content.startswith("*"):
                continue
            # Otherwise it's a section marker → flush current and emit as paragraph
            if current:
                para = clean_paragraph(" ".join(current))
                if para:
                    paragraphs.append(para)
                current = []
            section_text = clean_paragraph(content)
            if section_text:
                paragraphs.append(section_text)
            continue

        # Skip standalone italic-only lines (translator/editor notes like *Translated from...*)
        if line.startswith("*") and line.endswith("*") and not line.startswith("**"):
            continue

        # Empty line = paragraph break
        if not line:
            if current:
                para = clean_paragraph(" ".join(current))
                if para:
                    paragraphs.append(para)
                current = []
        else:
            current.append(line)

    if current:
        para = clean_paragraph(" ".join(current))
        if para:
            paragraphs.append(para)

    return paragraphs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--maqala", type=int, required=True, choices=[1, 2])
    ap.add_argument("--lang", required=True, choices=["en", "he"])
    args = ap.parse_args()

    key = (args.maqala, args.lang)
    if key not in SOURCES:
        print(f"ERROR: no source configured for maqala {args.maqala} lang {args.lang}", file=sys.stderr)
        sys.exit(1)

    src_dir = SOURCES[key]
    if not src_dir.exists():
        print(f"ERROR: source dir not found: {src_dir}", file=sys.stderr)
        sys.exit(1)

    # Find bab files: NN_bab_NN.md  (skip 00_introduction.md)
    bab_files = sorted(f for f in src_dir.glob("*.md") if not f.name.startswith("00_"))

    produced = 0
    for md_path in bab_files:
        # Extract bab number from filename like "02_bab_02.md"
        m = re.match(r'^(\d+)_', md_path.name)
        if not m:
            continue
        bab_n = int(m.group(1))
        if bab_n == 0:
            continue
        # M1 bab01 is already hand-authored in the app — skip it
        if args.maqala == 1 and bab_n == 1:
            continue

        paragraphs = parse_md(md_path)
        if not paragraphs:
            print(f"WARNING: no paragraphs extracted from {md_path.name}")
            continue

        suffix = LANG_SUFFIX[args.lang]
        out_file = OUT_DIR / f"qirqisani-m{args.maqala}-bab{bab_n:02d}-{suffix}.json"
        payload = {
            "translator": TRANSLATOR[args.lang],
            "paragraphs": paragraphs,
        }
        out_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

        # For English files, also write an aligned stub if M1 (M2 aligned stubs from build-m2-json.py)
        if args.lang == "en" and args.maqala == 1:
            stub_file = OUT_DIR / f"qirqisani-m{args.maqala}-bab{bab_n:02d}-aligned.json"
            if not stub_file.exists():
                stub_file.write_text(json.dumps({"pages": {}}, ensure_ascii=False, indent=2), encoding="utf-8")

        print(f"  {out_file.name}: {len(paragraphs)} paragraphs")
        produced += 1

    print(f"\nDone — {produced} files written to {OUT_DIR}")


if __name__ == "__main__":
    main()

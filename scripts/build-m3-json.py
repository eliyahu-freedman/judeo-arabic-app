#!/usr/bin/env python3
"""
Build M3 base Arabic JSON + English JSON from reqirqisanifiles re-ocr-output structure.
Each bab has: merged-arabic.txt (=== pNNN === delimited) + english.md

Usage:
  python3 scripts/build-m3-json.py

Produces in data/:
  qirqisani-m3-bab{NN}.json          — base (Arabic script)
  qirqisani-m3-bab{NN}-english.json  — English paragraphs
  qirqisani-m3-bab{NN}-aligned.json  — empty alignment stub
"""

import json
import re
from pathlib import Path

OCR_ROOT = Path.home() / "Downloads/reqirqisanifiles/re-ocr-output"
OUT_DIR = Path(__file__).parent.parent / "data"

WORK = "Kitāb al-Anwār wa'l-Marāqib"
AUTHOR = "Yaʿqūb al-Qirqisānī (10th c.)"
SUBTITLE = "Discourse III: Polemics against Christianity and Islam"
TRANSLATOR = "Eliyahu Freedman (working draft, 2026)"

# M3 bab titles (extracted from english.md H2 headers)
# These are filled dynamically.


def extract_bab_title_en(md_text: str) -> str:
    """Extract the H2 bab title from the English markdown."""
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("## "):
            return line[3:].strip()
    return ""


def extract_bab_title_ar(arabic_text: str) -> str:
    """Extract first الباب / الشعر line from the Arabic as the section_ja."""
    for line in arabic_text.splitlines():
        line = line.strip()
        # Skip page markers and empty lines
        if line.startswith("===") or not line:
            continue
        # Skip line-number prefixes (lone digits at start)
        line_clean = re.sub(r'^\d+\s+', '', line)
        if line_clean:
            return line_clean
    return ""


def parse_arabic(path: Path) -> list[dict]:
    """
    Parse merged-arabic.txt into pages.
    Format:
      === pNNN ===
      <Arabic text lines>
      === pNNN ===
      ...
    Returns list of {page_he: str, paragraphs: [str]} dicts.
    """
    pages = []
    current_page = None
    current_lines: list[str] = []

    def flush():
        if current_page is None:
            return
        # Join lines into paragraphs (blank line = paragraph break)
        paragraphs = []
        para_lines: list[str] = []
        for ln in current_lines:
            stripped = ln.strip()
            # Strip leading line numbers (e.g. "5 ", "10 " at start of line)
            stripped = re.sub(r'^\d+\s+', '', stripped)
            if not stripped:
                if para_lines:
                    paragraphs.append(' '.join(para_lines).strip())
                    para_lines = []
            else:
                para_lines.append(stripped)
        if para_lines:
            paragraphs.append(' '.join(para_lines).strip())
        paragraphs = [p for p in paragraphs if p]
        if paragraphs:
            pages.append({"page_he": str(current_page), "paragraphs": paragraphs})

    for raw in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r'^===\s*(p\d+)\s*===$', raw.strip())
        if m:
            flush()
            current_page = m.group(1)
            current_lines = []
        else:
            if current_page is not None:
                current_lines.append(raw)

    flush()
    return pages


def clean_md_paragraph(text: str) -> str:
    """Strip markdown formatting from a paragraph."""
    # Strip footnote refs [^N]
    text = re.sub(r'\[\^[\w\d]+\]', '', text)
    # Strip inline links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Strip bold/italic
    text = re.sub(r'\*{1,3}([^\*]+)\*{1,3}', r'\1', text)
    # Normalise whitespace
    text = ' '.join(text.split()).strip()
    return text


def parse_english_md(path: Path) -> list[str]:
    """Extract prose paragraphs from the English markdown."""
    paragraphs = []
    current: list[str] = []

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()

        # Skip H1, H2, H3 headers and blockquotes and --- dividers
        if line.startswith("# ") or line.startswith("## ") or line.startswith("### *"):
            continue
        if line.startswith("> "):
            continue
        if line == "---":
            if current:
                para = clean_md_paragraph(" ".join(current))
                if para:
                    paragraphs.append(para)
                current = []
            continue

        # ### lines: H3-italic subtitle → skip; section marker → keep as text
        if line.startswith("### "):
            content = line[4:].strip()
            if content.startswith("*"):
                continue
            if current:
                para = clean_md_paragraph(" ".join(current))
                if para:
                    paragraphs.append(para)
                current = []
            section_text = clean_md_paragraph(content)
            if section_text:
                paragraphs.append(section_text)
            continue

        # Skip standalone italic-only lines (translator notes like *Translated from...*)
        if line.startswith("*") and line.endswith("*") and not line.startswith("**"):
            continue

        if not line:
            if current:
                para = clean_md_paragraph(" ".join(current))
                if para:
                    paragraphs.append(para)
                current = []
        else:
            current.append(line)

    if current:
        para = clean_md_paragraph(" ".join(current))
        if para:
            paragraphs.append(para)

    return paragraphs


def main():
    # Find all maqala3-babN directories
    bab_dirs = sorted(
        d for d in OCR_ROOT.iterdir()
        if d.is_dir() and re.match(r'^maqala3-bab(\d+)$', d.name)
    )

    if not bab_dirs:
        print(f"ERROR: no maqala3-bab* dirs found under {OCR_ROOT}")
        return

    print(f"Found {len(bab_dirs)} M3 bab directories")

    for bab_dir in bab_dirs:
        m = re.match(r'^maqala3-bab(\d+)$', bab_dir.name)
        bab_n = int(m.group(1))
        nn = f"{bab_n:02d}"

        ar_path = bab_dir / "merged-arabic.txt"
        en_path = bab_dir / "english.md"

        if not ar_path.exists():
            print(f"  WARNING: no merged-arabic.txt in {bab_dir.name}, skipping")
            continue
        if not en_path.exists():
            print(f"  WARNING: no english.md in {bab_dir.name}, skipping")
            continue

        ar_raw = ar_path.read_text(encoding="utf-8")
        en_raw = en_path.read_text(encoding="utf-8")

        pages = parse_arabic(ar_path)
        en_paragraphs = parse_english_md(en_path)
        bab_title_en = extract_bab_title_en(en_raw)
        bab_title_ar = extract_bab_title_ar(ar_raw)

        section = f"Discourse III · Bab {bab_n}: {bab_title_en}" if bab_title_en else f"Discourse III · Bab {bab_n}"

        # Base file
        base = {
            "work": WORK,
            "section": section,
            "section_ja": bab_title_ar,
            "subtitle": SUBTITLE,
            "author": AUTHOR,
            "script": "arabic",
            "pages": pages,
        }
        base_path = OUT_DIR / f"qirqisani-m3-bab{nn}.json"
        base_path.write_text(json.dumps(base, ensure_ascii=False, indent=2), encoding="utf-8")

        # English file
        en_payload = {
            "translator": TRANSLATOR,
            "paragraphs": en_paragraphs,
        }
        en_path_out = OUT_DIR / f"qirqisani-m3-bab{nn}-english.json"
        en_path_out.write_text(json.dumps(en_payload, ensure_ascii=False, indent=2), encoding="utf-8")

        # Aligned stub
        aligned_stub = {"pages": {}}
        aligned_path = OUT_DIR / f"qirqisani-m3-bab{nn}-aligned.json"
        aligned_path.write_text(json.dumps(aligned_stub, ensure_ascii=False, indent=2), encoding="utf-8")

        print(f"  m3-bab{nn}: {len(pages)} pages, {len(en_paragraphs)} EN paras")

    print(f"\nDone — files written to {OUT_DIR}")


if __name__ == "__main__":
    main()

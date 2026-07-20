#!/usr/bin/env python3
"""Split the full Kuzari (Kitāb al-Khazarī) source into per-maqala Advanced-reader
gate JSON files.

Input  : data-source/kuzari/kuzari.json
         (FJMS resourceId 95, 228 pages; each page carries `cleanedText` and a
          `parentUnitNames[0]` naming its top-level unit.)
Output : data/kuzari-maqala-{1..5}.json — one file per maqala, minimal gate format:
           { work, section, section_ja, subtitle, author,
             pages: [ { page_he, paragraphs: [ "<joined JA text>" ] } ] }

The title page (page 3, parentUnitNames[0] = "המענה והראיה על אודות הדת המושפלה")
is folded into maqala-1, which already covers it as the book's opening.

Page-text join recipe: strip CR, split on LF, strip each line, drop blanks, join
with a single space — matches the Bahya gate recipe exactly.
"""

from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "data-source" / "kuzari" / "kuzari.json"
DATA = Path(__file__).resolve().parent.parent / "data"

WORK = "The Kuzari"
AUTHOR = "Yehuda HaLevi (d. 1141)"

# source parentUnitNames[0] → (slug, section label, section_ja, subtitle)
# The title page ("המענה…") is folded into maqala-1 via the TITLE_GROUP below.
TITLE_GROUP = "המענה והראיה על אודות הדת המושפלה"

MAQALOT: "OrderedDict[str, tuple[str, str, str, str]]" = OrderedDict([
    ("מאמר א", (
        "maqala-1",
        "Maqala I — The First Treatise",
        "מאמר א",
        "The dream, the Philosopher, the Christian, and the Muslim — until the Rabbi answers",
    )),
    ("מאמר ב", (
        "maqala-2",
        "Maqala II — The Second Treatise",
        "מאמר ב",
        "The Rabbi explains the foundations of Jewish faith and law",
    )),
    ("מאמר ג", (
        "maqala-3",
        "Maqala III — The Third Treatise",
        "מאמר ג",
        "Divine attributes, creation, prophecy, and the Hebrew language",
    )),
    ("מאמר ד", (
        "maqala-4",
        "Maqala IV — The Fourth Treatise",
        "מאמר ד",
        "The divine order, divine names, and the Kuzari's conversion",
    )),
    ("מאמר ה", (
        "maqala-5",
        "Maqala V — The Fifth Treatise",
        "מאמר ה",
        "Language, grammar, the Land of Israel, and the Kuzari's departure",
    )),
])


def join_page(cleaned: str) -> str:
    lines = cleaned.replace("\r", "").split("\n")
    return " ".join(l.strip() for l in lines if l.strip())


def build() -> None:
    src = json.loads(SRC.read_text())
    pages_all = src["pages"]

    # Group pages by parentUnitNames[0]; fold title page into maqala-1.
    by_maqala: "OrderedDict[str, list[dict]]" = OrderedDict()
    for key in MAQALOT:
        by_maqala[key] = []
    title_pages: list[dict] = []

    for p in pages_all:
        group = p["parentUnitNames"][0] if p["parentUnitNames"] else None
        if group == TITLE_GROUP:
            title_pages.append(p)
        elif group in by_maqala:
            by_maqala[group].append(p)
        else:
            raise SystemExit(f"Unexpected parentUnitNames[0]: {group!r}")

    # Prepend title pages to maqala-1.
    first_key = next(iter(by_maqala))
    by_maqala[first_key] = title_pages + by_maqala[first_key]

    total_pages = 0
    for group, (slug, section, section_ja, subtitle) in MAQALOT.items():
        pages_src = by_maqala[group]
        if not pages_src:
            raise SystemExit(f"No source pages for group {group!r}")

        work: dict = {
            "work": WORK,
            "section": section,
            "section_ja": section_ja,
            "subtitle": subtitle,
            "author": AUTHOR,
            "pages": [
                {"page_he": p["page"], "paragraphs": [join_page(p["cleanedText"])]}
                for p in pages_src
            ],
        }

        out = DATA / f"kuzari-{slug}.json"
        out.write_text(json.dumps(work, ensure_ascii=False, indent=2))
        print(f"  {slug:12} {len(pages_src):>3} pages  {pages_src[0]['page']}–{pages_src[-1]['page']}  → {out.name}")
        total_pages += len(pages_src)

    print(f"\n{len(MAQALOT)} maqalot, {total_pages} pages total.")


if __name__ == "__main__":
    build()

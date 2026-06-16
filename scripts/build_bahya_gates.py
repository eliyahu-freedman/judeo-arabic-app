#!/usr/bin/env python3
"""Split the full Bahya (Ḥovot ha-Levavot) source into per-gate Advanced-reader
WorkData JSON files.

Input  : ~/Downloads/genizah-research/bahya-hovot/bahya-hovot.json
         (FJMS resourceId 48, 421 pages; each page carries `cleanedText` and a
          `parentUnitNames[0]` naming its top-level gate.)
Output : data/bahya-<slug>.json — one file per gate, minimal WorkData shape:
           { work, section, section_ja, subtitle, author,
             pages: [ { page_he, paragraphs: [ "<joined JA text>" ] } ] }

The page-text join recipe (strip each source line, drop blanks, join with a
single space) reproduces the existing hand-built data/bahya-bab1.json
byte-for-byte, so generated gates match the established format exactly.

By default we write only the NEW gates (bab2…bab10). The hakdamah and bab1
already exist as hand-curated files (bab1 has paired english/aligned data) and
are left untouched — but we still build them in-memory and ASSERT they match the
on-disk files, so any silent drift in the source or recipe is caught.
"""

from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path

SRC = Path.home() / "Downloads" / "genizah-research" / "bahya-hovot" / "bahya-hovot.json"
DATA = Path(__file__).resolve().parent.parent / "data"

# Arabic gate name (parentUnitNames[0]) → (slug, section label, English subtitle).
# Subtitles render the gate's own "פתיחה פי …" topic line from the source.
GATES: "OrderedDict[str, tuple[str, str, str]]" = OrderedDict([
    ("הקדמה",          ("hakdamah", "Hakdamah",            "")),
    ("אלבאב אלאול",    ("bab1",  "Bab 1 — The First Gate",   "On the Purification of Affirming the Unity of the Creator")),
    ("אלבאב אלת'אני",  ("bab2",  "Bab 2 — The Second Gate",  "On Reflection upon Created Things and God's Abundant Grace toward Them")),
    ("אלבאב אלת'אלת'", ("bab3",  "Bab 3 — The Third Gate",   "On the Obligation to Submit to the Service of God")),
    ("אלבאב אלראבע",   ("bab4",  "Bab 4 — The Fourth Gate",  "On Trust in God Alone")),
    ("אלבאב אלכ'אמס",  ("bab5",  "Bab 5 — The Fifth Gate",   "On the Sincere Devotion of Action to God Alone")),
    ("אלבאב אלסאדס",   ("bab6",  "Bab 6 — The Sixth Gate",   "On Humility")),
    ("אלבאב אלסאבע",   ("bab7",  "Bab 7 — The Seventh Gate", "On Repentance — Its Aspects, Limits, and Attendant Matters")),
    ("אלבאב אלת'אמן",  ("bab8",  "Bab 8 — The Eighth Gate",  "On a Person's Spiritual Accounting before God")),
    ("אלבאב אלתאסע",   ("bab9",  "Bab 9 — The Ninth Gate",   "On the Forms of Abstinence from the World")),
    ("אלבאב אלעאשר",   ("bab10", "Bab 10 — The Tenth Gate",  "On the True Love of God")),
])

WORK = "Chovot HaLevavot"
AUTHOR = "Bahya ibn Paquda"
# Hand-curated files we must not clobber, but do verify against.
PROTECTED = {"hakdamah", "bab1"}


def join_page(cleaned: str) -> str:
    """Collapse a source page's `cleanedText` into one paragraph string.

    Matches the recipe used for the existing bahya-bab1.json: strip CRs, split on
    LF, strip each line, drop blanks, join with a single space.
    """
    lines = cleaned.replace("\r", "").split("\n")
    return " ".join(l.strip() for l in lines if l.strip())


def build() -> None:
    src = json.loads(SRC.read_text())
    by_gate: "OrderedDict[str, list[dict]]" = OrderedDict()
    for p in src["pages"]:
        gate = p["parentUnitNames"][0]
        by_gate.setdefault(gate, []).append(p)

    unknown = set(by_gate) - set(GATES)
    if unknown:
        raise SystemExit(f"Source has gate names not in GATES map: {unknown}")

    total_pages = 0
    for gate, (slug, section, subtitle) in GATES.items():
        pages_src = by_gate.get(gate)
        if not pages_src:
            raise SystemExit(f"No source pages for gate {gate!r}")
        section_ja = None if slug == "hakdamah" else gate
        work: dict = {
            "work": WORK,
            "section": section,
            "section_ja": section_ja,
            "subtitle": subtitle or None,
            "author": AUTHOR,
            "pages": [
                {"page_he": p["page"], "paragraphs": [join_page(p["cleanedText"])]}
                for p in pages_src
            ],
        }
        # Drop empty optional top-level fields for hakdamah parity.
        work = {k: v for k, v in work.items() if v is not None}

        out = DATA / f"bahya-{slug}.json"
        if slug in PROTECTED and out.exists():
            verify_protected(out, work, slug)
            print(f"  {slug:9} {len(pages_src):>3} pages  {pages_src[0]['page']}–{pages_src[-1]['page']}  [protected, verified]")
        else:
            out.write_text(json.dumps(work, ensure_ascii=False, indent=2))
            print(f"  {slug:9} {len(pages_src):>3} pages  {pages_src[0]['page']}–{pages_src[-1]['page']}  → {out.name}")
        total_pages += len(pages_src)

    print(f"\n{len(GATES)} gates, {total_pages} pages total.")


def verify_protected(path: Path, built: dict, slug: str) -> None:
    """Assert our generated pages match the existing hand-curated file's pages."""
    existing = json.loads(path.read_text())
    eb = [(p["page_he"], p["paragraphs"]) for p in existing["pages"]]
    nb = [(p["page_he"], p["paragraphs"]) for p in built["pages"]]
    if eb != nb:
        # Report the first divergence to make drift debuggable.
        for i, (a, b) in enumerate(zip(eb, nb)):
            if a != b:
                raise SystemExit(
                    f"{slug}: generated pages diverge from {path.name} at index {i} "
                    f"(page {a[0]!r} vs {b[0]!r})."
                )
        raise SystemExit(f"{slug}: page count differs ({len(eb)} on disk vs {len(nb)} built).")


if __name__ == "__main__":
    build()

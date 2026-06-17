"""Fetch Ibn Tibbon's vocalized Hebrew of Bab {N} from Sefaria.

Usage: fetch_bahya_bab1_hebrew.py [BAB]   (BAB defaults to 1)

Each gate on Sefaria comes in two pieces, e.g. for Bab 1:
  - "Duties of the Heart, First Treatise on Unity, Introduction" (Petiḥa)
  - "Duties of the Heart, First Treatise on Unity"                (chapters)

Combined into one flat list of paragraphs. Hebrew is no longer rendered in the
reader (reader.tsx: the `he` crib is "retained in data but no longer rendered");
it serves only as a reference candidate for the alignment-authoring bundles.
"""

from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

# Sefaria treatise title per bab (the "Duties of the Heart, <X>" base ref).
TREATISE = {
    1: "First Treatise on Unity",
    2: "Second Treatise on Examination",
    3: "Third Treatise on Service of God",
    4: "Fourth Treatise on Trust",
    5: "Fifth Treatise on Devotion",
    6: "Sixth Treatise on Submission",
    7: "Seventh Treatise on Repentance",
    8: "Eighth Treatise on Examining the Soul",
    9: "Ninth Treatise on Abstinence",
    10: "Tenth Treatise on Devotion to God",
}

BAB = int(sys.argv[1]) if len(sys.argv) > 1 else 1
SECTION = f"Bab {BAB} — The {['','First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth'][BAB]} Gate"

OUT = (
    Path(__file__).resolve().parent.parent
    / "data"
    / f"bahya-bab{BAB}-hebrew.json"
)


def strip_html(s: str) -> str:
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return s.strip()


def fetch(ref: str) -> object:
    url = f"https://www.sefaria.org/api/v3/texts/{urllib.parse.quote(ref)}"
    r = subprocess.run(
        ["curl", "-fsSL", "--max-time", "30", url],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(r.stdout)
    if data.get("error"):
        raise SystemExit(f"sefaria error for {ref}: {data['error']}")
    versions = data.get("versions", [])
    target = next(
        (v for v in versions if v.get("language") == "he"
         and "Vocalized" in v.get("versionTitle", "")), None,
    )
    if target is None:
        target = next((v for v in versions if v.get("language") == "he"), None)
    if target is None:
        raise SystemExit(f"no Hebrew version for {ref}")
    return target.get("text", [])


def flatten(text: object) -> list[str]:
    """Sefaria can return either flat list of paragraphs or list of
    lists (chapters → paragraphs). Flatten and clean."""
    out: list[str] = []
    if isinstance(text, list):
        for item in text:
            if isinstance(item, str):
                s = strip_html(item)
                if s:
                    out.append(s)
            elif isinstance(item, list):
                out.extend(flatten(item))
    return out


def main() -> int:
    base = f"Duties of the Heart, {TREATISE[BAB]}"
    petiha = flatten(fetch(f"{base}, Introduction"))
    chapters_raw = fetch(base)
    chapter_paragraphs: list[list[str]] = []
    if isinstance(chapters_raw, list):
        for ch in chapters_raw:
            chapter_paragraphs.append(flatten(ch))
    paragraphs: list[str] = list(petiha)
    for ch in chapter_paragraphs:
        paragraphs.extend(ch)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "work": "Chovot HaLevavot",
                "section": SECTION,
                "translator": "Yehuda Ibn Tibbon",
                "version": "Vocalized Edition (Sefaria)",
                "petiha_paragraph_count": len(petiha),
                "chapter_paragraph_counts": [len(ch) for ch in chapter_paragraphs],
                "paragraphs": paragraphs,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {len(paragraphs)} total paragraphs "
          f"(petiḥa: {len(petiha)}, "
          f"chapters: {[len(c) for c in chapter_paragraphs]}) "
          f"to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

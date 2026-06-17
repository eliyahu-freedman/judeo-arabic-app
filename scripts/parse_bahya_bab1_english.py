"""Parse Eli's bab{N}.md (English translation) into JSON paragraphs.

Usage: parse_bahya_bab1_english.py [BAB]   (BAB defaults to 1)

Strategy:
  - Read the markdown.
  - Drop everything from "## Notes" onward (footnote definitions).
  - Strip superscript footnote markers (¹²³…) wherever they appear.
  - Skip lines starting with `#` (headers).
  - Treat blank lines as paragraph separators.

Output: { "paragraphs": ["...", ...] } at data/bahya-bab{N}-english.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BAB = int(sys.argv[1]) if len(sys.argv) > 1 else 1

SRC = (
    Path.home()
    / "Downloads"
    / "genizah-research"
    / "bahya-hovot"
    / "edition"
    / "translation"
    / f"bab{BAB}.md"
)
OUT = (
    Path(__file__).resolve().parent.parent
    / "data"
    / f"bahya-bab{BAB}-english.json"
)

# Unicode superscript digits used as footnote markers.
SUPERS_RE = re.compile(r"[⁰¹²³⁴-⁹]+")


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    # Cut off the notes section. Bab 1 heads it "## Notes"; bab 2 uses
    # "## Footnotes — Bab 2". Match any header whose text starts Notes/Footnotes.
    m = re.search(r"\n#+\s*(?:Notes|Footnotes)\b", text)
    if m:
        text = text[: m.start()]
    # Strip superscript markers, then split on blank lines.
    text = SUPERS_RE.sub("", text)
    paragraphs: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        # Drop markdown headers and bare "---" horizontal-rule separators.
        keep_lines = [
            line
            for line in block.splitlines()
            if not line.lstrip().startswith("#") and line.strip() != "---"
        ]
        joined = " ".join(l.strip() for l in keep_lines if l.strip())
        if joined:
            paragraphs.append(joined)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "source_file": str(SRC),
                "translator": "Eliyahu Freedman (working draft)",
                "paragraphs": paragraphs,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {len(paragraphs)} paragraphs to {OUT}")


if __name__ == "__main__":
    main()

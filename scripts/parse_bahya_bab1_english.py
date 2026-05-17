"""Parse Eli's bab1.md (English translation) into JSON paragraphs.

Strategy:
  - Read the markdown.
  - Drop everything from "## Notes" onward (footnote definitions).
  - Strip superscript footnote markers (¹²³…) wherever they appear.
  - Skip lines starting with `#` (headers).
  - Treat blank lines as paragraph separators.

Output: { "paragraphs": ["...", ...] }
"""

from __future__ import annotations

import json
import re
from pathlib import Path

SRC = (
    Path.home()
    / "Downloads"
    / "genizah-research"
    / "bahya-hovot"
    / "edition"
    / "translation"
    / "bab1.md"
)
OUT = (
    Path(__file__).resolve().parent.parent / "data" / "bahya-bab1-english.json"
)

# Unicode superscript digits used as footnote markers.
SUPERS_RE = re.compile(r"[⁰¹²³⁴-⁹]+")


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    # Cut off the Notes section.
    cutoff = text.find("\n## Notes")
    if cutoff != -1:
        text = text[:cutoff]
    # Strip superscript markers, then split on blank lines.
    text = SUPERS_RE.sub("", text)
    paragraphs: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        # Drop lines that are markdown headers.
        keep_lines = [
            line for line in block.splitlines() if not line.lstrip().startswith("#")
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

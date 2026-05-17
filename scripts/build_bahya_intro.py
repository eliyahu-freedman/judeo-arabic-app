"""Extract Bahya's hakdamah from the FJMS scrape into structured JSON.

Source: ~/Downloads/genizah-research/bahya-hovot/bahya-hovot.txt
The scrape has `[עמוד: <page>]  [<section>]` page headers followed by
plain JA text with manual line breaks every ~60 chars. We:

  1. Walk through the file, splitting on page headers.
  2. Take only pages where the section is [הקדמה].
  3. Join hard-wrapped lines back into paragraphs (blank lines mark
     paragraph boundaries within a page).

Output schema: {pages: [{page_he: "יג", paragraphs: [str, ...]}, ...]}
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SOURCE = (
    Path.home()
    / "Downloads"
    / "genizah-research"
    / "bahya-hovot"
    / "bahya-hovot.txt"
)
OUT = (
    Path(__file__).resolve().parent.parent / "data" / "bahya-hakdamah.json"
)

PAGE_RE = re.compile(r"^\[עמוד:\s*([^\]]+)\]\s*\[([^\]]+)\]\s*$")


def parse(path: Path) -> list[dict]:
    pages: list[dict] = []
    current_page: str | None = None
    current_section: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        if current_page is None or current_section != "הקדמה":
            return
        # Join hard-wrapped lines into paragraphs.
        paragraphs: list[str] = []
        buf: list[str] = []
        for line in current_lines:
            if line.strip() == "":
                if buf:
                    paragraphs.append(" ".join(buf).strip())
                    buf = []
            else:
                buf.append(line.strip())
        if buf:
            paragraphs.append(" ".join(buf).strip())
        paragraphs = [p for p in paragraphs if p]
        if paragraphs:
            pages.append({"page_he": current_page, "paragraphs": paragraphs})

    with path.open(encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            m = PAGE_RE.match(line.strip())
            if m:
                flush()
                current_page = m.group(1).strip()
                current_section = m.group(2).strip()
                current_lines = []
            else:
                current_lines.append(line)
        flush()

    return pages


def main() -> int:
    if not SOURCE.exists():
        print(f"missing source: {SOURCE}", file=sys.stderr)
        return 1
    pages = parse(SOURCE)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "work": "Chovot HaLevavot",
                "section": "Hakdamah",
                "author": "Bahya ibn Paquda",
                "pages": pages,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    para_count = sum(len(p["paragraphs"]) for p in pages)
    print(f"wrote {len(pages)} pages ({para_count} paragraphs) to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

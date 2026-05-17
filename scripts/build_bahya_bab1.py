"""Extract Bahya's bab 1 from the FJMS scrape into structured JSON.

Same shape as build_bahya_intro.py but filters for [אלבאב אלאול].
Bab 1 spans pages מד–צג, ~50 source pages.
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
OUT = Path(__file__).resolve().parent.parent / "data" / "bahya-bab1.json"

PAGE_RE = re.compile(r"^\[עמוד:\s*([^\]]+)\]\s*\[([^\]]+)\]\s*$")
TARGET_SECTION = "אלבאב אלאול"


def parse(path: Path) -> list[dict]:
    pages: list[dict] = []
    current_page: str | None = None
    current_section: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        if current_page is None or current_section != TARGET_SECTION:
            return
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
                "section": "Bab 1 — The First Gate",
                "section_ja": "אלבאב אלאול",
                "subtitle": "On the Purification of Affirming the Unity of the Creator",
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

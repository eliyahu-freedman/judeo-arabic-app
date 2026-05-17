"""Fetch Ibn Tibbon's vocalized Hebrew of Bahya's hakdamah from Sefaria.

Sefaria's catalog ref: 'Duties of the Heart, Introduction of the Author'.
Returns 128 paragraphs (Vocalized Edition). We strip Sefaria's inline
HTML tags and save as JSON for use by the advanced reader.
"""

from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

API = (
    "https://www.sefaria.org/api/v3/texts/"
    + urllib.parse.quote("Duties of the Heart, Introduction of the Author")
)
OUT = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "bahya-hakdamah-hebrew.json"
)


def strip_html(s: str) -> str:
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return s.strip()


def fetch() -> list[str]:
    # urllib's SSL handling on brew Python is flaky; curl is simpler.
    result = subprocess.run(
        ["curl", "-fsSL", "--max-time", "30", API],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(result.stdout)
    if data.get("error"):
        raise SystemExit(f"sefaria error: {data['error']}")
    versions = data.get("versions", [])
    target = next(
        (
            v
            for v in versions
            if v.get("language") == "he"
            and "Vocalized" in v.get("versionTitle", "")
        ),
        None,
    )
    if target is None and versions:
        target = next((v for v in versions if v.get("language") == "he"), None)
    if target is None:
        raise SystemExit("no Hebrew version returned")
    text = target.get("text", [])
    if not isinstance(text, list):
        raise SystemExit("unexpected text shape")
    return [strip_html(s) for s in text if s.strip()]


def main() -> int:
    paragraphs = fetch()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "work": "Chovot HaLevavot",
                "section": "Hakdamah",
                "author": "Bahya ibn Paquda",
                "translator": "Yehuda Ibn Tibbon",
                "version": "Vocalized Edition (Sefaria)",
                "source": "https://www.sefaria.org/Duties_of_the_Heart,_Introduction_of_the_Author",
                "paragraphs": paragraphs,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {len(paragraphs)} paragraphs to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

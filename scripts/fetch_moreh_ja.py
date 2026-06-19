#!/usr/bin/env python3
"""Fetch the Judeo-Arabic original of Guide Part I (ch. 29-36) from the Sefaria
API → data/moreh-ja-jrb.json, as the source text for authoring moreh-bab{N}.json.

The on-disk FJMS source (resourceId 6) only covers I:1-28. Sefaria hosts the full
Guide in Judeo-Arabic — version "Judeo Arabic, Paris, 1856 [jrb]" (the 1856
Paris/Munk Arabic base, public-domain by age; Sefaria tags the licence "unknown").
This is a *reference* scratch file — it does NOT overwrite the hand-authored
moreh-bab*.json. Uses curl (the system Python here lacks SSL roots).

Run:  python3 scripts/fetch_moreh_ja.py
"""
import json, re, subprocess, time, urllib.parse
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
VERSION = "Judeo Arabic, Paris, 1856 [jrb]"
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def clean(s: str) -> str:
    return WS.sub(" ", TAG.sub(" ", s)).strip()


def fetch(n: int) -> list[str]:
    ref = f"Guide_for_the_Perplexed, Part 1.{n}"
    url = (
        "https://www.sefaria.org/api/texts/"
        + urllib.parse.quote(ref)
        + "?context=0&commentary=0&vhe="
        + urllib.parse.quote(VERSION)
    )
    out = subprocess.run(
        ["curl", "-sS", "-A", "Mozilla/5.0", url], capture_output=True, text=True
    ).stdout
    d = json.loads(out)
    he = d.get("he") or []
    if d.get("heVersionTitle") != VERSION:
        raise SystemExit(f"ch{n}: unexpected version {d.get('heVersionTitle')!r}")
    return [clean(s) for s in he if clean(s)]


def main():
    chapters = {}
    for n in range(29, 37):
        segs = fetch(n)
        chapters[str(n)] = segs
        print(f"ch{n}: {len(segs)} segments")
        time.sleep(0.4)
    doc = {
        "_note": "Judeo-Arabic original of Guide Part I, ch. 29-36, fetched as the "
                 "source text for authoring the reader's moreh-bab{N}.json. HTML stripped.",
        "_source": "Sefaria (https://www.sefaria.org), API",
        "_versionTitle": VERSION,
        "_license": "unknown (Sefaria tag); public-domain by age (1856 Paris base)",
        "chapters": chapters,
    }
    path = DATA / "moreh-ja-jrb.json"
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path}: {len(chapters)} chapters")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Fetch the public-domain Ibn Tibbon Hebrew of Guide Part I (ch. 1-28) from the
Sefaria API → data/moreh-tibbon.json, for the Arabic ⇄ Ibn Tibbon parallel view.

Ibn Tibbon's medieval Hebrew translation is public domain; we fetch it from
Sefaria ("Moreh Nevuchim, translated by Ibn Tibon", Public Domain). Uses curl
(the system Python here lacks SSL roots). Polite serial fetch with a short pause.

Run:  python3 scripts/fetch_moreh_tibbon.py
"""
import json, re, subprocess, time, urllib.parse
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
VERSION = "Moreh Nevuchim, translated by Ibn Tibon"
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
    for n in range(1, 29):
        segs = fetch(n)
        chapters[str(n)] = segs
        print(f"ch{n}: {len(segs)} segments")
        time.sleep(0.4)
    doc = {
        "_note": "Ibn Tibbon's medieval Hebrew translation of Guide Part I, ch. 1-28, "
                 "for the Arabic-vs-translation parallel view. HTML stripped.",
        "_source": "Sefaria (https://www.sefaria.org), API",
        "_versionTitle": VERSION,
        "_license": "Public Domain",
        "chapters": chapters,
    }
    path = DATA / "moreh-tibbon.json"
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path}: {len(chapters)} chapters")


if __name__ == "__main__":
    main()

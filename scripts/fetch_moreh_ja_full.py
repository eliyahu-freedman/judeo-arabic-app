#!/usr/bin/env python3
"""Fetch Judeo-Arabic source for the full Moreh Nevukhim from Sefaria jrb.

Produces three scratch reference files — NEVER overwrite the hand-authored
moreh-bab*.json. Run once at the start of a new authoring session.

  data/moreh-ja-p1-37-76.json  — Part I remaining (ch 37–76)
  data/moreh-ja-p2.json        — Part II (ch 1–48)
  data/moreh-ja-p3.json        — Part III (ch 1–54)

Version: "Judeo Arabic, Paris, 1856 [jrb]" (public-domain by age).
Uses curl because system Python may lack SSL roots.
"""
import json, re, subprocess, time, urllib.parse
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
VERSION = "Judeo Arabic, Paris, 1856 [jrb]"
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")

PARTS = [
    # (part_number, start_ch, end_ch_inclusive, output_stem)
    (1, 37, 76, "moreh-ja-p1-37-76"),
    (2,  1, 48, "moreh-ja-p2"),
    (3,  1, 54, "moreh-ja-p3"),
]


def clean(s: str) -> str:
    return WS.sub(" ", TAG.sub(" ", s)).strip()


def fetch(part: int, n: int) -> list[str]:
    ref = f"Guide_for_the_Perplexed, Part {part}.{n}"
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
    vtitle = d.get("heVersionTitle", "")
    if vtitle != VERSION:
        raise SystemExit(f"P{part}:{n}: unexpected version {vtitle!r}")
    he = d.get("he") or []
    return [clean(s) for s in he if clean(s)]


def main():
    for part, start, end, stem in PARTS:
        chapters: dict[str, list[str]] = {}
        for n in range(start, end + 1):
            segs = fetch(part, n)
            chapters[str(n)] = segs
            print(f"P{part}:{n}: {len(segs)} segments")
            time.sleep(0.35)
        doc = {
            "_note": f"Judeo-Arabic original of Guide Part {part}, ch {start}–{end}. "
                     "HTML stripped. Scratch reference — do NOT overwrite moreh-bab*.json.",
            "_source": "Sefaria (https://www.sefaria.org), API",
            "_versionTitle": VERSION,
            "_license": "unknown (Sefaria tag); public-domain by age (1856 Paris base)",
            "part": part,
            "chapters": chapters,
        }
        path = DATA / f"{stem}.json"
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {path} ({len(chapters)} chapters)\n")


if __name__ == "__main__":
    main()

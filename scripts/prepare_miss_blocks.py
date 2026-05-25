"""Split data/coverage-misses.json into per-block files for parallel authoring.

Each block file (data/_misses_block_NN.json) carries, per miss surface:
  - surface, count, bucket
  - up to 3 example contexts: {book, ch, v, ja} pulled from the real Tafsir JSONs

A Sonnet subagent then authors one block: for each surface it queries the local
lexicon CLI itself (it can infer the root, e.g. ולדת -> ولد), grounds the gloss
in a retrieved Lane/Lisan/Blau entry, and writes data/_lane_frag_NN.json.

Run:  python3 scripts/prepare_miss_blocks.py --blocks 8
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TOKEN_RE = re.compile(r"[א-ת']+")


def strip_punct(s: str) -> str:
    return re.sub(r'^[.,:;؛،"\'\s]+|[.,:;؛،"\'\s]+$', "", s)


def normalize(t: str) -> str:
    t = strip_punct(t)
    if t.startswith("ו") and len(t) > 1:
        t = t[1:]
    if t.startswith("אל") and len(t) > 2:
        t = t[2:]
    return t


def build_context_index() -> dict[str, list[dict]]:
    idx: dict[str, list[dict]] = collections.defaultdict(list)
    for fp in sorted(DATA.glob("tafsir-*-*.json")):
        if "-english" in fp.name or "-alignment" in fp.name:
            continue
        m = re.match(r"tafsir-([a-z]+)-(\d+)\.json$", fp.name)
        if not m:
            continue
        book = m.group(1)
        try:
            d = json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            continue
        for v in d.get("verses", []):
            text = v.get("ja", "") or ""
            vnum = v.get("v")
            ch = v.get("ch", int(m.group(2)))
            seen_here = set()
            for tok in TOKEN_RE.findall(text):
                n = normalize(tok)
                if not n or n in seen_here:
                    continue
                seen_here.add(n)
                if len(idx[n]) < 3:
                    short = text if len(text) <= 160 else text[:160] + "…"
                    idx[n].append({"book": book, "ch": ch, "v": vnum, "ja": short})
    return idx


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--blocks", type=int, default=8)
    args = ap.parse_args()

    queue = json.loads((DATA / "coverage-misses.json").read_text(encoding="utf-8"))["queue"]
    ctx = build_context_index()
    for item in queue:
        item["contexts"] = ctx.get(normalize(item["surface"]), [])

    # Drop pure ocr-junk from authoring (kept in the queue file as residual).
    authorable = [q for q in queue if q["bucket"] != "ocr-junk"]
    n = args.blocks
    blocks = [authorable[i::n] for i in range(n)]  # round-robin keeps freq spread even
    for i, b in enumerate(blocks):
        p = DATA / f"_misses_block_{i:02d}.json"
        p.write_text(json.dumps({"block": i, "surfaces": b}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {p.name}: {len(b)} surfaces")
    print(f"\ntotal authorable: {len(authorable)} (ocr-junk skipped: {len(queue) - len(authorable)})")


if __name__ == "__main__":
    main()

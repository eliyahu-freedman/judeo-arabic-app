"""Merge authored _lane_frag_*.json fragments into data/dictionary-lane.json.

- Assigns unique ids (suffixing on collision).
- Normalizes source "lisan" -> "lane" (no lisan badge exists; both are standard
  classical Arabic; the precise dict stays recorded in `_grounding`).
- Keeps source "blau" and absent-source (proper nouns) as-is.
- Skips exact duplicates (same lemma_ja + gloss_en already present).

Run:  python3 scripts/merge_lane_frags.py data/_lane_frag_00.json data/_lane_frag_01.json data/_lane_frag_04.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANE = ROOT / "data" / "dictionary-lane.json"


def main(frag_paths: list[str]) -> None:
    lane = json.loads(LANE.read_text(encoding="utf-8"))
    ids = {e["id"] for e in lane["entries"]}
    existing = {(e["lemma_ja"], e.get("gloss_en")) for e in lane["entries"]}

    added = 0
    skipped = 0
    src_norm = 0
    for fp in frag_paths:
        d = json.loads(Path(fp).read_text(encoding="utf-8"))
        for e in d.get("entries", []):
            if not e.get("id") or not e.get("lemma_ja"):
                continue
            if e.get("source") == "lisan":
                e["source"] = "lane"
                src_norm += 1
            key = (e["lemma_ja"], e.get("gloss_en"))
            if key in existing:
                skipped += 1
                continue
            base = e["id"]
            n = 1
            while e["id"] in ids:
                n += 1
                e["id"] = f"{base}_{n}"
            ids.add(e["id"])
            existing.add(key)
            lane["entries"].append(e)
            added += 1

    LANE.write_text(json.dumps(lane, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"merged: +{added} entries (skipped {skipped} dups, normalized {src_norm} lisan->lane)")
    print(f"dictionary-lane.json now has {len(lane['entries'])} entries")


if __name__ == "__main__":
    main(sys.argv[1:])

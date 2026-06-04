#!/usr/bin/env python3
"""
One-shot: stamp tier='twist' on every existing entry in tafsir-divergence.json.

The DivergenceEntry type defaults `tier` to 'twist' when omitted, so this
doesn't change app behavior — but stamping makes the data file self-documenting
once mixed-tier entries (note, gloss) land, so curators don't have to remember
the default.

Run once after the schema change; idempotent (skips entries that already
carry a tier).

Run from repo root:
  python3 scripts/stamp_tier_twist.py
"""

from __future__ import annotations

import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parent.parent / "data" / "tafsir-divergence.json"


def main() -> int:
    payload = json.loads(DATA.read_text())
    entries = payload.get("entries", [])
    stamped = 0
    for e in entries:
        if "tier" not in e:
            # Insert tier near the top of the entry for readability — after
            # lemma fields so the data flows lemma → tier → semantics.
            new = {}
            inserted = False
            for k, v in e.items():
                new[k] = v
                if not inserted and k == "root":
                    new["tier"] = "twist"
                    inserted = True
            if not inserted:
                new["tier"] = "twist"
            e.clear()
            e.update(new)
            stamped += 1

    DATA.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(f"stamped tier='twist' on {stamped}/{len(entries)} entries in {DATA.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

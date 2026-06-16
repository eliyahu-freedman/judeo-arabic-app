#!/usr/bin/env python3
"""
Stage the Advanced-reader coverage misses into a lemma-grouped worklist.

Reads `data/coverage-advanced.json` (produced by coverage_advanced.py), takes
the miss surfaces for the in-scope texts, groups them by their maximal
prefix-stripped + final-normalized reduction (mirroring lib/lookup.ts), and
attaches the Arabic-script transliteration of each group key via the
arabic-lexicon toolkit's `ja_script.ja_to_ar`.

Output `data/_advanced_misses_grouped.json` is the hand-authoring worklist:
one row per lemma-candidate, with every observed surface form (so they can be
folded in as `variants`), occurrence counts, and the Arabic form to look up in
Lane/Blau. Authoring then happens against this file; nothing here ships.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from coverage_report import DATA, candidate_chain, normalize_finals  # noqa: E402

# arabic-lexicon toolkit (for ja_to_ar).
LEX = Path.home() / "Tools" / "arabic-lexicon"
sys.path.insert(0, str(LEX))
import ja_script  # noqa: E402

IN_SCOPE = ["moreh-bab1", "kuzari-maqala1", "saadia-emunot-intro", "qirqisani-anwar",
            "bahya-bab1", "bahya-hakdamah",
            "bahya-bab2", "bahya-bab3", "bahya-bab4", "bahya-bab5", "bahya-bab6",
            "bahya-bab7", "bahya-bab8", "bahya-bab9", "bahya-bab10"]


def reduce_key(surface: str) -> str:
    """Maximal reduction: the shortest candidate the lookup chain produces,
    final-normalized. This is the best single lemma-grouping key — surfaces
    that differ only by ו / ב ל כ פ / אל prefixes collapse together."""
    cands = candidate_chain(surface)
    if not cands:
        return normalize_finals(surface)
    # Prefer the shortest (most-stripped) candidate as the canonical stem.
    return min((normalize_finals(c) for c in cands), key=len)


def main() -> int:
    cov = json.loads((DATA / "coverage-advanced.json").read_text())["by_text"]

    # surface -> (total count, set of texts it appears in)
    surf_count: dict[str, int] = defaultdict(int)
    surf_texts: dict[str, set[str]] = defaultdict(set)
    for label in IN_SCOPE:
        for m in cov[label]["misses"]:
            surf_count[m["surface"]] += m["count"]
            surf_texts[m["surface"]].add(label)

    # Group surfaces by reduced key.
    groups: dict[str, list[str]] = defaultdict(list)
    for surf in surf_count:
        groups[reduce_key(surf)].append(surf)

    rows = []
    for key, surfaces in groups.items():
        surfaces_sorted = sorted(surfaces, key=lambda s: -surf_count[s])
        total = sum(surf_count[s] for s in surfaces)
        texts = sorted(set().union(*(surf_texts[s] for s in surfaces)))
        rows.append(
            {
                "key": key,
                "ar": ja_script.ja_to_ar(key),
                "count": total,
                "texts": texts,
                "surfaces": surfaces_sorted,
            }
        )
    rows.sort(key=lambda r: -r["count"])

    out = {
        "_generated": "scripts/stage_advanced_misses.py",
        "_lemma_groups": len(rows),
        "_surface_forms": len(surf_count),
        "groups": rows,
    }
    out_path = DATA / "_advanced_misses_grouped.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"{len(rows)} lemma groups from {len(surf_count)} surface forms")
    print(f"Wrote {out_path}")
    # Preview the top 30.
    for r in rows[:30]:
        print(f"  {r['count']:>3}  {r['key']:12} {r['ar']:12} <- {' '.join(r['surfaces'][:6])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

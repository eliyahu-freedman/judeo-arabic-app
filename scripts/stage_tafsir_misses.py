#!/usr/bin/env python3
"""
Stage Tafsir coverage misses into the SAME lemma-grouped worklist format the
Advanced-reader pipeline uses (`data/_advanced_misses_grouped.json`), so the
existing `autopatch_advanced_misses.py` + `apply_dict_advanced.py` +
`bahya_coverage_workflow.js` machinery can be reused verbatim for the Tafsir.

Sources the running JA (`ja` fields) from `data/tafsir-{book}-*.json` for one
book (default: devarim), finds tokens not covered by starter+lane via the exact
runtime candidate chain, groups by maximal prefix-stripped reduction, and
attaches the back-converted Arabic for Lane lookups.

Usage: python3 scripts/stage_tafsir_misses.py [book]
"""
from __future__ import annotations

import glob
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from coverage_report import (  # noqa: E402
    DATA, candidate_chain, normalize_finals, strip_punct,
    load_dict_index, tokenise_via_cli, chunked,
)

LEX = Path.home() / "Tools" / "arabic-lexicon"
sys.path.insert(0, str(LEX))
import ja_script  # noqa: E402


def reduce_key(surface: str) -> str:
    cands = candidate_chain(surface)
    if not cands:
        return normalize_finals(surface)
    return min((normalize_finals(c) for c in cands), key=len)


def main() -> int:
    book = sys.argv[1] if len(sys.argv) > 1 else "devarim"
    starter_keys, _ = load_dict_index(DATA / "dictionary-starter.json")
    lane_keys, _ = load_dict_index(DATA / "dictionary-lane.json")
    hand = starter_keys | lane_keys

    pat = "tafsir-*.json" if book == "all" else f"tafsir-{book}-*.json"
    files = [p for p in sorted(glob.glob(str(DATA / pat)))
             if not any(x in p for x in ("-english", "-alignment", "-divergence"))]
    strings: list[str] = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "ja" and isinstance(v, str):
                    strings.append(v)
                else:
                    walk(v)
        elif isinstance(o, list):
            for x in o:
                walk(x)

    for fp in files:
        walk(json.loads(Path(fp).read_text()))

    def covered(raw: str) -> bool:
        return any(c in hand for c in candidate_chain(raw))

    surf_count: dict[str, int] = defaultdict(int)
    for chunk in chunked(strings, 64):
        for words in tokenise_via_cli(chunk):
            for w in words:
                jw = re.sub(r"[֑-ׇ]", "", w)
                tok = strip_punct(jw)
                if not tok or covered(jw):
                    continue
                surf_count[tok] += 1

    groups: dict[str, list[str]] = defaultdict(list)
    for surf in surf_count:
        groups[reduce_key(surf)].append(surf)

    rows = []
    for key, surfaces in groups.items():
        surfaces_sorted = sorted(surfaces, key=lambda s: -surf_count[s])
        total = sum(surf_count[s] for s in surfaces)
        rows.append({
            "key": key,
            "ar": ja_script.ja_to_ar(key),
            "count": total,
            "texts": [f"tafsir-{book}"],
            "surfaces": surfaces_sorted,
        })
    rows.sort(key=lambda r: -r["count"])

    out = {
        "_generated": f"scripts/stage_tafsir_misses.py ({book})",
        "_lemma_groups": len(rows),
        "_surface_forms": len(surf_count),
        "groups": rows,
    }
    out_path = DATA / "_advanced_misses_grouped.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"[{book}] {len(rows)} lemma groups from {len(surf_count)} surface forms")
    print(f"Wrote {out_path}")
    for r in rows[:15]:
        print(f"  {r['count']:>3}  {r['key']:12} {r['ar']:12} <- {' '.join(r['surfaces'][:5])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

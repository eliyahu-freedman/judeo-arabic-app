#!/usr/bin/env python3
"""
Auto-patch Advanced-reader miss surfaces onto existing dictionary stems.

The runtime lookup chain (lib/lookup.ts) strips leading prefixes (ו / ב ל כ פ /
אל) but NOT pronominal / inflectional SUFFIXES. So a large share of the Bahya
"misses" are simply suffixed forms of a stem that already has an entry in
starter/lane. This script finds those and emits a patch ({entry_id: [surface…]})
plus a residual worklist of surfaces that need genuine hand-authoring.

For each miss surface we take every prefix-stripped candidate (the exact runtime
chain), then peel one inflectional suffix at a time, normalize finals, and look
the stem up in a {normalized lemma/variant -> entry_id} index built from
starter + lane. The LONGEST surviving stem match wins (most specific), and we
require the stem to be >= MIN_STEM letters to avoid spurious short collisions.

Output:
  data/_dict_advanced_patch.json        merged patch (id -> [surfaces])  [WRITTEN]
  data/_advanced_misses_residual.json   groups with >=1 unmatched surface [WRITTEN]

Nothing here ships until apply_dict_advanced.py is run.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from coverage_report import DATA, candidate_chain, normalize_finals  # noqa: E402

# Pronominal / inflectional suffixes, longest first so we peel maximally.
# (Judaeo-Arabic object/possessive enclitics + a few nominal/verbal endings.)
SUFFIXES = [
    "המא", "כמא", "תמא",
    "הם", "הן", "הא", "כם", "כן", "נא", "ני", "הו",
    "ון", "ין", "אן", "את", "ות",
    # Single-letter enclitics only — ו/י/ת/ן/א are too often radicals to strip.
    "ה", "ך", "כ",
]
MIN_STEM = 3  # don't match a stem shorter than this (avoid junk collisions)


def build_index() -> dict[str, str]:
    """normalized lemma/variant surface -> entry id (first writer wins)."""
    idx: dict[str, str] = {}
    for fname in ("dictionary-starter.json", "dictionary-lane.json"):
        d = json.loads((DATA / fname).read_text())
        for e in d.get("entries", []):
            eid = e.get("id")
            if not eid:
                continue
            keys = [e.get("lemma_ja")] + list(e.get("variants", []) or [])
            for k in keys:
                if k:
                    idx.setdefault(normalize_finals(k), eid)
    return idx


def match_surface(surface: str, idx: dict[str, str]) -> str | None:
    """Return the entry id of the longest stem match for a suffixed surface."""
    best_id: str | None = None
    best_len = -1
    for cand in candidate_chain(surface):
        c = normalize_finals(cand)
        # Direct hit shouldn't happen (it's a miss) but guard anyway.
        if c in idx and len(c) > best_len:
            best_id, best_len = idx[c], len(c)
        for suf in SUFFIXES:
            if c.endswith(suf):
                stem = c[: -len(suf)]
                if len(stem) >= MIN_STEM and stem in idx and len(stem) > best_len:
                    best_id, best_len = idx[stem], len(stem)
    return best_id


def main() -> int:
    idx = build_index()
    grouped = json.loads((DATA / "_advanced_misses_grouped.json").read_text())

    patch: dict[str, list[str]] = defaultdict(list)
    matched = 0
    residual_groups = []
    for g in grouped["groups"]:
        unmatched = []
        for surf in g["surfaces"]:
            eid = match_surface(surf, idx)
            if eid:
                patch[eid].append(surf)
                matched += 1
            else:
                unmatched.append(surf)
        if unmatched:
            residual_groups.append({**g, "surfaces": unmatched})

    # Merge into existing patch file (preserve any hand-authored entries).
    patch_path = DATA / "_dict_advanced_patch.json"
    existing = json.loads(patch_path.read_text()) if patch_path.exists() else {}
    for eid, surfs in patch.items():
        merged = list(dict.fromkeys((existing.get(eid, []) or []) + surfs))
        existing[eid] = merged
    patch_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2) + "\n")

    residual = {
        "_generated": "scripts/autopatch_advanced_misses.py",
        "_residual_groups": len(residual_groups),
        "_residual_surfaces": sum(len(g["surfaces"]) for g in residual_groups),
        "groups": residual_groups,
    }
    res_path = DATA / "_advanced_misses_residual.json"
    res_path.write_text(json.dumps(residual, ensure_ascii=False, indent=2))

    total_surf = sum(len(g["surfaces"]) for g in grouped["groups"])
    print(f"surfaces: {total_surf}  auto-patched: {matched}  "
          f"residual: {residual['_residual_surfaces']} "
          f"({residual['_residual_groups']} groups)")
    print(f"patch entries touched: {len(patch)}")
    print(f"Wrote {patch_path}\nWrote {res_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

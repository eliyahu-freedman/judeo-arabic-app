#!/usr/bin/env python3
"""
Apply inflected-lemma corrections to dictionary-lane.json IN PLACE, by id.

Why in-place (not the apply_dict_advanced.py append/fold path): that path FOLDS a
new entry's surfaces into whichever existing entry already owns the surface — the
very mechanism that created this bug (a clean base entry folds into the suffixed
entry that already claims the base form as a variant). Here we instead OVERWRITE
the flagged entry's own fields by id, so the headword moves to the base citation
form while the entry keeps its identity.

Input  : data/_inflected_fixes.json — list of fix objects:
           {id, action: "rekey"|"keep",
            lemma_ja, lemma_ar, root, pos, gloss_en, gloss_he, variants}
         Only "rekey" objects mutate; "keep" is a no-op (recorded for the count).

Coverage guard: the corrected entry's key set (norm(lemma_ja) ∪ {norm(variant)})
MUST be a superset of the entry's ORIGINAL key set. Any surface the agent dropped
is re-added to variants, so a token that was covered before stays covered.

Merge: after rewriting, entries that now share (norm(lemma_ja), root) — with a
real (non "—") root — are collapsed into the earliest one, unioning variants.

Write-back: json.dumps(..., ensure_ascii=False, indent=2) + "\\n", then re-parse.
Run from repo root:  python3 scripts/apply_inflected_fixes.py
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# fields a rekey is allowed to overwrite; everything else (id, source, notes,
# saadia_note, scope, ...) is preserved verbatim.
REKEY_FIELDS = ("lemma_ja", "lemma_ar", "root", "pos", "gloss_en", "gloss_he", "variants")


def _norm(s: str) -> str:
    s = (s or "").replace("ך", "כ").replace("ם", "מ").replace("ן", "נ").replace("ף", "פ").replace("ץ", "צ")
    return s[:-1] if s.endswith("'") else s


def _keys(entry) -> set[str]:
    out = set()
    if entry.get("lemma_ja"):
        out.add(_norm(entry["lemma_ja"]))
    for v in entry.get("variants") or []:
        if v:
            out.add(_norm(v))
    return out


def main() -> int:
    lane_path = DATA / "dictionary-lane.json"
    fixes_path = DATA / "_inflected_fixes.json"
    for p in (lane_path, fixes_path):
        if not p.exists():
            print(f"FATAL: {p} not found", file=sys.stderr)
            return 1

    lane = json.loads(lane_path.read_text())
    fixes = json.loads(fixes_path.read_text())
    if isinstance(fixes, dict):  # tolerate {"fixes": [...]}
        fixes = fixes.get("fixes", [])

    by_id = {e.get("id"): e for e in lane["entries"] if e.get("id")}
    # Snapshot every surface key across ALL entries (id-bearing or not) so the
    # post-write assertion proves no token lost coverage.
    all_keys_before = set()
    for e in lane["entries"]:
        all_keys_before |= _keys(e)

    rekeyed = kept = missing = restored = 0
    for fx in fixes:
        if (fx.get("action") or "rekey") != "rekey":
            kept += 1
            continue
        eid = fx.get("id")
        entry = by_id.get(eid)
        if entry is None:
            missing += 1
            print(f"  WARN: fix id not found: {eid}", file=sys.stderr)
            continue
        orig_keys = _keys(entry)
        for f in REKEY_FIELDS:
            if f in fx and fx[f] is not None:
                entry[f] = fx[f]
        # Coverage guard: every original surface key must survive as lemma|variant.
        variants = entry.setdefault("variants", [])
        present = _keys(entry)
        # Recover the verbatim original surfaces (lemma + variants) to re-add the
        # exact strings, not just their normalized forms.
        orig_surfaces = []
        # entry was mutated, so reconstruct from keys_before via the lane snapshot
        # is impossible; instead trust that fx.variants should contain them. Re-add
        # any normalized original key that's now missing using the agent's variants
        # plus a fallback: we kept orig_keys, so synthesize from there is lossy.
        for nk in orig_keys:
            if nk not in present:
                variants.append(nk)  # normalized form is a valid lookup key
                present.add(nk)
                restored += 1
        rekeyed += 1

    # ---- merge entries that now share (norm(lemma_ja), root) -----------------
    merged = 0
    seen: dict[tuple[str, str], dict] = {}
    out_entries = []
    for e in lane["entries"]:
        root = (e.get("root") or "").strip()
        key = (_norm(e.get("lemma_ja", "")), root)
        if root and root != "—" and key in seen:
            tgt = seen[key]
            tv = tgt.setdefault("variants", [])
            have = _keys(tgt)
            for v in [e.get("lemma_ja")] + (e.get("variants") or []):
                if v and _norm(v) not in have:
                    tv.append(v)
                    have.add(_norm(v))
            # keep the longer gloss if the target's is thinner
            if len(e.get("gloss_en") or "") > len(tgt.get("gloss_en") or ""):
                tgt["gloss_en"] = e["gloss_en"]
            merged += 1
            continue
        seen[key] = e
        out_entries.append(e)
    lane["entries"] = out_entries

    # ---- coverage assertion -------------------------------------------------
    all_keys_after = set()
    for e in lane["entries"]:
        all_keys_after |= _keys(e)
    lost = all_keys_before - all_keys_after
    if lost:
        print(f"FATAL: {len(lost)} surface keys would be lost — aborting write. "
              f"e.g. {list(sorted(lost))[:10]}", file=sys.stderr)
        return 2

    lane_path.write_text(json.dumps(lane, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())  # parse-check

    print(f"rekeyed={rekeyed}  kept(no-op)={kept}  missing={missing}  "
          f"restored_dropped_surfaces={restored}  merged_duplicates={merged}")
    print(f"surface keys: before={len(all_keys_before)}  after={len(all_keys_after)}  "
          f"(superset OK, +{len(all_keys_after) - len(all_keys_before)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

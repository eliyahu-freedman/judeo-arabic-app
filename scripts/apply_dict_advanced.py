"""
Dictionary Coverage — Advanced-reader apply (Moreh / Kuzari / Saadia Emunot).

Same contract as scripts/apply_dict_batch2.py, reading the advanced-pass inputs:

  APPEND: data/_dict_advanced.json  [ {full entry}, ... ]
          Net-new, corpus-grounded stems whose glosses are Lane-based (classical
          Arabic) or, for Hebrew words the texts quote (e.g. צלם, נעשה), a
          Hebrew-aware gloss. Each entry carries every observed surface form as a
          variant (the runtime lookup does NOT strip pronominal suffixes).
          Dedup against the HAND dicts (starter + lane) + tafsir-divergence.json.
          A new entry whose id/lemma already exists is skipped; a variant
          colliding with an existing surface is dropped (entry still added).

  PATCH : data/_dict_advanced_patch.json  {entry_id_or_lemma: [surfaces...]}
          For inflected surfaces whose stem ALREADY has an entry in starter/lane,
          extend that entry's variants[]. Located by id, fallback lemma_ja.

Write-back: json.dumps(..., ensure_ascii=False, indent=2) + "\\n", then re-parse.
"""
import json
import pathlib
import sys


def _norm(s: str) -> str:
    s = (s or "").replace("ך", "כ").replace("ם", "מ").replace("ן", "נ").replace("ף", "פ").replace("ץ", "צ")
    if s.endswith("'"):
        s = s[:-1]
    return s


def _surfaces(d):
    out = set()
    for e in d.get("entries", []):
        if e.get("lemma_ja"):
            out.add(_norm(e["lemma_ja"]))
        for v in e.get("variants", []) or []:
            out.add(_norm(v))
    return out


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    data = root / "data"
    lane_path = data / "dictionary-lane.json"
    starter_path = data / "dictionary-starter.json"
    new_path = data / "_dict_advanced.json"
    patch_path = data / "_dict_advanced_patch.json"
    div_path = data / "tafsir-divergence.json"

    for p in (lane_path, starter_path, new_path):
        if not p.exists():
            print(f"FATAL: {p} not found — run from judeo-arabic-app root", file=sys.stderr)
            sys.exit(1)

    lane = json.loads(lane_path.read_text())
    starter = json.loads(starter_path.read_text())
    starter_before = json.dumps(starter, ensure_ascii=False, sort_keys=True)
    div = json.loads(div_path.read_text()) if div_path.exists() else {"entries": []}
    new_entries = json.loads(new_path.read_text())
    patch = json.loads(patch_path.read_text()) if patch_path.exists() else {}

    # Index entries by id and by lemma_ja across starter + lane (patch targets).
    by_id, by_lemma = {}, {}
    for d in (starter, lane):
        for e in d.get("entries", []):
            if e.get("id"):
                by_id.setdefault(e["id"], e)
            if e.get("lemma_ja"):
                by_lemma.setdefault(e["lemma_ja"], e)

    # ---- APPEND phase -------------------------------------------------------
    # Dedup against the HAND dicts (starter + lane) ONLY. NOT tafsir-divergence:
    # the Advanced reader's lookup() consults only starter + lane, so a word that
    # exists in divergence is still UNCOVERED in the Advanced texts and must be
    # added to lane here. (The Tafsir reader keeps its own divergence handling.)
    _ = div  # loaded for reference; intentionally not used for APPEND dedup
    ids = {e.get("id") for d in (starter, lane) for e in d.get("entries", [])}
    lemmas = {e.get("lemma_ja") for d in (starter, lane) for e in d.get("entries", [])}
    surfaces = _surfaces(starter) | _surfaces(lane)

    before = len(lane["entries"])
    added, skipped, dropped_vars = 0, [], 0
    for e in new_entries:
        if e.get("id") in ids:
            skipped.append((e.get("lemma_ja"), e.get("id"), "id exists"))
            continue
        if e.get("lemma_ja") in lemmas or _norm(e.get("lemma_ja", "")) in surfaces:
            skipped.append((e.get("lemma_ja"), e.get("id"), "lemma_ja/surface exists"))
            continue
        clean_vars = []
        for v in e.get("variants", []) or []:
            if _norm(v) in surfaces:
                dropped_vars += 1
            else:
                clean_vars.append(v)
        e["variants"] = clean_vars
        lane["entries"].append(e)
        # keep new entry reachable as a patch target in this same run
        by_id.setdefault(e["id"], e)
        by_lemma.setdefault(e["lemma_ja"], e)
        ids.add(e.get("id"))
        lemmas.add(e.get("lemma_ja"))
        surfaces.add(_norm(e["lemma_ja"]))
        for v in clean_vars:
            surfaces.add(_norm(v))
        added += 1

    # ---- PATCH phase --------------------------------------------------------
    patched_entries, patched_variants, patch_missing = 0, 0, []
    for eid, surfs in patch.items():
        target = by_id.get(eid) or by_lemma.get(eid)
        if target is None:
            patch_missing.append(eid)
            continue
        existing = target.setdefault("variants", [])
        existing_norm = {_norm(v) for v in existing}
        existing_norm.add(_norm(target.get("lemma_ja", "")))
        added_here = 0
        for s in surfs:
            if _norm(s) not in existing_norm:
                existing.append(s)
                existing_norm.add(_norm(s))
                added_here += 1
        if added_here:
            patched_entries += 1
            patched_variants += added_here

    lane_path.write_text(json.dumps(lane, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())  # parse-check

    # Some patch targets live in starter (the Bereshit-1 seed), not lane. Write
    # starter back too if a patch augmented one of its entries — otherwise those
    # added variants would be silently lost (lane was the only file written).
    if json.dumps(starter, ensure_ascii=False, sort_keys=True) != starter_before:
        starter_path.write_text(json.dumps(starter, ensure_ascii=False, indent=2) + "\n")
        json.loads(starter_path.read_text())
        print("  (starter dictionary also updated — patched seed entries)")

    print(f"APPEND: lane entries {before} -> {len(lane['entries'])}  (+{added}); "
          f"{dropped_vars} colliding variants dropped")
    if skipped:
        print(f"  skipped {len(skipped)} new entries:")
        for lj, eid, why in skipped:
            print(f"    - {lj} ({eid}): {why}")
    print(f"PATCH : {patched_entries} entries augmented, +{patched_variants} variants")
    if patch_missing:
        print(f"  patch targets not found ({len(patch_missing)}): {', '.join(patch_missing)}")


if __name__ == "__main__":
    main()

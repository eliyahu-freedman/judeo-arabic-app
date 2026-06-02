"""
Dictionary Coverage — Batch 2 apply (variant augmentation + net-new stems).

Two phases against data/dictionary-lane.json -> entries[]:

  PATCH : data/_dict_batch2_patch.json  {entry_id: [surfaces...]}
          For each entry (located by id, fallback lemma_ja in starter OR lane),
          extend variants[] with the listed surfaces (dedup, final-letter +
          trailing-' normalized). These are exact corpus miss surfaces of
          inflected / pronominal-suffix forms whose stem already has an entry —
          the runtime lookup (lib/lookup.ts) does NOT strip suffixes, so they
          must be explicit variants.

  APPEND: data/_dict_batch2.json  [ {full entry}, ... ]
          Net-new, corpus-grounded stems. Dedup is against the HAND dicts
          (starter + lane) and tafsir-divergence.json ONLY — NOT the auto
          (camel) dict, which is being retired and which a hand entry is meant
          to supersede (a form like פכתב misses today precisely because כתב is
          only an unverified auto lemma). Skipped only if id or lemma_ja already
          exists in a hand/divergence source; a variant colliding with an
          existing hand/divergence surface is dropped (entry still added) so a
          coincidental collision can't suppress a whole new stem.

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
    """All normalized lemma_ja + variant surfaces across an {entries:[]} dict."""
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
    auto_path = data / "dictionary-auto.json"
    patch_path = data / "_dict_batch2_patch.json"
    new_path = data / "_dict_batch2.json"

    for p in (lane_path, starter_path, auto_path, patch_path, new_path):
        if not p.exists():
            print(f"FATAL: {p} not found — run from judeo-arabic-app root", file=sys.stderr)
            sys.exit(1)

    div_path = data / "tafsir-divergence.json"
    lane = json.loads(lane_path.read_text())
    starter = json.loads(starter_path.read_text())
    auto = json.loads(auto_path.read_text())
    div = json.loads(div_path.read_text()) if div_path.exists() else {"entries": []}
    patch = json.loads(patch_path.read_text())
    new_entries = json.loads(new_path.read_text())

    # Index entries by id and by lemma_ja across starter + lane (patch targets).
    by_id, by_lemma = {}, {}
    for d in (starter, lane):
        for e in d.get("entries", []):
            if e.get("id"):
                by_id.setdefault(e["id"], e)
            if e.get("lemma_ja"):
                by_lemma.setdefault(e["lemma_ja"], e)

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

    # ---- APPEND phase -------------------------------------------------------
    # Dedup against HAND dicts + divergence only (NOT the auto/camel dict).
    ids = {e.get("id") for d in (starter, lane) for e in d.get("entries", [])}
    lemmas = {e.get("lemma_ja") for d in (starter, lane, div) for e in d.get("entries", [])}
    surfaces = _surfaces(starter) | _surfaces(lane) | _surfaces(div)

    before = len(lane["entries"])
    added, skipped, dropped_vars = 0, [], 0
    for e in new_entries:
        if e.get("id") in ids:
            skipped.append((e.get("lemma_ja"), "id exists"))
            continue
        if e.get("lemma_ja") in lemmas or _norm(e.get("lemma_ja", "")) in surfaces:
            skipped.append((e.get("lemma_ja"), "lemma_ja/surface exists"))
            continue
        # Drop only the colliding variants, keep the entry.
        clean_vars = []
        for v in e.get("variants", []) or []:
            if _norm(v) in surfaces:
                dropped_vars += 1
            else:
                clean_vars.append(v)
        e["variants"] = clean_vars
        lane["entries"].append(e)
        ids.add(e.get("id"))
        lemmas.add(e.get("lemma_ja"))
        surfaces.add(_norm(e["lemma_ja"]))
        for v in clean_vars:
            surfaces.add(_norm(v))
        added += 1

    lane_path.write_text(json.dumps(lane, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())  # parse-check

    print(f"PATCH : {patched_entries} entries augmented, +{patched_variants} variants")
    if patch_missing:
        print(f"  patch targets not found ({len(patch_missing)}): {', '.join(patch_missing)}")
    print(f"APPEND: lane entries {before} -> {len(lane['entries'])}  (+{added}); "
          f"{dropped_vars} colliding variants dropped")
    if skipped:
        print(f"  skipped {len(skipped)} new entries:")
        for lj, why in skipped:
            print(f"    - {lj}: {why}")


if __name__ == "__main__":
    main()

"""
Dictionary Coverage — Batch 1 apply.

Appends the verified, corpus-grounded entries in data/_dict_batch1.json to the
hand-curated lane tier (data/dictionary-lane.json -> entries[]). These close the
most frequent tap-to-define misses (top ~250 ranked surfaces in
data/coverage-misses.json), grouped at the stem level with suffixed surfaces in
variants[]. Glosses trace to the aligned Hebrew of an actual corpus occurrence;
non-obvious / Saadia-specific / low-confidence rows were deferred (see
data/_dict_batch1_deferred.json), not shipped.

Dedup: skip any entry whose id or lemma_ja already exists in starter/lane/auto,
or whose lemma_ja / any variant collides (after final-letter + trailing-'
normalization) with an existing lemma_ja or variant in any of the three dicts.
(The serializer already deduped incl. against tafsir-divergence.json; this is a
belt-and-suspenders re-check at apply time.)

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


def _existing_keys(*dicts):
    ids, lemmas, surfaces = set(), set(), set()
    for d in dicts:
        for e in d.get("entries", []):
            if e.get("id"):
                ids.add(e["id"])
            lj = e.get("lemma_ja")
            if lj:
                lemmas.add(lj)
                surfaces.add(_norm(lj))
            for v in e.get("variants", []) or []:
                surfaces.add(_norm(v))
    return ids, lemmas, surfaces


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    data = root / "data"
    lane_path = data / "dictionary-lane.json"
    batch_path = data / "_dict_batch1.json"

    for p in (lane_path, batch_path, data / "dictionary-starter.json", data / "dictionary-auto.json"):
        if not p.exists():
            print(f"FATAL: {p} not found — run from judeo-arabic-app root", file=sys.stderr)
            sys.exit(1)

    lane = json.loads(lane_path.read_text())
    starter = json.loads((data / "dictionary-starter.json").read_text())
    auto = json.loads((data / "dictionary-auto.json").read_text())
    batch = json.loads(batch_path.read_text())

    ids, lemmas, surfaces = _existing_keys(starter, lane, auto)

    before = len(lane["entries"])
    added, skipped = 0, []
    for e in batch:
        why = None
        if e.get("id") in ids:
            why = "id exists"
        elif e.get("lemma_ja") in lemmas:
            why = "lemma_ja exists"
        else:
            collide = [_norm(e["lemma_ja"])] + [_norm(v) for v in e.get("variants", []) or []]
            hit = next((c for c in collide if c in surfaces), None)
            if hit:
                why = f"surface collision ({hit})"
        if why:
            skipped.append((e.get("lemma_ja"), why))
            continue
        lane["entries"].append(e)
        ids.add(e.get("id"))
        lemmas.add(e["lemma_ja"])
        surfaces.add(_norm(e["lemma_ja"]))
        for v in e.get("variants", []) or []:
            surfaces.add(_norm(v))
        added += 1

    lane_path.write_text(json.dumps(lane, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())  # parse-check

    print(f"lane entries: {before} -> {len(lane['entries'])}  (+{added})")
    print(f"skipped: {len(skipped)}")
    for lj, why in skipped:
        print(f"  - {lj}: {why}")


if __name__ == "__main__":
    main()

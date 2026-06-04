#!/usr/bin/env python3
"""
Batch 2 harvest helper (dev-only; not shipped logic).

For each ranked tap-to-define miss in data/coverage-misses.json, decide whether
its stem ALREADY has a hand entry (starter/lane) reachable by stripping a
pronominal/verbal suffix — in which case the fix is to append the suffixed
surface to that entry's variants[] (cheap "augment") — or whether no stem entry
exists yet ("new", needs a full corpus-grounded entry).

This only mirrors the lookup *prefix* chain (lib/lookup.ts) and then additionally
tries suffix stripping, which the runtime lookup deliberately does NOT do. The
output is a curation worklist, not runtime behaviour.

Writes data/_batch2_worklist.json and prints a summary.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

PREFIXES = ("ב", "ל", "כ", "פ")

# Common JA (Hebrew-script) inflectional / pronominal-suffix endings, longest
# first so we strip the maximal affix. These are heuristics for *grouping*, the
# gloss/sense is always confirmed by hand against the corpus before shipping.
SUFFIXES = [
    "המא", "כמא", "תמא", "המא",
    "הם", "הן", "כם", "כן", "נא", "תם", "תן", "הא", "וא", "ון", "ין", "את", "אן",
    "ני", "ה", "ך", "ך", "י", "ת", "ן", "א", "ו",
]


def strip_punct(tok: str) -> str:
    return re.sub(r"^[.,:;؛،\"'\s]+|[.,:;؛،\"'\s]+$", "", tok)


def normalize_finals(s: str) -> str:
    s = (
        s.replace("ך", "כ").replace("ם", "מ").replace("ן", "נ")
        .replace("ף", "פ").replace("ץ", "צ")
    )
    if s.endswith("'"):
        s = s[:-1]
    return s


def prefix_candidates(raw: str) -> list[str]:
    """Mirror lib/lookup.ts candidate chain (prefix strips), final-normalized."""
    tok = strip_punct(raw)
    if not tok:
        return []
    tries: set[str] = set()

    def with_al(s: str) -> None:
        if not s:
            return
        tries.add(s)
        if s.startswith("אל") and len(s) > 2:
            tries.add(s[2:])

    with_al(tok)
    after_vav = None
    if tok.startswith("ו") and len(tok) > 1:
        after_vav = tok[1:]
        with_al(after_vav)
    for base in [tok, after_vav]:
        if not base:
            continue
        for p in PREFIXES:
            if base.startswith(p) and len(base) > 1:
                with_al(base[1:])
    base = list(tries)
    return list({*base, *(normalize_finals(t) for t in base)})


def reduced_variant(raw: str) -> str:
    """Most general surface to add as a variant: leading ו / prep / אל removed,
    verbal prefixes + suffixes kept, final-normalized."""
    t = strip_punct(raw)
    if t.startswith("ו") and len(t) > 1:
        t = t[1:]
    if t and t[0] in PREFIXES and len(t) > 1:
        t = t[1:]
    if t.startswith("אל") and len(t) > 2:
        t = t[2:]
    return normalize_finals(t)


def build_index() -> dict[str, dict]:
    """norm-surface -> {tier, id, lemma_ja, gloss_en}. starter wins over lane."""
    idx: dict[str, dict] = {}
    for tier, fname in (("lane", "dictionary-lane.json"), ("starter", "dictionary-starter.json")):
        obj = json.loads((DATA / fname).read_text())
        for e in obj.get("entries", []):
            rec = {"tier": tier, "id": e.get("id"), "lemma_ja": e.get("lemma_ja"),
                   "gloss_en": e.get("gloss_en", "")}
            for surf in [e.get("lemma_ja")] + (e.get("variants") or []):
                if surf:
                    idx[normalize_finals(surf)] = rec  # starter overwrites lane
    return idx


def auto_keys() -> set[str]:
    obj = json.loads((DATA / "dictionary-auto.json").read_text())
    return {e["lemma_ja"] for e in obj.get("entries", []) if e.get("lemma_ja")}


def divergence_keys() -> set[str]:
    p = DATA / "tafsir-divergence.json"
    if not p.exists():
        return set()
    obj = json.loads(p.read_text())
    keys: set[str] = set()
    entries = obj.get("entries", obj if isinstance(obj, list) else [])
    for e in entries:
        for surf in [e.get("lemma_ja")] + (e.get("variants") or []):
            if surf:
                keys.add(normalize_finals(surf))
    return keys


# Verbal-imperfect / derivational leading letters to peel when *hinting* at an
# existing root entry (NOT part of the runtime chain — used only to route a
# miss to an entry whose full surface we then add verbatim as a variant).
VERBAL_PREFIXES = ("ית", "ת", "י", "נ", "א", "מ", "ست", "אן")


def deep_stem_entry(surface: str, idx: dict[str, dict]):
    """Aggressively peel prefixes (conjunction/prep/article, up to 2x, plus a
    verbal-imperfect prefix) and a trailing suffix, looking for an existing
    entry. Returns the matched entry rec or None. Over-stripping is acceptable
    here because the variant we ultimately add is the *full* surface; this only
    suggests which entry to hang it on (and is hand-confirmed per cluster)."""
    t0 = normalize_finals(strip_punct(surface))
    bases: set[str] = {t0}
    # peel leading conjunction / prep / article up to two layers
    cur = {t0}
    for _ in range(2):
        nxt = set()
        for s in cur:
            if s.startswith("ו") and len(s) > 2:
                nxt.add(s[1:])
            if s and s[0] in PREFIXES and len(s) > 2:
                nxt.add(s[1:])
            if s.startswith("אל") and len(s) > 3:
                nxt.add(s[2:])
        bases |= nxt
        cur = nxt
    # add verbal-prefix-stripped variants of every base
    for s in list(bases):
        for vp in VERBAL_PREFIXES:
            if s.startswith(vp) and len(s) - len(vp) >= 2:
                bases.add(s[len(vp):])
    # now try direct + one-suffix-strip against the index
    for b in sorted(bases, key=len, reverse=True):
        if b in idx:
            return idx[b]
        for suf in SUFFIXES:
            if b.endswith(suf) and len(b) - len(suf) >= 2:
                stem = normalize_finals(b[: -len(suf)])
                if stem in idx:
                    return idx[stem]
    return None


def classify(surface: str, idx: dict[str, dict], auto: set[str], div: set[str]) -> dict:
    cands = prefix_candidates(surface)
    # Any prefix candidate already in index => should resolve; flag for inspect.
    for c in cands:
        if c in idx:
            return {"status": "already-resolves?", "stem": c, "entry": idx[c]}
    # Try stripping a suffix off each prefix candidate.
    for c in sorted(cands, key=len, reverse=True):
        for suf in SUFFIXES:
            if c.endswith(suf) and len(c) - len(suf) >= 2:
                stem = normalize_finals(c[: -len(suf)])
                if stem in idx:
                    return {"status": "augment", "suffix": suf, "stem": stem,
                            "entry": idx[stem]}
    # Net-new. Note overlaps with divergence/auto for triage.
    flags = []
    if reduced_variant(surface) in div:
        flags.append("divergence-overlap")
    if normalize_finals(strip_punct(surface)) in auto or reduced_variant(surface) in auto:
        flags.append("in-auto")
    return {"status": "new", "flags": flags, "stem_guess": reduced_variant(surface)}


def main() -> int:
    misses = json.loads((DATA / "coverage-misses.json").read_text())["misses"]
    idx = build_index()
    auto = auto_keys()
    div = divergence_keys()

    rows = []
    for m in misses:
        surf, cnt = m["surface"], m["count"]
        if len(strip_punct(surf)) <= 1:
            cls = {"status": "noise"}
        else:
            cls = classify(surf, idx, auto, div)
        rows.append({"surface": surf, "count": cnt,
                     "reduced": reduced_variant(surf), **cls})

    (DATA / "_batch2_worklist.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n"
    )

    by_status = Counter(r["status"] for r in rows)
    occ_by_status: Counter = Counter()
    for r in rows:
        occ_by_status[r["status"]] += r["count"]

    print("Batch 2 harvest")
    print("=" * 40)
    print(f"miss surfaces analysed: {len(rows)}")
    print(f"{'status':<18}{'surfaces':>10}{'occurrences':>14}")
    for st in ("augment", "new", "already-resolves?", "noise"):
        print(f"{st:<18}{by_status.get(st,0):>10}{occ_by_status.get(st,0):>14}")
    print()

    # ---- AUGMENT: group by entry id; the variant we add is the EXACT surface
    # (punct-stripped) so the chain's layer-1 resolves it with no over-strip. ----
    aug = [r for r in rows if r["status"] == "augment"]
    by_entry: dict[str, dict] = {}
    for r in aug:
        eid = r["entry"]["id"] or r["entry"]["lemma_ja"]
        slot = by_entry.setdefault(eid, {"entry": r["entry"], "surfs": []})
        slot["surfs"].append({"surface": strip_punct(r["surface"]), "count": r["count"]})
    patch_auto = {eid: sorted({s["surface"] for s in v["surfs"]})
                  for eid, v in by_entry.items()}
    (DATA / "_batch2_patch_auto.json").write_text(
        json.dumps(patch_auto, ensure_ascii=False, indent=2) + "\n"
    )
    print(f"augment: {len(aug)} surfaces -> {len(by_entry)} distinct entries")
    print("top augment entries (occ / lemma / id / gloss / surfaces-to-add):")
    ranked = sorted(by_entry.items(),
                    key=lambda kv: sum(x["count"] for x in kv[1]["surfs"]), reverse=True)
    for eid, v in ranked[:45]:
        occ = sum(x["count"] for x in v["surfs"])
        lemma = v["entry"]["lemma_ja"]
        gloss = (v["entry"]["gloss_en"] or "")[:26]
        surfs = " ".join(s["surface"] for s in v["surfs"][:7])
        print(f"  {occ:>4}  {lemma:<7} [{eid:<18}] {gloss:<28} {surfs}")
    print()

    # ---- NEW: cluster by a conservative stem key to surface high-value new
    # stems (one entry can cover several inflected surfaces). ----
    new = [r for r in rows if r["status"] == "new"]
    clusters: dict[str, list] = {}
    for r in new:
        clusters.setdefault(r["stem_guess"], []).append(r)
    ranked_new = sorted(clusters.items(),
                        key=lambda kv: sum(x["count"] for x in kv[1]), reverse=True)
    print(f"new: {len(new)} surfaces -> {len(clusters)} stem clusters")
    print("top NEW stem clusters (occ / stem-guess / hint-entry / surfaces):")
    for stem, items in ranked_new[:80]:
        occ = sum(x["count"] for x in items)
        if occ < 4:
            break
        flags = ",".join(sorted({f for x in items for f in x.get("flags", [])}))
        # hint: does an existing entry plausibly cover this cluster?
        hint = deep_stem_entry(items[0]["surface"], idx)
        htxt = f"->{hint['lemma_ja']}[{hint['id']}]" if hint else ""
        surfs = " ".join(x["surface"] for x in sorted(items, key=lambda x: -x["count"])[:8])
        tag = ("[" + flags + "]") if flags else ""
        print(f"  {occ:>4}  {stem:<9} {htxt:<26} {tag:<20} {surfs}")
    print()
    print(f"Wrote {DATA / '_batch2_worklist.json'}")
    print(f"Wrote {DATA / '_batch2_patch_auto.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

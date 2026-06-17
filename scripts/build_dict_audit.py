#!/usr/bin/env python3
"""Build a semantic-QC audit worklist for the tap-to-define dictionary, grounded
in a translated gate's phrase alignment.

Usage: build_dict_audit.py [BAB] [--pages N]
  BAB        gate number (default 1)
  --pages N  limit the audit to the first N pages (JA order) — for subsection
             pilots; default = all pages.

For every tappable Judeo-Arabic word in bahya-bab<BAB>-aligned.json we resolve
the entry the READER would show (via scripts/_audit_dict_cli.ts, which calls the
real lib/lookup.ts) and pair it with the contextual English from the alignment.
We then dedup to distinct (surface -> resolved entry) units and flag SUSPECTS
likely to be mis-tagged, so the LLM judge only has to look at the suspicious
slice rather than the gate's whole vocabulary.

Outputs (under data/_dict_audit/):
  bab<BAB>.json          — every distinct (surface, entry_id) unit + context
  bab<BAB>_suspects.json — the flagged subset, ranked (the LLM judge worklist)
"""
import json
import os
import re
import subprocess
import sys

argv = sys.argv[1:]
PAGES_LIMIT = None
if "--pages" in argv:
    i = argv.index("--pages")
    PAGES_LIMIT = int(argv[i + 1])
    del argv[i : i + 2]
BAB = int(argv[0]) if argv else 1
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUTDIR = os.path.join(DATA, "_dict_audit")

# Reuse the inflected-lemma gloss heuristics if available (best-effort import).
try:
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    from find_inflected_lemmas import signals_for  # type: ignore
except Exception:
    def signals_for(lemma_ja, gloss_en, gloss_he, variants):  # fallback
        return []

# JA orthography apostrophe-modified letters (ت'=ث etc.). A surface containing
# none of these AND only "plain" Hebrew letters is a weak signal for embedded
# Tanakh Hebrew, which is frequently mis-glossed as Arabic.
APOS = "'"


def resolve_phrases(phrases):
    """Run every phrase through the runtime resolver CLI in one tsx process."""
    cli = os.path.join(ROOT, "scripts", "_audit_dict_cli.ts")
    payload = "".join(json.dumps({"text": p}, ensure_ascii=False) + "\n" for p in phrases)
    proc = subprocess.run(
        ["npx", "tsx", cli],
        input=payload, capture_output=True, text=True, cwd=ROOT,
    )
    if proc.returncode != 0:
        sys.exit(f"_audit_dict_cli.ts failed:\n{proc.stderr}")
    out = []
    for line in proc.stdout.splitlines():
        out.append(json.loads(line) if line.strip() else [])
    return out


def main():
    aligned = json.load(open(os.path.join(DATA, f"bahya-bab{BAB}-aligned.json")))

    # Collect (ja_phrase, en_phrase, kind) occurrences. PAIRS give the tightest
    # JA<->EN context; the full segment JA gives complete tappable coverage for
    # words that sit outside any pair.
    occ = []  # list of (ja_phrase, en_phrase, kind, is_single_word_pair)
    page_items = list(aligned.get("pages", {}).items())
    if PAGES_LIMIT is not None:
        page_items = page_items[:PAGES_LIMIT]
    for page_he, segs in page_items:
        for seg in segs:
            sja, sen = seg.get("ja", ""), seg.get("en", "")
            if sja:
                occ.append((sja, sen, "seg", False))
            for pair in seg.get("pairs", []) or []:
                pja, pen = pair.get("ja", ""), pair.get("en", "")
                if pja:
                    single = len(pja.split()) == 1
                    occ.append((pja, pen, "pair", single))

    phrases = [o[0] for o in occ]
    resolved = resolve_phrases(phrases)

    # Dedup to distinct (surface, entry_id). Keep occurrence count + the BEST
    # context (prefer a single-word pair, then any pair, then a segment; shorter
    # ja_phrase wins as the more isolated, stronger signal).
    units = {}  # key (surface, entry_id) -> record
    ctx_rank = {"single": 0, "pair": 1, "seg": 2}

    for (ja_phrase, en_phrase, kind, single), words in zip(occ, resolved):
        for w in words:
            surface = w["surface"]
            e = w["entry"]
            entry_id = e["id"] if e else "<MISS>"
            key = (surface, entry_id)
            this_ctx = "single" if (kind == "pair" and single) else kind
            rec = units.get(key)
            if rec is None:
                units[key] = rec = {
                    "surface": surface,
                    "n_hits": w["n_hits"],
                    "entry": e,
                    "count": 0,
                    "ever_single_pair": False,
                    "_ctx_rank": 99,
                    "ja_phrase": ja_phrase,
                    "en_phrase": en_phrase,
                }
            rec["count"] += 1
            if this_ctx == "single":
                rec["ever_single_pair"] = True
            r = ctx_rank[this_ctx]
            if r < rec["_ctx_rank"] or (
                r == rec["_ctx_rank"] and len(ja_phrase) < len(rec["ja_phrase"])
            ):
                rec["_ctx_rank"] = r
                rec["ja_phrase"] = ja_phrase
                rec["en_phrase"] = en_phrase

    all_units = list(units.values())
    for r in all_units:
        r.pop("_ctx_rank", None)

    # ---- suspect scoring ----------------------------------------------------
    # Bare variant-match flags ~1/3 of the vocabulary and is mostly fine
    # (the whole point of variants). The signals that actually correlate with a
    # MIS-tag are: (a) the gloss shares no content with the contextual English
    # AND the match was via a variant (the חאל/רבי/ד'כרנא class); (b) a genuine
    # homograph (n_hits>1, two lemmas compete); (c) the gloss text itself reads
    # as an inflected/possessed form (find_inflected_lemmas). We require a tight
    # PAIR context for (a)/(b) so en_phrase is a real per-word gloss, not a whole
    # sentence that overlaps any gloss by chance.
    STOP = set(
        "a an the of to in on and or for with by is be it its his her their from "
        "that this which who whom as at upon them they he she we you i not no into "
        "one s".split()
    )

    def content_stems(s):
        return {w[:5] for w in re.findall(r"[a-z']+", (s or "").lower())
                if w not in STOP and len(w) > 2}

    def pairish(u):
        return len(u["en_phrase"].split()) <= 6

    suspects = []
    for r in all_units:
        e = r["entry"]
        reasons = []
        score = 0
        if e is None:
            reasons.append("uncovered")
            score += 5
        else:
            pi = pairish(r)
            vm = e.get("matched") == "variant"
            overlap = len(content_stems(e.get("gloss_en")) & content_stems(r["en_phrase"]))
            if vm and pi and overlap == 0:
                reasons.append("variant+zero-overlap")
                score += 3
            if r["n_hits"] > 1 and pi:
                reasons.append("homograph")
                score += 2
            sig = signals_for(e.get("lemma_ja", ""), e.get("gloss_en", ""), "", [])
            if sig:
                reasons.append("gloss-inflection:" + ",".join(sig))
                score += 1
            r["gloss_ctx_overlap"] = overlap
        if reasons:
            r2 = dict(r)
            r2["suspect_reasons"] = reasons
            r2["suspect_score"] = score
            suspects.append(r2)

    suspects.sort(key=lambda r: (-r["suspect_score"], r["surface"]))

    # ---- ledger dedup: drop (surface,entry) already adjudicated anywhere -----
    ledger_path = os.path.join(OUTDIR, "judged_ledger.json")
    ledger = {}
    if os.path.exists(ledger_path):
        ledger = json.load(open(ledger_path)).get("ledger", {})
    n_before = len(suspects)
    def led_key(r):
        return r["surface"] + "\t" + ((r["entry"] or {}).get("id", "<MISS>"))
    fresh = [r for r in suspects if led_key(r) not in ledger]
    n_skipped = n_before - len(fresh)

    # ---- group the fresh suspects by entry_id (one verdict per entry) --------
    groups = {}
    for r in fresh:
        eid = (r["entry"] or {}).get("id", "<MISS>")
        g = groups.get(eid)
        if g is None:
            groups[eid] = g = {
                "entry_id": eid,
                "entry": r["entry"],
                "surfaces": [],
            }
        g["surfaces"].append({
            "surface": r["surface"],
            "ja_phrase": r["ja_phrase"],
            "en_phrase": r["en_phrase"],
            "n_hits": r["n_hits"],
            "suspect_reasons": r["suspect_reasons"],
        })
    grouped = sorted(groups.values(), key=lambda g: -len(g["surfaces"]))

    os.makedirs(OUTDIR, exist_ok=True)
    json.dump(
        {"bab": BAB, "units": all_units},
        open(os.path.join(OUTDIR, f"bab{BAB}.json"), "w"),
        ensure_ascii=False, indent=2,
    )
    json.dump(
        {"bab": BAB, "suspects": fresh},   # flat fresh suspects (ledger-deduped)
        open(os.path.join(OUTDIR, f"bab{BAB}_suspects.json"), "w"),
        ensure_ascii=False, indent=2,
    )
    json.dump(
        {"bab": BAB, "groups": grouped},   # entry-grouped worklist for the judge
        open(os.path.join(OUTDIR, f"bab{BAB}_groups.json"), "w"),
        ensure_ascii=False, indent=2,
    )

    scope = f"first {PAGES_LIMIT} pages" if PAGES_LIMIT is not None else "all pages"
    from collections import Counter
    tally = Counter()
    for s in fresh:
        for r in s["suspect_reasons"]:
            tally[r.split(":")[0]] += 1
    print(f"bab {BAB} ({scope}): {len(all_units)} distinct (surface,entry) units")
    print(f"  suspects: {n_before} total; {n_skipped} already in ledger; "
          f"{len(fresh)} FRESH -> {len(grouped)} entry-groups to judge")
    print(f"  fresh reasons: {dict(tally)}")
    print(f"  ~{-(-len(grouped)//30)} judge agents @30 entry-groups/batch")
    print(f"wrote {OUTDIR}/bab{BAB}.json, bab{BAB}_suspects.json, bab{BAB}_groups.json")


if __name__ == "__main__":
    main()

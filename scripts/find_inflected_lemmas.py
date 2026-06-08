#!/usr/bin/env python3
"""
Lint: dictionary entries whose HEADWORD (lemma_ja) is an inflected form.

The runtime convention (see lib/lookup.ts) is:
    lemma_ja  = the base CITATION form (singular, no article, no possessive;
                for verbs the dictionary's citation form).
    variants  = equal-or-MORE-inflected surface forms only.

When that invariant is violated — an inflected surface form sits in the lemma
slot with an inflected gloss, while the base form is buried in variants[] — a
user who taps the BASE form (e.g. אלאימאן "the faith") resolves to the entry via
its variant and sees the wrong, suffixed headword + gloss (אימנאך "your faith,
your belief (+ suffix)"). This script flags those entries so they can be
re-keyed to the base citation form.

Outputs data/_inflected_worklist.json (full entries + signals) for the
correction workflow, and prints counts. Used both to build the worklist and,
after the fix, as a regression lint (the high-confidence count should be ≈0).

Run from the repo root:  python3 scripts/find_inflected_lemmas.py
"""

from __future__ import annotations

import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# ---- gloss signals that the headword denotes an inflected (non-citation) sense
POSSESSIVE = re.compile(r"^\s*(its|his|her|their|your|our|my)\b", re.I)
SUFFIX = re.compile(r"suffix", re.I)
# conjugated-verb / bound-form markers in the gloss
CONJ = re.compile(
    r"\b(pf\.|impf\.|perfect|imperfect|[123](?:sg|pl|ms|fs|mp|fp|cp|cs))\b"
    r"|form\s+[IVX]+\s*\+|\bI\s+\w+ed it\b|\bhe\s+\w+s it\b",
    re.I,
)

# Pronominal-suffix endings (Hebrew-script JA). Longest-first so the multi-letter
# ones are recognised before their single-letter tails.
PRON_SUFFIXES = ["המא", "המ", "הן", "הא", "כמ", "כן", "נא", "ני", "ה", "ך", "כ", "י", "ם", "ן"]

# Known false-positives: the trailing ה/א is ROOT, not a pronominal suffix, so
# these must never be flagged on the morphology heuristic alone. (Mirrors the
# caveats in lib/lookup.ts:48-54.) The gloss-signal path can still flag a real
# inflected gloss; this set only suppresses the bare-morphology heuristic.
MORPH_SAFELIST = {
    "אלאה", "אללה", "אלה", "מלאיכה", "מלאכה", "חכמה", "קצה", "אמה",
    "כלמה", "סנה", "איה", "מאיה", "סאעה", "ספינה",
}


def _norm(s: str) -> str:
    s = (s or "").replace("ך", "כ").replace("ם", "מ").replace("ן", "נ").replace("ף", "פ").replace("ץ", "צ")
    return s[:-1] if s.endswith("'") else s


def _ends_with_pron_suffix(lemma: str) -> str | None:
    for suf in PRON_SUFFIXES:
        if len(lemma) > len(suf) + 1 and lemma.endswith(suf):
            return suf
    return None


def signals_for(lemma_ja: str, gloss_en: str, gloss_he: str, variants: list[str]) -> list[str]:
    sig: list[str] = []
    g = gloss_en or ""
    if SUFFIX.search(g) or SUFFIX.search(gloss_he or ""):
        sig.append("gloss:suffix")
    if POSSESSIVE.search(g):
        sig.append("gloss:possessive")
    if CONJ.search(g):
        sig.append("gloss:conjugation")

    lj = lemma_ja or ""
    shorter = [v for v in (variants or []) if len(_norm(v)) < len(_norm(lj))]
    if shorter and _norm(lj) not in MORPH_SAFELIST:
        suf = _ends_with_pron_suffix(_norm(lj))
        if suf:
            sig.append(f"morph:suffix-{suf}+shorter-variant")
    return sig


def scan_entries(entries, lemma_key="lemma_ja", gloss_en_key="gloss_en", gloss_he_key="gloss_he"):
    """Tag each flagged entry with a tier:

      A     gloss denotes a bound/possessed/conjugated sense AND a strictly
            shorter (base) form is in variants[] -> a base form is provably
            SHADOWED by this inflected headword. The reported bug class.
      B     gloss denotes an inflected sense but no shorter base form is in the
            entry -> headword-quality issue, no in-entry shadowing.
      morph morphology-only signal (lemma ends in a possible suffix + a shorter
            variant) with NO gloss signal. DOMINATED by tā-marbūṭa false
            positives (פצ'ה "silver", קריה "town"); NOT auto-fixed.

    Only tiers A and B are fix candidates; the gloss is the reliable signal.
    """
    flagged = []
    for e in entries:
        lj = e.get(lemma_key) or ""
        variants = e.get("variants") or []
        sig = signals_for(lj, e.get(gloss_en_key) or e.get("blau_sense_en") or "",
                          e.get(gloss_he_key) or e.get("blau_sense_he") or "", variants)
        if not sig:
            continue
        shorter = sorted({v for v in variants if len(_norm(v)) < len(_norm(lj))}, key=len)
        gloss_sig = any(s.startswith("gloss:") for s in sig)
        tier = ("A" if gloss_sig and shorter else
                "B" if gloss_sig else
                "morph")
        rec = dict(e)
        rec["_signals"] = sig
        rec["_shorter_variants"] = shorter
        rec["_tier"] = tier
        flagged.append(rec)
    return flagged


def main() -> int:
    lane = json.loads((DATA / "dictionary-lane.json").read_text())
    lane_flagged = scan_entries(lane.get("entries", []))

    overlays = {}
    for path in sorted(glob.glob(str(DATA / "blau-notes-*.json"))):
        doc = json.loads(Path(path).read_text())
        notes = doc.get("notes", []) if isinstance(doc, dict) else []
        f = scan_entries(notes)
        if f:
            overlays[Path(path).name] = f

    def tier(lst, t):
        return [e for e in lst if e["_tier"] == t]

    lane_A, lane_B, lane_m = tier(lane_flagged, "A"), tier(lane_flagged, "B"), tier(lane_flagged, "morph")
    overlay_fix = {n: [e for e in f if e["_tier"] in ("A", "B")] for n, f in overlays.items()}

    # Fix candidates = gloss-signal tiers (A + B) only; morph-only is reported
    # but never auto-fixed (tā-marbūṭa false positives).
    fix_candidates = lane_A + lane_B
    worklist = {
        "_generated": "scripts/find_inflected_lemmas.py",
        "lane": {
            "tier_A": len(lane_A),
            "tier_B": len(lane_B),
            "tier_morph": len(lane_m),
            "fix_candidates": fix_candidates,
        },
        "overlays": overlay_fix,
    }
    out = DATA / "_inflected_worklist.json"
    out.write_text(json.dumps(worklist, ensure_ascii=False, indent=2) + "\n")

    print("Inflected-lemma lint")
    print("====================")
    print(f"  dictionary-lane.json : tier A (shadowing bug) = {len(lane_A)}  |  "
          f"tier B (inflected headword) = {len(lane_B)}  |  "
          f"morph-only (FP, ignored) = {len(lane_m)}")
    print(f"  -> fix candidates (A+B): {len(fix_candidates)}")
    for name, f in overlay_fix.items():
        print(f"  {name:24}: {len(f)} fix candidates")
    print(f"\nWrote {out}")
    print("\nRegression gate after fix: tier A should be ≈0 (a fixed entry's base "
          "gloss no longer carries an inflection signal).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

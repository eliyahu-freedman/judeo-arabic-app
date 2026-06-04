"""
Phase 4 — pilot batch (Blau-mined note + gloss entries).

Five hand-curated picks from data/_blau_saadia_candidates.json:
  - 1 NOTE entry: blau_id 14560 (جسس → גסס, Gen 31:34) — calibration exemplar.
    Hebrew Pi'el גישש shapes Saadia's choice of Arabic Form II جسّس instead
    of the more idiomatic Form V تجسّس. Blau-direct.
  - 3 GLOSS entries:
      * blau_id 14492 (بجريرة → בגרירה, Gen 12:13) — JA preposition for "because of"
      * blau_id 14513 (جررة → גרז, Gen 37:7) — non-cognate rendering of Hebrew אלומה
      * blau_id 14557 (جساسة → גסאסה, Gen 42:30) — abstract noun for "espionage"
  - 1 SKIP (logged in data/_blau_saadia_deferred.json): blau_id 14600
    (إجماع), non-Tafsir Geniza usage throughout Blau's senses.

Mirrors the apply-script shape of scripts/apply_round7_I_chunk1.py:422-469
but targets data/tafsir-divergence.json (DivergenceEntry schema — no `id`
field; dedupe on `lemma_ja`).

Idempotent against re-runs: skips entries whose lemma_ja is already present.
"""

import json
import pathlib
import sys


NEW_ENTRIES = [
    # ---- NOTE — Gen 31:34, Laban gropes Rachel's tent ----------------------
    {
        "lemma_ja": "גסס",
        "variants": ["פגסס"],
        "lemma_ar": "جسّس",
        "root": "ج-س-س",
        "tier": "note",
        "classical_en": "Form V تجسّس, the idiomatic Arabic verb for tactile groping",
        "classical_he": "תְּגַסַּס בבניין החמישי, הוא הפועל הערבי הרגיל לְמִשּׁוּשׁ",
        "saadia_en": "Form II جسّس, mirroring Hebrew Pi'el גישש",
        "saadia_he": "ג'סס בבניין השני, מקבילה מורפולוגית לפיעל העברי גישש",
        "mechanism": "Saadia chooses Arabic Form II (geminate-doubled root) over the more idiomatic Form V; the choice tracks the Hebrew Pi'el verb גישש morphologically, which Blau reads as the Hebrew form shaping the Arabic morphological selection.",
        "verses": [{"book": "Bereshit", "ch": 31, "v": 34}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "جسس",
            "sense": "Form II جسّس 'to grope, to feel' — Blau records that bringing the verb from non-Jewish sources weakens any hypothesis of direct Hebrew גישש influence, but the Form II pairing with Hebrew Pi'el is itself the marked feature. Cited on Gen 31:34 and (groping prophecy) Deut 28:29 / Isa 59:10.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 12:13, Avraham's "say you are my sister" --------------
    {
        "lemma_ja": "גרירה",
        "variants": ["בגרירתך", "גרירתך"],
        "lemma_ar": "جريرة",
        "root": "ج-ر-ر",
        "tier": "gloss",
        "classical_en": "for your sake, on your account",
        "classical_he": "בְּגְלָלֵךְ",
        "saadia_en": "on your account",
        "saadia_he": "בגללך, על-ידך",
        "mechanism": "JA preposition بـ + جريرة 'on account of'; Saadia renders the Hebrew idiomatic בִּגְלָלֵךְ with a non-cognate Arabic phrasing Blau treats as standard medieval JA usage.",
        "verses": [{"book": "Bereshit", "ch": 12, "v": 13}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "جرر",
            "sense": "بجريرة 'because of, on account of' — Blau attests citing Saadia on Gen 12:13 directly (compare من جريرة in the same construction).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 37:7, Joseph's dream of sheaves -----------------------
    {
        "lemma_ja": "גרז",
        "variants": ["גרזא", "גרזתי", "גרזכם", "נגרז"],
        "lemma_ar": "جرز",
        "root": "ج-ر-ز",
        "tier": "gloss",
        "classical_en": "sheaves of grain, bundles bound after reaping",
        "classical_he": "אֲלֻמִּים",
        "saadia_en": "sheaves",
        "saadia_he": "אלומות, עמרים",
        "mechanism": "Non-cognate dialectal pairing: Saadia uses Arabic root ج-ر-ز for Hebrew אלומה rather than the better-known Arabic حزمة; Blau treats the lemma جزّزة under root جرز.",
        "verses": [{"book": "Bereshit", "ch": 37, "v": 7}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "جرز",
            "sense": "جزّزة (related to جرز) 'sheaf, bundle' — Blau attests citing Saadia on Gen 37:7 ('מאלמים אלימים' = נגרז גרזא); compare Saadia on Ps 126:6 'נושא אלמתיו' = ויחמל גרזה.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 42:30, Joseph's brothers reported as spies ------------
    {
        "lemma_ja": "גסאסה",
        "variants": ["בגסאסה"],
        "lemma_ar": "جساسة",
        "root": "ج-س-س",
        "tier": "gloss",
        "classical_en": "as espionage, on a spying-mission",
        "classical_he": "כִּמְרַגְּלִים",
        "saadia_en": "as espionage",
        "saadia_he": "בריגול, כמרגלים",
        "mechanism": "Saadia recasts the Hebrew predicate-noun idiom כִּמְרַגְּלִים ('as spies') with an Arabic abstract verbal-noun construction بـ + جساسة ('in espionage'). The lemma is a regularly-formed Form-I action noun.",
        "verses": [{"book": "Bereshit", "ch": 42, "v": 30}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "جسس",
            "sense": "جساسة 'espionage' — Blau attests citing Saadia on Gen 42:30 directly ('כי אתנו כמרגלים את הארץ' = ואתהמונא בגסאסה אלבלד).",
            "relation": "direct",
        },
    },
]


def main():
    path = pathlib.Path("data/tafsir-divergence.json")
    if not path.exists():
        print(f"FATAL: {path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    payload = json.loads(path.read_text())

    existing_lemmas = {e["lemma_ja"] for e in payload["entries"]}
    added = 0
    skipped = []
    for entry in NEW_ENTRIES:
        if entry["lemma_ja"] in existing_lemmas:
            skipped.append((entry["lemma_ja"], "lemma already present"))
            continue
        payload["entries"].append(entry)
        existing_lemmas.add(entry["lemma_ja"])
        added += 1

    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(path.read_text())  # sanity round-trip

    print(f"Added {added} entries to {path}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    # Per-tier breakdown
    from collections import Counter
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")


if __name__ == "__main__":
    main()

"""
Phase 4 — Bereshit Batch 3.

Three entries surfaced by deeper triage of the "no detected verse ref"
pool (166 candidates). The technique: index 2-3 word Hebrew n-grams
across all Bereshit Tafsir files, then scan candidate body_excerpts +
saadia_citation_lines for embedded biblical phrases and reverse-look-up
which verse they came from. Of 19 anchored candidates, 3 survived
hand-verification against the Tafsir verse text.

Tier breakdown:
  - 1 NOTE  — Saadia makes explicit the implicit subject
  - 2 GLOSS — JA preposition + high-register noun

Apply pattern mirrors batches 1-2.
"""

import json
import pathlib
import sys
from collections import Counter


NEW_ENTRIES = [
    # ---- NOTE — Gen 31:37: Jacob's complaint to Laban (the swap) -----------
    {
        "lemma_ja": "אלבד'ל",
        "variants": ["בד'ל", "באלבד'ל"],
        "lemma_ar": "البَدَل",
        "root": "ب-د-ل",
        "tier": "note",
        "classical_en": "Hebrew וְיוֹכִיחוּ בֵּין שְׁנֵינוּ — 'let them decide between us' (subject unspecified)",
        "classical_he": "וְיוֹכִיחוּ בֵּינֵינוּ — קריאה משפטית סתמית, ללא נושא מפורש",
        "saadia_en": "Saadia names the disputed object — 'let them judge between us about the swap (אלבד'ל)' — the alleged misappropriation",
        "saadia_he": "רס״ג מפרש את נושא ההכרעה: שיכריעו בינינו על החליפין/הגניבה",
        "mechanism": "The Hebrew verse leaves the matter to be adjudicated implicit; Saadia supplies it. 'אלבד'ל' (the swap, the exchange) names the specific dispute — Laban's accusation that Jacob took his household gods. Saadia turns a generic juridical formula into a pointed reference to the underlying property claim.",
        "verses": [{"book": "Bereshit", "ch": 31, "v": 37}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "بدل",
            "sense": "بدل 'exchange, swap, substitute' — Blau records the JA usage of بدل as a substantive for an exchange or substitution; here Saadia uses it to name the matter Laban wants adjudicated.",
            "relation": "adjacent",
        },
    },
    # ---- GLOSS — Gen 19:8: Lot pleading with the men of Sodom -------------
    {
        "lemma_ja": "עדא",
        "variants": [],
        "lemma_ar": "عدا",
        "root": "ع-د-و",
        "tier": "gloss",
        "classical_en": "except (for), but for — JA preposition rendering biblical רַק",
        "classical_he": "מלבד, חוץ מ-, אבל ל-",
        "saadia_en": "except for",
        "saadia_he": "מלבד, רק",
        "mechanism": "Standard JA preposition: عدا renders biblical-Hebrew רַק in the 'only, except' sense; Blau records the equivalence (with a note that the form blends عداه and فضلاً عنه).",
        "verses": [{"book": "Bereshit", "ch": 19, "v": 8}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "عدو",
            "sense": "عدا 'except (for), but (for)' — Blau attests citing Saadia on Gen 19:8 ('רק לאנשים האל אל תעשו' = עדא בהולאי אלקום לא תצנעו).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 15:17: the smoking furnace and flaming torch ---------
    {
        "lemma_ja": "פליל",
        "variants": ["אלפליל", "פלאיל"],
        "lemma_ar": "فليل",
        "root": "ف-ل-ل",
        "tier": "gloss",
        "classical_en": "torch (high-register Arabic synonym for the common مشعل / شعلة)",
        "classical_he": "לַפִּיד",
        "saadia_en": "torch",
        "saadia_he": "לפיד",
        "mechanism": "High-register noun choice: Saadia preserves the biblical-Hebrew register of לַפִּיד (rare, elevated) by reaching for Arabic فليل rather than the prosaic مشعل; Blau records the equivalence with plural فلائل.",
        "verses": [{"book": "Bereshit", "ch": 15, "v": 17}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "فلل",
            "sense": "فليل (pl. فلائل) 'torch' — Blau attests citing Saadia on Gen 15:17 ('ולפיד אש' = ופליל נאר) and the parallel rendering of לפידים at Ex 20:18.",
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
    json.loads(path.read_text())

    print(f"Added {added} entries to {path}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")


if __name__ == "__main__":
    main()

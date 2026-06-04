"""
Phase 4 — Bereshit Batch 2.

Four hand-curated entries from the verse-anchored remainder of
data/_blau_saadia_candidates.json after pilot + batch 1.

Tier breakdown:
  - 3 NOTE   — interpretive semantic shifts
  - 1 GLOSS  — JA prepositional usage

Stopping note (see PHASE4_BERESHIT_SESSION_NOTES.md): the candidate
pool's verse-anchored yield drops sharply after batch 1 — most of the
remaining 200+ rows are page-line refs to Saadia's commentary footnotes,
not verse-grounded JA renderings. Realistic ceiling for first-pass clean
mining is ~25-35 entries (vs the original 80-100 target). The harder
batches require deeper triage of the "no detected verse ref" pool — a
separate sub-task.

Apply pattern mirrors batch 1.
"""

import json
import pathlib
import sys
from collections import Counter


NEW_ENTRIES = [
    # ---- NOTE — Gen 18:27: Abraham's "I am dust and ashes" -----------------
    {
        "lemma_ja": "אמענת",
        "variants": ["אמען", "ימען", "תמען", "אמעאן"],
        "lemma_ar": "أمعنتُ",
        "root": "م-ع-ن",
        "tier": "note",
        "classical_en": "Hebrew הוֹאַלְתִּי — 'I have undertaken / been so bold as to (speak)'",
        "classical_he": "הוֹאַלְתִּי בלשון העברית — 'נטלתי על עצמי, ערבתי את לבי לדבר'",
        "saadia_en": "Form IV أمعن — 'I have persisted / gone deep' in speaking",
        "saadia_he": "אמען בבניין הרביעי — 'התעמקתי, הִתְמַדְתִּי' בדיבור",
        "mechanism": "Saadia reads Abraham's diplomatic apology not as 'I dared to speak' (the volitional Hebrew הואלתי) but as 'I have persisted / gone in deep' (the intensive Arabic أمعن في الكلام). The shift moves Abraham's posture from boldness to persistence — closer to the rabbinic gloss of his repeated mercy-pleas.",
        "verses": [{"book": "Bereshit", "ch": 18, "v": 27}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "معن",
            "sense": "Form IV أمعن في 'to persist deep in, to go far in (an action)' — Blau records the JA usage citing Saadia on Gen 18:27 ('הואלתי לדבר' = אמענת פי אלכלאם).",
            "relation": "direct",
        },
    },
    # ---- NOTE — Gen 49:3: Reuven, "first of my strength" -------------------
    {
        "lemma_ja": "נילי",
        "variants": ["ניל", "ננאל", "ינאל"],
        "lemma_ar": "نَيلي",
        "root": "ن-ي-ل",
        "tier": "note",
        "classical_en": "Hebrew אוֹנ — 'virility, generative power' (the procreative reading)",
        "classical_he": "אוֹן בלשון העברית — 'כוח גברי, כוח הזרע'",
        "saadia_en": "Arabic نيل — 'acquisition, gain' (the economic-status reading)",
        "saadia_he": "ניל בלשון הערבית — 'השגה, רווח, קניין' — קריאה כלכלית-מעמדית",
        "mechanism": "Saadia recasts the biblical-Hebrew אוֹנ — usually read as generative strength — as Arabic نَيل ('what one gains, one's acquisition'). Jacob's blessing of Reuven shifts from a statement about virility to a statement about firstborn-economic priority. Blau treats the rendering under root نيل alongside the parallel נילי 'my gain'.",
        "verses": [{"book": "Bereshit", "ch": 49, "v": 3}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "نيل",
            "sense": "نَيل 'acquisition, gain' — Blau attests citing Saadia on Gen 49:3 ('כחי וראשית אוני' = וקותי ואוול נילי).",
            "relation": "direct",
        },
    },
    # ---- NOTE — Gen 30:13: Leah names Asher ("happy am I") -----------------
    {
        "lemma_ja": "וצפי",
        "variants": ["יצפני", "וצף", "אלוצף"],
        "lemma_ar": "وصفي",
        "root": "و-ص-ف",
        "tier": "note",
        "classical_en": "Hebrew אֹשֶׁר / אִשֵּׁר — 'happiness' / 'to call happy, congratulate'",
        "classical_he": "אֹשֶׁר ואִשֵּׁר בלשון המקרא — 'אושר' ו'לקרוא מאושר'",
        "saadia_en": "Arabic وصف — 'description, characterization' / Form I 'to describe, characterize (favorably)'",
        "saadia_he": "וצף בלשון הערבית — 'תיאור (לשבח)' ו'לתאר, לפאר'",
        "mechanism": "Saadia renders Leah's word-play אִשְּׁרוּנִי בָּנוֹת ('daughters have called me happy') with a verb of public characterization יצפני אלנסא ('women will describe/characterize me [favorably]'). The shift moves the inner state (happiness) outward into reputation — Asher as 'the one I am praised for'.",
        "verses": [{"book": "Bereshit", "ch": 30, "v": 13}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "وصف",
            "sense": "وصف Form I 'to describe, characterize, extol' — Blau attests in the laudatory sense citing Saadia on Gen 30:13 ('באשרי כי אשרוני' = מן וצפי אן יצפני).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 37:22: Reuven's plan to save Joseph -------------------
    {
        "lemma_ja": "לקבל",
        "variants": [],
        "lemma_ar": "لقِبَل",
        "root": "ق-ب-ل",
        "tier": "gloss",
        "classical_en": "for the purpose of, in order that — JA equivalent of Hebrew לְמַעַן",
        "classical_he": "לְמַעַן, על מנת ש- (תרגום ערבי-יהודי קבוע)",
        "saadia_en": "in order that",
        "saadia_he": "לְמַעַן, כדי ש-",
        "mechanism": "Standard JA prepositional phrase: لـِ + قِبَل ('toward the matter that') renders biblical לְמַעַן (purpose); Blau notes the systematic equivalence.",
        "verses": [{"book": "Bereshit", "ch": 37, "v": 22}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "قبل",
            "sense": "لقِبَل 'for the sake of, in order that' — Blau notes Saadia regularly renders biblical לְמַעַן with this JA phrase, citing Gen 37:22.",
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

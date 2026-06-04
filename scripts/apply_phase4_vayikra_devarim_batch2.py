"""
Phase 4 Vayikra/Devarim Batch 2 — apply 1 net-new NOTE entry to
data/tafsir-divergence.json, and mark the Phase 3 R2 Batch 1 חאכם skip
record RESOLVED in data/_blau_saadia_deferred.json.

Window
------
- Source: the 9 bare-noun judicial hits logged at
  data/_blau_saadia_deferred.json#/phase3_r2/batch1/skip (lemma חאכם):
    Shemot 21:6, 22:7, 22:8; Devarim 17:9, 17:12, 21:19, 22:15, 25:2, 25:7.
- All 9 Saadia surface forms were read directly from
  data/tafsir-{book}-{ch}.json during planning and confirmed bare-noun
  judicial (not the divine-speech-act participle of the חאכמא TWIST).

Triage outcome
--------------
NEW ENTRY — 1 NOTE:
  - NOTE אלחאכם  Ex 21:6, 22:7, 22:8 + Deut 17:9, 17:12, 21:19, 22:15, 25:2,
                25:7 — Saadia collapses three distinct Heb judicial terms
                (הָאֱלֹהִים / הַשֹּׁפֵט / הַשַּׁעַר) onto the single bare noun
                אלחאכם "(the) judge". Distinct register from the חאכמא TWIST
                (circumstantial-accusative participle حاكمًا inserted into
                divine speech-acts).

Blau sourcing decision
----------------------
sources = [lane, saadia-direct, blau-dict], blau_dict.relation = "adjacent".
Blau's חכם entry attests the judicial VERB (Form III "שפט, דן / to judge" +
the legal "to sue / summon to lawsuit") but gives the bare-noun substantive
حاكم "(the) judge" no separate headword. That noun is the classical
agent-noun of the verb Blau glosses (Lane, s.v. حكم). We mirror the sibling
חאכמא TWIST, which cites blau-dict at relation="adjacent" for the same root,
and state the verb-vs-noun distinction honestly in blau_dict.sense.
(Confirmed in planning via the arabic-lexicon skill, slug blau-judeoarabic:
no bare-noun حاكم headword; only the verb senses.)

Apply pattern
-------------
- Mirrors scripts/apply_phase4_devarim_batch1.py: NEW_ENTRIES append by
  lemma_ja uniqueness, write-back via
  json.dumps(..., ensure_ascii=False, indent=2) + "\n" then re-parse.
- _mark_resolved() stamps status + resolution onto the existing חאכם skip
  record (kept as audit trail, not deleted). Idempotent on re-run.
"""

import json
import pathlib
import sys
from collections import Counter

RESOLVED_DATE = "2026-05-30"

# ============================================================================
# NEW ENTRIES
# ============================================================================

NEW_ENTRIES = [
    # ---- NOTE — Ex 21:6, 22:7-8 + Deut 17:9/12, 21:19, 22:15, 25:2/7 -------
    {
        "lemma_ja": "אלחאכם",
        "variants": ["חאכם", "אלחאכם"],
        "lemma_ar": "الحاكم",
        "root": "ح-ك-م",
        "tier": "note",
        "classical_en": "حاكم — the active participle of حكم 'to judge, to govern', used as a substantive: 'judge, ruler, arbitrator', the one who decides between disputants. The definite الحاكم is the standard administrative-judicial noun for '(the) judge' in legal-procedural Arabic.",
        "classical_he": "حاكم — בינוני הפועל של حكم ('לשפוט, למשול'), בשימוש כשם עצם: 'שופט, מושל, פוסק', מי שמכריע בין בעלי הדין. הצורה המיודעת الحاكم היא שם העצם המנהלי-משפטי הסטנדרטי ל'(ה)שופט' בלשון הדיון המשפטי.",
        "saadia_en": "the judge — Saadia routes the entire judicial-administrative apparatus through the single bare noun אלחאכם, collapsing three distinct Hebrew terms (הָאֱלֹהִים, הַשֹּׁפֵט, הַשַּׁעַר) onto one Arabic substantive.",
        "saadia_he": "השופט — סעדיה ממיר את כל המנגנון המשפטי-מנהלי באמצעות שם העצם הבודד אלחאכם, וממזג שלושה מונחים עבריים שונים (הָאֱלֹהִים, הַשֹּׁפֵט, הַשַּׁעַר) לכלל שם עצם ערבי אחד.",
        "mechanism": "Lexical systematization of the judicial-administrative vocabulary onto a single bare substantive across two books. Saadia routes three distinct Hebrew judicial terms through the one Arabic noun אלחאכם ('the judge'): (1) הָאֱלֹהִים at Shemot 21:6 ('וְהִגִּישׁוֹ אֲדֹנָיו אֶל-הָאֱלֹהִים' = פליקדמה מולאה אלי' אלחאכם — 'his master shall bring him to the judge'), 22:7 ('וְנִקְרַב בַּעַל-הַבַּיִת אֶל-הָאֱלֹהִים' = תקדם מולא אלמנזל אלי' אלחאכם) and 22:8 ('עַד הָאֱלֹהִים יָבֹא דְּבַר-שְׁנֵיהֶם ... אֲשֶׁר יַרְשִׁיעֻן אֱלֹהִים' = פאלי' אלחאכם ירפע אמרהמא ... פמן צ'למה אלחאכם) — the famous elohim-as-judges passages, where rendering 'God / the elohim' as 'the judge' adopts the rabbinic-juridical reading AND is anti-anthropomorphic-adjacent (the litigation venue is the human judge, not the deity); (2) הַשֹּׁפֵט, the direct judicial-official term, at Devarim 17:9 ('וְאֶל-הַשֹּׁפֵט' = ואלי' אלחאכם), 17:12 ('אוֹ אֶל-הַשֹּׁפֵט' = או מן אלחאכם) and 25:2 ('וְהִפִּילוֹ הַשֹּׁפֵט' = פליבסטה אלחאכם); (3) הַשַּׁעַר / הַשָּׁעְרָה, the city gate — the biblical judicial venue — at Devarim 21:19 ('וְאֶל-שַׁעַר מְקֹמוֹ' = ואלי' באב חאכם מוצ'עה), 22:15 ('אֶל-זִקְנֵי הָעִיר הַשָּׁעְרָה' = אלי' באב אלחאכם) and 25:7 ('וְעָלְתָה יְבִמְתּוֹ הַשַּׁעְרָה' = פלתצעד אלי' באב אלחאכם), where Saadia renders 'the gate' as באב אלחאכם 'the gate of the judge', making the gate's juridical function lexically explicit. The cross-attestation across Ex 21-22 and Deut 17/21/22/25 shows this is a programmatic register-choice, not per-verse improvisation. CRITICAL register-distinction: this bare-noun judicial אלחאכם is structurally distinct from the חאכמא TWIST. The TWIST is the circumstantial-accusative participle حاكمًا that Saadia INSERTS into divine speech-acts (Bereshit 1:22, Shemot 2:14/22:27, Vayikra 20:24) to avoid anthropomorphism — a syntactic deployment in divine-speech. This NOTE is the ordinary substantive for human judicial officials in legal-procedural narrative (see the Phase 4 Devarim B1 session notes, the explicit register-distinction at lines 158-160). Same root ح-ك-م, opposite move: the TWIST adds a participle to elevate divine 'speaking' into 'decreeing'; the NOTE flattens varied Hebrew judicial nouns down to one administrative substantive. Pedagogically distinctive because it exhibits Saadia's management of the whole judicial-administrative lexical field through a single Arabic anchor.",
        "verses": [
            {"book": "Shemot", "ch": 21, "v": 6},
            {"book": "Shemot", "ch": 22, "v": 7},
            {"book": "Shemot", "ch": 22, "v": 8},
            {"book": "Devarim", "ch": 17, "v": 9},
            {"book": "Devarim", "ch": 17, "v": 12},
            {"book": "Devarim", "ch": 21, "v": 19},
            {"book": "Devarim", "ch": 22, "v": 15},
            {"book": "Devarim", "ch": 25, "v": 2},
            {"book": "Devarim", "ch": 25, "v": 7},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "حكم",
            "sense": "Blau (Dict. of Medieval Judaeo-Arabic Texts, s.v. חכם) attests the judicial VERB — Form III 'to judge / שפט, דן' (Pirqei Avot: אלחק ... יחאכם אל ללאיק עלא חסב אפעאלהם) and the legal 'to sue / summon to lawsuit' (אחכמנאה ואשלצנאה) — but does not give the bare-noun substantive حاكم '(the) judge' a separate headword; that noun is the classical agent-noun of the verb Blau glosses (Lane, s.v. حكم: active participle 'judge, ruler, arbitrator'). The divergence catalogued here is Saadia's systematic collapse of three Hebrew judicial terms (הָאֱלֹהִים / הַשֹּׁפֵט / הַשַּׁעַר) onto this one substantive across Shemot 21-22 and Devarim 17/21/22/25. Distinct register from the inserted circumstantial-accusative participle حاكمًا of the חאכמא TWIST entry.",
            "relation": "adjacent",
        },
    },
]


# ============================================================================
# Helpers
# ============================================================================

def _mark_resolved(deferred_path: pathlib.Path) -> dict:
    """Stamp status + resolution onto the existing חאכם skip record in
    data/_blau_saadia_deferred.json#/phase3_r2/batch1/skip. Kept as audit
    trail (not deleted). Idempotent on re-run.
    """
    payload = json.loads(deferred_path.read_text())
    skip = (
        payload.get("phase3_r2", {})
        .get("batch1", {})
        .get("skip", [])
    )
    resolution = (
        "Shipped as NOTE אלחאכם via apply_phase4_vayikra_devarim_batch2.py: "
        "9 bare-noun judicial verses (Ex 21:6, 22:7, 22:8; Deut 17:9, 17:12, "
        "21:19, 22:15, 25:2, 25:7) covering Saadia's collapse of three Hebrew "
        "judicial terms (הָאֱלֹהִים / הַשֹּׁפֵט / הַשַּׁעַר) onto the single "
        "Arabic noun אלחאכם. sources=[lane, saadia-direct, blau-dict] "
        "(relation=adjacent — Blau attests the judicial verb, not the bare "
        "noun; mirrors the חאכמא TWIST). Distinct register from the divine-"
        "speech-act participle of the חאכמא TWIST."
    )
    found = False
    for rec in skip:
        if isinstance(rec, dict) and rec.get("lemma") == "חאכם":
            rec["status"] = f"RESOLVED {RESOLVED_DATE}"
            rec["resolution"] = resolution
            found = True
            break
    if found:
        deferred_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        )
        json.loads(deferred_path.read_text())  # parse-check
    return {"חאכם_skip_resolved": found}


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    div_path = root / "data" / "tafsir-divergence.json"
    deferred_path = root / "data" / "_blau_saadia_deferred.json"

    if not div_path.exists():
        print(f"FATAL: {div_path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    if not deferred_path.exists():
        print(f"FATAL: {deferred_path} not found", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(div_path.read_text())

    # Append new entries by lemma_ja uniqueness.
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

    div_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(div_path.read_text())  # parse-check

    deferred_summary = _mark_resolved(deferred_path)

    print(f"Added {added} entries to {div_path.name}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")
    print(f"Deferred file summary: {json.dumps(deferred_summary, ensure_ascii=False)}")


if __name__ == "__main__":
    main()

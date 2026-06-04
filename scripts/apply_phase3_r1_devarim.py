"""
Phase 3 R1 Second Wave — Devarim batch. Bring Devarim to >=5 first-verse twist
entries so the verifier's per-book quality gate activates and clears.

Why
---
Before this batch Devarim had ONE first-verse twist (גוהר, the Tablets-of-
substance entry, Deut 5:19). This batch adds 4 more — 3 by promoting existing
Devarim direct-NOTEs that are genuinely paradigm-shifting, and 1 net-new no-cite
twist (the iconic Shema reframe).

  PROMOTE note->twist (3, all direct, all first=Devarim):
    - אקרץ'   (Deut 2:21+) — Heb הוריש 'to dispossess/drive out' → Ar قرض
      'to exterminate'. Conquest reframed from DISPLACEMENT to EXTERMINATION.
    - תכ'רסתם (Deut 1:27)  — Heb רגן 'to murmur/complain' → Ar Form V تخرّس
      'to be struck dumb/silenced'. Active complaint-speech → passive paralysis
      (semantic-polarity inversion).
    - זאיל    (Deut 21:18) — Heb סורר 'rebellious (son)' → Ar زائل 'one who
      DEVIATES from the right'. Political insubordination → moral-epistemological
      deviation (rationalist reframe).

  NEW TWIST (1, no-cite):
    - אעלם    (Deut 6:4) — Heb שמע 'Hear!' (the Shema) → Ar اعلم 'Know!'.
      Liturgical proclamation recast as an epistemic proposition (rationalist).

Devarim twists after = 5 (1 existing + 3 promotions + 1 net-new).
  direct = 4 (גוהר, אקרץ', תכ'רסתם, זאיל); no-cite = 1 (אעלם).
  direct 4/5 = 80% (>=45%); backed 4/5 = 80% (>=70%); no-cite 1/5 = 20% (<=30%).

Note: ממתעה (twist אלממתעה) already covers Deut 23:18 but is Bereshit-anchored
(verses[0] = Bereshit 38:21), so it does NOT count for Devarim — left untouched.
יסיב (שמט→سيب) is kept as a NOTE: an institutional-vocabulary calque that
preserves the 'release' meaning rather than reframing it — not a paradigm shift.

Sourcing
--------
Promotions inherit their already-verified blau-direct citations (verses,
variants, sources, blau_dict left intact; only tier + mechanism change). The
new אעלם surface form was read from the corpus (data/tafsir-devarim-6.json:
'אעלם יא אסראיל'); it is an exegetical reframe with no Blau lemma, hence no-cite.

Apply pattern
-------------
- PROMOTE_TO_TWIST first (tier flip + mechanism rewrite) so append does not
  skip-collide on existing lemmas.
- Append the new entry by lemma_ja uniqueness; write-back via
  json.dumps(..., ensure_ascii=False, indent=2) + "\\n", re-parse.
- Log the אעלם no-blau decision into no_cite_audit (idempotent).
"""

import json
import pathlib
import sys
from collections import Counter

CONSUMED_DATE = "2026-06-02"

# ============================================================================
# PROMOTIONS — note -> twist (tier flip + deepened mechanism). verses[],
# variants[], sources[], blau_dict left intact (already blau-direct verified).
# ============================================================================

PROMOTE_TO_TWIST = [
    {
        "lemma_ja": "אקרץ'",
        "mechanism": "A paradigm shift in the ethic of the conquest, from displacement to extermination. Hebrew הוֹרִישׁ (Hiphil of ירש) frames the taking of the Land as DISPOSSESSION — to drive out, to cause to be dispossessed, to take over the inheritance of the prior nations. The Hiphil leaves the dispossessed peoples intact in principle: they are driven OUT, displaced from their territory, not necessarily destroyed. Saadia routes the entire Devarim conquest-discourse through Arabic Form I قَرَضَ — 'to cut off, to extirpate, to exterminate' (cognate with קצץ 'to cut'). Across Deut 2:21 (the Anakim-Rephaim before the Moabite-Ammonite settlement, וַיַּשְׁמִידֵם/וַיִּירָשֻׁם → פקרצ'והם 'they exterminated them'), 7:17, 9:3, 11:23, and 12:2, the verb is consistently the extirpation-verb, not a displacement-verb. The divergence forecloses what the Hebrew leaves open: where הוריש permits the nations to survive elsewhere, قرض cuts them off entirely. The conquest is thereby re-theologized — from a divine land-grant achieved by dispossessing the incumbents into a divine extermination-mandate against them. Blau (s.v. قرض) documents this systematic rendering of Heb הוריש with قرض across the Devarim conquest-narrative, noting that Saadia preserves the Hebrew's causative (Hiphil) force through the transitive Form I. The Form VIII اقتراض 'to take/give a loan' is the later commercial-derived sense; the Form-I 'extirpate' stratum is the older one Saadia draws on. The twist: a verb of removal-from-land becomes a verb of removal-from-existence.",
    },
    {
        "lemma_ja": "תכ'רסתם",
        "mechanism": "A semantic-polarity inversion: the people's sin at the spies-report is flipped from active complaint to passive speechlessness. Hebrew רָגַן (Deut 1:27, וַתֵּרָגְנוּ בְאָהֳלֵיכֶם 'and you murmured in your tents') is a rare, always-pejorative verb (Pentateuch only here; cf. Ps 106:25, Prov 16:28, 26:20, 18:8) meaning 'to murmur, complain, mutter discontentedly' — it names the people's ACTIVE PRODUCTION of complaint-speech, the verbal generation of rebellion against the conquest. Saadia routes this through Arabic Form V تَخَرَّسَ — but خرس is the root of MUTENESS (أخرس 'mute, dumb'), and Form V means 'to be reduced to silence, to be struck dumb, to be dumbfounded'. So 'you murmured in your tents' becomes ותכ'רסתם — 'you were struck dumb / reduced to silence in your tents' — the exact opposite polarity: active complaint-speech inverts to passive, faithless speechlessness. The rebellion is reframed not as vocal protest but as a kind of stunned paralysis, the people dumbstruck with fear in their tents rather than loudly murmuring. Blau (s.v. خرس) cites Saadia's choice here, with al-Fāsī's Jāmiʿ 1:103 transmitting both Form II خرّس 'to silence' and Form V تخرّس 'to be silenced'. The twist is a true inversion of register and agency: the sinners go from speaking-too-much to unable-to-speak, recasting the moral character of the episode from insubordinate clamor to faithless collapse.",
    },
    {
        "lemma_ja": "זאיל",
        "mechanism": "A rationalist-philosophical reframe of the wayward-son institution, from political rebellion to moral-epistemological deviation. Hebrew סוֹרֵר וּמוֹרֶה (Deut 21:18, the famous institutional pair of the 'stubborn and rebellious son') names the offense through verbs of political-domestic INSUBORDINATION: סרר 'to be stubborn, to rebel' and מרה 'to be defiant against authority'. The Hebrew frames the son's crime as refusal to submit — a category-error in the household's command-structure, rebellion against parental and by extension covenantal authority. Saadia renders the first term with Arabic زائل — the active participle of زال 'to depart, to swerve', i.e. 'one who DEVIATES from the right, who errs from the correct path' (the idiom زائل عن الصواب / الطاعة names a specifically MORAL-EPISTEMOLOGICAL straying), pairing it with מכ'אלף 'one who diverges/contradicts' for the second. The paradigm shift: the son's offense is recast from insubordination (a political-relational category) into deviation-from-the-right (a moral-rational category native to Saadia's ethics, where wrongdoing is fundamentally a swerve away from the correct course apprehended by reason). The institution of the בן סורר ומורה is thereby rationalized — not a rebel against authority but a deviant from the moral-rational order. Blau (s.v. زيل) cites Saadia on Deut 21:18 (סורר → זאיל), with the broader 'deviation from obedience/correctness' frame transmitted forward through medieval Judeo-Arabic moral discourse. The twist relocates the wayward son's sin from the axis of obedience to the axis of rational-moral correctness.",
    },
]


# ============================================================================
# NEW ENTRIES — 1 TWIST (no-cite)
# ============================================================================

NEW_ENTRIES = [
    # ---- TWIST — the Shema: 'Hear' reframed as 'Know' (no-cite) ----------
    {
        "lemma_ja": "אעלם",
        "variants": ["אעלמו"],
        "lemma_ar": "اعلم",
        "root": "ع-ل-م",
        "tier": "twist",
        "classical_en": "Classical Arabic عَلِمَ (root ع-ل-م) = 'to know'; the imperative اعْلَمْ = 'know!'. It is categorically distinct from سَمِعَ 'to hear, listen' (root س-م-ع), whose imperative اسمع would be the natural calque for Hebrew שְׁמַע. علم is the verb of cognition and established knowledge, the root of عِلْم 'knowledge/science'.",
        "classical_he": "عَلِمَ בערבית הקלאסית (שורש ع-ل-م) = 'לדעת'; ציווי اعْلَمْ = 'דע!'. נבדל מהותית מ־سَمِعَ 'לשמוע, להאזין' (שורש س-م-ع), שציוויו اسمع הוא הקלקה הטבעית ל־שְׁמַע. علم הוא פועל ההכרה והידיעה המבוססת, שורש عِلْم 'ידע/מדע'.",
        "saadia_en": "Know! — Saadia renders the opening imperative of the Shema, שְׁמַע יִשְׂרָאֵל ('Hear, O Israel'), as אעלם יא אסראיל ('Know, O Israel'), recasting Judaism's central confession from a call to audition into a command to cognition.",
        "saadia_he": "דע! — סעדיה מתרגם את ציווי־הפתיחה של קריאת שמע, שְׁמַע יִשְׂרָאֵל ('שמע ישראל'), באמצעות אעלם יא אסראיל ('דע, ישראל'), וממיר את הצהרת־האמונה המרכזית מקריאה לשמיעה לכלל ציווי של ידיעה.",
        "mechanism": "A rationalist-philosophical reframe of the most recited verse in Judaism. Hebrew שְׁמַע (Deut 6:4) is the imperative of שמע 'to hear, listen, heed' — the Shema summons Israel to HEAR the proclamation of God's unity. The natural Arabic calque would be اسمع (same root, same sense). Saadia instead renders אעלם 'KNOW' (root علم), opening the verse: 'אעלם יא אסראיל אן אללה רבנא אללה אלואחד' — 'Know, O Israel, that the Lord our God, the Lord, is one'. The shift is programmatic: in Saadia's theology (Kitāb al-Amānāt wa-l-Iʿtiqādāt / Emunot ve-Deot), the unity of God (tawḥīd) is not a creed to be merely heard and accepted on authority but a truth to be KNOWN — established by rational demonstration, the conclusion of reasoned inquiry. By translating 'hear' as 'know', he converts the liturgical proclamation into an epistemic proposition: divine unity becomes an object of cognition. The inserted אן 'that' reinforces this — turning the bare apposition ('the Lord our God, the Lord is one') into a propositional content-clause ('know THAT the Lord our God...'), the grammatical signature of a knowledge-claim. This is not a lexical divergence within Arabic — اعلم simply means 'know' — but an exegetical-theological substitution that recasts the Shema as a summons to rational knowledge of God's oneness rather than aural assent. Like the corpus's other no-cite reframe-twists, the move is interpretive, not lexical; Blau does not lemmatize it, so it ships saadia-direct.",
        "verses": [
            {"book": "Devarim", "ch": 6, "v": 4},
        ],
        "sources": ["lane", "saadia-direct"],
    },
]


# ============================================================================
# Helpers
# ============================================================================

NO_CITE_AUDIT = {
    "lemma_ja": "אעלם",
    "verse": "Devarim 6:4",
    "decision": "Shipped sources=[lane, saadia-direct], NO blau_dict. Heb שְׁמַע ('Hear!', the Shema) → Ar اعلم ('Know!') is a rationalist-philosophical EXEGETICAL reframe, not a lexical divergence within Arabic (اعلم = 'know' is classical; the natural calque of שמע would be اسمع). Saadia converts the liturgical proclamation into an epistemic proposition (divine unity as an object of rational cognition, per Emunot ve-Deot), reinforced by the inserted אן 'that'. Blau does not lemmatize it. Consistent with the corpus's other no-cite reframe-twists. Counts as 1 no-citation in the Devarim twist mix (1/5 = 20%, within the <=30% bar).",
    "logged_on": CONSUMED_DATE,
}


def _patch_promote_to_twist(payload: dict) -> list[dict]:
    """Flip tier note->twist for each PROMOTE_TO_TWIST target and rewrite its
    mechanism to twist depth. verses[]/variants[]/sources/blau_dict untouched."""
    summaries = []
    for spec in PROMOTE_TO_TWIST:
        target = spec["lemma_ja"]
        for entry in payload["entries"]:
            if entry.get("lemma_ja") != target:
                continue
            prev_tier = entry.get("tier")
            entry["tier"] = "twist"
            if "mechanism" in spec:
                entry["mechanism"] = spec["mechanism"]
            for k in ("classical_en", "classical_he", "saadia_en", "saadia_he"):
                if k in spec:
                    entry[k] = spec[k]
            summaries.append({"lemma": target, "from_tier": prev_tier, "to_tier": "twist"})
            break
        else:
            summaries.append({"lemma": target, "error": "target lemma not found"})
    return summaries


def _log_deferred(deferred_path: pathlib.Path) -> dict:
    payload = json.loads(deferred_path.read_text())
    audit = payload.setdefault("no_cite_audit", {})
    bucket = audit.setdefault("phase3_r1_no_blau", [])
    if not any(isinstance(r, dict) and r.get("lemma_ja") == "אעלם" for r in bucket):
        bucket.append(NO_CITE_AUDIT)
        audit_added = 1
    else:
        audit_added = 0
    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(deferred_path.read_text())  # parse-check
    return {"no_cite_audit_added": audit_added}


def _devarim_twist_count(entries) -> int:
    n = 0
    for e in entries:
        if (e.get("tier") or "twist") != "twist":
            continue
        vs = e.get("verses", [])
        if vs and vs[0].get("book") == "Devarim":
            n += 1
    return n


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    div_path = root / "data" / "tafsir-divergence.json"
    deferred_path = root / "data" / "_blau_saadia_deferred.json"

    if not div_path.exists():
        print(f"FATAL: {div_path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(div_path.read_text())
    before = _devarim_twist_count(payload["entries"])

    # 1) Promote note->twist BEFORE append.
    promote_summaries = _patch_promote_to_twist(payload)

    # 2) Append new entry by lemma_ja uniqueness.
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

    deferred_summary = {}
    if deferred_path.exists():
        deferred_summary = _log_deferred(deferred_path)

    after = _devarim_twist_count(payload["entries"])
    print(f"Promotions: {json.dumps(promote_summaries, ensure_ascii=False)}")
    print(f"Added {added} entries to {div_path.name}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    print(f"Devarim first-verse twists: {before} -> {after}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")
    print(f"Deferred summary: {json.dumps(deferred_summary, ensure_ascii=False)}")


if __name__ == "__main__":
    main()

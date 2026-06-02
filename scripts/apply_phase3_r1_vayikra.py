"""
Phase 3 R1 Second Wave — Vayikra batch. Add 5 net-new TWIST-tier entries to
data/tafsir-divergence.json, anchored (first verse) in Vayikra, to activate
and clear the verifier's per-book quality gate for Vayikra.

Why
---
The verifier's per-book relation-mix gate activates for a book only once it has
>=5 twist-tier entries (counted by the FIRST verse's book). Before this batch
Vayikra had ZERO first-verse twists (the one twist touching Vayikra — חאכמא —
is anchored in Bereshit 1:22). This batch adds 5 so the gate activates and clears:
  Vayikra twists after = 5 (all net-new).
  direct = 3 (תרפק, פיצ'הא, אלכ'אמע); adjacent = 1 (אלקצבה);
  no-cite = 1 (שיאטין — a demythologizing identification, see below).
  direct 3/5 = 60% (>=45%); backed 4/5 = 80% (>=70%); no-cite 1/5 = 20% (<=30%).

Sourcing
--------
Candidates mined from data/_blau_saadia_candidates.json and VERIFIED against the
Saadia corpus (data/tafsir-vayikra-{ch}.json, fields ch/v/ja/hebrew) — every
surface form below was read from the corpus, not hand-authored. Classical senses
via Lane; Blau senses via the arabic-lexicon skill (slug blau-judeoarabic).

Triage outcome
--------------
NEW ENTRIES — 5 TWIST:
  - TWIST תרפק    Lev 25:3, 25:4 — Heb תִּזְמֹר 'prune' → Ar رفق (Aramaic-driven
                  calque: رفق 'be gentle' loaded with Aramaic רפק 'to dig/prune')
  - TWIST פיצ'הא  Lev 15:28 — Heb זוֹב 'genital flux' → Ar فيضة (Hebrew-driven
                  calque: فيض 'overflow' specialized to pathological discharge)
  - TWIST אלכ'אמע Lev 21:18 — Heb שָׂרוּעַ (priestly blemish) → Ar خامع
                  'dislocated-hip' (vernacular sense, not classical 'to limp')
  - TWIST אלקצבה  Lev 1:8, 1:12, 8:20 — Heb הַפָּדֶר 'the suet' → Ar قصبة
                  'the interior/pluck (liver-lungs-heart)' (anatomical reframe)
  - TWIST שיאטין  Lev 17:7 — Heb שְׂעִירִם 'goat-demons' → Ar الشياطين 'the
                  demons/satans' (demythologizing midrashic identification)

Note on שיאטין (no-citation): the divergence is an EXEGETICAL identification
(Heb שעירים 'hairy goat-demons' → 'demons'), not a lexical shift in Arabic
(شيطان = 'demon' is classical). Blau does not lemmatize it. Shipped as
sources=[lane, saadia-direct] with NO blau_dict, exactly as the existing
demythologizing identification-entries are catalogued (אשראף בני-האלהים→nobility,
קרדא Ararat→Qardū, אתון Ur→furnace — all no-cite). Logged in no_cite_audit.

Apply pattern
-------------
- Mirrors scripts/apply_phase3_r1_shemot.py: append by lemma_ja uniqueness,
  write-back via json.dumps(..., ensure_ascii=False, indent=2) + "\n", re-parse.
- Logs consumed Blau ids into phase3_r1_consumed + the שיאטין no-blau decision
  into no_cite_audit (audit trail; idempotent).
"""

import json
import pathlib
import sys
from collections import Counter

CONSUMED_DATE = "2026-05-30"

# ============================================================================
# NEW ENTRIES — 5 TWIST
# ============================================================================

NEW_ENTRIES = [
    # ---- TWIST — prune (Aramaic-driven calque) ---------------------------
    {
        "lemma_ja": "תרפק",
        "variants": ["ארפק", "רפק", "תרפקה"],
        "lemma_ar": "رفق",
        "root": "ر-ف-ق",
        "tier": "twist",
        "classical_en": "Classical Arabic رَفَقَ (Form I) = 'to be gentle, to treat kindly, to act with gentleness/deliberation'; the noun رِفْق = 'gentleness, kindness, gentle handling'. There is no agricultural sense in classical Arabic — رفق never means 'to prune' or 'to dig'.",
        "classical_he": "רَפَקَ בערבית הקלאסית (בניין I) = 'לנהוג בעדינות, לטפל ברוך, לפעול במתינות'; שם העצם רِفْק = 'עדינות, רכות, טיפול מתון'. אין משמע חקלאי בערבית הקלאסית — رفق לעולם אינו 'לזמור' או 'לחפור'.",
        "saadia_en": "to prune (a vineyard) — Saadia renders Hebrew זָמַר 'to prune' with رفق, importing the Aramaic רְפַק 'to dig/hoe' sense into an Arabic root that classically means only 'to be gentle'.",
        "saadia_he": "לזמור (כרם) — סעדיה מתרגם את זָמַר 'לזמור' באמצעות رفق, ומייבא את משמעות הארמית רְפַק 'לחפור/לעדור' אל שורש ערבי שמשמעו הקלאסי הוא 'לנהוג בעדינות' בלבד.",
        "mechanism": "An Aramaic-driven calque that loads an Arabic 'gentleness' root with an agricultural sense it does not natively have. The Hebrew זָמַר (root ז-מ-ר 'to prune, trim a vine') in the Sabbatical-year law (Lev 25:3-4) names vineyard-pruning. Classical Arabic رفق means 'to be gentle, to handle with care' — never to prune or dig. Saadia chooses رفق anyway (וסת סנין תרפק כרמך 'and six years you shall prune your vineyard', 25:3; ולא תרפק כרמך 'and you shall not prune your vineyard', 25:4) because the Aramaic-Babylonian cognate רְפַק carries the agricultural sense 'to dig, to hoe' — the meaning current in the Aramaic-speaking milieu of the Babylonian academies. Blau records exactly this, glossing the Form I as 'to hoe, to prune' and explicitly flagging the Aramaic רפק 'to dig' substrate, citing Saadia at Lev 25:3. The move is a lexical bridge across THREE languages: a Hebrew agricultural verb rendered by an Arabic root selected for its Aramaic (not Arabic) sense — the Tafsir thinking through the trilingual lexical environment of Geonic Babylonia. Pedagogically distinctive because the divergence is invisible from Arabic alone: only the Aramaic layer explains why a 'gentleness' word means 'prune' here.",
        "verses": [
            {"book": "Vayikra", "ch": 25, "v": 3},
            {"book": "Vayikra", "ch": 25, "v": 4},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "رفق",
            "sense": "Blau (s.v. رفق) glosses the Form I 'to hoe, to prune', noting the Aramaic-Babylonian רְפַק 'to dig' as the source sense and citing Saadia's rendering of Heb זמר at Lev 25:3 (תזמר = תרפק). Classical Arabic رفق means only 'to be gentle'; the agricultural sense is the Aramaic-driven calque catalogued here.",
            "relation": "direct",
        },
    },

    # ---- TWIST — genital flux (Hebrew-driven calque) ---------------------
    {
        "lemma_ja": "פיצ'הא",
        "variants": ["פיצ'", "פיצ'ה", "פיצ'תהא"],
        "lemma_ar": "فيضة",
        "root": "ف-ي-ض",
        "tier": "twist",
        "classical_en": "Classical Arabic فَيْض (root ف-ي-ض) = 'an overflowing, a pouring-forth, abundance, flood' — of water brimming over, of wealth or grace in superabundance (Lane). The semantic field is positive abundance and overflow, with no pathological or genital connotation.",
        "classical_he": "פَيْض בערבית הקלאסית (שורש ف-ي-ض) = 'שפיעה, גלישה, שפע, הצפה' — של מים העולים על גדותיהם, של עושר או חסד בשפע (ליין). השדה הסמנטי הוא שפע חיובי וגלישה, בלא קונוטציה פתולוגית או מינית.",
        "saadia_en": "genital flux / pathological discharge — Saadia renders Hebrew זוֹב (the impurity-law term for an abnormal genital discharge) with فيضة, narrowing the 'overflow' field to a technical purity-law sense.",
        "saadia_he": "זוב / הפרשה פתולוגית — סעדיה מתרגם את זוֹב (מונח דיני־הטומאה להפרשה גופנית חריגה) באמצעות فيضة, ומצמצם את שדה ה'גלישה' למשמע טכני בדיני־טהרה.",
        "mechanism": "A Hebrew-driven specialization that channels a 'positive abundance' root into a clinical purity-law sense. Hebrew זוֹב (from זוּב 'to flow') is the technical term in the impurity laws (Lev 15) for an abnormal genital discharge — the zav/zavah's pathological flow that renders them ritually impure. Classical Arabic فيض / فيضة names overflow and abundance in the POSITIVE register (brimming water, superabundant grace). Saadia bends it to the clinical-pathological sense, rendering מִזּוֹבָהּ 'from her flux' as מן פיצ'הא (Lev 15:28). The move tracks the Hebrew: the root meaning 'to flow' is what links the two languages, and Saadia lets זוב's specific medical-purity sense ride into the Arabic فيضة, which Blau then lemmatizes precisely as 'genital flux, gonorrhea / זוב', citing this verse. The result is a euphemistic-clinical coinage: the same root an Arabic reader associates with overflowing bounty is repurposed as the discreet technical term for the impurity-generating discharge. Pedagogically distinctive because the divergence is a register-collapse — Saadia narrows a broad 'abundance' word to a single pathological referent, driven by the Hebrew source-term's specialized sense.",
        "verses": [
            {"book": "Vayikra", "ch": 15, "v": 28},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "فيض",
            "sense": "Blau (s.v. فيض, headword فيضة) glosses 'genitals; (genital) flux, gonorrhea / זוב', citing Saadia's rendering of Heb זוב at Lev 15:28 (מזובה = מן פיצ'הא). Classical Arabic فيض = 'overflow, abundance'; the pathological purity-law sense is the Hebrew-driven specialization catalogued here.",
            "relation": "direct",
        },
    },

    # ---- TWIST — priestly blemish, vernacular sense ----------------------
    {
        "lemma_ja": "כ'אמע",
        "variants": ["אלכ'אמע", "כ'אמעא"],
        "lemma_ar": "خامع",
        "root": "خ-م-ع",
        "tier": "twist",
        "classical_en": "Classical Arabic خَمَعَ = 'to limp, to walk with a slight lameness' — said especially of the hyena or wolf (Lane: a gait between limping and trotting). The classical sense is a manner of walking, not a structural deformity of the limb.",
        "classical_he": "خَمَعَ בערבית הקלאסית = 'לצלוע, ללכת בצליעה קלה' — נאמר במיוחד על הצבוע או הזאב (ליין: הילוך שבין צליעה לדהירה). המשמע הקלאסי הוא אופן הליכה, לא מום מבני באבר.",
        "saadia_en": "one with a dislocated hip / a stretched-out limb — Saadia renders the priestly-blemish term שָׂרוּעַ with خامع in the vernacular sense 'dislocated-hipped', a colloquial meaning outside the classical 'to limp'.",
        "saadia_he": "בעל ירך שמוטה / אבר מתוח — סעדיה מתרגם את מונח־המום הכהני שָׂרוּעַ באמצעות خامع במשמע הדיבורי 'בעל מפרק ירך נקוע', משמעות עממית שמחוץ למשמע הקלאסי 'לצלוע'.",
        "mechanism": "A vernacular-sense identification that fixes an obscure Hebrew blemish-term with a colloquial Arabic word rather than its classical meaning. שָׂרוּעַ (Lev 21:18, in the list of priestly disqualifying blemishes) is itself obscure — traditionally 'a limb stretched out / abnormally long', a structural deformity. The Arabic root خمع classically means 'to limp' (a GAIT, said of the hyena), but Saadia uses אלכ'אמע (ואלאכ'רם ואלכ'אמע 'the one with a mutilated nose and the dislocated-hipped one') in the COLLOQUIAL sense 'one whose hip is dislocated / נשמטה ירכו' — a meaning Blau documents from the vernacular lexica (Muḥīṭ al-Muḥīṭ) and explicitly distinguishes from classical 'to limp' (and from خلع 'to dislocate'). The choice resolves the obscure Hebrew blemish not by classical Arabic but by the living dialectal sense of a related root — Saadia reaching past the classical register to the spoken word that actually names the deformity. Pedagogically distinctive because it exposes the Tafsir's willingness to use vernacular Judaeo-Arabic medical vocabulary to pin down the Torah's technical blemish-terms, where the classical lexicon would mislead.",
        "verses": [
            {"book": "Vayikra", "ch": 21, "v": 18},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "خمع",
            "sense": "Blau (s.v. خمع) glosses 'to be dislocated (of the hip) / נשמטה ירכו', citing Saadia's rendering of שרוע at Lev 21:18 and noting the vernacular attestation (Muḥīṭ al-Muḥīṭ); he distinguishes it from classical خمع 'to limp' and from خلع. The dislocated-hip blemish sense is the divergence catalogued here.",
            "relation": "direct",
        },
    },

    # ---- TWIST — the suet read as the interior/pluck ---------------------
    {
        "lemma_ja": "קצבה",
        "variants": ["אלקצבה", "קצבתה", "קצבת"],
        "lemma_ar": "قصبة",
        "root": "ق-ص-ب",
        "tier": "twist",
        "classical_en": "Classical Arabic قَصَبَة is the unit-noun of قصب: a reed, cane, or tube; also 'to cut up a carcass into joints' (the butcher's qaṣṣāb). By extension قصبة names 'the interior of a town/house' (its central tract). The application to the body's interior organs (liver, lungs, heart) is a post-classical anatomical extension.",
        "classical_he": "قَصَبَة בערבית הקלאסית הוא שם־היחידה של قصب: קנה, גבעול, או צינור; וגם 'לחלק פגר לנתחים' (קצב, القصّاب). בהרחבה قصبة מציין 'פנים העיר/הבית' (מרכזה). היישום לאיברי הפנים של הגוף (כבד, ריאות, לב) הוא הרחבה אנטומית בתר־קלאסית.",
        "saadia_en": "the interior / the pluck (liver-lungs-heart bloc) — Saadia renders Hebrew פֶּדֶר ('the suet/fat-portion' of the burnt offering) as قصبة 'the interior organ-bloc', reading the term not as fat but as the animal's inner-organ section.",
        "saadia_he": "הפנים / מקבץ האיברים הפנימיים (כבד-ריאות-לב) — סעדיה מתרגם את פֶּדֶר ('חלק החֵלב' של העולה) באמצעות قصبة 'מקבץ האיברים הפנימיים', וקורא את המונח לא כחֵלב אלא כמדור האיברים הפנימיים של הבהמה.",
        "mechanism": "An exegetical-anatomical identification that re-reads an obscure sacrificial term. Hebrew פֶּדֶר (Lev 1:8, 1:12, 8:20) is a rare cultic word usually understood as 'the suet, the fat-portion' arranged on the altar with the head and the cut pieces. Saadia instead renders it אלקצבה — pairing it in the burnt-offering sequence as אלאעצ'א ואלראס ואלקצבה ('the limbs, the head, and the qaṣaba', 1:8) and וראסה וקצבתה ('its head and its qaṣaba', 1:12). قصبة in this anatomical sense (which Blau glosses as 'the interior of the body — liver, lungs, heart') names the inner-organ bloc, the 'pluck', not the fat. The identification reflects an interpretive decision about what פדר denotes: not the suet-layer but the central organ-section of the carcass that is laid on the altar. The move imports the post-classical anatomical sense of قصبة (an extension from 'interior of a town' to 'interior of the body') to fix the Hebrew cultic term. Pedagogically distinctive because it shows Saadia resolving a sacrificial hapax-like word by anatomical identification rather than by the traditional 'fat' gloss — a real interpretive fork in how the offering is pictured on the altar.",
        "verses": [
            {"book": "Vayikra", "ch": 1, "v": 8},
            {"book": "Vayikra", "ch": 1, "v": 12},
            {"book": "Vayikra", "ch": 8, "v": 20},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "قصب",
            "sense": "Blau (s.v. قصب, headword قصبة) glosses 'the interior of the body (liver, lungs, heart) / פנים הגוף', a post-classical extension from 'interior of a town/house'. Blau attests the anatomical sense but does not cite the Lev 1:8 פדר rendering directly, hence relation=adjacent: the divergence is Saadia's application of this interior-organ sense to the Hebrew suet-term פדר.",
            "relation": "adjacent",
        },
    },

    # ---- TWIST — sheirim demythologized as 'demons' ----------------------
    {
        "lemma_ja": "שיאטין",
        "variants": ["אלשיאטין", "שיטאן"],
        "lemma_ar": "الشياطين",
        "root": "ش-ط-ن",
        "tier": "twist",
        "classical_en": "Classical Arabic شَيْطَان (pl. شياطين) = 'a satan, devil, demon' — a rebellious or malevolent spirit. The word is the standard Arabic term for a demonic being and carries no agricultural or caprine sense.",
        "classical_he": "شَيْطَان (רבים شياطين) בערבית הקלאסית = 'שטן, שד, רוח רעה' — ישות רוחנית מורדת או מרושעת. זוהי המילה הערבית הסטנדרטית ליצור שֵׁדִי, ואין לה משמע חקלאי או עִזִּי.",
        "saadia_en": "the demons — Saadia renders Hebrew שְׂעִירִם ('hairy ones / goat-demons / satyrs') with الشياطين 'the demons', making explicit the demonic identity of the beings to which Israelites illicitly sacrifice.",
        "saadia_he": "השדים — סעדיה מתרגם את שְׂעִירִם ('שעירים / שדי-עזים / שעירי-שדה') באמצעות الشياطين 'השדים', ומבהיר את זהותם הדמונית של היצורים שאליהם זובחים בני ישראל באיסור.",
        "mechanism": "A demythologizing-by-identification move characteristic of Saadia: an obscure or mythologically-loaded Hebrew noun is rendered with the Arabic term that names its REFERENT's true category. Hebrew שְׂעִירִם literally means 'hairy ones' — the goat-shaped field-spirits / satyrs to which Lev 17:7 says Israelites must no longer sacrifice ('ולא יזבחו עוד את זבחיהם לשעירם'). Rather than calquing 'the hairy ones' (which would obscure what they are), Saadia identifies them outright as אלשיאטין 'the demons' (לאלשיאטין), classifying the forbidden cult as demon-worship. This is the same interpretive strategy by which Saadia renders בְּנֵי הָאֱלֹהִים as 'the nobles' (אשראף, anti-mythological), אֲרָרָט as Qardū (geographic identification), and אוּר כַּשְׂדִּים as the Babylonian 'furnace' (אתון): the translation does exegesis by naming the thing. The divergence is not lexical-within-Arabic (شيطان simply means 'demon') but interpretive: Saadia decides what the שעירים ARE and translates accordingly. Pedagogically distinctive because it lays bare the Tafsir's identificatory method — and its theological program of demythologizing Israel's lapses into a stark monotheist-vs-demonic frame. (Like Saadia's other identification-renderings, this is a saadia-direct reading not lemmatized as a lexical divergence in Blau.)",
        "verses": [
            {"book": "Vayikra", "ch": 17, "v": 7},
        ],
        "sources": ["lane", "saadia-direct"],
    },
]


# ============================================================================
# Helpers
# ============================================================================

CONSUMED_LOG = [
    {"blau_id": 15824, "landed_as": "twist תרפק (Vayikra 25:3-4)", "note": "Heb תזמר → Ar رفق (Aramaic-driven prune calque)."},
    {"blau_id": 18378, "landed_as": "twist פיצ'הא (Vayikra 15:28)", "note": "Heb זוב → Ar فيضة (Hebrew-driven flux specialization)."},
    {"blau_id": 17407, "landed_as": "twist אלכ'אמע (Vayikra 21:18)", "note": "Heb שרוע → Ar خامع 'dislocated-hip' (vernacular sense)."},
    {"blau_id": 18594, "landed_as": "twist אלקצבה (Vayikra 1:8+)", "note": "Heb פדר → Ar قصبة 'interior/pluck' (anatomical reframe; adjacent)."},
]

NO_CITE_AUDIT = {
    "lemma_ja": "שיאטין",
    "verse": "Vayikra 17:7",
    "decision": "Shipped sources=[lane, saadia-direct], NO blau_dict. Heb שעירים ('goat-demons') → Ar الشياطين ('the demons') is an EXEGETICAL identification, not a lexical divergence within Arabic (شيطان = 'demon' is classical). Blau does not lemmatize it. Consistent with the existing demythologizing identification-entries (אשראף, קרדא, אתון — all no-cite). Counts as 1 no-citation in the Vayikra twist mix (1/5 = 20%, within the <=30% bar).",
    "logged_on": CONSUMED_DATE,
}


def _log_deferred(deferred_path: pathlib.Path) -> dict:
    payload = json.loads(deferred_path.read_text())
    consumed = payload.setdefault("phase3_r1_consumed", [])
    existing_ids = {it.get("blau_id") for it in consumed if isinstance(it, dict)}
    added = 0
    for item in CONSUMED_LOG:
        if item["blau_id"] in existing_ids:
            continue
        rec = dict(item)
        rec["consumed_on"] = CONSUMED_DATE
        consumed.append(rec)
        existing_ids.add(item["blau_id"])
        added += 1

    audit = payload.setdefault("no_cite_audit", {})
    bucket = audit.setdefault("phase3_r1_no_blau", [])
    if not any(isinstance(r, dict) and r.get("lemma_ja") == "שיאטין" for r in bucket):
        bucket.append(NO_CITE_AUDIT)
        audit_added = 1
    else:
        audit_added = 0

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(deferred_path.read_text())  # parse-check
    return {"phase3_r1_consumed_added": added, "no_cite_audit_added": audit_added}


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    div_path = root / "data" / "tafsir-divergence.json"
    deferred_path = root / "data" / "_blau_saadia_deferred.json"

    if not div_path.exists():
        print(f"FATAL: {div_path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(div_path.read_text())

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

    print(f"Added {added} entries to {div_path.name}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")
    print(f"Deferred summary: {json.dumps(deferred_summary, ensure_ascii=False)}")


if __name__ == "__main__":
    main()

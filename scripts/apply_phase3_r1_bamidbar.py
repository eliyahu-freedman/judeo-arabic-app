"""
Phase 3 R1 Second Wave — Bamidbar batch. Activate and clear the verifier's
per-book quality gate for Bamidbar (Numbers).

Why
---
The verifier's per-book relation-mix gate activates for a book only once it has
>=5 twist-tier entries (counted by the FIRST verse's book). Before this batch
Bamidbar had ZERO first-verse twists — its Bamidbar-anchored entries were all
note (גבן, מגרד, מחפצה, ראם) or gloss. This batch brings Bamidbar to 5 by:

  PROMOTE note->twist (1):
    - ראם (Num 13:21+) — Heb תור 'to scout/explore' → Ar روم 'to seek-after,
      pursue (volitionally)'. Physical-exploration verb reframed as volitional
      pursuit; sharpest at Num 15:39 (do not PURSUE after heart+eyes). direct.
      (The other 3 Bamidbar direct-NOTEs — גבן, מגרד, מחפצה — are left as notes:
       referent-identical framing / coinage-matching, not paradigm shifts.)

  NEW TWIST (4):
    - אלת'רא  (Num 16:30, 16:33) — Heb שאול 'Sheol/underworld' → Ar الثرى 'the
      (damp) earth' (demythologizing; Blau: Saadia renders שאול with it בקביעות). direct.
    - דראדר   (Num 21:14) — obscure toponym את והב בסופה → 'the breakers of
      al-Qulzum (the Red Sea)' (demythologizing geographic identification). direct.
    - מחצ'ר   (Num 6:18, 16:2) — cultic מועד / אהל מועד → Ar محضر 'assembly'
      (de-sacralizing the divine-appointment term). direct.
    - קצד     (Num 6:26) — anthropomorphic יִשָּׂא...פָּנָיו 'lift His face' →
      ויקבל בקצדה 'receive with His intent' (anti-anthropomorphic; no-cite).

Bamidbar twists after = 5.
  direct = 4 (ראם, אלת'רא, דראדר, מחצ'ר); no-cite = 1 (קצד).
  direct 4/5 = 80% (>=45%); backed 4/5 = 80% (>=70%); no-cite 1/5 = 20% (<=30%).

Sourcing
--------
Surface forms read from the Saadia corpus (data/tafsir-bamidbar-{ch}.json, field
`ja`) — never hand-authored. Blau senses verified against the Blau dictionary
extract (data/_blau_saadia_candidates.json: ثرى#14403, دردور#15439, محضر#17364);
the ראם promotion inherits its already-verified blau-direct citation.

Apply pattern
-------------
- PROMOTE_TO_TWIST first (tier flip + mechanism rewrite) so the append step does
  not skip-collide on the existing lemma.
- Append new entries by lemma_ja uniqueness; write-back via
  json.dumps(..., ensure_ascii=False, indent=2) + "\\n", re-parse.
- Log consumed Blau ids into phase3_r1_consumed + the קצד no-blau decision into
  no_cite_audit (audit trail; idempotent).
"""

import json
import pathlib
import sys
from collections import Counter

CONSUMED_DATE = "2026-06-02"

# ============================================================================
# PROMOTIONS — note -> twist (tier flip + deepened mechanism). The entry's
# verses[], variants[], sources[], blau_dict are left intact (already verified).
# ============================================================================

PROMOTE_TO_TWIST = [
    {
        "lemma_ja": "ראם",
        "mechanism": "Volitional reframe of a physical-exploration verb — a paradigm shift in what the spies (and the worshipper's eyes) are doing. Hebrew תור across the Bamidbar narrative is fundamentally a verb of PHYSICAL exploration-and-traverse: the spies range over the land (וַיָּתֻרוּ אֶת-הָאָרֶץ, Num 13:21; אֲשֶׁר תָּרוּ אֹתָהּ, 13:32), the eyes physically rove after the heart's desire (Num 15:39). Saadia renders all three with روم — but روم is not a motion-verb at all: it is a VOLITIONAL verb of intentional pursuit, 'to seek-after, to aim at acquiring, to set oneself toward' (distinct from أراد 'to wish' by foregrounding the going-after). The divergence relocates the whole semantics of biblical תור from the physical plane to the plane of will and intention. It is sharpest at Num 15:39: Hebrew וְלֹא-תָתוּרוּ אַחֲרֵי לְבַבְכֶם 'do not go-roving after your heart and eyes' (outward following) becomes ולא תרומו אתבאע קלובכם ועיונכם 'do not PURSUE/seek after your heart and eyes' — the commandment is internalized from outward wandering into inner volitional pursuit of desire. The reconnaissance of the land is likewise recast: the spies do not merely traverse it, they intentionally seek-after it. Blau (s.v. روم) glosses Form I 'to seek-after, intend, pursue', citing Saadia on Num 13:21, 13:32, 15:39, with cross-attestation in Yefet on Daniel 92 (ما رام إلى إثباته 'what he sought to confirm') confirming the volitional-pursuit frame as Saadia's stable choice for תור. The twist: a verb of bodily exploration becomes a verb of will.",
    },
]


# ============================================================================
# NEW ENTRIES — 4 (3 TWIST direct + 1 TWIST no-cite)
# ============================================================================

NEW_ENTRIES = [
    # ---- TWIST — Sheol demythologized as 'the earth' --------------------
    {
        "lemma_ja": "אלת'רא",
        "variants": ["ת'רא"],
        "lemma_ar": "الثرى",
        "root": "ث-ر-ي",
        "tier": "twist",
        "classical_en": "Classical Arabic الثرى (root ث-ر-ي) = 'the moist earth, the damp soil, the dust of the ground' (Lane: التُّراب النَّدِيّ, the moistened dust). The semantic field is ordinary physical earth — there is no underworld or netherworld sense in classical Arabic.",
        "classical_he": "الثرى בערבית הקלאסית (שורש ث-ر-ي) = 'האדמה הלחה, העפר הרטוב, אבק הקרקע' (ליין: התראב הלח). השדה הסמנטי הוא קרקע פיזית רגילה — אין משמע של שאול או עולם־מתים בערבית הקלאסית.",
        "saadia_en": "the netherworld / Sheol — Saadia renders Hebrew שְׁאוֹל ('Sheol', the chthonic realm of the dead) with الثرى 'the (damp) earth', dissolving the mythological underworld into ordinary ground.",
        "saadia_he": "עולם־המתים / שאול — סעדיה מתרגם את שְׁאוֹל ('שאול', ממלכת המתים התת־קרקעית) באמצעות الثرى 'האדמה (הלחה)', וממוסס את העולם־התחתון המיתולוגי לכלל קרקע רגילה.",
        "mechanism": "A demythologizing substitution that erases biblical cosmology's underworld. Hebrew שְׁאֹלָה (Num 16:30, 16:33) is 'down to Sheol' — the named chthonic realm of the dead into which Korah's company descend ALIVE, the earth opening its mouth to swallow them into a netherworld. Saadia renders 'וירדו חיים שאלה' as 'וינזלו אחיא אלי' אלת'רא' — 'and they go down alive into the (damp) earth/ground'. Classical Arabic الثرى means only 'the moist soil, the dust of the earth' (Lane); it carries no netherworld sense. Blau (s.v. ثرى) records the post-classical sense 'underworld / שאול' precisely AS Saadia's usage, noting that he renders Hebrew שאול with it REGULARLY (בקביעות), cross-referenced in Dozy, al-Fāsī's Jāmiʿ, and Ibn Janāḥ. The move is programmatic demythologizing: Sheol — a populated realm with its own topography in the biblical imagination — is reduced to mere dirt. Korah and his household do not descend into an underworld but simply sink alive into the ground, which then closes over them (וג'טת עליהם אלארץ', 16:33). The paradigm shift is cosmological: where the Hebrew pictures a descent into a mythic netherworld, Saadia's Arabic pictures only a swallowing by ordinary earth. This belongs to his broader program of stripping mythological geography and topography from the Torah — the same impulse by which he flattens other loaded cosmic terms into rationalized physical referents.",
        "verses": [
            {"book": "Bamidbar", "ch": 16, "v": 30},
            {"book": "Bamidbar", "ch": 16, "v": 33},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "ثرى",
            "sense": "Blau (s.v. ثرى) records the post-classical sense 'underworld / שאול' and notes that Saadia regularly (בקביעות) renders Hebrew שאול with it, cross-referencing Dozy, al-Fāsī's Jāmiʿ, and Ibn Janāḥ. Classical Arabic الثرى = only 'the moist earth, the soil'; the netherworld sense is Saadia's systematic demythologizing rendering, instanced here at Num 16:30, 33.",
            "relation": "direct",
        },
    },

    # ---- TWIST — opaque toponym identified as the Red Sea breakers ------
    {
        "lemma_ja": "דראדר",
        "variants": ["אלדראדר", "דרדור"],
        "lemma_ar": "درادر",
        "root": "د-ر-د-ر",
        "tier": "twist",
        "classical_en": "Classical Arabic دُرْدُور (pl. درادر) = 'a whirlpool, an eddy, a place where the sea churns and breaks; a billow/breaker' (Lane: the swirling water in the sea where ships are imperilled). A concrete maritime-water term for the surging, breaking sea.",
        "classical_he": "دُرْدُور (רבים درادر) בערבית הקלאסית = 'מערבולת, נחשול, מקום שבו הים סוער ונשבר; גל מתנפץ' (ליין: המים המסתחררים בים שבהם ספינות בסכנה). מונח ימי קונקרטי לים הגועש והנשבר.",
        "saadia_en": "the breakers of the Red Sea — Saadia renders the obscure archaic toponym-fragment אֶת-וָהֵב בְּסוּפָה with מן אלדראדר אלקלזם 'from the breakers of al-Qulzum (the Red Sea)', identifying an unintelligible place-name with a known body of water.",
        "saadia_he": "נחשולי ים־סוף — סעדיה מתרגם את צירוף שם־המקום הארכאי הסתום אֶת-וָהֵב בְּסוּפָה באמצעות מן אלדראדר אלקלזם 'מן הנחשולים של אלקלזם (ים־סוף)', ומזהה שם־מקום בלתי־מובן עם גוף־מים ידוע.",
        "mechanism": "A demythologizing geographic identification that dissolves a fossilized epic fragment into rationalized realia. Num 21:14 quotes 'the Book of the Wars of the LORD' with the famously opaque clause אֶת-וָהֵב בְּסוּפָה — archaic, possibly corrupt, traditionally read as an unintelligible place-name ('Waheb in Suphah'). Saadia refuses to leave it standing as an opaque name: he renders the whole as 'פי כתאב פתוח אללה מן אלדראדר אלקלזם' — 'in the book of God's conquests, from the breakers of al-Qulzum'. al-Qulzum is the classical Arabic name of the Red Sea / Gulf of Suez; Saadia reads בְּסוּפָה not as a toponym but through יַם-סוּף (the Sea of Reeds / Red Sea), and renders וָהֵב via درادر 'breakers, billows'. Blau (s.v. دردور 'breaker, billow', pl. درادر) cites THIS exact verse (רס״ג לבמדבר כא:יד 'את והב בסופה'), glossing the אלקלזם identification as 'מן הנחשולים [ים] סוף'. The paradigm shift: where the Hebrew preserves an undeciphered scrap of ancient war-poetry geography, Saadia converts it into a concrete physical-geographic statement about the surf of a named sea. The opaque becomes the identified; epic toponymy becomes maritime realia — a characteristic move of the Tafsir's rationalizing program toward obscure biblical names.",
        "verses": [
            {"book": "Bamidbar", "ch": 21, "v": 14},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "دردور",
            "sense": "Blau (s.v. دردور 'breaker, billow', pl. درادر) cites Saadia on Num 21:14 (את והב בסופה → ... אלקלזם), glossing 'מן הנחשולים [ים] סוף' — the breakers of the Red Sea (al-Qulzum). Classical دردور = a sea-whirlpool / eddy / breaker; the divergence catalogued here is Saadia's use of it to dissolve the opaque toponym וָהֵב בְּסוּפָה into a Red-Sea geographic identification.",
            "relation": "direct",
        },
    },

    # ---- TWIST — cultic 'appointed meeting' de-sacralized to 'assembly' -
    {
        "lemma_ja": "מחצ'ר",
        "variants": ["אלמחצ'ר"],
        "lemma_ar": "محضر",
        "root": "ح-ض-ر",
        "tier": "twist",
        "classical_en": "Classical Arabic محضر (from حضر 'to be present') = 'a place or act of presence; an assembly of people; a written record/minutes; a court-session or tribunal (and those present at it)'. The semantic field is civic-juridical — gathering, attendance, the convened court — with no sense of a divinely-appointed sacred meeting.",
        "classical_he": "محضر בערבית הקלאסית (מן حضر 'להיות נוכח') = 'מקום או מעשה של נוכחות; אסיפת אנשים; פרוטוקול/רישום; מושב בית־דין (והנוכחים בו)'. השדה הסמנטי הוא אזרחי־משפטי — התכנסות, נוכחות, בית־הדין המכונס — בלא משמע של מועד קדוש שנקבע בידי האל.",
        "saadia_en": "the assembly — Saadia renders the cultic מוֹעֵד ('appointed meeting'; and אֹהֶל מוֹעֵד 'the Tent of Meeting') with محضر 'assembly', recasting the divine-appointment term as a neutral civic gathering.",
        "saadia_he": "האספה — סעדיה מתרגם את מוֹעֵד הפולחני ('מועד שנקבע'; ואֹהֶל מוֹעֵד 'אוהל מועד') באמצעות محضر 'אספה', וממיר את מונח המפגש־עם־האל בהתכנסות אזרחית ניטרלית.",
        "mechanism": "A de-sacralizing reframe that drains a sacred-appointment term of its theological charge. Hebrew מוֹעֵד in the priestly vocabulary denotes the divinely-APPOINTED meeting — the fixed sacred rendezvous between God and Israel (root יעד 'to designate, appoint by [divine] decree'), and by metonymy אֹהֶל מוֹעֵד, 'the Tent of Meeting', the very locus of that encounter. Saadia routes it through محضر — a civic-juridical term meaning 'assembly, those present, court-session'. At Num 16:2, קְרִאֵי מוֹעֵד 'those summoned of the appointed-assembly' becomes דעאת מחצ'ר 'the summoned-ones of the assembly'; at Num 6:18, פֶּתַח אֹהֶל מוֹעֵד 'the entrance of the Tent of Meeting' becomes ענד באב כ'בא אלמחצ'ר 'at the door of the tent of the assembly'. Blau (s.v. محضر 'assembly / קהל') notes that Saadia 'frequently uses this word to translate עדה, מועד', citing Num 16:2 (דעאת מחצ'ר 'מזמני העדה') and the خباء المحضر = 'אהל מועד ... בעצם אוהל האספה' (Tent of Meeting = really tent of assembly) rendering. The paradigm shift: the term sheds its theological sense of DIVINE appointment and becomes a sociological 'assembly/gathering'; the sacred rendezvous between God and people is re-described as an ordinary civic convocation. That محضر also means 'tribunal/court' deepens the secular-institutional register — the holy meeting-place reconceived as a civic assembly-hall.",
        "verses": [
            {"book": "Bamidbar", "ch": 6, "v": 18},
            {"book": "Bamidbar", "ch": 16, "v": 2},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "محضر",
            "sense": "Blau (s.v. محضر 'assembly, קהל; court/tribunal') notes Saadia frequently renders עדה / מועד with it, citing Num 16:2 (קראי מועד → דעאת מחצ'ר 'מזמני העדה') and the خباء المحضر = 'אהל מועד ... בעצם אוהל האספה' (tent of meeting = really tent of assembly). The divergence catalogued here is Saadia's de-sacralizing of the cultic appointed-meeting מועד into a civic 'assembly'.",
            "relation": "direct",
        },
    },

    # ---- TWIST — anthropomorphic 'lift His face' → 'receive with intent' (no-cite)
    {
        "lemma_ja": "קצד",
        "variants": ["קצדה", "בקצדה"],
        "lemma_ar": "قصد",
        "root": "ق-ص-د",
        "tier": "twist",
        "classical_en": "Classical Arabic قَصْد / قَصَدَ (root ق-ص-د) = 'aim, intent, purpose; the directing of oneself toward something; to head for, to aim at, to intend' (Lane). An abstract noun/verb of intention and purposeful direction — not a body-part and not a gesture.",
        "classical_he": "قَصْد / قَصَدَ בערבית הקלאסית (שורש ق-ص-د) = 'כוונה, מטרה, תכלית; הפניית האדם את עצמו אל דבר; לפנות אל, לכוון אל, להתכוון' (ליין). שם־עצם/פועל מופשט של כוונה והכוונה תכליתית — לא אבר־גוף ולא מחווה.",
        "saadia_en": "(God's) intent / favorable regard — Saadia renders the anthropomorphic יִשָּׂא יְהוָה פָּנָיו אֵלֶיךָ ('may the LORD lift His face toward you') by removing the divine 'face' altogether: ויקבל בקצדה אליך 'and may He receive (you) with His intent toward you'.",
        "saadia_he": "כוונתו / חסדו (של האל) — סעדיה מתרגם את יִשָּׂא יְהוָה פָּנָיו אֵלֶיךָ האנתרופומורפי ('יישא ה' פניו אליך') תוך הסרת 'פני' האל כליל: ויקבל בקצדה אליך 'ויקבל אותך בכוונתו אליך'.",
        "mechanism": "An anti-anthropomorphic substitution inside the Priestly Blessing (Num 6:24-26). Hebrew יִשָּׂא יְהוָה פָּנָיו אֵלֶיךָ (6:26) literally has God 'lift/raise His FACE toward you' — a bodily idiom of favorable regard. Saadia, programmatically refusing to attribute a face or body to God, renders it ויקבל בקצדה אליך — 'and may He receive (you) with His intent/purpose (qaṣd) toward you'. The divine 'face' (פנים) is replaced by the abstract noun of intention (قصد), and the gesture of 'lifting the face' becomes 'receiving with intent'. The selectivity is the proof of design: in the immediately preceding clause (6:25) יָאֵר יְהוָה פָּנָיו אֵלֶיךָ 'may the LORD make His face shine', Saadia DOES keep a face-word (ויצ'י וגהה 'may His countenance shine') — so the 6:26 abstraction is a deliberate LOCAL anti-anthropomorphism, applied precisely where 'lifting the face' would most strongly suggest a bodily turning of God toward the worshipper. This is not a lexical divergence within Arabic — قصد simply means 'intent' — but an EXEGETICAL substitution: Saadia decides what 'lifting the face' means (the granting of God's favorable intent) and translates the interpretation rather than the image. Like the corpus's other no-cite identification-twists (אשראף, קרדא, שיאטין), the move is interpretive, not lexical; Blau does not lemmatize it, so it ships saadia-direct.",
        "verses": [
            {"book": "Bamidbar", "ch": 6, "v": 26},
        ],
        "sources": ["lane", "saadia-direct"],
    },
]


# ============================================================================
# Helpers
# ============================================================================

CONSUMED_LOG = [
    {"blau_id": 14403, "landed_as": "twist אלת'רא (Bamidbar 16:30, 33)", "note": "Heb שאול → Ar الثرى 'the (damp) earth' (demythologizing; Blau: Saadia renders שאול with it בקביעות)."},
    {"blau_id": 15439, "landed_as": "twist דראדר (Bamidbar 21:14)", "note": "Obscure את והב בסופה → 'breakers of al-Qulzum (Red Sea)' (geographic identification; Blau cites the verse)."},
    {"blau_id": 17364, "landed_as": "twist מחצ'ר (Bamidbar 6:18, 16:2)", "note": "Cultic מועד / אהל מועד → Ar محضر 'assembly' (de-sacralizing; Blau cites Num 16:2)."},
]

NO_CITE_AUDIT = {
    "lemma_ja": "קצד",
    "verse": "Bamidbar 6:26",
    "decision": "Shipped sources=[lane, saadia-direct], NO blau_dict. Heb יִשָּׂא...פָּנָיו ('lift His face') → ויקבל בקצדה ('receive with His intent') is an anti-anthropomorphic EXEGETICAL substitution, not a lexical divergence within Arabic (قصد = 'intent' is classical). Blau does not lemmatize it. Selectivity confirmed: Num 6:25 retains a face-word (ויצ'י וגהה), so 6:26 is a deliberate local anti-anthropomorphism. Consistent with the corpus's other no-cite identification-twists (אשראף, קרדא, שיאטין). Counts as 1 no-citation in the Bamidbar twist mix (1/5 = 20%, within the <=30% bar).",
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
    if not any(isinstance(r, dict) and r.get("lemma_ja") == "קצד" for r in bucket):
        bucket.append(NO_CITE_AUDIT)
        audit_added = 1
    else:
        audit_added = 0

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(deferred_path.read_text())  # parse-check
    return {"phase3_r1_consumed_added": added, "no_cite_audit_added": audit_added}


def _bamidbar_twist_count(entries) -> int:
    n = 0
    for e in entries:
        if (e.get("tier") or "twist") != "twist":
            continue
        vs = e.get("verses", [])
        if vs and vs[0].get("book") == "Bamidbar":
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
    before = _bamidbar_twist_count(payload["entries"])

    # 1) Promote note->twist BEFORE append.
    promote_summaries = _patch_promote_to_twist(payload)

    # 2) Append new entries by lemma_ja uniqueness.
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

    after = _bamidbar_twist_count(payload["entries"])
    print(f"Promotions: {json.dumps(promote_summaries, ensure_ascii=False)}")
    print(f"Added {added} entries to {div_path.name}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    print(f"Bamidbar first-verse twists: {before} -> {after}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")
    print(f"Deferred summary: {json.dumps(deferred_summary, ensure_ascii=False)}")


if __name__ == "__main__":
    main()

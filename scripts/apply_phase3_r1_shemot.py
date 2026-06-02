"""
Phase 3 R1 Second Wave — Shemot batch. Add 5 net-new TWIST-tier entries to
data/tafsir-divergence.json, anchored (first verse) in Shemot, to activate
and clear the verifier's per-book quality gate for Shemot.

Why
---
The verifier's per-book relation-mix gate activates for a book only once it
has >=5 twist-tier entries (counted by the FIRST verse's book). Before this
batch Shemot had exactly 1 twist (תגלא, no-citation). This batch adds 5
Blau-backed twists so the gate activates and clears:
  Shemot twists after = 6 (תגלא no-cite + 5 new).
  direct = 4 (שריעה, אגתחד, צריח, מתרבץ); adjacent = 1 (אלמהל);
  no-cite = 1 (תגלא).
  direct 4/6 = 67% (>=45%); backed 5/6 = 83% (>=70%); no-cite 1/6 = 17% (<=30%).

Sourcing
--------
Candidates mined from data/_blau_saadia_candidates.json (Blau Saadia-citing
entries) and VERIFIED against the Saadia corpus (data/tafsir-shemot-{ch}.json,
fields ch/v/ja/hebrew) — every surface form below was read from the corpus,
not hand-authored. Classical senses confirmed via Lane; Blau senses via the
arabic-lexicon skill (slug blau-judeoarabic).

Triage outcome
--------------
NEW ENTRIES — 5 TWIST:
  - TWIST שריעה   Ex 12:49, 13:9, 16:4, 16:29, 18:20, 24:12 — Heb תורה/תורת
                  → Ar شريعة (Torah-as-sharīʿa calque; direct)
  - TWIST אלמהל   Ex 34:6 — Heb אֶרֶךְ אַפַּיִם → Ar طويل المهل
                  (anti-anthropomorphic; adjacent)
  - TWIST אגתחד   Ex 9:15 — Heb וַתִּכָּחֵד → Ar اجتحد 'be destroyed'
                  (Hebrew-driven bilingual calque; direct)
  - TWIST צריח    Ex 12:19, 12:48, 12:49 — Heb אֶזְרָח → Ar صريح
                  'of pure/unmixed lineage' (legal-category reframe; direct)
  - TWIST מתרבץ   Ex 9:17 — Heb מִסְתּוֹלֵל (hapax) → Ar متربّص 'detaining'
                  (hapax reframe; direct)

Apply pattern
-------------
- Mirrors scripts/apply_phase4_devarim_batch1.py: NEW_ENTRIES append by
  lemma_ja uniqueness, write-back via
  json.dumps(..., ensure_ascii=False, indent=2) + "\n" then re-parse.
- Logs the 5 consumed Blau ids into _blau_saadia_deferred.json#/phase3_r1_consumed
  (audit trail; idempotent on blau_id).
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
    # ---- TWIST — Torah rendered as sharīʿa -------------------------------
    {
        "lemma_ja": "שריעה",
        "variants": ["שראיע", "שראיעי", "שראיעה", "אלשריעה", "שריעת"],
        "lemma_ar": "شريعة",
        "root": "ش-ر-ع",
        "tier": "twist",
        "classical_en": "Classical Arabic شَرِيعَة derives from شَرَعَ, whose primary concrete sense is 'a watering-place, the approach to water where beasts come to drink' (Lane). The legal sense ('a divinely-instituted ordinance / revealed law') develops from شَرَعَ لهم = سَنَّ 'to institute a religious ordinance', and is the loaded theological register the Qur'an uses for revealed law (شريعة).",
        "classical_he": "שׁَرִيעַة בערבית הקלאסית נגזרת מن شَرَعَ, שמשמעו הקונקרטי הראשוני 'מקום השקאה, המבוא אל המים שאליו באים העדרים לשתות' (ליין). המשמע המשפטי ('חוק אלוהי מחוקק / תורה מגולה') מתפתח מن شَرَعَ لهم = سَنَّ 'לחוקק חוק דתי', והוא המשלב התאולוגי הטעון שבו הקֻראן משתמש לתורה מגולה (شريعة).",
        "saadia_en": "law, revealed legislation — Saadia renders Hebrew תּוֹרָה / תּוֹרַת ה' (and the plural תּוֹרֹת) systematically with شريعة / شرائع, the Islamic-theological term for revealed divine law.",
        "saadia_he": "חוק, תורה מגולה — סעדיה מתרגם באופן שיטתי את תּוֹרָה / תּוֹרַת ה' (ואת הרבים תּוֹרֹת) באמצעות شريعة / شرائع, המונח התאולוגי-איסלאמי לחוק האלוהי המגולה.",
        "mechanism": "Theological calque that re-codes the Mosaic תּוֹרָה into the Arabic revelation-as-law category. Hebrew תּוֹרָה primarily means 'instruction, teaching, direction' (from ירה Hiphil 'to instruct/point the way') — a broad term spanning teaching, ruling, and the Pentateuch as a whole. Saadia could have rendered it with a teaching-word (تعليم) or the transliterated توراة; instead he chooses شريعة — the term whose theological weight is precisely 'a revealed, codified body of divine law', the same word the Qur'an and Islamic jurisprudence use for the divine Law. The choice maps the biblical torah onto the Islamic šarīʿa concept, narrowing 'teaching' to 'legislation' and aligning Israel's revelation with the Arabic-Islamic category of revealed law. The rendering is systematic across Shemot's torah-vocabulary: the singular at 12:49 ('תּוֹרָה אַחַת' = שריעה ואחדה 'one law'), 13:9 ('תּוֹרַת יְהוָה' = שריעה' אללה 'the law of God'), and 16:29 (where even 'the Sabbath' itself is glossed as שריעה' אלסבת 'the law of the Sabbath'); and the plural תּוֹרֹת at 16:4 ('בְּתוֹרָתִי' = פי שראיעי), 18:20 ('הַתּוֹרֹת' = אלשראיע) and 24:12 ('וְהַתּוֹרָה' = ואלשראיע, the tablets-of-the-Law verse). The cross-passage invariance shows this is Saadia's programmatic equation torah = šarīʿa, not a one-off. Pedagogically distinctive because the single lexical choice carries a whole theology of revelation: the Sinai teaching is presented to an Arabic readership as revealed Law in the fullest Islamic-juridical sense — a calque that both translates and theologically re-frames.",
        "verses": [
            {"book": "Shemot", "ch": 12, "v": 49},
            {"book": "Shemot", "ch": 13, "v": 9},
            {"book": "Shemot", "ch": 16, "v": 4},
            {"book": "Shemot", "ch": 16, "v": 29},
            {"book": "Shemot", "ch": 18, "v": 20},
            {"book": "Shemot", "ch": 24, "v": 12},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "شرع",
            "sense": "Blau (Dict. of Medieval Judaeo-Arabic Texts, s.v. شرع) glosses شريعة as 'divine commandment / religious law', and the definite plural الشرائع as a name for the Pentateuch — exactly the Saadia sense claimed here, that Hebrew תורה is rendered with the revealed-law term شريعة. Blau cites Saadia's tafsir for the equation.",
            "relation": "direct",
        },
    },

    # ---- TWIST — erekh apayim, anti-anthropomorphic ----------------------
    {
        "lemma_ja": "אלמהל",
        "variants": ["מהל", "אלמהלה"],
        "lemma_ar": "مهل",
        "root": "م-ه-ل",
        "tier": "twist",
        "classical_en": "Classical Arabic مَهْل / مُهْلَة = 'a leisurely pace; delay, respite; gentleness, deliberateness' (Lane: التُّؤَدَة 'unhurried deliberation'). The idiom طويل المهل = 'one of long forbearance, who grants long respite'. The semantic field is patience-as-delay, not bodily emotion.",
        "classical_he": "مَهْل / مُهْلَة בערבית הקלאסית = 'התנהלות מתונה; דחייה, ארכה; נחת ושיקול דעת' (ליין: التؤدة 'התנהלות בלא חיפזון'). הביטוי طويل المهل = 'בעל אורך־רוח, המעניק ארכה ארוכה'. השדה הסמנטי הוא סבלנות־כדחייה, לא רגש גופני.",
        "saadia_en": "long of forbearance / slow to act — Saadia renders the anthropomorphic אֶרֶךְ אַפַּיִם ('long of nostrils/anger') as طويل المهل, replacing the bodily idiom with the abstract attribute of patient respite.",
        "saadia_he": "אֲרֵךְ אורך־רוח / מאריך ארכה — סעדיה מתרגם את אֶרֶךְ אַפַּיִם ('ארך הנחיריים/האף') באמצעות طويل المهل, ומחליף את הניב הגופני בתכונה המופשטת של ארכה וסבלנות.",
        "mechanism": "Anti-anthropomorphic substitution in the great Thirteen-Attributes verse (Shemot 34:6). Hebrew אֶרֶךְ אַפַּיִם literally means 'long of nostrils/of the two nostrils' — the somatic Hebrew idiom for slowness to anger (אַף 'nose' doubling as 'anger', the flaring nostril of wrath). Saadia, programmatically refusing to ascribe a body or passions to God, renders the whole divine self-revelation through abstract moral attributes: אֵל רַחוּם וְחַנּוּן becomes אללה אלטאיק אלרחום אלראוף, and crucially אֶרֶךְ אַפַּיִם becomes טויל אלמהל — 'long of forbearance / one who grants long respite'. The choice strips the anatomical metaphor (nostrils → anger) entirely and substitutes the patience-as-delay field of مهل (deliberate, unhurried granting of time before acting). This is the same anti-anthropomorphic strategy Saadia applies to the divine 'face', 'hand', and 'descent' elsewhere — here applied to the attribute-formula that the liturgy treats as the kernel of divine mercy. Pedagogically distinctive because the substitution is doing theology: the verse that the tradition reads as God's emotional self-portrait is rendered as a catalogue of impassible moral perfections, with مهل converting 'slow to flare in anger' into 'long in granting respite' — mercy reframed as forbearance rather than feeling.",
        "verses": [
            {"book": "Shemot", "ch": 34, "v": 6},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "مهل",
            "sense": "Blau (s.v. مهل) attests مهل / أمهل in the sense 'respite, delay; to grant a respite' in medieval Judaeo-Arabic — the patience-as-delay field. Blau does not lemmatize the divine-attribute rendering of אֶרֶךְ אַפַּיִם itself; the anti-anthropomorphic application of طويل المهل to the Thirteen Attributes is Saadia's own deployment of the attested 'respite' sense, hence relation=adjacent.",
            "relation": "adjacent",
        },
    },

    # ---- TWIST — Hebrew-driven 'destroy' calque on jaḥada ----------------
    {
        "lemma_ja": "אגתחד",
        "variants": ["אגתחדת", "ואגתחדת"],
        "lemma_ar": "اجتحد",
        "root": "ج-ح-د",
        "tier": "twist",
        "classical_en": "Classical Arabic جَحَدَ = 'to deny, to disacknowledge' (Lane: to deny a thing or a right, whether knowing the truth or not); a secondary stratum means 'to be niggardly / scanty', and of land 'to be dry and yield no good'. There is NO classical sense 'to destroy / be destroyed'.",
        "classical_he": "جَحَدَ בערבית הקלאסית = 'להכחיש, לכפור' (ליין: להכחיש דבר או זכות, בין ביודעין בין בלא יודעין); רובד משני = 'לקמץ / להמעיט', ועל אדמה 'להיות צחיחה ולא להניב'. אין משמע קלאסי 'להשמיד / להישמד'.",
        "saadia_en": "you were destroyed / wiped out — Saadia uses Form VIII اجتحد for the Niphal וַתִּכָּחֵד 'you would have been effaced', importing the Hebrew root's 'destroy' sense into an Arabic verb that classically means only 'deny'.",
        "saadia_he": "נכחדת / נמחית — סעדיה משתמש בבניין VIII اجتحد עבור הנפעל וַתִּכָּחֵד, ומייבא את משמעות 'השמדה' של השורש העברי אל פועל ערבי שמשמעו הקלאסי הוא 'הכחשה' בלבד.",
        "mechanism": "A bilingual (Hebrew-driven) calque that bends an Arabic verb to its Hebrew cognate's extra sense. The Hebrew root כ-ח-ד carries a double range: 'to hide / conceal / deny' (Piel-Hiphil) AND, in the Niphal, 'to be effaced, blotted out, destroyed' (e.g. וַתִּכָּחֵד מִן הָאָרֶץ 'and you would have been wiped from the earth', Shemot 9:15). The cognate Arabic root جحد shares the FIRST half of that range — 'to deny, disacknowledge' — but classical Arabic never developed the 'be destroyed' half. Saadia, translating God's warning to Pharaoh, reaches for the etymological cognate جحد (Form VIII اجتحد: ואגתחדת מן אלבלד 'and you would have been destroyed from the land') and stretches it to cover the Hebrew's destruction-sense — a sense Arabic speakers would not natively hear in the root. Blau flags exactly this (citing Derenbourg on this verse) as a Hebrew-influenced semantic extension. The move is the inverse of the usual translation direction: instead of finding the Arabic word that matches the Hebrew meaning, Saadia keeps the Hebrew ROOT (via its Arabic cognate) and lets the Hebrew semantics ride along. Pedagogically distinctive because it exposes the bilingual substrate of the Tafsir — Saadia thinking in Hebrew-Arabic cognate pairs, and willing to load an Arabic verb with a sense it only has in Hebrew.",
        "verses": [
            {"book": "Shemot", "ch": 9, "v": 15},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "جحد",
            "sense": "Blau (s.v. جحد) records the Form IV/VIII 'to destroy / be destroyed' as a Hebrew-influenced sense (השפעת העברית כחד/שמד), citing Derenbourg's note on Saadia at Shemot 9:15 (ותכחד = ואגתחדת). The classical Arabic root means only 'to deny'; the destruction-sense is the calque catalogued here.",
            "relation": "direct",
        },
    },

    # ---- TWIST — ezrach as 'pure-lineage native' -------------------------
    {
        "lemma_ja": "צריח",
        "variants": ["אלצריח", "צריחא", "צריחי"],
        "lemma_ar": "صريح",
        "root": "ص-ر-ح",
        "tier": "twist",
        "classical_en": "Classical Arabic صَرِيح = 'pure, unmixed, clear' — of lineage, 'of pure unmixed descent' (صريح النسب); of speech, 'explicit, plain'. The core sense is unmixed purity, especially of pedigree.",
        "classical_he": "صَرِيح בערבית הקלאסית = 'טהור, בלתי־מעורב, צלול' — ביוחסין, 'בן ייחוס טהור ובלתי־מעורב' (صريح النسب); בדיבור, 'מפורש, ברור'. הגרעין הוא טוהר בלתי־מעורב, ובמיוחד טוהר־יוחסין.",
        "saadia_en": "the native-born of pure descent — Saadia renders Hebrew אֶזְרָח ('native, full citizen') with صريح 'one of pure unmixed lineage', recasting biblical native-birth as a category of genealogical purity opposite the גֵּר / دخيل (incomer).",
        "saadia_he": "האזרח טהור־הייחוס — סעדיה מתרגם את אֶזְרָח ('יליד הארץ, אזרח גמור') באמצעות صريح 'בן ייחוס טהור ובלתי־מעורב', וממַסגר מחדש את האזרחות המקראית כקטגוריה של טוהר־יוחסין אל מול הגֵּר / دخيل (הנכרי הנספח).",
        "mechanism": "A legal-category reframe that imports a genealogical-purity lens onto biblical citizenship. Hebrew אֶזְרָח means simply 'native, home-born, full member of the community' (probably from a root for 'rising / springing from the soil'), and the Torah uses it to mark the born-Israelite as against the גֵּר, the resident alien. A neutral Arabic rendering would be بلدي or أهلي ('local, of the country'). Saadia instead chooses صريح — whose primary classical sense is 'pure, unmixed, of clear pedigree' (صريح النسب) — and pairs it antithetically with دخيل ('incomer, intruder', the word he uses for גֵּר): the Passover-law triad at Shemot 12:19 (וְאֶזְרַח הָאָרֶץ = וצריח אלבלד), 12:48 (כְּאֶזְרַח הָאָרֶץ = כצריח אלבלד), and 12:49 (לָאֶזְרָח = לאלצריח, opposite אלג'ריב אלדכ'יל). The choice silently converts the biblical native/sojourner distinction (a matter of birthplace and residence) into a native/incomer distinction framed by purity of descent — the born member is not merely 'local' but 'of unmixed stock'. Pedagogically distinctive because the lexical pairing صريح ↔ دخيل re-reads the Torah's inclusion-law (one law for native and stranger) through a genealogical register the Hebrew does not itself foreground.",
        "verses": [
            {"book": "Shemot", "ch": 12, "v": 19},
            {"book": "Shemot", "ch": 12, "v": 48},
            {"book": "Shemot", "ch": 12, "v": 49},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "صرح",
            "sense": "Blau (s.v. صرح, headword صريحي) glosses 'of pure race, native' and cites Saadia's rendering of אזרח at Shemot 12 — the native-of-pure-descent sense claimed here. The corpus surface is the base form צריח (صريح); Blau lemmatizes the nisba صريحي of the same root and sense.",
            "relation": "direct",
        },
    },

    # ---- TWIST — mistolel (hapax) reframed as 'detaining' ----------------
    {
        "lemma_ja": "מתרבץ",
        "variants": ["תרבץ", "מתרבצא"],
        "lemma_ar": "متربّص",
        "root": "ر-ب-ص",
        "tier": "twist",
        "classical_en": "Classical Arabic تَرَبَّصَ (Form V of ربص) = 'to wait, to expect, to lie in wait, to bide one's time' (Lane: to await, watch for). The active participle مُتَرَبِّص = 'one who waits / lies in wait'. The sense is expectant waiting, not detaining another.",
        "classical_he": "تَرَبَّصَ בערבית הקלאסית (בניין V של ربص) = 'לחכות, לצַפּות, לארוב, להמתין לשעת כושר' (ליין: להמתין, לארוב ל-). הבינוני הפעיל مُتَرَبِّص = 'הממתין / האורב'. המשמע הוא המתנה דרוכה, לא עיכוב הזולת.",
        "saadia_en": "holding back / detaining — Saadia renders the Hebrew hapax מִסְתּוֹלֵל with متربّص 'detaining (my people, so as not to release them)', reading Pharaoh's offense as obstruction rather than self-exaltation.",
        "saadia_he": "מעכב / עוצר — סעדיה מתרגם את ההפקס העברי מִסְתּוֹלֵל באמצעות متربّص 'המעכב (את עמי, לבל ישלחם)', וקורא את חטא פרעה כעיכוב ולא כהתנשאות.",
        "mechanism": "Exegetical reframe of an obscure Hebrew hapax through a sense-shifted Arabic participle. מִסְתּוֹלֵל (Shemot 9:17) is a hapax legomenon — the only Hitpael of the root ס-ל-ל in the Bible — traditionally read 'you still exalt yourself / lord it over my people' (from סלל 'to lift up, raise a highway'). Its meaning is genuinely uncertain. Saadia fixes it with متربّص in the clause ומהמאך מתרבץ' בקומי ללא תטלקהום ('and you are still detaining my people so as not to release them'), where the continuation 'so as not to release them' shows he reads the offense as obstruction — Pharaoh holding the people back from departure — rather than arrogance. But classical تربّص means 'to wait, to lie in wait, to bide one's time', an INTRANSITIVE posture of expectant waiting; Saadia bends it to a transitive 'detain, hold back (someone)', the sense Blau records (post-classical ربص + ب 'to put off, hold back', cited at this very verse). The move resolves a hapax not by etymology but by context-driven sense-selection, and in doing so shifts the participle from 'one who waits' to 'one who detains'. Pedagogically distinctive because it shows Saadia's hapax-strategy: when the Hebrew is opaque, pick an Arabic word whose range can be stretched to fit the verse's logic, and let the syntax (here the purpose-clause) carry the interpretation.",
        "verses": [
            {"book": "Shemot", "ch": 9, "v": 17},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "ربص",
            "sense": "Blau (s.v. ربص) records the post-classical transitive ربص + ب 'to put off, to hold back, to detain', citing Saadia at Shemot 9:17 (מסתולל = מתרבץ' ב-). Classical Arabic تربّص is the intransitive 'to wait / lie in wait'; the detaining sense applied to Pharaoh's obstruction is the divergence catalogued here.",
            "relation": "direct",
        },
    },
]


# ============================================================================
# Helpers
# ============================================================================

CONSUMED_LOG = [
    {"blau_id": 16530, "landed_as": "twist שריעה (Shemot 12:49+)", "note": "Heb תורה → Ar شريعة (Torah-as-sharīʿa calque)."},
    {"blau_id": 19552, "landed_as": "twist אלמהל (Shemot 34:6)", "note": "Heb אֶרֶךְ אַפַּיִם → Ar طويل المهل (anti-anthropomorphic)."},
    {"blau_id": 14480, "landed_as": "twist אגתחד (Shemot 9:15)", "note": "Heb וַתִּכָּחֵד → Ar اجتحد 'be destroyed' (Hebrew-driven calque)."},
    {"blau_id": 16947, "landed_as": "twist צריח (Shemot 12:19+)", "note": "Heb אֶזְרָח → Ar صريح 'of pure lineage' (legal-category reframe)."},
    {"blau_id": 15668, "landed_as": "twist מתרבץ (Shemot 9:17)", "note": "Heb מִסְתּוֹלֵל (hapax) → Ar متربّص 'detaining' (hapax reframe)."},
]


def _log_consumed(deferred_path: pathlib.Path) -> dict:
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
    if added:
        deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        json.loads(deferred_path.read_text())  # parse-check
    return {"phase3_r1_consumed_added": added}


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

    consumed_summary = {}
    if deferred_path.exists():
        consumed_summary = _log_consumed(deferred_path)

    print(f"Added {added} entries to {div_path.name}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")
    print(f"Deferred summary: {json.dumps(consumed_summary, ensure_ascii=False)}")


if __name__ == "__main__":
    main()

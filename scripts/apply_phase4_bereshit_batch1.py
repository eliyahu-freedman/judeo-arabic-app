"""
Phase 4 — Bereshit Batch 1.

Twelve hand-curated entries from blau_ids 13770-20000 of
data/_blau_saadia_candidates.json. Each one has been verified against
data/tafsir-bereshit-{ch}.json — the lemma surfaces in the cited verse
under a form reachable via prefix-strip + the variants list.

Tier breakdown:
  - 8 GLOSS  — non-cognate Heb→Ar pairings, register shifts
  - 4 NOTE   — semantic surprises with short stated mechanism

Deferred (logged separately in data/_blau_saadia_deferred.json):
  - 1 STRICT (twist-grade): 16430 سيد on Gen 49:8 (Saadia reframes
    Hebrew "yodukha" 'they will praise you' as denominative "yusayyiduunaka"
    'they will make you ruler' — paradigm political reading of Judah blessing)
  - 1 BORDERLINE: 18250 فضض on Gen 3:5 (Blau attests root فضض, but
    JA shows تنفض from نفض — root attribution requires deeper check)
  - Skips for this window are not enumerated; the survival rate inside
    this 50-candidate window is high enough that listing every miss
    bloats the log.

Apply pattern mirrors scripts/apply_round7_I_chunk1.py:422-469;
dedupe is on lemma_ja only (DivergenceEntry has no `id` field).
"""

import json
import pathlib
import sys
from collections import Counter


NEW_ENTRIES = [
    # ---- GLOSS — Gen 25:31, 25:33: Esau sells birthright -------------------
    {
        "lemma_ja": "בכורה",
        "variants": ["בכורתך", "בכורתה", "אלבכורה"],
        "lemma_ar": "بكورية",
        "root": "ب-ك-ر",
        "tier": "gloss",
        "classical_en": "firstborn-right, primogeniture status",
        "classical_he": "בְּכֹרָה",
        "saadia_en": "birthright",
        "saadia_he": "בכורה",
        "mechanism": "Standard JA noun for the legal status; Blau treats it under primogeniture rather than as a general 'firstness' abstract.",
        "verses": [
            {"book": "Bereshit", "ch": 25, "v": 31},
            {"book": "Bereshit", "ch": 25, "v": 33},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "بكر",
            "sense": "بكورية 'primogeniture' (alongside 'virginity'); Blau attests in the inheritance sense citing Saadia on Gen 25:31-34, noting alternation with the variant بكورة.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 50:23: third-generation descendants -------------------
    {
        "lemma_ja": "ת'ואלת'",
        "variants": ["ת'ואלת'א"],
        "lemma_ar": "ثوالث",
        "root": "ث-ل-ث",
        "tier": "gloss",
        "classical_en": "those of the third (generation), great-grandchildren",
        "classical_he": "בְּנֵי שִׁלֵּשִׁים",
        "saadia_en": "(children) of the third generation",
        "saadia_he": "בני שלישים, ניני־נכדים",
        "mechanism": "Saadia uses Arabic plural ثوالث (lit. 'thirds') as a fixed substantival for the biblical-Hebrew kinship term שלשים; Blau treats it as a denominative that surfaces also at Ex 20:5 (شَلاشِيم).",
        "verses": [{"book": "Bereshit", "ch": 50, "v": 23}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "ثلث",
            "sense": "ثوالث (plural of ثالث) 'those of the third generation' — Blau attests citing Saadia on Gen 50:23 ('בני שלשים' = ת'ואלת'א) and the parallel at Ex 20:5.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 39:21: Joseph favored in prison -----------------------
    {
        "lemma_ja": "חצ'אא",
        "variants": ["אלחצ'אא"],
        "lemma_ar": "حظاء",
        "root": "ح-ظ-و",
        "tier": "gloss",
        "classical_en": "grace, favor",
        "classical_he": "חֵן",
        "saadia_en": "favor",
        "saadia_he": "חן, חסד",
        "mechanism": "Saadia uses Arabic حظاء — formally a plural of حظوة 'favor', but here used as a singular — for Hebrew חֵן ('favor in the eyes of').",
        "verses": [{"book": "Bereshit", "ch": 39, "v": 21}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "حظو",
            "sense": "حظاء 'grace, favor' — ostensibly plural of حظوة but Saadia uses it as a singular; Blau records the JA usage citing Saadia on Gen 39:21.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 37:2: Joseph brings an evil report --------------------
    {
        "lemma_ja": "שנאעה",
        "variants": ["בשנאעה"],
        "lemma_ar": "شناعة",
        "root": "ش-ن-ع",
        "tier": "gloss",
        "classical_en": "an evil rumor, slander",
        "classical_he": "דִּבָּה רָעָה",
        "saadia_en": "an evil report",
        "saadia_he": "דיבה רעה, לשון הרע",
        "mechanism": "Non-cognate substantive: Saadia renders Hebrew דבה רעה ('an evil report') with the Arabic abstract شناعة 'rumor, slander' rather than the cognate دباب-derivatives.",
        "verses": [{"book": "Bereshit", "ch": 37, "v": 2}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "شنع",
            "sense": "شناعة 'rumor, slander' (not necessarily 'evil rumor') — Blau attests citing Saadia on Gen 37:2.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 8:22: post-flood seasons ------------------------------
    {
        "lemma_ja": "קייצ'",
        "variants": ["אלקייצ'"],
        "lemma_ar": "قيظ",
        "root": "ق-ي-ظ",
        "tier": "gloss",
        "classical_en": "midsummer heat (the hottest part of summer)",
        "classical_he": "קַיִץ",
        "saadia_en": "midsummer heat",
        "saadia_he": "קיץ, חום הקיץ",
        "mechanism": "Register choice: Saadia uses قيظ (specifically the hot core of summer) rather than the general صَيْف; the lexical pairing with cognate-sounding Hebrew קַיִץ is precise rather than approximate.",
        "verses": [{"book": "Bereshit", "ch": 8, "v": 22}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "قيظ",
            "sense": "قيظ 'summer (heat)' — Blau attests citing Saadia on Gen 8:22.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 49:9: Judah a lion's whelp ----------------------------
    {
        "lemma_ja": "לבו",
        "variants": [],
        "lemma_ar": "لبو",
        "root": "ل-ب-و",
        "tier": "gloss",
        "classical_en": "lion, lioness (high-register synonym)",
        "classical_he": "לָבִיא",
        "saadia_en": "lion",
        "saadia_he": "לביא, אריה",
        "mechanism": "High-register synonym: Saadia preserves the biblical-Hebrew elevation of לָבִיא over the prosaic אַרְיֵה by reaching for لبوة (formally f.) used as a masculine; the Aggron also pairs لبو ~ לביא.",
        "verses": [{"book": "Bereshit", "ch": 49, "v": 9}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "لبو",
            "sense": "لبو(ة) 'lion (lioness, used m.)' — Blau attests citing Saadia on Gen 49:9 and the Aggron 262:1 (לביא לבו).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 49:17: Dan a viper on the path ------------------------
    {
        "lemma_ja": "מטרון",
        "variants": ["כאלמטרון", "אלמטרון"],
        "lemma_ar": "مطرون",
        "root": "م-ط-ر",
        "tier": "gloss",
        "classical_en": "a kind of small fierce viper",
        "classical_he": "שְׁפִיפֹן",
        "saadia_en": "a striking viper",
        "saadia_he": "שפיפון, מין נחש קטן וארסי",
        "mechanism": "Non-cognate dialectal pairing: Saadia uses Arabic مطرون (Blau-Festschrift area 143-145) for Hebrew שְׁפִיפֹן — a regional Arabic term for the same viper class, not derivable from the standard ثعبان used elsewhere in the verse for נָחָשׁ.",
        "verses": [{"book": "Bereshit", "ch": 49, "v": 17}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "مطر",
            "sense": "مطرون 'a kind of viper' — Blau attests citing Saadia on Gen 49:17 ('שפיפון עלי אורח' = וכאלמטרון).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 49:15: Issachar bowed shoulder to burden --------------
    {
        "lemma_ja": "נקל",
        "variants": ["ללנקל", "אלנקל"],
        "lemma_ar": "نقل",
        "root": "ن-ق-ل",
        "tier": "gloss",
        "classical_en": "transport, carriage, a load to be borne",
        "classical_he": "סֵבֶל",
        "saadia_en": "burden-bearing",
        "saadia_he": "סבל, נשיאת משא",
        "mechanism": "Saadia substantivizes the act of bearing: the Hebrew verbal infinitive לִסְבֹּל ('to bear') becomes the Arabic noun نقل ('transport, carriage'), preserving the corvée-like load but as a thing rather than an action.",
        "verses": [{"book": "Bereshit", "ch": 49, "v": 15}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "نقل",
            "sense": "نقل 'transport, conveyance (especially of a burden)' — Blau attests citing Saadia on Gen 49:15 ('ויט שכמו לסבל' = פימד ענקה ללנקל).",
            "relation": "direct",
        },
    },
    # ---- NOTE — Gen 9:7: post-flood blessing to multiply -------------------
    {
        "lemma_ja": "אסעו",
        "variants": ["אסעי", "סעי"],
        "lemma_ar": "اسعوا",
        "root": "س-ع-ي",
        "tier": "note",
        "classical_en": "Form I سعى, classically 'to strive, walk briskly'",
        "classical_he": "סעי בבניין הראשון, פירושו המוקדם הוא 'להתאמץ, ללכת במהירות'",
        "saadia_en": "Form I سعى extended semantically to 'teem, swarm, multiply'",
        "saadia_he": "סעי בבניין הראשון, מורחב סמנטית ל'רחש, שרץ, התרבה'",
        "mechanism": "Saadia stretches Arabic سعى (classically 'to strive, run') to render Hebrew שָׁרַץ ('teem, multiply'). The extension brings the verb into the biblical reproductive-blessing field; Blau treats it as a marked semantic widening rather than a standard equivalence.",
        "verses": [{"book": "Bereshit", "ch": 9, "v": 7}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "سعي",
            "sense": "سعى 'in all its biblical senses (creep, teem, multiply, be fruitful)' — Blau records the wide extension citing Saadia.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Gen 38:26: Judah didn't give Tamar to Shelah ---------------
    {
        "lemma_ja": "אזווגהא",
        "variants": ["יזווג", "תזווג", "זוג'", "תזויג"],
        "lemma_ar": "أزوّجها",
        "root": "ز-و-ج",
        "tier": "note",
        "classical_en": "to give in marriage, the unmarked verb for 'I gave (her) (to him)' for a daughter-in-law",
        "classical_he": "לתת, להעניק (פועל סתמי לתיאור מתן בת לאיש)",
        "saadia_en": "Form II زوّج 'to marry off' — sharpens the legal kind of giving",
        "saadia_he": "זוג' בבניין השני, 'להשיא, לחתן' — מחדד את אופי המתן המשפטי",
        "mechanism": "Saadia reads Hebrew נְתַתִּיהָ ('I gave her') not as a generic transfer but specifically as a marriage transaction, rendering with Form II زوّج 'to marry off' rather than the general أعطى.",
        "verses": [{"book": "Bereshit", "ch": 38, "v": 26}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "زوج",
            "sense": "زوج Form II '(with و-)' 'to form a marriage alliance, give in marriage' — Blau records the JA usage; here on Gen 38:26 Saadia sharpens the Hebrew נְתַתִּיהָ into a marriage-specific act.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Gen 45:26: Jacob's heart on hearing Joseph lives -----------
    {
        "lemma_ja": "שכך",
        "variants": ["פשכך", "ישכך"],
        "lemma_ar": "شكّك",
        "root": "ش-ك-ك",
        "tier": "note",
        "classical_en": "(his heart) grew faint, slackened — the physiological reading of וַיָּפָג",
        "classical_he": "(לבו) פג, נחלש פיזית — הקריאה הפיזיולוגית של וַיָּפָג",
        "saadia_en": "(his heart) doubted — Form II شكّك 'to cause to doubt'",
        "saadia_he": "(לבו) הטיל ספק, חשש — שכך בבניין השני 'גרם להטיל ספק'",
        "mechanism": "Saadia reframes Jacob's reaction from physical faintness to cognitive doubt: וַיָּפָג לִבּוֹ ('his heart grew faint') becomes פשכך קלבה ('his heart doubted'). The verse's own continuation — 'because he did not believe them' — supports the cognitive reading Saadia pulls forward into the main verb.",
        "verses": [{"book": "Bereshit", "ch": 45, "v": 26}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "شكك",
            "sense": "Form II شكّك 'to cause doubt'; Blau records the JA Form II citing Saadia on Gen 45:26 ('ויפג לבו' = פשכך קלבה).",
            "relation": "direct",
        },
    },
    # ---- NOTE — Gen 49:5: Simeon and Levi's "weapons of violence" ----------
    {
        "lemma_ja": "פרצ'תהמא",
        "variants": ["פרצ'ה", "אלפרצ'ה"],
        "lemma_ar": "فرضتهما",
        "root": "ف-ر-ض",
        "tier": "note",
        "classical_en": "their weapons — the standard rendering of the disputed Hebrew מְכֵרֹתֵיהֶם",
        "classical_he": "כליהם — הקריאה הסטנדרטית של ה'מְכֵרֹתֵיהֶם' החידתי",
        "saadia_en": "their appointed-allotments — Saadia reads מְכֵרֹתֵיהֶם as 'fated portions', from فرض 'to appoint, allot'",
        "saadia_he": "מנותיהם הקצובות — רס״ג קורא 'מְכֵרֹתֵיהֶם' כ'חלקים שנקצבו', מן فرض",
        "mechanism": "The Hebrew hapax מְכֵרֹתֵיהֶם is famously disputed (LXX renders 'their conspiracies', Ibn Ezra 'their swords'); Saadia derives it from a root meaning 'allotment, divinely-fixed share', rendering with فَرْض. This is a lexical-theological choice that softens the violence into 'their appointed portion'.",
        "verses": [{"book": "Bereshit", "ch": 49, "v": 5}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "فرض",
            "sense": "فرضة 'an appointed/allotted portion' — Blau attests citing Saadia on Gen 49:5 ('כלי חמס מכרתיהם' = פי אלאת אלצ'לם פרצ'תהמא).",
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

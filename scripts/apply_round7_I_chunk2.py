#!/usr/bin/env python3
"""Phase 2 Round 7 Batch I — chunk 2 (25 candidates).

8 of the 25 are simply new surface forms on existing lemmas
(dhikr, rasm, alf, nazala, dhiraʿ, samiʿa, wajh, taʾiq) — patched in.
The remaining 17 are new entries.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Verbs ----------
    {
        "id": "tala-overlay",
        "lemma_ja": "טלא",
        "lemma_ar": "طَلَى",
        "root": "ṭ-l-y",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to coat, plate, overlay (a surface with metal, paint, pitch); to anoint",
        "gloss_he": "צִפָּה, מָשַׁח (בזהב/כסף וכד')",
        "saadia_note": "Saadia's regular gloss for Hebrew צִפָּה (overlay with gold/silver) in the Tabernacle construction passages (Exod 26-27; e.g. וטלאהא פצ'ה 'and he overlaid them with silver', Exod 27:10-11).",
        "source": "lane",
        "variants": [
            "וטלא", "פטלא",
            "טלאהא", "וטלאהא", "פטלאהא",
            "טלאה", "וטלאה", "טלאהם",
            "טלית", "טליתהא", "טלינא",
            "יטלי", "ויטלי",
            "מטלי", "מטליה", "מטליין",
            "מטלוין",
        ],
    },

    # ---------- Nouns / adjectives ----------
    {
        "id": "hakim-judge",
        "lemma_ja": "חאכם",
        "lemma_ar": "حَاكِم",
        "root": "ḥ-k-m",
        "pos": "noun / active participle (m.)",
        "gloss_en": "judge, ruler, magistrate; one who exercises authority",
        "gloss_he": "שׁוֹפֵט, שָׂר, פּוֹסֵק",
        "saadia_note": "Saadia's regular gloss for Hebrew שֹׁפֵט in the judicial passages (e.g. Deut 17:9, 17:12: ואלי' אלחאכם אלד'י ילי פי ד'אלך אלזמאן 'and to the judge who is in office in that time').",
        "source": "lane",
        "variants": [
            "אלחאכם", "ואלחאכם",
            "וחאכם", "באלחאכם", "ללחאכם",
            "חכאם", "אלחכאם", "ואלחכאם",
            "חאכים", "אלחאכים",
        ],
    },
    {
        "id": "hadhiq-skilled",
        "lemma_ja": "חאד'ק",
        "lemma_ar": "حَاذِق",
        "root": "ḥ-dh-q",
        "pos": "adjective / active participle (m.)",
        "gloss_en": "skilled, expert, accomplished (especially of a craftsman)",
        "gloss_he": "אֻמָּן, מָהִיר, מְלֶאכֶת חוֹשֵׁב",
        "saadia_note": "Saadia's regular gloss for Hebrew חוֹשֵׁב in the Tabernacle-craftsmanship formulas (e.g. Exod 26:1, 26:31: צנעה' חאד'ק 'the work of a skilled [craftsman]').",
        "source": "lane",
        "variants": [
            "אלחאד'ק", "ואלחאד'ק",
            "וחאד'ק", "באלחאד'ק",
            "חאד'קה", "אלחאד'קה",
            "חאד'קין", "אלחאד'קין",
            "חד'אק", "אלחד'אק",
        ],
    },
    {
        "id": "shahm-fat",
        "lemma_ja": "שחם",
        "lemma_ar": "شَحْم",
        "root": "sh-ḥ-m",
        "pos": "noun (m.)",
        "gloss_en": "fat, suet (of an animal); especially the fat reserved for the altar",
        "gloss_he": "חֵלֶב, שׁוּמָן",
        "saadia_note": "Saadia's regular gloss for Hebrew חֵלֶב — the fat of sacrificial animals that is to be burned on the altar (Lev 3-4, 7; Exod 29; passim). The verb shaḥuma = 'to grow fat'; the adjective shaḥīm = 'fatty'.",
        "source": "lane",
        "variants": [
            "אלשחם", "ואלשחם",
            "שחמה", "שחמהא", "שחמכם", "שחמהם",
            "באלשחם", "כשחם",
            "שחומה", "אלשחומה",
        ],
    },
    {
        "id": "hayda-menstruation",
        "lemma_ja": "חיצ'ה",
        "lemma_ar": "حَيْضَة",
        "root": "ḥ-y-ḍ",
        "pos": "noun (f.)",
        "gloss_en": "menstruation, menstrual flow",
        "gloss_he": "נִדָּה, וֶסֶת",
        "saadia_note": "Saadia's regular gloss for Hebrew נִדָּה in the impurity passages (Lev 12; Lev 15; Lev 18; Lev 20) — חיצ'תהא 'her menstruation' (Lev 12:2, 12:5).",
        "source": "lane",
        "variants": [
            "אלחיצ'ה", "ואלחיצ'ה",
            "חיצ'תהא", "חיצ'תך", "חיצ'תה",
            "חיצ' ", "אלחיצ'",
            "חאיצ'ה", "אלחאיצ'ה",
            "באלחיצ'ה",
        ],
    },
    {
        "id": "tisʿa-nine",
        "lemma_ja": "תסעה",
        "lemma_ar": "تِسْعَة",
        "root": "t-s-ʿ",
        "pos": "numeral",
        "gloss_en": "nine (masculine counted)",
        "gloss_he": "תִּשְׁעָה",
        "notes": "Arabic gender polarity: tisʿa (with tā' marbūṭa) counts masculine nouns; tisʿ counts feminine. The form תסעין = 'ninety'.",
        "source": "lane",
        "variants": [
            "ותסעה", "פתסעה",
            "אלתסעה", "ואלתסעה",
            "תסעין", "ותסעין",
            "תסעה' עשר", "תסעה ועשרין",
        ],
    },
    {
        "id": "ajnabi-foreigner",
        "lemma_ja": "אגנבי",
        "lemma_ar": "أَجْنَبِيّ",
        "root": "j-n-b",
        "pos": "adjective / noun (m.)",
        "gloss_en": "foreign, outsider, stranger; non-priestly (in cultic contexts)",
        "gloss_he": "נָכְרִי, זָר",
        "saadia_note": "Saadia's regular gloss for Hebrew זָר in cultic-disqualification contexts — 'an outsider/non-priest who approaches shall be put to death' (Num 1:51, 17:5 — ואי אגנבי תקדם אלי' ד'אלך פליקתל). Distinct from גריב (gharīb) 'stranger, sojourner' which Saadia uses for גֵּר.",
        "source": "lane",
        "variants": [
            "ואגנבי", "אלאגנבי", "ואלאגנבי",
            "באלאגנבי",
            "אגנבייה", "אלאגנבייה",
            "אגנבייין", "אלאגנבייין",
        ],
    },
    {
        "id": "mashriq-east",
        "lemma_ja": "משרק",
        "lemma_ar": "مَشْرِق",
        "root": "sh-r-q",
        "pos": "noun (m.)",
        "gloss_en": "east; the place of sunrise",
        "gloss_he": "מִזְרָח",
        "saadia_note": "Saadia's regular gloss for Hebrew מִזְרָח in directional descriptions — especially the layout of the tribes around the Tabernacle (Num 2:3, 10:5: אלנאזלין פי אלמשרק 'those encamped to the east').",
        "source": "lane",
        "variants": [
            "אלמשרק", "ואלמשרק",
            "באלמשרק", "במשרק",
            "ללמשרק", "ומשרק",
            "מן אלמשרק", "אלי' אלמשרק",
        ],
    },
    {
        "id": "batn-belly",
        "lemma_ja": "בטן",
        "lemma_ar": "بَطْن",
        "root": "b-ṭ-n",
        "pos": "noun (m.)",
        "gloss_en": "belly, abdomen, womb",
        "gloss_he": "בֶּטֶן, רֶחֶם",
        "saadia_note": "Saadia's regular gloss for Hebrew בֶּטֶן / רֶחֶם — both anatomical 'belly' and reproductive 'womb'. The phrase כל אוול בטן 'every first-of-the-womb' renders Heb פֶּטֶר רֶחֶם (Num 18:15).",
        "source": "lane",
        "variants": [
            "אלבטן", "ואלבטן",
            "בטנה", "בטנהא", "בטני", "בטנכם", "בטנהם",
            "מן בטן", "פי בטן",
            "אוול בטן", "אוואיל בטן",
            "בטון", "אלבטון",
        ],
    },

    # ---------- Function words ----------
    {
        "id": "thumma-then",
        "lemma_ja": "תם",
        "lemma_ar": "ثُمَّ",
        "root": "—",
        "pos": "conjunction",
        "gloss_en": "then, thereafter, afterwards (sequential — distinct from fa- 'and then immediately')",
        "gloss_he": "אַחַר כָּךְ, אָז, וְאַחֲרֵי כֵן",
        "notes": "Saadia uses tum (תם) rather than the more usual classical thumma (ת'ם, with apos) — scribal/orthographic variation. The sequential nuance (a clear interval between events) distinguishes it from fa- (immediate consequence) and wa- (mere conjunction).",
        "saadia_note": "Saadia's regular sequential conjunction at the head of new narrative units — often glosses Hebrew וַיְהִי-narrative openers (e.g. Num 13:1: תם כלם אללה מוסי' 'Then YHWH spoke to Moses'; Num 20:1; Exod 18:1).",
        "source": "lane",
        "variants": [
            "ות'ם", "ת'ם",
            "פת'ם", "פתם",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "yitro-name",
        "lemma_ja": "יתרו",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Jethro — priest of Midian, father-in-law of Moses",
        "gloss_he": "יִתְרוֹ, חוֹתֵן מֹשֶׁה",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ויתרו", "ליתרו", "ביתרו",
        ],
    },
    {
        "id": "eliab-name",
        "lemma_ja": "אליאב",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Eliab — (1) son of Helon, chieftain of Zebulun in the wilderness census; (2) son of Pallu (Reubenite), father of Dathan and Abiram",
        "gloss_he": "אֱלִיאָב",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ואליאב", "לאליאב", "באליאב",
            "אבן אליאב", "אבני אליאב",
        ],
    },
    {
        "id": "zin-place",
        "lemma_ja": "צין",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Zin — a wilderness south of Canaan, the southernmost section of the Israelite itinerary (Num 13:21; 20:1; 27:14; Deut 32:51)",
        "gloss_he": "מִדְבַּר צִן",
        "notes": "Distinct from סין (Sin, also a southern wilderness, Exod 16:1; 17:1). Saadia retains both Hebrew forms unchanged.",
        "source": "lane",
        "variants": [
            "וצין", "לצין", "בצין",
            "ברייה' צין", "ברייה צין",
        ],
    },
    {
        "id": "hittite-people",
        "lemma_ja": "חתיין",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun (gentilic plural)",
        "gloss_en": "Hittites — one of the seven Canaanite peoples; descendants of Heth son of Canaan",
        "gloss_he": "הַחִתִּי, הַחִתִּים",
        "notes": "Always plural-gentilic in Saadia (the -iyyīn ending). Frequently appears in the seven-nation list (Exod 13:5; Num 13:29; Deut 7:1).",
        "saadia_note": "Saadia retains the Hebrew name and uses the standard Arabic-style gentilic plural — see also כנעאניין, פרזיין, אמוריין, חויין, יבוסיין, גרגאשיין.",
        "source": "lane",
        "variants": [
            "אלחתיין", "ואלחתיין",
            "חתי", "אלחתי", "ואלחתי",   # singular gentilic
        ],
    },

    # ---------- More nouns ----------
    {
        "id": "shati-shore",
        "lemma_ja": "שאט",
        "lemma_ar": "شَاطِئ",
        "root": "sh-ṭ-ʾ",
        "pos": "noun (m.)",
        "gloss_en": "shore, bank (of a river, sea, or wadi)",
        "gloss_he": "חוֹף, שָׂפָה, גָּדָה",
        "saadia_note": "Saadia's regular gloss for Hebrew שָׂפָה / גְּדָה when describing the bank of a river, sea, or wadi (e.g. Num 13:29: עלי שאט אלארדון 'on the bank of the Jordan'; Gen 22:17: עלי' שאט אלבחר 'on the seashore').",
        "source": "lane",
        "variants": [
            "אלשאט", "ואלשאט",
            "שאטי", "אלשאטי", "ואלשאטי",
            "שאטא", "באלשאט", "ללשאט",
            "עלי שאט", "עלי' שאט",
        ],
    },
    {
        "id": "tifl-child",
        "lemma_ja": "טפל",
        "lemma_ar": "طِفْل",
        "root": "ṭ-f-l",
        "pos": "noun (m.)",
        "gloss_en": "child, infant, young one (esp. of human children); pl. aṭfāl = 'the little ones'",
        "gloss_he": "יֶלֶד, טַף",
        "saadia_note": "Saadia's regular gloss for Hebrew טַף (collective 'the little ones, dependents') throughout the Exodus and Numbers narratives (e.g. Num 14:31: ואטפאלכם 'and your little ones').",
        "source": "lane",
        "variants": [
            "אלטפל", "ואלטפל",
            "אטפאל", "אלאטפאל", "ואלאטפאל",
            "אטפאלכם", "ואטפאלכם", "אטפאלהם", "ואטפאלהם",
            "אטפאלנא", "ואטפאלנא", "אטפאלך", "ואטפאלך",
            "באלאטפאל", "ללאטפאל",
        ],
    },
    {
        "id": "taqa-able",
        "lemma_ja": "טאק",
        "lemma_ar": "طَاق",
        "root": "ṭ-w-q",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to be able, to have the power/capacity to (something)",
        "gloss_he": "יָכוֹל, הָיָה בִּיכָלְתּוֹ",
        "notes": "Distinct from the existing entry taʾiq-able (lemma טאיק), which is the active participle ṭāʾiq 'able [adj.]'. This is the finite-verb form. Often paired with an + verb: 'he was able to + INF'.",
        "saadia_note": "Saadia's regular gloss for Hebrew יָכֹל in narrative — e.g. Num 14:16 ממא לם יטיק 'because he was not able'; Gen 36:7 ולם יטיק בלד 'and the land was not able [to support them]'.",
        "source": "lane",
        "variants": [
            "טאקת", "טאקו", "טאקנא",
            "וטאק", "פטאק",
            "אטאק", "תטאק",
            "נטאק", "תטיק", "אטיק",
            "טאקה", "אלטאקה", "באלטאקה",
        ],
    },
]


VARIANTS_PATCH = {
    "dhikr-mention":  ["ואד'כר", "אד'כר", "פאד'כר"],
    "rasm-decree":    ["רסומי", "רסומה", "רסומהא", "רסומך", "רסומכם", "רסומהם"],
    "alf-thousand":   ["אלוף", "ואלוף", "אלאלוף", "ואלאלוף", "באלאלוף"],
    "nazala-descend": ["ינזלון", "וינזלון", "תנזלון", "ננזלון"],
    "dhiraʿ-cubit":   ["ד'ראעין", "ד'ראעי", "אלד'ראעין"],
    "samiʿa-hear":    ["אסמעו", "ואסמעו", "פאסמעו"],
    "wajh":           ["וגוההמא", "וגוההמ", "וגוההם", "וגוההן"],
    "taʾiq-able":     ["יטיק", "ויטיק", "תטיק"],
}


def main():
    path = pathlib.Path("data/dictionary-lane.json")
    if not path.exists():
        print(f"FATAL: {path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    d = json.loads(path.read_text())

    existing_ids = {e["id"] for e in d["entries"]}
    existing_lemmas = {e["lemma_ja"] for e in d["entries"]}
    added = 0
    skipped = []
    for entry in NEW_ENTRIES:
        if entry["id"] in existing_ids:
            skipped.append((entry["id"], "id exists"))
            continue
        if entry["lemma_ja"] in existing_lemmas:
            print(f"  [HOMOGRAPH] {entry['id']} lemma {entry['lemma_ja']} already exists — adding as second sense")
        d["entries"].append(entry)
        existing_ids.add(entry["id"])
        existing_lemmas.add(entry["lemma_ja"])
        added += 1

    by_id = {e["id"]: e for e in d["entries"]}
    variant_added = 0
    variant_skipped = []
    for entry_id, new_variants in VARIANTS_PATCH.items():
        if entry_id not in by_id:
            variant_skipped.append((entry_id, "id not found"))
            continue
        target = by_id[entry_id]
        existing_variants = target.setdefault("variants", [])
        for v in new_variants:
            if v in existing_variants:
                variant_skipped.append((entry_id, f"already had {v}"))
                continue
            existing_variants.append(v)
            variant_added += 1

    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    json.loads(path.read_text())

    print(f"Added {added} new entries. Skipped: {len(skipped)}")
    for s, reason in skipped:
        print(f"  - {s}: {reason}")
    print(f"Added {variant_added} variants. Skipped: {len(variant_skipped)}")
    for s, reason in variant_skipped:
        print(f"  - {s}: {reason}")
    print(f"Total entries now: {len(d['entries'])}")


if __name__ == "__main__":
    main()

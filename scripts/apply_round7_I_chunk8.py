#!/usr/bin/env python3
"""Phase 2 Round 7 Batch I — chunk 8 (25 candidates).

Final chunk of Round 7. Adds 21 new lemmas + 4 variant patches.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Verbs ----------
    {
        "id": "shariba-drink",
        "lemma_ja": "שרב",
        "lemma_ar": "شَرِب",
        "root": "sh-r-b",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to drink, sip, imbibe; (with min) to drink of",
        "gloss_he": "שָׁתָה",
        "saadia_note": "Saadia's regular gloss for Hebrew שָׁתָה — the daily-life verb and the cultic 'libation' contexts. Imperative ishrab = 'drink!' (Gen 24:14, 18, 46 — Rebekah at the well).",
        "source": "lane",
        "variants": [
            "אשרב", "ואשרב", "פאשרב", "ישרב", "וישרב", "תשרב", "נשרב",
            "ישרבון", "תשרבו", "תשרבון",
            "שרבת", "שרבו", "שרבוא", "שרבנא",
            "ושרב", "ושרבת", "ושרבו",
            "אשרבני", "אשרבונא", "ואשרבונא",
            "מאשרב", "אלמשרב", "ואלמשרב", "אלמשרוב",
        ],
    },
    {
        "id": "ʿada-still",
        "lemma_ja": "עאד",
        "lemma_ar": "عَاد",
        "root": "ʿ-w-d",
        "pos": "verb (Form I, perfect) / adverb",
        "gloss_en": "to return; (idiomatic with adjective-complement) 'to be still / yet [in a state]' (hal ʿāda X bāqī = 'is X still alive?')",
        "gloss_he": "עוֹדוֹ, חָזַר; הַעוֹד",
        "saadia_note": "Saadia's regular gloss for Hebrew הַעוֹדֶנּוּ / עוֹד in the recurring formula 'is your father still alive?' (Gen 43:7, 27, 28; 45:3, 26, 28 — הל עאד אביכם באקי 'is your father still surviving'). Also used in narrative 'returning' senses.",
        "source": "lane",
        "variants": [
            "ועאד", "פעאד",
            "עאדת", "עאדו", "עאדוא",
            "יעוד", "ויעוד", "תעוד", "אעוד", "נעוד",
            "ליעוד", "ליעודן",
            "הל עאד", "פהל עאד",
            "עאיד", "אלעאיד",
        ],
    },
    {
        "id": "khafa-fear",
        "lemma_ja": "כ'אף",
        "lemma_ar": "خَاف",
        "root": "kh-w-f",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to fear, be afraid (of); (idiomatic) 'fear not!' lā takhaf",
        "gloss_he": "פָּחַד, יָרֵא",
        "saadia_note": "Saadia's regular gloss for Hebrew יָרֵא — both 'fear of God' and 'fear of harm'. The recurring oracle formula 'fear not!' renders Heb אַל-תִּירָא (לא תכ'אפ; pl. לא תכ'אפו, Gen 43:23; 50:19, 21).",
        "source": "lane",
        "variants": [
            "כ'אפת", "כ'אפו", "כ'אפנא",
            "ולא כ'אפת", "פכ'אף",
            "תכ'אף", "ולא תכ'אף", "פלא תכ'אף", "אכ'אף", "נכ'אף",
            "תכ'אפו", "ולא תכ'אפו", "לא תכ'אפו",
            "יכ'אף", "ויכ'אף", "פיכ'אף", "יכ'אפון",
            "כ'איף", "אלכ'איף",
            "כ'וף", "אלכ'וף", "ואלכ'וף", "באלכ'וף",
        ],
    },
    {
        "id": "sara-walk",
        "lemma_ja": "סאר",
        "lemma_ar": "سَار",
        "root": "s-y-r",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to walk, go, travel, journey; (with bayn yaday) to go before / lead the way",
        "gloss_he": "הָלַךְ, צָעַד, נָסַע",
        "saadia_note": "Saadia's regular gloss for Hebrew הָלַךְ in the recurring 'YHWH (or his light) walks before you' formula (Deut 31:3 נורה יסיר בין ידיך; Exod 32:1 יסיר בין ידינא; Num 14:14). Also 'walk in his ways' (Deut 10:12 תסיר פי טרקה).",
        "source": "lane",
        "variants": [
            "סארת", "סארו", "סארוא", "סארנא",
            "וסאר", "וסארת", "וסארו", "פסאר",
            "יסיר", "ויסיר", "פיסיר", "תסיר",
            "אסיר", "נסיר",
            "יסירון", "תסירון", "תסירו", "נסירו",
            "סאיר", "אלסאיר", "ואלסאיר",
            "סארי", "אלסארי",
            "מסירה", "אלמסירה",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "dakka-pillar",
        "lemma_ja": "דכה",
        "lemma_ar": "دَكَّة",
        "root": "d-k-k",
        "pos": "noun (f.)",
        "gloss_en": "mound, raised platform; (in Saadia) a standing-stone monument, pillar",
        "gloss_he": "מַצֵּבָה",
        "saadia_note": "Saadia's regular gloss for Hebrew מַצֵּבָה — Jacob's pillar at Bethel (Gen 28:18, 22 — וגעלהא דכה 'and he made it a pillar'; 31:13, 45-52; 35:14, 20). Note: this is the cultic/memorial 'standing stone', distinct from the polytheistic מַצֵּבָה condemned in the Deuteronomic legislation.",
        "source": "lane",
        "variants": [
            "אלדכה", "ואלדכה",
            "ודכה", "באלדכה", "ללדכה",
            "דכאת", "אלדכאת", "ואלדכאת",
        ],
    },
    {
        "id": "adhn-ear",
        "lemma_ja": "אד'ן",
        "lemma_ar": "أُذُن",
        "root": "ʔ-dh-n",
        "pos": "noun (f.) / particle",
        "gloss_en": "(1) ear (anatomical); (2) particle idhan = 'truly, indeed, in fact; therefore, in that case'",
        "gloss_he": "(1) אֹזֶן; (2) אַכֵן, אֲזַי",
        "notes": "The two senses share the same surface but are etymologically distinct (ʔ-dh-n 'ear' vs. the particle idhan from ʔ-dh-n 'permission/then'). Context disambiguates.",
        "saadia_note": "Saadia uses אד'ן in both senses: (1) anatomical ear in the priestly consecration and leper-purification rites (Exod 29:20 שחמה' אד'ן הרון 'the lobe of Aaron's ear'; Lev 14:14); (2) the truly/indeed particle at sudden realization (Gen 28:16 אד'ן נור אללה פי הד'א אלמוצ'ע 'truly YHWH's light is in this place' = אָכֵן יֵשׁ יְהוָה בַּמָּקוֹם הַזֶּה).",
        "source": "lane",
        "variants": [
            "אלאד'ן", "ואלאד'ן",
            "אד'אן", "אלאד'אן", "ואלאד'אן", "שחמאת אד'אן",
            "אד'נה", "אד'נהא", "אד'נכם",
            "ואד'ן", "פאד'ן",
        ],
    },
    {
        "id": "khatim-seal",
        "lemma_ja": "כ'אתם",
        "lemma_ar": "خَاتَم",
        "root": "kh-t-m",
        "pos": "noun (m.)",
        "gloss_en": "seal, signet, signet-ring (used both as personal authentication and as an engraving tool)",
        "gloss_he": "חוֹתָם, טַבַּעַת",
        "saadia_note": "Saadia's regular gloss for Hebrew חוֹתָם / חוֹתֶמֶת — Judah's signet given as Tamar's pledge (Gen 38:18, 25 הד'א אלכ'אתם); the engraving of priestly-breastplate names (Exod 28:11, 21, 36; 39:6, 14, 30: כנקש אלכ'אתם 'like the engraving of a seal').",
        "source": "lane",
        "variants": [
            "אלכ'אתם", "ואלכ'אתם",
            "וכ'אתם", "באלכ'אתם",
            "כ'אתמה", "כ'אתמהא", "כ'אתמך",
            "כ'ואתם", "אלכ'ואתם",
            "כנקש אלכ'אתם",
        ],
    },
    {
        "id": "ruh-spirit",
        "lemma_ja": "רוח",
        "lemma_ar": "رُوح",
        "root": "r-w-ḥ",
        "pos": "noun (f.)",
        "gloss_en": "spirit, soul, breath; vital principle; (in theological contexts) the divine spirit",
        "gloss_he": "רוּחַ, נֶפֶשׁ",
        "saadia_note": "Saadia's regular gloss for Hebrew רוּחַ — both the divine 'spirit of God' (Gen 41:38 רוח אללה; Num 11:17, 25, 26, 29; Num 24:2) and the human-vital 'spirit revived' (Gen 45:27 פעאשת רוח יעקוב). Saadia uses different lexical strategies for רוח-as-wind (typically ריח) and רוח-as-spirit (רוח).",
        "source": "lane",
        "variants": [
            "אלרוח", "ואלרוח",
            "ורוח", "באלרוח", "ללרוח",
            "רוחי", "רוחה", "רוחהא", "רוחכם", "רוחהם",
            "ארואח", "אלארואח", "ואלארואח", "ארואחהם",
            "רוח אללה", "רוחה אלקדס",
        ],
    },
    {
        "id": "wariq-silver",
        "lemma_ja": "ורק",
        "lemma_ar": "وَرِق",
        "root": "w-r-q",
        "pos": "noun (m., collective)",
        "gloss_en": "silver (especially as currency, minted silver coinage)",
        "gloss_he": "כֶּסֶף (כמטבע, מטבעות כסף)",
        "notes": "Distinct from the noun fiḍḍa (פצ'ה) 'silver' as a metal — wariq specifically denotes coined / monetary silver.",
        "saadia_note": "Saadia's regular gloss for Hebrew כֶּסֶף in monetary contexts (currency for the famine, slave-purchases, indemnities) — Gen 47:14-15: אלורק 'the silver', 'until the silver ran out' (פני אלורק). Saadia uses fiḍḍa (פצ'ה) for non-monetary silver (Tabernacle utensils, raw metal).",
        "source": "lane",
        "variants": [
            "אלורק", "ואלורק",
            "וורק", "באלורק",
            "ורקא", "ללורק",
        ],
    },
    {
        "id": "zilf-hoof",
        "lemma_ja": "צ'לף",
        "lemma_ar": "ظِلْف",
        "root": "ẓ-l-f",
        "pos": "noun (m.)",
        "gloss_en": "cloven hoof (of ruminants — sheep, goat, cattle)",
        "gloss_he": "פַּרְסָה (שְׁסוּעָה)",
        "saadia_note": "Saadia's regular gloss for Hebrew פַּרְסָה in the clean-animal criteria of Lev 11 and Deut 14:6-8 — מצ'לפה בצ'לף 'cleft-hoofed in its hoof'.",
        "source": "lane",
        "variants": [
            "אלצ'לף", "ואלצ'לף",
            "וצ'לף", "באלצ'לף", "בצ'לף",
            "אצ'לאף", "אלאצ'לאף", "ואלאצ'לאף", "באצ'לאף",
            "אצ'לאפהא", "אצ'לאפה",
            "מצ'לף", "אלמצ'לף", "מצ'לפה", "אלמצ'לפה",
            "מצ'לפין", "אלמצ'לפין", "ואלמצ'לפין",
        ],
    },
    {
        "id": "ightirar-rumination",
        "lemma_ja": "אגתראר",
        "lemma_ar": "اِجْتِرَار",
        "root": "j-r-r",
        "pos": "noun (m., Form-VIII verbal-noun)",
        "gloss_en": "rumination, chewing the cud (of ruminant animals)",
        "gloss_he": "הַעֲלָאַת גֵּרָה",
        "saadia_note": "Saadia's regular gloss for Hebrew גֵּרָה in the clean-animal criteria (Lev 11; Deut 14:6-7) — מצעדה אגתראר 'bringing up the cud'. The verbal form ijtarra = 'to ruminate, chew the cud'; the active ptcp mujtirr.",
        "source": "lane",
        "variants": [
            "אלאגתראר", "ואלאגתראר",
            "באלאגתראר", "מן אלאגתראר",
            "מגתר", "אלמגתר", "ואלמגתר",
            "מצעדי אלאגתראר",
            "יגתר", "לא יגתר",
        ],
    },
    {
        "id": "khamir-leaven",
        "lemma_ja": "כ'מיר",
        "lemma_ar": "خَمِير",
        "root": "kh-m-r",
        "pos": "noun (m.)",
        "gloss_en": "leaven, leavened bread; (broader) anything that has fermented",
        "gloss_he": "חָמֵץ, שְׂאוֹר",
        "notes": "Distinct from khamr 'wine' (also kh-m-r). The Passover-leaven prohibition uses khamīr; the wine sense uses khamr.",
        "saadia_note": "Saadia's regular gloss for Hebrew חָמֵץ in the Passover prohibitions (Exod 12:15, 19, 20; Exod 13:7; Lev 2:11; Deut 16:3-4 — ולא ירא לך כ'מיר 'and no leaven shall be seen by you'). The leavened-loaf object is al-mukhammar (אלמכ'מר).",
        "source": "lane",
        "variants": [
            "אלכ'מיר", "ואלכ'מיר",
            "וכ'מיר", "באלכ'מיר",
            "כל כ'מיר", "מן כ'מיר",
            "מכ'מר", "אלמכ'מר", "ואלמכ'מר",
        ],
    },
    {
        "id": "jarad-locusts",
        "lemma_ja": "גראד",
        "lemma_ar": "جَرَاد",
        "root": "j-r-d",
        "pos": "noun (m., collective)",
        "gloss_en": "locust, locusts (the swarming grasshopper)",
        "gloss_he": "אַרְבֶּה",
        "saadia_note": "Saadia's regular gloss for Hebrew אַרְבֶּה — the eighth plague (Exod 10:4-19); the destructive-pestilence-on-crops formulas (Deut 28:38, 42); the clean-insect list (Lev 11:22).",
        "source": "lane",
        "variants": [
            "אלגראד", "ואלגראד",
            "וגראד", "באלגראד",
            "ללגראד", "כאלגראד",
        ],
    },
    {
        "id": "halqa-ring",
        "lemma_ja": "חלקה",
        "lemma_ar": "حَلْقَة",
        "root": "ḥ-l-q",
        "pos": "noun (f.)",
        "gloss_en": "ring, loop, link (especially of metal — the gold rings of the Tabernacle furnishings)",
        "gloss_he": "טַבַּעַת",
        "saadia_note": "Saadia's regular gloss for Hebrew טַבַּעַת in the Tabernacle-construction passages (Exod 25:12-15, 26-27; 26:24, 29; 27:4, 7; 28:23-28; 30:4; 35:22; 36:34; 37:3-5, 13-14, 27; 38:5, 7; 39:16-21). Plural ḥalaq, dual ḥalqatān.",
        "source": "lane",
        "variants": [
            "אלחלקה", "ואלחלקה",
            "וחלקה", "באלחלקה",
            "חלק", "אלחלק", "ואלחלק", "באלחלק",
            "חלקתין", "אלחלקתין",
            "חלקאת", "אלחלקאת",
        ],
    },
    {
        "id": "hashiya-edge",
        "lemma_ja": "חאשיה",
        "lemma_ar": "حَاشِيَة",
        "root": "ḥ-sh-y",
        "pos": "noun (f.)",
        "gloss_en": "edge, border, margin (of a curtain, garment, page)",
        "gloss_he": "שָׂפָה (של יריעה)",
        "saadia_note": "Saadia's regular gloss for Hebrew שְׂפַת (in the construct 'edge of') in the Tabernacle-curtain passages (Exod 26:4, 10; 36:11, 17 — חאשיה' אלשקה 'the edge of the curtain').",
        "source": "lane",
        "variants": [
            "אלחאשיה", "ואלחאשיה",
            "וחאשיה", "באלחאשיה",
            "חאשיה' אלשקה",
            "חואשי", "אלחואשי", "ואלחואשי",
        ],
    },
    {
        "id": "mahabb-direction",
        "lemma_ja": "מהב",
        "lemma_ar": "مَهَبّ",
        "root": "h-b-b",
        "pos": "noun (m.)",
        "gloss_en": "direction (of the wind); compass-quarter, side",
        "gloss_he": "צַד, רוּחַ (כיוון רוח)",
        "saadia_note": "Saadia's regular gloss for Hebrew פֵּאָה in the Tabernacle-construction directional formulas (Exod 26:18, 20, 27, 35; 27:9, 11, 12, 13; 36:23, 25, 32 — מן גהה' מהב אלגנוב 'from the southern direction'; מן גהה' מהב אלשמאל 'from the northern direction').",
        "source": "lane",
        "variants": [
            "אלמהב", "ואלמהב",
            "ומהב", "באלמהב",
            "מהאב", "אלמהאב",
            "מהב אלגנוב", "מהב אלשמאל", "מהב אלמשרק", "מהב אלמג'רב",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "hamor-name",
        "lemma_ja": "חמור",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Hamor — Hivite chieftain of Shechem; father of Shechem the violator of Dinah (Gen 33:19; 34 passim; Josh 24:32; Judg 9:28)",
        "gloss_he": "חֲמוֹר אֲבִי שְׁכֶם",
        "saadia_note": "Saadia retains the Hebrew name unchanged. The homograph with ḥamār 'donkey' is purely orthographic.",
        "source": "lane",
        "variants": [
            "וחמור", "לחמור", "בחמור",
            "אבן חמור", "בני חמור",
        ],
    },
    {
        "id": "shechem-name",
        "lemma_ja": "שכם",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Shechem — (1) son of Hamor the Hivite, violator of Dinah (Gen 33:19; 34); (2) the city in the central hill country between Mts. Gerizim and Ebal (Gen 12:6; 33:18; 37:12-14; Num 26:31; Josh 24:1, 32)",
        "gloss_he": "שְׁכֶם",
        "saadia_note": "Saadia retains the Hebrew name unchanged for both senses.",
        "source": "lane",
        "variants": [
            "ושכם", "לשכם", "בשכם",
            "אבן שכם", "בית שכם",
            "מן שכם", "אלי' שכם",
        ],
    },
]


VARIANTS_PATCH = {
    "raʾa-see":       ["ירא", "וירא", "תרא", "ותרא", "פירא", "פתרא", "יראה", "וירוא", "יראון", "וירון"],
    "taʾiq-able":     ["יטיקו", "ויטיקו", "תטיקו", "פיטיקו"],
    "hafiza-keep":    ["ותחפץ", "פתחפץ", "ותחפצ'", "פתחפצ'"],
    "zawj-spouse":    ["יתזווג", "ויתזווג", "ויתזווגן", "תזווג", "ותזווג",
                       "אתזווג", "נתזווג", "ליתזווג", "לתזווג"],
}

STARTER_VARIANTS_PATCH = {}


def main():
    lane_path = pathlib.Path("data/dictionary-lane.json")
    starter_path = pathlib.Path("data/dictionary-starter.json")
    d = json.loads(lane_path.read_text())
    ds = json.loads(starter_path.read_text())

    existing_ids = {e["id"] for e in d["entries"]}
    existing_lemmas = {e["lemma_ja"] for e in d["entries"]}
    added = 0; skipped = []
    for entry in NEW_ENTRIES:
        if entry["id"] in existing_ids:
            skipped.append((entry["id"], "id exists")); continue
        if entry["lemma_ja"] in existing_lemmas:
            print(f"  [HOMOGRAPH] {entry['id']} lemma {entry['lemma_ja']} already exists — adding as second sense")
        d["entries"].append(entry)
        existing_ids.add(entry["id"]); existing_lemmas.add(entry["lemma_ja"]); added += 1

    by_id = {e["id"]: e for e in d["entries"]}
    variant_added = 0; variant_skipped = []
    for entry_id, new_variants in VARIANTS_PATCH.items():
        if entry_id not in by_id:
            variant_skipped.append((entry_id, "id not found in lane")); continue
        target = by_id[entry_id]; existing_variants = target.setdefault("variants", [])
        for v in new_variants:
            if v in existing_variants:
                variant_skipped.append((entry_id, f"already had {v}")); continue
            existing_variants.append(v); variant_added += 1

    by_id_s = {e["id"]: e for e in ds["entries"]}
    starter_variant_added = 0
    for entry_id, new_variants in STARTER_VARIANTS_PATCH.items():
        if entry_id not in by_id_s:
            variant_skipped.append((entry_id, "id not found in starter")); continue
        target = by_id_s[entry_id]; existing_variants = target.setdefault("variants", [])
        for v in new_variants:
            if v in existing_variants:
                variant_skipped.append((entry_id, f"already had {v}")); continue
            existing_variants.append(v); starter_variant_added += 1

    lane_path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    starter_path.write_text(json.dumps(ds, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text()); json.loads(starter_path.read_text())

    print(f"Added {added} new entries (lane). Skipped: {len(skipped)}")
    for s, reason in skipped: print(f"  - {s}: {reason}")
    print(f"Added {variant_added} lane variants + {starter_variant_added} starter variants. Skipped: {len(variant_skipped)}")
    for s, reason in variant_skipped: print(f"  - {s}: {reason}")
    print(f"Total lane entries: {len(d['entries'])}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Phase 2 Round 7 Batch I — chunk 7 (25 candidates).

Mixed bag: narrative verbs, livestock/property vocab, Tabernacle illumination
vocab, more proper nouns. 17 new + 7 variant patches.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Function-word / "this (f)" alt ----------
    {
        "id": "aya-verse",
        "lemma_ja": "אייה",
        "lemma_ar": "آيَة",
        "root": "ʔ-y-y",
        "pos": "noun (f.)",
        "gloss_en": "sign, token; (in Quranic and Saadianic usage) a scriptural verse, a wonder",
        "gloss_he": "אוֹת, מוֹפֵת; פָּסוּק",
        "saadia_note": "Saadia uses āya for Hebrew אוֹת (sign, miraculous portent) — the signs of Moses (Exod 4; Num 14:11, 14:22). The form אייה' (with trailing apos) is the construct.",
        "source": "lane",
        "variants": [
            "ואייה", "אלאייה", "אלאייה'", "ואלאייה",
            "אייאת", "אלאייאת", "ואלאייאת", "באלאייאת",
            "אייה'",
        ],
    },

    # ---------- Verbs ----------
    {
        "id": "hayya-live",
        "lemma_ja": "חיא",
        "lemma_ar": "حَيَّ",
        "root": "ḥ-y-y",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to live, be alive, come to life",
        "gloss_he": "חַי, חָיָה",
        "saadia_note": "Saadia's regular gloss for Hebrew חַי / חָיָה in the live-or-die formulas — 'oh that Ishmael might live before you' (Gen 17:18 לית אסמאעיל יחיא); 'woe to the one who lives' (Num 24:23).",
        "source": "lane",
        "variants": [
            "יחיא", "ויחיא", "פיחיא",
            "תחיא", "אחיא", "נחיא",
            "יחיון", "ויחיון", "תחיון",
            "חיית", "חייתם", "חיינא",
            "חי", "אלחי", "ואלחי",
            "חיאה", "אלחיאה", "ואלחיאה", "באלחיאה",
            "חיאת", "אלחיאת",
        ],
    },
    {
        "id": "ʿaqada-bind",
        "lemma_ja": "עקד",
        "lemma_ar": "عَقَد",
        "root": "ʿ-q-d",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to tie, bind, knot, contract; (figuratively) to make a binding agreement, vow",
        "gloss_he": "קָשַׁר, אָסַר (נדר על נפש)",
        "saadia_note": "Saadia's regular gloss for Hebrew אָסַר אִסָּר in the vows pericope (Num 30: עקד עקודהא 'she has bound her bindings'). The cognate noun ʿaqd / ʿuqūd = 'contract, knot, binding-vow'.",
        "source": "lane",
        "variants": [
            "עקדת", "עקדתה", "עקדהא", "עקדנא",
            "ועקד", "ועקדת", "פעקדת", "פעקד",
            "יעקד", "ויעקד", "תעקד",
            "אעקד", "נעקד",
            "מעקוד", "אלמעקוד",
            "עקד", "אלעקד", "ואלעקד", "עקוד", "אלעקוד", "עקודהא", "ועקודהא",
        ],
    },
    {
        "id": "fana-perish",
        "lemma_ja": "פני",
        "lemma_ar": "فَنِيَ",
        "root": "f-n-y",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to perish, come to an end, be consumed, be exhausted; to die out",
        "gloss_he": "כָּלָה, תָּם, פָּסַק",
        "saadia_note": "Saadia's regular gloss for Hebrew תָּם / כָּלָה in extinction-formulas — 'until all that generation died out' (Num 32:13 אלי' אן פני גמיע אלגיל; Deut 2:14-15); 'the money ran out' (Gen 47:15 פני אלורק 'the silver was exhausted').",
        "source": "lane",
        "variants": [
            "פנא", "ופני", "פפני",
            "פניו", "פניוא", "ופניו",
            "יפני", "ויפני", "תפני",
            "אפני", "נפני",
            "פאני", "אלפאני", "פאניה",
        ],
    },
    {
        "id": "kamala-complete",
        "lemma_ja": "כמל",
        "lemma_ar": "كَمَل",
        "root": "k-m-l",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to be complete, be finished, come to fullness; (with subject = 'days') to be fulfilled (of a period of time)",
        "gloss_he": "תַּם, נִשְׁלַם, נִגְמַר",
        "saadia_note": "Saadia's regular gloss for Hebrew וַיְכֻלּוּ / וַתִּמְלָאוּ — 'the heavens and earth were completed' (Gen 2:1 כמלת אלסמאואת); 'her days to give birth were fulfilled' (Gen 25:24 ולמא כמלת איאם ולאדהא). Cognate noun kamāl is in the separate kamal-completion entry.",
        "source": "lane",
        "variants": [
            "כמלת", "כמלו", "כמלוא", "וכמל", "וכמלת", "פכמלת",
            "יכמל", "ויכמל", "תכמל",
            "אכמל", "נכמל",
            "כאמל", "אלכאמל", "ואלכאמל",
            "כאמלה", "אלכאמלה",
            "מתכאמל",
        ],
    },
    {
        "id": "dafana-bury",
        "lemma_ja": "דפן",
        "lemma_ar": "دَفَن",
        "root": "d-f-n",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to bury (a corpse), inter; to conceal in the ground",
        "gloss_he": "קָבַר",
        "saadia_note": "Saadia's regular gloss for Hebrew קָבַר in the burial-narratives — Abraham burying Sarah (Gen 23:4-19 אדפן מייתי 'that I may bury my dead'); the patriarchal burials at Machpelah; Joseph's burial requests (Gen 50).",
        "source": "lane",
        "variants": [
            "דפנת", "דפנו", "דפנוא", "דפנתה", "דפנהא",
            "ודפן", "ודפנת", "ודפנו", "פדפן",
            "אדפן", "תדפן", "ידפן", "וידפן", "נדפן",
            "תדפנו", "תדפנון", "ידפנון",
            "אלדפן", "ואלדפן",
            "מדפון", "אלמדפון", "מדפנא",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "mashiya-livestock",
        "lemma_ja": "מאשיה",
        "lemma_ar": "مَاشِيَة",
        "root": "m-sh-y",
        "pos": "noun (f., collective)",
        "gloss_en": "livestock, cattle (the animals that 'walk', as opposed to fixed property)",
        "gloss_he": "מִקְנֶה",
        "notes": "Plural mawāshī (מואשי).",
        "saadia_note": "Saadia's regular gloss for Hebrew מִקְנֶה in property-and-livestock contexts (Num 32:1, 4: ומאשיה כת'ירה 'and great livestock'; Gen 46:32; 47:6; Exod 12:38).",
        "source": "lane",
        "variants": [
            "אלמאשיה", "ואלמאשיה",
            "ומאשיה", "באלמאשיה", "ללמאשיה",
            "מאשיתה", "מאשיתהא", "מאשיתהם", "מאשיתי",
            "מואשי", "אלמואשי", "ואלמואשי", "ומואשי", "מואשיהם",
            "רעא מאשיה", "רעא אלמאשיה",
        ],
    },
    {
        "id": "ruʿah-shepherds",
        "lemma_ja": "רעא",
        "lemma_ar": "رُعَاة",
        "root": "r-ʿ-y",
        "pos": "noun (m., plural) / verb",
        "gloss_en": "(1) shepherds (plural of rāʿī); (2) to pasture, tend a flock (as verb)",
        "gloss_he": "רוֹעִים; לִרְעוֹת",
        "saadia_note": "Saadia's regular gloss for Hebrew רוֹעִים in pastoral narratives — 'a dispute arose between the herdsmen of Abram and the herdsmen of Lot' (Gen 13:7 בין רעא מאשיה' אברם), 'the shepherds gathered' (Gen 29:3, 8).",
        "source": "lane",
        "variants": [
            "אלרעא", "ואלרעא",
            "ורעא", "באלרעא", "ללרעא",
            "ראעי", "אלראעי", "ואלראעי",
            "ראעא", "ראעאה",
            "רעאתי", "ורעאתי", "רעאתך", "רעאתה", "רעאתהא", "רעאתהם",
            "רעא מאשיה",
        ],
    },
    {
        "id": "hima-refuge",
        "lemma_ja": "חמא",
        "lemma_ar": "حِمَى",
        "root": "ḥ-m-y",
        "pos": "noun (m.)",
        "gloss_en": "protected enclosure, sanctuary, refuge; an asylum-area",
        "gloss_he": "מִקְלָט",
        "saadia_note": "Saadia's regular gloss for Hebrew עִיר מִקְלָט ('city of refuge') — Num 35:11-15, Deut 19:1-13 (קרא חמא 'cities of refuge'; קרי' אלחמא).",
        "source": "lane",
        "variants": [
            "אלחמא", "ואלחמא",
            "וחמא", "באלחמא", "ללחמא",
            "קרא חמא", "קרי' חמא", "קרי' אלחמא",
        ],
    },
    {
        "id": "idaʾa-illumination",
        "lemma_ja": "אצ'אה",
        "lemma_ar": "إِضَاءَة",
        "root": "ḍ-w-ʾ",
        "pos": "noun (f., verbal-noun)",
        "gloss_en": "illumination, giving-of-light, shining; (in Saadia) the act of lighting the lamps / luminaries",
        "gloss_he": "הָאָרָה, הַדְלָקָה",
        "saadia_note": "Saadia's regular gloss for Hebrew לְהָאִיר in the luminary-creation and lampstand-oil passages — 'a luminary for illumination by day' (Gen 1:16 לאלאצ'אה פי אלנהאר); 'oil for the lighting' (Exod 25:6; 27:20; 35:14; Lev 24:2).",
        "source": "lane",
        "variants": [
            "אלאצ'אה", "ואלאצ'אה",
            "באלאצ'אה", "לאלאצ'אה", "ללאצ'אה",
            "אצ'אא", "אלאצ'אא",
            "אצ'יא", "אלאצ'יא",
        ],
    },
    {
        "id": "ʿard-width",
        "lemma_ja": "ערצ'",
        "lemma_ar": "عَرْض",
        "root": "ʿ-r-ḍ",
        "pos": "noun (m.)",
        "gloss_en": "width, breadth; (geometrically) the lateral dimension (paired with ṭūl 'length')",
        "gloss_he": "רֹחַב",
        "saadia_note": "Saadia's regular gloss for Hebrew רֹחַב in measurement passages — both Tabernacle dimensions (Exod 26:2 וערצ'הא ארבעה' אד'רע) and land-extent ('walk through the land its length and width' Gen 13:17 טולהא וערצ'הא).",
        "source": "lane",
        "variants": [
            "אלערצ'", "ואלערצ'",
            "וערצ'", "באלערצ'",
            "ערצ'ה", "ערצ'הא", "ערצ'הם", "ערצ'כם",
            "וערצ'הא", "וערצ'ה", "וערצ'כם",
            "טולהא וערצ'הא",
        ],
    },
    {
        "id": "shajara-tree",
        "lemma_ja": "שגרה",
        "lemma_ar": "شَجَرَة",
        "root": "sh-j-r",
        "pos": "noun (f.)",
        "gloss_en": "tree, plant, shrub (with a woody stem)",
        "gloss_he": "עֵץ, אִילָן",
        "saadia_note": "Saadia's regular gloss for Hebrew עֵץ (both singular tree and collective). Frequent in narrative ('rest under the tree' Gen 18:4, 8 תחת אלשגרה) and theological-symbolic ('the tree of life, the tree of knowledge of good and evil' Gen 2:9 — שגרה' אלחיאה / שגרה' מערפה' אלכ'יר ואלשר).",
        "source": "lane",
        "variants": [
            "אלשגרה", "ואלשגרה",
            "ושגרה", "באלשגרה", "ללשגרה",
            "תחת אלשגרה",
            "שגר", "אלשגר", "ואלשגר", "באלשגר",
            "אשגאר", "אלאשגאר", "ואלאשגאר",
            "שגרה' אלחיאה", "שגרה' מערפה' אלכ'יר ואלשר",
        ],
    },
    {
        "id": "qibala-facing",
        "lemma_ja": "קבאלה",
        "lemma_ar": "قُبَالَة",
        "root": "q-b-l",
        "pos": "preposition / adverb",
        "gloss_en": "facing, opposite, in front of, across-from",
        "gloss_he": "מוּל, נֹכַח, לְעֻמַּת",
        "notes": "Synonym of ḥidhāʾ (חד'א, also 'facing') — Saadia uses both, sometimes interchangeably.",
        "source": "lane",
        "variants": [
            "אלקבאלה", "ואלקבאלה",
            "בקבאלה", "באלקבאלה",
            "וקבאלה", "פקבאלה",
        ],
    },
    {
        "id": "jamal-camel",
        "lemma_ja": "גמל",
        "lemma_ar": "جَمَل",
        "root": "j-m-l",
        "pos": "noun (m.)",
        "gloss_en": "camel; pl. jimāl = 'camels'",
        "gloss_he": "גָּמָל",
        "saadia_note": "Saadia's regular gloss for Hebrew גָּמָל — the camels in Rebekah's betrothal narrative (Gen 24 passim — אלגמאל 'the camels'), Jacob and Laban (Gen 31), and the levitical animal-clean/unclean lists (Lev 11:4; Deut 14:7).",
        "source": "lane",
        "variants": [
            "אלגמל", "ואלגמל",
            "וגמל", "באלגמל",
            "גמלך", "גמלה", "גמלהא",
            "גמלין",
            "גמאל", "אלגמאל", "ואלגמאל",
            "באלגמאל", "ללגמאל",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "machir-name",
        "lemma_ja": "מכיר",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Machir — son of Manasseh, ancestor of the Machirite clan and of Gilead (Gen 50:23; Num 26:29; 27:1; 32:39-40; 36:1; Deut 3:15; Josh 13:31; 17:1)",
        "gloss_he": "מָכִיר בֶּן מְנַשֶּׁה",
        "saadia_note": "Saadia retains the Hebrew name unchanged. The gentilic 'Machirites' = אלמכיריין.",
        "source": "lane",
        "variants": [
            "ומכיר", "למכיר", "במכיר",
            "אבן מכיר", "מכיריין", "אלמכיריין",
        ],
    },
    {
        "id": "haran-place",
        "lemma_ja": "חרן",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Haran — (1) Abraham's brother, father of Lot, Milcah, Iscah (Gen 11:27-29); (2) Aramean city in upper Mesopotamia, Abraham's intermediate dwelling-place (Gen 11:31-12:5; 27:43; 28:10; 29:4)",
        "gloss_he": "חָרָן",
        "saadia_note": "Saadia retains the Hebrew name unchanged for both senses (person and place).",
        "source": "lane",
        "variants": [
            "וחרן", "לחרן", "בחרן",
            "אבן חרן", "פי חרן",
        ],
    },
]


VARIANTS_PATCH = {
    "ab-father":       ["אביהמא", "ואביהמא"],
    "sayyid-lord":     ["סיידנא", "וסיידנא", "סיידנו"],
    "qattala-kill":    ["פקתלה", "ופקתלה", "וקתלה",
                        "פקתלהא", "פקתלהם", "פיקתלה"],
    "nisa-women":      ["נסאא", "ונסאא", "נסאוא"],
    "hadhihi":         ["הוד'י", "ולהוד'י", "והוד'י", "פהוד'י"],
    "iʿta-give":       ["אעטיך", "ואעטיך", "פאעטיך",
                        "נעטיך", "תעטיך"],
}

STARTER_VARIANTS_PATCH = {
    "alima":           ["עלמת", "ועלמת", "פעלמת"],
}


def main():
    lane_path = pathlib.Path("data/dictionary-lane.json")
    starter_path = pathlib.Path("data/dictionary-starter.json")
    d = json.loads(lane_path.read_text())
    ds = json.loads(starter_path.read_text())

    existing_ids = {e["id"] for e in d["entries"]}
    existing_lemmas = {e["lemma_ja"] for e in d["entries"]}
    added = 0
    skipped = []
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

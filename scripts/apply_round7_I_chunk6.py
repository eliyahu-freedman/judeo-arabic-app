#!/usr/bin/env python3
"""Phase 2 Round 7 Batch I — chunk 6 (25 candidates).

Mix of new lemmas (proper nouns, narrative vocab, sacrificial/spatial nouns)
and patches on heavy-frequency verb stems already in the dict.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Adjectives / comparatives ----------
    {
        "id": "aslah-better",
        "lemma_ja": "אצלח",
        "lemma_ar": "أَصْلَح",
        "root": "ṣ-l-ḥ",
        "pos": "adjective (comparative / elative)",
        "gloss_en": "better, more beneficial, more advantageous, the best choice",
        "gloss_he": "הַטּוֹב יוֹתֵר, הַמּוּטָב",
        "saadia_note": "Saadia's regular gloss for Hebrew טוֹב לָנוּ ('better for us') in the wilderness-rebellion grumbling formulas (Num 11:18 וכאן אלאצלח לנא במצר 'and it was better for us in Egypt'; Num 14:3 אלאצלח לנא אלרגוע אלי' מצר 'better for us to return to Egypt').",
        "source": "lane",
        "variants": [
            "אלאצלח", "ואלאצלח",
            "ואצלח", "באלאצלח",
            "אצלחהם", "אצלחנא",
        ],
    },
    {
        "id": "hadid-keen",
        "lemma_ja": "חדיד",
        "lemma_ar": "حَدِيد",
        "root": "ḥ-d-d",
        "pos": "adjective (m.) / noun",
        "gloss_en": "(1) sharp, keen (of eyes, perception); (2) iron (as noun)",
        "gloss_he": "(1) חַד (רֹאֶה לְמֵרָחוֹק); (2) בַּרְזֶל",
        "notes": "The adjectival sense 'sharp / keen-of-sight' translates Heb שְׁתֻם הָעָיִן in Balaam's oracle; the nominal sense 'iron' appears in weapons contexts.",
        "saadia_note": "Saadia uses חדיד אלבצר 'keen-of-sight' for Hebrew שְׁתֻם הָעָיִן in Balaam's third and fourth oracles (Num 24:3, 24:15 — אלרגל אלחדיד אלבצר 'the man with the keen sight'). The 'iron' sense surfaces in homicide-by-iron-weapon passages (Num 35:16 בְאֶבֶן יָד 'with an iron implement').",
        "source": "lane",
        "variants": [
            "אלחדיד", "ואלחדיד",
            "וחדיד", "באלחדיד",
            "חדידא",
            "חדאד", "אלחדאד",
            "אנא חדיד",
        ],
    },

    # ---------- Verbs (mostly new — Forms I/VII) ----------
    {
        "id": "halaka-perish",
        "lemma_ja": "הלך",
        "lemma_ar": "هَلَك",
        "root": "h-l-k",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to perish, die (violently or by judgment); to be destroyed",
        "gloss_he": "אָבַד, סָפָה, נֶהֱרַס",
        "saadia_note": "Saadia's regular gloss for Hebrew הִכָּרֵת / אָבַד / סָפָה in judgment contexts — 'lest they perish' (Num 17:25, 18:3 — לא יהלכון; Deut 4:26).",
        "source": "lane",
        "variants": [
            "הלכת", "הלכו", "ההלך",
            "יהלך", "ויהלך", "פיהלך",
            "תהלך", "אהלך", "נהלך",
            "יהלכון", "ויהלכון", "תהלכון",
            "אהלאך", "אלאהלאך",
            "האלך", "אלהאלך", "ההאלכון",
        ],
    },
    {
        "id": "inqataʿa-cut-off",
        "lemma_ja": "אנקטע",
        "lemma_ar": "اِنْقَطَع",
        "root": "q-ṭ-ʿ",
        "pos": "verb (Form VII, perfect)",
        "gloss_en": "to be cut off, severed, terminated; (in karet contexts) to be excised from the community",
        "gloss_he": "נִכְרַת, נֶעֱקַר",
        "notes": "Form VII (passive-reflexive) of q-ṭ-ʿ. The Form-I qataʿa 'he cut' is transitive; Form VII inqataʿa is the result-state.",
        "saadia_note": "Saadia's regular gloss for Hebrew הִכָּרֵת (the karet penalty 'cut off') in covenant-violation contexts — Num 15:31 פינקטע ד'אלך אלאנסאן 'and that person shall be cut off'; Num 19:20.",
        "source": "lane",
        "variants": [
            "ינקטע", "פינקטע", "וינקטע",
            "תנקטע", "אנקטע", "ננקטע",
            "אנקטעת", "פאנקטעת",
            "ינקטעו", "פינקטעו",
            "אנקטאע", "אלאנקטאע",
            "מנקטע", "אלמנקטע",
        ],
    },
    {
        "id": "rafaʿa-lift",
        "lemma_ja": "רפע",
        "lemma_ar": "رَفَع",
        "root": "r-f-ʿ",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to lift, raise, elevate; to take up (an offering)",
        "gloss_he": "הֵרִים, נָשָׂא, הִגְבִּיהַּ",
        "notes": "Form-I cognate of the existing marfu-raised (passive participle). Form VIII irtafaʿa = 'to rise up'.",
        "saadia_note": "Saadia's regular gloss for Hebrew הֵרִים / נָשָׂא in physical-lifting and offering-elevation contexts — 'he lifted his hand' (Num 20:11 פרפע ידה), 'Moses brought their case before YHWH' (Num 27:5 פרפע מוסי' חכמהן), 'he shall take up an offering' (Num 18:24 ירפעוהא; Lev 7).",
        "source": "lane",
        "variants": [
            "ורפע", "פרפע",
            "רפעת", "רפעו", "רפעוא", "רפענא",
            "ירפע", "וירפע", "תרפע", "ארפע", "נרפע",
            "ירפעו", "וירפעו", "תרפעו", "ירפעוהא",
            "ירפעונהא", "ירפעוהם",
            "רפעא", "אלרפעא",
            "רפיע",   # already marfu-related
        ],
    },
    {
        "id": "irtafaʿa-rise",
        "lemma_ja": "ארתפע",
        "lemma_ar": "اِرْتَفَع",
        "root": "r-f-ʿ",
        "pos": "verb (Form VIII, perfect)",
        "gloss_en": "to rise up, ascend, be raised up, be lifted",
        "gloss_he": "עָלָה, הִתְרוֹמֵם, הִסְתַּלֵּק",
        "notes": "Form VIII (اِرْتَفَع) of r-f-ʿ. Used both literally ('the cloud lifted/ascended') and figuratively ('the divine glory was lifted').",
        "saadia_note": "Saadia's regular gloss for Hebrew נֶעֱלָה / הֵעָלָה — most prominently for the cloud lifting from over the Tabernacle and the people setting out (Num 9:21-22, Num 10:11 — ירתפע אלג'מאם 'the cloud lifts up'). Also: 'and YHWH's light was lifted from Abraham' (Gen 17:22, 18:33 — ארתפע נור אללה ען אברהים).",
        "source": "lane",
        "variants": [
            "ירתפע", "וירתפע", "פירתפע",
            "תרתפע", "ארתפע", "נרתפע",
            "ארתפעת", "פארתפעת", "וארתפעת",
            "ארתפע נור אללה",
            "מרתפע", "אלמרתפע",
        ],
    },
    {
        "id": "ghatta-cover",
        "lemma_ja": "ג'טא",
        "lemma_ar": "غَطَّى",
        "root": "gh-ṭ-w",
        "pos": "verb (Form II, perfect)",
        "gloss_en": "to cover, blanket, conceal (with a covering)",
        "gloss_he": "כִּסָּה, חִפָּה",
        "notes": "Form II (غَطَّى). The active ptcp mughaṭṭi 'covering' and passive ptcp mughaṭṭā 'covered' both appear.",
        "saadia_note": "Saadia's regular gloss for Hebrew כִּסָּה — most notably in Balak's complaint about Israel 'covering the face of the land' (Num 22:5, 22:11 — קד ג'טא צ'אהר אלארץ' 'has covered the face of the land'). Also the technical 'the caul that covers the entrails' (אלת'רב אלמג'טי אלגוף, Lev 3:3 etc.).",
        "source": "lane",
        "variants": [
            "ג'טי", "וג'טא", "פג'טא",
            "ג'טאהא", "ג'טאה", "ג'טאהם",
            "יג'טי", "ויג'טי", "תג'טי",
            "אג'טי", "נג'טי",
            "מג'טי", "אלמג'טי", "אלמג'טא",
            "מג'טיה", "אלמג'טיה",
            "ג'טא", "אלג'טא", "באלג'טא",
        ],
    },
    {
        "id": "halla-alight",
        "lemma_ja": "חל",
        "lemma_ar": "حَلَّ",
        "root": "ḥ-l-l",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to alight, descend, settle (upon); to come to rest in a place; (idiomatic) to befall, come upon",
        "gloss_he": "חָנָה, יָרַד עַל, פָּקַד",
        "notes": "Form I of ḥ-l-l. The Form-IV causative ahalla 'to cause to alight' is already in the dict.",
        "saadia_note": "Saadia's regular gloss for Hebrew הָיְתָה עָלָיו ('it came upon him') in prophetic-spirit contexts — Num 24:2: חלת עלי'ה נבווה' אללה 'the prophecy of God alighted upon him'; Deut 2:15: חלת בהם 'it [the hand of YHWH] came upon them'.",
        "source": "lane",
        "variants": [
            "חלת", "חלוא", "וחלת", "פחלת",
            "יחל", "ויחל", "תחל",
            "אחל", "נחל",
            "חאל", "אלחאל",
            "חלול", "אלחלול",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "darba-blow",
        "lemma_ja": "צ'רבה",
        "lemma_ar": "ضَرْبَة",
        "root": "ḍ-r-b",
        "pos": "noun (f., verbal-noun)",
        "gloss_en": "a (single) blow, strike, hit; (in Saadia) a plague-strike",
        "gloss_he": "מַכָּה",
        "saadia_note": "Saadia's regular gloss for Hebrew מַכָּה — both the literal blow (Num 35:16 צ'רבה באנא חדיד 'a blow with an iron implement') and the divine plague-strike (Num 11:33 פצ'רבהם צ'רבה עצ'ימה גדא 'he struck them with a very great blow').",
        "source": "lane",
        "variants": [
            "אלצ'רבה", "ואלצ'רבה",
            "וצ'רבה", "באלצ'רבה",
            "צ'רבאת", "אלצ'רבאת", "ואלצ'רבאת",
            "צ'רבתה", "צ'רבתהם",
        ],
    },
    {
        "id": "hulm-dream",
        "lemma_ja": "חלם",
        "lemma_ar": "حُلْم",
        "root": "ḥ-l-m",
        "pos": "noun (m.)",
        "gloss_en": "dream, nighttime vision",
        "gloss_he": "חֲלוֹם",
        "saadia_note": "Saadia's regular gloss for Hebrew חֲלוֹם in prophetic-revelation contexts ('I speak to him in a dream', Num 12:6 כ'אטבתה פי חלם; Gen 20:3 פי חלם אלליל 'in the dream of the night') and in narrative (Joseph and Pharaoh's dreams, Gen 37, 40-41).",
        "source": "lane",
        "variants": [
            "אלחלם", "ואלחלם",
            "וחלם", "באלחלם", "פי חלם",
            "חלמי", "חלמך", "חלמה", "חלמהם",
            "אחלאם", "אלאחלאם", "ואלאחלאם", "חלם אלליל",
            "חאלם", "אלחאלם",
        ],
    },
    {
        "id": "nasib-portion",
        "lemma_ja": "נציב",
        "lemma_ar": "نَصِيب",
        "root": "n-ṣ-b",
        "pos": "noun (m.)",
        "gloss_en": "portion, share, lot (of inheritance, of spoils, of one's allotment)",
        "gloss_he": "חֵלֶק, נַחֲלָה, גּוֹרָל",
        "saadia_note": "Saadia's regular gloss for Hebrew חֵלֶק in inheritance and apportionment contexts — 'you shall have no portion among them' (Num 18:20 ולא יכון לך נציב פי מא בינהם; Deut 10:9, 12:12, 14:27, 14:29, 18:1). Also for war-spoils apportionment (Num 31).",
        "source": "lane",
        "variants": [
            "אלנציב", "ואלנציב",
            "ונציב", "באלנציב",
            "נציבך", "נציבה", "נציבהא", "נציבהם", "נציבכם",
            "אנציבה", "אלאנציבה",
            "נצאיב",
        ],
    },
    {
        "id": "fariq-group",
        "lemma_ja": "פריק",
        "lemma_ar": "فَرِيق",
        "root": "f-r-q",
        "pos": "noun (m.)",
        "gloss_en": "group, troop, division, party; band of people",
        "gloss_he": "כַּת, חֲבוּרָה, פְלֻגָּה",
        "saadia_note": "Saadia's regular gloss for Hebrew אִישׁ עַל-דִּגְלוֹ / אִישׁ עַל-מַחֲנֵהוּ ('each by his standard') and similar group-designations in the encampment passages (Num 2:17 כל פריק פי מכאנה 'each group in its place'; Num 4:19 כל פריק עלי כ'דמתה 'each group to its task').",
        "source": "lane",
        "variants": [
            "אלפריק", "ואלפריק",
            "ופריק", "באלפריק",
            "פרק", "אלפרק", "ואלפרק",
            "אפרק", "אלאפרק",
            "פריקין", "אלפריקין",
        ],
    },
    {
        "id": "tilqaʾ-toward",
        "lemma_ja": "תלקא",
        "lemma_ar": "تِلْقَاء",
        "root": "l-q-y",
        "pos": "preposition / adverb",
        "gloss_en": "facing, toward, in front of, to meet (with motion-verbs of meeting/intercepting)",
        "gloss_he": "לִקְרַאת, מוּל, פָּנִים אֶל פָּנִים",
        "saadia_note": "Saadia's regular gloss for Hebrew לִקְרַאת ('toward, to meet') in meeting-narratives — 'Edom came out toward them' (Num 20:20 פכ'רג אדום תלקאהם; Num 21:23; 22:36; Gen 14:17; 24:17; 32:7).",
        "source": "lane",
        "variants": [
            "תלקאה", "תלקאהא", "תלקאהם", "תלקאהמא", "תלקאך", "תלקאכם", "תלקאי",
            "ותלקא", "ותלקאה", "ותלקאהם",
            "פתלקאה",
            "מן תלקא", "מן תלקאי",
        ],
    },
    {
        "id": "tibn-straw",
        "lemma_ja": "תבן",
        "lemma_ar": "تِبْن",
        "root": "t-b-n",
        "pos": "noun (m., collective)",
        "gloss_en": "straw, chopped straw (used as fodder)",
        "gloss_he": "תֶּבֶן",
        "saadia_note": "Saadia's regular gloss for Hebrew תֶּבֶן — fodder for camels (Gen 24:25, 32 — ואעטא תבנא וקתא לאלגמאל 'and he gave straw and provender to the camels') and the recurring 'straw is given' in the Exodus brick-making formula (Exod 5).",
        "source": "lane",
        "variants": [
            "אלתבן", "ואלתבן",
            "ותבן", "באלתבן",
            "תבנא", "ותבנא", "תבנכם",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "miriam-name",
        "lemma_ja": "מרים",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Miriam — sister of Moses and Aaron, prophetess and leader of the women's song at the Sea (Exod 15:20-21; Num 12; 20:1; 26:59)",
        "gloss_he": "מִרְיָם",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ומרים", "למרים", "במרים",
            "יא מרים",
        ],
    },
    {
        "id": "hebron-place",
        "lemma_ja": "חברא",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Hebron — the patriarchal city; site of Machpelah and Mamre (Gen 13:18; 23:2, 19; 35:27; 37:14; Num 13:22; Josh 14-15)",
        "gloss_he": "חֶבְרוֹן",
        "notes": "Saadia uses the form חברא (without the final ון suffix) — the Aramaic-style truncation rather than the Hebrew construct.",
        "saadia_note": "Saadia's standard form for Hebrew חֶבְרוֹן. The variant חברון also appears.",
        "source": "lane",
        "variants": [
            "וחברא", "לחברא", "בחברא",
            "חברון", "וחברון", "לחברון", "בחברון",
        ],
    },
]


VARIANTS_PATCH = {
    "kallam":           ["כלאמי", "כלאמך", "כלאמה", "כלאמהא", "כלאמכם", "כלאמהם", "כלאמנא"],
    "daraba-strike":    ["צ'רבה", "אלצ'רבה", "ואלצ'רבה", "צ'רבאת"],   # noun-form patch
    "jamaʿa-collect":   ["אגמעין", "ואגמעין", "אגמעון", "באגמעין"],
    "akala-eat":        ["תאכלה", "ותאכלה", "פתאכלה", "תאכלהא", "תאכלהם"],
    "jaʿala-place":     ["געלתהא", "געלתה", "געלתהם", "געלתכם", "געלתך"],
    "baraka-bless":     ["ברכאת", "אלברכאת", "ואלברכאת"],   # noun-form patch onto verb entry
    "qala":             ["יקולה", "ויקולה", "יקולהא", "יקולהם"],
    "taʾiq-able":       ["נטיק", "ננטיק", "ונטיק"],   # 1mp impf of ṭ-w-q
}

STARTER_VARIANTS_PATCH = {}


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
            variant_skipped.append((entry_id, "id not found in lane"))
            continue
        target = by_id[entry_id]
        existing_variants = target.setdefault("variants", [])
        for v in new_variants:
            if v in existing_variants:
                variant_skipped.append((entry_id, f"already had {v}"))
                continue
            existing_variants.append(v)
            variant_added += 1

    by_id_s = {e["id"]: e for e in ds["entries"]}
    starter_variant_added = 0
    for entry_id, new_variants in STARTER_VARIANTS_PATCH.items():
        if entry_id not in by_id_s:
            variant_skipped.append((entry_id, "id not found in starter"))
            continue
        target = by_id_s[entry_id]
        existing_variants = target.setdefault("variants", [])
        for v in new_variants:
            if v in existing_variants:
                variant_skipped.append((entry_id, f"already had {v}"))
                continue
            existing_variants.append(v)
            starter_variant_added += 1

    lane_path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    starter_path.write_text(json.dumps(ds, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())
    json.loads(starter_path.read_text())

    print(f"Added {added} new entries (lane). Skipped: {len(skipped)}")
    for s, reason in skipped:
        print(f"  - {s}: {reason}")
    print(f"Added {variant_added} lane variants + {starter_variant_added} starter variants. Skipped: {len(variant_skipped)}")
    for s, reason in variant_skipped:
        print(f"  - {s}: {reason}")
    print(f"Total lane entries: {len(d['entries'])}")


if __name__ == "__main__":
    main()

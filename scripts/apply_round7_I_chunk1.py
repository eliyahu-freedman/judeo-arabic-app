#!/usr/bin/env python3
"""Phase 2 Round 7 Batch I — chunk 1 (25 candidates).

Pulls the next 25 uncovered candidates after Batch H.

Two notable cases:
  • אמה (amah, maidservant) is a homograph with the existing umma-nation
    (lemma אמה = nation). Added as second sense; ahl-family handles family.
  • ת'מאן (thamān, fem-form 'eight' / '800') is a sibling of the Batch-H
    thamaniya-eight entry — patched in as a variant rather than a new entry.
  • יחל and ליחל are the same root (ḥ-l-l in Form IV) used as
    "to cause to dwell (the divine name in the place)". Single new entry.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Verbs ----------
    {
        "id": "baʿl-husband",
        "lemma_ja": "בעל",
        "lemma_ar": "بَعْل",
        "root": "b-ʿ-l",
        "pos": "noun (m.)",
        "gloss_en": "husband, master, lord; possessor (of a thing)",
        "gloss_he": "בעל, אדון, אישהּ",
        "saadia_note": "Saadia's regular gloss for Hebrew בַּעַל / אִישׁ in marriage contexts (e.g. the vows pericope, Num 30:7-15: בעלהא 'her husband').",
        "source": "lane",
        "variants": [
            "אלבעל", "ואלבעל", "באלבעל",
            "בעלהא", "בעלה", "בעלי", "בעלכם", "בעלך",
            "ובעלהא", "ובעלה",
            "בעולה", "אלבעולה",
        ],
    },
    {
        "id": "ahalla-cause-dwell",
        "lemma_ja": "אחל",
        "lemma_ar": "أَحَلَّ",
        "root": "ḥ-l-l",
        "pos": "verb (Form IV, perfect)",
        "gloss_en": "to cause to alight, settle, or dwell; to make (a thing) descend or repose (in a place)",
        "gloss_he": "השכין, הוריד, גרם לחנות",
        "notes": "Form IV (أَحَلَّ) of ḥ-l-l. The Form-I yaḥull means 'to alight, descend' intransitively; Form IV is transitive.",
        "saadia_note": "Saadia's regular gloss for the recurring Deuteronomic formula 'the place where YHWH will cause his name to dwell' (לְשַׁכֵּן שְׁמוֹ שָׁם) — rendered אן יחל נורה פיה / ליחל נורה פיה 'that he may cause his light to alight there' (Deut 12:5, 12:11, 14:23, 14:24, etc., with the characteristic anti-anthropomorphic substitution of nūr 'light' for šēm 'name').",
        "source": "lane",
        "variants": [
            "יחל", "ליחל",
            "אן יחל", "לאן יחל",
            "אחל", "ואחל",
            "תחל", "אחלל",
            "אחלוא", "פאחלוא",
            "מחלל",
        ],
    },
    {
        "id": "tahara-pure",
        "lemma_ja": "טהר",
        "lemma_ar": "طَهَر",
        "root": "ṭ-h-r",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to be / become ritually pure, clean (of persons, vessels, garments)",
        "gloss_he": "טהר, נטהר",
        "saadia_note": "Saadia's regular gloss for Hebrew טָהֵר / טָהוֹר in purity contexts (Lev 11-15; Num 19) — both verbal 'become pure' and adjectival 'pure'.",
        "source": "lane",
        "variants": [
            "יטהר", "ויטהר",
            "תטהר", "פתטהר",
            "אטהר", "נטהר",
            "טהרת", "טהרתה", "טהרנא",
            "טאהר", "אלטאהר", "ואלטאהר",
            "טאהרה", "טאהרין", "טאהראת",
            "טהרה", "אלטהרה", "ואלטהרה",
        ],
    },
    {
        "id": "tajalla-appear",
        "lemma_ja": "תגלא",
        "lemma_ar": "تَجَلَّى",
        "root": "j-l-w",
        "pos": "verb (Form V, perfect)",
        "gloss_en": "to appear, manifest oneself, become manifest; (of God) to reveal himself",
        "gloss_he": "נגלה, התגלה, הופיע",
        "saadia_note": "Saadia's regular gloss for theophanic Hebrew verbs נִרְאָה / וַיֵּרָא when God appears to a patriarch (Gen 17:1 תגלא לה אללה = וַיֵּרָא יהוה אֵלָיו; Gen 48:3). Part of Saadia's anti-anthropomorphic-but-still-personal vocabulary for divine self-disclosure.",
        "source": "lane",
        "variants": [
            "ותגלא", "פתגלא",
            "יתגלא", "ויתגלא",
            "אתגלא", "נתגלא",
            "תגלי", "תגליה",
            "תגלת", "תגלת לה",
            "מתגלי", "אלמתגלי",
        ],
    },
    {
        "id": "razaqa-provide",
        "lemma_ja": "רזק",
        "lemma_ar": "رَزَق",
        "root": "r-z-q",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to provide for, give sustenance to, supply with livelihood",
        "gloss_he": "סיפק מזון, פרנס, נתן רֶזֶק",
        "saadia_note": "Saadia's regular gloss for Hebrew nātan / bērēkh in the recurring Deuteronomic formula 'as YHWH your God has given/blessed you' (כַּאֲשֶׁר נָתַן / בֵּרַךְ → כמא רזקך אללה רבך, Deut 12:7, 12:21).",
        "source": "lane",
        "variants": [
            "רזקך", "רזקנא", "רזקכם", "רזקהם",
            "ורזק", "ורזקך", "ורזקנא",
            "יזרק",   # rare metathesis variant — usually yarzuq
            "ירזק", "וירזק", "תרזק",
            "אלרזק", "ואלרזק", "רזקא", "ארזאק",
        ],
    },
    {
        "id": "khara-go-well",
        "lemma_ja": "יכ'אר",
        "lemma_ar": "يُخَار",
        "root": "kh-y-r",
        "pos": "verb (Form IV passive imperfect, 3ms)",
        "gloss_en": "(impersonal) it will go well (with you); (idiomatic) may you / may things prosper",
        "gloss_he": "ייטב, יהיה לך לטובה",
        "notes": "Form IV passive of kh-y-r 'to be good'. Used impersonally with li- + addressee: yukhāru laka = 'may it go well for you'.",
        "saadia_note": "Saadia's regular gloss for the Deuteronomic formula לְמַעַן יִיטַב לְךָ — rendered לכי יכ'אר לך 'so that it may go well for you' (Deut 12:25, 12:28).",
        "source": "lane",
        "variants": [
            "ליכ'אר", "ויכ'אר",
            "לכי יכ'אר",
        ],
    },
    {
        "id": "dajaʿa-lie-with",
        "lemma_ja": "צ'אגע",
        "lemma_ar": "ضَاجَع",
        "root": "ḍ-j-ʿ",
        "pos": "verb (Form III, perfect)",
        "gloss_en": "to lie with (sexually), have sexual relations with",
        "gloss_he": "שכב עם",
        "saadia_note": "Saadia's regular euphemistic gloss for Hebrew שָׁכַב in sexual contexts (e.g. Gen 26:10 about Abimelech's near-violation of Rebekah; Gen 34:7 about Shechem and Dinah). Form III ḍājaʿa 'to lie with [s.o.]' is the relational sense; Form I ḍajaʿa is just 'to lie down'.",
        "source": "lane",
        "variants": [
            "וצ'אגע", "פצ'אגע",
            "יצ'אגע", "ויצ'אגע", "תצ'אגע",
            "צ'אגעת", "צ'אגעתה", "צ'אגעהא",
            "צ'אגעו", "וצ'אגעו",
            "מצ'אגעה",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "nusk-naziriteship",
        "lemma_ja": "נסך",
        "lemma_ar": "نُسْك",
        "root": "n-s-k",
        "pos": "noun (m., verbal-noun)",
        "gloss_en": "religious devotion, ascetic vow, consecration; (technical, in Saadia) Naziriteship",
        "gloss_he": "נְזִירוּת, התקדשות, התנזרות",
        "saadia_note": "Saadia's regular technical gloss for Hebrew נֵזֶר / נְזִיר / נְזִירוּת — the entire Nazirite pericope at Num 6 uses נסך as the technical term (e.g. אייאם נסכה 'the days of his Naziriteship', Num 6:4). The denominal verb nasaka = 'to be a Nazirite'.",
        "source": "lane",
        "variants": [
            "נסכה", "נסכהא", "נסכי", "נסככם", "נסכהם",
            "אלנסך", "ואלנסך", "באלנסך",
            "ונסך", "נסכא",
            "תנסכה", "תנסכהא", "ינסך", "וינסך",
            "אלנאסך", "ואלנאסך", "אלנאסכין",
            "מנסוך", "אלמנסוך",
        ],
    },
    {
        "id": "hamam-pigeons",
        "lemma_ja": "חמאם",
        "lemma_ar": "حَمَام",
        "root": "ḥ-m-m",
        "pos": "noun (collective, m.)",
        "gloss_en": "pigeons, doves (collective)",
        "gloss_he": "יונים",
        "saadia_note": "Saadia's regular gloss for Hebrew יוֹנָה in offering contexts (especially the formula 'two turtledoves or two young pigeons' תֹּרִים אוֹ בְנֵי יוֹנָה → שפנינין או פרכ'י חמאם, Num 6:10; Gen 15:9).",
        "source": "lane",
        "variants": [
            "אלחמאם", "ואלחמאם",
            "וחמאם", "באלחמאם",
            "פרכ' חמאם", "פרכ'י חמאם",
            "חמאמה", "אלחמאמה",
        ],
    },
    {
        "id": "manara-lampstand",
        "lemma_ja": "מנארה",
        "lemma_ar": "مَنَارَة",
        "root": "n-w-r",
        "pos": "noun (f.)",
        "gloss_en": "lampstand, candelabrum; (in Saadia) the menorah",
        "gloss_he": "מנורה",
        "saadia_note": "Saadia's regular gloss for Hebrew מְנוֹרָה — both the seven-branched Tabernacle menorah (Num 8:2-4) and any lampstand.",
        "source": "lane",
        "variants": [
            "אלמנארה", "ואלמנארה",
            "באלמנארה", "ומנארה",
            "מנאראת", "אלמנאראת",
        ],
    },
    {
        "id": "unas-people",
        "lemma_ja": "אנאס",
        "lemma_ar": "أُنَاس",
        "root": "ʔ-n-s",
        "pos": "noun (collective, m.)",
        "gloss_en": "people, persons, (some) men, folk",
        "gloss_he": "אנשים, בני אדם",
        "notes": "Often used in the partitive sense 'some people' (kāna fīhim unās = 'there were among them some people who...'). Distinct from al-nās (the people in general, the populace).",
        "saadia_note": "Saadia uses unās for the unspecified-plural 'some people / certain men' — e.g. Num 9:6 פכאן פיהם אנאס תנגסו 'there were among them some men who had become defiled'; Gen 47:2 כ'מסה' אנאס מן אכ'ותה 'five of his brothers' (lit. 'five men from his brothers').",
        "source": "lane",
        "variants": [
            "ואנאס", "באנאס", "לאנאס",
            "אלאנאס", "ואלאנאס",
        ],
    },
    {
        "id": "wizr-burden",
        "lemma_ja": "וזר",
        "lemma_ar": "وِزْر",
        "root": "w-z-r",
        "pos": "noun (m.)",
        "gloss_en": "burden, load; (figurative) sin, guilt, transgression carried as a burden",
        "gloss_he": "משא, אשמה, עוון",
        "saadia_note": "Saadia's regular gloss for Hebrew עֲוֹן in the formula 'and he shall bear his sin' (וְנָשָׂא חֶטְאוֹ / עֲוֹנוֹ → פקד חמל וזרה 'and he has borne his burden/sin' — Num 9:13; Lev 17:16).",
        "source": "lane",
        "variants": [
            "וזרה", "וזרהא", "וזרי", "וזרכם", "וזרהם",
            "אלוזר", "ואלוזר",
            "אוזאר", "אלאוזאר",
        ],
    },
    {
        "id": "tufan-flood",
        "lemma_ja": "טופאן",
        "lemma_ar": "طُوفَان",
        "root": "ṭ-w-f",
        "pos": "noun (m.)",
        "gloss_en": "flood, deluge",
        "gloss_he": "מַבּוּל",
        "saadia_note": "Saadia's regular gloss for Hebrew מַבּוּל — the Noahide Flood (Gen 6-11, e.g. Gen 10:1 בנין בעד אלטופאן 'sons after the Flood').",
        "source": "lane",
        "variants": [
            "אלטופאן", "ואלטופאן",
            "באלטופאן", "וטופאן",
            "לאלטופאן",
        ],
    },
    {
        "id": "jinan-garden",
        "lemma_ja": "גנאן",
        "lemma_ar": "جِنَان",
        "root": "j-n-n",
        "pos": "noun (m., here used as sg. 'the Garden')",
        "gloss_en": "garden, orchard, paradise; (in Saadia) the Garden of Eden",
        "gloss_he": "גן, גן עדן",
        "saadia_note": "Saadia's regular gloss for Hebrew גַּן in Gen 2-3 (the Garden of Eden). Lexically jinān is the plural of janna but is used here in the singular collective sense common in Judeo-Arabic.",
        "source": "lane",
        "variants": [
            "אלגנאן", "ואלגנאן",
            "באלגנאן", "ללגנאן",
            "גנאנא", "מן אלגנאן",
        ],
    },
    {
        "id": "amah-maidservant",
        "lemma_ja": "אמה",
        "lemma_ar": "أَمَة",
        "root": "ʔ-m-w",
        "pos": "noun (f.)",
        "gloss_en": "maidservant, female slave, handmaid",
        "gloss_he": "אָמָה, שפחה",
        "notes": "Homograph with umma (lemma אמה also) 'nation, community' — root ʔ-m-m, distinct. Context disambiguates: amah always appears in household / personal-possession contexts; umma in nation / people contexts.",
        "saadia_note": "Saadia's regular gloss for Hebrew אָמָה (handmaid, female slave) — Sarah's amah Hagar; Rachel's amah Bilhah; the household amah of the Decalogue and tithe-laws (Deut 12:18: ועבדך ואמתך 'your manservant and your maidservant').",
        "source": "lane",
        "variants": [
            "אמתך", "ואמתך", "אמתי", "אמתה", "אמתהא", "אמתכם", "אמתהם",
            "אלאמה", "ואלאמה",
            "באלאמה", "אמתא",
            "אמא", "אלאמא",   # broken plural: imāʾ
        ],
    },
    {
        "id": "jariya-young-woman",
        "lemma_ja": "גאריה",
        "lemma_ar": "جَارِيَة",
        "root": "j-r-y",
        "pos": "noun (f.)",
        "gloss_en": "young woman, maidservant, slave-girl; (broadly) any girl in service",
        "gloss_he": "נערה, אָמָה, שפחה",
        "saadia_note": "Saadia's regular gloss for Hebrew נַעֲרָה (young woman) in narrative — notably for Rebekah's attendant and Rebekah herself before betrothal (Gen 24:28, 24:55), and parallel passages.",
        "source": "lane",
        "variants": [
            "אלגאריה", "ואלגאריה",
            "באלגאריה", "ללגאריה",
            "ג'אריה", "אלג'אריה",   # alt-orthography with apos
            "גואר", "אלגואר",
            "גאריאת", "אלגאריאת",
        ],
    },
    {
        "id": "armala-widow",
        "lemma_ja": "ארמלה",
        "lemma_ar": "أَرْمَلَة",
        "root": "ʔ-r-m-l",
        "pos": "noun (f.)",
        "gloss_en": "widow",
        "gloss_he": "אַלְמָנָה",
        "saadia_note": "Saadia's regular gloss for Hebrew אַלְמָנָה — usually appearing in the triad 'the stranger, the orphan, and the widow' (אלג'ריב ואליתים ואלארמלה, e.g. Deut 10:18, 14:29).",
        "source": "lane",
        "variants": [
            "אלארמלה", "ואלארמלה",
            "וארמלה", "באלארמלה", "ללארמלה",
            "ארמלאת", "אלארמלאת", "ואלארמלאת",
        ],
    },
    {
        "id": "ubudiyya-bondage",
        "lemma_ja": "עבודיה",
        "lemma_ar": "عُبُودِيَّة",
        "root": "ʿ-b-d",
        "pos": "noun (f., abstract)",
        "gloss_en": "slavery, bondage, servitude",
        "gloss_he": "עַבְדוּת, שיעבוד",
        "saadia_note": "Saadia's regular gloss for Hebrew עֲבָדִים in the Exodus-redemption formula 'the house of bondage' (בֵּית עֲבָדִים → בית אלעבודייה, Deut 13:6, 13:11, and parallel passages in Exod and Deut).",
        "source": "lane",
        "variants": [
            "אלעבודיה", "אלעבודייה",
            "ואלעבודיה", "ואלעבודייה",
            "באלעבודיה", "באלעבודייה",
            "ללעבודייה",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "perizzite-people",
        "lemma_ja": "פרזיין",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun (gentilic plural)",
        "gloss_en": "Perizzites — one of the seven Canaanite peoples of pre-Israelite Canaan",
        "gloss_he": "הַפְּרִזִּי, הַפְּרִזִּים",
        "notes": "Always plural-gentilic in Saadia (the -iyyīn ending). Frequently paired with אלכנעאניין (Canaanites) — 'and the Canaanites and the Perizzites were then dwelling in the land' (Gen 13:7; 34:30; Deut 7:1).",
        "saadia_note": "Saadia retains the Hebrew name; the Arabic-style -iyy- + -īn gentilic plural ending is Saadia's standard for pre-Israelite Canaanite peoples (כנעאניין, פרזיין, אמוריין, חתיין, חויין, יבוסיין, גרגאשיין).",
        "source": "lane",
        "variants": [
            "ואלפרזיין", "אלפרזיין",
            "פרזי", "ופרזי", "אלפרזי",
        ],
    },
    {
        "id": "mamre-place",
        "lemma_ja": "ממרא",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Mamre — (1) an Amorite ally of Abraham; (2) the oak / grove / plain of Mamre, the patriarchal cult site near Hebron",
        "gloss_he": "מַמְרֵא — בעל ברית אברהם והמקום הקרוי על שמו",
        "saadia_note": "Saadia retains the Hebrew name unchanged. The locale appears in the formula 'the plain/oak of Mamre' (אֵלוֹנֵי מַמְרֵא → מרג ממרא, e.g. Gen 13:18; 14:13; 18:1; 23:17, 19; 35:27).",
        "source": "lane",
        "variants": [
            "וממרא", "לממרא", "במרא",
            "מרג ממרא",
        ],
    },
    {
        "id": "heth-name",
        "lemma_ja": "חת",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Heth — son of Canaan, eponymous ancestor of the Hittites (Gen 10:15); 'sons of Heth' = Hittites (Gen 23 passim)",
        "gloss_he": "חֵת בֶּן כְּנַעַן",
        "notes": "Saadia retains the Hebrew form. The gentilic form is אלחתיין (the Hittites).",
        "source": "lane",
        "variants": [
            "וחת", "לחת", "בחת",
            "בני חת", "לבני חת",
        ],
    },
    {
        "id": "bilhah-name",
        "lemma_ja": "בלהה",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Bilhah — Rachel's handmaid (gifted by Laban); mother of Dan and Naphtali",
        "gloss_he": "בִּלְהָה, שפחת רחל; אֵם דן ונפתלי",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ובלהה", "לבלהה", "בבלהה",
        ],
    },
    {
        "id": "ibri-hebrew",
        "lemma_ja": "עבראני",
        "lemma_ar": "عِبْرَانِيّ",
        "root": "—",
        "pos": "adjective / noun (gentilic)",
        "gloss_en": "Hebrew (sg.) — of or pertaining to the Hebrew people; an Israelite",
        "gloss_he": "עִבְרִי",
        "notes": "Plural אלעבראניין 'the Hebrews'. Both forms are Saadia's standard renderings of Hebrew עִבְרִי / עִבְרִים — usually in non-Israelite mouths (Egyptians, Philistines) referring to the patriarchal-Israelite community externally (Gen 14:13 אברם אלעבראני; Gen 39:14, 17; 40:15; 43:32).",
        "source": "lane",
        "variants": [
            "אלעבראני", "ואלעבראני",
            "עבראניין", "אלעבראניין", "ואלעבראניין",
            "באלעבראניין", "ללעבראניין",
            "בלד אלעבראניין",
        ],
    },
]


VARIANTS_PATCH = {
    # ת'מאן 'eight' (fem-counted) and the 800-pattern (e.g. ת'מאן מאיה
    # 'eight hundred', Gen 5:4, 5:7) is a sibling of Batch-H's thamaniya-eight.
    "thamaniya-eight": ["ת'מאן", "ות'מאן", "ת'מאני", "ות'מאני"],
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

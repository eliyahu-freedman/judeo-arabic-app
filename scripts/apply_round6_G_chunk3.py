#!/usr/bin/env python3
"""Phase 2 Round 6 Batch G chunk 3 — long-tail sweep (no API).

18 new lemma entries + 5 variant patches. Skipped: רת (count 14, no contexts).
Skipped: אלחרב bare form (auto-covered by ḥarb-war lemma).

New ibna-daughter entry intentionally homographs the existing ibn entry on
surface אבנה — the lookup chain will surface BOTH senses on tap, which is
the desired behavior (אבנה reads as either ibnahu 'his son' or ibna
'daughter' depending on context).
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Nouns ----------
    {
        "id": "harb-war",
        "lemma_ja": "חרב",
        "lemma_ar": "حَرْب",
        "root": "ḥ-r-b",
        "pos": "noun (f.)",
        "gloss_en": "war, battle, armed conflict, military campaign",
        "gloss_he": "מלחמה, קרב",
        "saadia_note": "Saadia uses ḥarb as the regular gloss for Hebrew מִלְחָמָה.",
        "source": "lane",
        "variants": [
            "אלחרב", "ואלחרב", "באלחרב", "לאלחרב",
            "חרבא", "חרוב", "אלחרוב", "ואלחרוב",
        ],
    },
    {
        "id": "maksab-gain",
        "lemma_ja": "מכסב",
        "lemma_ar": "مَكْسَب",
        "root": "k-s-b",
        "pos": "noun (m.)",
        "gloss_en": "gain, profit, acquisition, livelihood-earning",
        "gloss_he": "רווח, השגה, מלאכת קנין",
        "saadia_note": "In the festival prohibition 'kull ṣanʿat maksab lā taʿmalū', Saadia renders Hebrew כָּל מְלֶאכֶת עֲבֹדָה לֹא תַעֲשׂוּ ('no work-of-acquisition shall you perform') — distinguishing servile work from food-preparation labor allowed on Yom Tov.",
        "source": "lane",
        "variants": ["אלמכסב", "ואלמכסב", "באלמכסב", "מכאסב", "אלמכאסב"],
    },
    {
        "id": "fasH-passover",
        "lemma_ja": "פסח",
        "lemma_ar": "—",
        "root": "—",
        "pos": "noun (m.)",
        "gloss_en": "Passover — the festival commemorating the Exodus from Egypt",
        "gloss_he": "פסח",
        "saadia_note": "Saadia retains the Hebrew form פסח for the festival. The Arabic cognate fish (الفِصْح) is used for the Christian Easter; Saadia avoids it.",
        "source": "lane",
        "variants": ["אלפסח", "ואלפסח", "באלפסח", "פסחי", "פסחנא", "פסחכם", "פסחהם", "פסחא"],
    },
    {
        "id": "samgh-frankincense",
        "lemma_ja": "צמג",
        "lemma_ar": "صَمْغ",
        "root": "ṣ-m-gh",
        "pos": "noun (m.)",
        "gloss_en": "gum, resin (especially aromatic resin used as incense)",
        "gloss_he": "שרף, צרי, גומי-עצים (לקטורת)",
        "saadia_note": "Saadia uses al-ṣamgh as the regular gloss for Hebrew לְבֹנָה (frankincense — the aromatic resin in the Tabernacle incense, Exod 30:34; Num 4:16).",
        "source": "lane",
        "variants": ["צמג'", "אלצמג", "אלצמג'", "ואלצמג", "ואלצמג'", "באלצמג", "באלצמג'", "אלצמוג", "אלצמוג'"],
    },
    {
        "id": "mash-anointing",
        "lemma_ja": "מסח",
        "lemma_ar": "مَسْح",
        "root": "m-s-ḥ",
        "pos": "noun (m., verbal-noun)",
        "gloss_en": "an anointing, an act of smearing with oil; (in construct) oil-of-anointing",
        "gloss_he": "משיחה (בשמן)",
        "saadia_note": "Saadia uses dahn al-masḥ as the regular gloss for Hebrew שֶׁמֶן הַמִּשְׁחָה (the anointing oil, Exod 25:6 and parallels).",
        "source": "lane",
        "variants": ["אלמסח", "ואלמסח", "באלמסח", "לאלמסח", "מסחא", "מסחה", "מסחהם"],
    },
    {
        "id": "shaʿr-hair",
        "lemma_ja": "שער",
        "lemma_ar": "شَعْر",
        "root": "sh-ʿ-r",
        "pos": "noun (m., collective)",
        "gloss_en": "hair (collective: the hair of a head, body, or animal)",
        "gloss_he": "שׂער (של ראש, גוף או חיה)",
        "saadia_note": "Saadia uses shaʿr as the regular gloss for Hebrew שֵׂעָר (especially in Nazirite passages, Num 6).",
        "source": "lane",
        "variants": ["אלשער", "ואלשער", "באלשער", "שערה", "שערהא", "שערהם", "שערך", "שעיר", "אלשעיר", "ואלשעיר"],
    },
    {
        "id": "darj-spoon",
        "lemma_ja": "דרג",
        "lemma_ar": "دَرْج",
        "root": "d-r-j",
        "pos": "noun (m.)",
        "gloss_en": "a small container or ladle (Saadia: an incense-spoon)",
        "gloss_he": "כף (מתכת, לקטורת)",
        "saadia_note": "Saadia uses darj as the regular gloss for Hebrew כַּף (the gold incense-spoon of each tribal offering, Num 7:14ff).",
        "source": "lane",
        "variants": ["ודרגא", "אלדרג", "ואלדרג", "באלדרג", "דרגא", "דרגין", "דרוג", "אלדרוג", "ואלדרוג"],
    },
    {
        "id": "baqara-cow",
        "lemma_ja": "בקרה",
        "lemma_ar": "بَقَرَة",
        "root": "b-q-r",
        "pos": "noun (f.)",
        "gloss_en": "cow, head of cattle (singular); (collective) cattle",
        "gloss_he": "פרה; (כשם קיבוצי) בקר",
        "saadia_note": "Saadia uses baqara as the regular gloss for Hebrew פָּרָה. The collective al-baqar renders הַבָּקָר ('the cattle').",
        "source": "lane",
        "variants": [
            "אלבקרה", "ואלבקרה", "באלבקרה", "בקרתין",
            "בקראת", "אלבקראת",
            "אלבקר", "ואלבקר", "באלבקר",
        ],
    },
    {
        "id": "taHawwuz-possession",
        "lemma_ja": "תחוזה",
        "lemma_ar": "تَحَوُّز",
        "root": "ḥ-w-z",
        "pos": "noun (m., verbal-noun)",
        "gloss_en": "a taking possession, a holding, a possessed inheritance",
        "gloss_he": "אחוזה, חזקה, נחלה",
        "saadia_note": "Saadia uses li-taḥawwuz as the regular gloss for Hebrew לִירֻשָּׁה / לְמוֹרָשָׁה ('as a possession' — the patriarchal promise of the land, Gen 15:7; Deut 11:10).",
        "source": "lane",
        "variants": ["לתחוזה", "אלתחוזה", "ואלתחוזה", "באלתחוזה", "תחוזתה", "תחוזתכם", "תחוזתהם", "תחוזתי"],
    },
    {
        "id": "ibna-daughter",
        "lemma_ja": "אבנה",
        "lemma_ar": "اِبْنَة",
        "root": "b-n-y",
        "pos": "noun (f.)",
        "gloss_en": "daughter",
        "gloss_he": "בת",
        "notes": "Homograph with ibnahu 'his son' (m. + suffix). Context disambiguates. The explicit feminine form ibnatuhu (אבנתה) is unambiguous.",
        "source": "lane",
        "variants": [
            "אבנתה", "אבנתהא", "אבנתי", "אבנתך", "אבנתכם", "אבנתהם",
            "אבנת'", "ואבנה", "באבנה", "אבנאת", "אלאבנאת", "ואלאבנאת",
            "בנאת", "אלבנאת", "ואלבנאת",
        ],
    },
    {
        "id": "horeb-name",
        "lemma_ja": "חריב",
        "lemma_ar": "حُورِيب",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Horeb — the mountain of Sinai (the alternative name in Deuteronomy)",
        "gloss_he": "חורב",
        "source": "lane",
        "variants": ["וחריב", "לחריב", "בחריב", "חוריב", "וחוריב"],
    },
    {
        "id": "takhtaja-plank",
        "lemma_ja": "תכ'תגה",
        "lemma_ar": "تَخْتَجَة",
        "root": "—",
        "pos": "noun (f.)",
        "gloss_en": "a plank, a wooden board (Saadia: a Tabernacle plank)",
        "gloss_he": "קרש (של המשכן)",
        "saadia_note": "Saadia uses takhtaja as the regular gloss for Hebrew קֶרֶשׁ (the upright planks of the Tabernacle, Exod 26:15ff). The form is a Persian loanword (takhtah 'plank') Arabicized with a feminine ending.",
        "source": "lane",
        "variants": ["אלתכ'תגה", "ואלתכ'תגה", "תכ'אתג", "אלתכ'אתג", "ואלתכ'אתג", "תכ'תגתין", "באלתכ'תגה"],
    },
    {
        "id": "Hawalay-around",
        "lemma_ja": "חואלי",
        "lemma_ar": "حَوَالَيْ",
        "root": "ḥ-w-l",
        "pos": "preposition",
        "gloss_en": "around, surrounding, on all sides of",
        "gloss_he": "סביב, מסביב ל-, מכל עברי",
        "saadia_note": "Saadia uses ḥawālay as the regular gloss for Hebrew סָבִיב (around).",
        "source": "lane",
        "variants": ["וחואלי", "פחואלי", "חואלין", "חואלינא", "חואליכם", "חואליהם"],
    },
    {
        "id": "law-if-contrary",
        "lemma_ja": "לו",
        "lemma_ar": "لَو",
        "root": "—",
        "pos": "particle (conditional)",
        "gloss_en": "if (contrary-to-fact); if only; were it that",
        "gloss_he": "לו, אילו, אם (תנאי בלתי-אפשרי)",
        "notes": "Distinct from in (إِنْ), which marks open conditional ('if X happens'). law marks counterfactual or hypothetical ('if only X had happened').",
        "source": "lane",
        "variants": ["ולו", "פלו"],
    },
    {
        "id": "yabusi-jebusite",
        "lemma_ja": "יבוסי",
        "lemma_ar": "يَبُوسِي",
        "root": "—",
        "pos": "gentilic (m.)",
        "gloss_en": "Jebusite — descendant of Jebus (= Jerusalem); the pre-Israelite inhabitants of the city",
        "gloss_he": "יבוסי",
        "source": "lane",
        "variants": [
            "אליבוסי", "ואליבוסי", "באליבוסי",
            "יבוסיין", "אליבוסיין", "ואליבוסיין", "באליבוסיין",
        ],
    },
    {
        "id": "nadhr-vow",
        "lemma_ja": "נד'ר",
        "lemma_ar": "نَذْر",
        "root": "n-dh-r",
        "pos": "noun (m.)",
        "gloss_en": "a vow, a votive pledge, a thing dedicated by oath",
        "gloss_he": "נדר",
        "saadia_note": "Saadia uses naḏr as the regular gloss for Hebrew נֶדֶר. The verb tasawwagha naḏran ('to fulfill a vow') glosses לְפַלֵּא נֶדֶר.",
        "source": "lane",
        "variants": [
            "נד'רא", "אלנד'ר", "ואלנד'ר", "באלנד'ר",
            "נד'רה", "נד'רך", "נד'רכם", "נד'רהם",
            "נד'ור", "אלנד'ור", "ואלנד'ור", "נד'ורה", "נד'ורהם",
        ],
    },

    # ---------- Verbs ----------
    {
        "id": "qama-rise",
        "lemma_ja": "קאם",
        "lemma_ar": "قَامَ",
        "root": "q-w-m",
        "pos": "verb",
        "gloss_en": "to rise, to stand up, to arise; (imperative) arise! get up!",
        "gloss_he": "קם, התקומם, עמד; (ציווי) קום!",
        "source": "lane",
        "variants": [
            "קם", "וקם", "פקם",
            "קומו", "קומוא", "קומי", "פקומו", "וקומו",
            "יקום", "תקום", "אקום", "נקום",
            "יקומון", "יקומוא", "פיקומון",
            "קמת", "קאמת", "קמנא", "קאמא", "קאימא", "אלקאים",
        ],
    },
    {
        "id": "yali-face",
        "lemma_ja": "ולי",
        "lemma_ar": "وَلِيَ",
        "root": "w-l-y",
        "pos": "verb",
        "gloss_en": "to be next to, to face, to follow; (in construction 'mā yalī') what is next to / what faces",
        "gloss_he": "עמד מול, פנה אל, היה סמוך ל-; (במבנה 'מא ילי') מול, לעומת",
        "notes": "Surface ילי (yalī, 3ms impf) appears most often in the construction 'mā yalī' = 'what faces, what is opposite' — Saadia's gloss for Hebrew אֶל מוּל ('toward, opposite').",
        "source": "lane",
        "variants": ["ילי", "וילי", "פילי", "תלי", "ילון", "מאלי", "מולי", "מואלין"],
    },
]


VARIANTS_PATCH = {
    "dakhala-enter":  ["ידכל", "ידכלו", "ידכלון", "תדכלון"],
    "akhadha-take":   ["וכד", "פכד", "כד"],
    "raʾa-see":       ["פראי"],
    "hadiyya-gift":   ["לאלהדייה"],
    "ghasala-wash":   ["פליג'סל", "ליג'סל", "וליג'סל"],
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

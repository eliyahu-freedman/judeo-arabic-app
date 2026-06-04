#!/usr/bin/env python3
"""Phase 2 Round 6 Batch G chunk 4 — long-tail sweep (no API).

20 new lane entries + 3 lane variant patches + 2 starter variant patches.
First chunk in Round 6 to touch dictionary-starter.json — the starter holds
the Bereshit-1 exemplars and is Priority 1 in the lookup chain, so high-
frequency surface forms covered by a bare-lemma starter entry should be
added there to short-circuit lookups.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Nouns ----------
    {
        "id": "shah-sheep",
        "lemma_ja": "שאה",
        "lemma_ar": "شَاة",
        "root": "sh-w-h",
        "pos": "noun (f.)",
        "gloss_en": "a sheep, a head of small livestock (sheep or goat)",
        "gloss_he": "שה, ראש צאן (כבש או עז)",
        "saadia_note": "Saadia uses shāh as the regular gloss for Hebrew שֶׂה (a single head of small livestock).",
        "source": "lane",
        "variants": ["אלשאה", "ואלשאה", "באלשאה", "שאהא", "שאהי", "שיאה", "אלשיאה"],
    },
    {
        "id": "ʿasa-rod",
        "lemma_ja": "עצא",
        "lemma_ar": "عَصَا",
        "root": "ʿ-ṣ-w",
        "pos": "noun (f.)",
        "gloss_en": "rod, staff, scepter, walking-stick",
        "gloss_he": "מטה, מקל, שבט",
        "saadia_note": "Saadia uses ʿaṣā as the regular gloss for Hebrew מַטֶּה (the tribal rods, Num 17; Moses' staff).",
        "source": "lane",
        "variants": [
            "אלעצא", "ואלעצא", "באלעצא",
            "עצאה", "עצאהא", "עצאך", "עצאהם",
            "עציי", "אלעציי", "ואלעציי",
        ],
    },
    {
        "id": "baydat-plains",
        "lemma_ja": "בידאת",
        "lemma_ar": "بَيْدَات",
        "root": "b-y-d",
        "pos": "noun (f., plural)",
        "gloss_en": "plains, level wildernesses (plural of bayḍāʾ 'desert plain')",
        "gloss_he": "ערבות, מישורי מדבר",
        "saadia_note": "Saadia uses bīdāt as the regular gloss for Hebrew עַרְבוֹת (the plains of Moab, the Aravah, Num 22:1; 33:48ff).",
        "source": "lane",
        "variants": ["בידאת מואב", "ובידאת", "פי בידאת", "בידא", "אלבידא", "ואלבידא"],
    },
    {
        "id": "mil-full",
        "lemma_ja": "מל",
        "lemma_ar": "مِلْء",
        "root": "m-l-'",
        "pos": "noun (m.)",
        "gloss_en": "fullness, the full content of (a container)",
        "gloss_he": "מלא (מידת תכולת כלי)",
        "notes": "In the construction 'milʾ bayti-hi (faḍḍatan wa-dhahaban)' = '(equivalent to) his house full (of silver and gold)' — Saadia's gloss for Hebrew מְלֹא בֵיתוֹ (Num 22:18; 24:13).",
        "source": "lane",
        "variants": ["מלא", "מלי", "מלאהא", "מלאה", "מלאהם", "ומל", "פמל"],
    },
    {
        "id": "hawz-possession",
        "lemma_ja": "חוז",
        "lemma_ar": "حَوْز",
        "root": "ḥ-w-z",
        "pos": "noun (m., verbal-noun)",
        "gloss_en": "possession, the act of taking possession or holding",
        "gloss_he": "אחיזה, נחלה, ירושה",
        "notes": "Bare Form-I verbal noun. The Form-V verbal noun taḥawwuz (see taHawwuz-possession) carries the same sense.",
        "saadia_note": "Saadia uses ḥawz as the regular gloss for Hebrew יְרֻשָּׁה / מוֹרָשָׁה ('inheritance, possession of land', Num 27:7; 32:32).",
        "source": "lane",
        "variants": ["אלחוז", "ואלחוז", "באלחוז", "חוזה", "חוזכם", "חוזהם", "חוזנא"],
    },
    {
        "id": "shahid-witness",
        "lemma_ja": "שאהד",
        "lemma_ar": "شَاهِد",
        "root": "sh-h-d",
        "pos": "noun / active participle (m.)",
        "gloss_en": "witness, one who testifies; one who is present",
        "gloss_he": "עד, מי שמעיד",
        "saadia_note": "Saadia uses shāhid as the regular gloss for Hebrew עֵד (witness) in legal contexts (Num 35:30; Deut 19:15).",
        "source": "lane",
        "variants": [
            "אלשאהד", "ואלשאהד", "באלשאהד",
            "שאהדין", "אלשאהדין", "ושאהדין", "ושאהד",
            "שהוד", "אלשהוד", "ואלשהוד",
        ],
    },
    {
        "id": "sinaʿa-craft",
        "lemma_ja": "צנאעה",
        "lemma_ar": "صِنَاعَة",
        "root": "ṣ-n-ʿ",
        "pos": "noun (f.)",
        "gloss_en": "craft, work, labor, manufacture; an act of making",
        "gloss_he": "מלאכה, עבודה, צניעת מעשה",
        "saadia_note": "Saadia uses ṣināʿa as the regular gloss for Hebrew מְלָאכָה (work, especially the Tabernacle's prohibited Sabbath labor and the priestly service-labor of Num 4:3).",
        "source": "lane",
        "variants": [
            "אלצנאעה", "ואלצנאעה", "באלצנאעה",
            "צנאעתה", "צנאעתהם", "צנאעתכם", "צנאעתי",
        ],
    },
    {
        "id": "sanaʾiʿ-works",
        "lemma_ja": "צנאיע",
        "lemma_ar": "صَنَائِع",
        "root": "ṣ-n-ʿ",
        "pos": "noun (f., broken plural)",
        "gloss_en": "works, labors, crafts (plural of ṣanīʿa)",
        "gloss_he": "מלאכות, עבודות, צניעות",
        "saadia_note": "Saadia uses al-ṣanāʾiʿ as the regular gloss for Hebrew הַמְּלָאכוֹת in plural festival/Sabbath-prohibition contexts ('any of the labors' — Exod 12:16; Deut 5:14).",
        "source": "lane",
        "variants": ["אלצנאיע", "ואלצנאיע", "באלצנאיע"],
    },
    {
        "id": "darush-tahash",
        "lemma_ja": "דארש",
        "lemma_ar": "—",
        "root": "—",
        "pos": "noun (m.)",
        "gloss_en": "dārush — Saadia's term for Hebrew תַּחַשׁ, the dyed-skin covering of the Tabernacle",
        "gloss_he": "תחש (עור הצובה את המשכן)",
        "saadia_note": "Saadia uses dārush as the regular gloss for Hebrew תַּחַשׁ (the mysterious outer-covering skins of the Tabernacle, Exod 25:5; Num 4:6). The classical Arabic identification is uncertain; medieval commentators connect it to Persian darshī ('a kind of dyed leather') or Aramaic תַּחְשָׁא.",
        "source": "lane",
        "variants": ["ודארש", "אלדארש", "ואלדארש", "באלדארש"],
    },
    {
        "id": "tahrik-wave-offering",
        "lemma_ja": "תחריך",
        "lemma_ar": "تَحْرِيك",
        "root": "ḥ-r-k",
        "pos": "noun (m., verbal-noun)",
        "gloss_en": "shaking, moving, waving (Form-II verbal noun of ḥarraka)",
        "gloss_he": "תנופה (של קרבן)",
        "saadia_note": "Saadia uses taḥrīk as the regular gloss for Hebrew תְּנוּפָה (the wave-offering, Exod 29:24; Num 6:20).",
        "source": "lane",
        "variants": ["תחריכא", "אלתחריך", "ואלתחריך", "באלתחריך"],
    },
    {
        "id": "shem-name",
        "lemma_ja": "שם",
        "lemma_ar": "سَام",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Shem — the eldest son of Noah; ancestor of the Semitic peoples",
        "gloss_he": "שם (בן נח)",
        "notes": "Homograph with Hebrew שֵׁם ('name') and שָׁם ('there'). Context disambiguates — in Saadia's tafsir the surface שם most often refers to the patriarch.",
        "source": "lane",
        "variants": ["ושם", "לשם", "בשם"],
    },
    {
        "id": "thaman-price",
        "lemma_ja": "ת'מן",
        "lemma_ar": "ثَمَن",
        "root": "th-m-n",
        "pos": "noun (m.)",
        "gloss_en": "price, value, payment in money; (with bi-) for a price, bought with money",
        "gloss_he": "מחיר, ערך, כסף קניין",
        "saadia_note": "In 'al-mushtarī bi-thaman' (Gen 17:12-13), Saadia renders Hebrew מִקְנַת כֶּסֶף ('purchased with silver').",
        "source": "lane",
        "variants": ["בת'מן", "אלת'מן", "ואלת'מן", "באלת'מן", "ת'מנה", "ת'מנהם", "ת'מנך", "אלאת'מאן"],
    },
    {
        "id": "madda-stretch",
        "lemma_ja": "מד",
        "lemma_ar": "مَدَّ",
        "root": "m-d-d",
        "pos": "verb",
        "gloss_en": "to stretch out, to extend, to reach out (especially of the hand)",
        "gloss_he": "פשט, שלח, מתח, הושיט (יד)",
        "saadia_note": "Saadia uses madda as the regular gloss for Hebrew שָׁלַח (to send out / stretch out one's hand, Gen 19:10; 22:10).",
        "source": "lane",
        "variants": [
            "פמד", "ומד", "מדדת",
            "ימד", "פימד", "וימד", "תמד", "אמד",
            "ימדוא", "תמדוא", "מדוא", "מדוה", "מדה", "מדהא",
        ],
    },
    {
        "id": "qaid-leader",
        "lemma_ja": "קאיד",
        "lemma_ar": "قَائِد",
        "root": "q-w-d",
        "pos": "noun / active participle (m.)",
        "gloss_en": "leader, commander, chief, one who leads",
        "gloss_he": "מנהיג, מצביא, ראש, נשיא",
        "saadia_note": "Saadia uses al-quwwād (broken plural of qā'id) as one regular gloss for Hebrew הָעֲבָדִים / שָׂרִים when these denote officials and military officers (Gen 20:8; 40:20).",
        "source": "lane",
        "variants": [
            "אלקאיד", "ואלקאיד", "באלקאיד",
            "קואד", "אלקואד", "ואלקואד", "באלקואד",
            "קואדה", "קואדהם", "קואדכם",
        ],
    },
    {
        "id": "asfal-lower",
        "lemma_ja": "אספל",
        "lemma_ar": "أَسْفَل",
        "root": "s-f-l",
        "pos": "noun / adjective (m., comparative-superlative)",
        "gloss_en": "the lower part, the bottom; below, beneath",
        "gloss_he": "תחתון, החלק התחתון, מתחת",
        "saadia_note": "Saadia uses asfal as the regular gloss for Hebrew תַּחַת in expressions of 'beneath, under' (Gen 35:8 'beneath Bethel'; Deut 32:22 'the depths of the earth').",
        "source": "lane",
        "variants": ["ואספל", "פאספל", "אלאספל", "ואלאספל", "באספל", "אספלה", "אספלהא"],
    },
    {
        "id": "ʿayn-eye",
        "lemma_ja": "עין",
        "lemma_ar": "عَيْن",
        "root": "ʿ-y-n",
        "pos": "noun (f.)",
        "gloss_en": "eye; spring of water; (in textual usage) the letter or visible mark of a written text",
        "gloss_he": "עין; מעיין; (לטקסט) אות, פנים הכתוב",
        "notes": "The broken plural ʿuyūn covers the same range — see ʿuyun-eyes-springs.",
        "source": "lane",
        "variants": [
            "אלעין", "ואלעין", "באלעין",
            "עיני", "עינך", "עיניך", "עיניה", "עיניהא", "עיניהם", "עיניכם",
            "עינאן", "אלעינאן", "עינאך", "ועינאך",
        ],
    },
    {
        "id": "qila-curtain",
        "lemma_ja": "קלע",
        "lemma_ar": "قِلَاع",
        "root": "q-l-ʿ",
        "pos": "noun (m./f.)",
        "gloss_en": "curtain, hanging cloth (especially a courtyard or sail-cloth)",
        "gloss_he": "קלע, יריעת חצר",
        "saadia_note": "Saadia uses qulūʿ (pl. of qilāʿ) as the regular gloss for Hebrew קְלָעִים (the courtyard hangings of the Tabernacle, Exod 27:9ff).",
        "source": "lane",
        "variants": ["אלקלע", "ואלקלע", "באלקלע", "קלוע", "אלקלוע", "ואלקלוע", "באלקלוע"],
    },
    {
        "id": "taʿal-come",
        "lemma_ja": "תעאל",
        "lemma_ar": "تَعَالَ",
        "root": "ʿ-l-w",
        "pos": "verb (imperative)",
        "gloss_en": "come! (imperative — literally 'be exalted toward me')",
        "gloss_he": "בא! בואו! (ציווי)",
        "notes": "Lexicalized imperative — historically the imperative of taʿālā 'to be exalted', but used in classical Arabic and Saadia's JA as a bare 'come!' Saadia's regular gloss for Hebrew לְכָה / לֵךְ.",
        "source": "lane",
        "variants": ["תעאלו", "תעאלוא", "ותעאל", "פתעאל", "תעאלי"],
    },
    {
        "id": "tala-be-long",
        "lemma_ja": "טאל",
        "lemma_ar": "طَالَ",
        "root": "ṭ-w-l",
        "pos": "verb",
        "gloss_en": "to be long, to last long, to endure",
        "gloss_he": "ארך, נמשך זמן רב, האריך ימים",
        "saadia_note": "Saadia uses ṭāla as the regular gloss for Hebrew אָרַךְ in 'that your days may be long' (Deut 11:9; 11:21).",
        "source": "lane",
        "variants": [
            "יטול", "תטול", "אטול", "נטול",
            "יטולון", "יטולוא", "תטולון",
            "ויטול", "פיטול", "ותטול", "פתטול",
            "טאלת", "טאלוא",
        ],
    },
    {
        "id": "daraba-strike",
        "lemma_ja": "צ'רב",
        "lemma_ar": "ضَرَبَ",
        "root": "ḍ-r-b",
        "pos": "verb",
        "gloss_en": "to strike, to beat, to hit; (idiomatic) to utter (a parable or proverb)",
        "gloss_he": "הכה, פגע; (ביטוי) משל משל",
        "saadia_note": "Saadia uses ḍaraba mathalan as the regular gloss for Hebrew נָשָׂא מָשָׁל ('to take up a parable', Balaam's oracles, Num 23-24).",
        "source": "lane",
        "variants": [
            "פצ'רב", "וצ'רב", "אצ'רב", "תצ'רב",
            "יצ'רב", "פיצ'רב", "ויצ'רב", "נצ'רב",
            "צ'רבת", "צ'רבוא", "צ'רבו",
            "אצ'רבוא", "תצ'רבוא", "פיצ'רבון",
            "צ'אריב", "אלצ'אריב", "מצ'רוב",
        ],
    },
]


VARIANTS_PATCH = {
    "hifz-charge":            ["ואחפץ", "פאחפץ", "אחפצוא", "פאחפצוא", "ואחפצוא"],
    "taHawwuz-possession":    ["לתחוזוה", "תחוזוה", "ולתחוזוה"],
    "ʿuyun-eyes-springs":     ["עינאך"],
}

STARTER_VARIANTS_PATCH = {
    "ard":   ["ארצ'ך", "ארצ'ה", "ארצ'הא", "ארצ'הם", "ארצ'נא", "ארצ'י",
              "אלארץ'", "ואלארץ'", "באלארץ'", "ארץ'ך"],
    "jalad": ["גלוד", "אלגלוד", "ואלגלוד", "גלודה", "גלודהם", "באלגלוד"],
}


def main():
    lane_path = pathlib.Path("data/dictionary-lane.json")
    starter_path = pathlib.Path("data/dictionary-starter.json")
    if not lane_path.exists() or not starter_path.exists():
        print("FATAL: dict files not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    d = json.loads(lane_path.read_text())
    ds = json.loads(starter_path.read_text())

    # --- Pass 1: append NEW_ENTRIES to lane ---
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

    # --- Pass 2: lane variant patches ---
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

    # --- Pass 3: starter variant patches ---
    by_id_s = {e["id"]: e for e in ds["entries"]}
    s_variant_added = 0
    s_variant_skipped = []
    for entry_id, new_variants in STARTER_VARIANTS_PATCH.items():
        if entry_id not in by_id_s:
            s_variant_skipped.append((entry_id, "id not found in starter"))
            continue
        target = by_id_s[entry_id]
        existing_variants = target.setdefault("variants", [])
        for v in new_variants:
            if v in existing_variants:
                s_variant_skipped.append((entry_id, f"already had {v}"))
                continue
            existing_variants.append(v)
            s_variant_added += 1

    # --- Write back + validate round-trip ---
    lane_path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    starter_path.write_text(json.dumps(ds, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())
    json.loads(starter_path.read_text())

    print(f"LANE — Added {added} new entries. Skipped: {len(skipped)}")
    for s, reason in skipped:
        print(f"  - {s}: {reason}")
    print(f"LANE — Added {variant_added} variants. Skipped: {len(variant_skipped)}")
    for s, reason in variant_skipped:
        print(f"  - {s}: {reason}")
    print(f"STARTER — Added {s_variant_added} variants. Skipped: {len(s_variant_skipped)}")
    for s, reason in s_variant_skipped:
        print(f"  - {s}: {reason}")
    print(f"Lane total entries now: {len(d['entries'])}")
    print(f"Starter total entries: {len(ds['entries'])}")


if __name__ == "__main__":
    main()

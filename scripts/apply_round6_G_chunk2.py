#!/usr/bin/env python3
"""Phase 2 Round 6 Batch G chunk 2 — long-tail sweep (no API).

21 new lemma entries + 3 variant patches against existing entries (madhbah,
ʿamila-do-act, ila-h-god). Skipped: רת (count 14, no contexts) again.
Skipped: צנדוק bare form (auto-covered by aṣ-ṣundūq entry's lemma).
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Verbs ----------
    {
        "id": "mada-go",
        "lemma_ja": "מצ'א",
        "lemma_ar": "مَضَى",
        "root": "m-ḍ-y",
        "pos": "verb",
        "gloss_en": "to go, to proceed, to pass on, to go forth, to elapse",
        "gloss_he": "הלך, יצא לדרך, עבר, חלף",
        "source": "lane",
        "variants": [
            "פמצ'א", "ומצ'א", "אמץ'", "ואמץ'", "פאמץ'",
            "ימצ'י", "פימצ'י", "אמצ'י", "תמצ'י", "נמצ'י",
            "ומצ'ו", "ומצ'וא", "פמצ'וא", "אמצ'ו", "אמצ'וא",
            "מצ'יתם", "מצ'ינא", "מצ'יתה", "מצ'יתהא",
        ],
    },
    {
        "id": "baqiya-remain",
        "lemma_ja": "בקי",
        "lemma_ar": "بَقِيَ",
        "root": "b-q-y",
        "pos": "verb / proper noun",
        "gloss_en": "to remain, to be left over, to endure; (as proper noun) Bukki (a personal name, Num 34:22)",
        "gloss_he": "נשאר, נותר, התקיים; (כשם פרטי) בקי",
        "notes": "Homograph: the verb baqiya and the biblical proper noun Bukki share the same surface form. Context disambiguates.",
        "source": "lane",
        "variants": [
            "יבקי", "תבקי", "אבקי", "פבקי", "פיבקי",
            "בקיא", "בקיו", "בקיוא", "בקית", "בקיתם", "וביקי",
            "באקי", "אלבאקי", "ואלבאקי", "באקיה", "אלבאקיה",
            "באקין", "אלבאקין",
        ],
    },
    {
        "id": "nala-attain",
        "lemma_ja": "נאל",
        "lemma_ar": "نَالَ",
        "root": "n-w-l",
        "pos": "verb",
        "gloss_en": "to attain, to reach, to obtain, to acquire, to come into possession of",
        "gloss_he": "השיג, השיגה ידו, הגיע ל-, רכש",
        "saadia_note": "Saadia uses 'mā tanāl yad-' as the regular gloss for Hebrew הִשִּׂיגָה יָדוֹ / כְּפִי מַתְּנַת יָדוֹ ('within his means', 'according to what his hand can attain').",
        "source": "lane",
        "variants": [
            "ינאל", "תנאל", "אנאל", "ננאל",
            "ינאלון", "ינאלוא", "תנאלון",
            "ינילה", "תנילה", "תנילך", "תנילני",
            "נאלת", "נאלוא", "נאלהם", "נאלה",
            "ונאל", "פנאל", "תנילהא",
        ],
    },
    {
        "id": "aqsama-swear",
        "lemma_ja": "אקסם",
        "lemma_ar": "أَقْسَمَ",
        "root": "q-s-m",
        "pos": "verb (form IV)",
        "gloss_en": "to swear (an oath), to take an oath, to make a solemn pledge",
        "gloss_he": "נשבע, השביע, נדר",
        "saadia_note": "Saadia uses aqsama as the regular gloss for Hebrew נִשְׁבַּע, especially in 'God's oath to the patriarchs' formulations.",
        "source": "lane",
        "variants": [
            "אקסמת", "ואקסם", "פאקסם",
            "תקסם", "יקסם", "נקסם",
            "אקסמו", "אקסמוא", "אקסמתם", "אקסמתה", "אקסמתהא",
            "יקסמון", "יקסמוא",
            "מקסמא", "אלמקסם", "ואלמקסם",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "shaʿb-people",
        "lemma_ja": "שעב",
        "lemma_ar": "شَعْب",
        "root": "sh-ʿ-b",
        "pos": "noun (m.)",
        "gloss_en": "people, nation, tribal collective",
        "gloss_he": "עם, אומה, ציבור",
        "notes": "Used by Saadia alongside qawm and umma for Hebrew עַם — especially in poetic and oracular contexts (e.g. Balaam's oracles, Num 23).",
        "source": "lane",
        "variants": [
            "אלשעב", "ואלשעב", "באלשעב",
            "שעבא", "שעבי", "שעבך", "שעבכם", "שעבה", "שעבהם", "שעבהא",
            "אלשעוב", "ואלשעוב", "שעוב",
        ],
    },
    {
        "id": "sabt-sabbath",
        "lemma_ja": "סבת",
        "lemma_ar": "سَبْت",
        "root": "—",
        "pos": "noun (m.)",
        "gloss_en": "Sabbath, the day of rest, Saturday",
        "gloss_he": "שבת",
        "saadia_note": "Saadia retains the Hebrew form סבת for שַׁבָּת. The Arabic cognate sabt has the same denotation but is more limited in classical usage to 'Saturday'.",
        "source": "lane",
        "variants": [
            "אלסבת", "ואלסבת", "באלסבת", "פי אלסבת",
            "סבתא", "סבתכם", "סבתות", "אלסבתות", "ואלסבתות",
            "סבת'", "אלסבת'",
        ],
    },
    {
        "id": "sunduq-box-ark",
        "lemma_ja": "צנדוק",
        "lemma_ar": "صُنْدُوق",
        "root": "ṣ-n-d-q",
        "pos": "noun (m.)",
        "gloss_en": "box, chest, casket, ark; a wooden or metal container with a lid",
        "gloss_he": "תיבה, ארגז, ארון",
        "saadia_note": "Saadia uses ṣundūq as the regular gloss for Hebrew אָרוֹן (the Ark of the Covenant; the box for the broken tablets, Deut 10:2).",
        "source": "lane",
        "variants": [
            "אלצנדוק", "ואלצנדוק", "באלצנדוק", "פי אלצנדוק",
            "צנדוקא", "צנדוקה", "צנדוקין", "צנאדיק", "אלצנאדיק",
        ],
    },
    {
        "id": "qasʿa-bowl",
        "lemma_ja": "קצעה",
        "lemma_ar": "قَصْعَة",
        "root": "q-ṣ-ʿ",
        "pos": "noun (f.)",
        "gloss_en": "bowl, dish, large basin (especially for serving food or holding offerings)",
        "gloss_he": "קערה, אגן, צלחת גדולה",
        "saadia_note": "Saadia uses qaṣʿa as the regular gloss for Hebrew קְעָרָה (the silver basin of each tribal offering, Num 7:13ff).",
        "source": "lane",
        "variants": ["אלקצעה", "ואלקצעה", "באלקצעה", "קצעאת", "אלקצעאת", "ואלקצעאת", "קצעתי"],
    },
    {
        "id": "ams-yesterday",
        "lemma_ja": "אמס",
        "lemma_ar": "أَمْس",
        "root": "—",
        "pos": "adverb",
        "gloss_en": "yesterday; (in the construction mithl ams) as before, as in time past",
        "gloss_he": "אתמול, יום אתמול",
        "source": "lane",
        "variants": ["אמסא", "באלאמס", "ואמס"],
    },
    {
        "id": "khayr-good",
        "lemma_ja": "כ'יר",
        "lemma_ar": "خَيْر",
        "root": "kh-y-r",
        "pos": "noun (m.) / adjective",
        "gloss_en": "good, goodness, benefit, prosperity; (in comparative usage) better",
        "gloss_he": "טוב, טובה, ברכה, שפע",
        "saadia_note": "Saadia uses khayr as the regular gloss for Hebrew טוֹב in moral and beneficent senses ('do good', 'God planned good').",
        "source": "lane",
        "variants": [
            "כ'ירא", "אלכ'יר", "ואלכ'יר", "באלכ'יר", "וכ'יר",
            "כ'יראת", "אלכ'יראת", "ואלכ'יראת",
            "כ'ירך", "כ'ירכם", "כ'ירה", "כ'ירהם",
        ],
    },
    {
        "id": "ʿumr-life",
        "lemma_ja": "עמר",
        "lemma_ar": "عُمْر",
        "root": "ʿ-m-r",
        "pos": "noun (m.)",
        "gloss_en": "life, lifetime, age, span of life",
        "gloss_he": "חיים, אורך ימים, גיל",
        "saadia_note": "Saadia uses ʿumr as the regular gloss for Hebrew יָמִים / שְׁנֵי חַיִּים in genealogical age formulas ('all the days of his life').",
        "source": "lane",
        "variants": [
            "עמרה", "עמרהם", "עמרי", "עמרך", "עמרכם",
            "אלעמר", "ואלעמר", "באלעמר", "עמרהא", "עמרא",
            "אלאעמאר", "אעמאר",
        ],
    },
    {
        "id": "lawh-tablet",
        "lemma_ja": "לוח",
        "lemma_ar": "لَوْح",
        "root": "l-w-ḥ",
        "pos": "noun (m.)",
        "gloss_en": "tablet, plank, board, slab (especially of stone or wood)",
        "gloss_he": "לוח (אבן, עץ או מתכת)",
        "saadia_note": "Saadia uses lawḥ as the regular gloss for Hebrew לוּחַ (the tablets of stone at Sinai; Deut 10:1-3).",
        "source": "lane",
        "variants": [
            "אללוח", "ואללוח", "באללוח",
            "לוחי", "לוחין", "אללוחין", "ואללוחין", "לוחיהמא",
            "אלואח", "אלאלואח", "ואלאלואח", "לוחא",
        ],
    },
    {
        "id": "malʿun-cursed",
        "lemma_ja": "מלעון",
        "lemma_ar": "مَلْعُون",
        "root": "l-ʿ-n",
        "pos": "passive participle / adjective (m.)",
        "gloss_en": "cursed, accursed, under a curse",
        "gloss_he": "ארור, מקולל",
        "saadia_note": "Saadia's regular gloss for Hebrew אָרוּר, especially in the Mount Ebal curses (Deut 27).",
        "source": "lane",
        "variants": [
            "ומלעון", "אלמלעון", "ואלמלעון",
            "מלעונין", "אלמלעונין", "ומלעונין",
            "מלעונה", "אלמלעונה", "מלעונאת", "אלמלעונאת",
        ],
    },
    {
        "id": "ʿutla-rest-day",
        "lemma_ja": "עטלה",
        "lemma_ar": "عُطْلَة",
        "root": "ʿ-ṭ-l",
        "pos": "noun (f.)",
        "gloss_en": "rest, day of rest, cessation from work, holiday",
        "gloss_he": "מנוחה, יום שבתון, השבתת מלאכה",
        "saadia_note": "Saadia uses ʿuṭla as the regular gloss for Hebrew שַׁבָּתוֹן, pairing with sabt to render the full phrase שַׁבַּת שַׁבָּתוֹן (e.g. Exod 16:23; 31:15).",
        "source": "lane",
        "variants": ["אלעטלה", "ואלעטלה", "באלעטלה", "עטלתכם", "עטלתהם"],
    },
    {
        "id": "maʿdud-counted",
        "lemma_ja": "מעדוד",
        "lemma_ar": "مَعْدُود",
        "root": "ʿ-d-d",
        "pos": "passive participle / adjective",
        "gloss_en": "counted, numbered, enumerated, accounted",
        "gloss_he": "פקוד, נמנה, נספר",
        "saadia_note": "Saadia uses al-maʿdūdīn as the regular gloss for Hebrew הַפְּקֻדִים (those numbered in the wilderness census, Num 1-4).",
        "source": "lane",
        "variants": [
            "אלמעדודין", "ואלמעדודין", "באלמעדודין",
            "מעדודין", "מעדודון", "אלמעדודון",
            "אלמעדוד", "ואלמעדוד", "מעדודה", "אלמעדודה",
        ],
    },
    {
        "id": "aimma-priests",
        "lemma_ja": "אימה",
        "lemma_ar": "أَئِمَّة",
        "root": "'-m-m",
        "pos": "noun (m., broken plural)",
        "gloss_en": "imams, religious leaders; (Saadia) the priests",
        "gloss_he": "כהנים, מנהיגי דת",
        "saadia_note": "Saadia uses al-a'imma (pl. of imām) as the regular gloss for Hebrew הַכֹּהֲנִים (the priests / sons of Aaron). The singular imām renders הַכֹּהֵן.",
        "source": "lane",
        "variants": [
            "אלאימה", "ואלאימה", "באלאימה", "אימה'",
            "אמאם", "אלאמאם", "ואלאמאם", "באלאמאם", "לאלאמאם",
            "אמאמא", "אמאמך", "אמאמכם",
        ],
    },
    {
        "id": "ʿuyun-eyes-springs",
        "lemma_ja": "עיון",
        "lemma_ar": "عُيُون",
        "root": "ʿ-y-n",
        "pos": "noun (m., broken plural)",
        "gloss_en": "eyes; springs of water; (in textual usage) the letters or contents of a written text",
        "gloss_he": "עיניים; מעיינות מים; (לטקסט כתוב) אותיות הכתוב",
        "notes": "Broken plural of ʿayn ('eye, spring, source'). Saadia uses ʿuyūn in three distinct senses: (1) eyes — perception/awareness; (2) springs — water sources; (3) text — the letters/words of a written document.",
        "saadia_note": "In the Mount Ebal stone-engraving passage (Deut 27:3, 8), Saadia uses עיון הד'ה אלתורייה for 'the words/letters of this Torah'.",
        "source": "lane",
        "variants": ["אלעיון", "ואלעיון", "באלעיון", "עיונהא", "עיונה", "עיונכם", "עיונהם", "עיוני"],
    },
    {
        "id": "takhm-border",
        "lemma_ja": "תכ'ם",
        "lemma_ar": "تَخْم",
        "root": "—",
        "pos": "noun (m.)",
        "gloss_en": "border, boundary, frontier, limit of a territory",
        "gloss_he": "גבול, תחום, קצה",
        "saadia_note": "Saadia uses takhm as the regular gloss for Hebrew גְּבוּל (territorial border).",
        "source": "lane",
        "variants": [
            "תכ'מך", "תכ'מי", "תכ'מה", "תכ'מהם", "תכ'מהא",
            "תכ'ום", "אלתכ'ום", "ואלתכ'ום",
            "אלתכ'ם", "ואלתכ'ם", "תכ'מא",
        ],
    },
    {
        "id": "wadi-valley",
        "lemma_ja": "ואד",
        "lemma_ar": "وَادٍ",
        "root": "w-d-y",
        "pos": "noun (m.)",
        "gloss_en": "valley, dry riverbed, wadi, watercourse",
        "gloss_he": "נחל, ואדי, גיא",
        "saadia_note": "Saadia uses wādī as the regular gloss for Hebrew נַחַל (valley / seasonal watercourse).",
        "source": "lane",
        "variants": [
            "אלואד", "ואלואד", "באלואד",
            "ואדיא", "ואדי'", "אלוואדי", "ואלוואדי",
            "ודיאן", "אלודיאן", "ואלודיאן", "אלאודיה",
        ],
    },

    # ---------- Adjective / participle ----------
    {
        "id": "mamluww-filled",
        "lemma_ja": "ממלוו",
        "lemma_ar": "مَمْلُوء",
        "root": "m-l-'",
        "pos": "passive participle / adjective (m.)",
        "gloss_en": "filled, full (especially: filled with a specified substance)",
        "gloss_he": "מלא, ממולא",
        "saadia_note": "Saadia uses mamlū' as the regular gloss for Hebrew מָלֵא in the tribal-gift incense-spoon formula (Num 7:14ff: 'a gold spoon filled with incense').",
        "source": "lane",
        "variants": [
            "ממלווא", "ממלוון", "ממלווה", "ממלווין",
            "אלממלוו", "אלממלוון", "ממלי", "אלממלי",
            "ממלייה",
        ],
    },
]


VARIANTS_PATCH = {
    "madhbah":         ["ואלמד'בח", "באלמד'בח", "מד'בחא", "ואלמד'אבח", "מד'בחהם"],
    "ʿamila-do-act":   ["ואעמלו", "אעמלו", "אעמלוא"],
    "ila-h-god":       ["אלאהא"],
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

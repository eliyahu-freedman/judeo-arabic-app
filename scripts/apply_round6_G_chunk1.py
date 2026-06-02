#!/usr/bin/env python3
"""Phase 2 Round 6 Batch G chunk 1 — inline long-tail sweep (no API).

23 new lemma entries + 1 variant patch (ות'ורא → thawr-bull), drawn from the
top-25 post-F miss queue (counts 13-14). Same pattern as apply_round6_F.py.

Skipped: רת (count 14) — no context hits in the index, surface too ambiguous
to gloss confidently without a verse to disambiguate. Will revisit if it
resurfaces with context after later batches.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Nouns ----------
    {
        "id": "dhikra-remembrance",
        "lemma_ja": "ד'כרא",
        "lemma_ar": "ذِكْرَى",
        "root": "dh-k-r",
        "pos": "noun (f., verbal-noun)",
        "gloss_en": "remembrance, memorial, reminder; a thing called to mind",
        "gloss_he": "זכר, זיכרון",
        "source": "lane",
        "variants": ["ד'כראהם", "ד'כראך", "ד'כראכם", "ד'כראהא"],
    },
    {
        "id": "muqim-resident",
        "lemma_ja": "מקים",
        "lemma_ar": "مُقِيم",
        "root": "q-w-m",
        "pos": "active participle / noun (m.)",
        "gloss_en": "resident, dweller, one who resides or stays in a place",
        "gloss_he": "תושב, יושב, מתגורר",
        "source": "lane",
        "variants": ["אלמקים", "מקימין", "אלמקימין", "ומקימין", "ואלמקימין", "מקימה", "אלמקימה"],
    },
    {
        "id": "qist-measure",
        "lemma_ja": "קסט",
        "lemma_ar": "قِسْط",
        "root": "q-s-ṭ",
        "pos": "noun (m.)",
        "gloss_en": "qist — a measure of capacity (about half a hin / quarter of a kor); also: justice, equity, fairness",
        "gloss_he": "מידה (כקסת/כהין); צדק, יושר",
        "saadia_note": "Saadia uses qisṭ as the regular gloss for Hebrew הִין (the Tabernacle liquid-measure).",
        "source": "lane",
        "variants": ["אלקסט", "ואלקסט", "וקסט", "קסטא"],
    },
    {
        "id": "dayʿa-estate",
        "lemma_ja": "צ'יעה",
        "lemma_ar": "ضَيْعَة",
        "root": "ḍ-y-ʿ",
        "pos": "noun (f.)",
        "gloss_en": "estate, landed property, plot of land, field, village or rural settlement",
        "gloss_he": "שדה, נחלה, אחוזה, חלקת קרקע",
        "saadia_note": "Saadia uses ḍayʿa as the regular gloss for Hebrew שָׂדֶה in property/legal and topographic contexts (e.g. Gen 23 Machpelah, Num 23 Balaam's heights).",
        "source": "lane",
        "variants": [
            "אלצ'יעה", "ואלצ'יעה", "צ'יעה'", "באלצ'יעה",
            "אלצ'יאע", "צ'יאע", "ואלצ'יאע", "באלצ'יאע",
            "צ'יעתה", "צ'יעתהא",
        ],
    },
    {
        "id": "hadiyya-gift",
        "lemma_ja": "הדייה",
        "lemma_ar": "هَدِيَّة",
        "root": "h-d-y",
        "pos": "noun (f.)",
        "gloss_en": "gift, present, offering brought to a superior or to God",
        "gloss_he": "מתנה, מנחה, שי",
        "saadia_note": "Saadia uses hadiyya as one regular gloss for Hebrew מִנְחָה (gift, offering), especially in non-cultic contexts (Cain in Gen 4, Jacob's gift to Esau in Gen 32).",
        "source": "lane",
        "variants": ["אלהדייה", "ואלהדייה", "באלהדייה", "הדאיא", "הדאיאהם", "הדאיאכם", "הדייה'"],
    },
    {
        "id": "tawrah-torah",
        "lemma_ja": "תורייה",
        "lemma_ar": "تَوْرَاة",
        "root": "—",
        "pos": "proper noun (f.)",
        "gloss_en": "the Torah — the Five Books of Moses, the Mosaic Law",
        "gloss_he": "התורה",
        "source": "lane",
        "variants": [
            "אלתורייה", "ואלתורייה", "באלתורייה", "לאלתורייה",
            "תורייתה", "תורייתכם", "תורייתי",
            "אלתוראה", "תוראה",
        ],
    },
    {
        "id": "sahra-wilderness",
        "lemma_ja": "צחרי",
        "lemma_ar": "صَحْرَاء",
        "root": "ṣ-ḥ-r",
        "pos": "noun (f.)",
        "gloss_en": "the open country, the wilderness, the wide expanse outside settled areas",
        "gloss_he": "שדה פתוח, מדבר, אזור פתוח",
        "saadia_note": "Saadia uses al-ṣaḥrā' for Hebrew הַשָּׂדֶה in the sense of 'open country / wilderness' (e.g. Exod 22:30 'flesh torn in the field').",
        "source": "lane",
        "variants": ["אלצחרי", "ואלצחרי", "באלצחרי", "צחראא", "אלצחראא", "צחרא", "צחראהא"],
    },
    {
        "id": "shuqqa-curtain-panel",
        "lemma_ja": "שקה",
        "lemma_ar": "شُقَّة",
        "root": "sh-q-q",
        "pos": "noun (f.)",
        "gloss_en": "a length of fabric, a panel, a curtain (especially of woven cloth or felt)",
        "gloss_he": "יריעה (של אריג)",
        "saadia_note": "Saadia uses shuqqa as the regular gloss for Hebrew יְרִיעָה (the Tabernacle curtains, Exod 26).",
        "source": "lane",
        "variants": ["אלשקה", "ואלשקה", "באלשקה", "שקה'", "אלשקאק", "שקאק", "ואלשקאק", "אלשקקאת", "שקקאת"],
    },
    {
        "id": "ruʾya-vision",
        "lemma_ja": "רויא",
        "lemma_ar": "رُؤْيَا",
        "root": "r-'-y",
        "pos": "noun (f.)",
        "gloss_en": "vision, dream-vision; a prophetic seeing",
        "gloss_he": "חזון, מראה, חלום נבואי",
        "source": "lane",
        "variants": ["אלרויא", "ואלרויא", "רוי'", "רויאה", "רויאך", "רויאהם", "רויאכם", "רויאי"],
    },
    {
        "id": "ithm-sin-guilt",
        "lemma_ja": "את'ם",
        "lemma_ar": "إِثْم",
        "root": "'-th-m",
        "pos": "noun (m.)",
        "gloss_en": "sin, guilt, transgression, moral offense",
        "gloss_he": "אשם, חטא, פשע",
        "saadia_note": "In sacrificial contexts קרבאן אלאת'ם renders Hebrew אָשָׁם (guilt-offering).",
        "source": "lane",
        "variants": ["אלאת'ם", "ואלאת'ם", "באלאת'ם", "את'מה", "את'מהם", "את'מכם", "את'מי"],
    },
    {
        "id": "dhakwa-offering",
        "lemma_ja": "דכוה",
        "lemma_ar": "ذَكْوَة",
        "root": "dh-k-w",
        "pos": "noun (f., verbal-noun)",
        "gloss_en": "an act of ritual slaughter; (Saadia, technical) the sin-offering",
        "gloss_he": "(אצל סעדיה) חטאת",
        "saadia_note": "Saadia uses ḏakwa as the regular gloss for Hebrew חַטָּאת (sin-offering). In classical Arabic the underlying root denotes ritual slaughter (ḏakāh).",
        "source": "lane",
        "variants": [
            "אלדכוה", "ואלדכוה", "באלדכוה", "לאלדכוה", "ולאלדכוה",
            "דכותה", "דכותהם", "ודכותהם", "דכותכם", "דכותהא",
        ],
    },

    # ---------- Hebrew loans / retained Hebrew nouns ----------
    {
        "id": "ʿever-trans",
        "lemma_ja": "עבר",
        "lemma_ar": "—",
        "root": "—",
        "pos": "noun (m.)",
        "gloss_en": "the far side, the trans-(river) region; (in construct, e.g. עבר הירדן) across the Jordan",
        "gloss_he": "עבר, צד שני (של נהר)",
        "saadia_note": "Saadia retains the Hebrew noun עֵבֶר ('side, beyond') in the construct phrase עבר אלארדן for the trans-Jordanian region.",
        "notes": "Homograph with the classical Arabic verb ʿabara 'he crossed' (root ʿ-b-r) — context disambiguates.",
        "source": "lane",
        "variants": ["באלעבר", "ועבר", "פי עבר"],
    },
    {
        "id": "amin-amen",
        "lemma_ja": "אמין",
        "lemma_ar": "آمِين",
        "root": "—",
        "pos": "interjection",
        "gloss_en": "amen — so be it; (affirmation of oaths and curses)",
        "gloss_he": "אמן",
        "source": "lane",
        "variants": [],
    },

    # ---------- Adjectives / participles ----------
    {
        "id": "sahih-sound",
        "lemma_ja": "צחיח",
        "lemma_ar": "صَحِيح",
        "root": "ṣ-ḥ-ḥ",
        "pos": "adjective",
        "gloss_en": "healthy, sound, intact, whole, unblemished",
        "gloss_he": "בריא, שלם, תמים (לקרבן)",
        "saadia_note": "Saadia uses ṣaḥīḥ as the regular gloss for Hebrew תָּמִים in sacrificial contexts ('without blemish').",
        "source": "lane",
        "variants": [
            "צחיחא", "צחיחה", "צחאחא", "צחאח",
            "אלצחיח", "אלצחיחה", "ואלצחיח", "ואלצחיחה",
            "צחיחין", "אלצחאח", "ואלצחאח",
        ],
    },
    {
        "id": "muqaddas-holy",
        "lemma_ja": "מקדס",
        "lemma_ar": "مُقَدَّس",
        "root": "q-d-s",
        "pos": "passive participle / adjective (m.)",
        "gloss_en": "sanctified, holy, consecrated, set apart",
        "gloss_he": "מקודש, קדוש",
        "saadia_note": "Saadia's regular gloss for Hebrew קָדוֹשׁ.",
        "source": "lane",
        "variants": [
            "מקדסא", "מקדסה", "מקדסין", "ומקדסין",
            "אלמקדס", "ואלמקדס", "אלמקדסה", "אלמקדסון", "אלמקדסין",
        ],
    },

    # ---------- Verbs ----------
    {
        "id": "ajaba-answer",
        "lemma_ja": "אגאב",
        "lemma_ar": "أَجَابَ",
        "root": "j-w-b",
        "pos": "verb (form IV)",
        "gloss_en": "to answer, to reply, to respond",
        "gloss_he": "ענה, השיב",
        "source": "lane",
        "variants": [
            "אגאבה", "פאגאבה", "אגאבהם", "פאגאבהם", "אגאבני", "פאגאבני",
            "אגאבא", "אגאבוא", "אגאבו",
            "יגיב", "פיגיב", "ויגיב", "תגיב", "אגיב", "נגיב",
            "ויגיבון", "ויגיבוא", "פיגיבוא",
            "אגבה", "אגבני", "אגיבני",
        ],
    },
    {
        "id": "nazara-look",
        "lemma_ja": "נצ'ר",
        "lemma_ar": "نَظَرَ",
        "root": "n-ẓ-r",
        "pos": "verb",
        "gloss_en": "to look, to see, to observe, to behold",
        "gloss_he": "הביט, ראה, התבונן",
        "notes": "Surface אנצ'ר covers both 1ms imperfect 'anẓuru ('I look') and the imperative unẓur ('look!') — context disambiguates.",
        "source": "lane",
        "variants": [
            "אנצ'ר", "ואנצ'ר", "פאנצ'ר",
            "אנצ'רו", "אנצ'רוא", "ואנצ'רו", "ואנצ'רוא",
            "ינצ'ר", "וינצ'ר", "תנצ'ר", "ננצ'ר",
            "ינצ'רון", "ינצ'רוא", "נצ'רו", "נצ'רוא",
            "נצ'ר", "ונצ'ר", "פנצ'ר",
        ],
    },
    {
        "id": "raʾa-see",
        "lemma_ja": "ראי",
        "lemma_ar": "رَأَى",
        "root": "r-'-y",
        "pos": "verb",
        "gloss_en": "to see, to look at, to perceive, to behold",
        "gloss_he": "ראה, הסתכל, ראה והכיר",
        "source": "lane",
        "variants": [
            "ראי'", "ראא", "ראיא",
            "ראת", "וראת", "פראת",
            "ראינא", "וראינא", "פראינא",
            "ראית", "ראיתה", "ראיתהא", "ראיתם",
            "ראיתך", "ראיתכם",
            "ויראהא", "ויראה", "פיראה",
            "תראי", "תראה", "תרי",
            "אראך", "אראה", "אראהם",
        ],
    },
    {
        "id": "daʿa-call",
        "lemma_ja": "דעא",
        "lemma_ar": "دَعَا",
        "root": "d-ʿ-w",
        "pos": "verb / noun (m.)",
        "gloss_en": "to call, to summon, to invoke, to pray; (as noun duʿā') a call, prayer, supplication",
        "gloss_he": "קרא, קרא בשם, התפלל; (כשם עצם) תפילה, קריאה",
        "notes": "Homograph: the surface דעא covers both the perfect verb daʿā ('he called') and the verbal noun duʿā' ('prayer'). Context disambiguates.",
        "source": "lane",
        "variants": [
            "ידעא", "ידעו", "ידעי", "ויידעא", "ויידעו",
            "פדעא", "ודעא", "תדעא",
            "דעאני", "דעאנא", "דעאכם", "דעאהם", "דעאה", "דעאהא",
            "דעיתה", "דעיתהא",
            "אדעי", "תדעי", "ידעי", "נדעי",
        ],
    },
    {
        "id": "khala-except",
        "lemma_ja": "כ'לא",
        "lemma_ar": "خَلَا",
        "root": "kh-l-w",
        "pos": "preposition (with mā)",
        "gloss_en": "(with preceding mā) except, save for, apart from",
        "gloss_he": "מלבד, חוץ מ-, פרט ל-",
        "notes": "Construction מא כ'לא (mā khalā) functions as 'except, save for'. The verb khalā literally means 'to be empty / devoid (of)'.",
        "source": "lane",
        "variants": ["וכ'לא", "פכ'לא"],
    },
    {
        "id": "asma-name",
        "lemma_ja": "אסמי",
        "lemma_ar": "أَسْمَى",
        "root": "s-m-w",
        "pos": "verb (form IV)",
        "gloss_en": "to give a name to, to name, to call (someone) by a name",
        "gloss_he": "קרא בשם, נתן שם",
        "source": "lane",
        "variants": [
            "אסמת", "ואסמת", "אסמתה", "ואסמתה", "פאסמתה",
            "אסמאה", "אסמאהם", "אסמיתה", "אסמיתהא",
            "ויסמי", "ויסמיהא", "ויסמיה",
        ],
    },
    {
        "id": "sanada-lay-upon",
        "lemma_ja": "סנד",
        "lemma_ar": "سَنَدَ",
        "root": "s-n-d",
        "pos": "verb",
        "gloss_en": "to lay (a hand) upon; to lean upon, support, prop",
        "gloss_he": "סמך, השעין, הניח (יד)",
        "saadia_note": "Saadia uses sanada as the regular gloss for Hebrew סָמַךְ in the 'laying of hands' on a sacrifice (Exod 29:10, Lev 1:4 and parallels).",
        "source": "lane",
        "variants": [
            "יסנד", "ויסנד", "אסנד", "ואסנד", "פיסנד",
            "תסנד", "נסנד",
            "ויסנדו", "ויסנדוא", "אסנדו", "אסנדוא",
            "פסנד", "וסנד", "סנדה", "סנדהא",
        ],
    },

    # ---------- Adverb ----------
    {
        "id": "hinaidh-then",
        "lemma_ja": "חיניד",
        "lemma_ar": "حِينَئِذٍ",
        "root": "—",
        "pos": "adverb",
        "gloss_en": "at that time, then, in that moment",
        "gloss_he": "אז, באותו הזמן",
        "notes": "Compound demonstrative adverb: ḥīna (time) + iḏ (when/that-time).",
        "source": "lane",
        "variants": ["וחיניד", "פחיניד"],
    },
]


VARIANTS_PATCH = {
    "thawr-bull": ["ות'ורא", "ת'ורא"],
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

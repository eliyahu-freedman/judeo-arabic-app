#!/usr/bin/env python3
"""Phase 2 Round 4 Batch A — Proper names.

Adds ~28 new lemma entries to data/dictionary-lane.json for patriarchs,
tribal/personal names, biblical places, and Saadia's gazetteer
Arabic-name renderings of biblical locations.

Per plan: gazetteer entries (Nile=Pishon, Zawila=Havilah, etc.) get the
biblical identification in gloss_en/gloss_he and NO saadia_note — they are
medieval geographic identifications, not Saadia twists. Retained-name
entries (Lot, Abimelech, etc.) also avoid saadia_note unless the form
itself is Arabicized (אסמאעיל for Ishmael).
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Patriarchs / personal names (Hebrew retained) ----------
    {
        "id": "lot-name",
        "lemma_ja": "לוט",
        "lemma_ar": "لُوط",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Lot (Abraham's nephew; father of Moab and Ammon)",
        "gloss_he": "לוט",
        "source": "lane",
        "variants": ["ולוט", "ללוט", "בלוט", "ולוטא", "לוטא"],
    },
    {
        "id": "avimelekh-name",
        "lemma_ja": "אבימלך",
        "lemma_ar": "أَبِيمَلِك",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Abimelech (king of Gerar / Philistia in Gen 20-21, 26)",
        "gloss_he": "אבימלך",
        "source": "lane",
        "variants": ["ואבימלך", "לאבימלך", "באבימלך"],
    },
    {
        "id": "rivka-rebecca",
        "lemma_ja": "רבקה",
        "lemma_ar": "رِفْقَة",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Rebecca (Isaac's wife; mother of Jacob and Esau)",
        "gloss_he": "רבקה",
        "source": "lane",
        "variants": ["ורבקה", "לרבקה", "ברבקה", "רבקה'"],
    },
    {
        "id": "nun-name",
        "lemma_ja": "נון",
        "lemma_ar": "نُون",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Nun (father of Joshua, of the tribe of Ephraim)",
        "gloss_he": "נון",
        "source": "lane",
        "variants": ["ונון", "לנון", "בנון"],
    },
    {
        "id": "yehoshua-joshua",
        "lemma_ja": "יהושע",
        "lemma_ar": "يَهُوشَع",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Joshua (son of Nun; Moses' attendant and successor)",
        "gloss_he": "יהושע",
        "source": "lane",
        "variants": ["ויהושע", "ליהושע", "ביהושע"],
    },
    {
        "id": "gershon-name",
        "lemma_ja": "גרשון",
        "lemma_ar": "جَرْشُون",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Gershon (firstborn of Levi; the Gershonite clan)",
        "gloss_he": "גרשון",
        "source": "lane",
        "variants": ["וגרשון", "לגרשון", "בגרשון", "אלגרשוני", "גרשוני", "אלגרשונים"],
    },
    {
        "id": "qehat-kohath",
        "lemma_ja": "קהת",
        "lemma_ar": "قَهَات",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Kohath (second son of Levi; ancestor of Moses, Aaron, Miriam)",
        "gloss_he": "קהת",
        "source": "lane",
        "variants": ["וקהת", "לקהת", "בקהת", "אלקהתי", "קהתי", "אלקהתיין"],
    },
    {
        "id": "hagar-name",
        "lemma_ja": "הגר",
        "lemma_ar": "هَاجَر",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Hagar (Sarah's Egyptian handmaid; mother of Ishmael)",
        "gloss_he": "הגר",
        "source": "lane",
        "variants": ["והגר", "להגר", "בהגר", "הגר'"],
    },
    {
        "id": "amaleq-name",
        "lemma_ja": "עמלק",
        "lemma_ar": "عَمَالِيق",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Amalek (Esau's descendant; the Amalekite nation)",
        "gloss_he": "עמלק",
        "source": "lane",
        "variants": ["ועמלק", "לעמלק", "בעמלק", "אלעמלקי", "עמלקי", "אלעמלקיין", "עמלקיין"],
    },
    {
        "id": "qayin-cain",
        "lemma_ja": "קין",
        "lemma_ar": "قَايِن",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Cain (firstborn of Adam; killer of Abel)",
        "gloss_he": "קין",
        "source": "lane",
        "variants": ["וקין", "לקין", "בקין", "אלקיני", "קיני", "אלקיניין"],
        "notes": "Homograph with the Kenite tribal gentilic — context disambiguates.",
    },
    {
        "id": "havel-abel",
        "lemma_ja": "הבל",
        "lemma_ar": "هَابِيل",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Abel (second son of Adam, killed by Cain)",
        "gloss_he": "הבל",
        "source": "lane",
        "variants": ["והבל", "להבל", "בהבל"],
    },
    {
        "id": "dina-name",
        "lemma_ja": "דינה",
        "lemma_ar": "دِينَة",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Dinah (daughter of Jacob and Leah; Gen 30, 34)",
        "gloss_he": "דינה",
        "source": "lane",
        "variants": ["ודינה", "לדינה", "בדינה", "דינה'"],
    },
    {
        "id": "efron-ephron",
        "lemma_ja": "עפרון",
        "lemma_ar": "عِفْرُون",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Ephron the Hittite (seller of the Machpelah cave; Gen 23)",
        "gloss_he": "עפרון",
        "source": "lane",
        "variants": ["ועפרון", "לעפרון", "בעפרון"],
    },
    {
        "id": "og-name",
        "lemma_ja": "עוג",
        "lemma_ar": "عُوج",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Og (king of Bashan; Num 21, Deut 3)",
        "gloss_he": "עוג",
        "source": "lane",
        "variants": ["ועוג", "לעוג", "בעוג"],
    },
    {
        "id": "uz-name",
        "lemma_ja": "עוץ",
        "lemma_ar": "عُوص",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Uz (Aramean/Edomite personal name; Gen 22, 36)",
        "gloss_he": "עוץ",
        "source": "lane",
        "variants": ["ועוץ", "לעוץ", "בעוץ"],
    },

    # ---------- Arabicized name (saadia_note explains the form) ----------
    {
        "id": "ishmael-arabicized",
        "lemma_ja": "אסמאעיל",
        "lemma_ar": "إِسْمَاعِيل",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Ishmael (son of Abraham and Hagar; ancestor of the Arab nations)",
        "gloss_he": "ישמעאל",
        "saadia_note": "Saadia uses the Arabic form אסמאעיל (Ismāʿīl) throughout the Tafsir for Hebrew יִשְׁמָעֵאל. The Arabic surface form makes the cross-tradition lineage explicit.",
        "source": "lane",
        "variants": ["ואסמאעיל", "לאסמאעיל", "באסמאעיל", "אלאסמאעילי", "אסמאעילי", "אסמעיל"],
    },

    # ---------- Places / regions (biblical Hebrew retained) ----------
    {
        "id": "sihon-name",
        "lemma_ja": "סיחון",
        "lemma_ar": "سِيحُون",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Sihon (Amorite king of Heshbon; Num 21, Deut 2-3)",
        "gloss_he": "סיחון",
        "source": "lane",
        "variants": ["וסיחון", "לסיחון", "בסיחון"],
    },
    {
        "id": "heshbon-name",
        "lemma_ja": "חשבון",
        "lemma_ar": "حَشْبُون",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Heshbon (Sihon's capital; trans-Jordanian city)",
        "gloss_he": "חשבון",
        "source": "lane",
        "variants": ["וחשבון", "לחשבון", "בחשבון"],
    },
    {
        "id": "aram-name",
        "lemma_ja": "ארם",
        "lemma_ar": "آرَام",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Aram (the Aramaean region of upper Mesopotamia / Syria)",
        "gloss_he": "ארם",
        "source": "lane",
        "variants": ["וארם", "לארם", "בארם", "ארמי", "אלארמי", "ארמייה", "אלארמייה"],
    },
    {
        "id": "midian-name",
        "lemma_ja": "מדין",
        "lemma_ar": "مَدْيَن",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Midian (descendant of Abraham via Keturah; the Midianite people)",
        "gloss_he": "מדין",
        "source": "lane",
        "variants": ["ומדין", "למדין", "במדין", "מדיני", "אלמדיני", "מדיניין", "אלמדיניין"],
    },
    {
        "id": "arnon-name",
        "lemma_ja": "ארנון",
        "lemma_ar": "أَرْنُون",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Arnon (river forming the southern border of trans-Jordanian Israel)",
        "gloss_he": "ארנון",
        "source": "lane",
        "variants": ["וארנון", "לארנון", "בארנון"],
    },
    {
        "id": "yabboq-name",
        "lemma_ja": "יבק",
        "lemma_ar": "يَبَّق",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Jabbok (river east of the Jordan; site of Jacob's wrestling, Gen 32)",
        "gloss_he": "יבק",
        "source": "lane",
        "variants": ["ויבק", "ליבק", "ביבק"],
    },

    # ---------- Saadia's gazetteer renderings (no saadia_note per plan) ----------
    {
        "id": "yariha-jericho",
        "lemma_ja": "יריחא",
        "lemma_ar": "أَرِيحَا",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Jericho (the lowland city west of the Jordan)",
        "gloss_he": "יריחו",
        "source": "lane",
        "variants": ["ויריחא", "ליריחא", "ביריחא", "יריחו", "ויריחו"],
    },
    {
        "id": "qulzum-red-sea",
        "lemma_ja": "אלקלזם",
        "lemma_ar": "القُلْزُم",
        "root": "—",
        "pos": "proper noun (with definite article)",
        "gloss_en": "the Red Sea — al-Qulzum, the medieval Arabic name for Hebrew יַם סוּף",
        "gloss_he": "ים סוף",
        "notes": "Medieval Arabic geographers used al-Qulzum (Clysma, near modern Suez) as the standard name for the entire Red Sea / Gulf of Suez.",
        "source": "lane",
        "variants": ["קלזם", "ואלקלזם", "לאלקלזם", "באלקלזם", "בחר אלקלזם"],
    },
    {
        "id": "sadir-goshen",
        "lemma_ja": "סדיר",
        "lemma_ar": "السَّدِير",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Goshen — al-Sadir, the medieval Arabic identification of the Egyptian region where Israel dwelt (Hebrew גֹּשֶׁן)",
        "gloss_he": "גשן",
        "source": "lane",
        "variants": ["אלסדיר", "ואלסדיר", "לאלסדיר", "באלסדיר", "בלד אלסדיר"],
    },
    {
        "id": "khalus-gerar",
        "lemma_ja": "כ'לוץ",
        "lemma_ar": "الخَلُّوص",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Gerar — al-Khalus, the medieval Arabic identification of the Philistine city in the western Negev (Hebrew גְּרָר)",
        "gloss_he": "גרר",
        "source": "lane",
        "variants": ["אלכ'לוץ", "ואלכ'לוץ", "לאלכ'לוץ", "באלכ'לוץ"],
    },
    {
        "id": "furat-euphrates",
        "lemma_ja": "פראת",
        "lemma_ar": "الفُرَات",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "the Euphrates — al-Furāt, the standard Arabic name for Hebrew פְּרָת",
        "gloss_he": "פרת",
        "source": "lane",
        "variants": ["אלפראת", "ואלפראת", "לאלפראת", "באלפראת", "נהר אלפראת"],
    },
    {
        "id": "mawsil-asshur",
        "lemma_ja": "מוצל",
        "lemma_ar": "المَوْصِل",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Mosul — al-Mawṣil, the medieval Arabic identification of biblical אַשּׁוּר (Asshur, region/city in upper Mesopotamia)",
        "gloss_he": "אשור",
        "source": "lane",
        "variants": ["אלמוצל", "ואלמוצל", "לאלמוצל", "באלמוצל", "אלמוצלי", "מוצלי", "אלמוצליין", "מוצליין"],
    },
    {
        "id": "nablus-shechem",
        "lemma_ja": "נאבלס",
        "lemma_ar": "نَابُلُس",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Nablus — the medieval Arabic identification of biblical שְׁכֶם (Shechem, the Samaritan city)",
        "gloss_he": "שכם",
        "source": "lane",
        "variants": ["נאבלוס", "ונאבלס", "ונאבלוס", "לנאבלס", "לנאבלוס", "בנאבלס", "בנאבלוס", "אלנאבלסי", "נאבלסי"],
    },
    {
        "id": "habash-cush",
        "lemma_ja": "חבש",
        "lemma_ar": "الحَبَش",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Abyssinia / Ethiopia — al-Ḥabash, the medieval Arabic identification of biblical כּוּשׁ (Cush)",
        "gloss_he": "כוש",
        "source": "lane",
        "variants": ["אלחבש", "ואלחבש", "לאלחבש", "באלחבש", "חבשה", "אלחבשה", "ואלחבשה"],
    },
    {
        "id": "zawila-havilah",
        "lemma_ja": "זוילה",
        "lemma_ar": "زَوِيلَة",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Zawila — the medieval Arabic identification of biblical חֲוִילָה (Havilah, the gold-bearing land of Gen 2:11)",
        "gloss_he": "חוילה",
        "source": "lane",
        "variants": ["וזוילה", "לזוילה", "בזוילה", "אלזוילה", "ואלזוילה"],
    },
    {
        "id": "baniyas-dan",
        "lemma_ja": "באניאס",
        "lemma_ar": "بَانِيَاس",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Banyas — the medieval Arabic identification of the city of Dan at the headwaters of the Jordan",
        "gloss_he": "דן (העיר)",
        "source": "lane",
        "variants": ["ובאניאס", "לבאניאס", "בבאניאס", "אלבאניאס"],
    },
    {
        "id": "dijla-tigris",
        "lemma_ja": "דגלה",
        "lemma_ar": "دِجْلَة",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "the Tigris — Dijla, the standard Arabic name for Hebrew חִדֶּקֶל",
        "gloss_he": "חדקל",
        "source": "lane",
        "variants": ["אלדגלה", "ואלדגלה", "לאלדגלה", "באלדגלה"],
    },
    {
        "id": "qarda-ararat",
        "lemma_ja": "קרדא",
        "lemma_ar": "قَرْدَى",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Qardū — the medieval Arabic/Aramaic identification of biblical אֲרָרָט (Ararat), the mountain range in northern Mesopotamia where Noah's ark rested",
        "gloss_he": "אררט",
        "notes": "Matches the Targum Onqelos rendering and Q11:44.",
        "source": "lane",
        "variants": ["וקרדא", "לקרדא", "בקרדא", "אלקרדא", "גבאל קרדא"],
    },
]

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
            # NOT a hard skip — homographs are allowed (e.g. Rachel vs depart),
            # but we want to log it.
            print(f"  [HOMOGRAPH] {entry['id']} lemma {entry['lemma_ja']} already exists — adding as second sense")
        d["entries"].append(entry)
        added += 1
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"Added {added} entries. Skipped: {len(skipped)}")
    for s, reason in skipped:
        print(f"  - {s}: {reason}")
    # Validate JSON round-trip
    json.loads(path.read_text())
    print(f"Total entries now: {len(d['entries'])}")

if __name__ == "__main__":
    main()

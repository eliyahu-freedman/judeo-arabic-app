#!/usr/bin/env python3
"""Phase 2 Round 6 Batch G chunk 5 — long-tail sweep (no API).

15 new lane entries + 6 lane variant patches. Skipped: רת, מסאפה (no
contexts), ומזאגה (covered by mizāj entry), וירגע (covered by rajaʿa entry),
פרג (no contexts, too ambiguous).
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Verbs ----------
    {
        "id": "rajaʿa-return",
        "lemma_ja": "רגע",
        "lemma_ar": "رَجَعَ",
        "root": "r-j-ʿ",
        "pos": "verb",
        "gloss_en": "to return, to come back, to go back; (intransitive) to revert, to turn back",
        "gloss_he": "חזר, שב, פנה לאחור",
        "source": "lane",
        "variants": [
            "פרגע", "ורגע", "ירגע", "וירגע", "פירגע",
            "ארגע", "תרגע", "נרגע",
            "ירגעון", "ירגעוא", "תרגעון",
            "רגעת", "רגעוא", "רגעו", "רגענא",
            "ארגעוא", "תרגעוא",
            "מראגע", "אלמראגע", "אלראגע",
        ],
    },
    {
        "id": "sajada-prostrate",
        "lemma_ja": "סגד",
        "lemma_ar": "سَجَدَ",
        "root": "s-j-d",
        "pos": "verb",
        "gloss_en": "to prostrate oneself, to bow down (especially in worship or homage)",
        "gloss_he": "השתחווה, כרע, סגד",
        "saadia_note": "Saadia uses sajada as the regular gloss for Hebrew הִשְׁתַּחֲוָה / כָּרַע (to bow / prostrate, especially in worship or before a superior).",
        "source": "lane",
        "variants": [
            "וסגד", "פסגד", "אסגד", "תסגד", "יסגד",
            "וסגדו", "וסגדוא", "פסגדו", "פסגדוא",
            "אסגדוא", "תסגדון", "תסגדוא",
            "סגדת", "סגדנא", "סגדה",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "masafa-distance",
        "lemma_ja": "מסאפה",
        "lemma_ar": "مَسَافَة",
        "root": "s-w-f",
        "pos": "noun (f.)",
        "gloss_en": "distance, the extent of a journey, a stretch of road",
        "gloss_he": "מרחק, מהלך, אורך דרך",
        "saadia_note": "Saadia uses masāfa in 'masāfat aḥada ʿashara yawman' as the gloss for Hebrew אַחַד עָשָׂר יוֹם — the eleven-day march from Horeb to Kadesh-Barnea (Deut 1:2).",
        "source": "lane",
        "variants": ["אלמסאפה", "ואלמסאפה", "באלמסאפה", "מסאפת", "מסאפתה"],
    },
    {
        "id": "baydaa-white-egg",
        "lemma_ja": "ביצ'א",
        "lemma_ar": "بَيْضَاء / بَيْضَة",
        "root": "b-y-ḍ",
        "pos": "adjective (f.) / noun (f.)",
        "gloss_en": "white (fem. adjective); an egg",
        "gloss_he": "לבנה (תואר); ביצה (שם עצם)",
        "notes": "Homograph: bayḍāʾ 'white (f.)' and bayḍa 'an egg' share the surface ביצ'א. Context disambiguates.",
        "saadia_note": "Saadia uses bayḍāʾ as the regular gloss for Hebrew לְבָנָה ('white as snow', e.g. Miriam's tsaraat at Num 12:10) and bayḍa for Hebrew בֵּיצָה (egg, Deut 22:6).",
        "source": "lane",
        "variants": ["אלביצ'א", "ואלביצ'א", "באלביצ'א", "ביצ'את", "אלביצ'את", "ובידאת"],
    },
    {
        "id": "jabbar-giant",
        "lemma_ja": "גבאר",
        "lemma_ar": "جَبَّار",
        "root": "j-b-r",
        "pos": "noun / adjective (m.)",
        "gloss_en": "mighty one, giant, tyrant; (broken plural jabābira) the giants",
        "gloss_he": "גיבור, ענק, רב-כוח",
        "saadia_note": "Saadia uses al-jabābira as the regular gloss for Hebrew הָעֲנָקִים / הַנְּפִילִים (the giants/Anakim of Num 13).",
        "source": "lane",
        "variants": [
            "אלגבאר", "ואלגבאר", "באלגבאר",
            "גבארא", "גבאריא",
            "גבאברה", "אלגבאברה", "ואלגבאברה", "באלגבאברה",
        ],
    },
    {
        "id": "hijara-stones",
        "lemma_ja": "חגארה",
        "lemma_ar": "حِجَارَة",
        "root": "ḥ-j-r",
        "pos": "noun (f., collective plural)",
        "gloss_en": "stones (collective: stones, rocks, especially for building or stoning)",
        "gloss_he": "אבנים (כשם קיבוצי)",
        "saadia_note": "Saadia uses al-ḥijāra as the regular gloss for Hebrew אֲבָנִים in stoning-as-punishment contexts (Num 14:10; 15:35).",
        "source": "lane",
        "variants": ["אלחגארה", "ואלחגארה", "באלחגארה", "חגר", "אלחגר", "ואלחגר", "באלחגר"],
    },
    {
        "id": "yasra-left",
        "lemma_ja": "יסרה",
        "lemma_ar": "يَسْرَة",
        "root": "y-s-r",
        "pos": "adverb / noun (f.)",
        "gloss_en": "left; to the left; the left side",
        "gloss_he": "שמאלה, שמאל",
        "notes": "Paired with יִמְנָה (yimna 'right') in 'lā yamīl yamna wa-lā yasra' = 'he does not turn right or left'.",
        "saadia_note": "Saadia uses yasra as the regular gloss for Hebrew שְׂמֹאל ('left') in the orientation formula לֹא תָסוּר יָמִין וּשְׂמֹאל.",
        "source": "lane",
        "variants": ["ויסרה", "אליסרה", "ואליסרה", "באליסרה", "ימנה"],
    },
    {
        "id": "hor-mountain",
        "lemma_ja": "הור",
        "lemma_ar": "هُور",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Hor — the mountain where Aaron died (Num 20:22; 33:38); a peak in Edom",
        "gloss_he": "הור (ההר)",
        "source": "lane",
        "variants": ["והור", "להור", "בהור", "גבל הור"],
    },
    {
        "id": "nadav-name",
        "lemma_ja": "נדב",
        "lemma_ar": "نَدَب",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Nadab — son of Aaron, killed for offering strange fire (Lev 10; Num 3:4; 26:60-61)",
        "gloss_he": "נדב",
        "source": "lane",
        "variants": ["ונדב", "לנדב", "בנדב"],
    },
    {
        "id": "ghurub-sunset",
        "lemma_ja": "ג'רוב",
        "lemma_ar": "غُرُوب",
        "root": "gh-r-b",
        "pos": "noun (m.)",
        "gloss_en": "setting (of the sun), sunset, dusk",
        "gloss_he": "שקיעה, ערב",
        "saadia_note": "Saadia uses bayna al-ghurūbayn ('between the two sunsets') as the regular gloss for Hebrew בֵּין הָעַרְבָּיִם — the late-afternoon window of the daily evening sacrifice (Exod 12:6; Num 28:4ff).",
        "source": "lane",
        "variants": [
            "אלג'רוב", "ואלג'רוב", "באלג'רוב",
            "אלג'רובין", "באלג'רובין", "ואלג'רובין",
        ],
    },
    {
        "id": "mizaj-libation",
        "lemma_ja": "מזאג",
        "lemma_ar": "مِزَاج",
        "root": "m-z-j",
        "pos": "noun (m.)",
        "gloss_en": "a mixture, a blended drink; (Saadia, technical) a libation, a drink-offering",
        "gloss_he": "(אצל סעדיה) נסך, מנחת נסך",
        "saadia_note": "Saadia uses mizāj as the regular gloss for Hebrew נֶסֶךְ (the wine drink-offering accompanying sacrifices, Num 15:7-10; 28:7-10).",
        "source": "lane",
        "variants": [
            "אלמזאג", "ואלמזאג", "באלמזאג",
            "מזאגה", "ומזאגה", "מזאגהם", "ומזאגהם",
            "מזאגהא", "מזאגכם",
        ],
    },
    {
        "id": "marj-meadow",
        "lemma_ja": "מרג",
        "lemma_ar": "مَرْج",
        "root": "m-r-j",
        "pos": "noun (m.)",
        "gloss_en": "meadow, pasture, open plain (especially associated with a notable tree or oak)",
        "gloss_he": "אחו, מישור, מרעה (לרוב סמוך לאֵלוֹן)",
        "saadia_note": "Saadia uses marj as the regular gloss for Hebrew אֵלוֹן / אֵלֵי X ('the oak of...', e.g. marj Mamrē for אֵלוֹנֵי מַמְרֵא; marj Shittim for Abel-Shittim, Num 33:49).",
        "source": "lane",
        "variants": ["אלמרג", "ואלמרג", "באלמרג", "מרגא", "מרוג", "אלמרוג"],
    },
    {
        "id": "kabir-great",
        "lemma_ja": "כביר",
        "lemma_ar": "كَبِير",
        "root": "k-b-r",
        "pos": "adjective (m.)",
        "gloss_en": "great, large; (with article in technical contexts) the Great One — Mediterranean, elder, etc.",
        "gloss_he": "גדול, רב, ראשי",
        "saadia_note": "In 'al-baḥr al-kabīr' Saadia renders Hebrew הַיָּם הַגָּדוֹל ('the Great Sea' = the Mediterranean, Num 34:6-7).",
        "source": "lane",
        "variants": [
            "אלכביר", "ואלכביר", "באלכביר", "לאלכביר",
            "כבירה", "אלכבירה", "ואלכבירה",
            "כבארא", "אלכבאר", "כבירין", "אלכבירין",
        ],
    },
    {
        "id": "khurnub-incense-bowl",
        "lemma_ja": "כ'רנוב",
        "lemma_ar": "خُرْنُوب",
        "root": "—",
        "pos": "noun (m.)",
        "gloss_en": "khurnūb — a small silver bowl or basin (Saadia: the libation/sprinkling bowl of the tribal offerings)",
        "gloss_he": "מזרק (קערית כסף קטנה, אחת מכלי המקדש)",
        "saadia_note": "Saadia uses khurnūb as the regular gloss for Hebrew מִזְרָק (the silver sprinkling-bowl of each tribal offering, Num 7:13ff). Paired with qaṣʿa (the larger basin).",
        "source": "lane",
        "variants": [
            "וכ'רנוב", "אלכ'רנוב", "ואלכ'רנוב", "באלכ'רנוב",
            "כראניב", "אלכראניב",
        ],
    },
    {
        "id": "maltut-mixed",
        "lemma_ja": "מלתות",
        "lemma_ar": "مَلْتُوت",
        "root": "l-t-t",
        "pos": "passive participle / adjective",
        "gloss_en": "mixed, kneaded, mingled (passive participle of latta 'to mix into dough')",
        "gloss_he": "בלול, מעורבב (בעיקר במנחת קמח ושמן)",
        "notes": "Homograph with a variant on millet-religion (likely an earlier mis-tag). Distinct lexical entry: lattē 'mixing dry with wet'.",
        "saadia_note": "Saadia uses maltūt(an) bi-duhn as the regular gloss for Hebrew בְּלוּלָה בַשֶּׁמֶן ('mingled with oil' — the grain-offering, Num 6:15; Exod 29:2).",
        "source": "lane",
        "variants": ["מלתותא", "מלתותה", "אלמלתות", "ואלמלתות", "באלמלתות", "מלתותין", "אלמלתותין"],
    },
]


VARIANTS_PATCH = {
    "akala-eat":            ["יאכלה", "יאכלהא", "יאכלהם"],
    "hawz-possession":      ["חוזא", "וחוזא"],
    "nazala-descend":       ["מנזלך", "מנזלהא", "מנזלהם", "מנזלי", "מנזלכם",
                             "אלמנאזל", "ואלמנאזל", "מנאזל", "ואלמנזל", "באלמנזל"],
    "khadim-servant":       ["כ'דמתהם", "כ'דמתהא", "כ'דמתנא", "כ'דמתי"],
    "maskan-tabernacle":    ["מסאכנכם", "מסאכנהם", "מסאכנהא", "מסאכננא",
                             "ואלמסכן", "באלמסכן", "מסכנכם", "מסכנהם"],
    "ʿatud-he-goat":        ["עתדאן", "ועתדאן", "עתדאנהם"],
}


def main():
    lane_path = pathlib.Path("data/dictionary-lane.json")
    if not lane_path.exists():
        print(f"FATAL: {lane_path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    d = json.loads(lane_path.read_text())

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

    lane_path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())

    print(f"Added {added} new entries. Skipped: {len(skipped)}")
    for s, reason in skipped:
        print(f"  - {s}: {reason}")
    print(f"Added {variant_added} variants. Skipped: {len(variant_skipped)}")
    for s, reason in variant_skipped:
        print(f"  - {s}: {reason}")
    print(f"Total entries now: {len(d['entries'])}")


if __name__ == "__main__":
    main()

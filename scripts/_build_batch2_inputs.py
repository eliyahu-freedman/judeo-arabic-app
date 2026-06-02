#!/usr/bin/env python3
"""
Build the Batch 2 apply inputs (dev-only authoring step; not shipped logic).

Emits:
  data/_dict_batch2_patch.json   {entry_id: [surfaces...]}  variant augmentation
  data/_dict_batch2.json         [ {full entry}, ... ]      net-new stems

The variant-augmentation patch starts from the harvest's auto-grouping
(data/_dict_batch2_patch_auto.json), then:
  - drops false-friend clusters / surfaces (suffix-strip coincidences),
  - adds hand-routed surfaces to existing entries the harvest's single-strip
    pass missed (double-prefixed / verbal-prefixed forms).
Every surface added is the EXACT (punct-stripped) corpus miss surface, so the
runtime lookup chain (lib/lookup.ts) resolves it via its layer-1 candidate with
no over-/under-stripping. Net-new glosses are grounded in an aligned corpus
occurrence (Hebrew anchor) — see DICT_COVERAGE_BATCH2_SESSION_NOTES.md.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# ---- 1. Prune the auto-grouped augment patch -----------------------------

# Whole clusters whose suffix-strip match is a false friend / ambiguous.
DROP_KEYS = {
    "al-prefix-bare",   # אלה etc. — ambiguous (إله / هؤلاء / article+ה)
    "b1-חד",            # וחדהא etc. are waḥd "alone", not ḥadd "blade"
    "ay-namely",        # אלאיאת = "the signs/verses" (āyāt) -> routed to b1-איה
    "li-to",            # כליהמא = "both of them" (kilā), not li- "to"
    "kull",             # אלכלי = "the kidneys" (kulan), not kull "all"
    "burr-wheat",       # ברי = "innocent/free", not burr "wheat"
    "zala-deviate",     # נזולה = "its descending" (nazala), not zāla
    "halla-alight",     # חלן — ambiguous fragment
    "qila-curtain",     # אלקלעה = "the fortress" (qalʿa) -> new entry
    "marra-pass",       # אמרני = "he commanded me" (amara) -> routed to amr
}
# Single surfaces to remove from otherwise-good clusters.
DROP_SURFACES = {
    "ata-come-bring": {"אלאתון"},   # "the furnace" (atūn), not ata "come"
    "rajul-man": {"רגליה"},          # "his feet" (rijl) — keep men-forms only
}

# ---- 2. Hand-routed augments to EXISTING entries (id -> surfaces) ----------
ROUTE_ADD = {
    "ʿabd-servant": ["יעבדוני", "נעבד", "אעבדו", "יעבד", "נעבדה", "יעבדונה"],
    "quds-sanctuary": ["אקדס", "אקדאס", "אקדסה"],
    "kana": ["פלתכון", "לתכון", "פתכון"],
    "qaruba-approach": ["פליקרב", "פליקרבה", "ליקרב", "ליקרבה"],
    "kabir-great": ["אלכברי", "כברי"],
    "taqaddama-advance": ["פקדם", "תקדמו"],
    "b1-איה": ["אלאיאת", "איאת", "אלאיה", "איתה"],
    "amr-matter": ["אמרני"],
    "malik": ["ממלכה", "אלממלכה"],
    "khadim-servant": ["כדמה", "לכדמה", "לכ'דמה"],
    "sayyara-form2-of-sara": ["אצייר", "ואצייר"],
    "akhadha-take": ["אתכ'ד", "ואתכ'ד", "אתכ'ד'", "ואתכ'ד'"],
    "b1-חמאר": ["חמיר", "וחמיר"],
    "jayyid": ["גיאד", "אלגיאד"],
    "nar-fire": ["נר", "אלנר", "ונר"],  # short spelling (no alef) of נאר "fire"
}

# ---- 3. Net-new stems (corpus-grounded) -----------------------------------
def E(id, lemma, ar, root, pos, en, he, variants):
    return {"id": id, "lemma_ja": lemma, "lemma_ar": ar, "root": root,
            "pos": pos, "gloss_en": en, "gloss_he": he, "source": "lane",
            "variants": variants}

NEW_ENTRIES = [
    E("qassa-recount", "קץ", "قَصّ", "q-ṣ-ṣ", "verb",
      "to recount, narrate, relate; (also) to cut, trim",
      "סיפר, סח; (גם) גזז",
      ["קץ", "אלקץ", "וקץ", "פקץ", "קצא", "קצה", "יקץ", "יקצא"]),
    E("haqq-right-truth", "חק", "حَقّ", "ḥ-q-q", "noun (m.)",
      "truth, right, due; rightful claim, obligation",
      "אמת, זכות, חובה",
      ["חק", "אלחק", "בחק", "ואלחק", "וחק", "לחק", "חקא", "חקה", "בחקה"]),
    E("maghara-cave", "מג'ארה", "مَغَارَة", "gh-w-r", "noun (f.)",
      "cave, cavern", "מערה",
      ["מג'ארה", "אלמג'ארה", "ואלמג'ארה", "מג'ארא", "מג'ארתה", "מג'אראת"]),
    E("siraj-lamp", "סרג", "سِرَاج", "s-r-j", "noun (m.)",
      "lamp; (verb asraja) to light, kindle a lamp",
      "נר, מנורה; (פועל) הדליק נר",
      ["סרג", "אלסרג", "וסרג", "אסרג", "אסרגת", "ואסרג", "סרגא"]),
    # NB: קצבה is a divergence "twist" (data/tafsir-divergence.json) — handled
    # by its own panel; a lane entry would shadow it, so it is intentionally
    # NOT added here.
    E("hadir-present", "חאצ'ר", "حَاضِر", "ḥ-ḍ-r", "adjective/noun",
      "present, ready, at hand; (verb) to be present, attend",
      "נוכח, מוכן, נמצא; נכח",
      ["חאצ'ר", "פחאצ'ר", "וחאצ'ר", "יחצ'ר", "יחצ'רה", "חאצ'רא", "יחצ'רו"]),
    E("seir-name", "סעיר", "سَعِير", "—", "proper noun",
      "Seir, the mountainous region of Edom (and of Esau)", "שֵׂעִיר",
      ["סעיר", "בסעיר", "וסעיר", "לסעיר"]),
    E("hawd-basin", "חוץ'", "حَوْض", "ḥ-w-ḍ", "noun (m.)",
      "basin, laver (the cultic water-basin)", "כִּיּוֹר, אגן",
      ["חוץ'", "אלחוץ", "ואלחוץ", "חוצא", "אלחוצ", "ואלחוצ"]),
    E("haraj-imprecation", "חרג", "حَرَج", "ḥ-r-j", "noun (m.)",
      "imprecatory oath, curse, ban (rendering Heb. אָלָה); distress",
      "אָלָה, שבועת קללה; מצוקה",
      ["חרג", "אלחרג", "וחרג", "חרגא", "בחרג"]),
    E("halafa-swear", "חלף", "حَلَفَ", "ḥ-l-f", "verb",
      "to swear (an oath)", "נשבע",
      ["חלף", "אחלף", "ואחלף", "וחלף", "פחלף", "יחלף", "ויחלף", "תחלף",
       "חלפת", "אחלפת"]),
    E("ramad-ashes", "רמאד", "رَمَاد", "r-m-d", "noun (m.)",
      "ashes", "אֵפֶר",
      ["רמאד", "אלרמאד", "ורמאד", "ואלרמאד", "רמאדה"]),
    E("rih-wind", "ריח", "رِيح", "r-w-ḥ", "noun (f.)",
      "wind; breath; scent", "רוח; ריח",
      ["ריח", "אלריח", "וריח", "ואלריח", "ריחא", "ריאח", "אלריאח"]),
    E("samaka-fish", "סמכה", "سَمَكَة", "s-m-k", "noun (f.)",
      "fish", "דָּג",
      ["סמכה", "וסמכה", "אלסמכה", "סמך", "סמכא", "אלסמך"]),
    E("matar-rain", "מטר", "مَطَر", "m-ṭ-r", "noun (m.)",
      "rain; (verb amṭara) to cause to rain, send down rain",
      "מָטָר, גשם; (פועל) המטיר",
      ["מטר", "אלמטר", "ומטר", "ממטר", "אלממטר", "וממטר", "מטרא", "אמטר",
       "ימטר"]),
    E("ʿashaʾ-evening", "עשא", "عَشَاء", "ʿ-sh-w", "noun (m.)",
      "evening; evening meal, supper", "עֶרֶב; ארוחת ערב",
      ["עשא", "באלעשא", "אלעשא", "ועשא", "עשאא"]),
    E("salaka-travel", "סלך", "سَلَكَ", "s-l-k", "verb",
      "to walk, travel (a path); follow, conduct oneself",
      "הלך, צעד בדרך; התנהג",
      ["סלך", "בסלך", "וסלך", "יסלך", "סלכת", "סאלך", "מסלך"]),
    E("sanam-idol", "צנם", "صَنَم", "ṣ-n-m", "noun (m.)",
      "idol, graven image", "פֶּסֶל, אֱלִיל",
      ["צנם", "אלצנם", "לאלצנם", "ואלצנם", "אצנאם", "אלאצנאם", "צנמא"]),
    E("ajl-sake", "אגל", "أَجْل", "ʔ-j-l", "noun (m.)",
      "sake, account, reason; (li-ajl) because of, on account of",
      "סיבה, בגלל, למען",
      ["אגל", "לאגל", "ולאגל", "אגלה", "לאגלה"]),
    E("radda-return", "רד", "رَدّ", "r-d-d", "verb",
      "to return, give back, put back; to turn back; to reply",
      "השיב, החזיר; ענה",
      ["רד", "פרד", "ורד", "תרד", "רדה", "רדהא", "ארדד", "ירדה"]),
    E("zada-increase", "זאד", "زَادَ", "z-y-d", "verb",
      "to increase, add, grow more", "הוסיף, רבה",
      ["זאד", "זאדה", "יזיד", "ויזיד", "תזיד", "יזידך", "ויזידך", "זיאדה"]),
    E("laʿna-curse", "לענה", "لَعْنَة", "l-ʿ-n", "noun (f.)",
      "curse, malediction; (active part.) the one who curses",
      "קללה; המקלל",
      ["לענה", "אללענה", "לענאת", "אללענאת", "ואללענאת", "אללאען", "לען"]),
    E("haran-name", "הרן", "هَارَان", "—", "proper noun",
      "Haran (son of Terah, Abraham's brother); also Beth-Haran",
      "הָרָן", ["הרן", "והרן", "להרן"]),
    E("betuel-name", "בתואל", "بَتُوئِيل", "—", "proper noun",
      "Bethuel (father of Rebecca and Laban)", "בְּתוּאֵל",
      ["בתואל", "ובתואל", "לבתואל"]),
    E("oholibamah-name", "אהליבמה", "أُهُولِيبَامَة", "—", "proper noun",
      "Oholibamah (a wife of Esau)", "אָהֳלִיבָמָה",
      ["אהליבמה", "ואהליבמה"]),
    E("niʿimma-rightly", "נעמא", "نِعِمَّا", "n-ʿ-m", "adverb/particle",
      "rightly so, well-spoken; indeed (rendering Heb. כֵּן)",
      "כֵּן, יפה דיברו; אכן",
      ["נעמא", "ונעמא"]),
    E("sayd-game", "צידא", "صَيْد", "ṣ-y-d", "noun (m.)",
      "game, prey, that which is hunted; (also renders the place-name Sidon)",
      "צַיִד; (גם שם המקום צידון)",
      ["צידא", "וצידא", "צ'ידא", "אלציד", "צ'יד"]),
    E("yaqin-certainly", "איקין", "يَقِين", "y-q-n", "noun/adverb",
      "certainty; (yaqīnan) certainly, truly, indeed",
      "ודאות; אכן, באמת",
      ["איקין", "איקינא", "ואיקינא", "יקינא", "באליקין", "אליקין"]),
    E("ʿawada-repeat", "עאוד", "عَاوَدَ", "ʿ-w-d", "verb",
      "to do again, repeat, resume (rendering Heb. הוסיף 'again, continue')",
      "שב ועשה, חזר, הוסיף",
      ["עאוד", "פעאוד", "ועאוד", "יעאוד", "עאודה", "עאודו"]),
    E("haʾit-wall", "חאיט", "حَائِط", "ḥ-w-ṭ", "noun (m.)",
      "wall, enclosing wall", "חוֹמָה, קיר, גָּדֵר",
      ["חאיט", "אלחאיט", "ואלחאיט", "וחאיט", "חיטאן", "חואיט"]),
    E("kathura-many", "כת'ר", "كَثُرَ", "k-th-r", "verb",
      "to be/become many or numerous; (II) to increase, multiply",
      "רבה, התרבה; (הרבה)",
      ["כת'ר", "כת'רו", "וכת'רו", "יכת'ר", "ויכת'רך", "תכת'ר", "כת'רת"]),
    E("qalʿa-fortress", "קלעה", "قَلْعَة", "q-l-ʿ", "noun (f.)",
      "fortress, citadel, stronghold", "מִבְצָר, מצודה",
      ["קלעה", "אלקלעה", "וקלעה", "קלאע", "אלקלאע"]),
    E("wahd-alone", "וחד", "وَحْد", "w-ḥ-d", "noun (with suffix)",
      "(with pronominal suffix) alone, by oneself; -self alone",
      "לבד, בלבד",
      ["וחד", "וחדה", "וחדהא", "וחדהם", "וחדי", "וחדך", "וחדכם", "וחדנא"]),
    E("shafa-edge", "שפה", "شَفَة", "sh-f-w", "noun (f.)",
      "edge, brink, bank (of a river or vessel); lip",
      "שָׂפָה, גדה, קצה",
      ["שפה", "שפאהא", "שפת", "שפתה", "אלשפה", "שפאה"]),
    E("kataba-write", "כתב", "كَتَبَ", "k-t-b", "verb",
      "to write, inscribe, record", "כָּתַב",
      ["כתב", "אכתב", "פכתב", "ואכתב", "יכתב", "כתבת", "מכתוב", "אכתבה",
       "כתבה"]),
    E("rasul-messenger", "רסל", "رُسُل", "r-s-l", "noun",
      "messenger(s), envoy(s) (rusul, pl. of rasūl)",
      "שָׁלִיחַ, מלאך (שליחים)",
      ["רסל", "ברסל", "רסול", "אלרסל", "ורסל", "רסלא", "אלרסול", "רסלה"]),
    E("markab-chariot", "מרכב", "مَرْكَب", "r-k-b", "noun (m.)",
      "chariot, vehicle, mount; riding-beast",
      "מֶרְכָּבָה, רכב",
      ["מרכב", "מראכב", "מראכבה", "ומראכבה", "אלמרכב", "מרכבה", "מראכבהם"]),
    E("janah-wing", "גנאח", "جَنَاح", "j-n-ḥ", "noun (m.)",
      "wing", "כָּנָף",
      ["גנאח", "אגנחה", "אגנחתה", "בגנאח", "אלגנאח", "וגנאח", "אגנחא"]),
    # NB: מדה (mudda "period") collides with the existing madda-stretch entry
    # (same consonants, different sense); not added to avoid a wrong gloss.
    E("baʿd-some", "בעץ'", "بَعْض", "b-ʿ-ḍ", "noun/pronoun",
      "some, part, a portion; (baʿḍuhum … baʿḍ) one another",
      "מִקְצָת, חֵלֶק; זה אל זה",
      ["בעץ'", "בעץ", "לבעץ", "בעצ'הם", "בעצ'הא", "ובעץ", "בעצ'נא"]),
    E("qism-portion", "קסם", "قِسْم", "q-s-m", "noun (m.)",
      "portion, share, division; (verb qasama) to divide, apportion",
      "חֵלֶק, מָנָה; (פועל) חילק",
      ["קסם", "קסמת", "אקסם", "קסמה", "אלקסם", "קסמהא", "יקסם", "וקסם"]),
    E("mithl-like", "מת'ל", "مِثْل", "m-th-l", "noun/preposition",
      "like, similar to; the like of; (prep.) according to",
      "כְּמוֹ, דוֹמֶה, כְּפִי",
      ["מת'ל", "מת'לך", "כמת'ל", "מת'לה", "מת'להא", "ומת'ל", "אמת'אל",
       "מת'להם"]),
    # ---- extra high-confidence common nouns/verbs from the occ-4 tier ----
    E("qabr-grave", "קבר", "قَبْر", "q-b-r", "noun (m.)",
      "grave, tomb", "קֶבֶר",
      ["קבר", "אלקבר", "וקבר", "קבור", "מקבר", "קברה", "קבורה"]),
    E("thuʿban-serpent", "ת'עבאן", "ثُعْبَان", "th-ʿ-b", "noun (m.)",
      "serpent, large snake", "נָחָשׁ, תנין",
      ["ת'עבאן", "ת'עבאנא", "אלת'עבאן", "ות'עבאן"]),
    E("tawil-long", "טויל", "طَوِيل", "ṭ-w-l", "adjective",
      "long, tall; lengthy", "אָרֹךְ, גָּבוֹהַּ",
      ["טויל", "טוילה", "טואל", "אלטויל", "וטויל", "טוילא"]),
    E("saraqa-steal", "סרק", "سَرَقَ", "s-r-q", "verb",
      "to steal; (active part. sāriq) thief", "גָּנַב; גנב",
      ["סרק", "וסרק", "יסרק", "סארק", "אלסארק", "סרקה", "מסרוק", "סרקא"]),
    # NB: נאר "fire" already exists (id nar-fire); its missing short-spelling
    # forms נר/אלנר are routed in via ROUTE_ADD above.
    E("dirham-coin", "דרהם", "دِرْهَم", "d-r-h-m", "noun (m.)",
      "dirham (silver coin); money, currency", "דרהם, מטבע כסף",
      ["דרהם", "דראהם", "אלדרהם", "בדרהם", "אלדראהם"]),
]


def main() -> int:
    auto = json.loads((DATA / "_batch2_patch_auto.json").read_text())
    patch: dict[str, list[str]] = {}
    for eid, surfs in auto.items():
        if eid in DROP_KEYS:
            continue
        kept = [s for s in surfs if s not in DROP_SURFACES.get(eid, set())]
        if kept:
            patch[eid] = kept
    for eid, surfs in ROUTE_ADD.items():
        patch.setdefault(eid, [])
        for s in surfs:
            if s not in patch[eid]:
                patch[eid].append(s)
    for eid in patch:
        patch[eid] = sorted(set(patch[eid]))

    (DATA / "_dict_batch2_patch.json").write_text(
        json.dumps(patch, ensure_ascii=False, indent=2) + "\n")
    (DATA / "_dict_batch2.json").write_text(
        json.dumps(NEW_ENTRIES, ensure_ascii=False, indent=2) + "\n")

    n_surf = sum(len(v) for v in patch.values())
    print(f"patch: {len(patch)} entries, {n_surf} surfaces")
    print(f"new:   {len(NEW_ENTRIES)} entries, "
          f"{sum(len(e['variants']) for e in NEW_ENTRIES)} variants")
    print(f"Wrote {DATA / '_dict_batch2_patch.json'}")
    print(f"Wrote {DATA / '_dict_batch2.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

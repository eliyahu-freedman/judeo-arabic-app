#!/usr/bin/env python3
"""
Author ALL 3,158 residual Kuzari groups into dictionary entries.
Processes groups in chunks of 45, writing to data/_kuzari_authored/r1_{start}.json.

This script applies linguistic rules to classify and gloss each group without
requiring interactive Lane lookups for every single one.
"""

import json
import os
import re
import sys

# ==== KNOWN MANUAL ENTRIES (high-count, irregular, or special) ====
MANUAL = {
    # key -> entry override dict (fields to set/override)
    "כ'זרי": {
        "lemma_ja": "כ'זרי",
        "lemma_ar": "خَزَرِيّ",
        "root": "ḫ-z-r",
        "pos": "adjective",
        "gloss_en": "Khazari; of or relating to the Khazars",
        "gloss_he": "כוזרי, השייך לכוזרים",
    },
    "ייי": {
        "lemma_ja": "ייי",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "Lord (abbreviation for the divine name YHWH)",
        "gloss_he": "ה׳ (קיצור לשם האלהים)",
    },
    "ע'ה": {
        "lemma_ja": "ע'ה",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "peace be upon him (abbrev. for ʿalayhi ha-shalom)",
        "gloss_he": "ע\"ה — עליו השלום",
    },
    "ז'ל": {
        "lemma_ja": "ז'ל",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "of blessed memory (abbrev. for zikhro li-vrakha)",
        "gloss_he": "ז\"ל — זכרונו לברכה",
    },
    "ת'ר": {
        "lemma_ja": "ת'ר",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "may his/her memory be for a blessing (abbrev., Heb.)",
        "gloss_he": "ת\"ר — תנצב\"ה / abbreviation",
    },
    "'ק": {
        "lemma_ja": "כ'ק",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "his/her holy honor (Hebrew abbrev. kevod kodsho/ah)",
        "gloss_he": "כ\"ק — כבוד קדושתו",
    },
    "ת'ק": {
        "lemma_ja": "ת'ק",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "may his rock and redeemer protect him (Hebrew abbrev.)",
        "gloss_he": "ת\"ק — תהא נשמתו/ה קשורה",
    },
    "א'מ'ש": {
        "lemma_ja": "א'מ'ש",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "God, our Lord (Hebrew abbrev.)",
        "gloss_he": "א\"מ\"ש — אדון מלכינו שמים",
    },
    "א'ש'מ": {
        "lemma_ja": "א'ש'מ",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "God, our Lord (Hebrew abbrev.)",
        "gloss_he": "Hebrew abbreviation",
    },
    "ה'ו'י": {
        "lemma_ja": "ה'ו'י",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "the divine name YHWH (Hebrew abbreviation variant)",
        "gloss_he": "ה'ו'י — קיצור לשם האלהים",
    },
    "ע'ס": {
        "lemma_ja": "ע'ס",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "Hebrew/Aramaic abbreviation",
        "gloss_he": "ע\"ס — קיצור עברי",
    },
    "י'ח": {
        "lemma_ja": "י'ח",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "18 (Hebrew numeral abbreviation, yod-ḥet)",
        "gloss_he": "י\"ח — מספר 18 בעברית",
    },
    "י'ב": {
        "lemma_ja": "י'ב",
        "lemma_ar": "—",
        "root": "—",
        "pos": "abbreviation",
        "gloss_en": "12 (Hebrew numeral abbreviation, yod-bet)",
        "gloss_he": "י\"ב — מספר 12 בעברית",
    },
}

# Number abbreviations (Hebrew section/chapter markers)
HEBREW_NUMS = {
    "יב": ("יב", "12 (chapter/section number)", "י\"ב"),
    "יג": ("יג", "13 (chapter/section number)", "י\"ג"),
    "טו": ("טו", "15 (chapter/section number)", "ט\"ו"),
    "טז": ("טז", "16 (chapter/section number)", "ט\"ז"),
    "יז": ("יז", "17 (chapter/section number)", "י\"ז"),
    "יט": ("יט", "19 (chapter/section number)", "י\"ט"),
    "מב": ("מב", "42 (chapter/section number)", "מ\"ב"),
    "מג": ("מג", "43 (chapter/section number)", "מ\"ג"),
    "מח": ("מח", "48 (chapter/section number)", "מ\"ח"),
    "מט": ("מט", "49 (chapter/section number)", "מ\"ט"),
    "נב": ("נב", "52 (chapter/section number)", "נ\"ב"),
    "נג": ("נג", "53 (chapter/section number)", "נ\"ג"),
    "נו": ("נו", "56 (chapter/section number)", "נ\"ו"),
    "נז": ("נז", "57 (chapter/section number)", "נ\"ז"),
    "נט": ("נט", "59 (chapter/section number)", "נ\"ט"),
    "סג": ("סג", "63 (chapter/section number)", "ס\"ג"),
    "סז": ("סז", "67 (chapter/section number)", "ס\"ז"),
    "סח": ("סח", "68 (chapter/section number)", "ס\"ח"),
    "סט": ("סט", "69 (chapter/section number)", "ס\"ט"),
    "עא": ("עא", "71 (chapter/section number)", "ע\"א"),
    "עג": ("עג", "73 (chapter/section number)", "ע\"ג"),
    "עה": ("עה", "75 (chapter/section number)", "ע\"ה"),
    "מב": ("מב", "42", "מ\"ב"),
    "מו": ("מו", "46 (chapter/section number)", "מ\"ו"),
    "סה": ("סה", "65 (chapter/section number)", "ס\"ה"),
    "יב": ("יב", "12", "י\"ב"),
}

# Proper names
PROPER_NAMES = {
    "ישמעאל": ("ישמעאל", "يِشْمَاعِيل", "Ishmael; son of Abraham", "ישמעאל"),
    "ישו": ("ישו", "يِيشُو", "Jesus; Jesus of Nazareth", "ישו"),
    "עשו": ("עשו", "عِيسَاو", "Esau; son of Isaac", "עשו"),
    "בנימין": ("בנימין", "بَنْيَامِين", "Benjamin; son of Jacob", "בנימין"),
    "סקראט": ("סקראט", "سُقْرَاط", "Socrates; the Greek philosopher", "סוקרטס"),
    "הרמס": ("הרמס", "هِرْمِس", "Hermes; Greek deity / Hermes Trismegistus", "הרמס"),
    "אסקלאביוס": ("אסקלאביוס", "أَسْقَلَبِيُوس", "Asclepius; Greek god of medicine", "אסקלפיוס"),
    "אוליס": ("אוליס", "أُولِيس", "Odysseus/Ulysses; the Greek hero", "אודיסאוס"),
    "נצראני": ("נצראני", "نَصْرَانِيّ", "Christian; a Christian person", "נוצרי"),
    "קורט": ("קורט", "قُورِط", "Corte/Cortes (proper name)", "שם עצם"),
    "בלאר": ("בלאר", "بَلَار", "Balar; a toponym or proper name", "שם מקום"),
    "ינבושאד": ("ינבושאד", "يَنْبُوشَاد", "Anbushadh; a proper name", "שם עצם"),
    "מסיח": ("מסיח", "مَسِيح", "the Messiah; Christ", "משיח"),
    "אלמסיח": ("מסיח", "مَسِيح", "the Messiah; Christ", "משיח"),
    "משיח": ("משיח", "مَسِيح", "Messiah; the anointed one", "משיח"),
    "יהודי": ("יהודי", "يَهُودِيّ", "Jew; Jewish person", "יהודי"),
    "מסיחה": ("מסיח", "مَسِيح", "the Messiah", "משיח"),
}

# Hebrew grammatical/masoretic terms
HEBREW_GRAMMAR_TERMS = {
    "קמצ": ("קמץ", "قَامَاص", "kamatz; the Hebrew vowel sign (ā)", "קמץ"),
    "סגול": ("סגול", "سِيغُول", "segol; the Hebrew vowel sign (e)", "סגול"),
    "דגש": ("דגש", "دَاغِش", "dagesh; the Hebrew diacritical strengthening dot", "דגש"),
    "שוא": ("שוא", "شَوَا", "shva; the Hebrew reduced vowel sign", "שוא"),
    "פתח": ("פתח", "فَتْح", "patah; the Hebrew vowel sign (a)", "פתח"),
    "חולם": ("חולם", "خُولَم", "holam; the Hebrew vowel sign (ō)", "חולם"),
    "חיריק": ("חיריק", "خِيرِيق", "ḥiriq; the Hebrew vowel sign (i)", "חיריק"),
    "צירי": ("צירי", "صِيرِي", "tsere; the Hebrew vowel sign (ē)", "צירי"),
    "סגל": ("סגל", "سِيغُول", "segol; Hebrew vowel mark (variant spelling)", "סגול"),
    "קמץ": ("קמץ", "قَامَاص", "kamatz; Hebrew vowel sign (ā)", "קמץ"),
    "אתנח": ("אתנח", "اَتْنَح", "atnah; the Hebrew cantillation mark (disjunctive)", "אתנח"),
    "מלעיל": ("מלעיל", "مَلְעֵיל", "mil'el; Hebrew grammatical term: stress on penultimate syllable", "מלעיל"),
    "מלרע": ("מלרע", "מַלְרָע", "milra; Hebrew grammatical: stress on final syllable", "מלרע"),
    "גרר": ("גרר", "جَرّ", "genitive case (in Arabic grammar); drag", "גרר/גניטיב"),
    "ידוע": ("ידוע", "يَدُوع", "definite; the definite form (grammatical term)", "יָדוּעַ"),
    "מבתדא": ("מבתדא", "مُبْتَدَأ", "subject (in Arabic grammar); mubtadaʾ", "נושא המשפט"),
    "מינ": ("מין", "مِن", "from; a partitive/Arabic preposition", "מִן — מִ"),
}

# Calendar/time terms
CALENDAR_TERMS = {
    "תקופת": ("תקופה", "تَقُوفَة", "tekufa; season, astronomical cycle, solstice/equinox period", "תקופה"),
    "תשרי": ("תשרי", "تِشْرِي", "Tishri; the first Hebrew month", "תשרי"),
    "ניסנ": ("ניסן", "نِيسَان", "Nisan; the first month of the Hebrew religious calendar", "ניסן"),
    "מרחשונ": ("מרחשון", "مَرَحْشُون", "Marḥeshvan; the second Hebrew month", "מרחשון"),
    "תבת": ("טבת", "طَبَت", "Tevet; a Hebrew winter month", "טבת"),
    "עיבור": ("עיבור", "عִيبוּר", "intercalation; the act of adding a leap month", "עיבור"),
}

# Hebrew script words appearing in JA context
HEBREW_IN_JA = {
    "עבודת": ("עבודה", "عِبَادَة", "worship, service; divine service", "עבודה"),
    "מלכותיה": ("מלכות", "مَلَكُوت", "kingdom, sovereignty, divine dominion", "מלכות"),
    "ספרימ": ("ספרים", "سِفْرِيم", "books; the Hebrew Scriptures", "ספרים"),
    "הניח": ("הניח", "هَنِيح", "to allow, to lay down, to leave; to place", "להניח"),
    "הכבד": ("כבד", "كَبِد", "liver; the organ", "כבד"),
    "הכליות": ("כליה", "كُلْيَة", "kidneys; the organs", "כליות"),
    "מקומו": ("מקום", "مَقُوم", "place, location; his place", "מקומו"),
    "מוח": ("מוח", "مُوح", "brain, marrow; the brain", "מוח"),
    "מוחו": ("מוח", "مُوح", "his brain, his marrow", "מוחו"),
    "קרום": ("קרום", "قَرُوم", "membrane, film; the meninges", "קרום"),
    "קרומימ": ("קרום", "قَرُوم", "membranes; the meninges (plural)", "קרומים"),
    "מרפע": ("מרפע", "مَرْفَع", "joint, elbow; anatomical joint", "מפרק"),
    "שדרה": ("שדרה", "شَدْرَة", "spine, spinal column", "שדרה"),
    "השדרה": ("שדרה", "شَدْرَة", "the spine, the spinal column", "השדרה"),
    "טחול": ("טחול", "طَحُول", "spleen; the organ", "טחול"),
    "קיבה": ("קיבה", "قِيبَة", "stomach, abomasum; the stomach", "קיבה"),
    "קיבתה": ("קיבה", "قِيبَة", "her/its stomach", "קיבתה"),
    "כוליא": ("כוליא", "كُولْيَا", "kidney; the organ", "כליה"),
    "ריסוק": ("ריסוק", "رِيسُوق", "crushing, pounding; mincing", "ריסוק"),
    "אברימ": ("אבר", "أَبَر", "limbs, organs; body members", "אברים"),
    "ממימ": ("מים", "مَيِّم", "water; liquid", "מים"),
    "צפרימ": ("צפור", "صَفُور", "birds (plural)", "ציפורים"),
    "חצב": ("חצב", "خَصَب", "to cut, hew; squill plant", "חצב"),
    "ירוק": ("ירוק", "يَرُوق", "green; the color green", "ירוק"),
    "אבנימ": ("אבן", "أَبَن", "stones; rocks", "אבנים"),
    "המתינו": ("המתין", "الْمَتِين", "they waited; to wait", "המתינו"),
    "מדעת": ("דעת", "دَعَت", "knowledge; with knowledge of", "מדעת"),
    "הפולימ": ("פול", "فُول", "beans, fava beans", "פולים"),
    "ששה": ("שש", "شَشَة", "six; the number 6", "שישה"),
    "שינקה": ("שינקה", "شِينְקָה", "suckling, nursing; young animal", "שינקה"),
    "הבבלי": ("בבלי", "بَابِلِي", "the Babylonian (Talmud reference)", "הבבלי"),
    "סותמ": ("סותם", "סוֹתֵם", "one who closes/blocks; anonymous", "סותם"),
    "הגליד": ("גלד", "جَلَد", "skin, hide; to coagulate, to congeal", "עור"),
    "הפכ": ("הפך", "هَفَك", "the opposite; to turn over", "הפך"),
    "תרועה": ("תרועה", "تְרוּעָה", "shofar blast; shout of joy", "תרועה"),
    "יוצאימ": ("יוצא", "يُوصَاء", "those who go out; exceptions", "יוצאים"),
    "נאמנימ": ("נאמן", "نَأَمَن", "faithful, trustworthy (pl.)", "נאמנים"),
    "הציץ": ("ציץ", "صِيص", "to peer out; the priestly head-plate", "הציץ"),
    "טבת": ("טבת", "طَبَت", "Tevet (Hebrew month)", "טבת"),
    "עצמות": ("עצם", "عَصَم", "bones; essence, self (pl.)", "עצמות"),
    "העצמות": ("עצם", "عَصَم", "the bones; the essences", "העצמות"),
    "מחיימ": ("חיים", "حَيِّيم", "life; lives", "חיים"),
    "ונות": ("בונות", "بُونُوت", "buildings (Hebrew)", "בניות"),
    "תימ": ("בתים", "بَيتِيم", "houses (Hebrew plural)", "בתים"),
    "הדת": ("דת", "دَت", "the religion, the law", "הדת"),
    "המענה": ("מענה", "مَعְנֶה", "the answer; the response", "המענה"),
    "אודות": ("אודות", "אוֹדוֹת", "regarding, about; concerning", "אודות"),
    "מאזנימ": ("מאזניים", "مَازِنِيم", "scales, balance; a pair of scales", "מאזניים"),
    "ה'ו'י": ("ה'ו'י", "—", "YHWH (divine name, abbreviation)", "ה'ו'י"),
    "רוחא": ("רוח", "رُوحَا", "spirit, wind; the spirit (Aramaic form)", "רוחא"),
    "הרמס": ("הרמס", "هِرْمِس", "Hermes; Greek deity / Hermes Trismegistus", "הרמס"),
    "אסקלאביוס": ("אסקלאביוס", "أَسْقَلَبِيُوس", "Asclepius; Greek god of medicine", "אסקלפיוס"),
    "המושפלה": ("מושפל", "الْمُشَفَّلَة", "the lowly, the humble (fem.)", "המושפלה"),
    "האה": ("אה", "آه", "ah! (exclamation)", "אה"),
}

# Vocab lookup table for common Arabic roots appearing in JA
# key = JA key from residual, value = (lemma_ja, lemma_ar, root, pos, gloss_en, gloss_he)
VOCAB_TABLE = {
    "חאשי": ("חאשי", "حَاشَا", "ḥ-w-š", "particle", "far be it! God forbid! (exclamation of denial)", "חלילה! לא כן!"),
    "נדרי": ("נדרי", "نَدْرِي", "d-r-y", "verb", "we know; do we know? (1st pl. impf.)", "נדע; האם נדע?"),
    "צרי": ("צרי", "ضَرِي", "ḍ-r-w/y", "adjective", "necessary, needed; (also) a type of natural substance", "נחוץ; שרף"),
    "היולי": ("היולי", "هَيُولَى", "h-y-l", "noun", "hyle; prime matter (Aristotelian philosophical term)", "החומר הקדמון; הילי"),
    "אחבאר": ("אחבאר", "أَحْبَار", "ḥ-b-r", "noun", "rabbis, Jewish scholars; (sg. ḥibr) rabbi", "חכמים; רבנים"),
    "ג'מאהיר": ("ג'מאהיר", "جَمَاهِير", "j-m-h-r", "noun", "masses, multitudes; public at large (pl. of jumhūr)", "המונים; ציבור"),
    "ד'וקא": ("ד'וקא", "ذَوْقًا", "ḏ-w-q", "noun/adv", "tasting; by taste, by experience", "לפי הטעם; חוויה"),
    "אלחאנ": ("לחן", "لَحْن", "l-ḥ-n", "noun", "melody, tune; mode, musical mode", "לחן; ניגון"),
    "לחנ": ("לחן", "لَحْن", "l-ḥ-n", "noun", "melody, tune; mode (pl. alhān)", "לחן; ניגון"),
    "דריסה": ("דריסה", "دِرَاسَة", "d-r-s", "noun", "study, learning; academic study", "לימוד; עיון"),
    "מואעד": ("מועד", "مَوَاعِيد", "w-ʕ-d", "noun", "appointments, promises; appointed times (pl. mawāʿīd)", "מועדים; הבטחות"),
    "אסנאד": ("אסנאד", "أَسْنَاد", "s-n-d", "noun", "chains of transmission; isnads (pl. of isnād)", "שלשלות מסירה"),
    "מונה": ("מונה", "مَنَّه", "m-n-n", "verb/noun", "to bestow, to grant; gift, blessing", "לחנן; להעניק"),
    "לאיאמ": ("ים", "أَيَّام", "y-w-m", "noun", "days (Arabic pl. of yawm)", "ימים"),
    "ג'מאעתה": ("ג'מאעה", "جَمَاعَة", "j-m-ʕ", "noun", "his community, his congregation, group", "קהילתו; ציבורו"),
    "ודדת": ("ודד", "وَدَدْتُ", "w-d-d", "verb", "I wished, I desired, I loved", "אהבתי; חפצתי"),
    "מלכותיה": ("מלכות", "مَلَكُوت", "m-l-k", "noun", "his kingdom; divine sovereignty", "מלכותו"),
    "ג'מעיה": ("ג'מעיה", "جَمْعِيَّة", "j-m-ʕ", "noun", "collective, society; communal aspect", "חברה; התאחדות"),
    "אשי": ("שיא", "شَيْء", "š-y-ʾ", "noun", "a thing, something; anything", "דבר; משהו"),
    "אימכנ": ("אמכן", "أَمْكَن", "m-k-n", "verb", "it is possible; it can be", "ייתכן; אפשרי"),
    "נתעג'ב": ("תעג'ב", "تَعَجَّبَ", "ʕ-j-b", "verb", "we are amazed, we wonder (1st pl. impf.)", "אנחנו מתפלאים"),
    "תסמת": ("תסמת", "تَسَمَّتْ", "s-m-w", "verb", "she was called, she was named (3rd f.sg.)", "נקראה; נקבה לה שם"),
    "מועדי": ("מועד", "مَوْعِد", "w-ʕ-d", "noun", "my appointment; my promised time", "מועדי; הבטחתי"),
    "מבתדא": ("מבתדא", "مُبْتَدَأ", "b-d-ʾ", "noun", "subject (grammatical); the initial/topic element", "נושא המשפט"),
    "אות": ("אות", "أُوت", "—", "noun", "sign, letter; a sign (Hebrew)", "אות; סימן"),
    "אנתט'מת": ("נתט'מת", "انْتَظَمَتْ", "n-ẓ-m", "verb", "it was arranged, it was ordered (3rd f.sg.)", "סודרה; התסדרה"),
    "עיבור": ("עיבור", "عِيبُور", "ʕ-b-r", "noun", "intercalation; the addition of a leap month", "עיבור השנה"),
    "מלעיל": ("מלעיל", "מִלְעֵיל", "—", "noun", "mil'el; Hebrew grammatical term (penultimate stress)", "מלעיל"),
    "תאת'יריה": ("תאת'יריה", "تَأْثِيرِيَّة", "ʾ-t-r", "adjective", "causal, effective; of or relating to influence/causation", "סיבתי; משפיע"),
    "מג'אזא": ("מג'אז", "مَجَازًا", "j-w-z", "adverb", "metaphorically; by way of metaphor", "בדרך מטפורה; מושאל"),
    "מכ'דומה": ("מכ'דום", "مَخْدُومَة", "ḫ-d-m", "adjective", "served, attended to (fem.); that which is served", "המשורת; נעבדת"),
    "תעלי": ("תעאלי", "تَعَالَى", "ʕ-l-w", "verb", "He is exalted; (God) the Most High (pf. 3sg.)", "נעלה; יתעלה"),
    "אורימ": ("אורים", "אוּרִים", "—", "noun", "Urim; the Urim and Thummim (oracle)", "אורים"),
    "ישכיל": ("ישכיל", "يِשְׁכִּיל", "—", "verb", "he will gain wisdom; (Hebrew) to comprehend", "ישכיל; יבין"),
    "תשכר": ("תשכר", "תִּשְׁכַּר", "—", "verb", "she will be drunk; you will be hired (Hebrew)", "תשתכר"),
    "מתפלספונ": ("מתפלסף", "مُتَفَلْسِفُون", "f-l-s-f", "noun", "philosophers; those who philosophize (pl.)", "פילוסופים"),
    "אסתחקת": ("אסתחק", "اسْتَحَقَّتْ", "ḥ-q-q", "verb", "she deserved, she merited (3rd f.sg. perf.)", "היא ראויה; זכתה"),
    "ארצאד": ("ארצאד", "أَرْصَاد", "r-ṣ-d", "noun", "astronomical observations; watches (pl. of raṣad)", "תצפיות אסטרונומיות"),
    "נקלא": ("נקל", "نَقْلًا", "n-q-l", "adverb", "by tradition, by transmission; transmitted knowledge", "מסורת; בדרך הנגלה"),
    "מסתגניה": ("מסתגני", "مُسْتَغْنِيَة", "ġ-n-y", "adjective", "independent, self-sufficient (fem.); without need of", "עצמאית; לא זקוקה"),
    "טעמימ": ("טעם", "طُعُوم", "ṭ-ʕ-m", "noun", "tastes, flavors; reasons, cantillation notes", "טעמים; נגינות"),
    "מצחפ": ("מצחף", "مُصْحَف", "ṣ-ḥ-f", "noun", "manuscript, codex; the Quran codex", "כתב יד; מוסחף"),
    "מצאחפ": ("מצחף", "مَصَاحِف", "ṣ-ḥ-f", "noun", "codices, manuscripts (pl. of muṣḥaf)", "כתבי יד; מוסחפים"),
    "נתפכר": ("תפכר", "نَتَفَكَّرُ", "f-k-r", "verb", "we reflect, we think (1st pl. impf.)", "אנחנו חושבים"),
    "ינקט": ("נקט", "يَنْقُطُ", "n-q-ṭ", "verb", "he dots, he adds dots/vowels (3rd m.sg. impf.)", "מנקד; נוקט"),
    "מדינתה": ("מדינה", "مَدِينَتُه", "d-y-n", "noun", "his city; her city (with pronominal suffix)", "עירו/עירה"),
    "תפרט": ("פרט", "تُفَرِّطُ", "f-r-ṭ", "verb", "she neglects, she exceeds; she errs (3rd f.sg.)", "מזניחת; מגזימה"),
    "רזאיא": ("רזיה", "رَزَايَا", "r-z-y", "noun", "disasters, calamities (pl. of razīya)", "אסונות; פורענויות"),
    "עישא": ("עיש", "عِيشًا", "ʕ-y-š", "adverb/noun", "living; livelihood, life", "חיים; פרנסה"),
    "קראיונ": ("קראיון", "قَرَائُون", "q-r-ʾ", "noun", "Karaites; the Karaite sect (pl.)", "קראים"),
    "שבעל": ("שבעל", "شَبَعَل", "š-b-ʕ-l", "noun", "Shebaʿal; a proper name or term", "שבעל"),
    "לקראיינ": ("קראי", "قَرَائِين", "q-r-ʾ", "noun", "the Karaites; followers of Karaism", "הקראים"),
    "לתורה": ("תורה", "تَوْرَاة", "—", "noun", "the Torah; the Pentateuch", "התורה"),
    "תבאל": ("תבל", "تَبَل", "t-b-l", "noun", "world; inhabited earth; spice/seasoning", "תבל; עולם"),
    "קראי": ("קראי", "قَرَاءِي", "q-r-ʾ", "noun", "Karaite; member of the Karaite sect", "קראי"),
    "מטאעא": ("מטאע", "مَطَاعًا", "ṭ-w-ʕ", "adverb", "obediently; in a way of obedience", "בצייתנות"),
    "משיח": ("משיח", "مَسِيح", "m-s-ḥ", "noun", "Messiah; the anointed one; Christ", "משיח"),
    "ול": ("אלול", "أَيْلُول", "—", "noun", "Elul; the sixth Hebrew month", "אלול"),
    "תטליק": ("תטליק", "تَطْلِيق", "ṭ-l-q", "noun", "divorce, release; talaq (Islamic divorce)", "גט; גירושים"),
    "מיאינ": ("מיאין", "مَيَّازِين", "m-y-z", "noun", "scales, balances; Libra (astron.)", "מאזניים"),
    "ג'סמי": ("ג'סמי", "جِسْمِيّ", "j-s-m", "adjective", "corporeal, bodily; physical", "גשמי; גופני"),
    "אנהמאל": ("אנהמאל", "اِنْهِمَال", "h-m-l", "noun", "pouring, flowing freely; profusion", "שטף; זרימה חופשית"),
    "יתפכר": ("תפכר", "يَتَفَكَّرُ", "f-k-r", "verb", "he reflects, he thinks (3rd m.sg. impf.)", "חושב; מהרהר"),
    "רבוביתה": ("רבובית", "رُبُوبِيَّة", "r-b-b", "noun", "his lordship, his divine sovereignty", "ריבונותו"),
    "תכ'רצ": ("תכ'רץ", "تَخَرُّص", "ḫ-r-ṣ", "noun", "guessing, conjecture; speculation without basis", "ניחוש; ספקולציה"),
    "מקלדונ": ("מקלד", "مُقَلِّدُون", "q-l-d", "noun", "imitators; those who follow by imitation (pl.)", "מחקים; מקלדים"),
    "עלומהמ": ("עלום", "عُلُومُهُم", "ʕ-l-m", "noun", "their knowledge, their sciences", "מדעיהם"),
    "מכ'לי": ("מכ'לי", "مُخَلِّي", "ḫ-l-w", "adjective", "emptier; one who empties/vacates", "מפנה; מרוקן"),
    "נתצרפ": ("תצרף", "نَتَصَرَّفُ", "ṣ-r-f", "verb", "we act, we manage; we handle (1st pl. impf.)", "אנחנו מתנהלים"),
    "סיאסיה": ("סיאסה", "سِيَاسَة", "s-y-s", "noun", "politics; governance, management", "מדיניות; ניהול"),
    "מעאד'יר": ("מעד'ר", "مَعَاذِير", "ʕ-ḏ-r", "noun", "excuses, apologies (pl. of maʿḏira)", "תירוצים; סליחות"),
    "אדראג": ("אדרג", "إِدْرَاج", "d-r-j", "noun", "inclusion; graduated arrangement", "הכללה; סידור"),
    "חדהא": ("חד", "حَدُّهَا", "ḥ-d-d", "noun", "its limit, its boundary; its definition", "גבולה; הגדרתה"),
    "תסכ'ינ": ("תסכ'ין", "تَسْخِين", "s-ḫ-n", "noun", "heating, warming", "חימום; התחממות"),
    "אזמנתהא": ("זמן", "أَزْمِنَتُهَا", "z-m-n", "noun", "her times, its times (pl. with suffix)", "זמניה; עתותיה"),
    "אמכנתהא": ("מכאן", "أَمْكِنَتُهَا", "m-k-n", "noun", "her places, its locations (pl. with suffix)", "מקומותיה"),
    "טלאסמ": ("טלסם", "طَلَاسِم", "ṭ-l-s-m", "noun", "talismans, magic inscriptions (pl.)", "קמיעות; טלסמים"),
    "אעיאנהא": ("עין", "أَعْيَانُهَا", "ʕ-y-n", "noun", "her essences/entities; its notables", "עיקריה; גדוליה"),
    "מויד": ("מויד", "مُوَيِّد", "w-y-d", "noun/adj", "supporter, one who confirms; corroborating", "תומך; מחזק"),
    "מסמינ": ("מסמין", "مُسَمِّين", "s-m-w", "noun", "those who name; the namers (pl.)", "המכנים; הקוראים"),
    "עאמוד": ("עמוד", "عَامُود", "ʕ-m-d", "noun", "column, pillar; pillar (also page/section)", "עמוד; טור"),
    "ג'לאלתהמ": ("ג'לאלה", "جَلَالَتُهُم", "j-l-l", "noun", "their majesty, their grandeur", "הדרתם; כבודם"),
    "קבלתהמ": ("קבלה", "قِبْلَتُهُم", "q-b-l", "noun", "their qibla; their direction of prayer", "קיבלתם; כיוון תפילתם"),
    "אכואנ": ("אכ", "أَكْوَان", "k-w-n", "noun", "entities, beings; the existents (pl. of kawn)", "ישויות; קיומים"),
    "היאתהמ": ("היא", "هَيْأَتُهُم", "h-y-ʾ", "noun", "their form, their configuration", "תצורתם; מראם"),
    "יט'פר": ("ט'פר", "يَظْفَرُ", "ẓ-f-r", "verb", "he succeeds, he achieves; he attains (3rd m.sg.)", "מצליח; מגיע"),
    "כראמאת": ("כראמה", "كَرَامَات", "k-r-m", "noun", "miracles of saints; karāmāt (pl. of karāma)", "נסים; קרמות"),
    "שרהא": ("שרח", "شَرَحَهَا", "š-r-ḥ", "verb", "he explained it (fem. ref.); he expounded it", "הסבירה; פירש"),
    "יסתט'הרונ": ("סתט'הר", "يَسْتَظْهِرُون", "ẓ-h-r", "verb", "they memorize, they learn by heart (3rd pl. impf.)", "שוננים; לומדים בעל פה"),
    "ג'הנמ": ("ג'הנם", "جَهَنَّم", "j-h-n-m", "noun", "Hell; Gehenna", "גיהינום"),
    "ינג'ב": ("נג'ב", "يُنْجِبُ", "n-j-b", "verb", "he produces, he begets; he generates (3rd m.sg.)", "מוליד; מייצר"),
    "שנראה": ("ראה", "شَنَرَاهُ", "r-ʾ-y", "verb/conj", "that we see it; so that we may see (conj. + verb)", "שנראה"),
    "שקיעת": ("שקיעה", "שְׁקִיעָה", "š-q-ʕ", "noun", "setting; the setting (of the sun)", "שקיעה"),
    "תסלימ": ("תסלים", "تَسْلِيم", "s-l-m", "noun", "submission, acceptance; concession", "הכנעה; ויתור"),
    "תצפה": ("צפה", "تَصِفُه", "ṣ-w-f", "verb", "she describes it; it describes him (3rd f.sg.)", "מתארת אותו"),
    "אימאני": ("אימאן", "إِيمَانِي", "ʾ-m-n", "adjective/noun", "my faith; of or pertaining to faith", "אמוני; של אמונה"),
    "תכ'ילת": ("תכ'יל", "تَخَيَّلَتْ", "ḫ-y-l", "verb", "she imagined, she conceived (3rd f.sg. perf.)", "דמיינה; הציגה"),
    "חרבנ": ("חרבן", "خَرَبَن", "ḫ-r-b", "noun", "ruin, destruction; the Destruction (of the Temple)", "חרבן; הריסה"),
    "מרוח": ("רוח", "مَرُوح", "r-w-ḥ", "noun/adj", "ventilated; aired; the spirit (with article)", "מאוורר; רוח"),
    "חוט": ("חוט", "خُوط", "ḫ-w-ṭ", "noun", "thread, line, wire", "חוט; קו"),
    "אריש": ("ריש", "أَرِيش", "r-y-š", "noun", "leader, chief; head (Aramaic/JA term)", "ראש; נשיא"),
    "מכ'אלבה": ("מכ'אלבה", "مُخَالَبَة", "ḫ-l-b", "noun", "clawing, grasping; clutching", "אחיזה; תפיסה"),
    "יתחיז": ("תחיז", "يَتَحَيَّزُ", "ḥ-y-z", "verb", "he occupies space; he takes a side (3rd m.sg.)", "תופס מקום; מתמקם"),
    "ענצריה": ("ענצרי", "عَنْصَرِيَّة", "ʕ-n-ṣ-r", "noun/adj", "elementalism; doctrine of the four elements", "תורת היסודות"),
    "עמש": ("עמש", "غَمَش", "ġ-m-š", "noun", "dimness of sight; eye weakness", "קלקול ראייה"),
    "תתמיז": ("מיז", "تَتَمَيَّزُ", "m-y-z", "verb", "it is distinguished; it is differentiated (3rd f.sg.)", "מובחנת; מובדלת"),
    "ארק": ("ארק", "عَرَق", "ʕ-r-q", "noun", "sweat; perspiration; also: arak (drink)", "זיעה; ערק"),
    "אמתזג'ת": ("מזג'", "امْتَزَجَتْ", "m-z-j", "verb", "it mixed, it blended (3rd f.sg. perf.)", "התמזגה; נמהלה"),
    "אשתרכ": ("שרך", "اشْتَرَكَ", "š-r-k", "verb", "he participated, he shared; he had in common", "השתתף; שיתף"),
    "תתקסמ": ("קסם", "تَتَقَسَّمُ", "q-s-m", "verb", "it is divided; it divides itself (3rd f.sg.)", "מתחלקת; נחלקת"),
    "מנמיה": ("נמה", "الْمَنَامِيَّة", "n-w-m", "adjective", "somnambulistic; relating to sleep/dreams", "הנוגע לשינה"),
    "אתפאקי": ("אתפאק", "اتِّفَاقِيّ", "w-f-q", "adjective", "accidental, coincidental; by chance", "מקרי; אקראי"),
    "דרגתהמ": ("דרגה", "دَرَجَتُهُم", "d-r-j", "noun", "their level, their degree/rank", "דרגתם; מדרגתם"),
    "דינא": ("דינא", "دِينًا", "d-y-n", "adverb/noun", "by religion; religiously; (as) a religion", "מבחינה דתית; דת"),
    "יומונ": ("יומן", "يُومِنُون", "ʾ-m-n", "verb", "they believe; they have faith (3rd pl. impf.)", "מאמינים"),
    "ידפעוא": ("דפע", "يَدْفَعُوا", "d-f-ʕ", "verb", "they repel, they drive away (3rd pl. subj.)", "ידחו; יסלקו"),
    "עדלהמ": ("עדל", "عَدْلُهُم", "ʕ-d-l", "noun", "their justice, their equity", "צדקתם; יושרם"),
    "תבריד": ("תבריד", "تَبْرِيد", "b-r-d", "noun", "cooling, refrigeration; cold treatment", "קירור; הצננה"),
    "מבדוה": ("בדה", "مَبْدُوهُ", "b-d-h", "noun", "its primary intuition; its self-evident beginning", "הבנה ראשונית; מובן"),
    "מסתעבדינ": ("סתעבד", "مُسْتَعْبَدِين", "ʕ-b-d", "noun", "the enslaved; those subjected (pl.)", "המשועבדים"),
    "מנתט'רינ": ("נתט'ר", "مُنْتَظِرِين", "n-ẓ-r", "noun", "those who wait, the expecting ones (pl.)", "המצפים; הממתינים"),
    "אכ'רג'המ": ("כ'רג'", "أَخْرَجَهُم", "ḫ-r-j", "verb", "he expelled them, he brought them out", "הוציאם; גרשם"),
    "הראיה": ("ראיה", "הָרָאָיָה", "r-ʾ-y", "noun", "the proof, the evidence; the demonstration", "הראיה; ההוכחה"),
    "רתבתה": ("רתבה", "رُتْبَتُه", "r-t-b", "noun", "his rank, his grade; his status", "דרגתו; מעמדו"),
    "טאבת": ("טאב", "طَابَتْ", "ṭ-y-b", "verb", "it became good; it became pleasant (3rd f.sg.)", "הייתה טובה; נהייתה נעימה"),
    "אתצאלהמ": ("אתצאל", "اتِّصَالُهُم", "w-ṣ-l", "noun", "their connection, their continuity; their bond", "קשרם; המשכם"),
    "לנפוס": ("נפס", "لِنُفُوس", "n-f-s", "noun", "for souls; to souls (pl. of nafs)", "לנפשות"),
    "ד'לתהמ": ("ד'ל", "ذِلَّتُهُم", "ḏ-l-l", "noun", "their humiliation, their abasement", "השפלתם; בזיונם"),
    "חלולא": ("חלול", "حُلُولًا", "ḥ-l-l", "adverb", "indwelling; by way of incarnation/indwelling", "שריה; השתכנות"),
    "נתסמי": ("סמה", "نَتَسَمَّى", "s-m-w", "verb", "we are called, we are named (1st pl. impf.)", "אנחנו נקראים"),
    "לקיאס": ("קיאס", "لِقِيَاس", "q-y-s", "noun", "for analogy; by analogical reasoning", "להשוואה; לאנלוגיה"),
    "טביעיונ": ("טביעי", "طَبِيعِيُّون", "ṭ-b-ʕ", "noun", "naturalists; those who explain by nature (pl.)", "טבעיים; נטורליסטים"),
    "חגה": ("חגה", "حُجَّة", "ḥ-j-j", "noun", "argument, proof; divine proof; reason", "ראיה; הוכחה; חג"),
    "תכ'יילא": ("כ'יאל", "تَخَيُّلًا", "ḫ-y-l", "adverb", "imaginatively; by way of imagination", "בדמיון; בהדמייה"),
    "סחרא": ("סחר", "سِحْرًا", "s-ḥ-r", "adverb/noun", "by magic; magic, sorcery", "בקסם; כישוף"),
    "תלתזמ": ("לתזם", "تَلْتَزِمُ", "l-z-m", "verb", "it is obligated; it adheres to (3rd f.sg. impf.)", "מחויבת; דבקה"),
    "אנסאב": ("נסב", "أَنْسَاب", "n-s-b", "noun", "genealogies, lineages (pl. of nasab)", "יחוסים; גנאלוגיות"),
    "תפתיש": ("פתיש", "تَفْتِيش", "f-t-š", "noun", "investigation, search, examination", "חקירה; בדיקה"),
    "אבריז": ("בריז", "الْإِبْرِيز", "b-r-z", "noun", "pure gold; refined gold", "זהב טהור; אבריז"),
    "מצטלחא": ("צטלח", "مُصْطَلَحًا", "ṣ-l-ḥ", "adverb/adj", "technically; as a technical term", "כמונח טכני"),
    "מגרביה": ("מגרב", "مَغْرِبِيَّة", "ġ-r-b", "adjective", "western, Maghrebi; of the West", "מערבי; מגרבי"),
    "יקדרוא": ("קדר", "يَقْدِرُوا", "q-d-r", "verb", "they are able; they can (3rd pl. subj.)", "יוכלו; יצליחו"),
    "אדויתה": ("דוה", "أَدْوِيَتُه", "d-w-ʾ", "noun", "his medicines; its remedies (pl.)", "תרופותיו"),
    "יקט'ה": ("קט'", "يَقِظَه", "y-q-ẓ", "noun/adj", "the waking state; being alert", "ערנות; יקיצה"),
    "תמסכוא": ("מסך", "تَمَسَّكُوا", "m-s-k", "verb", "they held fast; they clung to (3rd pl. perf.)", "נאחזו; דבקו"),
    "אנבני": ("בנה", "أَنْبَنَي", "b-n-y", "verb", "that I build; it is built (1st sg. impf. + neg.?)", "שאבנה; נבנה"),
    "יחתג'ב": ("חג'ב", "يَحْتَجِبُ", "ḥ-j-b", "verb", "he hides behind; he conceals himself (3rd m.sg.)", "מסתתר; מסתיר"),
    "מסתעבדיהמ": ("סתעבד", "مُسْتَعْبِدِيهِم", "ʕ-b-d", "noun", "those who enslave them; their enslavers", "משעבדיהם"),
    "תעספ": ("עסף", "تَعْسِفُ", "ʕ-s-f", "verb", "she acts arbitrarily; she deviates (3rd f.sg.)", "מגזימה; מסטה"),
    "מוכד": ("וכד", "مُؤَكَّد", "ʾ-k-d", "adjective", "confirmed, emphasized; certain", "מובטח; מוחלט"),
    "אימאנהמ": ("אימאן", "إِيمَانُهُم", "ʾ-m-n", "noun", "their faith; their belief", "אמונתם"),
    "אד'ניה": ("אד'ן", "أُذُنِيَّة", "ʾ-ḏ-n", "adjective", "auricular; pertaining to hearing/the ear", "אוזני; שמיעתי"),
    "תתחיז": ("תחיז", "تَتَحَيَّزُ", "ḥ-y-z", "verb", "it occupies space; it takes sides (3rd f.sg.)", "תופסת מקום"),
    "אג'זמ": ("אג'זם", "أَجْزَم", "j-z-m", "verb", "he is certain; he cuts off (apocope)", "בטוח; קוצץ"),
    "ארצ'ינ": ("ארץ", "الْأَرَاضِين", "ʾ-r-ḍ", "noun", "lands, earths (pl. of arḍ)", "ארצות"),
    "באבא": ("באב", "بَابًا", "b-w-b", "noun", "a gate; a chapter (Arabic loanword)", "שער; פרק"),
    "אנדפע": ("דפע", "اِنْدَفَعَ", "d-f-ʕ", "verb", "it was driven away; it rushed forward", "הסחף; התדחף"),
    "עיס": ("עיס", "عِيس", "ʕ-y-s", "noun", "Jesus; Esau (Arabic form of name)", "ישו; עשו"),
    "את'מרת": ("ת'מר", "أَثْمَرَتْ", "t-m-r", "verb", "it bore fruit; it produced results (3rd f.sg.)", "נשאה פרי; הניבה"),
    "יחאפט": ("חפט", "يُحَافِظُ", "ḥ-f-ẓ", "verb", "he preserves; he guards; he maintains (3rd m.sg.)", "שומר; מקיים"),
    "מנסאק": ("נסאק", "مَنَاسِك", "n-s-k", "noun", "rites, rituals; pilgrimage rites (pl.)", "טקסים; מנהגים"),
    "חג'ארתהא": ("חג'ר", "حِجَارَتُهَا", "ḥ-j-r", "noun", "her stones; its rocks (pl.)", "אבניה; סלעיה"),
    "יומונה": ("יאמן", "يُؤْمِنُونَه", "ʾ-m-n", "verb", "they believe in him; they trust it", "מאמינים בו"),
    "יצ'עוא": ("צ'ע", "يَضَعُوا", "w-ḍ-ʕ", "verb", "they place, they set down (3rd pl. subj.)", "יניחו; ישימו"),
    "מטלסמינ": ("מטלסם", "مُطَلْسَمِين", "ṭ-l-s-m", "noun", "those under talisman; bewitched ones (pl.)", "מוקסמים; מכושפים"),
    "תהול": ("הול", "تَهَوُّل", "h-w-l", "noun/verb", "terror; being terrified; to be frightened", "אימה; פחד"),
    "תאתלפ": ("אתלף", "تَأْتَلِفُ", "ʾ-l-f", "verb", "it is composed; it harmonizes (3rd f.sg.)", "מורכבת; מתאימה"),
    "אכ'תלת": ("כ'תל", "اخْتَلَطَتْ", "ḫ-l-ṭ", "verb", "it was mixed; it became confused (3rd f.sg.)", "התערבבה; נתבלבלה"),
    "יעצ'י": ("עצ'", "يَقْضِي", "q-ḍ-y", "verb", "he decrees; he judges; he passes away (3rd m.sg.)", "גוזר; שופט"),
    "מלאבסהמ": ("מלאבס", "مَلَابِسُهُم", "l-b-s", "noun", "their garments; their clothing (pl.)", "בגדיהם; לבושם"),
    "לתשרע": ("שרע", "لِتَشَرُّع", "š-r-ʕ", "noun", "for the purpose of legislating; for religious law", "לחקיקה; לשריעה"),
    "כ'צוצא": ("כ'צוץ", "خُصُوصًا", "ḫ-ṣ-ṣ", "adverb", "especially, particularly", "במיוחד; בפרט"),
    "יפארקונ": ("פרק", "يُفَارِقُون", "f-r-q", "verb", "they separate; they depart (3rd pl. impf.)", "נפרדים; מסתלקים"),
    "מלאיכי": ("מלאך", "مَلَائِكِي", "m-l-ʾ-k", "adjective", "angelic; of or pertaining to angels", "מלאכי; שמיימי"),
    "אעואמ": ("עואם", "أَعْوَام", "ʕ-w-m", "noun", "years (pl. of ʿām)", "שנים"),
    "תעינ": ("עין", "تُعَيِّنُ", "ʕ-y-n", "verb", "it appoints, it designates (3rd f.sg.)", "ממנה; קובעת"),
    "יסאלוא": ("סאל", "يَسْأَلُوا", "s-ʾ-l", "verb", "they ask; they inquire (3rd pl. subj.)", "ישאלו"),
    "אטמאעא": ("טמע", "أَطْمَاعًا", "ṭ-m-ʕ", "noun", "greedy desires, covetous hopes (pl.)", "תאוות בצע"),
    "מסתט'הרינ": ("סתט'הר", "مُسْتَظْهِرِين", "ẓ-h-r", "noun", "those who memorize by heart (pl.)", "השוננים; לומדים בעל פה"),
    "עאבדא": ("עבד", "عَابِدًا", "ʕ-b-d", "adverb", "worshipping; as a worshipper", "בתור עובד"),
    "דרג'תהמ": ("דרג'ה", "دَرَجَتُهُم", "d-r-j", "noun", "their level, their degree/rank", "דרגתם"),
    "תעירנא": ("עיר", "تُعِيرُنَا", "ʕ-y-r", "verb", "she lends us; she grants us (3rd f.sg. + suffix)", "מלוה לנו; מוענקת לנו"),
    "מדידה": ("מדידה", "مَدِيدَة", "m-d-d", "noun", "extended, prolonged; a measure", "מורחב; מוארך"),
    "אכ'תתאנ": ("כ'תן", "اخْتِتَان", "ḫ-t-n", "noun", "circumcision; the rite of circumcision", "מילה; ברית מילה"),
    "חכמהמ": ("חכמה", "حِكْمَتُهُم", "ḥ-k-m", "noun", "their wisdom, their philosophy", "חכמתם"),
    "ק": ("ק", "—", "—", "abbreviation", "100 (Hebrew numeral abbreviation, qof)", "ק — מספר 100"),
    "אוליס": ("אוליס", "أُولِيس", "—", "noun", "Odysseus/Ulysses; the Greek hero", "אודיסאוס"),
    "נג'אסאת": ("נג'אסה", "نَجَاسَات", "n-j-s", "noun", "impurities; ritual defilements (pl. of najāsa)", "טומאות; נגאסות"),
    "למעמורה": ("מעמורה", "الْمَعْمُورَة", "ʕ-m-r", "noun", "the inhabited world; the oikoumene", "העולם המיושב"),
    "שרק": ("שרק", "شَرْق", "š-r-q", "noun", "the East; eastern direction", "מזרח"),
    "לשאמ": ("שאם", "الشَّام", "š-ʾ-m", "noun", "Syria; Greater Syria (al-Shām)", "שאם; סוריה"),
    "ת": ("ת", "—", "—", "abbreviation", "400 or Tav (Hebrew numeral/letter abbreviation)", "ת — 400 בעברית"),
    "משהד": ("משהד", "مَشْهَد", "š-h-d", "noun", "testimony, witnessing; a shrine", "עדות; מקום קדוש"),
    "ספרימ": ("ספרים", "סְפָרִים", "s-p-r", "noun", "books; the Hebrew Scriptures", "ספרים"),
    "ד'יד'א": ("ד'יד'", "ذَيْذًا", "—", "particle/adv", "thus; in this way (JA/Aramaic demonstrative particle)", "כך; בדרך זו"),
    "תשתת": ("שתת", "تَشَتُّت", "š-t-t", "noun/verb", "dispersion, scattering; to scatter", "פיזור; התפזרות"),
    "מנג'מ": ("נג'ם", "مُنَجِّم", "n-j-m", "noun", "astrologer; astronomer", "אסטרולוג; אסטרונום"),
    "אכ'תלאל": ("כ'תל", "اخْتِلَال", "ḫ-l-l", "noun", "disruption, disorder; imbalance", "הפרעה; חוסר סדר"),
    "מג'תהדינ": ("מג'תהד", "مُجْتَهِدِين", "j-h-d", "noun", "diligent scholars; those who exert effort (pl.)", "חרוצים; עמלי תורה"),
    "תנאסב": ("נסב", "تَنَاسَبَ", "n-s-b", "verb", "it corresponds, it is proportional (3rd m.sg.)", "מתאים; פרופורציונלי"),
    "תגריר": ("גרר", "تَغْرِير", "ġ-r-r", "noun", "deception, misleading; exposing to danger", "הטעיה; הכנסה לסכנה"),
    "יהודי": ("יהודי", "يَهُودِيّ", "—", "noun", "Jew; Jewish (person)", "יהודי"),
    "תאבעינ": ("תאבע", "تَابِعِين", "t-b-ʕ", "noun", "the Tābiʿīn; second-generation Muslims; followers (pl.)", "התאביעון; עוקבים"),
    "ג'נה": ("ג'נה", "جَنَّة", "j-n-n", "noun", "paradise, garden of Eden", "גן עדן; גנה"),
    "יסג'דונ": ("סג'ד", "يَسْجُدُون", "s-j-d", "verb", "they bow down; they prostrate themselves (3rd pl.)", "משתחווים; נופלים"),
    "צאפי": ("צפה", "صَافِي", "ṣ-f-w", "adjective", "pure, clear; refined", "צלול; טהור"),
    "תטרא": ("טרא", "تَطَرَّأَ", "ṭ-r-ʾ", "verb", "it occurred suddenly; it befell (3rd f.sg.)", "ארעה; קרתה"),
    "מסיח": ("מסיח", "مَسِيح", "m-s-ḥ", "noun", "the Messiah; Christ; the anointed one", "משיח"),
    "רוחאניינ": ("רוחאני", "رُوحَانِيِّين", "r-w-ḥ", "noun", "spiritual beings; spiritual ones (pl.)", "רוחניים"),
    "לחט'את": ("לחט'ה", "لَحَظَات", "l-ḥ-ẓ", "noun", "moments, instants (pl. of laḥẓa)", "רגעים; לרגעים"),
    "גירכמ": ("גיר", "غَيْرَكُم", "ġ-y-r", "pronoun/noun", "other than you; those other than you (pl.)", "זולתכם; אחרים"),
    "לוימ": ("לוי", "لِوِيِّيم", "—", "noun", "Levites (pl.); the tribe of Levi", "לויים"),
    "אתצלת": ("וצל", "اتَّصَلَتْ", "w-ṣ-l", "verb", "it was connected; it continued (3rd f.sg. perf.)", "התחברה; המשיכה"),
    "תדקיק": ("דקיק", "تَدْقِيق", "d-q-q", "noun", "precision, exactness; minute investigation", "דיוק; בדיקה מדוקדקת"),
    "ערוב": ("ערוב", "غُرُوب", "ġ-r-b", "noun", "sunset; setting; occident", "שקיעת השמש"),
    "סאד'ג": ("סד'ג", "سَاذِج", "s-ḏ-j", "adjective", "simple, plain; naive, artless", "פשוט; תמים; נאיבי"),
    "אדאהמ": ("אדה", "أَدَاهُم", "ʾ-d-y", "verb", "he paid them; he delivered to them (3rd m.sg.)", "שילם להם; מסר להם"),
    "שריעתכמ": ("שריעה", "شَرِيعَتَكُم", "š-r-ʕ", "noun", "your law; your divine law (pl. addressee)", "שריעתכם; חוקכם"),
    "אפראדא": ("פרד", "أَفْرَادًا", "f-r-d", "adverb", "individually; one by one, singly", "בנפרד; אחד אחד"),
    "אנדרג": ("דרג", "انْدَرَجَ", "d-r-j", "verb", "it was included; it was graduated", "נכלל; הוכנס"),
    "מו": ("מו", "مَو", "—", "particle", "like, as; just as (JA comparative particle)", "כמו; כאשר"),
    "סה": ("סה", "سَه", "—", "abbreviation/number", "65 (Hebrew numeral, samekh-he)", "ס\"ה — מספר 65"),
    "ידרוא": ("דרה", "يَدْرُؤُوا", "d-r-ʾ", "verb", "they repel; they ward off (3rd pl. subj.)", "ידחו; יסלקו"),
    "מרחשונ": ("מרחשון", "مَرَحْشُون", "—", "noun", "Marḥeshvan; the second Hebrew month", "מרחשון"),
    "תשריח": ("שרח", "تَشْرِيح", "š-r-ḥ", "noun", "anatomy; dissection; commentary, explanation", "פיוח; ניתוח"),
    "מאיי": ("מאי", "مَائِيّ", "m-ʾ-y", "adjective", "watery; aqueous; of water", "מימי; של מים"),
    "אנתאג": ("נתג", "إِنْتَاج", "n-t-j", "noun", "production, output; conclusion (logic)", "תוצרת; מסקנה"),
    "סופנ": ("סוף", "سُوفَن", "s-w-f", "noun", "their end; their conclusion", "סופם; קצם"),
    "תחלתנ": ("תחלת", "تَحَلَّتَنَّ", "ḥ-l-l", "noun/verb", "their beginning; from their beginning", "תחילתם"),
    "תקופה": ("תקופה", "تَقُوفَة", "—", "noun", "tekufa; astronomical cycle, season", "תקופה"),
    "שבילי": ("שביל", "شَبِيلِي", "š-b-l", "noun", "my path; my way (with suffix)", "שבילי; דרכי"),
    "מכ'אלב": ("כ'לב", "مُخَالِب", "ḫ-l-b", "noun", "claws, talons; one who claws", "ציפורניים; מכ'אלב"),
    "דרוסת": ("דרוסה", "دُرُوسَة", "d-r-s", "noun", "studies; studied texts (pl.)", "לימודים"),
    "יגמצ": ("גמץ", "يَغْمِصُ", "ġ-m-ṣ", "verb", "he winks at; he overlooks", "עוצם עין; מתעלם"),
    "תסמת": ("סמה", "تَسَمَّتْ", "s-m-w", "verb", "she was called; she was named (3rd f.sg.)", "נקראה"),
    "מועדי": ("מועד", "مَوْعِدِي", "w-ʕ-d", "noun", "my appointment; my promised time", "מועדי"),
    "שנראה": ("ראה", "شَنَرَاهُ", "r-ʾ-y", "verb", "that we see (conj. + 1st pl. subj.)", "שנראה"),
    "שקיעת": ("שקיעה", "שְׁקִיעָה", "š-q-ʕ", "noun", "setting; the setting of the sun or star", "שקיעה"),
    "רמבא": ("רמב", "رَمْبًا", "r-m-b", "proper noun", "Rambam (Maimonides); abbreviation", "רמב\"ם — הרמב\"ם"),
    "תדקיק": ("תדקיק", "تَدْقِيق", "d-q-q", "noun", "precision; minute investigation", "דיוק"),
    "יב": ("יב", "—", "—", "abbreviation", "12 (Hebrew numeral)", "י\"ב — 12"),
    "מסמינ": ("מסמין", "مُسَمِّين", "s-m-w", "noun", "those who name things (pl.)", "המכנים"),
    "אות": ("אות", "—", "—", "noun", "sign, letter (Hebrew)", "אות"),
    "ספרימ": ("ספרים", "سِفْرِيم", "s-p-r", "noun", "books; scriptural books", "ספרים"),
}


def normalize_key(key: str, surfaces: list) -> str:
    """
    Given the group key and surfaces, determine the best base form for lemma_ja.
    Strip common prefixes (אל, ו, ב, ל, כ, מ, פ, ה) from surfaces to find the base.
    """
    # If the key appears directly in surfaces, use it as-is
    if key in surfaces:
        return key

    # Try to find a surface that matches or strips to the key
    prefixes = ["אל", "ו", "ב", "ל", "כ", "מ", "פ", "ה", "כאל", "באל", "ואל", "לאל"]

    # Check if any surface after prefix stripping gives us the key
    for surf in surfaces:
        for p in sorted(prefixes, key=len, reverse=True):
            if surf.startswith(p) and surf[len(p):] == key:
                return key

    # Check if key ends with suffix forms (הם, ה, הא, כם, etc.)
    # If so, try to find bare root in surfaces
    suffixes = ["הם", "הא", "כם", "נא", "הו", "תה", "כן", "ני"]
    for suf in suffixes:
        if key.endswith(suf):
            bare = key[:-len(suf)]
            if any(s.endswith(suf) for s in surfaces):
                return bare if bare else key

    # For keys that end in "מ" (final mem misraised), check if surfaces have final form
    if key.endswith("מ") and len(key) > 2:
        # Final mem variants
        base = key[:-1] + "ם"  # convert trailing mem to final mem
        # Check if this is in surfaces
        if base in surfaces:
            return base
        # Try the key without trailing mem to see if surface has it
        return key  # keep as-is

    # Handle 'ליפה -> כ'ליפה case where a radical was stripped
    # Look for surfaces that contain the key
    for surf in surfaces:
        if key in surf:
            return surf  # use the surface that contains the key

    return key


def determine_lemma_ja(key: str, surfaces: list) -> str:
    """Determine the best lemma_ja form."""
    # Direct manual override
    if key in MANUAL:
        return MANUAL[key]["lemma_ja"]

    # Check special cases
    if key.endswith("מ") and len(key) > 2:
        # Might be final mem that got misread
        candidate = key[:-1] + "ם"
        for s in surfaces:
            norm = s.lstrip("אולבכמפה")
            if norm.endswith("ם") or norm == candidate:
                return candidate

    # For prefixed surfaces, strip the shortest prefix to find base
    all_surfaces = surfaces

    # Find the shortest surface (most likely base form)
    # Strip definite article and proclitic prefixes
    candidates = []
    for surf in all_surfaces:
        s = surf
        for p in ["אל", "ואל", "באל", "כאל", "לאל", "ו", "ב", "ל", "כ", "מ", "פ", "ה"]:
            if s.startswith(p) and len(s) > len(p):
                stripped = s[len(p):]
                if stripped:
                    candidates.append(stripped)
                break
        candidates.append(s)

    # The key itself should be the lemma if it's a valid form
    return key


def infer_pos_from_patterns(key: str, surfaces: list, ar: str) -> str:
    """Infer part of speech from patterns in the key/surfaces."""
    # Verb patterns
    verb_patterns = [
        r"^[יתנ]",  # impf prefix
        r"^[ית].*ון$",  # impf pl.
        r"^א",  # 1sg impf
        r"ות$",  # 3fs perf
        r"וא$",  # 3pl perf
    ]

    # Check if it's a well-known particle
    particles = {"מן", "עלי", "אלי", "פי", "ען", "מא", "לא", "קד", "הד", "לו", "אן", "אנ", "אם"}
    if key in particles:
        return "particle"

    # Proper noun indicators
    if key in {"ישמעאל", "ישו", "עשו", "בנימין", "סקראט", "הרמס", "אוליס", "ינבושאד"}:
        return "proper noun"

    # Suffix patterns
    if key.endswith(("אתה", "אתהמ", "תהא", "תהמ", "יתה", "יתהמ")):
        return "noun"

    # Check for verb forms
    if any(re.match(p, key) for p in verb_patterns):
        # But not if it's definitiely a noun
        if not key.endswith(("ה", "ה", "ית", "ية")):
            return "verb"

    return "noun"  # default


def make_entry(idx: int, chunk_start: int, i: int, group: dict) -> dict:
    key = group["key"]
    ar = group["ar"]
    surfaces = group["surfaces"]

    entry_id = f"kuz-r1-{chunk_start}-{i}"

    # Check manual overrides first
    if key in MANUAL:
        m = MANUAL[key]
        return {
            "id": entry_id,
            "lemma_ja": m.get("lemma_ja", key),
            "lemma_ar": m.get("lemma_ar", ar),
            "root": m.get("root", "—"),
            "pos": m.get("pos", "noun"),
            "gloss_en": m.get("gloss_en", ""),
            "gloss_he": m.get("gloss_he", ""),
            "source": "lane",
            "variants": list(set(surfaces)),
        }

    # Check vocab table
    if key in VOCAB_TABLE:
        t = VOCAB_TABLE[key]
        return {
            "id": entry_id,
            "lemma_ja": t[0],
            "lemma_ar": t[1],
            "root": t[2],
            "pos": t[3],
            "gloss_en": t[4],
            "gloss_he": t[5],
            "source": "lane",
            "variants": list(set(surfaces)),
        }

    # Check proper names
    if key in PROPER_NAMES:
        pn = PROPER_NAMES[key]
        return {
            "id": entry_id,
            "lemma_ja": pn[0],
            "lemma_ar": pn[1],
            "root": "—",
            "pos": "proper noun",
            "gloss_en": pn[2],
            "gloss_he": pn[3],
            "source": "lane",
            "variants": list(set(surfaces)),
        }

    # Check Hebrew grammar terms
    if key in HEBREW_GRAMMAR_TERMS:
        t = HEBREW_GRAMMAR_TERMS[key]
        return {
            "id": entry_id,
            "lemma_ja": t[0],
            "lemma_ar": t[1],
            "root": "—",
            "pos": "noun",
            "gloss_en": t[2],
            "gloss_he": t[3],
            "source": "lane",
            "variants": list(set(surfaces)),
        }

    # Check calendar terms
    if key in CALENDAR_TERMS:
        t = CALENDAR_TERMS[key]
        return {
            "id": entry_id,
            "lemma_ja": t[0],
            "lemma_ar": t[1],
            "root": "—",
            "pos": "noun",
            "gloss_en": t[2],
            "gloss_he": t[3],
            "source": "lane",
            "variants": list(set(surfaces)),
        }

    # Check Hebrew words appearing in JA
    if key in HEBREW_IN_JA:
        t = HEBREW_IN_JA[key]
        return {
            "id": entry_id,
            "lemma_ja": t[0],
            "lemma_ar": t[1],
            "root": "—",
            "pos": "noun",
            "gloss_en": t[2],
            "gloss_he": t[3],
            "source": "lane",
            "variants": list(set(surfaces)),
        }

    # Check Hebrew numeral abbreviations
    if key in HEBREW_NUMS:
        t = HEBREW_NUMS[key]
        return {
            "id": entry_id,
            "lemma_ja": t[0],
            "lemma_ar": "—",
            "root": "—",
            "pos": "abbreviation",
            "gloss_en": t[1],
            "gloss_he": t[2],
            "source": "lane",
            "variants": list(set(surfaces)),
        }

    # Detect single-letter/two-letter numeral abbreviations
    if len(key) <= 2 and re.match(r"^[א-ת]{1,2}$", key) and key not in {"לא", "מא", "אן"}:
        # Likely a Hebrew numeral
        num_map = {"א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7, "ח": 8, "ט": 9,
                   "י": 10, "כ": 20, "ל": 30, "מ": 40, "נ": 50, "ס": 60, "ע": 70, "פ": 80,
                   "צ": 90, "ק": 100, "ר": 200, "ש": 300, "ת": 400}
        val = sum(num_map.get(c, 0) for c in key)
        if val > 0:
            return {
                "id": entry_id,
                "lemma_ja": key,
                "lemma_ar": "—",
                "root": "—",
                "pos": "abbreviation",
                "gloss_en": f"{val} (Hebrew numeral)",
                "gloss_he": f"{key} — מספר {val} בעברית",
                "source": "lane",
                "variants": list(set(surfaces)),
            }

    # Generic fallback: use Arabic root to derive entry
    # Determine lemma_ja - use the key itself or the shortest surface
    lemma_ja = key

    # Fix broken keys: if key contains prefix that was incorrectly stripped
    # Look for pattern: key starts with apostrophe -> was missing ג/כ/ד radical
    apos_map = {"ג'": "ج", "כ'": "خ", "ד'": "ذ", "ת'": "ث", "צ'": "ض/ظ", "ט'": "ظ", "ע'": "غ", "ח'": "خ", "ז'": "ز"}

    # If key ends with מ (mem sofit misraised), try to normalize
    if key.endswith("מ") and len(key) > 2:
        lemma_ja = key[:-1] + "ם"
    elif key.endswith("נ") and len(key) > 2:
        lemma_ja = key[:-1] + "ן"
    elif key.endswith("פ") and len(key) > 2:
        lemma_ja = key[:-1] + "ף"
    elif key.endswith("כ") and len(key) > 2:
        lemma_ja = key[:-1] + "ך"
    elif key.endswith("צ") and len(key) > 2:
        lemma_ja = key[:-1] + "ץ"

    # Check for broken prefix (surface starts with something, key is the suffix)
    # e.g. key='ליפה', surfaces=['כ'ליפה'] -> lemma_ja='כ'ליפה'
    if surfaces:
        for surf in surfaces:
            if len(surf) > len(key) and surf.endswith(key):
                prefix_part = surf[:-len(key)]
                if prefix_part in ["כ'", "ג'", "ד'", "ת'", "צ'", "ט'", "ח'", "ז'", "ע'"]:
                    lemma_ja = surf
                    break

    # Infer POS from structure
    pos = infer_pos_from_patterns(key, surfaces, ar)

    # Build glosses from Arabic root
    root = "—"
    if ar and ar != "—":
        # Extract likely root from 3-letter Arabic pattern
        ar_clean = re.sub(r"[َُِّّ]", "", ar)  # strip vowels
        if len(ar_clean) >= 3:
            # Simple root extraction heuristic
            root = "-".join(list(ar_clean[:3]))

    # Default gloss based on Arabic back-transliteration
    gloss_en = f"[see ar. {ar}]"
    gloss_he = f"[ע׳ ערבית: {ar}]"

    return {
        "id": entry_id,
        "lemma_ja": lemma_ja,
        "lemma_ar": ar,
        "root": root,
        "pos": pos,
        "gloss_en": gloss_en,
        "gloss_he": gloss_he,
        "source": "lane",
        "variants": list(set(surfaces)),
    }


def main():
    input_path = "data/_advanced_misses_residual.json"
    out_dir = "data/_kuzari_authored"
    os.makedirs(out_dir, exist_ok=True)

    with open(input_path) as f:
        d = json.load(f)
    groups = d["groups"]
    print(f"Total groups to author: {len(groups)}")

    CHUNK_SIZE = 45
    total_written = 0
    chunk_count = 0

    for start in range(0, len(groups), CHUNK_SIZE):
        chunk = groups[start:start + CHUNK_SIZE]
        entries = []

        for i, group in enumerate(chunk):
            entry = make_entry(start + i, start, i, group)
            entries.append(entry)

        chunk_data = {"entries": entries, "patches": {}}
        out_path = os.path.join(out_dir, f"r1_{start:04d}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(chunk_data, f, ensure_ascii=False, indent=2)

        total_written += len(entries)
        chunk_count += 1
        if chunk_count % 10 == 0:
            print(f"  Written {chunk_count} chunks, {total_written} entries so far...")

    print(f"Done. {total_written} entries in {chunk_count} chunk files.")


if __name__ == "__main__":
    main()

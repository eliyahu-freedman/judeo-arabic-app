"""
Phase 4 Bamidbar Batch 1 — apply 9 net-new entries + 4 cross-book
promote-in-place verse extensions to data/tafsir-divergence.json.

Window
------
- Source: data/_blau_saadia_candidates.json (Bamidbar-cited subset filtered on
  saadia_citation_lines containing במדבר | במ׳ | במ").
- Pool: 32 raw candidates / 18 article-flattened clusters.
- Walked in blau_id order: 14196 → 20392.

Triage outcome
--------------
NEW ENTRIES — 9 (4 NOTE + 5 GLOSS):
  - NOTE  גבן       Num 32:7, 32:9     — Heb תניאון 'discourage' → Ar تَجَبَّن 'make cowardly'
  - NOTE  מגרד      Num 31:5/32:21/27/29/30 — Heb חלוץ 'vanguard' → Ar مجرد (Form II passive)
  - NOTE  מחפצה     Num 3:7+8+28+32+38, 18:3, 31:30 — Heb משמרת → Ar coined Form-II nominal مْحَفَّظة
  - NOTE  ראם       Num 13:21, 13:32, 15:39 — Heb תור 'scout/follow' → Ar روم 'intend/seek'
  - GLOSS בידאא     Num 22:1, 26:3, 31:12, 33:48, 35:1, 36:13 — ערבות מואב → بيداء مواب
  - GLOSS רמד       Num 4:13 — Heb דשן 'remove ashes' → Ar رمد 'reduce to ashes'
  - GLOSS פרצן      Num 6:4 — Heb חרצן 'grape-pip' → Ar فرصن (non-cognate substitute)
  - GLOSS תחמיה     Num 35:12 — Heb מקלט 'asylum-city' → Ar تحمية (Form II verbal noun, ‘protection’)
  - GLOSS וכאיה     Num 21:18 — Heb משענת 'staff/leaning' → Ar وكاية 'support/prop'

PROMOTE-IN-PLACE — 4 cross-book extensions:
  - מוגה   (Shemot 25:30, 35:13)  + Num 4:7        (already documented in blau_dict prose;
                                                    variants extended with double-waw מווגה / אלמווגה)
  - סלאמה  (Shemot 24:5, 32:6)    + Num 6:14, 7:17, 10:10, 15:8
                                                    — extends from "outside-Mishkan" attestation to
                                                    nazirite + chieftain-dedication + festival cycle
  - ד'כוה  (Vayikra 4:3/24, 7:7, 16:6/25) + Num 6:11, 7:16, 15:24, 28:15
                                                    — extends from Vayikra-core to nazirite +
                                                    inadvertent-sin + festival sin-offerings
  - יסתג'פר (Vayikra 5:6, 14:19, 16:6/16/30) + Num 5:8, 8:12, 15:25, 17:11
                                                    — extends from priestly-Yom-Kippur cluster to
                                                    Levite-consecration + national-supplication

DEFERRED — 11 SKIP / 0 borderline / 6 cluster-dupes logged
  - SKIP 14196 بكر, 14286 بيذر, 14347 ترك, 15295 خلاف, 17395 خدم, 17430 رأس,
         17639/40 عشر+عشريني (cluster), 19633 نحص, 19634/19635 نحل+نحلة (cluster),
         19861-19871 nfd family (11-row cluster — already deferred from Vayikra B1).
  - BORDERLINE: none. (Pre-scan lemma מסוחייה does NOT attest in Num 4 — Saadia uses
    دهن المسح, not مسوحية; the Vayikra B1 borderline stays put for Track B.)

Apply pattern
-------------
- Mirrors scripts/apply_phase4_vayikra_batch1.py with one structural extension:
  PROMOTE_IN_PLACE becomes a LIST (4 cross-book extensions vs Vayikra's 1).
  _patch_promote_in_place() iterates the list and returns a list of summaries.
- Fresh "bamidbar" namespace in data/_blau_saadia_deferred.json (idempotent on
  blau_id, same _update_deferred() helper).
"""

import json
import pathlib
import sys
from collections import Counter

# ============================================================================
# NEW ENTRIES
# ============================================================================

NEW_ENTRIES = [
    # ====================================================================
    # GLOSS — 5 net-new
    # ====================================================================

    # ---- GLOSS — Num 4:13: Reduce-to-ash (altar-cleaning) --------------
    {
        "lemma_ja": "רמד",
        "variants": ["וירמדו", "ירמד", "אלרמאד"],
        "lemma_ar": "رمد",
        "root": "ر-م-د",
        "tier": "gloss",
        "classical_en": "Classical Arabic رمد = 'to become ash, to be reduced to ashes' (Form I intransitive-essive); the noun رماد is the standard Arabic word for 'ash'. Form II رَمَّد carries the transitive 'to reduce to ashes', sometimes 'to spread ashes upon, to bury under ash'.",
        "classical_he": "בערבית הקלאסית رمد = 'נעשה אפר, הצטמצם לאפר' (בניין I פנימי-עיצומי); השם רמאד הוא המילה הערבית הסטנדרטית ל'אפר'. בניין II رَمَّد יוצא 'הפך לאפר', לעיתים 'פיזר אפר על, כיסה באפר'.",
        "saadia_en": "they shall reduce to ashes (the altar) — calque on Heb דשן but flipped essive",
        "saadia_he": "וְדִשְּׁנוּ אֶת-הַמִּזְבֵּחַ",
        "mechanism": "Essive-ablative semantic flip on the noun-derived verb: Hebrew דִשֵּׁן (D-stem of דשן, the 'ash' root) is an ABLATIVE denominal — 'to remove the (fatty) ashes from the altar'; the action removes ash, leaving the altar clean. Saadia renders it with Arabic Form I رَمَدَ — but רמד is an ESSIVE denominal of the same 'ash' root — 'to become ash, to be reduced to ash'. The two roots share the noun-base (Heb דֶּשֶׁן ~ Ar رماد both 'ash') but each parent language verbalized the noun in opposite directions. Saadia's choice preserves the root-link (both verbs derive from the language's word for 'ash') but inverts the action-direction (Heb: ash is removed; Ar: thing becomes ash). The result is a pedagogically vivid Heb→Ar pairing where the surface morphology rhymes but the underlying ergative orientation is reversed.",
        "verses": [{"book": "Bamidbar", "ch": 4, "v": 13}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "رمد",
            "sense": "رمد Form I 'to be reduced to ashes' (essive on the noun رماد 'ash') — Blau cites Saadia on Num 4:13 ('ודשנו את המזבח' = וירמדו אלמד'בח) with the note that classical-Arabic رمد is typically intransitive-essive, distinct from the standard Form-IV verb for ablative ash-removal. Tāj generalizes the field-domain but does not record the verbal essive sense in this specific noun.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Num 6:4: Grape-pip (nazirite prohibition) -------------
    {
        "lemma_ja": "פרצן",
        "variants": ["אלפרצן", "פרצנא"],
        "lemma_ar": "فرصن",
        "root": "ف-ر-ص-ن",
        "tier": "gloss",
        "classical_en": "Classical Arabic فرصن (a rare/late dialectal substantive; not in the major mainstream classical lexica as a vine-product noun) = 'grape-pip, grape-stone'; reflects either an Aramaic-via-Hebrew loan-bridge (Heb חרצן → JA פרצן via metathesis ḥrṣ → frṣ) or Saadia's coinage as a Hebraizing technical noun for the nazirite-prohibition list.",
        "classical_he": "בערבית הקלאסית فرصن (שם נדיר/מאוחר-דיאלקטלי; אינו מתועד במילונים הקלאסיים המרכזיים כשם של תוצרת-גפן) = 'גרעין-ענב, חרצן'; משקף או שאילה ארמית-עברית (חרצן → פרצן בהיפוך-עיצורים ḥrṣ → frṣ) או הטבעה רס\"גית של מונח טכני מעוּברת לרשימת איסורי הנזיר.",
        "saadia_en": "the grape-pip (חרצן)",
        "saadia_he": "חַרְצָן (גרעין הענב)",
        "mechanism": "Non-cognate lexical substitution for a nazirite-prohibition noun: Hebrew חַרְצָן ('grape-stone, pip' — the inner-most stone of the grape, distinct from זג the outer skin) gets the Arabic فرصن — itself a rare/marginal noun, probably formed under Hebrew influence as a learned technical equivalent. Saadia's pairing is pedagogically distinctive precisely because فرصن is non-classical; the lexical map exposes the Saadia-translator working at the fringes of standard Arabic, coining where necessary to preserve the precise priestly-halakhic taxonomy of forbidden grape-products in the nazirite vow. The pair contrasts with Saadia's standard rendering of זג at the same verse, where he uses אלזג directly — preserving the Hebrew as a transliteration.",
        "verses": [{"book": "Bamidbar", "ch": 6, "v": 4}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "فرص",
            "sense": "فرصن 'grape-pip' — Blau cites Saadia on Num 6:4 ('מחרצנים ועד זג' = מן אלפרצן אלי' אלזג), noting that the noun is essentially absent from classical lexica and likely formed as a Hebraizing technical coinage for the nazirite-pericope.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Num 21:18: Support / leaning (well-digging song) ------
    {
        "lemma_ja": "וכאיה",
        "variants": ["וכאיאת", "בוכאיאתהם", "אלוכאיה"],
        "lemma_ar": "وكاية",
        "root": "و-ك-ي",
        "tier": "gloss",
        "classical_en": "Classical Arabic وكاية (verbal-noun of Form I وكى) = 'reliance, support, leaning-upon, that-which-supports'; an abstract noun for the supporting-function rather than a concrete implement. Distinct from عَصا 'staff' and مِشْعَة 'walking-stick', which Arabic uses for the literal implement.",
        "classical_he": "בערבית הקלאסית وكاية (שם-פעולה של בניין I وكى) = 'הישענות, תמיכה, סמיכה, מה-שמסַייע'; שם מופשט לתפקוד-התמיכה ולא לכלי-המוחשי. שונה מ-عَصا 'מטה' ו-مِشْعَة 'מקל-הליכה' ששימשו את הערבית למשמעות המוחשית.",
        "saadia_en": "supports / leanings (משענת)",
        "saadia_he": "מִשְׁעֲנֹתָם (משענות-הסומכים)",
        "mechanism": "Concrete-to-abstract register shift: Hebrew מִשְׁעֲנֹתָם at Num 21:18 ('the well dug by princes, with their staves') is the concrete implement — a literal staff or leaning-rod the well-diggers carried and used. Saadia abstracts to وكاية, the verbal-noun of the supporting-function — 'their supports / their leanings'. The Heb construct מ-+שען (mafʿal of שען 'to lean') names the implement-via-its-action; Saadia's Ar verbal-noun names the action-without-the-implement. The choice generalizes the mythic well-digging song to a more abstract poetic register, fitting the Saadia tendency to smooth concrete-archaic Hebrew into philosophical-poetic Arabic at exactly the textual moments where the Heb is most archaic (cf. Num 21:14's quotation from the 'Book of the Wars of YHWH').",
        "verses": [{"book": "Bamidbar", "ch": 21, "v": 18}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "وكي",
            "sense": "وكاية 'reliance, support' — Blau cites Saadia on Num 21:18 ('במחקק במשענתם' = רסמוהא בוכאיאתהם 'they marked it out with their supports'), noting the abstract-noun choice over the concrete-implement options عَصا / مِشْعَة.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Num 22:1 +5 verses: Wilderness for Heb plains ---------
    {
        "lemma_ja": "בידאא",
        "variants": ["בידאת", "בידאת מואב", "אלבידאא"],
        "lemma_ar": "بيداء",
        "root": "ب-ي-د",
        "tier": "gloss",
        "classical_en": "Classical Arabic بيداء (plural بيداوات / بيد) = 'desert, wilderness, trackless waste'; a specifically arid-and-uninhabited landscape, distinct from عربة (Arabic cognate to Heb ערבה) which the Saadia could have chosen but avoided.",
        "classical_he": "בערבית הקלאסית بيداء (רבים بيداوات / بيد) = 'מדבר, ערבה שוממה, אזור שאין בו אדם'; נוף יבש וריק במובהק, שונה מ-عربة (קוגנט ערבי לעברית 'ערבה') שרס\"ג היה יכול לבחור בה אך נמנע.",
        "saadia_en": "the wildernesses of Moab (ערבות מואב)",
        "saadia_he": "עַרְבוֹת מוֹאָב (במשמעות מדברית, לא חקלאית-שולית)",
        "mechanism": "Landscape-semantic shift away from the cognate: Hebrew עַרְבוֹת מוֹאָב names the Trans-Jordanian steppe-band — the agricultural-fringe pastureland east of the Jordan, semi-cultivable, settled by tribal-shepherds. The Arabic cognate عربة exists and means roughly the same thing. But Saadia avoids the cognate and chooses بيداء — 'wilderness, trackless waste', a noun for fully-uninhabited arid land. The lexical choice flattens the steppe-vs-desert geographical distinction the Hebrew makes carefully (the Bible distinguishes מדבר 'wilderness' from ערבה 'steppe-arabah' as distinct biomes); Saadia rolls them both under the wilderness term. Pedagogically distinctive because the cognate-substitution is visible to any student of both languages: Saadia chose NOT to use the easy ערבת/עربה pair. Surfaces invariantly across the 6 ערבות-מואב verses of the Bamidbar travel narrative.",
        "verses": [
            {"book": "Bamidbar", "ch": 22, "v": 1},
            {"book": "Bamidbar", "ch": 26, "v": 3},
            {"book": "Bamidbar", "ch": 31, "v": 12},
            {"book": "Bamidbar", "ch": 33, "v": 48},
            {"book": "Bamidbar", "ch": 35, "v": 1},
            {"book": "Bamidbar", "ch": 36, "v": 13},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "بيد",
            "sense": "بيداء 'desert, wilderness' — Blau cites Saadia for Heb ערבה with بيداء/بيداوات, noting the choice of the non-cognate over the available عربة. Surfaces across Num 22:1, 26:3/63, 31:12, 33:48/49/50, 35:1, 36:13 as the consistent rendering of ערבות מואב.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Num 35:12: Protection-noun for asylum-cities ----------
    {
        "lemma_ja": "תחמיה",
        "variants": ["אלתחמיה", "תחמי", "חמאה"],
        "lemma_ar": "تحمية",
        "root": "ح-م-ي",
        "tier": "gloss",
        "classical_en": "Classical Arabic تحمية (Form II verbal noun of حمى) = 'protection, sheltering, the act of placing under one's protective custody'; a generic abstract noun for the protecting-function, distinct from the specific noun ملجأ ('refuge, place of resort') that Arabic uses for the concrete asylum-site.",
        "classical_he": "בערבית הקלאסית تحمية (שם-פעולה של בניין II من حمى) = 'הגנה, החסות, מתן מקלט-תחת-חסות'; שם מופשט-כללי לתפקוד-ההגנה, שונה מן השם הספציפי ملجأ ('מקום מקלט') שמשמש את הערבית למקום הקונקרטי.",
        "saadia_en": "(cities of) protection (ערי מקלט)",
        "saadia_he": "עָרֵי מִקְלָט (כפשוטו: 'ערים שהן הגנה')",
        "mechanism": "Specific-asylum to general-protection: Hebrew מִקְלָט is a precise priestly-legal noun for the asylum-city institution (the 6 levitical cities where the manslaughter-by-accident takes refuge from the blood-redeemer until the high-priest's death). Saadia renders it not with the available concrete-asylum noun ملجأ but with the abstract Form-II verbal noun تحمية — 'the protecting-function itself'. The shift dissolves the specific-institutional-noun into a generic action-noun, fitting the broader Saadia tendency to translate priestly-legal nouns by their function rather than their institutional shape. The cities don't get a name; they get a description — 'they shall be for you a protection'. The cognate تَحَمَّى (Form V 'to take refuge') was available; Saadia chose the Form II verbal noun for the GIVING-protection sense rather than the SEEKING-protection sense, foregrounding the cities' institutional role.",
        "verses": [{"book": "Bamidbar", "ch": 35, "v": 12}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "حمي",
            "sense": "تحمية (Form II verbal noun) 'protection, sheltering' — Blau cites Saadia on Num 35:12 ('והיו לכם הערים למקלט' = פתכון תלך אלקרא תחמיה), noting the abstract-noun choice over the concrete asylum-noun ملجأ.",
            "relation": "direct",
        },
    },

    # ====================================================================
    # NOTE — 4 net-new
    # ====================================================================

    # ---- NOTE — Num 32:7, 32:9: Heb תניאון/ויניאו → Ar גבן ------------
    {
        "lemma_ja": "גבן",
        "variants": ["תגבנון", "וגבנו", "תגבן", "מגבן"],
        "lemma_ar": "جبن",
        "root": "ج-ب-ن",
        "tier": "note",
        "classical_en": "Classical Arabic جبن (Form I) = 'to be cowardly, to shrink back in fear'; Form II جَبَّن (or causative-equivalent جَبَّنَ) = 'to make cowardly, to instill fear-of-action in someone', the transitive-causative deriving the cowardice-state in the object.",
        "classical_he": "בערבית הקלאסית جبن (בניין I) = 'להיות פחדן, להירתע מאימה'; בניין II جَبَّن (או הצורה הגורמת המקבילה جَبَّنَ) = 'לעשות פחדן, להטיל פחד-לפעולה במישהו', יוצא-גורם המביא את הפחדנות אל המושא.",
        "saadia_en": "you-PL cause to be cowardly / they caused to be cowardly (תניאון / ויניאו)",
        "saadia_he": "תְנִיאוּן / וַיָּנִיאוּ ('הם מנעו את לבם, רפו את ידיהם')",
        "mechanism": "Semantic narrowing from generic-dissuasion to specifically-emotional-cowardice. Hebrew תְּנִיאוּן / וַיָּנִיאוּ at Num 32:7-9 (the Reubenite-Gadite confrontation: 'And why are you DISCOURAGING the children of Israel from crossing over into the Land') is the Hiphil of נוא 'to discourage, draw back, restrain'. The Heb is general — it covers any kind of restraint-from-action: military, intellectual, moral. Saadia renders both occurrences with Ar Form II جبن — 'you cause them to be cowardly / they made them cowardly'. The Ar verb specifically names the EMOTIONAL state induced (timidity, fear of battle); the Heb merely names the behavioral OUTCOME (didn't go forward). Saadia thus reframes the Reubenite sin from 'discouraging Israel' (neutral) to 'making Israel cowardly' (morally pejorative), aligning with the rabbinic tradition that interprets this exchange as Moses accusing the eastern tribes of slander-by-fear-mongering. Pedagogically distinctive because the same Heb verb in non-military contexts gets different Ar renderings; the choice of جبن signals Saadia reading the Reubenite-confrontation as a SPECIFICALLY-military cowardice-inducement episode.",
        "verses": [
            {"book": "Bamidbar", "ch": 32, "v": 7},
            {"book": "Bamidbar", "ch": 32, "v": 9},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "جبن",
            "sense": "جبن Form II 'to make cowardly' — Blau cites Saadia on Num 32:7 ('ולמה תניאון את לב בני ישראל' = ולם תגבנון קלוב בני אסראיל) and Num 32:9 ('ויניאו את לב בני ישראל' = וגבנו קלוב בני אסראיל), noting the lexical choice that specifies the emotional-cowardice frame over a generic dissuasion-frame.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Num 31:5 +4 verses: Heb חלוץ → Ar מגרד ----------------
    {
        "lemma_ja": "מגרד",
        "variants": ["מגרדין", "אלמגרד", "מגרדה"],
        "lemma_ar": "مجرد",
        "root": "ج-ر-د",
        "tier": "note",
        "classical_en": "Classical Arabic مجرد (Form II passive participle of جرد 'to strip bare, to denude, to detach') = 'stripped, divested, bare, unencumbered'; in military usage = 'a soldier stripped of impediments for swift action, a light-cavalry detachment-fighter'. The participle frames the warrior by what he is WITHOUT (baggage, armor-encumbrance) rather than by what he has.",
        "classical_he": "בערבית הקלאסית مجرد (פעול בניין II מן جرد 'להפשיט, לערטל, לנתק') = 'מופשט, חשוף, ערום, ללא מסירבל'; בשימוש צבאי = 'חייל מופשט מנטל לפעולה מהירה, פרש-קל בקרב-יחידני'. הצורה מאפיינת את הלוחם על-פי מה שאין-לו (משא, שריון מכביד) ולא על-פי מה שיש-לו.",
        "saadia_en": "the vanguard / the stripped-for-action (חלוץ)",
        "saadia_he": "חָלוּץ (לוחם-החלץ ההולך לפני הצבא)",
        "mechanism": "Frame-shift from equipped-vanguard to stripped-for-action: Hebrew חָלוּץ is the priestly-military designation for the front-of-the-army warrior — the vanguard-equipped soldier, the 'one girded for war' (cognate with the verb חלץ 'to draw out, to gird'). The Heb foregrounds the GIRDING — the deliberate equipping. Saadia renders it with مجرد — the Form-II passive participle that foregrounds the STRIPPING — the deliberate removal of impediments. The two participles are nearly opposite in their frame: Heb 'equipped-for' vs Ar 'stripped-of'. Yet they name the same soldier-type. Saadia's choice routes the Heb military-cultic vocabulary through the classical-Arabic vocabulary of mounted-light-cavalry warfare, where the 'stripped' fighter (no armor, no provisions) is the model of swift mobile warfare. Surfaces invariantly across the Midianite-war + Transjordan-conquest cluster (Num 31:5, 32:21, 32:27, 32:29, 32:30) — exactly the warlike-frame pericopes of Bamidbar. The cross-pericope consistency confirms the choice is not contextual but lexical-fixed.",
        "verses": [
            {"book": "Bamidbar", "ch": 31, "v": 5},
            {"book": "Bamidbar", "ch": 32, "v": 21},
            {"book": "Bamidbar", "ch": 32, "v": 27},
            {"book": "Bamidbar", "ch": 32, "v": 29},
            {"book": "Bamidbar", "ch": 32, "v": 30},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "جرد",
            "sense": "مجرد (Form II passive participle) 'stripped-for-action, light-warrior' — Blau cites Saadia on Num 31:5 ('חלוצי צבא' = מגרדין לאלג'זו) and the Num 32 Reubenite-Gadite conditional-vow pericopes (32:21/27/29/30) where חלוץ is consistently rendered מגרד, noting the framing-inversion vs the underlying Heb root חלץ.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Num 3:7 +7 verses: Heb משמרת → Ar מחפצה ---------------
    {
        "lemma_ja": "מחפצה",
        "variants": ["מחפץ", "מחפץ'", "מחפצ'ה", "מחפט", "מחפט'ה", "אלמחפץ", "חפץ'"],
        "lemma_ar": "محفظة",
        "root": "ح-ف-ظ",
        "tier": "note",
        "classical_en": "Classical Arabic محفظة (Form II nominal مفعلة of حفظ 'to guard, preserve, keep watch') = 'the place/instrument/duty of guarding'; in classical usage it carries the concrete sense 'wallet, pocket, that which preserves' but Saadia coins it as a technical-administrative noun for the Levitical guard-duty institution. The Form II verb حَفَّظ ('to make guard, to assign as watch') backs the institution-noun.",
        "classical_he": "בערבית הקלאסית محفظة (שם בניין II במשקל مفعلة מן حفظ 'לשמור, להגן, לעמוד על המשמר') = 'המקום/הכלי/החובה של השמירה'; בשימוש הקלאסי השם נושא את המובן הקונקרטי 'ארנק, כיס, מה ששומר', אך רס\"ג טובע אותו כמונח טכני-אדמיניסטרטיבי למוסד משמרת הכוהנים והלויים. הפועל בבניין II حَفَّظ ('להפקיד על משמר, למנות כשומר') תומך בשם-המוסד.",
        "saadia_en": "the guard-duty / the charge / the watch (משמרת)",
        "saadia_he": "מִשְׁמֶרֶת (מוסד השמירה הלוויי-כהני)",
        "mechanism": "Institutional-technical coinage by Form II nominal: Hebrew מִשְׁמֶרֶת is the central priestly-administrative noun of the Bamidbar Levitical cycle — the assigned guard-duty/charge each Levite-clan owes the Mishkan, the formal watch over the holy precinct, the duty-rotation. The Hebrew is itself a coined-technical noun (mishkal mishkélet, mafʿélet of שמר). Saadia coins the parallel — Form II مفعلة of حفظ — to name the same institution. The coined noun is fixed and invariant across the 8 Bamidbar attestations of משמרת (Num 3:7, 3:8, 3:28, 3:32, 3:38, 8:26, 18:3, 31:30), surfacing in both subject ('the guards of the מחפץ') and object ('they will keep the מחפץ') positions. The choice parallels the Heb-coining strategy at the morphological level: just as Hebrew built מִשְׁמֶרֶת as the technical mafʿélet-of-שמר for this priestly office, Saadia builds مفعلة-of-حفظ as its Arabic counterpart. Pedagogically distinctive because the morphological-parallelism (both nouns are denominal-institutional, derived by the same template-pattern from the language's core 'guard' verb) makes the equation legible to a bilingual reader at the morphological level itself, beyond the lexical pairing.",
        "verses": [
            {"book": "Bamidbar", "ch": 3, "v": 7},
            {"book": "Bamidbar", "ch": 3, "v": 8},
            {"book": "Bamidbar", "ch": 3, "v": 28},
            {"book": "Bamidbar", "ch": 3, "v": 32},
            {"book": "Bamidbar", "ch": 3, "v": 38},
            {"book": "Bamidbar", "ch": 8, "v": 26},
            {"book": "Bamidbar", "ch": 18, "v": 3},
            {"book": "Bamidbar", "ch": 31, "v": 30},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "حفظ",
            "sense": "محفظة (Form II nominal مفعلة) 'guard-duty, charge' — Blau cites Saadia on Num 3:7 ('ושמרו את משמרתו ואת משמרת כל העדה' = ויחפצ'ו מחפצ'ה ומחפץ' אלגמאעה) and the broader Bamidbar cluster, noting the technical-administrative coinage that parallels the Heb mafʿélet-of-שמר institutional-noun template.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Num 13:21, 13:32, 15:39: Heb תור → Ar ראם -------------
    {
        "lemma_ja": "ראם",
        "variants": ["וראמו", "ראמוה", "תרומו", "לנרומה", "אראם", "ירומון", "רואם"],
        "lemma_ar": "روم",
        "root": "ر-و-م",
        "tier": "note",
        "classical_en": "Classical Arabic روم Form I (irregular weak-medial; perfect رَامَ, imperfect يَرُومُ) = 'to want, to seek-after, to intend, to aim-at-acquiring'; an intentional-volitional verb of pursuit, distinct from أراد ('to wish/will' in a more general sense) by foregrounding the seeking-out, going-after dimension. Form II رَوَّم likewise = 'to cause to pursue / to set in pursuit-after'.",
        "classical_he": "בערבית הקלאסית روم בניין I (חלוש העין; עבר رَامَ, עתיד يَرُومُ) = 'לרצות, לחפש-להשיג, לכוון אל-, לשאוף-לקבל'; פועל-כוונה רצוני של רדיפה, שונה מ-أراد ('לרצות/לחפוץ' במובן כללי) בהבלטת הרכיב של חיפוש-וירידה-אחרי-המטרה. בניין II רַוַּם דומה = 'לגרום-לרדוף / להשׂים-במרדף'.",
        "saadia_en": "to seek-after / to set in pursuit-of (תור)",
        "saadia_he": "תור ('לתור', 'לרגל', 'לחקור' — לפי ההקשר)",
        "mechanism": "Volitional reframe of a physical-exploration verb: Hebrew תור across the Bamidbar 12-spies narrative (וַיָּתֻרוּ אֶת-הָאָרֶץ Num 13:21, אֲשֶׁר תָּרוּ אֹתָהּ Num 13:32, with the metaphorical extension at Num 15:39 וְלֹא-תָתוּרוּ אַחֲרֵי לְבַבְכֶם 'do not go-after your heart and eyes') is fundamentally a verb of physical exploration-and-seeking — the spies physically traverse the land, the worshipper's eyes physically follow the heart's desire. Saadia consistently renders all three with روم — but روم is a VOLITIONAL verb of intentional pursuit, not a physical-motion verb. The shift relocates the action's center from the body (Heb: feet, eyes traverse) to the intention (Ar: the will pursues). The reframe is particularly striking at Num 15:39 — the prohibition against 'going-after' the heart and eyes becomes a prohibition against 'pursuing-with-intent' them, foregrounding the volitional-moral dimension that the rabbinic-philosophical tradition emphasizes in this verse. The cross-pericope consistency across two semantically-distinct contexts (physical land-spying + metaphorical desire-following) confirms that Saadia is making a lexical-fixed choice, not a context-driven one. Reinforces the broader Saadia tendency to abstract concrete-Hebrew motion-verbs into Arabic verbs of intention/will (cf. similar moves with √תור, √בקש, √רצה).",
        "verses": [
            {"book": "Bamidbar", "ch": 13, "v": 21},
            {"book": "Bamidbar", "ch": 13, "v": 32},
            {"book": "Bamidbar", "ch": 15, "v": 39},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "روم",
            "sense": "روم Form I 'to seek-after, intend, pursue' — Blau cites Saadia on Num 13:21 ('ויתורו את הארץ' = וראמו אלבלד), Num 13:32 ('אשר תרו אותה' = אלד'י ראמוה), and Num 15:39 ('ולא תתורו אחרי לבבכם ועיניכם' = ולא תרומו אתבאע קלובכם ועיונכם), with cross-attestation in Yefet on Dan 92 (لا يثبت له ما رام إلى إثباته 'what he sought to confirm') confirming the volitional-pursuit frame as Saadia's stable lexical choice for biblical תור.",
            "relation": "direct",
        },
    },
]


# ============================================================================
# PROMOTE-IN-PLACE — list of cross-book extensions
# ============================================================================

PROMOTE_IN_PLACE = [
    # --- מוגה (showbread) — Shemot → +Num 4:7 ------------------------------
    {
        "lemma_ja": "מוגה",
        "extend_verses": [
            {"book": "Bamidbar", "ch": 4, "v": 7},
        ],
        "extend_variants": ["מווגה", "אלמווגה"],
        "mechanism_rewrite": (
            "Calque-by-passive-participle: Hebrew לֶחֶם הַפָּנִים ('bread of the face/presence') "
            "gets rendered with خبز موجه ('faced bread') — a technical translation that preserves "
            "the construct-state's facial semantics by deploying the passive-participle of وجه ('to face, to direct'). "
            "Saadia uses موجه across the table-of-presence pericopes (Ex 25:30, 35:13) AND extends it to the "
            "Mishkan-furniture transport instructions at Num 4:7 ('שלחן הפנים' = מאידה' אלמווגה — 'the faced table'), "
            "where the same lexical move applies to the table itself rather than its bread. The cross-book extension "
            "confirms the term is paradigm-stable across the table-of-presence cluster. The double-waw spelling "
            "(מווגה ~ מוגה) reflects manuscript-tradition variation in the explicit-defective representation of the "
            "Form II passive-participle vowel pattern. al-Fāsī's Jāmiʿ 467-468 transmits the 'two-faced bread' "
            "interpretation that drives this calque-by-facing strategy."
        ),
        "blau_dict_sense_rewrite": (
            "موجه (Form II passive participle of وجه) 'faced, directed-to' — Blau cites Saadia on Ex 35:13 "
            "and the bundled Num 4:7 שולחן הפנים = אלמאידה אלמוגהה (variant מווגה), with al-Fāsī Jāmiʿ 467-468 "
            "transmitting the 'two-faced bread' interpretation."
        ),
    },

    # --- סלאמה (peace-offering) — Shemot → +Bamidbar (4-system extension) ---
    {
        "lemma_ja": "סלאמה",
        "extend_verses": [
            {"book": "Bamidbar", "ch": 6, "v": 14},
            {"book": "Bamidbar", "ch": 6, "v": 17},
            {"book": "Bamidbar", "ch": 7, "v": 17},
            {"book": "Bamidbar", "ch": 10, "v": 10},
        ],
        # ta-marbuta opens to -ת before pronominal suffixes (Num 10:10 'סלאמתכם')
        "extend_variants": ["סלאמת", "סלאמתכם"],
        "mechanism_rewrite": (
            "Cognate semantic-field pairing, now confirmed across four ritual systems: Heb שלם ~ Ar سلم share "
            "the 'wholeness/peace' root, so Saadia picks سلامة (the abstract noun) over the standard Arabic "
            "ذبيحة-السلام or قربان-السلام. The idiom ذبائح سلامة surfaces invariantly across (1) the covenant "
            "ceremony at Sinai (Ex 24:5; 32:6 — outside the Mishkan); (2) the nazirite-completion ritual "
            "(Num 6:14, 6:17, 6:18 — peace-offering at the conclusion of the nazirite vow); (3) the chieftain-"
            "dedication twelve-day cycle (Num 7:17, 7:23, 7:29, 7:35, 7:41, 7:47, 7:53, 7:59, 7:65, 7:71, 7:77, "
            "7:83 — peace-offerings as the climactic gift of each tribal chieftain); and (4) the festival-trumpet "
            "summons (Num 10:10 — peace-offerings on appointed festivals and rosh-chodesh). The four-system "
            "cross-attestation confirms سلامة is Saadia's invariant lexical choice for זבח שלמים regardless of "
            "the surrounding ritual context. Verses listed are representative anchors per system."
        ),
        "blau_dict_sense_rewrite": (
            "سلامة 'peace-offering' (idiom ذبائح السلامة) — Blau cites Saadia on Ex 24:5; 32:6 (with the Lev 3:1 "
            "cross-reference), with the Bamidbar nazirite-completion + chieftain-dedication + festival-cycle "
            "attestations (Num 6:14/17/18, 7:17ff, 10:10) confirming the four-system invariance. "
            "Geniza-attested قربان السلامة in Ḥafetz 139:12."
        ),
    },

    # --- ד'כוה (sin-offering) — Vayikra → +Bamidbar (broader subsystem) ----
    {
        "lemma_ja": "ד'כוה",
        "extend_verses": [
            {"book": "Bamidbar", "ch": 6, "v": 11},
            {"book": "Bamidbar", "ch": 7, "v": 16},
            {"book": "Bamidbar", "ch": 15, "v": 24},
            {"book": "Bamidbar", "ch": 28, "v": 15},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Theological reframe via noun-substitution, now confirmed across the FULL priestly-Numbers cycle: "
            "Hebrew חַטָּאת for the sin-offering is itself a contested name — the noun literally means "
            "'sin/transgression' (root ח-ט-א), but in priestly usage it refers to the OFFERING that REMOVES sin. "
            "Saadia takes the second sense and lexicalizes it directly with ذكوة, naming the offering by its "
            "EFFECT (purification) rather than its CAUSE (sin). The shift erases the paradox in the Hebrew "
            "nomenclature and aligns with the broader Quranic-Arabic z-k-w family of purification-language "
            "(زكاة 'alms-purification'). This is Saadia's invariant rendering across the FULL priestly-cultic "
            "lexicon: (1) Vayikra offering pericopes — 4:3, 4:24, 5:6, 7:7, 7:37, 14:19/22, 16:6/11, 16:15/25; "
            "(2) Bamidbar — the nazirite-impurity sin-offering (6:11), the chieftain-dedication twelve-day cycle "
            "(7:16, 7:22, 7:28, 7:34, 7:40, 7:46, 7:52, 7:58, 7:64, 7:70, 7:76, 7:82), the inadvertent-community-sin "
            "ordinance (15:24, 15:25, 15:27), and the festival sin-offerings of the new-moon + appointed-times cycle "
            "(28:15, 28:22, 29:5, 29:11, 29:16). The cross-pericope invariance — same lexical choice across Aaronic "
            "consecration, Day-of-Atonement, leper-purification, nazirite-completion, chieftain-dedication, "
            "inadvertent-sin, and festival sin-offerings — confirms ذكوة as Saadia's fixed name for the institution, "
            "not a context-driven choice. Ḥafetz 139:9 + 142:18 transmits the pairing. Verses listed are representative "
            "anchors per system."
        ),
        "blau_dict_sense_rewrite": (
            "ذكوة (plural ذكوات) 'sin-offering' — Blau cites Saadia on Lev 4:24 + 16:25, with the Bamidbar "
            "nazirite-impurity (6:11), chieftain-dedication (7:16ff), inadvertent-sin (15:24), and festival-cycle "
            "(28:15ff, 29:5ff) attestations confirming the invariant cultic-technical choice across the priestly "
            "subsystem. Ḥafetz 139:9 + 142:18 transmits Saadia's standard rendering."
        ),
    },

    # --- יסתג'פר (atonement) — Vayikra → +Bamidbar (broader subsystem) -----
    # NB Num 25:13 (Phinehas) was projected by the prompt but verified-OUT:
    # Saadia uses bare Form I "וכפר" there (cognate-direct), not Form X.
    {
        "lemma_ja": "יסתג'פר",
        "extend_verses": [
            {"book": "Bamidbar", "ch": 5, "v": 8},
            {"book": "Bamidbar", "ch": 8, "v": 12},
            {"book": "Bamidbar", "ch": 15, "v": 25},
            {"book": "Bamidbar", "ch": 17, "v": 11},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Theological reframe from ritual-mechanism to relational-supplication, now confirmed across the full "
            "Numbers atonement-vocabulary: Hebrew כָּפַר (root כ-פ-ר 'to cover') is the priestly verb for ritual "
            "atonement — the offering MECHANICALLY covers/wipes the sin from God's view. Saadia consistently "
            "translates this with Form X استغفر 'to seek forgiveness' — relocating the action from "
            "mechanical-covering to relational-supplication, from the offering's effect on God's vision to the "
            "supplicant's address to God's mercy. The Form X morphology (request/seek-after) reframes the priest's "
            "action as petitionary rather than performative. Surfaces invariantly across Vayikra (Lev 5:6, 14:19, "
            "16:6, 16:16, 16:30) AND the Bamidbar cluster: (1) restitution-with-guilt-offering (5:8 — 'beyond the "
            "ram of atonement with which he shall atone'); (2) Levite-consecration ritual (8:12 — 'to atone for "
            "the Levites', 8:19, 8:21); (3) inadvertent-communal-sin (15:25, 15:28); (4) national supplication in "
            "the Korach aftermath (17:11 — Aaron with the censer, 'to atone for them'); (5) festival sin-offerings "
            "(28:22, 28:30, 29:5, 29:11). Across all five contexts — guilt-restitution, Levite-consecration, "
            "communal-error, national-supplication, festival-cycle — the same Form X choice holds, confirming the "
            "supplication-reframe is invariant across the priestly atonement system. (Notable counter-case: at "
            "Num 25:13 — Phinehas's covenant of peace, 'because he was zealous for his God and atoned for the "
            "children of Israel' — Saadia does NOT use Form X, retaining the bare Form I cognate כפר; the choice "
            "marks the Phinehas episode as a covenant-zeal frame rather than a routine atonement-supplication, "
            "preserving the Hebrew's emphasis on the act-of-zeal that earned the priestly covenant.) "
            "Ḥibbur Yāfet transmits the standard Form-X pairing as Saadia's canonical rendering."
        ),
        "blau_dict_sense_rewrite": (
            "غفر (Form X استغفر) 'to forgive, to seek forgiveness' — Blau cites Saadia on Lev 16:6 with the Ex 29:36 "
            "parallel, plus the broader Bamidbar atonement-cluster (Num 5:8, 8:12/19/21, 15:25/28, 17:11, 28:22/30, "
            "29:5/11) confirming the invariant Form-X 'supplication' reframe of biblical כפר across the priestly "
            "atonement system. (Num 25:13 Phinehas-zeal is the marked exception: bare Form I cognate.) "
            "Ḥibbur Yāfet transmits the canonical pairing."
        ),
    },
]


# ============================================================================
# DEFERRED — skip / borderline / cluster-dupes
# ============================================================================

BATCH1_DEFERRED = {
    "skip": [
        {
            "blau_id": 14196,
            "root_ar": "بكر",
            "verse_hint": "Num 1:20 בכר ישראל / 3:2 הבכר / 3:12-13 בכור",
            "reason": "Direct cognate Heb בכור ~ Ar بكر 'firstborn'; Saadia uses بكر invariantly. Trivial cognate-pair, no semantic-field divergence.",
        },
        {
            "blau_id": 14286,
            "root_ar": "بيذر",
            "verse_hint": "Num 15:20 (Blau citation: 'תאג' גדול בזאון')",
            "reason": "No surface attestation of בידר/بيذر in the Bamidbar 15:20 tafsir; Saadia must use a different rendering for ראשית עריסותיכם. The citation appears to be a Lane/Tāj cross-reference, not a Saadia-direct anchor.",
        },
        {
            "blau_id": 14347,
            "root_ar": "ترك",
            "verse_hint": "Num 10:31 'אל נא תעזב' / 20:21 'יתרך' / 32:15 'תרכהם'",
            "reason": "Generic cognate-direct rendering of עזב/נטש 'to leave'; Saadia uses ترك uniformly. The Blau body excerpt foregrounds an idiom (تركه يفعل 'leave him to do') that's not paradigm-shifting in the Bamidbar attestations.",
        },
        {
            "blau_id": 15295,
            "root_ar": "خلاف",
            "verse_hint": "Methodology citation (Ibn Janāḥ, Sa'adia metalanguage, Daniel commentary)",
            "reason": "No JA-surface attestation in Bamidbar tafsir for the כלאף/خلاف headword; the Blau citation is methodological (Saadia's 'variant-reading' or 'different rendering' frame) rather than a Bamidbar-anchored lexical choice.",
        },
        {
            "blau_id": 17395,
            "root_ar": "خدم",
            "verse_hint": "Num 8:25 'ולא יעבד עוד' = ולא יכ'דם אבדא",
            "reason": "Saadia's standard rendering of priestly/cultic עבד with خدم is well-established (45+ Bamidbar attestations) but reflects a routine semantic-split (Heb עבד covers slave-labor + priestly-service + general-work; Ar narrows to خدم for attendant-service). Not paradigm-shifting; standard Arabic semantic field-split, not a Saadia coinage.",
        },
        {
            "blau_id": 17430,
            "root_ar": "رأس",
            "verse_hint": "Num 10:10 'ובראשי חדשיכם' = ורוס שהורכם",
            "reason": "Direct cognate Heb ראש ~ Ar رأس in the 'head/first/start' construct-of-time idiom; no semantic-field divergence at the cited verse.",
        },
        {
            "blau_id": 17639,
            "root_ar": "عشر",
            "verse_hint": "Num 26:42 'למשפחתם' (numerical-counting context)",
            "reason": "Direct cognate Heb עשר ~ Ar عشر 'ten / count-of-ten'; the Blau body excerpt foregrounds a counting-locution at the family-census verse, but the rendering is cognate-direct without semantic-field shift.",
        },
        {
            "blau_id": 17640,
            "root_ar": "عشريني",
            "verse_hint": "Num 26:42 (variant of 17639)",
            "reason": "Variant of 17639; no separate Bamidbar attestation of the headword עשריני (the bare-numerical 'twenty / vigesimal' substantive doesn't surface in the Bamidbar tafsir).",
        },
        {
            "blau_id": 19633,
            "root_ar": "نحص",
            "verse_hint": "Num 18:23 'ולא ינחלו נחלה'",
            "reason": "No surface attestation of נחצ/نحص in the Bamidbar 18:23 tafsir; Saadia uses نحل directly (cognate). The 17633 headword is likely a Blau-internal manuscript-variant cross-reference, not an independent reading.",
        },
        {
            "blau_id": 19634,
            "root_ar": "نحل",
            "verse_hint": "Num 18:23 'ולא ינחלו נחלה' = לא ינחלו נחלה",
            "reason": "Direct cognate Heb נחל ~ Ar نحل in the 'inherit' Form I; the Form II causative for הנחיל (Deut 1:38 etc., not Bamidbar-anchored) would be the more interesting reading, but at Num 18:23 the surface is direct-Form-I cognate.",
        },
        {
            "blau_id": 19635,
            "root_ar": "نحلة",
            "verse_hint": "Num 18:23-24 'נחלה' substantive",
            "reason": "Direct cognate substantive Heb נחלה ~ Ar نحلة 'inheritance, bequest'; cognate-pair, no semantic-field divergence.",
        },
        {
            "blau_id": 19861,
            "root_ar": "تنغيم / nfd family (11 rows)",
            "verse_hint": "Num 33:52 'והאבדתם את כל משכיותם' (Blau cluster cites Lev 26:30 + Num 33:52 + Deut 7:10 + Ps 37:38)",
            "reason": "11-row cluster (blau_ids 19861-19871) covering the nfd/nfx family ('to destroy, exterminate, blow-out'); Vayikra B1 already deferred this cluster because Lev 26:30 was missing from the tafsir chapter file. The Bamidbar attestation at Num 33:52 doesn't surface אנפד/أنفذ on a normalized scan — Saadia uses different rendering (probably تَخْريب or similar). Reasonable to keep deferred until a coordinated cluster-revisit. The single Num 5:2 hit on ינפו ('shall send-away the unclean from the camp', Form IV of نفي 'to exile') is the unrelated 'exile/banish' homograph, not the destruction-frame Blau cites.",
        },
        {
            "blau_id": 20392,
            "root_ar": "وكاية",
            "verse_hint": "Num 21:18 (handled — SHIPPED as gloss; entry above)",
            "reason": "Promoted to NEW_ENTRIES — see lemma וכאיה above.",
        },
    ],
    "borderline": [
        # None for Bamidbar B1.
        # Pre-scan lemma מסוחייה (Vayikra B1 borderline blau_id=19427) does NOT
        # attest in Bamidbar — Saadia renders שמן המשחה at Num 4:16 with دهن المسح,
        # not مسوحية. The Vayikra borderline stays put for Track B (Vayikra B2)
        # and is NOT consumed here.
    ],
    "_cluster_dupes_logged": [
        "17639≈17640 (عشر/عشريني cluster, 2 rows — cognate-direct numerical, both SKIP)",
        "18162≈18163 (فرص/فرصم cluster, 2 rows — 18162 SHIPPED as gloss פרצן; 18163 is the headword-variant)",
        "19633 + 19634 + 19635 (نحص/نحل/نحلة cluster, 3 rows — inheritance-vocabulary, all SKIP cognate)",
        "19861-19871 (nfd family, 11 rows — already cluster-deferred from Vayikra B1)",
        "סלאמה chieftain-dedication cluster (Num 7:17-83 = 12 verses) — collapsed to 1 representative anchor (7:17) in promote-in-place to avoid array bloat",
        "ד'כוה chieftain-dedication cluster (Num 7:16-82 = 12 verses) — collapsed to 1 representative anchor (7:16) in promote-in-place",
    ],
}


# ============================================================================
# Helpers
# ============================================================================

def _patch_promote_in_place(payload: dict) -> list[dict]:
    """Iterate PROMOTE_IN_PLACE (list) and apply each cross-book extension to
    its target entry. For each item: extend verses[] (dedup on (book, ch, v)),
    extend variants[] (dedup), and rewrite mechanism + blau_dict.sense.
    Returns a list of per-lemma summaries.
    """
    summaries = []
    for spec in PROMOTE_IN_PLACE:
        target_lemma = spec["lemma_ja"]
        for entry in payload["entries"]:
            if entry.get("lemma_ja") != target_lemma:
                continue
            # extend verses
            existing_v = {(v["book"], v["ch"], v["v"]) for v in entry.get("verses", [])}
            added_v = []
            for v in spec.get("extend_verses", []):
                key = (v["book"], v["ch"], v["v"])
                if key not in existing_v:
                    entry["verses"].append(v)
                    existing_v.add(key)
                    added_v.append(f"{v['book']} {v['ch']}:{v['v']}")
            # extend variants
            existing_var = set(entry.get("variants", []))
            added_var = []
            for var in spec.get("extend_variants", []):
                if var not in existing_var:
                    entry.setdefault("variants", []).append(var)
                    existing_var.add(var)
                    added_var.append(var)
            # rewrite mechanism + blau_dict.sense
            if added_v or added_var:
                if "mechanism_rewrite" in spec:
                    entry["mechanism"] = spec["mechanism_rewrite"]
                if "blau_dict_sense_rewrite" in spec:
                    entry.setdefault("blau_dict", {})["sense"] = spec["blau_dict_sense_rewrite"]
                summaries.append({
                    "lemma": target_lemma,
                    "verses_added": added_v,
                    "variants_added": added_var,
                    "total_verses_now": len(entry["verses"]),
                })
            else:
                summaries.append({
                    "lemma": target_lemma,
                    "verses_added": [],
                    "variants_added": [],
                    "note": "all extensions already present (idempotent re-run)",
                })
            break
        else:
            summaries.append({"lemma": target_lemma, "error": "target lemma not found in divergence file"})
    return summaries


def _update_deferred(deferred_path: pathlib.Path) -> dict:
    """Write Bamidbar Batch 1 entries into data/_blau_saadia_deferred.json
    under a fresh "bamidbar" namespace (idempotent on blau_id).
    """
    payload = json.loads(deferred_path.read_text())
    bm = payload.setdefault("bamidbar", {})

    added = {"skip": 0, "borderline": 0}
    for bucket, new_items in BATCH1_DEFERRED.items():
        if bucket.startswith("_"):
            continue
        existing = bm.setdefault(bucket, [])
        existing_ids = {it.get("blau_id") for it in existing if isinstance(it, dict)}
        for item in new_items:
            if item.get("blau_id") in existing_ids:
                continue
            existing.append(item)
            existing_ids.add(item.get("blau_id"))
            added[bucket] = added.get(bucket, 0) + 1

    cluster_log = bm.setdefault("_cluster_dupes_logged", [])
    if isinstance(cluster_log, list):
        for line in BATCH1_DEFERRED["_cluster_dupes_logged"]:
            if line not in cluster_log:
                cluster_log.append(line)

    bm.setdefault("_session", "Phase 4 Bamidbar Batch 1 (apply_phase4_bamidbar_batch1.py)")

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return {"added": added, "bamidbar_buckets_now": {k: len(v) if isinstance(v, list) else v for k, v in bm.items()}}


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    div_path = root / "data" / "tafsir-divergence.json"
    deferred_path = root / "data" / "_blau_saadia_deferred.json"

    if not div_path.exists():
        print(f"FATAL: {div_path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    if not deferred_path.exists():
        print(f"FATAL: {deferred_path} not found", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(div_path.read_text())

    # 1) Cross-book promote-in-place patches (BEFORE append so collisions don't
    #    skip-collide on the existing lemma).
    promote_summaries = _patch_promote_in_place(payload)

    # 2) Append new entries by lemma_ja uniqueness.
    existing_lemmas = {e["lemma_ja"] for e in payload["entries"]}
    added = 0
    skipped = []
    for entry in NEW_ENTRIES:
        if entry["lemma_ja"] in existing_lemmas:
            skipped.append((entry["lemma_ja"], "lemma already present"))
            continue
        payload["entries"].append(entry)
        existing_lemmas.add(entry["lemma_ja"])
        added += 1

    div_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(div_path.read_text())  # parse-check

    deferred_summary = _update_deferred(deferred_path)

    print(f"Promote-in-place: {json.dumps(promote_summaries, ensure_ascii=False, indent=2)}")
    print(f"Added {added} entries to {div_path.name}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")
    print(f"Deferred file summary: {json.dumps(deferred_summary, ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    main()

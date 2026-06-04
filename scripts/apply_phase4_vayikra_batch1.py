"""
Phase 4 — Vayikra Batch 1.

Twelve hand-curated entries from the Vayikra-flagged subset of
data/_blau_saadia_candidates.json (76 candidates, blau_id 13781-20399,
filtered on saadia_citation_lines containing ויקרא / ויק׳ / ויק"). Each
has been verified against data/tafsir-vayikra-{ch}.json — the JA surface
form physically appears in the cited verse, and the Hebrew anchor word
appears in the verse's hebrew column (nikud + final-form normalization
applied for matching). The actual tafsir uses dotted Hebrew letters
(ד', כ', צ', ת') for the corresponding Arabic ذ/خ/ض/ث consonants — all
lemma forms below match the Cairo 2019 baseline orthography directly.

Tier breakdown:
  - 7 GLOSS — non-cognate Heb→Ar pairings, register shifts, technical
    extensions in the offering/dietary/purity/jubilee vocabulary
  - 5 NOTE — semantic surprises with stated mechanism; 3 are multi-verse
    semantic-field calques across the sin-offering / atonement / land-
    possession systems (ד'כוה 4 verses, יסתג'פר 4 verses, חוז 4 verses)
  - 1 PROMOTE-IN-PLACE — existing Shemot entry שחמה' (Ex 29:20 ear-tip
    idiom) extended with 5 Vayikra attestations across consecration-of-
    priests + leper-purification rituals (Lev 8:23, 14:14, 14:17, 14:25,
    14:28). First cross-book promotion in the Vayikra batch; pattern
    follows the נקל precedent from Shemot Batch 2.

Coverage by chapter:
  - Sacrificial system (Lev 1-7): קצבה (deferred), בד'ל, ד'כוה,
    יסתג'פר, אכ'ס, סתותייה, פריך — the technical vocabulary for
    offering-rite and offering-state
  - Priestly-consecration + leper-purification (Lev 8, 14): שחמה
    promote-in-place + חוז
  - Dietary law (Lev 11): סמברץ
  - Sabbatical + jubilee (Lev 25): כ'לף + חוז cross-pericope extension
  - Holiness Code (Lev 19-26): אצר, חארה, צנגה, אכ'ס cross-pericope

Deferred (written to data/_blau_saadia_deferred.json#/vayikra — fresh
namespace; see _update_deferred() below):
  - SKIP (10): metalanguage-only, cognate-direct, manuscript-variant,
    or non-Cairo-baseline attestations
  - BORDERLINE (4): strong but at-batch-cap or pending tier-judgment
    (קצבה Lev 1:8, לג Lev 14:10, מסוחייה Lev 8:2/10, כ'אמע Lev 21:18)
    — these are NOTE-grade candidates that didn't make the 5-NOTE cap
    this batch; promote them in Batch 2
  - _cluster_dupes_logged (13 cluster groups, 48 source-SQLite rows
    covering 13 underlying Blau articles): the Vayikra pool has the
    heaviest cluster-duplication of any book seen so far — qadas (6),
    nafd (11), kull (6), tholul (6) families dominate

Apply pattern mirrors scripts/apply_phase4_shemot_batch2.py. Dedupe on
lemma_ja only (DivergenceEntry has no `id` field). The _update_deferred()
helper writes to a fresh "vayikra" namespace and is idempotent on
blau_id. main() additionally runs the promote-in-place patch for شحمة
(blau_id 16478) before appending new entries.
"""

import json
import pathlib
import sys
from collections import Counter


NEW_ENTRIES = [
    # ====================================================================
    # GLOSS — 7 net-new
    # ====================================================================

    # ---- GLOSS — Lev 1:8 N/A (deferred to BORDERLINE-bucket) ----------
    # קצבה Lev 1:8 פדר is NOTE-grade but deferred to Batch 2 cap-trim.

    # ---- GLOSS — Lev 2:14: Parched fresh-grain (first-fruits offering)
    {
        "lemma_ja": "פריך",
        "variants": ["פפריך", "אלפריך"],
        "lemma_ar": "فريك",
        "root": "ف-ر-ك",
        "tier": "gloss",
        "classical_en": "Classical Arabic فريك = 'fresh-roasted ears of grain, especially of barley still in milky stage'; a specific culinary-agricultural term for the parched green-spike preparation eaten at first-harvest.",
        "classical_he": "בערבית הקלאסית فريك = 'שיבולים טריות קלויות, בעיקר שעורה בשלב החלב'; מונח קולינרי-חקלאי ספציפי לתבואה הירוקה הקלויה הנאכלת בראשית הקציר.",
        "saadia_en": "fresh-parched grain (אביב קלוי)",
        "saadia_he": "אָבִיב קָלוּי",
        "mechanism": "Technical-agricultural pairing: Hebrew אָבִיב ('ear-of-grain in spring-ripening stage') gets the matching Arabic culinary term فريك — both refer specifically to the milky-stage spike roasted in fire. Saadia uses فريك throughout the spring-barley pericope (Ex 9:31, 13:4, 23:15, 34:18) and at Lev 2:14 for the first-fruits-of-the-harvest minḥah. Ibn Janāḥ Shorashim 131 transmits the equivalence.",
        "verses": [{"book": "Vayikra", "ch": 2, "v": 14}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "فرك",
            "sense": "فريك 'fresh ears, especially of barley' — Blau cites Saadia on Lev 2:14 ('אביב קלוי באש' = פפריך מקלי באלנאר) alongside the Ex 9:31, 13:4, 23:15, 34:18 spring-barley cluster, with Ibn Janāḥ Shorashim 131 transmitting the technical pairing.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Lev 6:14: Well-mixed dough (minḥah preparation) -------
    {
        "lemma_ja": "סתותייה",
        "variants": ["סתותיה", "אלסתותייה"],
        "lemma_ar": "ستوتية",
        "root": "ست",  # Loanword; no clean triliteral root
        "tier": "gloss",
        "classical_en": "Classical Arabic ستوتية (not in standard classical lexicons; a Greek-via-Aramaic loanword — likely ultimately from Aramaic שתיתא / Syriac štītā 'a kind of porridge or kneaded paste') = a specially-prepared dough, well-mixed and oil-saturated.",
        "classical_he": "ערבית קלסית ستوتية (אינה ערך במילונים הקלסיים; שאילה יוונית-ארמית — קרוב לוודאי מן הארמית שתיתא / סורית štītā 'מין דייסה או בצק מעובד') = בצק שהוכן בצורה מיוחדת, מעוך ורווי שמן.",
        "saadia_en": "a well-mixed dough (מרבכת)",
        "saadia_he": "מֻרְבֶּכֶת (בצק שהוכן בצורה מיוחדת)",
        "mechanism": "Greek-Aramaic culinary loan: the rare Hebrew hapax מֻרְבֶּכֶת ('well-mixed, oil-saturated dough', from the root ר-ב-ך appearing only in the minḥah-pericopes) gets the equally-rare Arabic ستوتية — itself a non-classical loanword. Saadia bridges two outside-the-mainstream culinary technical terms, preserving the obscure-technical register of the priestly text. Dirinburg's note traces the chain to Babylonian-Aramaic שתיתא (= Syriac štītā).",
        "verses": [{"book": "Vayikra", "ch": 6, "v": 14}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "ست",
            "sense": "ستوتية '(dough) prepared in a special way' — Blau cites Saadia on Lev 6:14 ('מרבכת תביאנה' = סתותייה תאתי בהא רפכ'ה תכון), noting Dirinburg's identification of the term with Babylonian-Aramaic שתיתא ~ Syriac štītā as a culinary-technical loan.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Lev 11:30: Salamander/lizard species (impure animals) ---
    {
        "lemma_ja": "אלסמברץ",
        "variants": ["סמברץ", "ואלסמברץ"],
        "lemma_ar": "سنبرص",
        "root": "س-م-ب-ر-ص",  # quadriliteral, treat as such
        "tier": "gloss",
        "classical_en": "Classical Arabic سنبرص (also سمبرص — a phonetic-variant byform of سامّ أبرص 'the bringer of leprosy') = the gecko species Lacerta mauritanica; a specific zoological-folk identification used in classical materia medica and Maimonidean halakhah.",
        "classical_he": "בערבית הקלאסית سنبرص (גם سمبرص — צורת-משנה פונטית של سامّ أبرص 'מביא הצרעת') = מין שממית Lacerta mauritanica; זיהוי זואולוגי-עממי ספציפי, מוכר מן הרפואה הקלסית ומן ההלכה המיימונית.",
        "saadia_en": "the gecko-class lizard (תנשמת)",
        "saadia_he": "תִּנְשֶׁמֶת (מין שממית)",
        "mechanism": "Non-cognate zoological identification: Hebrew תִּנְשֶׁמֶת (an opaque reptile-name in the dietary-impurity list) gets a precise Mediterranean-zoological identification as سنبرص — the gecko Lacerta mauritanica. Saadia's choice routes the priestly taxonomic list through Greco-Arab natural-history (Maimonides' Mishneh Torah commentary cites the same species). The unrelated roots — Heb נ-ש-ם (breathing) and Ar س-ا-م + أ-ب-ر-ص (poison + leprosy) — show the pairing is taxonomic-by-species, not linguistic.",
        "verses": [{"book": "Vayikra", "ch": 11, "v": 30}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "سنبرص",
            "sense": "سنبرص 'a kind of lizard, Lacerta mauritanica' — Blau cites Saadia on Lev 11:30 ('התנשמת' = אלסמברץ per Dirinburg's reading, סמברץ in the Tāj), with Maimonides Mishneh Torah parallel and Löw Tiere 67/73/81-82 transmitting the zoological identification.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Lev 19:36: Just metal-weights (honest measures) -------
    {
        "lemma_ja": "צנגה",
        "variants": ["צנגאת", "וצנגאת", "אלצנגה", "סנגה"],
        "lemma_ar": "صنجة",
        "root": "ص-ن-ج",
        "tier": "gloss",
        "classical_en": "Classical Arabic صنجة (Persian-Aramaic loan) = 'a metal weight used as commercial counterpoise, calibrated standard-weight in a balance'; the technical commercial-measure noun, narrower than the generic 'stone' used in everyday speech.",
        "classical_he": "בערבית הקלאסית صنجة (שאילה פרסית-ארמית) = 'משקולת מתכת המשמשת ככובד בכף-מאזניים, משקל-תקן מכוייל'; שם טכני מסחרי, צר מן 'אבן' הכללי שבשפת היומיום.",
        "saadia_en": "just weights (אבני צדק)",
        "saadia_he": "אַבְנֵי צֶדֶק (משקולות מתכת מכויילות)",
        "mechanism": "Technical commercial-measure pairing: Hebrew אֶבֶן (here 'standard weight' in the שֶׁקֶל-system, not literal stone) gets rendered with the precise Arabic technical term صنجة — a calibrated metal counterpoise. Saadia exposes the underlying commercial reality of the priestly demand for honest scales — the prohibition is about properly-calibrated metal weights, not generic stones. Ibn Janāḥ Shorashim, Tanḥum's Murshid, and al-Fāsī's Jāmiʿ all transmit the equivalence.",
        "verses": [{"book": "Vayikra", "ch": 19, "v": 36}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "صنج",
            "sense": "صنجة 'metal weight used as counterpoise' — Blau cites Saadia on Lev 19:36 ('אבני צדק' = צנגאת עאדלה) with al-Fāsī Jāmiʿ 1:161, Qirqisāni 47, and Friedländer transmitting the equivalence as Saadia's standard JA gloss for biblical weight-stones.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Lev 25:5: Volunteer aftergrowth (Sabbatical year) -----
    {
        "lemma_ja": "כ'לף",
        "variants": ["וכ'לף", "אלכ'לף"],
        "lemma_ar": "خلف",
        "root": "خ-ل-ف",
        "tier": "gloss",
        "classical_en": "Classical Arabic خلف = 'that which follows, successor, after-growth' (especially botanical: secondary crop emerging without sowing); the standard agricultural term for volunteer growth after the main harvest.",
        "classical_he": "בערבית הקלאסית خلف = 'בא בעקבות, יורש, צמיחת-משנה' (במיוחד בהקשר הצומח: יבול משני העולה ללא זריעה); המונח החקלאי הרגיל לצמיחה ספונטנית לאחר הקציר הראשי.",
        "saadia_en": "the aftergrowth (ספיח)",
        "saadia_he": "סְפִיחַ (יבול שעולה מאליו לאחר הקציר)",
        "mechanism": "Specialized agricultural pairing: Hebrew סָפִיחַ ('that which clings/follows', the volunteer crop in fallow-year) gets the precise Arabic agricultural-technical term خلف. Both terms route through a 'follow / come-after' frame, but the Heb root ס-פ-ח (lit. 'to attach') and Ar خ-ل-ف (lit. 'to succeed') are non-cognate. al-Fāsī Jāmiʿ 1:344 explicitly glosses the equivalence with the Sabbatical-year context: ספיח הזרע = כ'לף אלזרע, the unsowed grain that volunteers itself in the seventh-year fallow.",
        "verses": [{"book": "Vayikra", "ch": 25, "v": 5}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "خلف",
            "sense": "خلف 'additional, accidental growth' — Blau cites Saadia on Lev 25:5 ('את ספיח קצירך לא תקצור' = וכ'לף זרעך פלא תחצדה) with the Isa 37:30 cross-attestation and al-Fāsī Jāmiʿ 1:344 transmitting the equivalence.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Lev 26:13: Yoke-burden of slavery ---------------------
    {
        "lemma_ja": "אצר",
        "variants": ["אצרכם", "אלאצר"],
        "lemma_ar": "إصر",
        "root": "ا-ص-ر",
        "tier": "gloss",
        "classical_en": "Classical Arabic إصر (Quranic: Q3:81 'My binding-burden' أَخَذْتُمْ … إِصْرِي) = 'a binding burden, a constraint laid on someone, an oath-binding obligation'; semantically distinct from the agricultural-implement sense Arabic uses for نير ('yoke-of-oxen').",
        "classical_he": "בערבית הקלאסית إصر (קוראני, Q3:81 'בריתי' = إِصْرِي) = 'מעמסה כובלת, מגבלה מוטלת, התחייבות-שבועה'; שונה סמנטית מן المعנה החקלאי שערבית מבטאת ב-نير ('עוֹל של שוורים').",
        "saadia_en": "the binding-burden of your yoke (עֹל)",
        "saadia_he": "מַעֲמַסַת הָעֹל (העוֹל הכובל)",
        "mechanism": "Frame-shift from physical-implement to binding-obligation: Hebrew עֹל ('yoke' as wooden-implement on oxen, here metaphorical for slavery) gets rendered with Arabic إصر, a Quranic-register noun that names the binding-constraint frame rather than the implement frame. Saadia's choice routes the slavery-exodus declaration through an oath-bond semantic field (the burden God released = the binding-pledge dissolved) rather than the agricultural-implement field. Note: the Hebrew 'מטות עלכם' = 'bars of your yoke' becomes 'קראביס אצרכם' = 'the bindings of your burden-bond', preserving the construct + suffixed-possessive shape.",
        "verses": [{"book": "Vayikra", "ch": 26, "v": 13}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "اصر",
            "sense": "إصر 'yoke, burden' — Blau cites Saadia on Lev 26:13 ('ואשבר מטות עלכם' = וכסרת קראביס אצרכם), Deut 28:48 ('עול ברזל על צוארך' = נירא חדיד עלי ענק), and Isa 14:25 ('מעליהם עלו' = ענהם אצרה).",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Lev 26:16: Burning fever (curse-pericope illness) -----
    {
        "lemma_ja": "אלחארה",
        "variants": ["חארה", "ואלחארה", "חמא … אלחארה"],
        "lemma_ar": "حارة",
        "root": "ح-ر-ر",
        "tier": "gloss",
        "classical_en": "Classical Arabic حارة (fem. of حارّ 'hot') = 'the hot one' — a deadjectival noun used elliptically for 'fever' (الحمى الحارة 'the hot fever'); the everyday Arabic term for high-temperature illness, narrower than the technical حمى.",
        "classical_he": "בערבית הקלאסית حارة (נקבת حارّ 'חם') = 'החמה' — שם דה-תוארי המשמש בקיצור ל'קדחת' (الحمى الحارة 'הקדחת החמה'); הביטוי הערבי של היומיום למחלת חום, צר מן حمى הטכני.",
        "saadia_en": "the burning fever (קדחת)",
        "saadia_he": "הַקַּדַּחַת (חום-גוף בוער)",
        "mechanism": "Register-shift toward everyday illness-terminology: Hebrew קַדַּחַת ('burning, fever' from the root ק-ד-ח 'to burn, kindle') gets rendered with the matching everyday Arabic deadjectival noun الحارة 'the hot one' — preserving the heat-of-fever frame across roots. Saadia pairs it with אלסל ('the consumption') for Heb שַׁחֶפֶת, building a two-illness pair in the curses-pericope. The choice keeps the everyday-illness register rather than reaching for a technical medical term like سل or حمى مطبقة.",
        "verses": [{"book": "Vayikra", "ch": 26, "v": 16}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "حرر",
            "sense": "حارة 'fever' — Blau cites Saadia on Lev 26:16 ('את השחפת ואת הקדחת' = מן חמא אלסל ואלחארה) and Deut 28:22, with the deadjectival noun functioning as the everyday word for the high-temperature illness.",
            "relation": "direct",
        },
    },

    # ====================================================================
    # NOTE — 5 net-new
    # ====================================================================

    # ---- NOTE — Lev 7:18 / 19:7: Refuse-offering as Arabic superlative -
    {
        "lemma_ja": "אכ'ס",
        "variants": ["כאלאכ'ס", "אלאכ'ס"],
        "lemma_ar": "أخس",
        "root": "خ-س-س",
        "tier": "note",
        "classical_en": "Classical Arabic أخسّ ('the basest, the most despicable') is the elative form of خسيس 'base, contemptible'; the noun-use as a substantive ('the worst-thing') is post-classical and specifically Saadia-Karaite registered, rejected from the standard masāʾir lexicon.",
        "classical_he": "בערבית הקלאסית أخسّ ('הנבזה ביותר, הנקלה ביותר') הוא תואר-יתרון של خسيس 'נקלה, בזוי'; השימוש בו כשם עצם ('הנקלה-ביותר') הוא בתר-קלסי, ייחודי לרס\"ג ולקראים, ונדחה מן המילון הסטנדרטי.",
        "saadia_en": "a refuse-thing (פִּגּוּל), 'the worst-of-things'",
        "saadia_he": "פִּגּוּל ('הנקלה ביותר')",
        "mechanism": "Semantic-surprise via grammatical reframe: Hebrew פִּגּוּל is a sacrificial-technical noun for 'refuse-meat past its ritual window' (root פ-ג-ל). Saadia renders it not with a noun but with the Arabic ELATIVE substantive כאלאכ'ס ('like-the-worst-of-things'), forcing the priestly classification into a comparative-superlative frame. Heb fixed-category noun → Ar movable-grammatical-judgment. Blau notes the Tāj alternative כאללאיס ('like-the-non-thing'), with Ibn Janāḥ Shorashim 561:25 transmitting both readings. The Form-V elaboration also appears at Num 18:27 ('refuse-fat / chelev pigul').",
        "verses": [
            {"book": "Vayikra", "ch": 7, "v": 18},
            {"book": "Vayikra", "ch": 19, "v": 7},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "خسس",
            "sense": "أخس 'refuse, abomination' — Blau cites Saadia on Lev 19:7 ('פגול הוא' = פהו כאלאכ'ס) and Num 18:27 (Dirinburg variant), with Ibn Janāḥ Shorashim 561 transmitting the elative-substantive substitution.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Lev 4:3, 4:24, 7:7, 16:6, 16:25: Sin-offering = purity-offering
    {
        "lemma_ja": "ד'כוה",
        "variants": ["דכוה", "אלד'כוה", "אלדכוה", "אלד'כואת", "ד'כואת"],
        "lemma_ar": "ذكوة",
        "root": "ذ-ك-و",
        "tier": "note",
        "classical_en": "Classical Arabic ذكوة (plural ذكوات) = 'purity, purification, the act of becoming pure' (cognate with زكاة 'alms-purification'); never used in classical Arabic for any sacrificial category — Saadia coins the noun as a fixed cultic-technical term.",
        "classical_he": "בערבית הקלאסית ذكوة (רבים ذكوات) = 'טוהר, היטהרות, מעשה הזיכוך' (קוגנט زكاة 'צדקה-זיכוך'); אינה משמשת בערבית הקלסית בשום הקשר זיבוחי — רס\"ג ממציא את הצורה כמונח טכני-פולחני קבוע.",
        "saadia_en": "the sin-offering (חַטָּאת), lit. 'the purification-offering'",
        "saadia_he": "חַטָּאת (כפשוטו: 'קרבן הטוהרה')",
        "mechanism": "Theological reframe via noun-substitution: Hebrew חַטָּאת for the sin-offering is itself a contested name — the noun literally means 'sin/transgression' (root ח-ט-א), but in priestly usage it refers to the OFFERING that REMOVES sin. Saadia takes the second sense and lexicalizes it directly with ذكوة, naming the offering by its EFFECT (purification) rather than its CAUSE (sin). The shift erases the paradox in the Hebrew nomenclature and aligns with the broader Quranic-Arabic z-k-w family of purification-language (زكاة 'alms-purification'). This is Saadia's invariant rendering across the offering pericopes — appears at Lev 4:3 (priestly sin-offering), 4:24 (chieftain's), 5:6 (commoner's), 7:7, 7:37, 14:19/22 (leper-purification), 16:6/11 (Yom Kippur high priest), 16:15/25 (Yom Kippur goat). Ḥafetz 139:9 + 142:18 transmits the pairing.",
        "verses": [
            {"book": "Vayikra", "ch": 4, "v": 3},
            {"book": "Vayikra", "ch": 4, "v": 24},
            {"book": "Vayikra", "ch": 7, "v": 7},
            {"book": "Vayikra", "ch": 16, "v": 6},
            {"book": "Vayikra", "ch": 16, "v": 25},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "ذكو",
            "sense": "ذكوة (plural ذكوات) 'sin-offering' — Blau cites Saadia on Lev 4:24 ('חטאת הוא' = כד'אך מא יכון ד'כוה) and 16:25 ('חלב החטאת' = שחום אלד'כואת), with Ḥafetz 139:9 + 142:18 transmitting Saadia's invariant rendering of biblical חטאת with this purification-frame noun.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Lev 5:6, 14:19, 16:6/11/16/30/32: Atonement = seeking-forgiveness
    {
        "lemma_ja": "יסתג'פר",
        "variants": ["ויסתג'פר", "אסתג'פר", "ליסתג'פר", "פיסתג'פר", "אסתג'פאר"],
        "lemma_ar": "يستغفر",
        "root": "غ-ف-ر",
        "tier": "note",
        "classical_en": "Classical Arabic Form X استغفر = 'to seek forgiveness, ask for pardon' (root غ-ف-ر 'to cover, to forgive'); a quintessentially relational-religious verb in Arabic, describing the supplicant's act of pleading for divine pardon. Never used in classical Arabic to render ritual-mechanical atonement.",
        "classical_he": "בערבית הקלאסית בניין X استغفر = 'לבקש סליחה, להתחנן למחילה' (משורש غ-ف-ر 'לכסות, לסלוח'); פועל יחסי-דתי מובהק בערבית, המתאר את פעולת המתחנן המבקש מן האל סליחה. לעולם אינו משמש בערבית קלסית לתיאור כיפור פולחני-מנגנוני.",
        "saadia_en": "he atones / he seeks forgiveness (כפר)",
        "saadia_he": "מְכַפֵּר (\"מבקש סליחה\")",
        "mechanism": "Theological reframe from ritual-mechanism to relational-supplication: Hebrew כָּפַר (root כ-פ-ר 'to cover') is the priestly verb for ritual atonement — the offering MECHANICALLY covers/wipes the sin from the altar. Saadia renders it with Form X استغفر — 'to seek forgiveness' — converting the mechanical-cultic action into a relational-supplicative one. The priest no longer COVERS the sin; he PLEADS for its forgiveness. This is Saadia's invariant choice across the entire atonement system: appears at Lev 4:26/31, 5:6, 5:10, 5:13, 5:16, 5:18, 5:26, 14:19/20/21, 14:31, 16:6/10/11/16/17/18/20/24/27/30/32/33/34, 23:28 — every priestly atonement verse. The choice subordinates the priestly system to the Karaite-friendly framework where divine forgiveness is the operative act, not blood-manipulation. Blau notes the propagation to Ḥibbur Yāfe 148:1.",
        "verses": [
            {"book": "Vayikra", "ch": 5, "v": 6},
            {"book": "Vayikra", "ch": 14, "v": 19},
            {"book": "Vayikra", "ch": 16, "v": 6},
            {"book": "Vayikra", "ch": 16, "v": 16},
            {"book": "Vayikra", "ch": 16, "v": 30},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "غفر",
            "sense": "غفر (Form X استغفر) 'to forgive, to seek forgiveness' — Blau cites Saadia on Lev 16:6 ('וכפר בעדו ובעד ביתו' = ויסתג'פר ענה וען אלה) with the Ex 29:36 parallel and Ḥibbur Yāfe 148:1 transmitting the forgiveness-supplication frame for biblical כפר.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Lev 14:34, 25:13/24/41, 27:16: Land-possession = sound-similar Arabic root
    {
        "lemma_ja": "חוז",
        "variants": ["חוזא", "חוזכם", "חוזה", "אלחוז"],
        "lemma_ar": "حوز",
        "root": "ح-و-ز",
        "tier": "note",
        "classical_en": "Classical Arabic حوز (root ح-و-ز) = 'to gather, to encompass, to take possession of, to enclose within one's domain'; semantically near to but ETYMOLOGICALLY UNRELATED to Hebrew א-ח-ז ('to grasp, to hold'). The two roots have non-overlapping cognate sets (Heb ا-خ-ذ; Ar ح-و-ز).",
        "classical_he": "בערבית הקלאסית حوز (משורש ح-و-ز) = 'לאסוף, להקיף, לקחת בעלות, לכלוא בתוך תחום'; קרוב סמנטית אך לא ממש קוגנט עברית א-ח-ז ('לאחוז, להחזיק'). שני השרשים מקבילים בקבוצות-קוגנט שונות (עברית א-ח-ז ↔ ערבית ا-خ-ذ; ערבית ح-و-ز עומדת בפני עצמה).",
        "saadia_en": "(land-)possession (אֲחֻזָּה)",
        "saadia_he": "אֲחֻזָּה",
        "mechanism": "Pseudo-cognate substitution licensed by sound-similarity: Hebrew אֲחֻזָּה ('possession of land') derives from א-ח-ז ('to grasp') and would normally pair with Arabic أخذ ('to take') — but Saadia routes the entire Vayikra-Bemidbar land-tenure lexicon through a non-cognate look-alike, حوز ('to encompass'). Blau explicitly diagnoses this as a sound-similarity calque, not an etymological pairing: Saadia regularly substitutes ح-و-ز for א-ח-ז 'in spite of the etymological mismatch, because of the phonological convergence' (Blau body excerpt 17381). The pairing surfaces across the leper-house pericope (Lev 14:34), the jubilee-return pericope (Lev 25:13, 24, 28, 41), and the dedicated-field pericope (Lev 27:16). Pattern propagates forward into Sini 'lekhi' = 'אלכ'ל' [false-cognate].",
        "verses": [
            {"book": "Vayikra", "ch": 14, "v": 34},
            {"book": "Vayikra", "ch": 25, "v": 13},
            {"book": "Vayikra", "ch": 25, "v": 41},
            {"book": "Vayikra", "ch": 27, "v": 16},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "حوز",
            "sense": "حوز 'possession, that which is enclosed/grasped' — Blau cites Saadia's regular practice of translating biblical אחזה with حوز 'because of sound-similarity', e.g. Lev 14:34 ('ארץ אחזתכם' = ארץ' חוזכם), with the Ps 139:10, Eccles, and Sini parallels.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Lev 10:10, 21:7, 21:9: Profane semantic-field (noun + verb cluster)
    {
        "lemma_ja": "בד'ל",
        "variants": ["אלבד'ל", "ואלבד'ל", "מבד'ולה", "תבד'לת", "אלבדל"],
        "lemma_ar": "بذل",
        "root": "ب-ذ-ل",
        "tier": "note",
        "classical_en": "Classical Arabic بذل (root ب-ذ-ل) = 'to spend freely, to expend, to give without reserve' (positive sense); the derived negative sense 'to disgrace oneself by squandering one's honor, to profane' becomes operative in Form-V تبذّل ('to be brought down, to be made common'). Never the classical-Arabic choice for sacrilege-language.",
        "classical_he": "בערבית הקלאסית بذل (משורש ب-ذ-ل) = 'להוציא בנדיבות, לכלות, להעניק ללא חשבון' (משמעות חיובית); המשמעות השלילית הנגזרת 'לבזות את עצמו על-ידי בזבוז כבודו, לחלל' מתממשת בבניין V تبذّل ('להתגנות, להתבזות'). אינה בחירה ערבית קלסית לשפת חילול-קודש.",
        "saadia_en": "the profane / to be profaned (חַל / חִלֵּל / הִתְחַלֵּל)",
        "saadia_he": "חוֹל / לְחַלֵּל / לְהִתְחַלֵּל",
        "mechanism": "Semantic-field calque across noun+verb forms: Hebrew root ח-ל-ל ('to profane, to make common' — antonym of קָדַשׁ) gets a unified Saadian treatment via Arabic root ب-ذ-ل ('to spend without reserve'). The semantic bridge is the squandering-of-value frame: Heb 'to make profane' becomes Ar 'to expend, to give away cheaply' — both treating sanctity as an attribute that can be DEPLETED through misuse. Surfaces across noun + passive participle + Form-V verb: Lev 10:10 ('להבדיל בין הקדש ובין החל' = ולתפצלו בין אלקדס ואלבד'ל) renders the priestly-substantive 'profane' as noun; Lev 21:7 ('ואשה גרושה … חללה' = ובאמראה … ומבד'ולה) renders the passive participle 'a profaned-woman' as Form I/II ism mafʿūl; Lev 21:9 ('כי תחל לזנות' = תבד'לת פפגרת) renders the verb 'to profane oneself' as Form V. The unified treatment frames the priesthood's sanctity as something subject to financial-style depletion.",
        "verses": [
            {"book": "Vayikra", "ch": 10, "v": 10},
            {"book": "Vayikra", "ch": 21, "v": 7},
            {"book": "Vayikra", "ch": 21, "v": 9},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "بذل",
            "sense": "بذل (noun + Form V verb) 'profane / to be profaned' — Blau cites Saadia on Lev 10:10 ('החל' = אלבד'ל), Lev 21:7 ('וחללה' = ומבד'ולה), Lev 21:9 ('תחל' = תבד'לת), with the squandering-frame propagated across the Holiness-Code priestly-disqualification system.",
            "relation": "direct",
        },
    },
]


# Promote-in-place patch for شحمة (Shemot Ex 29:20 → extended to 5 Vayikra
# attestations). Mirrors the נקל precedent from Batch 2.
PROMOTE_IN_PLACE = {
    "lemma_ja": "שחמה'",  # current key in tafsir-divergence.json
    "extend_verses": [
        {"book": "Vayikra", "ch": 8, "v": 23},
        {"book": "Vayikra", "ch": 14, "v": 14},
        {"book": "Vayikra", "ch": 14, "v": 17},
        {"book": "Vayikra", "ch": 14, "v": 25},
        {"book": "Vayikra", "ch": 14, "v": 28},
    ],
    "mechanism_rewrite": (
        "Idiom-anchored pairing across consecration + purification rituals: "
        "Saadia renders Hebrew תְּנוּךְ ('lobe, tip') with the standard "
        "Arabic anatomical idiom شحمة الأذن — a semantic-field jump (Heb "
        "'projection/tip' → Ar 'fatty pad') licensed by the fixed Arabic "
        "compound. The pairing surfaces across two ritual systems that "
        "share the right-ear / right-thumb / right-toe blood-application "
        "structure: the consecration-of-priests at Ex 29:20 (Aaron + sons), "
        "and the leper-purification pericope at Lev 8:23 (priestly-"
        "installation continuation), Lev 14:14, 14:17, 14:25, 14:28 (the "
        "metsora). Saadia uses the same fixed idiom שחמה' אד'ן across "
        "both pericopes, making the Aaron-consecration and the metsora-"
        "purification syntactically parallel in JA where the Hebrew "
        "already parallels them lexically (the same תְּנוּךְ-בֹּהֶן triad)."
    ),
    "blau_dict_sense_rewrite": (
        "شحمة 'earlobe' (idiom شحمة الأذن) — Blau cites Saadia on Ex 29:20 "
        "('על תנוך אזן אהרן … ועל תנוך אזן בניו הימנית' = עלי שחמה' אד'ן "
        "הרון … ועלי' שחמאת אד'אן בניה), with plurals أشحام / شحمات for "
        "the multi-priest construction. The same fixed idiom propagates "
        "across the Vayikra ritual cluster: Lev 8:23 (priestly-"
        "consecration completion), 14:14 / 14:17 / 14:25 / 14:28 (leper-"
        "purification right-ear/thumb/toe blood-application)."
    ),
}


# Skip / borderline triage for the Vayikra Batch 1 window. Writes to a
# fresh "vayikra" namespace; idempotent on blau_id.
BATCH1_DEFERRED = {
    "skip": [
        {
            "blau_id": 13781,
            "root_ar": "أداء",
            "verse_hint": "(metalanguage on Lev 6:6)",
            "reason": "Blau body is meta-discussion of Dirinburg's reading of אזא as 'yield/crop' vs Blau's own counter-reading ('debt'); no verse-anchored Vayikra surface in the Cairo baseline. Defer to translation-theory metalanguage pool.",
        },
        {
            "blau_id": 14560,
            "root_ar": "جسس",
            "verse_hint": "(Saadia's Form II from Heb לְמַשֵּׁשׁ)",
            "reason": "Blau body explicitly ARGUES AGAINST the Hebrew-influence hypothesis ('the fact that Saadia brings it from non-Jewish sources weakens the hypothesis that Hebrew גישש influenced the Form-II usage'). Not divergence-grade.",
        },
        {
            "blau_id": 14655,
            "root_ar": "جوز",
            "verse_hint": "(metalanguage — Karaite/Maimonidean usage)",
            "reason": "Pure metalanguage about Saadia's syntactic-modal verb 'to be plausible' — not anchored to a Vayikra verse. Defer.",
        },
        {
            "blau_id": 14870,
            "root_ar": "تحصيل",
            "verse_hint": "(metalanguage — Sefer Yetzirah/Talmudic)",
            "reason": "Metalanguage on Saadia's translation-theory term 'exact counting'; no Vayikra verse anchor. Defer.",
        },
        {
            "blau_id": 15266,
            "root_ar": "خلة",
            "verse_hint": "(cross-book metalanguage)",
            "reason": "Saadia's pronoun-equivalent particle for 'matter/case'; mainly attested in Bereshit + Mishlei. Vayikra mention is incidental. Defer.",
        },
        {
            "blau_id": 15559,
            "root_ar": "دنو",
            "verse_hint": "(metalanguage on Maimonides + Aramaic-loan discussion)",
            "reason": "Blau body is about Saadia's Aramaic-influenced verb 'to draw near, to touch'; not anchored to a specific Vayikra verse. Defer to broader cross-book pass.",
        },
        {
            "blau_id": 15787,
            "root_ar": "رشم",
            "verse_hint": "(no clear Vayikra anchor — possibly Lev 19:28 קעקע)",
            "reason": "Body discusses 'sign, mark, tattoo' across Maimonides, Tanḥum; cited 'sign' surface but no clean Vayikra verse-anchor in the Blau body. Defer pending re-mining.",
        },
        {
            "blau_id": 15824,
            "root_ar": "رفق",
            "verse_hint": "Lev 25:3 (overlaps with 15954 زبر)",
            "reason": "Saadia's Aramaic-influenced 'to prune' for Heb זמר at Lev 25:3 — but the Blau body shows competing readings (Saadia uses both رفق at Isa 5:6 and زبر at Lev 25:3). Manuscript-variant ambiguity; defer pending recension-survey.",
        },
        {
            "blau_id": 16131,
            "root_ar": "ستر",
            "verse_hint": "(metalanguage on marriage-gifts)",
            "reason": "Blau's primary attestations are in Maimonides + Geniza marriage-document Arabic for 'wedding-gifts'; not anchored to a Vayikra verse despite the lemma being in the candidate pool. Defer.",
        },
        {
            "blau_id": 16407,
            "root_ar": "سوغ",
            "verse_hint": "Lev 22:21 (unclear)",
            "reason": "Blau body explicitly notes 'I do not understand the connection of this term to הבדלה והפרשה' at Lev 22:21 — i.e., Blau himself flags the cited divergence as obscure. Defer pending tafsir-side analysis.",
        },
        {
            "blau_id": 16820,
            "root_ar": "مصففة",
            "verse_hint": "Lev 24:7 מערכת",
            "reason": "Blau quotes 'ושים על המערכת לבנה אלמצפפ' לבאנא' but the Cairo 2019 baseline uses 'אגעל עלי כל צף לבאנא' (with masc. צף not fem. מצפפ). Recension difference — Blau's text is closer to Dirinburg's edition than to Cairo 2019. Defer pending edition-comparison.",
        },
        {
            "blau_id": 16869,
            "root_ar": "صمغ",
            "verse_hint": "Lev 16:12 קטרת ספים",
            "reason": "Pure consonantal cognate — Heb צ-מ-ג and Ar ص-م-غ both = 'resin, fragrant exudate'. No tier-promoting divergence to display.",
        },
        {
            "blau_id": 17953,
            "root_ar": "غريبة / غويب / غرابيب",
            "verse_hint": "Lev 11:15 עורב",
            "reason": "Heb עורב ↔ Ar غراب is a direct etymological cognate (both o/g-r-b roots, both 'raven/crow'). Saadia's specific spelling غرابيب is a register-variant, not a divergence. Skip.",
        },
        {
            "blau_id": 18463,
            "root_ar": "قدس",
            "verse_hint": "Lev 27:14 והקדיש",
            "reason": "Direct cognate — Heb ק-ד-ש ↔ Ar ق-د-س both = 'holy, sanctified'. The cluster head + 5 derivative-form rows (18464-18468) all reflect the same cognate-direct equivalence. No divergence to display.",
        },
        {
            "blau_id": 18995,
            "root_ar": "كل family (كل / كلل / كلول / كلما)",
            "verse_hint": "Lev 25:14 אל תונו איש את אחיו",
            "reason": "6-row cluster on the quantifier-particle كل rendering Heb אִישׁ (indefinite). Grammar-particle territory, not technical-vocabulary divergence. Defer (would need a separate grammar-particle methodology to ship).",
        },
        {
            "blau_id": 19861,
            "root_ar": "نفذ (cluster 11 rows)",
            "verse_hint": "Lev 26:30 והשמדתי",
            "reason": "The cited verse (Lev 26:30) is MISSING from data/tafsir-vayikra-26.json (chapter file jumps from v.29 to v.31). No baseline JA surface available to verify Saadia's אנפד reading. Defer pending Cairo edition-fill.",
        },
        {
            "blau_id": 20398,
            "root_ar": "وليمة / ولي",
            "verse_hint": "Lev 19:4 אל תפנו אל",
            "reason": "Cluster of 2 rows on Ar ولى ('to turn away/toward'). Heb פנה אל ↔ Ar ولى إلى is a fairly direct semantic-cognate pairing — both 'turn toward'. The Form-II surface (לא תולו אלי) is interesting but borderline-cognate, not tier-promoting. Defer.",
        },
    ],
    "borderline": [
        {
            "blau_id": 17407,
            "root_ar": "خمع",
            "verse_hint": "Lev 21:18 שרוע",
            "open_question": "Saadia renders Heb שָׂרוּעַ (a vague priestly-disqualifying physical defect — 'distorted, splayed') with the precise Arabic medical term خمع ('dislocated hip'). Surface (ואלכ'אמע) and Hebrew anchor (שרוע) both verified. Tier-grade NOTE candidate but cut from this batch's 5-NOTE cap; promote in Batch 2 alongside the priestly-disqualification cluster (Lev 21:18-23 has 6 more body-defect terms worth a coordinated pass).",
        },
        {
            "blau_id": 18594,
            "root_ar": "قصبة",
            "verse_hint": "Lev 1:8 פדר",
            "open_question": "Saadia renders Heb פֶּדֶר ('suet/caul-fat over kidneys') with Ar قصبة ('reed, then metonymically interior-of-body, viscera'). Surface (אלקצבה) and Hebrew anchor (הפדר) both verified — strong NOTE-grade body-cavity metonymic extension. Cut from this batch's 5-NOTE cap; promote in Batch 2 alongside other sacrificial-anatomy entries.",
        },
        {
            "blau_id": 19142,
            "root_ar": "لج",
            "verse_hint": "Lev 14:10 ולג שמן",
            "open_question": "Saadia retains Hebrew לֹג ('a liquid measure') as-is in JA — לג דהן — rather than translating to an Arabic measure-equivalent. Heb-loanword retention for technical-cultic measures is a NOTE-grade phenomenon (parallels the Persian-loan מרזבאן shipped in Shemot Batch 2). Cut from this batch's 5-NOTE cap; promote in Batch 2 as a measure-vocabulary entry.",
        },
        {
            "blau_id": 19427,
            "root_ar": "مسوحية",
            "verse_hint": "Lev 8:2, 8:10 שמן המשחה",
            "open_question": "Saadia renders Heb שֶׁמֶן הַמִּשְׁחָה ('oil of anointing') with דהן אלמסוחייה — using the Aramaic-Syriac-influenced abstract-noun form مسوحية rather than standard Arabic مسحة. Strong calque-style NOTE candidate. Cut from this batch's 5-NOTE cap; promote in Batch 2 alongside Mishkan-vocabulary cross-references.",
        },
    ],
    "_cluster_dupes_logged": [
        "13781 (أداء — single head, no cluster)",
        "17302≈17303≈17304≈17305≈17306≈17307 (ثلول/فغلول cluster, 6 rows on Lev 13:38 יבלת — manuscript-variant only)",
        "17381≈17382≈17383≈17384 (حوز/إحازة/حيز/حائز cluster, 4 rows; head 17381 shipping)",
        "17407≈17408 (خمع/خمن cluster, 2 rows; deferred to borderline)",
        "17953≈17954≈17955 (غريبة/مغرب/غويب cluster, 3 rows)",
        "17999≈18000 (غفر/غفارة cluster, 2 rows; head 17999 shipping)",
        "18190≈18191 (فركة/فريك cluster, 2 rows; head 18190 shipping)",
        "18378≈18379 (فيضة/فائض cluster, 2 rows; cut at-cap)",
        "18463≈18464≈18465≈18466≈18467≈18468 (قدس family cluster, 6 rows — cognate, skipped)",
        "18995≈18996≈18997≈18998≈18999≈19000 (كل family cluster, 6 rows — grammar-particle, skipped)",
        "19427≈19428 (مساحة/مسوحية cluster, 2 rows; deferred to borderline)",
        "19861≈19862≈19863≈19864≈19865≈19866≈19867≈19868≈19869≈19870≈19871 (نفذ family cluster, 11 rows — Lev 26:30 missing in baseline)",
        "20398≈20399 (وليمة/ولي cluster, 2 rows — cognate, skipped)",
    ],
}


def _patch_promote_in_place(payload: dict) -> dict | None:
    """Promote-in-place patch for the existing شحمة entry: extend the
    Shemot Ex 29:20-only entry with 5 Vayikra attestations across the
    consecration-of-priests + leper-purification rituals. Returns a
    small summary if the patch applied, else None.
    """
    target_lemma = PROMOTE_IN_PLACE["lemma_ja"]
    for entry in payload["entries"]:
        if entry.get("lemma_ja") == target_lemma:
            existing = {(v["book"], v["ch"], v["v"]) for v in entry.get("verses", [])}
            added = []
            for v in PROMOTE_IN_PLACE["extend_verses"]:
                key = (v["book"], v["ch"], v["v"])
                if key not in existing:
                    entry["verses"].append(v)
                    existing.add(key)
                    added.append(f"{v['book']} {v['ch']}:{v['v']}")
            if added:
                entry["mechanism"] = PROMOTE_IN_PLACE["mechanism_rewrite"]
                entry["blau_dict"]["sense"] = PROMOTE_IN_PLACE["blau_dict_sense_rewrite"]
                return {"lemma": target_lemma, "verses_added": added, "total_verses_now": len(entry["verses"])}
            return {"lemma": target_lemma, "verses_added": [], "note": "all verses already present (idempotent re-run)"}
    return None


def _update_deferred(deferred_path: pathlib.Path) -> dict:
    """Write Vayikra Batch 1 entries into data/_blau_saadia_deferred.json
    under a fresh "vayikra" namespace (idempotent on blau_id).
    """
    payload = json.loads(deferred_path.read_text())
    vy = payload.setdefault("vayikra", {})

    added = {"skip": 0, "borderline": 0, "phase3_r2_candidates": 0, "cross_book_dupes": 0}
    for bucket, new_items in BATCH1_DEFERRED.items():
        if bucket.startswith("_"):
            continue
        existing = vy.setdefault(bucket, [])
        existing_ids = {it.get("blau_id") for it in existing if isinstance(it, dict)}
        for item in new_items:
            if item.get("blau_id") in existing_ids:
                continue
            existing.append(item)
            existing_ids.add(item.get("blau_id"))
            added[bucket] = added.get(bucket, 0) + 1

    cluster_log = vy.setdefault("_cluster_dupes_logged", [])
    if isinstance(cluster_log, list):
        for line in BATCH1_DEFERRED["_cluster_dupes_logged"]:
            if line not in cluster_log:
                cluster_log.append(line)

    vy.setdefault("_session", "Phase 4 Vayikra Batch 1 (apply_phase4_vayikra_batch1.py)")

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return {"added": added, "vayikra_buckets_now": {k: len(v) if isinstance(v, list) else v for k, v in vy.items()}}


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

    # 1) Promote-in-place patch for شحمة (must run BEFORE append so we don't
    #    accidentally treat the lemma as collision-skip).
    promote_summary = _patch_promote_in_place(payload)

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

    print(f"Promote-in-place: {json.dumps(promote_summary, ensure_ascii=False)}")
    print(f"Added {added} entries to {div_path.name}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")
    print(f"Deferred file summary: {json.dumps(deferred_summary, ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    main()

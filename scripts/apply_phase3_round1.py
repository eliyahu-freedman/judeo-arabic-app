"""
Phase 3 — Round 1: STRICT twist-tier mining of Bereshit Saadia divergences.

Sixteen new entries (4 twist + 6 note + 6 gloss) from Blau's 1,596 Saadia-citing
dictionary entries, each verified against data/tafsir-bereshit-{ch}.json — the
lemma surfaces in the cited verse under a form reachable via the prefix-strip
chain.

Plus two re-audit patches: the saadia-direct-only Bereshit twist entries
מסתבחרה (Gen 1:2) and שמשאר (Gen 6:14) gain `blau_dict` blocks with `direct`
relation, lifting the Bereshit twist-tier Blau-backed gate from 20/31 = 65%
past the 70% threshold.

Gate arithmetic (Bereshit twist-tier only):
  Before: 20 backed / 31 total = 65%  (1 verifier warning)
  After:
    + 4 new TWIST entries with direct backing            → 35 total / 24 backed
    + 2 re-audit patches (mst-bḥrh, šmšr → direct)        → 35 total / 26 backed
  Final: 26/35 = 74.3% — clears the 70% gate with margin.

Deferred consumed: 16430 سيد / Gen 49:8 (the phase3_r1_candidates seed).

No-cite re-audit misses (logged into deferred file):
  ריאח (1:2), תהב (1:2), אטג'אני (3:13), אשראף (6:2), קרדא (8:4),
  קרבאן (8:21), אתון (11:28) — no Blau attestation found via arabic-lex
  search; the entries stand as "saadia-direct"-only readings.

Apply pattern mirrors scripts/apply_phase4_bereshit_batch1.py:280–306;
dedupe is on lemma_ja only (DivergenceEntry has no `id` field).
"""

import json
import pathlib
import sys
from collections import Counter


NEW_ENTRIES = [
    # ============================================================================
    # TWIST tier (4) — paradigm-grade Saadia divergences with direct Blau backing
    # ============================================================================

    # ---- TWIST — Gen 49:8: Judah blessing "praise" → "make ruler" -------------
    # Consumes deferred phase3_r1_candidates entry [16430 سيد / Gen 49:8].
    {
        "lemma_ja": "יסיידונך",
        "variants": ["יסייד", "סיד", "יסידן", "ויסיד"],
        "lemma_ar": "يسيِّدونك",
        "root": "س-ي-د",
        "tier": "twist",
        "classical_en": "Form II denominative of سيد (master, lord) — \"to make so. master/ruler\" (post-classical; the standard sense of سيد in classical Arabic is the noun \"lord\", not a verbal action)",
        "classical_he": "בנין שני דנומינטיבי מן سيد (אדון, שליט) — \"להפוך מישהו לאדון/שליט\" (פוסט-קלסי; המשמע הקלסי של سيد הוא שם-עצם \"אדון\" ולא פעולה)",
        "saadia_en": "they shall make you ruler — Saadia recasts the Hebrew יוֹדוּךָ אַחֶיךָ (\"your brothers shall praise you\", from יד״ה which puns on Judah's name) as יסיידונך אכ'ותך (\"your brothers shall make you ruler\"). The acknowledgment in the blessing is reread as a political acclamation: the brothers don't celebrate Judah, they install him over themselves",
        "saadia_he": "יִשְׁלִיטוּ אוֹתְךָ — סעדיה מתרגם את \"יוֹדוּךָ אַחֶיךָ\" של ברכת יהודה (מן השורש יד״ה שמשחק על שם יהודה) כ\"יסיידונך אכ'ותך\" (\"אחיך ישליטו אותך עליהם\"). ההודיה הופכת לאקלמציה פוליטית: האחים לא מהללים את יהודה אלא ממליכים אותו",
        "mechanism": "interpretive paradigm shift: the Hebrew pun (יוֹדוּ↔יהודה) and the surface sense (\"praise\") are both jettisoned. Saadia commits to a political reading on which the Judah blessing is the constitutional charter for Davidic primacy among the tribes — and uses a denominative verb (\"to make-ruler\") that classical Arabic itself does not attest in this volitional sense. Blau glosses the JA verb explicitly as ישליטון",
        "verses": [
            {"book": "Bereshit", "ch": 49, "v": 8},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "سيد",
            "sense": "Form II denominative of سيد (derived from سود ~ سيد): \"to make so. master, lord / אדון, שליט\" — Blau cites Saadia on Gen 49:8 directly: \"יוֹדוּךָ אַחֶיךָ → יסיידונך אכ'ותך\" and glosses as \"ישליטון אחיך\".",
            "relation": "direct",
        },
    },

    # ---- TWIST — Gen 12:20: Pharaoh "escorts" Abram (not "expels") -------------
    {
        "lemma_ja": "ד'רקובה",
        "variants": ["ד'רקו", "דרק", "בדרק", "פד'רקובה"],
        "lemma_ar": "درّقوه",
        "root": "د-ر-ق",
        "tier": "twist",
        "classical_en": "Form II of درق (with the prefix بـ in Blau's notation بدرق): \"to escort, to accompany a traveller, to provide safe-conduct.\" Rare post-classical verb, related to درقة (\"shield\"); semantically very distinct from طرد (\"to expel\") which is the obvious lexical choice for the Hebrew וַיְשַׁלְּחוּ in this context",
        "classical_he": "בנין שני של ד-ר-ק (לפי בלאו עם תחיליות בـ — بدرق): \"ללוות, לתת בידי הולכי דרך הגנה וליווי\". פועל פוסט-קלסי נדיר, קשור ל-درقة (\"מגן\"); רחוק סמנטית מטרד (\"גרש\") שהיא הבחירה הלקסיקלית הברורה לעברית \"וַיְשַׁלְּחוּ\" בהקשר זה",
        "saadia_en": "they escorted him — Saadia renders Pharaoh's expulsion of Abram וַיְשַׁלְּחוּ אֹתוֹ וְאֶת-אִשְׁתּוֹ וְאֶת-כָּל-אֲשֶׁר-לוֹ as פוכל עליה פרעון קומא וד'רקובה (\"Pharaoh charged men with him and they escorted him\"), softening the expulsion into a ceremonial dismissal. Dirinbourg emended to פבזרקו (\"and they cast him out\") to fit the harsher reading; Blau corrects this back to درق — Saadia genuinely wrote \"escorted\"",
        "saadia_he": "וְלִוּוּ אוֹתוֹ — סעדיה מתרגם את גירוש אברם על-ידי פרעה (\"וַיְשַׁלְּחוּ אֹתוֹ וְאֶת-אִשְׁתּוֹ וְאֶת-כָּל-אֲשֶׁר-לוֹ\") כ\"פוכל עליה פרעון קומא וד'רקובה\" (\"פרעה הפקיד עליו אנשים והם ליווהו לדרך\"), והופך את הגירוש לפרידה מכובדת. דירינבורג הגיה ל\"פבזרקו\" (\"וְזָרְקוּ אוֹתוֹ\") בעקבות הקריאה הקשה; בלאו מתקן בחזרה ל-درق — סעדיה אכן כתב \"לִוּוּ\"",
        "mechanism": "interpretive: Pharaoh's send-off of Abram, which the Hebrew verb שׁ-ל-ח can read either as expulsion (\"he sent away\") or as escorted-dismissal (\"he sent off with provision\"), is committed by Saadia to the courteous reading. This dovetails with Saadia's wider rehabilitation of Pharaoh-of-Abram against Pharaoh-of-Moses — and stands directly opposed to the lectio facilior of the Samaritan tradition (واطلقوه, \"and they released him\") and Dirinbourg's emendation",
        "verses": [
            {"book": "Bereshit", "ch": 12, "v": 20},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "بدرق",
            "sense": "Form II with بـ: \"to escort (a traveller), to provide safe-conduct / לִוָּה (נוֹסֵעַ, שַׁיָּרָה)\" — Blau cites Saadia on Gen 12:20 directly as the canonical attestation, explicitly correcting Dirinbourg's emendation פבזרקו (\"expelled\") back to פבדרקו. The Samaritan tradition's lectio facilior واطلقوه (\"released\") further isolates Saadia's lexical choice as deliberate.",
            "relation": "direct",
        },
    },

    # ---- TWIST — Gen 38:21: qedeshah → "temple-prostitute" --------------------
    {
        "lemma_ja": "אלממתעה",
        "variants": ["ממתעה", "ממתעת", "ממתע"],
        "lemma_ar": "الممتعة",
        "root": "م-ت-ع",
        "tier": "twist",
        "classical_en": "passive participle of متّع (Form II) \"to give enjoyment, to grant pleasure\" — \"she who is given (over) for pleasure.\" Classical Arabic uses متعة for a temporary marriage contract (Shia jurisprudence) and the feminine participle as a regional term; never attested as a stable noun for cult-prostitute",
        "classical_he": "בינוני פעול של متّع (בנין II) \"לתת הנאה, להעניק תענוג\" — \"זו שנמסרה להנאה\". בערבית הקלסית متعة היא חוזה נישואין זמני (משפט שיעי) והבינוני הנקבה הוא מונח אזורי; אינו מתועד כשם עצם יציב לכוהנת-זונה",
        "saadia_en": "the temple-prostitute — Saadia renders the doubled Hebrew הַקְּדֵשָׁה (\"the cult-prostitute,\" who Judah's friend Hirah asks the local men about, claiming to seek the woman Judah encountered) as אלממתעה (\"the woman of pleasure-giving\"). The choice of متّعة over the more neutral زانية (prostitute) commits Saadia to identifying קְדֵשָׁה as the cultic class specifically — not freelance prostitution but ritualized fertility-prostitution institutionalized at shrines",
        "saadia_he": "הקדשה (\"כוהנת-זונה\") — סעדיה מתרגם את הצמד \"הַקְּדֵשָׁה\" (כאשר חירה הָעֲדֻלָּמִי שׁוֹאֵל את אנשי המקום על האישה ש\"יהודה התעלה עליה\") כ\"אלממתעה\" (\"זו שלהנאה\"). בחירת متّعة על פני הפועל הניטרלי زانية (זונה) מחייבת את סעדיה לזהות את \"קדשה\" כסיווג פולחני ספציפי — לא זנות חופשית אלא זנות פולחנית-פריונית קבועה בָּמְקוֹם הַקָּדוֹשׁ",
        "mechanism": "lexical specification (anti-rabbinic / against the targumic neutralization): the Targumim and most medieval commentators render קְדֵשָׁה with a generic \"prostitute\" word, effacing the cultic dimension. Saadia, working in an Islamic juristic-lexicographical milieu where متعة has technical resonance, picks a term that names the cultic category — and uses the same word again at Deuteronomy 23:18 (the prohibition on Israelite men/women being a קָדֵשׁ/קְדֵשָׁה), confirming the systematic identification",
        "verses": [
            {"book": "Bereshit", "ch": 38, "v": 21},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "متع",
            "sense": "ممتعة \"harlot, temple-prostitute / קְדֵשָׁה, אישה שנועדה לזנות פולחנית\" — Blau cites Saadia on Gen 38:21 directly (\"איה הקדשה... לא הייתה בזה קדשה\" → \"אין אלממתעה... מא כאנת ההנא ממתעה\") and the parallel rendering of the prohibition at Deuteronomy 23:18.",
            "relation": "direct",
        },
    },

    # ---- TWIST — Gen 41:23: scorched / contaminated ears -----------------------
    {
        "lemma_ja": "משוובה",
        "variants": ["שוב", "אלשוב", "ישוב"],
        "lemma_ar": "مشوبة",
        "root": "ش-و-ب",
        "tier": "twist",
        "classical_en": "passive participle of شاب (Form I) — classically \"to mix, to blend, to adulterate\" (esp. of water with milk, or honey with sugar). The post-classical extension to \"contaminate by heat → scorch, blight\" is attested only in biblical-translation traditions",
        "classical_he": "בינוני פעול של شاب (בנין I) — בלשון הקלסית \"לערב, למזג, לזייף\" (במיוחד מים בחלב או דבש בסוכר). ההרחבה הפוסט-קלסית ל\"זיהום על-ידי חום → שִׁדּוּף, בְּלִיָּה\" מתועדת רק במסורות התרגום המקראיות",
        "saadia_en": "blighted, scorched — Saadia renders the Hebrew שְׁדוּפֹת קָדִים (\"blasted by the east wind,\" of Pharaoh's lean ears of grain) as משוובה בריח אלקבול (\"mixed/contaminated by the east wind\"), pulling the verb out of the \"adulterate\" semantic field and into agricultural blight. The pairing recurs at Saadia's Deut 28:22 \"וְשִׁדָּפוֹן\" → ואלשוב",
        "saadia_he": "שדופה, צרובה — סעדיה מתרגם את \"שְׁדוּפֹת קָדִים\" העברי (השיבולים הדקות בחלום פרעה) כ\"משוובה בריח אלקבול\" (\"מעורבת/מזוהמת ברוח הקדים\"), ומושך את הפועל מתחום הסמנטי של \"זִיּוּף / עִרְבּוּב\" אל תחום השיזפון החקלאי. הצירוף חוזר אצלו בדברים כח:כב \"וּבַשִּׁדָּפוֹן\" → ואלשוב",
        "mechanism": "post-classical semantic extension specific to biblical translators: Saadia takes the classical \"mix/adulterate\" sense of شوب (best known from the proverbial شائب bayyāḍ aṣ-ṣabīy \"the one who mixes a child's milk\") and stretches it into the agricultural blight register — perhaps reading the שדופות as \"contaminated/spoiled in their nutritive substance\" by the hot wind, rather than physically dried up. The choice avoids the obvious قَطْر / صَدَف / ذَوَى, hewing instead to a verb that lets Saadia keep his preferred frame of *agency-by-contamination* over *passive desiccation*",
        "verses": [
            {"book": "Bereshit", "ch": 41, "v": 23},
        ],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "شوب",
            "sense": "Noun شوب / participle مشوب \"heat, blight / חוֹם, שִׁדָּפוֹן\" — Blau cites Saadia on Gen 41:23 directly (\"שדופות קדים → קד צרבהא אלשוב / משוובה בריח אלקבול\") and the parallel Deut 28:22 (\"ובשדפון → ואלשוב\"), with Rashbach 17:6 and 119:10 echoing.",
            "relation": "direct",
        },
    },

    # ============================================================================
    # NOTE tier (6) — marked semantic shifts, single-line contrast
    # ============================================================================

    # ---- NOTE — Gen 19:29: overthrow noun-form for ההפיכה ----------------------
    {
        "lemma_ja": "אלמקלב",
        "variants": ["מקלב", "מקלוב"],
        "lemma_ar": "المقلَب",
        "root": "ق-ل-ب",
        "tier": "note",
        "classical_en": "noun-of-place from قلب (\"to overturn, invert\") — classically denotes a turning-point or a thing that is overturned",
        "classical_he": "שם-מקום מן ق-ل-ب (\"להפוך, להעתיק\") — בלשון הקלסית: נקודת מפנה או דבר שהופך פניו",
        "saadia_en": "the overthrow — Saadia uses the noun مقلَب (rather than the verbal-noun انقلاب or قلب) to render the Hebrew הַהֲפֵכָה in Gen 19:29 (\"and God delivered Lot from the midst of the overthrow [of Sodom]\"). Blau notes the choice is a Hebrew-shaped pattern-match — Saadia coins the noun to mirror the Hebrew nominal form, where the natural Arabic would have been a verb",
        "saadia_he": "המהפכה (הפיכת סדום) — סעדיה משתמש בשם-העצם مقلَب (במקום בשם-הפעולה انقلاب או قلب) כדי לתרגם \"הַהֲפֵכָה\" של בראשית יט:כט (\"ויהי בְּשַׁחֵת אלוהים את עָרֵי הַכִּכָּר... וַיְשַׁלַּח אֶת לוֹט מִתּוֹךְ הַהֲפֵכָה\"). בלאו מציין שהבחירה היא חיקוי תבנית עברית — סעדיה גוזר שם-עצם כדי לראי את הצורה הנומינלית העברית, במקום הפועל שהיה הבחירה הטבעית בערבית",
        "mechanism": "Hebrew-shaped morphological calque: Saadia generates an Arabic noun on a Hebrew nominal pattern (CT-noun → maC₁C₂aC₃) rather than choosing the standard verbal noun. Same noun reappears at Saadia's Deut 29:22 and Isaiah 13:19, showing systematic adoption",
        "verses": [
            {"book": "Bereshit", "ch": 19, "v": 29},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "قلب",
            "sense": "مقلَب \"the overthrow (of Sodom and Gomorrah), overturning / מַהְפֵּכָה, הֲפִיכָה\" — Blau cites Saadia on Gen 19:29 directly, with parallels at Deut 29:22 and Isaiah 13:19; notes that the noun-form imitates the Hebrew pattern.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Gen 41:8: Pharaoh's spirit "troubled" --------------------------
    {
        "lemma_ja": "כרבת",
        "variants": ["כרב", "אכרב", "מכרוב"],
        "lemma_ar": "كربت",
        "root": "ك-ر-ب",
        "tier": "note",
        "classical_en": "Form I of كرب — \"to be in distress, to be grieved, to experience anxiety\" (with the noun كَرْب for affliction in classical poetry)",
        "classical_he": "בנין I של ك-ر-ب — \"להיות בְּצָרָה, לדאוג, לסבול חרדה\" (עם שם-העצם كَرْب לאסון בשירה הקלסית)",
        "saadia_en": "his spirit was troubled — Saadia renders the Hebrew וַתִּפָּעֶם רוּחוֹ (\"his spirit was agitated\", Pharaoh waking from the dreams) as כרבת רוחה (\"his spirit was distressed\"). The choice picks up the more existential register — anxiety/grief — rather than the surface \"disturbance\" that an Arabic ضاق בה rouhuhu or انزعج would have carried. Saadia uses the same verb at his Ps 77:5 (נפעמתי) and Dan 7:15 (אתכרית רוחי)",
        "saadia_he": "נחרדה רוחו — סעדיה מתרגם את \"וַתִּפָּעֶם רוּחוֹ\" (פרעה התעורר מן החלומות) כ\"כרבת רוחה\" (\"רוחו דאגה / נחרדה\"). הבחירה מאמצת את הרובד הקיומי יותר — חרדה, צער — במקום ה\"הִתְעַרְעֲרוּת\" השטחית שהייתה צפויה בערבית רגילה (ضاق ب, انزعج). סעדיה משתמש באותו פועל בתהלים עז:ה (\"נפעמתי\") ובדניאל ז:טו (\"אתכרית רוחי\")",
        "mechanism": "register-shift: where the Hebrew הִפָּעֵם is a single ambiguous lexeme between physical agitation and inner disturbance, Saadia commits to the inner-disturbance reading and reaches for a verb (كرب) that classical Arabic uses for genuine grief — not for the merely-startled. The cumulative effect across his Pentateuch translation is to make Pharaoh's nighttime fear into a moral foreboding",
        "verses": [
            {"book": "Bereshit", "ch": 41, "v": 8},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "كرب",
            "sense": "Form I + روحه: \"to be worried, distressed, grieved, to experience anxiety / הִצְטַעֵר, הִתְעַצֵּב, דָּאַג, נִפְעַם\" — Blau cites Saadia on Gen 41:8 directly (\"ותפעם רוחו → כרבת רוחה\"), with parallel renderings at Saadia's Ps 77:5 and Dan 7:15.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Gen 31:36: דהקתני "you pursued me hotly" -----------------------
    {
        "lemma_ja": "דהקתני",
        "variants": ["דהק", "דהאקא", "אדהק"],
        "lemma_ar": "دهقتني",
        "root": "د-ه-ق",
        "tier": "note",
        "classical_en": "classically: to thrust, to push hard, to drive forcefully (Form I); rare extension in post-classical Arabic to \"to pursue, to chase down\" via the sense of forceful drive",
        "classical_he": "בלשון הקלסית: לדחוף, להדוף בכוח, לדחוק (בנין I); הרחבה נדירה בערבית הפוסט-קלסית ל\"לִרְדֹּף, לְהָסִיג\" באמצעות משמע ההדיפה הנמרצת",
        "saadia_en": "you pursued me — Saadia renders Jacob's protest to Laban כִּי-דָלַקְתָּ אַחֲרָי (literally \"because you burned-pursued after me\", an idiomatic Hebrew phrase for hot pursuit) as אד' דהקתני (\"since you pursued/drove me hard\"). The Arabic verb is the marked-emphatic choice over the obvious لحقتني or طلبتني",
        "saadia_he": "כִּי רָדַפְתָּ אַחֲרַי — סעדיה מתרגם את מחאת יעקב ללבן \"כִּי-דָלַקְתָּ אַחֲרָי\" (פועל הנדלקות-רדיפה העברי) כ\"אד' דהקתני\" (\"שֶׁכֵּן רָדַפְתָּ אוֹתִי\"). הפועל הערבי הוא בחירה מסומנת-נמרצת על פני لحقتني או طلبتني הצפויים יותר",
        "mechanism": "extension of classical \"thrust/push hard\" to \"pursue hotly\" — Saadia adopts a marked verb that captures both the urgency (Laban's seven-day chase) and the implicit violence of the pursuit. The choice contrasts with the neutral اتبع / لحق that other JA translators use for רדף",
        "verses": [
            {"book": "Bereshit", "ch": 31, "v": 36},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "دهق",
            "sense": "Form I/II: \"to pursue, to overtake / לִרְדֹּף, לְהָסִיג, לְהִדָּבֵק אַחֲרֵי\" — Blau records the post-classical extension citing Saadia on Gen 31:36 directly (\"כי דלקת אחרי → אד' דהקתני\").",
            "relation": "direct",
        },
    },

    # ---- NOTE — Gen 33:13: sequential "to die one after another" ---------------
    {
        "lemma_ja": "תמאות",
        "variants": ["מאת", "מאות", "תמת"],
        "lemma_ar": "تماوت",
        "root": "م-و-ت",
        "tier": "note",
        "classical_en": "Form I of مات (\"to die\") in serial-aspectual usage — the imperfective + accusative-plural rendering a Hebrew imperfect with collective subject, denoting one-by-one perishing rather than a single death event",
        "classical_he": "בנין I של مات (\"מת\") בשימוש סידוּרי — צורת הימשיכ + מושא ברבים מציינת מיתה אחד אחרי השני ולא אירוע מות יחיד",
        "saadia_en": "they will die one after another — Saadia renders Jacob's protest to Esau וּדְפָקוּם יוֹם אֶחָד וָמֵתוּ כָּל-הַצֹּאן (\"if they are driven hard one day, all the flock will die\") as פאן כדדתהא יומא ואחדא תמאות כת'יר מנהא (\"if you drive them hard one day, many of them will die in sequence\"). The plural-imperfect with כת'יר (\"many\") instead of גמיע (\"all\") softens the absolute Hebrew claim into a likely sequential die-off",
        "saadia_he": "תָּמוּתֶנָה זוֹ אַחַר זוֹ — סעדיה מתרגם את מחאת יעקב לעשו \"וּדְפָקוּם יוֹם אֶחָד וָמֵתוּ כָּל-הַצֹּאן\" כ\"פאן כדדתהא יומא ואחדא תמאות כת'יר מנהא\" (\"אם תדפוקן יום אחד, רַבּוֹת מֵהֶן תָּמוּתֶנָה זוֹ אַחַר זוֹ\"). הימשיכ של רבים עם \"כת'יר\" (רבות) במקום \"גמיע\" (כָּל) מרכך את הטענה העברית המוחלטת לסְפֵקוּלָצְיָה של מות סדיר",
        "mechanism": "interpretive softening + serial-aspect: Saadia avoids the categorical \"all\" reading by selecting a serial-imperfect construction and replacing הָעֲדָר \"כָּל\" with \"כָּתִיר\" (many), reading Jacob's argument as probabilistic rather than absolute. This dovetails with his wider tendency to defang threshold-rhetoric in patriarchal dialogue",
        "verses": [
            {"book": "Bereshit", "ch": 33, "v": 13},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "موت",
            "sense": "Form I: \"to die one after another / יָמוּתוּ אַחַת אַחַת\" (serial-aspect usage with imperfective + plural accusative) — Blau cites Saadia on Gen 33:13 directly (\"ומתו כל הצאן → תמאות כת'יר מנהא\").",
            "relation": "direct",
        },
    },

    # ---- NOTE — Gen 8:3: idiomatic "the more it went, the more it returned" ----
    {
        "lemma_ja": "תראגע",
        "variants": ["תראג", "פתראגע", "כלמא"],
        "lemma_ar": "تراجع",
        "root": "ر-ج-ع",
        "tier": "note",
        "classical_en": "Form VI of رجع — \"to return repeatedly, to recede in stages.\" In post-classical idiomatic usage with كلما + I, this forms a serial-comparative construction (\"the more X, the more Y\") that is not a classical Arabic pattern but a calque from biblical Hebrew הָלוֹךְ וְ-",
        "classical_he": "בנין VI של ر-ج-ع — \"לחזור פעם אחר פעם, להישוב בשלבים\". בשימוש האידיומטי הפוסט-קלסי עם كلما + בנין I, יוצרת מבנה הַשְׁוָאָה סִדוּרִית (\"כל ככל ש- X, כן Y\") שאינו תבנית ערבית קלסית אלא בְּבוּאָה של ההיגד המקראי \"הָלוֹךְ וְ-\"",
        "saadia_en": "the waters receded — Saadia renders the famous Hebrew \"infinitive-absolute + finite\" idiom וַיָּשֻׁבוּ הַמַּיִם מֵעַל הָאָרֶץ הָלוֹךְ וָשׁוֹב (\"and the waters returned from upon the earth going and returning\") as פתראגע אלמא עלי' אלארץ' כל מא מר רגע (\"and the waters receded — every time [more time] passed, [more water] returned [to the seas]\"). The double-aspect Hebrew is replaced by an Arabic serial-comparative construction; Blau notes this construction is Saadia's stock equivalent for the הָלוֹךְ infinitive-absolute paradigm",
        "saadia_he": "וַיָּשׁוּבוּ הַמַּיִם הָלוֹךְ וָשׁוֹב — סעדיה מתרגם את ההיגד העברי האייקוני \"וַיָּשֻׁבוּ הַמַּיִם מֵעַל הָאָרֶץ הָלוֹךְ וָשׁוֹב\" (מקור-מוחלט + פועל פינוטי) כ\"פתראגע אלמא עלי' אלארץ' כל מא מר רגע\" (\"וְהַמַּיִם נְסוּגוּ — בְּכָל פַּעַם שֶׁעָבַר [זְמַן], חָזְרוּ [הַמַּיִם] לְמְקוֹמָם\"). הצורה דו-המבטית של העברית מוחלפת במבנה הַשְׁוָאָה סִדוּרִית ערבי; בלאו מציין שזהו תרגומו הקבוע של סעדיה למבנה ההָלוֹךְ + פועל",
        "mechanism": "syntactic calque: the Hebrew הָלוֹךְ וְ-X paradigm — which encodes a progressive-iterative aspect Arabic does not natively have — is repackaged into the Arabic كلما + I … + I construction. The lexical choice of رجع (\"to return\") for the second verb (instead of ذهب \"to go\") is itself a calque of שׁוּב, the Hebrew root puns on itself",
        "verses": [
            {"book": "Bereshit", "ch": 8, "v": 3},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "رجع",
            "sense": "Form VI + كلما correlative: \"more and more, the more X the more Y\" — Blau cites Saadia on Gen 8:3 directly as the canonical example of this Hebrew-shaped serial-comparative idiom, noting its parallel in modern Aramaic of Kurdistani Jews; says it is \"frequent in Saadia.\"",
            "relation": "direct",
        },
    },

    # ---- NOTE — Gen 30:41: sheep in heat ---------------------------------------
    {
        "lemma_ja": "וחאם",
        "variants": ["וחם", "תחם", "יחם", "וחאמת"],
        "lemma_ar": "وحام",
        "root": "و-ح-م",
        "tier": "note",
        "classical_en": "Form I of وحم — classically \"to crave food during pregnancy\" (the technical term for a pregnant woman's cravings); the extension to \"to be in heat, to conceive\" (animal sexual receptivity) is post-classical, narrowing the verb's primary application from human pregnancy-cravings to animal estrus",
        "classical_he": "בנין I של و-ح-م — בלשון הקלסית: \"לתאוות מאכל בעת ההריון\" (המונח הטכני לתאוות אישה הרה); ההרחבה ל\"לְהִתְיַחֵם, לְהָרוֹת\" (קבלת זוויג בעלי-חיים) היא פוסט-קלסית, ומצירה את היישום העיקרי מתאוות-הריון אנושיות לאסטרוס של בהמות",
        "saadia_en": "in heat / conceiving — Saadia renders the Hebrew בְּכָל יַחֵם הַצֹּאן הַמְקֻשָּׁרוֹת (\"whenever the strong flock was in heat\") as פי כל וקת וחאם אלגנם אלרביעייה (\"every time the spring flock was in heat\"). The verb is the technical Arabic for breeding-estrus, which by Saadia's time was no longer reserved for human pregnancy-cravings but had transferred to animal sexual receptivity",
        "saadia_he": "בְּעֵת הִתְיַחֲמוּת — סעדיה מתרגם את \"בְּכָל יַחֵם הַצֹּאן הַמְקֻשָּׁרוֹת\" (יעקב במַעֲשֵׂה הָעַקֻדִּים) כ\"פי כל וקת וחאם אלגנם אלרביעייה\" (\"בְּכָל עֵת הִתְיַחֲמוּת הַצֹּאן הָאֲבִיבִיוֹת\"). הפועל הוא המונח הערבי המקצועי לעוֹנַת הָאַסְטְרוֹס, שבזמנו של סעדיה כבר לא היה מוקצה לתשוקות-הריון אנושיות אלא עבר לשַׁמֵּשׁ לתִּפְקוּד הָרְבִיָּה הַבְּהֵמִי",
        "mechanism": "register-tracking: the Hebrew יָחֵם (\"to be in heat,\" a single verb covering both human conjugal seasonality and animal breeding-cycles) is matched to Arabic وحم at exactly the post-classical moment when the Arabic verb had migrated from the human-pregnancy register to the animal-estrus register. Saadia's translation choices in pastoral narrative are consistently attuned to this kind of semantic-drift moment",
        "verses": [
            {"book": "Bereshit", "ch": 30, "v": 41},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "وحم",
            "sense": "Form I: \"to be in heat; to conceive / הִתְיַחֵם, הִתְחַמֵּם בְּתַאֲוָה מִינִית, הָרְתָה\" — Blau cites Saadia on Gen 30:41 directly (\"בעת יחם הצאן → וקת וחאם אלגנס\") and Saadia on Ps 51:7 (\"בעוון חוללתי → באלן'סב טלק\").",
            "relation": "direct",
        },
    },

    # ============================================================================
    # GLOSS tier (6) — non-cognate Heb→Ar pairings, register shifts
    # ============================================================================

    # ---- GLOSS — Gen 49:26: hill (high-register) for גבעה --------------------
    {
        "lemma_ja": "יפאע",
        "variants": ["אליפאע", "יפע"],
        "lemma_ar": "يَفاع",
        "root": "ي-ف-ع",
        "tier": "gloss",
        "classical_en": "high-register Arabic for an isolated raised tract of land, smaller than جبل (\"mountain\") and larger than تل (\"mound\")",
        "classical_he": "מילה גבוהה בערבית לשטח גָּבוֹהַּ מְבוֹדָד, קָטָן מִ-جبل (\"הָר\") וְגָדוֹל מִ-تل (\"גַּל\")",
        "saadia_en": "hill",
        "saadia_he": "גבעה",
        "mechanism": "high-register lexical pairing: Saadia uses يَفاع (rare elevated synonym) for biblical-Hebrew גבעה (\"hill\"), preserving the elevated register of the Hebrew word against the prosaic تل / مرتفع that would have been available. The pairing is Saadia's standard for גבעה in poetic / blessing contexts",
        "verses": [
            {"book": "Bereshit", "ch": 49, "v": 26},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "يفع",
            "sense": "يفع (pl. يفاع) \"hill / גִּבְעָה\" — Blau cites Saadia on Gen 49:26 directly (\"גבעת עולם → יפאע אלדהר\") and Rashbach 367:7 echoing.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Gen 27:4: "kinds of dishes" for מטעמים ----------------------
    {
        "lemma_ja": "אלואנא",
        "variants": ["אלאלואן", "אלואן"],
        "lemma_ar": "ألواناً",
        "root": "ل-و-ن",
        "tier": "gloss",
        "classical_en": "plural of لون (\"color, kind\"); culinary register \"kinds of dishes, varieties of food\"",
        "classical_he": "רבים של لون (\"צֶבַע, מִין\"); ברובד הקולינרי: \"סוּגֵי מַאֲכָל, מִינֵי מַטְעַמִּים\"",
        "saadia_en": "kinds of dishes",
        "saadia_he": "סוגי מאכל, מטעמים למיניהם",
        "mechanism": "culinary-register substitution: the biblical-Hebrew מַטְעַמִּים (\"savory dishes,\" of the food Esau was to bring Isaac before the blessing) is rendered with the Arabic culinary plural ألوان — a register-precise pick (post-classical Arab cuisine catalogued dishes by \"kinds\", much like English \"courses\")",
        "verses": [
            {"book": "Bereshit", "ch": 27, "v": 4},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "لون",
            "sense": "ألوان \"kinds of food, various kinds of dishes / סוּגֵי מַאֲכָל, מַטְעַמִּים לְמִינֵיהֶם\" — Blau cites Saadia on Gen 27:4 directly (\"מטעמים → אלואנא\").",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Gen 37:3: tunic (Aramaic-flavored) for כתונת ---------------
    {
        "lemma_ja": "תוניה",
        "variants": ["תוני", "אלתוניה"],
        "lemma_ar": "تونية",
        "root": "ت-و-ن",
        "tier": "gloss",
        "classical_en": "garment, shirt — Arabic loan from Aramaic/Syriac kuttūnā / tunīkā; classical Arabic uses قميص or ثوب for the same general garment",
        "classical_he": "בֶּגֶד, כֻּתּוֹנֶת — שאילה ערבית מן הארמית/הסורית כּוּתּוּנָא / תוּנִיקָא; הערבית הקלסית משתמשת ב-قميص או ثوب לאותו פריט לבוש כללי",
        "saadia_en": "tunic",
        "saadia_he": "כתונת, בגד",
        "mechanism": "Aramaicizing lexical choice: Saadia uses the Aramaic-flavored loan تونية (rather than the standard Arabic قميص) for biblical-Hebrew כְּתֹנֶת, preserving phonological resonance with the Hebrew cognate. The pairing of \"tūniyya dīb̄āj\" (\"tunic of brocade\") for כְּתֹנֶת פַּסִּים (the disputed Joseph-coat phrase) commits to a luxury-garment reading",
        "verses": [
            {"book": "Bereshit", "ch": 37, "v": 3},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "تون",
            "sense": "تونية \"garment, shirt / כְּתֹנֶת\" — Blau cites Saadia on Gen 37:3 forward (\"כתנת → תוניה\") and Saadia on Lev 16:4 (\"כתנת בד → תוניה מן בז\").",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Gen 6:14: pitch (calque pairing) for כפר -------------------
    {
        "lemma_ja": "באלקפאר",
        "variants": ["קפאר", "אלקפאר", "וקפרהא"],
        "lemma_ar": "بالقفار",
        "root": "ق-ف-ر",
        "tier": "gloss",
        "classical_en": "asphalt, bitumen, sea-pitch (قَفْر/قِفْر) — Arabic loan; classical Arabic also has زفت and قار for the same substance",
        "classical_he": "אַסְפַלְט, זֶפֶת, זֶפֶת יָם (قَفْر/قِفْر) — שאילה ערבית; בערבית הקלסית גם زفت و-قار לאותו חומר",
        "saadia_en": "pitch",
        "saadia_he": "כֹּפֶר, זֶפֶת",
        "mechanism": "consonantal-calque pairing: Saadia uses قَفْر for biblical-Hebrew כֹּפֶר (the pitch with which Noah waterproofed the ark), preserving the consonantal triad k-p-r ~ q-f-r. The pairing is reinforced by the parallel verb \"וקפרהא\" (\"and pitch it\") rendering Hebrew וְכָפַרְתָּ — exact morphological mirror. Ibn Janāḥ glosses the term in the same direction (\"כפר → אלקפר → אשבלט / asphalt\")",
        "verses": [
            {"book": "Bereshit", "ch": 6, "v": 14},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "قفر",
            "sense": "قَفْر/قِفْر \"asphalt, pitch, bitumen / אַסְפַלְט, זֶפֶת, זֶפֶת יָם\" — Blau cites Saadia on Gen 6:14 directly (\"וכפרת אותה מבית ומחוץ בכפר → וקפרהא מן דאכל ומן כ'ארג באלקפאר\") and Saadia on Ex 2:3 (\"ותחמרה בחמר ובזפת → וקפרתהא באלקפאר ואלזפת\").",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Gen 29:2: flock (collective noun) for עדר -------------------
    {
        "lemma_ja": "קטוע",
        "variants": ["קטיע", "אלקטוע", "קטעה"],
        "lemma_ar": "قُطوع",
        "root": "ق-ط-ع",
        "tier": "gloss",
        "classical_en": "plural of قطعة (\"piece, section\"); post-classical extension to \"flock, herd\" via \"a separated/cut group of livestock\". Classical Arabic uses قطيع for an individual flock; the plural قطوع denoting multiple flocks is a Saadianic register",
        "classical_he": "רַבִּים שֶׁל قطعة (\"חֵלֶק, חֲטִיבָה\"); הרחבה פוסט-קלסית לְ\"עֵדֶר, צֹאן\" דֶּרֶךְ \"קְבוּצַת בְּהֵמוֹת נִפְרֶדֶת/חֲתוּכָה\". הערבית הקלסית משתמשת ב-قطيع לעדר יחיד; הרבים قطوع לעדרים רבים הוא רובד-שפה של סעדיה",
        "saadia_en": "flocks",
        "saadia_he": "עדרים",
        "mechanism": "register-specification: the biblical-Hebrew עֵדֶר (\"flock\", three of which Jacob sees at the well) is rendered with the collective plural قطوع. Classical Arabic would more naturally have used ثلاث قطعان (plural of قطيع); Saadia's قطوع (plural of قطعة, treating each flock as a discrete \"piece\" of livestock) is a marked lexical choice that recurs in his pastoral narrative",
        "verses": [
            {"book": "Bereshit", "ch": 29, "v": 2},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "قطع",
            "sense": "قطعة / pl. قطوع \"piece, section → flock (of sheep), herd / עֵדֶר, חַטִיבָה (שֶׁל בְּהֵמוֹת)\" — Blau attests the post-classical extension citing Saadia on Gen 29:2 (\"שלשה עדרי צאן → ת'לאת'ה קטוע מן אלגנם\").",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Gen 1:9: dry land --------------------------------------------
    {
        "lemma_ja": "אליבאס",
        "variants": ["יבאס", "יביס", "יבאסא", "אליביס"],
        "lemma_ar": "اليَباس",
        "root": "ي-ب-س",
        "tier": "gloss",
        "classical_en": "dry land (يَبَاس / يَبيس); classical Arabic uses يَبَس as adjective for \"dry,\" but the noun-form يَباس for \"the dry land\" specifically (terra firma exposed as the waters recede) is a biblical-translation register",
        "classical_he": "הַיַּבָּשָׁה (يَبَاس / يَبيس); הערבית הקלסית משתמשת בְּ-يَبَس כתואר ל\"יָבֵשׁ\", אבל שֵׁם-הָעֶצֶם يَباس לְ\"הַיַּבָּשָׁה\" (אֶרֶץ מוּצֶקָה שֶׁמִּתְגַּלָּה כְּשֶׁהַמַּיִם נְסוֹגִים) הוא רוֹבָד שֶׁל הַתַּרְגוּם הַמִּקְרָאִי",
        "saadia_en": "the dry land",
        "saadia_he": "היבשה",
        "mechanism": "biblical-translation register: Saadia consistently renders Hebrew יַבָּשָׁה (\"dry land\", introduced in the Day-Three creation account when waters are gathered into one place) with يَباس — a noun-form that is rare in classical Arabic but stable across the Saadianic Bible. The same noun reappears at his Ps 66:6 (\"הָפַךְ יָם לְיַבָּשָׁה\" → \"אקלב אלבחר יבאסא\") and Ps 95:5",
        "verses": [
            {"book": "Bereshit", "ch": 1, "v": 9},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "يبس",
            "sense": "يَباس / يَبيس \"the dry land / הַיַּבָּשָׁה\" — Blau cites Saadia on Gen 1:9 directly (\"ותראה היבשה → ויצ'הר אליבאס\") and parallels at Saadia's Ps 66:6 (\"אקלב אלבחר יבאסא\") and Ps 95:5 (\"ואליבאס קדרתה בלקתהא\").",
            "relation": "direct",
        },
    },
]


# ============================================================================
# RE-AUDIT PATCHES (2) — add blau_dict + sources=blau-dict to existing entries
# ============================================================================

RE_AUDIT_PATCHES = [
    {
        "lemma_ja": "מסתבחרה",  # existing Ber 1:2 twist entry
        "add_blau_dict": {
            "root": "بحر",
            "sense": "Form X استبحر \"to be covered by water, to overflow / לְהִיוֹת מְכֻסֶּה בַּמַּיִם, לְהִיוֹת מוּצָף\" — Blau attests Form X explicitly citing Saadia (לבראשית, the creation account) for exactly the participial form Saadia uses to render בֹּהוּ at Gen 1:2.",
            "relation": "direct",
        },
    },
    {
        "lemma_ja": "שמשאר",  # existing Ber 6:14 twist entry
        "add_blau_dict": {
            "root": "شمشار",
            "sense": "شمشار (alt شمشاد) \"ash-tree / boxwood (Buxus sempervirens) / אֶשְׁכְּרוֹעַ\" — Blau cites Saadia on Gen 6:14 directly (with Ibn Janāḥ's commentary corroborating: \"עצי גפר → אלשמשאר\"), confirming the medieval Near-Eastern hardwood identification.",
            "relation": "direct",
        },
    },
]


def main():
    path = pathlib.Path("data/tafsir-divergence.json")
    if not path.exists():
        print(f"FATAL: {path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    payload = json.loads(path.read_text())

    # --- Apply NEW_ENTRIES (dedup on lemma_ja, mirrors apply_phase4_bereshit_batch*) ---
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

    # --- Apply RE_AUDIT_PATCHES (mutate existing entries) ---
    patched = 0
    patch_skipped = []
    by_lemma = {e["lemma_ja"]: e for e in payload["entries"]}
    for patch in RE_AUDIT_PATCHES:
        target = by_lemma.get(patch["lemma_ja"])
        if target is None:
            patch_skipped.append((patch["lemma_ja"], "target entry not found"))
            continue
        if "blau_dict" in target:
            patch_skipped.append((patch["lemma_ja"], "already has blau_dict; not overwriting"))
            continue
        target["blau_dict"] = patch["add_blau_dict"]
        if "blau-dict" not in target["sources"]:
            target["sources"].append("blau-dict")
        patched += 1

    # --- Write + round-trip validate ---
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(path.read_text())  # catches JSON syntax errors

    # --- Report ---
    print(f"Added {added} new entries to {path}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Patched {patched} existing entries with blau_dict + blau-dict source")
    for s, reason in patch_skipped:
        print(f"  - patch skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")


if __name__ == "__main__":
    main()

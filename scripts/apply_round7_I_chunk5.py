#!/usr/bin/env python3
"""Phase 2 Round 7 Batch I — chunk 5 (25 candidates).

Heavy Tabernacle / cultic vocabulary chunk. Adds 22 new lemmas + 3 patches.

Notable Form additions:
  • akhraja-bring-out — Form IV of kh-r-j (distinct from kharaja-exit).
  • tahhara-declare-clean — Form II of ṭ-h-r (distinct from tahara-pure, F I).
  • jaza-reward — Form III of j-z-y.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Verbs ----------
    {
        "id": "hafiza-keep",
        "lemma_ja": "חפצ'",
        "lemma_ar": "حَفِظ",
        "root": "ḥ-f-ẓ",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to keep, guard, preserve, watch over; (with abstract object) to observe (a commandment, a covenant)",
        "gloss_he": "שָׁמַר, נָצַר",
        "notes": "JA scribal convention varies: trailing ẓād may be written חפז (no apos), חפצ (apos absent, ṣād-style), or חפצ' (with apos marking ẓ). Variants list collapses all three.",
        "saadia_note": "Saadia's regular gloss for Hebrew שָׁמַר in covenantal / mitzvah contexts — 'and you shall keep' (Deut 5:29: ואחפצו; Exod 12:17: ואחפצו אלפטיר 'and you shall keep the unleavened bread').",
        "source": "lane",
        "variants": [
            "חפז", "חפצ",
            "חפצ'ת", "חפז'ת", "חפצת",
            "וחפצ'", "פחפצ'", "ואחפצו", "אחפצו", "פאחפצו",
            "ואחפצ'ו", "אחפצ'ו", "פאחפצ'ו",
            "יחפצ'", "ויחפצ'", "תחפצ'", "אחפצ'", "נחפצ'",
            "יחפז", "ויחפז", "תחפז",
            "יחפצ", "ויחפצ",
            "חאפצ'", "חאפז",
            "אסתחפץ'", "אסתחפצ", "אסתחפצתכם",
            "מחפוץ'", "אלמחפוץ'",
            "חפץ' ", "אלחפץ'", "באלחפץ'",
        ],
    },
    {
        "id": "akhraja-bring-out",
        "lemma_ja": "אכ'רג",
        "lemma_ar": "أَخْرَج",
        "root": "kh-r-j",
        "pos": "verb (Form IV, perfect)",
        "gloss_en": "to bring out, lead forth, cause to come out (transitive — Form IV of kharaja 'to go out')",
        "gloss_he": "הוֹצִיא",
        "notes": "Form IV (أَخْرَج). Distinct from the existing kharaja-exit which is Form I (intransitive 'to go out').",
        "saadia_note": "Saadia's regular gloss for Hebrew הוֹצִיא — the Exodus formula 'who brought you out from the land of Egypt' (אלמכ'רגכם מן בלד מצר). The 1cs perfect אכ'רגתהם 'I brought them out' appears in Deut 9:12, 9:29.",
        "source": "lane",
        "variants": [
            "אכ'רגת", "אכ'רגתהם", "אכ'רגתכם", "אכ'רגתה", "אכ'רגתהא",
            "ואכ'רג", "פאכ'רג",
            "אכ'רגה", "אכ'רגהא", "אכ'רגהם", "אכ'רגנא",
            "יכ'רג", "ויכ'רג", "פיכ'רג", "תכ'רג", "אכ'רג",
            "מכ'רג", "אלמכ'רג", "ואלמכ'רג",
            "אלמכ'רגכם", "אלמכ'רגנא", "אלמכ'רגהם",
            "אכ'רגוא", "ואכ'רגוא", "פאכ'רגוא",
        ],
    },
    {
        "id": "tahhara-declare-clean",
        "lemma_ja": "מטהר",
        "lemma_ar": "مُطَهَّر",
        "root": "ṭ-h-r",
        "pos": "verb (Form II, perfect) / passive participle",
        "gloss_en": "to declare ritually clean / pronounce pure (Form II ṭahhara, transitive — distinct from Form I 'to be pure'); (passive ptcp) the one who is being declared clean",
        "gloss_he": "טִהֵר (הכריז על טהרה), הִטְהִיר",
        "notes": "Form II (طَهَّر) of ṭ-h-r — declarative/causative 'to declare s.o. clean'. Distinct from the Form I tahara 'to be / become pure'. The active ptcp muṭahhir = 'the one who declares clean'; passive ptcp muṭahhar / muṭṭahhir = 'the one being purified'.",
        "saadia_note": "Saadia's regular gloss for Hebrew טִהֵר (pi'el) — the priest's declarative act of pronouncing a leprosy patient clean (Lev 13:6, 13:13, 13:17, 13:23, 13:28 — פליטהרה 'let him declare him clean'; Lev 14:7 ויטהרה).",
        "source": "lane",
        "variants": [
            "אלמטהר", "ואלמטהר",
            "מטהרה", "אלמטהרה",
            "מטהרין", "אלמטהרין",
            "פליטהרה", "פליטהרהא",
            "יטהרה", "ויטהרה", "ויטהרהא", "ויטהרהם",
            "טהרה", "וטהרה", "פטהרה",
            "תטהיר", "אלתטהיר",
        ],
    },
    {
        "id": "irtada-accept",
        "lemma_ja": "ארתצ'א",
        "lemma_ar": "اِرْتَضَى",
        "root": "r-ḍ-y",
        "pos": "verb (Form VIII, perfect)",
        "gloss_en": "to accept, approve, find acceptable (passive yurtaḍā = 'it is accepted/approved')",
        "gloss_he": "רָצָה, קִבֵּל בְּרָצוֹן",
        "notes": "Form VIII (اِرْتَضَى) of r-ḍ-y. Distinct from the Form-I raḍiya 'to be pleased' and Form-II raḍḍā 'to please'. The passive yurtaḍā renders 'it is approved/accepted'.",
        "saadia_note": "Saadia's regular gloss for the Hebrew technical formula 'it shall be accepted / for acceptance' (לִרְצֹנוֹ / יֵרָצֶה → ירתצ'א ענה / ירתצ'א מנכם 'it is accepted on his behalf / accepted from you', Lev 1:3, 19:5, 22:25, 22:27).",
        "source": "lane",
        "variants": [
            "ירתצ'א", "ירתצ'י", "וירתצ'א", "פירתצ'א",
            "תרתצ'א", "ארתצ'א", "ארתצ'י",
            "ירתצ'א ענה", "ירתצ'א מנכם", "ירתצ'א מנהם",
            "מרתצ'א", "אלמרתצ'א",
        ],
    },
    {
        "id": "jaza-reward",
        "lemma_ja": "גאזא",
        "lemma_ar": "جَازَى",
        "root": "j-z-y",
        "pos": "verb (Form III, perfect)",
        "gloss_en": "to requite, recompense, reward; (with 1cs subject) 'I will reward / repay'",
        "gloss_he": "גָּמַל, שִׁלֵּם, נָתַן גְּמוּל",
        "notes": "Form III jāzā (جَازَى) of j-z-y. The 1cs imperfect ujāzī takes a direct object (ujāzīkum 'I reward you') often with khayran ('with good') as the cognate complement.",
        "saadia_note": "Saadia's regular gloss for Hebrew אֲנִי יְהוָה / שָׁמַרְתֶּם וַעֲשִׂיתֶם וְאֶהְיֶה formulas of divine reward — 'I am YHWH your God who rewards you with good' (Lev 18:4, 18:30, 19:37, 25:55: אנא אללה רבכם אגאזיכם כ'ירא). The cognate noun jazāʾ = 'reward, requital'.",
        "source": "lane",
        "variants": [
            "וגאזא", "פגאזא",
            "אגאזי", "ואגאזי", "פאגאזי",
            "אגאזיכם", "ואגאזיכם",
            "אגאזיהם", "אגאזיכמא",
            "יגאזי", "ויגאזי", "תגאזי",
            "גאזית", "גאזיתה", "גאזיוא",
            "מגאזאה", "אלמגאזאה",
            "גזא", "אלגזא", "ואלגזא", "גזאא", "גזא וגזא",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "ghalla-produce",
        "lemma_ja": "ג'לה",
        "lemma_ar": "غَلَّة",
        "root": "gh-l-l",
        "pos": "noun (f.)",
        "gloss_en": "produce, yield, crop, harvest-revenue (of a field, vineyard, orchard)",
        "gloss_he": "תְּבוּאָה, יְבוּל, פֵּרוֹת הַשָּׂדֶה",
        "saadia_note": "Saadia's regular gloss for Hebrew תְּבוּאָה in the agricultural-cycle passages (Exod 23:10, Lev 25:3: ותגמע ג'לתהא 'and gather in its produce').",
        "source": "lane",
        "variants": [
            "אלג'לה", "ואלג'לה",
            "ג'לתהא", "ג'לתה", "ג'לתי", "ג'לתכם", "ג'לתהם",
            "באלג'לה", "ללג'לה",
            "ג'לאת", "אלג'לאת", "ואלג'לאת",
        ],
    },
    {
        "id": "zij-molding",
        "lemma_ja": "זיג",
        "lemma_ar": "زِيج",
        "root": "z-y-j",
        "pos": "noun (m.)",
        "gloss_en": "molding, decorative rim (a raised border running around the edge of a flat surface)",
        "gloss_he": "זֵר (מסגרת זהב הסובבת)",
        "saadia_note": "Saadia's regular gloss for Hebrew זֵר ('a golden rim/border') in the Tabernacle furniture passages — the rim around the Ark, the table, the altar (Exod 25:11 'a molding of gold around it' = זיגא מן ד'הב מסתדירא; 25:24-25; 30:3-4; 37:2, 11, 26).",
        "source": "lane",
        "variants": [
            "אלזיג", "ואלזיג",
            "ובאלזיג", "באלזיג",
            "זיגא", "וזיגא",
            "אזיאג", "אלאזיאג",
        ],
    },
    {
        "id": "dahuq-pole",
        "lemma_ja": "דהוק",
        "lemma_ar": "دَهُوق",
        "root": "d-h-q",
        "pos": "noun (m., plural)",
        "gloss_en": "carrying-poles, staves (the wooden bars used to carry the Ark, the Table, and the Altar)",
        "gloss_he": "בַּדִּים",
        "saadia_note": "Saadia's regular gloss for Hebrew בַּדִּים in the Tabernacle-construction passages (Exod 25:13-15, 26-28; 27:6-7; 30:4-5; 37:4-5, 14-15, 27-28; 38:5-7; 40:20 — אדכ'ל אלדהוק פי אלחלק 'put the staves into the rings').",
        "source": "lane",
        "variants": [
            "אלדהוק", "ואלדהוק",
            "באלדהוק", "ללדהוק",
            "דהאק", "אלדהאק",
            "ודהוק",
        ],
    },
    {
        "id": "wahid-one",
        "lemma_ja": "ואחד",
        "lemma_ar": "وَاحِد",
        "root": "w-ḥ-d",
        "pos": "numeral / adjective",
        "gloss_en": "one (m.sg.); a single, a particular",
        "gloss_he": "אֶחָד, יָחִיד",
        "notes": "The Arabic-form 'one' — distinct from the Hebrew form אחד (already in dict). Saadia uses wāḥid in his Arabic prose; the Hebrew form אחד appears mainly in the Shemaʿ (Deut 6:4: אללה רבנא אללה ואחד 'YHWH our God, YHWH is one') and other Hebraisms.",
        "saadia_note": "Saadia's regular gloss for Hebrew אֶחָד / אַחַת — the femminine ואחדה / אלואחדה appears repeatedly in the Tabernacle dimensions (Exod 26 passim — אלשקה אלואחדה 'the one curtain'). Numerical 'one and the other' / 'one of them' collocations also use this stem.",
        "source": "lane",
        "variants": [
            "אלואחד", "ואלואחד",
            "ואחדה", "ואלואחדה", "אלואחדה",
            "באלואחד", "באלואחדה",
            "ואחדא", "ואחדה'", "אלואחדה'",
            "ואחדכם", "ואחדהם",
        ],
    },
    {
        "id": "ʿurwa-loop",
        "lemma_ja": "ערוה",
        "lemma_ar": "عُرْوَة",
        "root": "ʿ-r-w",
        "pos": "noun (f.)",
        "gloss_en": "loop, hook-loop, eyelet (especially of cloth, for fastening)",
        "gloss_he": "לוּלָאָה",
        "saadia_note": "Saadia's regular gloss for Hebrew לֻלָאֹת ('loops') in the Tabernacle-curtain passages — 'fifty loops on each curtain' (Exod 26:4-11; 36:11-17 — כ'מסין ערוה).",
        "source": "lane",
        "variants": [
            "אלערוה", "ואלערוה",
            "וערוה", "באלערוה",
            "ערי", "אלערי", "ואלערי",   # broken plural
            "ערואת", "אלערואת",
        ],
    },
    {
        "id": "rukn-corner",
        "lemma_ja": "רכן",
        "lemma_ar": "رُكْن",
        "root": "r-k-n",
        "pos": "noun (m.)",
        "gloss_en": "corner, pillar, support; (in Tabernacle architecture) the corner-projection of the altar",
        "gloss_he": "פִּנָּה, קֶרֶן (קַרְנוֹת הַמִּזְבֵּחַ)",
        "saadia_note": "Saadia's regular gloss for Hebrew קֶרֶן in the altar-corner-projection sense ('horns' of the altar) — Exod 27:2, 30:2 ואצנע ארכאנה עלי' ארבע גהאתה 'make its corners on its four sides'; Exod 30:10; Lev 4 passim.",
        "source": "lane",
        "variants": [
            "אלרכן", "ואלרכן",
            "ארכאן", "אלארכאן", "ואלארכאן",
            "ארכאנה", "ארכאנהא", "ארכאנכם", "ארכאנהם",
            "ובארכאן", "ובארכאנה",
            "רכנא",
        ],
    },
    {
        "id": "tharb-caul",
        "lemma_ja": "ת'רב",
        "lemma_ar": "ثَرْب",
        "root": "th-r-b",
        "pos": "noun (m.)",
        "gloss_en": "caul, the fatty membrane covering the entrails (especially the omentum)",
        "gloss_he": "חֵלֶב הַמְכַסֶּה אֶת הַקֶּרֶב, יוֹתֶרֶת הַכָּבֵד",
        "saadia_note": "Saadia's regular gloss for Hebrew חֵלֶב הַמְכַסֶּה אֶת הַקֶּרֶב — the fatty caul over the inner organs of a sacrificial animal (Exod 29:13, 22; Lev 3:3, 9, 14; Lev 4:8 — אלת'רב אלמג'טי אלגוף 'the caul that covers the entrails').",
        "source": "lane",
        "variants": [
            "אלת'רב", "ואלת'רב",
            "באלת'רב", "ות'רב",
            "ת'רוב", "אלת'רוב",
        ],
    },
    {
        "id": "ibham-thumb",
        "lemma_ja": "אבהאם",
        "lemma_ar": "إِبْهَام",
        "root": "b-h-m",
        "pos": "noun (m.)",
        "gloss_en": "thumb (of the hand); big toe (of the foot)",
        "gloss_he": "בֹּהֶן (יָד אוֹ רֶגֶל)",
        "saadia_note": "Saadia's regular gloss for Hebrew בֹּהֶן — both 'thumb of the right hand' and 'big toe of the right foot' in the consecration of priests (Exod 29:20: עלי' אבהאם אידיהם אלאיאמין) and the cleansing of the leper (Lev 14:14, 14:17, 14:25, 14:28).",
        "source": "lane",
        "variants": [
            "אלאבהאם", "ואלאבהאם",
            "ואבהאם", "באלאבהאם",
            "אבהאם ידה", "אבהאם רגלה",
            "אבאהים", "אלאבאהים",
        ],
    },
    {
        "id": "kamal-completion",
        "lemma_ja": "כמאל",
        "lemma_ar": "كَمَال",
        "root": "k-m-l",
        "pos": "noun (m.)",
        "gloss_en": "completion, perfection, fulfillment; (technical, in Saadia) the ordination / consecration installment-offering",
        "gloss_he": "מִלּוּאִים (קרבן ההקדשה)",
        "saadia_note": "Saadia's regular technical gloss for Hebrew מִלּוּאִים ('ordination-installment') in the priestly-consecration passages (Exod 29:22, 26, 27, 31, 34: כבש אלכמאל 'the ram of the ordination'; Lev 8:22, 28-29, 31, 33). The Hebrew מילוי 'filling [of the hand]' and Arabic kamāl 'completion' are conceptually parallel.",
        "source": "lane",
        "variants": [
            "אלכמאל", "ואלכמאל",
            "וכמאל", "באלכמאל",
            "כבש אלכמאל",
            "אכמאל", "אלאכמאל",
            "כאמל", "אלכאמל",
        ],
    },
    {
        "id": "miqʿad-stand",
        "lemma_ja": "מקעד",
        "lemma_ar": "مِقْعَد",
        "root": "q-ʿ-d",
        "pos": "noun (m.)",
        "gloss_en": "stand, base, seat, pedestal (the supporting base of a vessel)",
        "gloss_he": "כֵּן, מַעֲמָד, בָּסִיס",
        "saadia_note": "Saadia's regular gloss for Hebrew כֵּן ('stand, base') of the laver (Exod 30:18; 30:28; 31:9; 35:16; 38:8; 39:39; 40:11; Lev 8:11 — אלחוץ' ומקעדה 'the laver and its stand').",
        "source": "lane",
        "variants": [
            "אלמקעד", "ואלמקעד",
            "ומקעד", "באלמקעד", "ללמקעד",
            "מקעדה", "מקעדהא",
            "מקאעד", "אלמקאעד",
        ],
    },
    {
        "id": "abyad-white",
        "lemma_ja": "אביצ'",
        "lemma_ar": "أَبْيَض",
        "root": "b-y-ḍ",
        "pos": "adjective (color)",
        "gloss_en": "white",
        "gloss_he": "לָבָן",
        "saadia_note": "Saadia's regular gloss for Hebrew לָבָן (the color, not the personal name). Most prominent in the leprosy-diagnosis passages (Lev 13 passim — אביצ'א 'white', בקעה ביצ'א 'a white spot').",
        "source": "lane",
        "variants": [
            "אביצ", "אביצא", "אביצ'א",
            "ואביצ'", "ואביצ'א",
            "ביצ'", "אלביצ'", "ואלביצ'",
            "ביצ'א", "אלביצ'א", "ואלביצ'א",
            "ביצ'אא", "אלביצ'אא",
            "ביצ' ", "ביצ",
        ],
    },
    {
        "id": "sawʾa-pudenda",
        "lemma_ja": "סוה",
        "lemma_ar": "سَوْأَة",
        "root": "s-w-ʾ",
        "pos": "noun (f.)",
        "gloss_en": "nakedness, pudenda; that which it is shameful to expose; (idiomatic, in Saadia) the genital sphere of a forbidden relative",
        "gloss_he": "עֶרְוָה",
        "saadia_note": "Saadia's regular euphemistic gloss for Hebrew עֶרְוָה in the forbidden-relations chapter (Lev 18; Lev 20). Form: 'do not uncover the pudenda of X' = לא תכשף סוות X (Lev 18:7-19; Deut 27:20).",
        "source": "lane",
        "variants": [
            "אלסוה", "ואלסוה",
            "סות", "סוות", "וסוות",
            "סוותה", "סותה",
            "סוותהא", "סותהא",
            "סוותכם", "סוותהם", "סוותך",
            "סוואת", "אלסוואת",
        ],
    },
    {
        "id": "musmata-solid",
        "lemma_ja": "מצמת",
        "lemma_ar": "مُصْمَت",
        "root": "ṣ-m-t",
        "pos": "passive participle / adjective",
        "gloss_en": "solid, of one piece, hammered/turned out from a single mass (not assembled)",
        "gloss_he": "מִקְשָׁה (אחת)",
        "saadia_note": "Saadia's regular gloss for Hebrew מִקְשָׁה — describing the construction of the silver trumpets (Num 10:2: מן פצה מצמתה 'of solid silver') and the menorah (Num 8:4: והד'ה צנעה' אלמנארה מצמתה ד'הב 'and this is the workmanship of the lampstand — solid gold'; Exod 25:18, 31, 36; 37:7, 17, 22).",
        "source": "lane",
        "variants": [
            "אלמצמת", "ואלמצמת",
            "מצמתה", "אלמצמתה", "ומצמתה",
            "מצמתא",
        ],
    },
    {
        "id": "markaz-center",
        "lemma_ja": "מרכז",
        "lemma_ar": "مَرْكَز",
        "root": "r-k-z",
        "pos": "noun (m.)",
        "gloss_en": "central position, station, central encampment-point; (in Saadia) the central / leading encampment of a tribal division",
        "gloss_he": "מַחֲנֶה, מַעֲמָד הַמֶּרְכָּז",
        "saadia_note": "Saadia's regular gloss for Hebrew דֶּגֶל ('standard, tribal-division banner') in the encampment-layout passages (Num 2 passim, Num 10:14-25 — מרכז עסכר X 'the central encampment of the troop of X').",
        "source": "lane",
        "variants": [
            "אלמרכז", "ואלמרכז",
            "ומרכז", "באלמרכז",
            "מראכז", "אלמראכז", "ומראכז",
            "מרכזה", "מרכזהא", "מרכזהם", "מרכזכם",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "ammihud-name",
        "lemma_ja": "עמיהוד",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Ammihud — father of Elishama (chieftain of Ephraim in the wilderness census; Num 1:10; 2:18; 7:48, 53; 10:22)",
        "gloss_he": "עַמִּיהוּד",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ועמיהוד", "לעמיהוד", "בעמיהוד",
            "אבן עמיהוד",
        ],
    },
    {
        "id": "enan-name",
        "lemma_ja": "עינן",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Enan — father of Ahira (chieftain of Naphtali in the wilderness census; Num 1:15; 2:29; 7:78, 83; 10:27)",
        "gloss_he": "עֵינָן",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ועינן", "לעינן", "בעינן",
            "אבן עינן",
        ],
    },
    {
        "id": "paran-place",
        "lemma_ja": "פארן",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Paran — the wilderness south of Canaan and east of the Sinai peninsula; major staging-point for the Israelite itinerary (Num 10:12; 12:16; 13:3, 26; Gen 21:21; Deut 1:1; 33:2; 1 Sam 25:1; Hab 3:3)",
        "gloss_he": "פָּארָן",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ופארן", "לפארן", "בפארן",
            "ברייה' פארן", "ברייה פארן",
            "אלפארן",
        ],
    },
    {
        "id": "reuel-name",
        "lemma_ja": "רעואל",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Reuel — (1) son of Esau and Basemath (Gen 36:4, 10, 13, 17; 1 Chr 1:35, 37); (2) Midianite priest, father-in-law of Moses (Exod 2:18; Num 10:29); (3) father of Eliasaph the Gadite chieftain (Num 2:14)",
        "gloss_he": "רְעוּאֵל",
        "notes": "Sometimes identified with Jethro / Hobab (Num 10:29 names Reuel as the father of Hobab the father-in-law of Moses; Exod 2:18 names Reuel directly as Moses' father-in-law).",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ורעואל", "לרעואל", "ברעואל",
            "אבן רעואל",
        ],
    },
]


VARIANTS_PATCH = {
    "thalath-three":  ["ותלאת'ין", "תלאת'ין", "אלת'לאת'ין", "ות'לאת'ין"],
    "iʿta-give":      ["אעטיכם", "ואעטיכם", "פאעטיכם",
                       "יעטיכם", "ויעטיכם", "תעטיכם", "נעטיכם"],
}

STARTER_VARIANTS_PATCH = {}


def main():
    lane_path = pathlib.Path("data/dictionary-lane.json")
    starter_path = pathlib.Path("data/dictionary-starter.json")
    d = json.loads(lane_path.read_text())
    ds = json.loads(starter_path.read_text())

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

    by_id_s = {e["id"]: e for e in ds["entries"]}
    starter_variant_added = 0
    for entry_id, new_variants in STARTER_VARIANTS_PATCH.items():
        if entry_id not in by_id_s:
            variant_skipped.append((entry_id, "id not found in starter"))
            continue
        target = by_id_s[entry_id]
        existing_variants = target.setdefault("variants", [])
        for v in new_variants:
            if v in existing_variants:
                variant_skipped.append((entry_id, f"already had {v}"))
                continue
            existing_variants.append(v)
            starter_variant_added += 1

    lane_path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    starter_path.write_text(json.dumps(ds, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())
    json.loads(starter_path.read_text())

    print(f"Added {added} new entries (lane). Skipped: {len(skipped)}")
    for s, reason in skipped:
        print(f"  - {s}: {reason}")
    print(f"Added {variant_added} lane variants + {starter_variant_added} starter variants. Skipped: {len(variant_skipped)}")
    for s, reason in variant_skipped:
        print(f"  - {s}: {reason}")
    print(f"Total lane entries: {len(d['entries'])}")


if __name__ == "__main__":
    main()

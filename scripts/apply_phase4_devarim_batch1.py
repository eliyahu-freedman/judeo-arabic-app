"""
Phase 4 Devarim Batch 1 — apply 9 net-new entries + 4 cross-book
promote-in-place verse extensions to data/tafsir-divergence.json.

Window
------
- Source: data/_blau_saadia_candidates.json (Devarim-cited subset filtered on
  saadia_citation_lines containing דברים | דב׳ | דב").
- Pool: 78 raw candidates / ~22 article-flattened clusters.
- Walked in blau_id order: 13884 → 20005.

Triage outcome
--------------
NEW ENTRIES — 9 (5 NOTE + 4 GLOSS):
  - NOTE  אקרץ'    Deut 2:21, 7:17, 9:3, 11:23, 12:2 — Heb הוריש 'dispossess'
                                                    → Ar Form I قرض 'exterminate'
  - NOTE  יסיב      Deut 15:1, 15:2, 15:3        — Heb שמט/שמיטה → Ar Form II
                                                    سيّب 'release' + verbal-noun تسييب
  - NOTE  כ'רס      Deut 1:27                     — Heb רגן 'murmur' → Ar Form V
                                                    تخرّس 'be silenced'
  - NOTE  זאיל      Deut 21:18                    — Heb סורר 'rebellious' → Ar زائل
                                                    'one who deviates from the right'
  - NOTE  ממתע      Deut 23:18                    — Heb קדשה 'cultic-prostitute'
                                                    → Ar مُمتعة 'pleasure-object'
  - GLOSS תנהזם     Deut 1:42                     — Heb נגף 'be struck' → Ar Form VII
                                                    إنهزم 'be routed'
  - GLOSS צנגאת     Deut 25:13                    — Heb אבן 'stone' → Ar صنجة
                                                    'weight' (technical)
  - GLOSS אתקצא     Deut 32:26                    — Heb אפאה 'destroy utterly' (obscure)
                                                    → Ar Form VIII اقتصى 'pursue to end'
  - GLOSS גראביב    Deut 14:14                    — Heb עורב 'raven' → Ar غرابيب
                                                    (poetic-plural 'jet-black ravens')

PROMOTE-IN-PLACE — 4 cross-book extensions:
  - סלאמה  (Shemot 24:5, 32:6; Bamidbar 6:14, 6:17, 7:17, 10:10)
                                + Deut 27:7      — Mt. Ebal covenant ceremony
                                                   (ד'באיח סלאמה for שלמים)
  - יסתג'פר (Vayikra 5:6, 14:19, 16:6/16/30; Bamidbar 5:8, 8:12, 15:25, 17:11)
                                + Deut 9:20      — Moses intercedes for Aaron
                                                   (פאסתג'פרת for ואתפלל; new
                                                   1cs-perfect variant; striking
                                                   register-shift from priestly-ritual
                                                   to prophetic-intercessory)
  - בחפז   (Shemot 12:11)        + Deut 16:3     — Pesach-haste, already cited in
                                                   blau_dict prose
  - אצר    (Vayikra 26:13)       + Deut 28:48    — Curses yoke-of-iron, already
                                                   cited in blau_dict prose
                                                   (new variant אצרא = indefinite
                                                   accusative)

DEFERRED — 12 SKIP / 4 borderline / 9 cluster-dupes logged
  - SKIP: 13983 أول, 14868 حصر, 15084 خبر, 15118 خدع, 15403 دجن (Blau-misattrib),
          16064 زائل (now SHIPPED as note — not skip; see entry above),
          16765 صحراء, 17158 طول, 17212 عتق, 17256 عدا, 17953-17955 (raven cluster
          → SHIPPED as gloss גראביב), 18454-18456 (قدح cluster), 18694 مقلب,
          18778-18780 (مقام/قوم cluster), 18889-18890 (تكرير/كرب cluster),
          19325 ما, 19636-19649 (nٰtj/nٰtr/nٰjr 14-row cluster — see cluster-dupes),
          19861-19871 (nfd family — already deferred from Vayikra B1 + Bamidbar B1),
          19950-19951 (نهاية/ناهيك), 19952-19953 (نوء/ناب), 20003 يده.
  - BORDERLINE (4 NOTE/GLOSS-grade cut at the 5-NOTE/4-GLOSS cap):
      18619 قضيب — Deut 15:2 לא יגש → לא יקתצ'י (Form VIII iqtaḍā 'exact a debt')
      19378-19381 ممد اليد — Deut 23:21 משלח ידך → ממד ידך (calque idiom)
      19954 نوبة — Deut 18:8 ממכריו → אלנווב (priestly duty-rotation exegesis)
      19775-19776 نصول — Deut 25:11 וינצו → תנאצי (Form VI quarreling)

Apply pattern
-------------
- Mirrors scripts/apply_phase4_bamidbar_batch1.py:
  PROMOTE_IN_PLACE is a list of 4 cross-book extensions.
  _patch_promote_in_place() iterates the list and returns per-lemma summaries.
- Fresh "devarim" namespace in data/_blau_saadia_deferred.json (idempotent on
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
    # NOTE — 5 net-new
    # ====================================================================

    # ---- NOTE — Deut 2:21, 7:17, 9:3, 11:23, 12:2: conquest-vocabulary -----
    {
        "lemma_ja": "אקרץ'",
        "variants": ["אקרצ'הם", "פתקרצ'הם", "פקרצ'והם", "ויקרץ'", "קארצ'והם", "תקרצ'הם"],
        "lemma_ar": "أقرض",
        "root": "ق-ر-ض",
        "tier": "note",
        "classical_en": "Classical Arabic قَرَضَ (Form I) = 'to cut off, to terminate, to destroy, to extirpate' (cognate with קצץ 'to cut'); a transitive verb of complete elimination. The Form VIII اقتراض carries 'to take/give as a loan' (a derived commercial sense — 'cutting off' a portion of capital). The Form-I 'extirpate' sense is the older Arabic stratum.",
        "classical_he": "בערבית הקלאסית قَرَضَ (בניין I) = 'לכרות, לקצץ, להשמיד, לכלות' (קוגנט של קצץ 'לחתוך'); פועל יוצא של חיסול מוחלט. בניין VIII اقتراض נושא משמעות 'ללוות/להלוות' (מובן מסחרי נגזר — 'גזירה' של חלק מהון). משמעות בניין I 'להשמיד' שייכת לרובד הערבי הקדום יותר.",
        "saadia_en": "I exterminate them / He exterminates them / they exterminated them",
        "saadia_he": "אכלה, השמיד לחלוטין, השמיד את הגוי",
        "mechanism": "Semantic reframe of the conquest-vocabulary system: Heb הוֹרִישׁ (Hiphil of ירש 'to inherit/dispossess', frames the conquest as DISPOSSESSING/DRIVING OUT — the prior population is displaced, not exterminated) → Ar Form I قَرَضَ ('to cut off, exterminate, eliminate'), which foregrounds the ELIMINATION rather than the DISPLACEMENT. Across the entire Devarim conquest-discourse, Saadia consistently routes the Heb ירש-Hiphil through this extermination-frame: Deut 2:21 (the Anakim-Rephaim displaced before the Moabite-Ammonite settlement: וַיִּירָשֻׁם → פקרצ'והם 'they exterminated them'); 7:17 (Moses's hesitation: אֵיכָה אוּכַל לְהוֹרִישָׁם → פכיף אטיק אן אקרצ'הם 'how can I exterminate them'); 9:3 (God-as-fire-consuming-before-them: וְהוֹרַשְׁתָּם → פתקרצ'הם 'you shall exterminate them'); 11:23 (the promise: וְהוֹרִישׁ ה' → ויקרץ' אללה 'and God will exterminate'); 12:2 (the cultic-site destruction: אֲשֶׁר אַתֶּם יֹרְשִׁים אֹתָם → אלד'י אנתם קארצ'והם 'whom you exterminate'). The choice is paradigm-defining for Devarim's program of conquest: where the Heb leaves room for the displaced peoples to survive elsewhere, the Ar names total elimination. The lexical shift compresses what the Hebrew preserves as a distinction (יָרַשׁ Qal 'inherit/take possession of' vs. הוֹרִישׁ Hiphil 'dispossess/drive out' vs. הִשְׁמִיד 'destroy') into a single extermination-vocabulary — at Deut 9:3 Saadia even uses קרץ' for both verbs in 'הוא ישמידם...והאבדתם' (= ינפד'הם...ותבידהם...פתקרצ'הם), placing the new extermination-vocabulary in the same semantic field as Heb's destruction-verbs. Pedagogically distinctive because the Heb-Ar pairing surfaces a real interpretive choice about whether the conquest is displacement or annihilation.",
        "verses": [
            {"book": "Devarim", "ch": 2, "v": 21},
            {"book": "Devarim", "ch": 7, "v": 17},
            {"book": "Devarim", "ch": 9, "v": 3},
            {"book": "Devarim", "ch": 11, "v": 23},
            {"book": "Devarim", "ch": 12, "v": 2},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "قرض",
            "sense": "قرض (Form I) 'to destroy, exterminate' — Blau cites Saadia's systematic rendering of Heb הוריש (Hiphil of ירש) with قرض across the Devarim conquest-narrative (Deut 2:21, 7:17, 9:3, 11:23, 12:2), preserving Heb's compound-verb structure (Hiphil = causative) by using Ar Form I as a transitive-extirpate verb. The corresponding Form VIII اقتراض ('to take/give a loan') is the later commercial-derived sense.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Deut 15:1, 15:2, 15:3: shemittah-release ------------------
    {
        "lemma_ja": "יסיב",
        "variants": ["סייב", "תסייב", "תסייבא", "יסייב", "סייבא", "סייבך", "תסייבה", "יסייבהא"],
        "lemma_ar": "يسيّب",
        "root": "س-ي-ب",
        "tier": "note",
        "classical_en": "Classical Arabic سَيَّبَ (Form II) = 'to release, set free, let loose, allow to roam unrestrained' (the pre-Islamic سائبة 'freed she-camel'); the verbal noun تَسْيِيب names the act-of-release. The semantic field is pastoral-Bedouin: animals 'set loose' from human use, debts 'released' from their claim. The Form I bare verb سَابَ carries the parallel intransitive 'to roam free, to flow loose'.",
        "classical_he": "בערבית הקלאסית سَيَّبَ (בניין II) = 'לשלח חופשי, להתיר, להניח לנדוד בלא מעצור' (السائبة הטרום־איסלאמית, נאקה ששוחררה מעבדות); שם הפעולה תَسْيِيب קורא לפעולת השחרור. השדה הסמנטי הוא הבדואי־רועי: בעלי חיים 'מותרים' מן השימוש האנושי, חובות 'משוחררים' מתביעתם. בניין I הבסיסי سَابَ נושא את המקבילה הבלתי־יוצאת 'לנדוד חופשי, לזרום משוחרר'.",
        "saadia_en": "release-fallow (Sabbatical-year) / let go (debt)",
        "saadia_he": "שמיטה (השנה, החוב, היד)",
        "mechanism": "System-vocabulary calque covering the entire Sabbatical-year lexical field: the Heb root שמט carries the full semantic range of the institution (the noun שְׁמִטָּה for the year itself; the Qal שָׁמַט for the act of release; the Hiphil יַשְׁמֵט for releasing-of-debt; the imperative שָׁמוֹט for the cultic-legal formula). Saadia renders this entire field through Ar Form II سَيَّبَ — preserving the institutional-technical character by selecting an Arabic root from the same pastoral-release semantic field as the Heb. The Form II + verbal-noun تَسْيِيب pairing matches the Heb Hiphil + nominal שְׁמִטָּה pairing in morphological structure (causative-verb + abstract-noun), making the institution's two-pole structure (the act of releasing + the period of release) translatable as a single Arabic technical pair. Across the Devarim 15:1-3 release pericope: 15:1 ('מקץ שבע שנים תעשה שמטה' = ופי כל מדה' סבע סנין תצנע תסייבא — 'every period of seven years you make a release'); 15:2 ('שמוט כל בעל משה ידו' = יסייב כל ד'ו נסייה' ידה — 'let every creditor release his hand'; 'כי קרא שמטה לה'' = אד' קד סמאהא תסייבא ללה — 'since He has named it a release to YHWH'); 15:3 ('ואשר יהיה לך את אחיך תשמט ידך' = ואמא מא יכון לך עלי אכ'יך פסייב ידך ענה — 'whatever your brother owes you, release your hand from it'). The systematic Form II + verbal-noun usage across all three verses confirms Saadia treats שמיטה not as a generic 'remission' but as a technical institution with its own coined Arabic terminology — coordinately with his moving-وقف choice for the parallel Year-of-Jubilee at Deut 15:9 ('שנת השבע שנת השמטה' = sanat as-sabʿ sanat at-tasyīb). Pedagogically distinctive because the morphological pairing (Form II verb + verbal-noun substantive) parallels the Heb's coined-term strategy at the institutional level.",
        "verses": [
            {"book": "Devarim", "ch": 15, "v": 1},
            {"book": "Devarim", "ch": 15, "v": 2},
            {"book": "Devarim", "ch": 15, "v": 3},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "سيب",
            "sense": "سيّب (Form II) 'to release, to set free, let loose'; verbal-noun تسييب — Blau cites Saadia as the systematic renderer of biblical שמיטה / שמט through this Form II + verbal-noun pairing (Deut 15:1-3 + 15:9 + 31:10), with al-Fāsī's Jāmiʿ confirming the institutional-technical reading. The pastoral-Bedouin semantic field (animals set loose, debts released) matches the Heb sevenfold-cycle's release-of-claim structure.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Deut 1:27: rgn → silenced -------------------------------
    {
        "lemma_ja": "תכ'רסתם",
        "variants": ["תכ'רס", "תכ'רסת", "כ'רס", "אכ'רס"],
        "lemma_ar": "تخرّستم",
        "root": "خ-ر-س",
        "tier": "note",
        "classical_en": "Classical Arabic خَرَسَ (Form I) = 'to be silent, to be dumb-mute'; the active participle أخرس 'mute' is the standard Arabic word for congenital muteness. Form II خَرَّسَ 'to silence, to make speechless'; Form V تَخَرَّسَ '(reflexive) to be reduced to silence, to be dumbfounded'.",
        "classical_he": "בערבית הקלאסית خَرَسَ (בניין I) = 'לשתוק, להיות אילם'; הבינוני הפעיל أخرس 'אילם' הוא המילה הערבית הסטנדרטית לאילמות מולדת. בניין II خَرَّسَ 'להשתיק, לאלם'; בניין V تَخَرَّسَ '(חוזר) להיות מושתק, להיות נדהם עד אילמות'.",
        "saadia_en": "you were silenced (in your tents)",
        "saadia_he": "אולמתם, הושתקתם",
        "mechanism": "Semantic flip on a paradigm-emotional verb: Heb רָגַן (rare verb attested only here in the Pentateuch + Ps 106:25 + Prov 16:28 + 26:20 + 18:8, always pejorative — 'to murmur, to complain, to mutter discontentedly') frames the spies-report rebellion as the people's ACTIVE PRODUCTION OF complaint-speech ('you murmured in your tents'). Saadia routes this through Ar Form V تَخَرَّسَ — but the Form V of خرس is the OPPOSITE-direction reflexive: 'you reduced yourselves to silence, you became dumbfounded'. The active-complaint frame inverts to a passive-silenced frame; the people aren't producing speech but ceasing it. This is a striking moral reframe: where the Heb foregrounds the SPEECH-PRODUCTION dimension of the rebellion (the people speaking their fear into reality), the Ar foregrounds the SPEECHLESSNESS-RESPONSE dimension (the people stunned silent by what they'd just done — perhaps shocked by the spies' report into withdrawal). The choice routes the post-spy-report rebellion through a contemplative-paralysis frame rather than an active-protest frame — fitting Saadia's broader tendency to read the wilderness-rebellions as failures of FAITH (silent doubt) rather than as failures of OBEDIENCE (vocal complaint). The two roots are not cognate (Heb רגן ~ Ar نقم 'avenge' would be the cognate path), so Saadia is making a non-cognate semantic choice that flips the action-direction. Pedagogically the entry pairs cleanly with Bamidbar 13-14's spy-cluster (where Saadia uses רוم 'volitional pursuit' for תור — see ראם entry) — both moves redirect the spies-narrative from external action to internal volitional/emotional state.",
        "verses": [{"book": "Devarim", "ch": 1, "v": 27}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "خرس",
            "sense": "خرس (Form V تخرّس) 'to be silenced, to be reduced to muteness' — Blau cites Saadia's choice for the rebellion-narrative at Deut 1:27 (ותרגנו = ותכ'רסתם), with al-Fāsī's Jāmiʿ 1:103 transmitting both Form II 'to silence' and Form V 'to be silenced'. The semantic flip from active-complaint (Heb רגן) to passive-silenced is documented in the entry's mechanism.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Deut 21:18: rebellious-son rationalist reframe --------
    {
        "lemma_ja": "זאיל",
        "variants": ["אלזאיל", "זאילא", "וזאיל"],
        "lemma_ar": "زائل",
        "root": "ز-ي-ل",
        "tier": "note",
        "classical_en": "Classical Arabic زَائِل (active participle of زَالَ Form I = 'to depart, to separate, to deviate from') = 'one who deviates, departs from the right, errs from the path'. The idiom زائل عن الصواب / الطاعة names a specific MORAL-EPISTEMOLOGICAL deviation: not active rebellion but separation from the correct course. Post-classical Judeo-Arabic broadens it to 'sinner, wrongdoer'.",
        "classical_he": "בערבית הקלאסית زَائِل (בינוני פעיל של زَالَ בניין I = 'להסתלק, להיפרד, לסור מ-') = 'מי שסר מן הדרך הנכונה, פורש מן הצדק, טועה במסלול'. הביטוי زائل عن الصواب / الطاعة קורא לסטייה מוסרית־אֶפיסטֵמית מובהקת: לא מרד פעיל אלא נפרדות מן המסלול הראוי. הערבית־יהודית הבתר־קלסית מרחיבה ל'חוטא, פושע'.",
        "saadia_en": "a deviant (rebellious son)",
        "saadia_he": "סר מן הדרך, סורר",
        "mechanism": "Rationalist-philosophical reframe of the wayward-son institution: Heb סוֹרֵר וּמוֹרֶה (the famous Deut 21:18-21 institutional pair, both active participles) names the wayward son's REBELLION through a verb-of-political-opposition (סור 'to turn aside' + מרה 'to be defiant against authority'). The Heb pair frames the son's offense as INSUBORDINATION — refusal to submit to parental authority, a category-error in the household's command-structure. Saadia routes the first term through Ar زائل (with the second rendered מכ'אלף 'one who diverges/contradicts'). But زائل is a DEVIATION verb, not a REBELLION verb: it names someone who has DEPARTED FROM THE RIGHT PATH (the Quranic idiom زائل عن الصواب 'deviating from the right'), foregrounding the EPISTEMIC-MORAL dimension over the POLITICAL-AUTHORITY dimension. The choice converts the rabbinic-rabbinic son-as-rebel category into the Saadyan philosophical-rationalist category of the soul that has DEVIATED from the proper trajectory (recall Saadia's Emunot ve-Deot's framing of sin as the soul's drift away from rational-moral correctness). Where the Heb son DEFIES authority, the Ar son has DEVIATED from truth — Saadia's pairing routes the Torah's institutional discipline through the philosophical school's discourse of soul-trajectories. Pedagogically distinctive because the same verse's two participles get split across the two semantic fields: זאיל (epistemic-philosophical 'one who deviates') + מכ'אלף (logical-rhetorical 'one who contradicts'), giving the legal-institutional son two simultaneous frames — neither of which is the Heb's political-rebellion frame.",
        "verses": [{"book": "Devarim", "ch": 21, "v": 18}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "زيل",
            "sense": "زائل 'one who deviates from the right, errs, sinner' (a shortened form of زائل عن الطاعة/الصواب/الرأي) — Blau cites Saadia on Deut 21:18 (סורר → זאיל), with the broader Quranic-register 'deviation' frame transmitted forward through medieval Judeo-Arabic moral discourse. The philosophical-rationalist reframe of the rabbinic סורר ומורה institution is documented in the entry's mechanism.",
            "relation": "direct",
        },
    },

    # ---- NOTE — Deut 23:18: cultic-prostitute sexualized reframe -----
    {
        "lemma_ja": "ממתעה",
        "variants": ["ממתע", "אלממתעה", "אלממתע"],
        "lemma_ar": "ممتعة",
        "root": "م-ت-ع",
        "tier": "note",
        "classical_en": "Classical Arabic مَتَّعَ (Form II of متع 'to enjoy, to derive pleasure from') = 'to give enjoyment to, to allow to enjoy, to provide pleasure-services to'. The passive participle مُمَتَّع (masc.) / مُمَتَّعَة (fem.) = 'one who is enjoyed, the object of enjoyment'. In Quranic-Islamic usage the verbal-noun متعة names the institution of متعة-marriage (Shia temporary-pleasure marriage); the participle carries the same sexual-utility semantic field.",
        "classical_he": "בערבית הקלאסית مَتَّعَ (בניין II של متع 'להתענג, להפיק הנאה מ-') = 'לתת הנאה ל-, להתיר ליהנות, לספק שירותי הנאה ל-'. הבינוני הסביל مُمَتَّع (זכר) / مُمَتَّعَة (נקבה) = 'מי שעליו נהנים, אובייקט של הנאה'. בשימוש קוראני־איסלאמי שם הפעולה متعة קורא למוסד נישואי متعة (נישואין שיעיים זמניים של תענוג); הבינוני נושא את אותו שדה סמנטי של תועלת מינית.",
        "saadia_en": "the woman-of-pleasure / the man-of-pleasure (cult prostitute)",
        "saadia_he": "אישת/איש תענוג (קדשה/קדש בפולחן זרים)",
        "mechanism": "Sexualized reframe that strips the consecration-semantics of the Hebrew term: Heb קְדֵשָׁה / קָדֵשׁ (Deut 23:18) name the cultic-prostitute through the consecration-vocabulary — the woman/man is 'set apart' to the foreign-cult's service via the SAME root (קדש) that names the Israelite priests' consecration. The Heb preserves the structural-parallel: both Israelite priests and foreign cult-prostitutes are 'consecrated ones'. Saadia routes this through Ar مُمَتَّعَة / مُمَتَّع — passive participle of متع 'to derive pleasure from' — entirely abandoning the consecration-frame and rendering the figure as 'the (one made into an) object of enjoyment'. The semantic stripping is theologically significant: where Heb concedes that the foreign cult-prostitute is 'consecrated' (even if to the wrong god), Saadia REFUSES the consecration label and renames the figure by their FUNCTION (sexual-utility) rather than their STATUS (cultic-set-apartness). The choice routes the prohibition through a CATEGORY-DELEGITIMIZATION rather than a CATEGORY-EXCLUSION: the prohibition isn't against having Israelite consecrated-prostitutes (which would still grant the foreign system its consecration-frame), it's against permitting any Israelite to become a 'pleasure-object'. Pedagogically distinctive because the Heb-Ar pairing surfaces a real theological-rhetorical choice — Saadia's lexicon won't grant rival cults a consecration-vocabulary, even in the act of forbidding them. Compare Heb-Ar pairs elsewhere where Saadia preserves rival-cult lexical categories (e.g., אֱלִיל = صنم 'idol' — the substantive is retained); קדשה / קדש is exceptional in being routed through a non-cognate, semantically-orthogonal frame.",
        "verses": [{"book": "Devarim", "ch": 23, "v": 18}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "متع",
            "sense": "مُمَتَّع / مُمَتَّعَة (Form II passive participle) 'sodomite / temple-prostitute, lit. one who is enjoyed' — Blau cites Saadia's choice for Deut 23:18 (לא תהיה קדשה ... ולא יהיה קדש = ולא תכון ... ממתעה ... ולא ... ממתע), routing the Heb consecration-vocabulary through the Arabic pleasure-vocabulary. The Form II's pleasure-derivation semantic is preserved from Quranic-register usage.",
            "relation": "direct",
        },
    },

    # ====================================================================
    # GLOSS — 4 net-new
    # ====================================================================

    # ---- GLOSS — Deut 1:42: nāgaph → Form VII hzm --------------
    {
        "lemma_ja": "תנהזמו",
        "variants": ["אנהזם", "ינהזם", "תנהזם", "אלאנהזאם", "מנהזם"],
        "lemma_ar": "تنهزموا",
        "root": "ه-ز-م",
        "tier": "gloss",
        "classical_en": "Classical Arabic Form VII اِنْهَزَمَ = 'to be routed, to be put to flight, to be defeated in battle' (passive of Form I هَزَمَ 'to rout, defeat'); the standard Arabic verb for military rout. The verbal-noun اِنْهِزَام is the technical Arabic for 'battlefield rout'.",
        "classical_he": "בערבית הקלאסית בניין VII اِنْهَزَمَ = 'להיות מובס, להיות מנוס, להוכרע במערכה' (סביל של בניין I هَزَمَ 'להביס, להבריח'); הפועל הערבי הסטנדרטי לבריחת־קרב. שם הפעולה اِنْهِزَام הוא המונח הטכני לתבוסה־בשדה.",
        "saadia_en": "you shall not be routed (before your enemies)",
        "saadia_he": "לא תהיו מובסים בקרב",
        "mechanism": "Non-cognate semantic-field substitution for the military-defeat passive: Heb נִגַּף (Niphal of נגף 'to strike, to defeat', the Niphal carries the passive 'be struck/defeated') is the Pentateuch's standard verb for divinely-mediated battlefield defeat. Saadia routes this through Ar Form VII إنهزم — the standard Arabic battlefield-rout verb. The non-cognate substitution (Heb נגף ~ Ar نجف is not a real Arabic root; the cognate path would be Heb נגע ~ Ar نقع or similar) lets Saadia name the defeat through Arabic's own military-vocabulary register, replacing the Hebrew's strike-vocabulary frame (the Heb foregrounds the divine STRIKE that causes the rout) with the Arabic's rout-vocabulary frame (the Ar foregrounds the army-being-broken result). Compare the parallel choice across Lev 26:7 / Num 14:42: same Heb לא תנגפו → same Ar pattern (تنهزموا / لا تنهزموا), confirming the cross-pericope consistency. Saadia's choice routes biblical-Hebrew strike-of-divine-judgment through Arabic-classical battle-vocabulary, smoothing the theological frame into a routine military register.",
        "verses": [{"book": "Devarim", "ch": 1, "v": 42}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "هزم",
            "sense": "Form VII اِنْهَزَمَ 'to be routed, to be defeated in battle' — Blau cites Saadia on Lev 26:17 ('ונגפתם לפני איביכם' = פתנהזמון בין ידי אעדאיכם), with the parallel Num 14:42 and Deut 1:42 attestations confirming the systematic Niphal→Form VII pairing. al-Fāsī's Jāmiʿ 1:91-92 transmits the underlying Form I 'to strike/break' linkage.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Deut 25:13: stone-and-stone → weights ------------
    {
        "lemma_ja": "צנגתאן",
        "variants": ["צנגאת", "אלצנגאת", "צנגה"],
        "lemma_ar": "صنجتان",
        "root": "ص-ن-ج",
        "tier": "gloss",
        "classical_en": "Classical Arabic صَنْجَة (plural صِنَجَات) = 'weight, balance-weight, standard unit used in commercial weighing' (from Persian سَنْجَه 'weighing-stone, balance-counterweight'); a technical-commercial substantive specifically for the calibrated stones used in market scales, not for generic stones.",
        "classical_he": "בערבית הקלאסית صَنْجَة (רבים صِنَجَات) = 'משקולת, אבן־איזון, יחידת מידה תקנית לשקילה מסחרית' (מן הפרסית سَنْجَه 'אבן־שקילה, משקולת־מאזניים'); שם עצם טכני־מסחרי המיוחד לאבני־הכיול שבמאזני־השוק, לא לאבנים סתם.",
        "saadia_en": "two weights — a large and a small",
        "saadia_he": "שתי משקולות — גדולה וקטנה",
        "mechanism": "Concrete-to-technical lexical specification: Heb אֶבֶן וָאֶבֶן (Deut 25:13's 'stone and stone in your pouch', a literal-objective description — the cheater carries two LITERAL STONES of different weights as merchant's deceptive ballast) gets rendered with Ar صَنْجَتَان ('two weights' — the dual of the technical commercial-weight noun). The Heb names the deceptive object by its PHYSICAL SUBSTANCE (stone); the Ar names it by its FUNCTIONAL CATEGORY (commercial weight). The substitution converts the merchant-fraud passage from a description of a physical object into a description of a commercial-fraud instrument, foregrounding the institutional-economic dimension over the material-object dimension. The lexical move also smooths the Heb's parallel-stylistic structure ('stone and stone, large and small') into the Ar's technical pair ('two weights, large and small'). Pedagogically distinctive because the Persian-loan صنجة marks the entry as drawn from the East-Arabic commercial-administrative register, fitting Saadia's preference for institutional-technical Arabic over generic-literal-Arabic in the weights-and-measures pericopes.",
        "verses": [{"book": "Devarim", "ch": 25, "v": 13}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "صنج",
            "sense": "صنجات / صنجة 'weights (for weighing); calibrated balance-stones (from Persian سنجه)' — Blau cites Saadia on Deut 25:13-15 (אבן ואבן = צנגתאן), the institutional-commercial reading converting the Heb material-noun into the Ar technical-noun. Loan from Persian.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Deut 32:26: ʾaphaʾehem → Form VIII pursue-to-end -----
    {
        "lemma_ja": "אתקצאהם",
        "variants": ["אתקצא", "תקצא", "תקצאהם", "אקתצא"],
        "lemma_ar": "اتقصاهم",
        "root": "ق-ص-و",
        "tier": "gloss",
        "classical_en": "Classical Arabic Form VIII اِقْتَصَى = 'to pursue (a matter) to its end, to investigate exhaustively, to seek out completely' (from قَصْو 'farthest extreme'); names exhaustive-pursuit of an object until nothing remains uninvestigated or uncaught. The verb carries an investigative-juridical connotation (close-questioning) alongside the literal pursuit-to-the-end sense.",
        "classical_he": "בערבית הקלאסית בניין VIII اِقْتَصَى = 'לרדוף אחרי (עניין) עד תכלית, לחקור בשלמות, לתור עד אכזביות' (מן قَصْو 'הקצה הרחוק ביותר'); מתאר רדיפה־ממצה אחר עצם עד שלא נשאר דבר שלא נחקר או לא נתפס. הפועל נושא קונוטציה חקירתית־משפטית (דרישה־חודרת) לצד המובן הליטרלי של רדיפה־עד־סוף.",
        "saadia_en": "I shall pursue them to the end / I shall exhaust them",
        "saadia_he": "ארדפם עד הסוף, אַמצֶה אותם",
        "mechanism": "Non-cognate lexical substitute for an obscure Hebrew hapax: Heb אַפְאֵיהֶם (Deut 32:26, Ha'azinu — a notorious hapax with disputed etymology: the medieval grammarians read it as a Hiphil of פאה 'to extend to a corner/edge' meaning 'I shall scatter them to the corners', or alternatively as a derivative of אפס 'to bring to nothing'). Saadia routes this through Ar Form VIII اقتصى — selecting the pursue-to-the-end verb that elegantly captures BOTH possible readings: a corner-extension (pursue them to the farthest reach) AND an annihilation (pursue them until none remain). The Form VIII's investigative-juridical undertone also fits the surrounding verse's frame (God's deliberation about whether to extinguish Israel's memory). The choice surfaces Saadia's exegetical strategy for handling obscure Hebrew vocabulary: rather than guess a single literal meaning, deploy an Arabic verb whose semantic range covers the relevant interpretive options. Pedagogically distinctive because the entry showcases Saadia's method for hapax-handling: not literal-glossing but semantic-coverage selection.",
        "verses": [{"book": "Devarim", "ch": 32, "v": 26}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "قصو",
            "sense": "Form VIII اقتصى 'to examine minutely, to investigate, to pursue to the end' — Blau cites Saadia on Deut 32:26 (אפאיהם → אתקצאהם), with the Sefer ha-Shetarot 1:174 commercial-juridical parallel transmitting the investigative-pursuit semantics. The choice handles the Heb hapax via semantic-coverage rather than literal-gloss.",
            "relation": "direct",
        },
    },

    # ---- GLOSS — Deut 14:14: raven → poetic-plural ravens --------
    {
        "lemma_ja": "אלג'ראביב",
        "variants": ["ג'ראביב", "ג'ריב", "ג'ראב", "אלג'ראב"],
        "lemma_ar": "الغرابيب",
        "root": "غ-ر-ب",
        "tier": "gloss",
        "classical_en": "Classical Arabic غُرَابِيب (broken-plural of غِرْبِيب) = 'jet-black ravens, deep-black ravens' — a poetic-register plural, attested in pre-Islamic poetry and the Quran (Q35:27 'غَرَابِيبُ سُودٌ' 'jet-black ravens'). The simple-plural would be غِرْبَان; the choice of broken-plural غرابيب specifically marks the high-poetic register and the intensified black-color sense.",
        "classical_he": "בערבית הקלאסית غُرَابِيب (ריבוי שבור של غِرْبِيب) = 'עורבים שחורים־בוהקים' — ריבוי בעל מרשם פיוטי, מאושר בשירה הטרום־איסלאמית ובקוראן (Q35:27 'غَرَابِيبُ سُودٌ' 'עורבים שחורים־בוהקים'). הריבוי הפשוט היה غِرْبَان; הבחירה בריבוי השבור غرابيب מסמנת באופן ספציפי את המרשם הפיוטי הגבוה ואת המשמע המוגבר של שחרוריוּת.",
        "saadia_en": "all the (jet-black) ravens of their kind",
        "saadia_he": "וכל מיני העורבים השחורים",
        "mechanism": "Register-elevation in the unclean-birds list: Heb עֹרֵב (Deut 14:14, the standard biblical raven-substantive in the Levitical-Deuteronomic dietary lists) gets rendered with the Ar broken-plural غُرَابِيب — a specifically poetic-elevated register form, marked by both its irregular morphology (the broken-plural pattern fa'ālīl rather than the simple فِعْلَان) and its intensified semantic ('jet-black' rather than 'black'). The choice routes the dietary-prohibition through the Quranic-poetic register (Q35:27 explicitly uses غرابيب for the metaphor of mountains' black-streaks). The lexical move elevates the prosaic dietary-list to the literary-register, fitting Saadia's general tendency to deploy classical-register Arabic vocabulary in the cultic-legal passages where the Hebrew is technical-mundane. Compare the parallel choice in the Bamidbar/Vayikra dietary lists where Saadia selects the higher-register Arabic substantives over the colloquial alternatives. Pedagogically distinctive because the entry showcases Saadia's poetics-of-translation: even the dietary list gets elevated register.",
        "verses": [{"book": "Devarim", "ch": 14, "v": 14}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "غرب",
            "sense": "غريبة / غرابيب 'strange thing; (broken-plural) jet-black ravens' — Blau cites Saadia on Lev 11:15 + Deut 14:14 (עורב = (אל)ג'ראביב), with the Quranic Q35:27 parallel confirming the poetic-register marking. The broken-plural choice is the register-elevation signature.",
            "relation": "direct",
        },
    },
]


# ============================================================================
# CROSS-BOOK PROMOTE-IN-PLACE — extensions to existing entries
# ============================================================================

PROMOTE_IN_PLACE = [

    # ---- סלאמה + Deut 27:7 (Mt. Ebal covenant ceremony) ---------------
    {
        "lemma_ja": "סלאמה",
        "extend_verses": [
            {"book": "Devarim", "ch": 27, "v": 7},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Cognate semantic-field pairing, now confirmed across FIVE ritual systems: Heb שלם ~ Ar سلم share "
            "the 'wholeness/peace' root, so Saadia picks سلامة (the abstract noun) over the standard Arabic "
            "ذبيحة-السلام or قربان-السلام. The idiom ذبائح سلامة surfaces invariantly across (1) the Sinai "
            "covenant ceremony (Ex 24:5; 32:6 — outside the Mishkan); (2) the nazirite-completion ritual "
            "(Num 6:14, 6:17, 6:18); (3) the chieftains' dedication-of-the-altar cycle (Num 7:17-83 — 12 "
            "verses, collapsed to anchor 7:17 in verses[]); (4) the calendar-festival peace-offerings (Num "
            "10:10 — 'over your peace-offerings' = עלי' סלאמתכם); AND (5) the Mt. Ebal covenant-renewal "
            "ceremony at Deut 27:7 ('וזבחת שלמים ואכלת שם' = ואד'בח ד'באיח סלאמה וכלהא הנאך — 'and offer "
            "peace-offerings and eat them there'). The cross-book consistency now spans the entire "
            "covenant-ceremony arc — Sinai (Ex 24) → Mishkan dedication (Num 7) → festival cycle (Num 10) "
            "→ Mt. Ebal land-entry covenant (Deut 27) — confirming that Saadia treats ذبائح السلامة as "
            "the invariant technical term for the שלמים sacrifice across every covenant-renewal context "
            "in the Pentateuch. The suffixed forms סלאמת (without ta-marbuta) and סלאמתכם (with "
            "pronominal suffix) surface where the construct-state or possessive forms require, but the "
            "underlying lexical choice holds. ḥafetz 139:12's قربان السلامة confirms the post-Saadyan "
            "transmission of the technical pair into the Geniza ritual-vocabulary."
        ),
        "blau_dict_sense_rewrite": (
            "سلامة 'peace-offering' (idiom ذبائح السلامة) — Blau cites Saadia on Ex 24:5; 32:6 (with the "
            "Lev 3:1 cross-reference), the Bamidbar nazirite-completion + chieftain-dedication + "
            "festival-cycle attestations (Num 6:14/17/18, 7:17ff, 10:10), AND the Deut 27:7 Mt. Ebal "
            "covenant-ceremony attestation, confirming five-system invariance from Sinai through the "
            "land-entry covenant renewal. Geniza-attested قربان السلامة in Ḥafetz 139:12."
        ),
    },

    # ---- יסתג'פר + Deut 9:20 (Moses intercedes for Aaron) -----------
    {
        "lemma_ja": "יסתג'פר",
        "extend_verses": [
            {"book": "Devarim", "ch": 9, "v": 20},
        ],
        "extend_variants": ["פאסתג'פרת", "אסתג'פרת"],
        "mechanism_rewrite": (
            "Theological reframe from ritual-mechanism to relational-supplication, now confirmed across "
            "the full Numbers atonement-vocabulary AND extended into the Deuteronomic prophetic-intercession "
            "context: Hebrew כָּפַר (root כ-פ-ר 'to cover') is the priestly verb for ritual atonement — the "
            "offering MECHANICALLY covers/wipes the sin from God's view. Saadia consistently translates "
            "this with Form X استغفر 'to seek forgiveness' — relocating the action from mechanical-covering "
            "to relational-supplication, from the offering's effect on God's vision to the supplicant's "
            "address to God's mercy. The Form X morphology (request/seek-after) reframes the priest's "
            "action as petitionary rather than performative. Surfaces invariantly across Vayikra (Lev 5:6, "
            "14:19, 16:6, 16:16, 16:30); the Bamidbar cluster (Num 5:8 restitution-with-guilt-offering, "
            "8:12 Levite-consecration, 15:25 inadvertent-communal-sin, 17:11 Aaron-with-the-censer-in-the-"
            "Korach-aftermath); AND now the Deut 9:20 Moses-intercedes-for-Aaron context: 'ואתפלל גם בעד "
            "אהרן' = פאסתג'פרת לה איצ'א פי ד'אלך אלוקת ('I sought forgiveness for him also at that "
            "time'). The Deut 9:20 attestation is doubly significant: (1) it introduces the FIRST-PERSON "
            "perfect form פאסתג'פרת — extending the entry's variant inventory beyond the third-person "
            "and imperfect forms; (2) it shifts the agent from the PRIEST (Lev/Num attestations) to the "
            "PROPHET (Moses-as-intercessor), confirming that the Form-X 'supplication' reframe applies to "
            "the broader category of mediated-atonement, not just the priestly-ritual subset. The Heb's "
            "verb here is הִתְפַּלֵּל ('to pray, to intercede') — Saadia renders it with the same Form-X "
            "structure he uses for the priestly כפר, COLLAPSING the Heb's lexical distinction between "
            "priestly-atonement and prophetic-intercession into a single Arabic supplication-vocabulary. "
            "Pedagogically distinctive because the cross-book extension converts what looked like a "
            "priestly-ritual lexical choice into a programmatic-theological choice spanning the entire "
            "Pentateuchal atonement-intercession field. (Notable counter-case still: at Num 25:13 — "
            "Phinehas's covenant of peace, 'because he was zealous for his God and atoned for the "
            "children of Israel' — Saadia does NOT use Form X, retaining the bare Form I cognate כפר; "
            "the choice marks the Phinehas episode as a covenant-zeal frame rather than a routine "
            "atonement-supplication, preserving the Hebrew's emphasis on the act-of-zeal that earned "
            "the priestly covenant.) Ḥibbur Yāfet transmits the standard Form-X pairing as Saadia's "
            "canonical rendering."
        ),
        "blau_dict_sense_rewrite": (
            "غفر (Form X استغفر) 'to forgive, to seek forgiveness' — Blau cites Saadia on Lev 16:6 with "
            "the Ex 29:36 parallel, plus the broader Bamidbar atonement-cluster (Num 5:8, 8:12/19/21, "
            "15:25/28, 17:11, 28:22/30, 29:5/11), AND the Deut 9:20 prophetic-intercession attestation "
            "(Moses for Aaron, golden-calf aftermath: ואתפלל = אסתג'פרת), confirming the invariant Form-X "
            "'supplication' reframe of biblical כפר/התפלל across the priestly AND prophetic mediated-"
            "atonement systems. (Num 25:13 Phinehas-zeal is the marked exception: bare Form I cognate.) "
            "Ḥibbur Yāfet transmits the canonical pairing."
        ),
    },

    # ---- בחפז + Deut 16:3 (Pesach-haste) ----------------------------
    {
        "lemma_ja": "בחפז",
        "extend_verses": [
            {"book": "Devarim", "ch": 16, "v": 3},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Consonantal-calque pairing (Heb ḥ-p-z ~ Ar ḥ-f-z), now confirmed across the canonical "
            "Pesach-haste pair: the original Ex 12:11 prescription ('ואכלתם אתו בחפזון' = ותאכלוה "
            "בחפז) AND the Deut 16:3 commemorative reminder ('כי בחפזון יצאת מארץ מצרים' = לאנך "
            "כ'רגת מן מצר בחפז 'because you went out from Egypt in haste'). Saadia strips the "
            "Hebrew -on abstract suffix (חִפָּזוֹן → حفز), rendering the prepositional בְּחִפָּזוֹן "
            "with the bare verbal noun in the same prep. The cross-attestation across the two Pesach "
            "passages (the original injunction + the Deuteronomic reminder) confirms the calque is the "
            "stable terminus-technicus for Saadia's Pesach-haste discourse. Blau records the parallel "
            "JA idiom بحفزون = בחפזון. Note that the Heb-Ar root-pair is a TRUE consonantal cognate "
            "(both ḥ-p/f-z, with the predictable Heb-Ar p/f sound-correspondence), making the calque "
            "morphologically transparent at the consonantal level even as the abstract-suffix gets "
            "elided."
        ),
        "blau_dict_sense_rewrite": (
            "حفز 'haste (and panic)'; idiom بحفزون = בחפזון, idiom بحفزي = בחפזי. Blau cites Saadia on "
            "Ex 12:11, Deut 16:3, Isa 52:12 ('כי לא בחפזון תצאו'), and Ps 31:23 / 116:11. The "
            "Pesach-original (Ex) + Pesach-reminder (Deut) attestation pair confirms the calque as "
            "Saadia's canonical Pesach-haste vocabulary."
        ),
    },

    # ---- אצר + Deut 28:48 (curses yoke-of-iron) ----------------------
    {
        "lemma_ja": "אצר",
        "extend_verses": [
            {"book": "Devarim", "ch": 28, "v": 48},
        ],
        "extend_variants": ["אצרא"],
        "mechanism_rewrite": (
            "Frame-shift from physical-implement to binding-obligation, now confirmed across the two "
            "Pentateuchal yoke-vocabulary pillars: Hebrew עֹל ('yoke' as wooden-implement on oxen, here "
            "metaphorical) gets rendered with Arabic إصر, a Quranic-register noun (Q3:81 'إِصْرِي' = "
            "'my covenant-pledge') that names the binding-constraint frame rather than the implement "
            "frame. The cross-book pair: (1) Vayikra 26:13 ('ואשבר מטות עלכם' = וכסרת קראביס אצרכם — "
            "'and I broke the bars of your yoke', the exodus-liberation rhetoric closing the Blessings); "
            "(2) Devarim 28:48 ('ונתן על ברזל על צוארך' = ויצ'ע אצרא מן חדיד עלי' ענקך — 'and he shall "
            "place a yoke of iron upon your neck', the Curses chiastic INVERSION of the liberation — "
            "now the indefinite-accusative אצרא surfaces the new variant form). The cross-attestation "
            "across the Blessings-Curses pair is structurally significant: where Vayikra 26:13 "
            "celebrates the BREAKING of the slavery-yoke at exodus, Deut 28:48 threatens the RESTORATION "
            "of the slavery-yoke as the curse for covenant-breaking — Saadia's consistent use of إصر "
            "across both pillars preserves the Hebrew's chiastic-structural pairing through a single "
            "Arabic lexical anchor. The Isa 14:25 prophetic-parallel ('מעליהם עלו' = ענהם אצרה — 'their "
            "yoke from upon them') extends the frame into the prophetic-eschatological deliverance. The "
            "choice routes the slavery-and-liberation declaration through an oath-bond semantic field "
            "(the burden God released = the binding-pledge), reframing the Heb's mechanical-implement "
            "metaphor as a relational-covenant metaphor — fitting Saadia's broader theological tendency "
            "to read political-physical bondage as a function of covenant-obligation."
        ),
        "blau_dict_sense_rewrite": (
            "إصر 'yoke, burden' — Blau cites Saadia on Lev 26:13 ('ואשבר מטות עלכם' = וכסרת קראביס "
            "אצרכם), Deut 28:48 ('עול ברזל על צוארך' = אצרא מן חדיד עלי ענק), and Isa 14:25 ('מעליהם "
            "עלו' = ענהם אצרה). The Blessings-Curses chiastic pair (Lev 26:13 / Deut 28:48) anchors "
            "the cross-Pentateuchal yoke-vocabulary, with the Isa 14:25 prophetic parallel completing "
            "the deliverance-frame."
        ),
    },
]


# ============================================================================
# DEFERRED — skip / borderline / cluster-dupes
# ============================================================================

BATCH1_DEFERRED = {
    "skip": [
        {
            "blau_id": 13983,
            "root_ar": "أول",
            "verse_hint": "Deut 13:10 בראשונה = אוול",
            "reason": "Direct adverbial cognate; Heb ראשון/בראשונה ~ Ar أول. Standard temporal-ordinal pairing without semantic-field divergence at the cited Devarim verse.",
        },
        {
            "blau_id": 14868,
            "root_ar": "حصر",
            "verse_hint": "Blau cites Ex 30:12 (כי תשא); no Devarim-anchored attestation in the body excerpt.",
            "reason": "Blau body excerpt foregrounds Ex 30:12 (כי תשא) and Ibn Janāḥ's grammatical methodology, not a Devarim-anchored lexical choice. No Devarim verse to verify.",
        },
        {
            "blau_id": 15084,
            "root_ar": "خبر",
            "verse_hint": "Methodology citation (Sefer ha-Shetarot, Qirqisani)",
            "reason": "No Devarim attestation in the body excerpt; the citations are metalanguage (fact-of-the-matter / matter / tradition) drawn from Saadia's halakhic-juridical writings, not the Devarim tafsir.",
        },
        {
            "blau_id": 15118,
            "root_ar": "خدع",
            "verse_hint": "Blau cites Ex 22:15 (כי יפתה איש בתולה) + Proverbs; no Devarim verse anchor.",
            "reason": "The body cites Ex 22:15 (פיתוי בתולה) and Prov 1:10 (פיתוי בנים) as the canonical Saadyan attestations. No Devarim-cited verse in the body excerpt. Possible Deut 13:7 (יסיתך) attestation but not surfaced in this candidate's citation lines.",
        },
        {
            "blau_id": 15403,
            "root_ar": "دجن",
            "verse_hint": "Deut 4:13, 11:14, 12:17, 14:23, 18:4, 28:51, 33:28 (דגן, 7 verses)",
            "reason": "Blau's headword دجن is MISATTRIBUTED for the Saadia surface — Saadia consistently uses Ar بَرّ ('wheat, grain', cognate of Heb בָּר 'pure-grain') across all 7 Devarim דגן-attestations, not دجن. The Blau citation appears to follow a Tanḥum-cluster manuscript-variant reading, but the Cairo 2019 surface uniformly shows ברّ. Defer to a future re-mining as a separate בَّر / دجن opposition entry once the manuscript-tradition split is clarified.",
        },
        {
            "blau_id": 16765,
            "root_ar": "صحراء",
            "verse_hint": "Deut 14:22 השדה = אלצחרא",
            "reason": "Direct sense-pairing for the generic field/wilderness substantive; Heb שדה (here in the construct 'product-of-the-field' for tithe) → Ar الصحراء (the standard Arabic field-or-wilderness substantive). No semantic-field divergence; the body excerpt notes Saadia uses the same word for both שדה and חוצות.",
        },
        {
            "blau_id": 17158,
            "root_ar": "طول",
            "verse_hint": "Deut 32:39 מחצתי",
            "reason": "Blau body cites Deut 32:39 but the Arabic root طول 'to be long, to extend' isn't the surface choice for מחצתי ('I struck'); the citation is methodological (Saadia's frequent use of طول-derivatives) rather than a Deut-32:39-anchored substitution. Standard cognate.",
        },
        {
            "blau_id": 17212,
            "root_ar": "عتق",
            "verse_hint": "No Devarim-anchored attestation; references to halakhic 'three things' (Heb דברים) misparsed.",
            "reason": "Body excerpt's 'דברים' references are to Heb דברים = 'things/matters' (in the rabbinic 'three things by which a slave is freed' formula), NOT the Book of Deuteronomy. No actual Devarim verse cited.",
        },
        {
            "blau_id": 17256,
            "root_ar": "عدا",
            "verse_hint": "No Devarim citation in body",
            "reason": "Standard preposition meaning 'except, beyond'; the body's references are to Pirqei De-Rabbi Eliezer and Avot literature, not Devarim. No Devarim attestation to verify.",
        },
        {
            "blau_id": 18454,
            "root_ar": "قدح",
            "verse_hint": "Deut 32:22 כי אש קדחה באפי = אן 00 (קד) קדחת באפי / אלנאו תנקדח",
            "reason": "Direct cognate; Heb קדח ('to burn, kindle') ~ Ar قدح. Saadia retains the cognate verb. No semantic-field divergence at the cited Deut 32:22.",
        },
        {
            "blau_id": 18455,
            "root_ar": "قوس قدح",
            "verse_hint": "Bow + قدح cluster head; same Deut 32:22 citation",
            "reason": "Cluster head of 18454 (קדח); same direct-cognate verdict applies. The rainbow-noun قوس قدح surfaces in Bereshit 9 (which is already in scope), not Devarim.",
        },
        {
            "blau_id": 18456,
            "root_ar": "قدر",
            "verse_hint": "Same Deut 32:22 cluster (mis-clustered to 18454)",
            "reason": "Cluster artifact; the Blau citation block in the candidate row is the 18454 קדח block. قدر ('to estimate, appraise') is unrelated and doesn't surface at Deut 32:22.",
        },
        {
            "blau_id": 18694,
            "root_ar": "مقلب",
            "verse_hint": "Deut 29:22 כמהפכת סדם (likely)",
            "reason": "Heb מהפכה (Sodom-overthrow noun) → Ar مقلب; Saadia uses the cognate Form II-passive imitation of the Heb mishkal. Already covered by the existing Bereshit-19 Sodom-narrative anchor; the Deut 29:22 attestation is a back-reference to the same lexical choice, not a new paradigm.",
        },
        {
            "blau_id": 18778,
            "root_ar": "بمقامهم",
            "verse_hint": "Deut 5:15 ולזאלך אמרך אן תקים פי יום אלסבת",
            "reason": "Standard cognate position-vocabulary; Heb קום (in 'observe the Sabbath' rendering) ~ Ar قام Form I 'to observe (a religious duty)'. The Saadyan choice مَقَام / تَقُوم for קום-derivatives is a routine institutional-religious cognate without paradigm-shifting semantic-field divergence.",
        },
        {
            "blau_id": 18779,
            "root_ar": "مقام",
            "verse_hint": "Same Deut 5:15 cluster (18778)",
            "reason": "Cluster head of 18778; same direct-cognate verdict applies. مقام as 'station/rank' is the standard Arabic position-noun.",
        },
        {
            "blau_id": 18780,
            "root_ar": "قوم",
            "verse_hint": "Same Deut 5:15 cluster (18778)",
            "reason": "Cluster head of 18778-18779; same direct-cognate verdict applies. قوم Form I 'to confirm, observe' is the standard Arabic institutional-religious verb.",
        },
        {
            "blau_id": 18889,
            "root_ar": "تكرير",
            "verse_hint": "No Devarim verse anchor (Qirqisani metempsychosis cite)",
            "reason": "Blau body excerpt cites Qirqisani's discussion of transmigration-of-souls (تكرير) plus Psalms 31:11; the Devarim references in the cluster are to Heb דברים = 'things' (in the philosophical discourse), not the Book of Deuteronomy. No Devarim attestation.",
        },
        {
            "blau_id": 18890,
            "root_ar": "كرب",
            "verse_hint": "Same 18889 cluster",
            "reason": "Cluster head of 18889; same no-Devarim-attestation verdict. كرب 'to be worried, distressed' isn't a Devarim-surface choice.",
        },
        {
            "blau_id": 19325,
            "root_ar": "ما",
            "verse_hint": "Deut 8:16 (אשר לא יעדון אבותיך = מא לם יערפה אבאיך)",
            "reason": "Standard relative-clause particle ('that which / what'); ما is the obvious Arabic correspondent for אשר and the substitution is grammatically routine. No semantic-field divergence; trivial particle-mapping.",
        },
        {
            "blau_id": 19636,
            "root_ar": "نتج (cluster head, 14 rows 19636-19649)",
            "verse_hint": "Deut 3:5 ובריח = ונגור (the cluster citation footprint)",
            "reason": "14-row cluster (نتج / نتر / منتور / نتن / نتو / نتي / نثث / نثر / نجاب / نجر / نجور / نجار / نجز) all citing Deut 3:5 ובריח 'and bar/bolt'. Saadia uses نجور ('bolts') for ברִיחַ at Deut 3:5 — a non-cognate substantive substitution (cognate Heb-Ar path would be بَرٌ — but برّ already serves 'grain'). Tier-grade GLOSS borderline but cluster-deferred at cap; revisit in Batch 2 if needed.",
        },
        {
            "blau_id": 19861,
            "root_ar": "تنغيم / nfd family (11 rows)",
            "verse_hint": "Deut 7:10 ומשלם לשנאיו אל פניו להאבידו = לאנפאזה (Form IV inf.)",
            "reason": "11-row cluster (blau_ids 19861-19871) covering the nfd/nfx family ('to destroy, exterminate, blow-out'); already deferred from Vayikra B1 (Lev 26:30 was missing from the tafsir chapter file) AND from Bamidbar B1 (Num 33:52 doesn't surface the destruction-frame). At Deut 7:10 Saadia uses لانفاذه (Form IV infinitive: 'to bring it to completion/utter end' — extermination), which IS the canonical انفذ destruction-frame Blau cites. Worth re-mining the cluster head in Phase 3 R2 to consolidate the cross-book destruction-vocabulary at the انفذ entry-level.",
        },
        {
            "blau_id": 19950,
            "root_ar": "نهاية",
            "verse_hint": "Deut 18:8 (Phase 3 R2 metalanguage 'wisdom')",
            "reason": "نهاية ('wisdom, completeness') is mostly a metalinguistic-philosophical noun, not Saadia's Devarim 18:8 surface choice. The Devarim citation in the body block refers to 18:8 ממכריו, but the surface Saadia uses is אלנווב 'priestly duty-rotation' (= 19954 نوبة article-head — see borderline below).",
        },
        {
            "blau_id": 19951,
            "root_ar": "ناهيك",
            "verse_hint": "Cluster of 19950",
            "reason": "Cluster head of 19950; particle 'much more (he)' isn't Saadia's choice for Deut 18:8. Same skip-reason as 19950.",
        },
        {
            "blau_id": 19952,
            "root_ar": "نوء",
            "verse_hint": "Storm; not a Devarim 18:8 candidate",
            "reason": "نوء ('storm, tempest') is unrelated to the Deut 18:8 priestly-rotation context. The cluster artifact links it via shared body-text but the actual lemma is 19954 نوبة 'duty-rotation' (see borderline).",
        },
        {
            "blau_id": 19953,
            "root_ar": "ناب",
            "verse_hint": "Verb 'to replace, to be allotted'; partial match to Deut 18:8",
            "reason": "Cluster artifact; ناب 'to follow in place of, to be allotted as one's share' is loosely linked to the Deut 18:8 priestly-portion theme but the surface lexical choice is the related substantive نوبة (see 19954 borderline), not the verb.",
        },
        {
            "blau_id": 20003,
            "root_ar": "يده / نال",
            "verse_hint": "Deut 16:10 מסת נדבת ידך = מקדאר מא תנאל ידך",
            "reason": "Standard idiomatic-substitution; Heb 'measure of the freewill-offering of your hand' → Ar 'as your hand attains/reaches'. The Arabic verb نال 'to obtain, attain' is the cognate-near substitute (Heb נאל / נחל overlapping cognates). The substitution is routine for the 'gift-from-hand' idiom; not paradigm-shifting.",
        },
    ],
    "borderline": [
        {
            "blau_id": 18619,
            "root_ar": "قضى / Form VIII اقتضى",
            "verse_hint": "Deut 15:2 לא יגש (creditor) = פלא יקתצ'י (Form VIII 'demand-payment')",
            "open_question": "Saadia routes the Heb נגש ('to exact a debt', the creditor's pressure-verb) through Ar Form VIII اقتضى ('to demand-payment, to call-in a debt') — preserving the legal-creditor semantic field via a specifically-legal Arabic verb. Strong NOTE candidate (single-verse but pairs with the יסיב shemittah-release entry as the creditor's complementary action). Cut at the 5-NOTE cap for Devarim B1; promote in Batch 2 alongside the broader Deut 15 release-law cluster.",
        },
        {
            "blau_id": 19379,
            "root_ar": "ممد اليد",
            "verse_hint": "Deut 23:21 משלח ידך = ממד ידך (calque idiom 'outstretching of the hand')",
            "open_question": "Strong calque-idiom candidate: Heb construct משלח-יד ('outstretching-of-hand', the standard biblical idiom for 'undertaking, livelihood') gets rendered with the Ar calque ممد اليد ('extending-of-the-hand'). The 23:21 attestation is the only clean noun-calque surface — Deut 15:10 uses the verbal-phrase form (תמד אליה ידך) rather than the noun-calque. GLOSS-borderline cut at the 4-GLOSS cap; promote in Batch 2.",
        },
        {
            "blau_id": 19954,
            "root_ar": "نوبة",
            "verse_hint": "Deut 18:8 ממכריו על האבות = מן אלנווב (priestly duty-rotation exegesis)",
            "open_question": "Striking exegetical reframe: Heb ממכריו (Deut 18:8's notoriously obscure 'his sale-proceeds' or 'his patrimony' — an etymologically-disputed noun) → Ar אלנווב 'the priestly duty-rotations (مَشَامِر الكهانة)'. Saadia adopts the rabbinic-Sifrei interpretation that the verse refers to the priestly-משמרות rotation-shift system, then translates accordingly with the Arabic equivalent. NOTE-borderline because it's an EXEGETICAL choice (adopting a rabbinic gloss) more than a LEXICAL twist; cut at the 5-NOTE cap; promote if/when Phase 3 R2 surfaces a coherent exegetical-tradition-anchor cluster.",
        },
        {
            "blau_id": 19775,
            "root_ar": "Form VI تناصى / נצול",
            "verse_hint": "Deut 25:11 וינצו אנשים = ואן תנאציאן רגלאן (Form VI of نصو 'to quarrel mutually')",
            "open_question": "Form VI mutual-reciprocity calque for the dual-conflict verb: Heb נצה (Niphal 'to quarrel') → Ar Form VI تناصى — the choice is morphologically interesting because Form VI explicitly marks the MUTUAL/RECIPROCAL dimension that the Heb Niphal leaves implicit. GLOSS-borderline candidate cut at cap; the morphological-mirroring criterion fits the מחפצה precedent from Bamidbar B1 well, so worth promoting in Batch 2.",
        },
    ],
    "_cluster_dupes_logged": [
        "14907 + 14928 (حفز/حفز cluster, 2 rows — both promote-in-place to בחפז, see PROMOTE_IN_PLACE)",
        "17953-17955 (غريبة/مغرب/غويب cluster, 3 rows — 17953-cluster-head SHIPPED as gloss גראביב)",
        "18454-18456 (قدح/قوس قدح/قدر cluster, 3 rows — direct-cognate SKIP)",
        "18519-18520 (قرض/قرضة cluster, 2 rows — 18519 SHIPPED as note אקרץ', 18520 is verbal-noun variant)",
        "18615-18619 (قصو/قضض/قضاض/قضب/قضيب cluster, 5 rows — 18615 SHIPPED as gloss אתקצא, 18619 → borderline as יקתצ'י, others SKIP)",
        "18778-18780 (بمقامهم/مقام/قوم cluster, 3 rows — all SKIP cognate-direct)",
        "18889-18890 (تكرير/كرب cluster, 2 rows — both SKIP no-Devarim-anchor)",
        "19342-19343 (متيع/ممتع cluster, 2 rows — 19343 SHIPPED as note ממתעה, 19342 is masc.-form variant)",
        "19378-19381 (مادي/ممد/ممدود/مدجة cluster, 4 rows — 19379 → borderline as ממד יד, 19378+19380+19381 are variant headwords)",
        "19636-19649 (نتج/نتر/منتور/.../نجز 14-row cluster — all cluster-deferred at Deut 3:5 ונגור; revisit for cross-book GLOSS in Phase 3 R2)",
        "19861-19871 (nfd family 11 rows — already deferred from Vayikra B1 + Bamidbar B1; Deut 7:10 לאנפאזה IS the canonical destruction-frame; consolidate at cluster-head in Phase 3 R2)",
        "19950-19954 (نهاية/ناهيك/نوء/ناب/نوبة cluster, 5 rows — 19954 → borderline as נווב, others SKIP)",
        "20003-20005 (يده/نيلي/نيل cluster, 3 rows — 20003 SKIP, 20004+20005 are not Saadia-surface for Deut 21:17 either; the Ja uses bare aval and nayl as routine idiom-noun)",
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
    """Write Devarim Batch 1 entries into data/_blau_saadia_deferred.json
    under a fresh "devarim" namespace (idempotent on blau_id).
    """
    payload = json.loads(deferred_path.read_text())
    dv = payload.setdefault("devarim", {})

    added = {"skip": 0, "borderline": 0}
    for bucket, new_items in BATCH1_DEFERRED.items():
        if bucket.startswith("_"):
            continue
        existing = dv.setdefault(bucket, [])
        existing_ids = {it.get("blau_id") for it in existing if isinstance(it, dict)}
        for item in new_items:
            if item.get("blau_id") in existing_ids:
                continue
            existing.append(item)
            existing_ids.add(item.get("blau_id"))
            added[bucket] = added.get(bucket, 0) + 1

    cluster_log = dv.setdefault("_cluster_dupes_logged", [])
    if isinstance(cluster_log, list):
        for line in BATCH1_DEFERRED["_cluster_dupes_logged"]:
            if line not in cluster_log:
                cluster_log.append(line)

    dv.setdefault("_session", "Phase 4 Devarim Batch 1 (apply_phase4_devarim_batch1.py)")

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return {"added": added, "devarim_buckets_now": {k: len(v) if isinstance(v, list) else v for k, v in dv.items()}}


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

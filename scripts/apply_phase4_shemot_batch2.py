"""
Phase 4 — Shemot Batch 2.

Twelve hand-curated entries from blau_ids 15700-20473 of
data/_blau_saadia_candidates.json (the 104-candidate Shemot-flagged window
after the Batch 1 cutoff). Each one has been verified against
data/tafsir-shemot-{ch}.json — the JA surface form physically appears in
the cited verse, and the Hebrew anchor word appears in the verse's hebrew
column (nikud + final-form normalization applied for matching).

Tier breakdown:
  - 7 GLOSS — non-cognate Heb→Ar pairings, register shifts, technical extensions
  - 5 NOTE  — semantic surprises with short stated mechanism

Coverage by chapter:
  - Mishkan-cluster bonus (Ex 24-39): 7 entries cover textiles + vessels +
    metalwork — تכלת-cousin paradigm. Multi-verse bundling common.
  - Slavery + Passover (Ex 1-2, 5-6, 12, 16, 23, 31): the social-legal +
    theological surface that produced Batch 1's strongest entries.

Deferred (merged into data/_blau_saadia_deferred.json#/shemot — see
_update_deferred() below; idempotent on blau_id):
  - 4 SKIP:
    * 15740 دلا — metalanguage-only marker ('note: citation' in source).
      No verse-anchored surface; defer to translation-theory pool.
    * 17144 طوف ('to flow over') on Ex 14/15 — Blau cites Saadia for the
      Sea-crossing wave-cover but Cairo 2019 tafsir uses غ-ط-و (אטא/ג'טא)
      throughout (Ex 14:28 ויכס, 15:5, 15:10). Either recension difference
      or a misattributed cite (Blau quotes "אלמא אטאף עלי פניהם" which is
      not in the Cairo baseline). Defer.
    * 18436 قتر ('to make smoke / burn incense') on Ex 29:13 — surface
      present (וקתר ז'אלך עלי' אלמדבח) but pure consonantal cognate with
      Hebrew קטר; no tier-promoting divergence to display. Skip.
    * 20277 وشمة ('woad/indigo dye') — source SQLite cluster head; the
      Shemot citation (Ex 21:6 ורצע) lives in the sibling root موسم
      ('mark, brand') — a quadriliteral وشم/سم cluster split across 4 rows
      (20277-20280). The موسم/ميسم branch is interesting but reads as a
      cognate of Heb רצע (awl-mark); defer the whole cluster pending a
      Mishpatim-pericope re-walk.
  - 2 BORDERLINE:
    * 17513 ضعيف ('weak / poor') on Ex 22:24 — surface (לצ'עיף) and
      anchor (עני) both present, but the Heb עני → Ar ضعيف pairing is a
      close register-shift cousin (Heb root ع-ن-ي ~ Ar root ض-ع-ف both
      cluster around 'weakness'). On the cognate-vs-divergence borderline;
      defer for a tier-judgment re-pass.
    * 19132 لبن ('to mould bricks') on Ex 1:14 / 5:7-14 — Blau explicitly
      tags this as Hebrew-influenced ('השימוש תלוי בעברית המקרא … אינו
      חלק מאוצר המילים הערבי' per Ibn Janāḥ). NOTE-tier mechanism in
      principle (denominal verb from a Heb-borrowed noun) but Saadia's
      Mishnaic-Hebrew-style surface use of لبن throughout Ex 5 is hard to
      gloss without inverting the bilingual frame. Defer.
  - 1 CROSS_BOOK_DUPE: (none this round — the cluster duplicates seen are
    all intra-Shemot, not cross-book.)

Cluster duplicates seen in the window (logged but not auto-deduped — same
pattern as Batch 1's 14907≈14928):
  - 17350 ≈ 17351 (both جيب / Ex 28:7 ff. — same article, two rows)
  - 17513 ≈ 17514 ≈ 17515 ≈ 17516 (ضعف cluster — 4 spelling rows)
  - 17597 ≈ 17598 (both عرم / Ex 15:8)
  - 17999 ≈ 18000 (غفر/غفارة — 'forgive' co-article)
  - 18778 ≈ 18779 ≈ 18780 (قوم cluster — 3 rows)
  - 19132 ≈ 19133 ≈ 19134 (لبن cluster — 3 rows)
  - 19545 ≈ 19546 ≈ 19547 ≈ 19548 (من 'time-interval' cluster — 4 rows)
  - 20065 ≈ 20066 ≈ 20067 ≈ 20068 (هل / Dirinburg-variant cluster — 4 rows)
  - 20114 ≈ 20115 ≈ 20116 ≈ 20117 ≈ 20118 (هاون/هوي cluster — 5 rows)
  - 20277 ≈ 20278 ≈ 20279 ≈ 20280 (وشمة/موسم cluster — 4 rows, deferred)
  - 20402 ≈ 20403 ≈ 20404 ≈ 20405 ≈ 20406 ≈ 20407 ≈ 20408 (ولع/ولف/توليف
    cluster — 7 rows; Ex 36:13 'ויחבר את היריעת' = 'to couple'; verified
    no clean single tier-grade reading, defer for a Mishkan-coupling
    pericope re-walk)

Apply pattern mirrors scripts/apply_phase4_shemot_batch1.py:347-385;
dedupe is on lemma_ja only (DivergenceEntry has no `id` field). The
_update_deferred() helper is rewritten vs Batch 1 to MERGE into the
existing shemot.{skip,borderline,phase3_r2_candidates,cross_book_dupes}
buckets, idempotent on blau_id.
"""

import json
import pathlib
import sys
from collections import Counter


NEW_ENTRIES = [
    # ---- GLOSS — Ex 24:5 / 32:6: Peace offerings -----------------------------
    {
        "lemma_ja": "סלאמה",
        "variants": ["סלאמה'", "ד'באיח סלאמה"],
        "lemma_ar": "سلامة",
        "root": "س-ل-م",
        "tier": "gloss",
        "classical_en": "Classical Arabic سلامة = 'safety, soundness, well-being' (verbal noun of سلم); Saadia repurposes it as the technical name for the biblical peace-offering.",
        "classical_he": "בערבית הקלאסית سلامة = 'שלום, שלמות, בריאות' (שם פעולה של سلم); רס\"ג מאמץ את המילה כשם טכני לקרבן השלמים המקראי.",
        "saadia_en": "peace-offering (שלמים)",
        "saadia_he": "זבחי שלמים",
        "mechanism": "Cognate semantic-field pairing: Heb שלם ~ Ar سلم share the 'wholeness/peace' root, so Saadia picks سلامة (the abstract noun) over the standard Arabic ذبيحة-السلام or قربان-السلام. The idiom ذبائح سلامة (= זבחי שלמים) becomes the JA technical term throughout the sacrificial corpus.",
        "verses": [
            {"book": "Shemot", "ch": 24, "v": 5},
            {"book": "Shemot", "ch": 32, "v": 6},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "سلم",
            "sense": "سلامة 'peace-offering' (idiom قوابين السلامة) — Blau cites Saadia on Ex 24:5; 32:6 (with the Lev 3:1 cross-reference) and the Geniza-attested قربان السلامة in Ḥafetz 139:12.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 29:20: Earlobe of Aaron / the priests --------------------
    {
        "lemma_ja": "שחמה'",
        "variants": ["שחמה", "שחמאת", "שחמה' אד'ן"],
        "lemma_ar": "شحمة",
        "root": "ش-ح-م",
        "tier": "gloss",
        "classical_en": "Classical Arabic شَحْمَة normally = 'a piece of fat'; the idiom شحمة الأذن ('fat of the ear') is the fixed Arabic expression for 'earlobe'.",
        "classical_he": "בערבית הקלאסית شَحْمَة היא בדרך כלל 'חלב, חתיכת שומן'; הצירוף شحمة الأذن ('חֵלֶב האוזן') הוא הביטוי הקבוע ל'תנוך האוזן'.",
        "saadia_en": "the earlobe (תנוך אזן)",
        "saadia_he": "תְּנוּךְ אֹזֶן",
        "mechanism": "Idiom-anchored pairing: Saadia renders Hebrew תְּנוּךְ ('lobe, tip') with the standard Arabic anatomical idiom شحمة الأذن — a semantic-field jump (Heb 'projection/tip' → Ar 'fatty pad') licensed by the fixed Arabic compound. Both elements (head + الأذن) get translated into JA in the consecration-of-priests pericope.",
        "verses": [{"book": "Shemot", "ch": 29, "v": 20}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "شحم",
            "sense": "شحمة 'earlobe' (idiom شحمة الأذن) — Blau cites Saadia on Ex 29:20 ('על תנוך אזן אהרן … ועל תנוך אזן בניו הימנית' = עלי שחמה' אד'ן הרון … ועלי' שחמאת אד'אן בניה), with plurals أشحام / شحمات for the multi-priest construction.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 28:8 / 28:27 / 28:28: Belt/girdle of the ephod -----------
    {
        "lemma_ja": "שפשג",
        "variants": ["שפשגהא", "אלשפשג"],
        "lemma_ar": "شفشج",
        "root": "ش-ف-ش-ج",  # quadriliteral, treated as such
        "tier": "gloss",
        "classical_en": "Classical Arabic شفشج (quadriliteral) = 'belt, girdle, sash' — a rare technical term outside Saadia's Tafsir; Ibn Janāḥ picks up the equivalence after him.",
        "classical_he": "בערבית הקלאסית شفشج (ארבע-עיצורי) = 'אבנט, חגורה' — מונח טכני נדיר מחוץ לתרגום רס\"ג; אבן ג'נאח אימץ את הזיהוי בעקבותיו.",
        "saadia_en": "the belt (חשב) of the ephod",
        "saadia_he": "חֵשֶׁב הָאֵפֹד",
        "mechanism": "Non-cognate technical pairing: the Hebrew construction-term חֵשֶׁב ('decorated band of the ephod') gets rendered with a rare Arabic quadriliteral שפשג rather than the more obvious حزام or منطقة — a choice Blau attributes to a Saadia-internal lexicon of Mishkan-vocabulary, transmitted forward through Ibn Janāḥ's Shorashim 253.",
        "verses": [
            {"book": "Shemot", "ch": 28, "v": 8},
            {"book": "Shemot", "ch": 28, "v": 27},
            {"book": "Shemot", "ch": 28, "v": 28},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "شفشج",
            "sense": "شفشج 'belt, girdle' (specifically the ephod's חֵשֶׁב) — Blau cites Saadia on Ex 28:8 (וְחֵשֶׁב אֲפֻדָּתוֹ = שפשג אלצדרה') with the broader pericope at 28:27-28, followed by Ibn Janāḥ Shorashim 253.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 27:3 / 38:3: Bronze ash-pans of the altar ----------------
    {
        "lemma_ja": "צנאן",
        "variants": ["אלצנאן", "צנאנה", "צנאנהא"],
        "lemma_ar": "صنان",
        "root": "ص-ن-ن",
        "tier": "gloss",
        "classical_en": "Classical Arabic صنان (singular; plural ostensibly أصنان in Saadia's spelling, hypercorrect for أصنان) = 'large vessel, basin'; in the Mishkan corpus narrowed to the bronze ash-pans of the burnt-offering altar.",
        "classical_he": "בערבית הקלאסית صنان (יחיד) = 'כלי גדול, אגן'; בהקשר המשכן מצומצם לכלי הנחושת המשמשים לפינוי אפר מהמזבח החיצוני.",
        "saadia_en": "the ash-pans (סירת לדשנו)",
        "saadia_he": "סִירוֹת לְדַשְּׁנוֹ (כלי נחושת לפינוי אפר)",
        "mechanism": "Technical narrowing: Hebrew סִיר ('pot, cauldron') gets two distinct Saadia renderings depending on context — قِدر for cooking-pots (e.g. Ex 16:3 'סִיר הַבָּשָׂר'), but صنان specifically for the Mishkan's ash-pans (Ex 27:3, 38:3). Ibn Janāḥ Shorashim 480:5 transmits the equivalence and rules against 'correcting' the plural.",
        "verses": [
            {"book": "Shemot", "ch": 27, "v": 3},
            {"book": "Shemot", "ch": 38, "v": 3},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "صنن",
            "sense": "أضنان / أصنان 'bronze vessels, basins for ashes' (singular صنان) — Blau cites Saadia on Ex 27:3 ('ועשית סירותיו לדשנו' = ואצנע צנאנה לרמאדה) and Ex 38:3 ('את הסירות' = אלצנאן), followed by Ibn Janāḥ Shorashim 480:5.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 12:7 / 12:22 / 12:23: Lintel of the Passover doorpost ----
    {
        "lemma_ja": "מטל",
        "variants": ["אלמטל", "ואלמטל"],
        "lemma_ar": "مطل",
        "root": "م-ط-ل",
        "tier": "gloss",
        "classical_en": "Classical Arabic مطل = 'an elevated place from which one looks down, an overhang' (related to إطلال 'to look down upon'); narrowed in Saadia's JA to the doorway lintel.",
        "classical_he": "בערבית הקלאסית مطل = 'מקום גבוה שמשקיפים ממנו, גגון' (קשור إطلال 'להשקיף ממעל'); בשימוש רס\"ג צומצם למשקוף הדלת.",
        "saadia_en": "the lintel (משקוף)",
        "saadia_he": "מַשְׁקוֹף",
        "mechanism": "Architectural specialization: Hebrew מַשְׁקוֹף ('the place from which one looks down on those entering') and Arabic مطل share the root-meaning 'overlook from above' — Saadia exploits the parallel architecture-of-vision to fix مطل as the JA equivalent throughout the Passover doorpost cluster (the blood goes ועל המשקוף ועל שתי המזוזות = עלי' אלמטל וכ'די אלבאב).",
        "verses": [
            {"book": "Shemot", "ch": 12, "v": 7},
            {"book": "Shemot", "ch": 12, "v": 22},
            {"book": "Shemot", "ch": 12, "v": 23},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "مطل",
            "sense": "مطل 'lintel' — Blau records Saadia consistently using it for biblical מַשְׁקוֹף in the Passover-blood pericope (Ex 12:7, 22, 23) and notes the etymological transparency ('related to a place from which one overlooks').",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 28:7 / 28:25 / 28:27: Shoulder-pieces of the ephod -------
    {
        "lemma_ja": "ג'יב",
        "variants": ["גיב", "גיבאן", "גיבי"],
        "lemma_ar": "جيب",
        "root": "ج-ي-ب",
        "tier": "gloss",
        "classical_en": "Classical Arabic جيب = 'opening of a garment at the neck/breast, pocket'; Saadia narrows the term to the ephod's two shoulder-pieces (and is criticized for it by later lexicographers, but the usage propagates).",
        "classical_he": "בערבית הקלאסית جيب = 'פתח הבגד בצוואר ובחזה, כיס'; רס\"ג מצמצם את המונח לשתי כתפות האפוד (וזכה לביקורת מאוחרת על כך, אך השימוש התמסד).",
        "saadia_en": "the shoulder-piece (כתף) of the ephod",
        "saadia_he": "כְּתֵפוֹת הָאֵפוֹד",
        "mechanism": "Specialized narrowing: Saadia picks جيب (typically the 'neck-opening' of a tunic) for the structural-textile element Hebrew calls כָּתֵף ('shoulder/side-piece') of the ephod. Blau notes the Aggron records 'כתף = ניב' (5:258), with Ibn Janāḥ Shorashim subsequently glossing the equivalence — the choice routes the Mishkan-ephod's two structural straps through an Arabic word for 'garment-opening,' an unobvious technical pairing.",
        "verses": [
            {"book": "Shemot", "ch": 28, "v": 7},
            {"book": "Shemot", "ch": 28, "v": 25},
            {"book": "Shemot", "ch": 28, "v": 27},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "جيب",
            "sense": "جيب 'shoulder-piece (of the ephod)' — Blau cites Saadia's Aggron 5:258 (כתף = גיב, with later lexicographers' criticism) and the Mishkan attestations at Ex 28:7 (ולהא גיבאן מכ'ייטאן), 28:25, 28:27 (גיבי אלצדרה).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 12:6: Twilight (between sunset and dark) -----------------
    {
        "lemma_ja": "אלג'רובין",
        "variants": ["ג'רובין", "בין אלג'רובין", "בין הגרובין"],
        "lemma_ar": "الغروبين",
        "root": "غ-ر-ب",
        "tier": "gloss",
        "classical_en": "Classical Arabic غروب = 'sunset'; the dual idiom بين الغروبين ('between the two sunsets') = the twilight window between sun-set and full dark.",
        "classical_he": "בערבית הקלאסית غروب = 'שקיעה'; הצירוף הזוגי بين الغروبين ('בין שתי השקיעות') = הדמדומים שבין שקיעת השמש לשקיעת אור הדמדומים.",
        "saadia_en": "between the two sunsets (between sun-set and dusk)",
        "saadia_he": "בֵּין שְׁתֵּי הַשְּׁקִיעוֹת (בין שקיעת השמש לשקיעת אור הדמדומים)",
        "mechanism": "Dual-idiom calque: Saadia renders the Hebrew dual idiom בֵּין הָעַרְבַּיִם ('between the two evenings') with the parallel Arabic dual بين الغروبين, then explicitly glosses the timing in Qirqisāni 4:878-3 ('the dawn-end window: from sun-sinking until light-sinking'). Preserves the dual-marking pattern Hebrew uses to define the Passover slaughter window.",
        "verses": [{"book": "Shemot", "ch": 12, "v": 6}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "غرب",
            "sense": "غروب; idiom بين الغروبين = בין הערבים — Blau records both idioms (بين الغروبين and the synonymous بين العشاءين) and cites Saadia on Ex 12:6 with Qirqisāni's window-definition.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 23:21: Forgive your transgression -------------------------
    {
        "lemma_ja": "יצפח",
        "variants": ["צפח", "אצפח", "לא יצפח"],
        "lemma_ar": "صفح",
        "root": "ص-ف-ح",
        "tier": "note",
        "classical_en": "Classical Arabic صفح + عن = 'to turn the page on, to overlook, to pardon'; the abstract sense ('to forgive') is well-established but never the default rendering for biblical נשא (which would normally take غفر or حمل).",
        "classical_he": "בערבית הקלאסית صفح + عن = 'להעלים עין, לסלוח'; המשמעות המופשטת ('לסלוח') מבוססת אך אינה הברירה הרגילה לתרגום נשא המקראי (שלרוב מתורגם غفر או حمل).",
        "saadia_en": "he will not pardon (your transgression)",
        "saadia_he": "לא יסלח (לפשעכם)",
        "mechanism": "Theological reframe: Hebrew נשא פשע ('lift/bear transgression') is a body-part-derived idiom — God 'carries away' the sin. Saadia renders it not with the cognate Arabic حمل ('carry') but with صفح ('turn the page on'), shifting the idiomatic ground from carrying-away to overlooking-past. Blau notes the move propagated to Psalms 32:1 (parallel) and that Dirinburg's alternative reading يغفر له ذنبه explicitly tries to restore the standard pairing — testifying to صفح being Saadia's marked choice.",
        "verses": [{"book": "Shemot", "ch": 23, "v": 21}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "صفح",
            "sense": "صفح (Form I) + عن: 'to forgive' — Blau cites Saadia on Ex 23:21 ('כי לא ישא לפשעכם' = פאנה לא יצפח (ל)גרמכם) with Deut 29:19 (Tāj variant יצפח לה) and the Ps 32:1 parallel.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 31:16: Uphold/establish the Sabbath -----------------------
    {
        "lemma_ja": "יקימו",
        "variants": ["יקים", "יקימו בהא", "אקאמה"],
        "lemma_ar": "يقيم",
        "root": "ق-و-م",
        "tier": "note",
        "classical_en": "Classical Arabic Form IV أقام (root ق-و-م) = 'to establish, set up, maintain'; the legal-religious sense 'to uphold a covenant/commandment' is well-attested in juristic Arabic.",
        "classical_he": "בערבית הקלאסית בניין IV أقام (משורש ق-و-م) = 'הקים, ייסד, קיים'; המשמעות המשפטית-דתית 'לקיים ברית או מצווה' מבוססת בערבית המשפטית.",
        "saadia_en": "they shall uphold/establish (the Sabbath) — not merely 'guard' it",
        "saadia_he": "יקיימוּ (את השבת) — לא רק 'ישמרוּ'",
        "mechanism": "Active-legal calque: Hebrew שָׁמַר ('guard, observe') gets rendered with Arabic Form IV أقام ('uphold, establish') in the Sabbath-covenant verse, a shift toward an active-juristic frame — Saadia even doubles the verb (ויחפצו … ויקימו = 'they shall delight … and uphold'). Blau's Sefer ha-Shṭarot citation (225:14-15) and Pirqe Avot parallels (במקאם אלנאס = 'in honoring people') confirm the قام-family as Saadia's term of choice for the upholding-of-commandments register.",
        "verses": [{"book": "Shemot", "ch": 31, "v": 16}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "قوم",
            "sense": "قوم (Form II/IV) 'to confirm, uphold, establish' — Blau cites Saadia on Ex 31:16 ('ושמרו בני ישראל את השבת' = ויחפצו בני אסראיל אלסבת ויקימו בהא) and the Sefer ha-Shṭarot 225 legal-document parallel.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 16:16: An omer per head (Persian-loan measure) -----------
    {
        "lemma_ja": "מרזבאן",
        "variants": ["מחבאן", "מרזבאן לכל גמגמה"],
        "lemma_ar": "مرزبان",
        "root": "م-ر-ز-ب-ا-ن",  # Persian loan, no triliteral root
        "tier": "note",
        "classical_en": "Classical Arabic مرزبان (Persian loanword, from marzbān 'frontier-warden, governor of a province') is a political-administrative title; Saadia repurposes the homophonic/orthographically-similar form as a dry-measure equivalent for the biblical omer.",
        "classical_he": "בערבית הקלאסית مرزبان (שאילה פרסית, מ-marzbān 'מושל ספר, מושל מחוז') הוא תואר מנהלי-פוליטי; רס\"ג מאמץ את הצורה (הומופונית או דומה אורתוגרפית) כיחידת מידה יבשה כשווה ערך לעומר המקראי.",
        "saadia_en": "an omer (dry measure) per person",
        "saadia_he": "עוֹמֶר (מידת יבש) לְגֻלְגֹּלֶת",
        "mechanism": "Persian-loan measure-equivalence: Saadia renders the Hebrew dry-measure עֹמֶר with مرزبان — a Persian loanword whose primary Arabic sense is administrative ('frontier-warden'). Ibn Janāḥ Shorashim 17 picks it up as the standard JA gloss for עומר. The pairing is opaque without Blau's note: the underlying Persian term may have carried a secondary measure-sense in Iraqi Arabic that didn't survive in classical-Arabic lexicography but lived on in JA technical translation.",
        "verses": [{"book": "Shemot", "ch": 16, "v": 16}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "مرزبان",
            "sense": "مرزبان 'an [omer-sized] measure' — Blau cites Saadia on Ex 16:16 ('עמר לגלגלת' = מרזבאן לכל גמגמה) with Ibn Janāḥ Shorashim 17 transmitting the equivalence as a fixed Saadian gloss for biblical עומר.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 1:11 / 2:11 / 5:4-5 / 6:6-7: Burden as transport ----------
    {
        "lemma_ja": "נקל",
        "variants": ["נקלהם", "לנקלכם", "אלנקל", "נקל אלמצריון"],
        "lemma_ar": "نقل",
        "root": "ن-ق-ل",
        "tier": "note",
        "classical_en": "Classical Arabic نقل = 'transport, transfer, carrying-from-one-place-to-another'; never the default rendering for biblical 'forced labor' or 'burden' (which would expect عمل, تكليف, or حمل).",
        "classical_he": "בערבית הקלאסית نقل = 'הובלה, העברה, נשיאה ממקום למקום'; אינה הברירה הרגילה ל'עבודת פרך' או 'מעמסה' במקרא (שמצופה עבורן عمل, تكليف, או حمل).",
        "saadia_en": "the transport-labor (of the Egyptians), the load-carrying burden",
        "saadia_he": "מַעֲמַסַת הַהַעֲבָרָה (של המצרים), עבודת ההובלה",
        "mechanism": "Semantic-field calque across the Egypt-slavery pericope: Hebrew סֵבֶל ('burden, forced labor') gets a unified Saadian rendering as نقل — narrowing the abstract 'burden' to the concrete 'transport/relocation' of building materials. The choice routes the entire slavery vocabulary through a logistics-frame rather than a labor-pain frame (Heb עָנָה→Ar تعذيب, but Heb סֵבֶל→Ar نقل). Blau notes that Rashbam 11 follows Saadia's reading. The pairing surfaces across six verses (Ex 1:11 בְּסִבְלֹתָם = בנקלהם; 2:11 בְּסִבְלֹתָם = בנקלהם; 5:4 לְסִבְלֹתֵיכֶם = לנקלכם; 5:5 מִסִּבְלֹתָם = מנקלהם; 6:6 סִבְלֹת = נקל; 6:7 סִבְלֹת = נקל), making it Saadia's invariant equivalent for סבל in the Exodus narrative.",
        "verses": [
            {"book": "Shemot", "ch": 1, "v": 11},
            {"book": "Shemot", "ch": 2, "v": 11},
            {"book": "Shemot", "ch": 5, "v": 4},
            {"book": "Shemot", "ch": 5, "v": 5},
            {"book": "Shemot", "ch": 6, "v": 6},
            {"book": "Shemot", "ch": 6, "v": 7},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "نقل",
            "sense": "نقل 'transportation of a load, carrying' (used to render Mishnaic-style סבל) — Blau cites Saadia on Gen 49:15, Ex 1:11, 2:11, 5:4-5, 6:6-7 (full Exodus-slavery cluster), with Rashbam 11 following the equivalence.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 25:30 / 35:13: Showbread ----------------------------------
    {
        "lemma_ja": "מוגה",
        "variants": ["מוג'ה", "אלמוגה", "אלמוג'ה", "כבזא מוגהא"],
        "lemma_ar": "موجه",
        "root": "و-ج-ه",
        "tier": "note",
        "classical_en": "Classical Arabic موجه (passive participle of وَجَّهَ) = 'directed, turned-toward, faced'; the idiom خبز موجه ('bread that is faced') is a Saadia-internal technical term, transmitted forward by al-Fāsī as 'bread of two faces'.",
        "classical_he": "בערבית הקלאסית موجه (בינוני סביל של وَجَّهَ) = 'מכוון, פונה כלפי, מופנה'; הצירוף خبز موجه ('לחם המופנה') הוא מונח טכני פנים-רס\"גי, אשר אל-פאסי משדר כ'לחם שני הפנים'.",
        "saadia_en": "the showbread (לחם הפנים), 'faced bread'",
        "saadia_he": "לֶחֶם הַפָּנִים (\"לחם המופנה\" / \"לחם שני הפנים\")",
        "mechanism": "Calque-by-passive-participle: Hebrew לֶחֶם הַפָּנִים ('bread of the face/presence') gets rendered with خبز موجه ('faced bread') — a technical translation that preserves the construct-state's facial semantics while turning the Hebrew noun-construct into an Arabic participle-modifier. al-Fāsī Jāmiʿ 467 explicitly glosses the equivalence as 'bread that has two faces.' Note: Saadia bundles the construction with שֻׁלְחָן הַפָּנִים at Num 4:7 = אלמאידה אלמוגהה ('the faced table'), preserving the parallel.",
        "verses": [
            {"book": "Shemot", "ch": 25, "v": 30},
            {"book": "Shemot", "ch": 35, "v": 13},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "وجه",
            "sense": "موجه; idiom خبز موجه = לחם הפנים — Blau cites Saadia on Ex 35:13 (and the bundled Num 4:7 שולחן הפנים = אלמאידה אלמוגהה), with al-Fāsī Jāmiʿ 467-468 transmitting the 'two-faced bread' explanation.",
            "relation": "direct",
        },
    },
]


# Skip / borderline triage for the Batch-2 window. Merges into the existing
# shemot.* namespace; idempotent on blau_id.
BATCH2_DEFERRED = {
    "skip": [
        {
            "blau_id": 15740,
            "root_ar": "دلا",
            "verse_hint": "(metalanguage-only)",
            "reason": "Source SQLite carries only 'note: citation: רס״ג לשמות' — no verse-anchored surface; defer to the Saadia-translation-theory metalanguage pool, not Phase 4.",
        },
        {
            "blau_id": 17144,
            "root_ar": "طوف",
            "verse_hint": "Ex 14:27-30 / 15:5 / 15:10",
            "reason": "Blau quotes 'אלמא אטאף עלי פניהם' for ויכס המים (Sea-crossing wave-cover), but Cairo 2019 baseline uses غ-ط-و (ג'טא/אטא) throughout — Ex 14:28 ויכס=וג'טא, 15:5 ג'מר ג'טאהם, 15:10 פג'טאהם אלבחר. Either recension difference or misattributed cite; defer.",
        },
        {
            "blau_id": 18436,
            "root_ar": "قتر",
            "verse_hint": "Ex 29:13, 29:25",
            "reason": "Surface present (וקתר ז'אלך עלי' אלמדבח for והקטרת המזבחה) but pure consonantal cognate with Hebrew קטר — Heb ק-ט-ר and Ar ق-ت-ر are direct etymological cousins with identical sense ('to make smoke, burn incense'). No tier-promoting divergence to display.",
        },
        {
            "blau_id": 20277,
            "root_ar": "وشمة",
            "verse_hint": "Ex 21:6 (cluster: 20277-20280 وشمة/موسم/ميسمة/ميسا)",
            "reason": "Source-SQLite cluster head; the Shemot citation (Ex 21:6 ורצע אדניו את אזנו = the slave's ear-piercing) actually lives in the sibling root موسم/ميسم ('mark, brand'). The pairing Heb רצע ('awl') ↔ Ar موسم ('branding-iron') reads as a culturally-equivalent tool-substitution (Heb piercing-awl → Ar branding-iron) but is borderline-cognate enough to defer pending a focused Mishpatim-pericope re-walk.",
        },
    ],
    "borderline": [
        {
            "blau_id": 17513,
            "root_ar": "ضعيف",
            "verse_hint": "Ex 22:24",
            "open_question": "Surface (לצ'עיף) and Hebrew anchor (עני) both verified, but the Heb עני → Ar ضعيف pairing is a close register-shift cousin — both root-clusters orbit 'weakness/poverty' so the divergence may be sub-tier. Defer for a tier-judgment re-pass (note: cluster of 4 source rows 17513-17516 maps to a single Blau entry).",
        },
        {
            "blau_id": 19132,
            "root_ar": "لبن",
            "verse_hint": "Ex 1:14 / 5:7 / 5:8 / 5:14",
            "open_question": "Blau explicitly tags the verb لبن ('to mould bricks') as Hebrew-influenced ('השימוש תלוי בעברית המקרא … אינו חלק מאוצר המילים הערבי' per Ibn Janāḥ Shorashim 344). NOTE-tier in principle (denominal verb from a Heb-borrowed noun), but Saadia's Mishnaic-Hebrew-style use throughout Ex 5 is hard to gloss without inverting the bilingual frame for the reader. Defer.",
        },
    ],
    "_cluster_dupes_logged": [
        "17350≈17351 (جيب)",
        "17513≈17514≈17515≈17516 (ضعف cluster, 4 rows)",
        "17597≈17598 (عرم)",
        "17999≈18000 (غفر/غفارة)",
        "18778≈18779≈18780 (قوم cluster, 3 rows)",
        "19132≈19133≈19134 (لبن cluster, 3 rows)",
        "19545≈19546≈19547≈19548 (من time-interval cluster, 4 rows)",
        "20065≈20066≈20067≈20068 (هل Dirinburg cluster, 4 rows)",
        "20114≈20115≈20116≈20117≈20118 (هاون/هوي cluster, 5 rows)",
        "20277≈20278≈20279≈20280 (وشمة/موسم cluster, 4 rows, deferred)",
        "20402-20408 (ولع/ولف/توليف cluster, 7 rows, Ex 36:13 'to couple')",
    ],
}


def _update_deferred(deferred_path: pathlib.Path) -> dict:
    """Merge Batch 2 entries into data/_blau_saadia_deferred.json#/shemot.

    Idempotent on blau_id: re-running is safe; already-present IDs are
    left untouched. Returns a small summary for the run log.
    """
    payload = json.loads(deferred_path.read_text())
    sh = payload.setdefault("shemot", {})

    added = {"skip": 0, "borderline": 0, "phase3_r2_candidates": 0, "cross_book_dupes": 0}
    for bucket, new_items in BATCH2_DEFERRED.items():
        if bucket.startswith("_"):
            continue
        existing = sh.setdefault(bucket, [])
        existing_ids = {it.get("blau_id") for it in existing if isinstance(it, dict)}
        for item in new_items:
            if item.get("blau_id") in existing_ids:
                continue
            existing.append(item)
            existing_ids.add(item.get("blau_id"))
            added[bucket] = added.get(bucket, 0) + 1

    # Append (don't overwrite) the cluster-dupes log
    cluster_log = sh.setdefault("_cluster_dupes_logged", [])
    if isinstance(cluster_log, list):
        for line in BATCH2_DEFERRED["_cluster_dupes_logged"]:
            if line not in cluster_log:
                cluster_log.append(line)

    # Update the session tag (additive — keep Batch 1's tag if present)
    if "_session" in sh and "Batch 2" not in sh["_session"]:
        sh["_session"] = sh["_session"] + " + Phase 4 Shemot Batch 2 (apply_phase4_shemot_batch2.py)"
    else:
        sh.setdefault("_session", "Phase 4 Shemot Batch 2 (apply_phase4_shemot_batch2.py)")

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return {"added": added, "shemot_buckets_now": {k: len(v) if isinstance(v, list) else v for k, v in sh.items()}}


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

    print(f"Added {added} entries to {div_path.name}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")
    print(f"Deferred file summary: {json.dumps(deferred_summary, ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    main()

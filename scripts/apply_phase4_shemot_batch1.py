"""
Phase 4 — Shemot Batch 1.

Eleven hand-curated entries from blau_ids 13769-15700 of
data/_blau_saadia_candidates.json (the 168 Shemot-flagged subset). Each one
has been verified against data/tafsir-shemot-{ch}.json — the JA surface form
physically appears in the cited verse, and the Hebrew anchor word appears
in the verse's hebrew column.

Tier breakdown:
  - 7 GLOSS  — non-cognate Heb→Ar pairings, register shifts, technical extensions
  - 4 NOTE   — semantic surprises with short stated mechanism

Deferred (logged via _update_deferred() into data/_blau_saadia_deferred.json
under a new shemot.* namespace):
  - 2 SKIP:
    * 14097 برص on Ex 2:23 — Dirinburg-variant-only reading
      ("ולקה בצרעת ומת מלך מצרים" is Dirinburg's interpolated text, not the
      Cairo 2019 baseline; our tafsir-shemot-2.json doesn't reflect it).
    * 13864 إنطرك ('styrax') on Ex 30:34 — Tanḥum-routed, ch:v cite OCR-corrupted
      ("תרגם רס״ג לשמות ٦7:9 ׳נטף׳ לפי תנחום, בערכו").
  - 1 BORDERLINE:
    * 15549 دفق ('bar for carrying') on Ex 26:14 — Blau cites Ex 26:14 but
      the tafsir at that verse uses different lexemes for both 'covering'
      and any bar-language. Either recension difference or mis-cite. Defer.
  - 1 PHASE3_R2_CANDIDATE:
    * 14507 جريحة ('miracle / finger of God') on Ex 8:15 — shipped here as
      NOTE-tier but flagged for potential promotion to TWIST in a later
      Phase 3 R2 pass. Saadia's reframe of אצבע אלהים = 'miracle' is
      theologically loaded; Blau cites a Qirqisani parallel.
  - 1 CROSS_BOOK_DUPE:
    * 14897 حظاء — already shipped as חצ'אא (Gen 39:21) in Bereshit Batch 1.
      The Shemot filter caught on an incidental mention of 'ספר אברהם
      לבראשית ושמות'; all verse-anchored cites are Bereshit.

Cluster duplicates seen in the window (logged but not auto-deduped):
  - 14907 ≈ 14928 (both حفز / Ex 12:11 — same Blau article duplicated in source SQLite)
  - 14909 ≈ 14930 (both محفظ — co-article with حفز; not surfaced for Shemot)
  - 14717 ≈ 14719 (both حجر — verified no Shemot anchor; skipped silently)

Apply pattern mirrors scripts/apply_phase4_bereshit_batch1.py:280-310;
dedupe is on lemma_ja only (DivergenceEntry has no `id` field).
"""

import json
import pathlib
import sys
from collections import Counter


NEW_ENTRIES = [
    # ---- GLOSS — Ex 37:24: Menorah of one talent of pure gold --------------
    {
        "lemma_ja": "בדרה'",
        "variants": ["בדרה", "אלבדרה'"],
        "lemma_ar": "بذرة",
        "root": "ب-ذ-ر",
        "tier": "gloss",
        "classical_en": "talent (a weight of precious metal)",
        "classical_he": "כִּכָּר (משקל של מתכת יקרה)",
        "saadia_en": "a talent (weight)",
        "saadia_he": "ככר משקל",
        "mechanism": "Non-cognate weight-measure: Saadia renders Hebrew כִּכָּר ('talent') with بذرة rather than the standard Arabic قنطار/طلنط; Blau records this as the JA technical pairing.",
        "verses": [{"book": "Shemot", "ch": 37, "v": 24}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "بذر",
            "sense": "بذرة 'talent (weight)' — Blau attests citing Saadia on Ex 37:24 (and Ps reference); the standard JA term for the biblical כִּכָּר as a weight.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 28:15 / 28:22 / 28:30: Breastplate of judgment ----------
    {
        "lemma_ja": "בדנה",
        "variants": ["אלבדנה"],
        "lemma_ar": "بدنة",
        "root": "ب-د-ن",
        "tier": "note",
        "classical_en": "Classical Arabic بدنة is a sacrificial camel/animal — not a garment; Saadia repurposes the term as a technical name for the high priest's breastplate.",
        "classical_he": "בערבית הקלאסית بدنة היא בהמת קרבן (גמל), לא בגד; רס\"ג מאמץ את המילה כשם טכני לחושן הכהן הגדול.",
        "saadia_en": "breastplate (חושן)",
        "saadia_he": "חושן (לבוש הכהן הגדול)",
        "mechanism": "Hebraizing technical coinage: Blau explicitly tags بدنة here as 'hebraizing' — Saadia adopts an Arabic substantive of unrelated classical sense as a fixed JA equivalent for the priestly חוֹשֶׁן throughout the Mishkan pericope (also surfaces in the construction account at 39:8 ff.).",
        "verses": [
            {"book": "Shemot", "ch": 28, "v": 15},
            {"book": "Shemot", "ch": 28, "v": 22},
            {"book": "Shemot", "ch": 28, "v": 30},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "بدن",
            "sense": "بدنة '(hebraizing): breastplate of the high priest' — Blau records it citing Saadia on Ex 28:* (specifically 28:6 in the entry head; broader Mishkan usage).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 25:4 / 28:6 / 35:25: Blue/azure (Mishkan textiles) -----
    {
        "lemma_ja": "אסמאנגון",
        "variants": ["ואסמאנגון", "אלאסמאנגון"],
        "lemma_ar": "أسمانجون",
        "root": "أ-س-م-ا-ن-ج-و-ن",  # Persian loan, no triliteral root
        "tier": "gloss",
        "classical_en": "sky-blue, azure (a Persian loanword in Arabic from āsmān-gōn 'sky-colored')",
        "classical_he": "כחול-שמיים, תכלת (שאילה פרסית בערבית מ-آسمان-گون 'בצבע השמיים')",
        "saadia_en": "azure (תכלת)",
        "saadia_he": "תכלת",
        "mechanism": "Saadia's standard rendering of biblical תְּכֵלֶת throughout the Mishkan pericopes; a Persian loanword adopted into Arabic, with Aggron, al-Fāsī, and Ibn Janāḥ all citing this as the canonical equivalence.",
        "verses": [
            {"book": "Shemot", "ch": 25, "v": 4},
            {"book": "Shemot", "ch": 28, "v": 6},
            {"book": "Shemot", "ch": 35, "v": 25},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "أسمانجون",
            "sense": "أسمانجون 'light blue, azure' — Blau records Saadia using this consistently for תכלת (citing the Aggron, al-Fāsī's Jāmiʿ, and Ibn Janāḥ's Shorashim).",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 9:32: Wheat and spelt not struck because they were apil -
    {
        "lemma_ja": "אפלתאן",
        "variants": ["אפלה", "אפלאת"],
        "lemma_ar": "آفلتان",
        "root": "أ-ف-ل",
        "tier": "note",
        "classical_en": "Classical Arabic آفل = 'setting (of sun, stars)'; metaphor for 'unripe, hidden, late to emerge'.",
        "classical_he": "בערבית הקלאסית آفل = 'שוקע, נסוג'; מטאפורה ל'לא בשל, חבוי, מאחר להופיע'.",
        "saadia_en": "late-ripening, not yet ripe (dual: 'they two were unripe')",
        "saadia_he": "מאחרות להבשיל, עדיין לא בשלות (זוגי: שתיהן היו אפלות)",
        "mechanism": "Saadia renders the Hebrew hapax אֲפִילֹת ('late, not yet ripe') with Arabic dual آفلتان, drawing on the root أ-ف-ل meaning 'to set, be hidden, be unripe' — a semantic-field extension Blau hedges with 'possibly so understood' ('אפשר שכך הבינו רס״ג'), though the surface form physically appears in the verse, so the hedge is about why Saadia chose it (probably influenced by Hebrew אפיל), not whether.",
        "verses": [{"book": "Shemot", "ch": 9, "v": 32}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "أفل",
            "sense": "آفل 'unripe' (with feminine آفلة and feminine plural آفلات) — Blau cites Saadia on Ex 9:32 (אפלתאן for אפילת), and al-Fāsī's Jāmiʿ for the underlying interpretation that אפילים are 'crops not yet ripe, hidden in the ground'.",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 8:15: Magicians say 'finger of God' = miracle -----------
    {
        "lemma_ja": "גריחה",
        "variants": ["גריחאת"],
        "lemma_ar": "جريحة",
        "root": "ج-ر-ح",
        "tier": "note",
        "classical_en": "Classical Arabic جريحة normally = 'wound, injury' — not 'miracle'.",
        "classical_he": "בערבית הקלאסית جريحة היא בדרך כלל 'פצע, חבלה' — לא 'נס'.",
        "saadia_en": "a miracle, a wondrous sign",
        "saadia_he": "נס, אות פלא",
        "mechanism": "Saadia recasts 'אֶצְבַּע אֱלֹהִים' ('the finger of God') as a substantive abstraction: 'this is a miracle from God' (גריחה מן ענד אללה). Blau flags this as a distinctive Saadian-school usage with a Qirqisani parallel (Qirqisāni 2:303 uses the cognate جرائح for biblical 'signs and wonders'); Muḥīṭ al-Muḥīṭ glosses it as أعجوبة.",
        "verses": [{"book": "Shemot", "ch": 8, "v": 15}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "جرح",
            "sense": "جريحة 'miracle' (also glossed 'sign, wonder' / נם) — Blau attests citing Saadia on Ex 8:15 (with cross-references to Muḥīṭ al-Muḥīṭ and a Qirqisāni parallel at 2:303).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 30:12: Census — 'when I have enumerated them' ----------
    {
        "lemma_ja": "אחציתהם",
        "variants": ["אחצי", "יחצי", "חצא"],
        "lemma_ar": "أحصيتهم",
        "root": "ح-ص-ي",
        "tier": "gloss",
        "classical_en": "Form IV أحصى (root ح-ص-ي / cognate cluster with ح-ص-ر) — 'to enumerate completely, take a comprehensive count'.",
        "classical_he": "בניין IV של أحصى (משורש ح-ص-ي, קרוב לאשכול ح-ص-ر) — 'למנות בשלמות, לערוך מפקד ממצה'.",
        "saadia_en": "when I have counted them all",
        "saadia_he": "כאשר אמנה את כולם בשלמות",
        "mechanism": "Saadia chooses a verb of comprehensive enumeration for the technical Hebrew פָּקַד ('muster') in the census-and-half-shekel pericope, and shifts the grammatical person to divine 1st-singular ('when I have counted them') — adding subject-explicitness to the Hebrew passive-feel construction בִּפְקֹד אֹתָם.",
        "verses": [{"book": "Shemot", "ch": 30, "v": 12}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "حصر",
            "sense": "حصر (Form I) 'to count, often with the connotation of enumerating all occurrences; to include entirely, to summarize completely' — Blau cites Saadia on Ex 30:12 for the JA census-enumeration usage (Form IV surface أحصى belongs to the related root ح-ص-ي; the senses cluster).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 12:11: Passover eaten in haste -------------------------
    {
        "lemma_ja": "בחפז",
        "variants": ["חפז", "חפזא"],
        "lemma_ar": "بحفز",
        "root": "ح-ف-ز",
        "tier": "gloss",
        "classical_en": "Classical Arabic حفز = 'haste, urging on' (also 'panic'); with prepositional ب- = 'in haste'.",
        "classical_he": "בערבית הקלאסית حفز = 'דחיפות, האצה' (וגם 'בהלה'); עם מילת היחס ب- = 'בחיפזון'.",
        "saadia_en": "in haste",
        "saadia_he": "בחיפזון",
        "mechanism": "Consonantal-calque pairing (Heb ḥ-p-z ~ Ar ḥ-f-z) — but Saadia strips the Hebrew -on abstract suffix (חִפָּזוֹן → حفز), rendering the prepositional בְּחִפָּזוֹן with the bare verbal noun in the same prep. Blau records the parallel JA idiom بحفزون = בחפזון.",
        "verses": [{"book": "Shemot", "ch": 12, "v": 11}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "حفز",
            "sense": "حفز 'haste (and panic)'; idiom بحفزون = בחפזון, idiom بحفزي = בחפזי. Blau cites Saadia on Ex 12:11, Deut 16:3, Isa 52:12 ('כי לא בחפזון תצאו'), and Ps 31:23 / 116:11.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 9:8: 'Take your dual handfuls of furnace soot' ---------
    {
        "lemma_ja": "חפניכמא",
        "variants": ["חפן", "חפנה", "חפניהם"],
        "lemma_ar": "حفنيكما",
        "root": "ح-ف-ن",
        "tier": "gloss",
        "classical_en": "Classical Arabic uses the feminine حَفْنَة 'a handful'; the masculine حفن (without the feminine suffix) is non-standard.",
        "classical_he": "בערבית הקלאסית המילה הרגילה ל'חופן' היא حَفْنَة (בנקבה); הצורה حفن (בלי סיומת נקבה) אינה סטנדרטית.",
        "saadia_en": "the dual of your two handfuls",
        "saadia_he": "מלוא חופניכם (זוגי)",
        "mechanism": "Register choice with Hebrew influence: Blau explicitly notes 'ולא حفنة, מן הסתם בהשפעת העברית' — Saadia picks the bare-stem حفن (closer to the consonantal Hebrew חֹפֶן) over the standard Arabic feminine حَفْنَة. The dual ending -hima resolves the biblical חָפְנֵיכֶם addressed to Moses and Aaron.",
        "verses": [{"book": "Shemot", "ch": 9, "v": 8}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "حفن",
            "sense": "حفن 'handful' — Blau notes 'not حفنة; presumably influenced by Hebrew'. Cites Saadia on Ex 9:8 as the canonical example.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 22:15: Seducer of a virgin must pay bride-price --------
    {
        "lemma_ja": "כ'דע",
        "variants": ["יכ'דע", "כ'דעא"],
        "lemma_ar": "خدع",
        "root": "خ-د-ع",
        "tier": "gloss",
        "classical_en": "Classical Arabic خدع = 'to deceive, beguile' (Form I); applied also to sexual seduction.",
        "classical_he": "בערבית הקלאסית خدع = 'הונה, רימה' (בניין I); משמש גם לפיתוי מיני.",
        "saadia_en": "if (a man) seduces (a virgin)",
        "saadia_he": "ואם (אדם) פיתה (בתולה)",
        "mechanism": "Non-cognate semantic-field pairing: Hebrew פתה ('persuade, entice, become open') is rendered with Arabic خدع ('deceive, seduce') — different lexical field but matching the legal context of unauthorized intercourse with an unbetrothed virgin. Blau cites the parallel rendering at Prov 1:10 ('אם יפתוך חטאים').",
        "verses": [{"book": "Shemot", "ch": 22, "v": 15}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "خدع",
            "sense": "خدع (Form I) 'to seduce' — Blau cites Saadia on Ex 22:15 ('וכי יפתה איש בתולה' = ואן כ'דע רג'ל ג'אריה) as the canonical attestation; Form III 'try to seduce', Form VII 'be seduced' (Deut 11:16, Job 31:9).",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Ex 12:49: 'One law for the citizen and the resident-alien' -
    {
        "lemma_ja": "אלדכ'יל",
        "variants": ["דכ'יל", "אלדכ'ילה"],
        "lemma_ar": "الدخيل",
        "root": "د-خ-ل",
        "tier": "gloss",
        "classical_en": "Classical Arabic دخيل = 'newcomer, intruder'; in legal/religious usage 'a convert, proselyte, neophyte'.",
        "classical_he": "בערבית הקלאסית دخيل = 'נכנס, זר'; בשימוש משפטי-דתי 'גר, מתגייר, מצטרף'.",
        "saadia_en": "the resident-alien who has entered (the covenant)",
        "saadia_he": "הגֵּר הנכנס (לברית/לעם)",
        "mechanism": "Saadia renders Hebrew גֵּר with a doublet: the standard ج‍ـريب ('stranger') paired with دخيل ('one who has entered, convert'). The دخيل element adds the religious-legal nuance — 'one who has joined the community' — that Qirqisāni later picks up explicitly ('אלדכ'יל פי אלדין' = the one who has entered the religion).",
        "verses": [{"book": "Shemot", "ch": 12, "v": 49}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "دخل",
            "sense": "دخيل 'neophyte, convert, proselyte' — Blau cites Saadia on Ex 12:49 ('תורה אחת יהיה לאזרח ולגר' = שריעה ואחדה תכון לאלצריח ואלג'ריב אלדכ'יל) and the Qirqisāni parallel (7:501).",
            "relation": "direct",
        },
    },
    # ---- NOTE — Ex 25:5 / 26:14: Tachash skins for the tabernacle ----------
    {
        "lemma_ja": "דארש",
        "variants": ["אלדארש"],
        "lemma_ar": "دارش",
        "root": "د-ا-ر-ش",  # loanword, treated as quadriliteral
        "tier": "note",
        "classical_en": "دارش = a specific kind of black-dyed leather used in tanning and shoemaking (loanword in Arabic; Qāmūs and al-Jawālīqī attest it).",
        "classical_he": "دارش = סוג מסוים של עור מעובד שחור, המשמש בעיבוד-עור ובסנדלרות (שאילה לערבית; הקאמוס ואל-ג'ואליקי מתעדים זאת).",
        "saadia_en": "(skins of) black-dyed leather (for the biblical תַּחַשׁ)",
        "saadia_he": "(עורות) דארש שחורים (לתחש המקראי)",
        "mechanism": "Parshanic identification: Saadia identifies the long-disputed biblical תַּחַשׁ with a culturally specific tanning product known to medieval Egypt — 'black-dyed leather' — rather than naming a particular animal. Blau notes the choice propagated through JA: al-Fāsī's Jāmiʿ glosses תחש ↔ דארש, and Ibn Janāḥ's Shorashim transmits the identification.",
        "verses": [
            {"book": "Shemot", "ch": 25, "v": 5},
            {"book": "Shemot", "ch": 26, "v": 14},
        ],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "دارش",
            "sense": "دارش 'black leather' (from al-Qāmūs; al-Jawālīqī, 145:2 with the spelling note ספרת) — Blau cites Saadia on Ex 25:5 ('ועורות תחשים' = וגלוד דארש) as the foundational attestation, followed by al-Fāsī (Jāmiʿ ב, 730) and Ibn Janāḥ (Shorashim 760:12-13).",
            "relation": "direct",
        },
    },
]


def _update_deferred(deferred_path: pathlib.Path) -> dict:
    """Append the shemot.* namespace to data/_blau_saadia_deferred.json.

    Idempotent: if the shemot key already exists, leave it alone (re-run safe).
    Returns a small summary dict for the run log.
    """
    payload = json.loads(deferred_path.read_text())
    if "shemot" in payload:
        return {"created": False, "reason": "shemot namespace already present; left untouched"}

    payload["shemot"] = {
        "skip": [
            {
                "blau_id": 14097,
                "root_ar": "برص",
                "verse_hint": "Ex 2:23",
                "reason": "Dirinburg-variant-only reading ('ולקה בצרעת ומת מלך מצרים'); not in baseline Cairo 2019 tafsir-shemot-2.json.",
            },
            {
                "blau_id": 13864,
                "root_ar": "إنطرك",
                "verse_hint": "Ex 30:34 (?)",
                "reason": "Tanḥum-routed citation ('תרגם רס״ג לשמות … לפי תנחום, בערכו'); ch:v OCR-corrupted as '٦7:9'. No direct verse anchor in baseline tafsir.",
            },
        ],
        "borderline": [
            {
                "blau_id": 15549,
                "root_ar": "دفق",
                "verse_hint": "Ex 26:14",
                "open_question": "Blau cites Saadia on Ex 26:14 for 'دهق / دهوق' ('bar for carrying'), but tafsir-shemot-26.json at v.14 uses different lexemes (no bar-language in the covering verse). Either a recension difference or a mis-cite; defer pending cross-check against bar-pericopes (25:13-14, 27:6).",
            },
        ],
        "phase3_r2_candidates": [
            {
                "blau_id": 14507,
                "root_ar": "جريحة",
                "verse_hint": "Ex 8:15",
                "twist_thesis": "Saadia recasts 'finger of God' (אצבע אלהים) as 'miracle' (גריחה מן ענד אללה) — theological reframe that turns a divine body-part idiom into an abstract event-noun. Paralleled by Qirqisāni (2:303 uses cognate جرائح for biblical 'signs and wonders') per Blau. Shipped in Batch 1 as NOTE-tier; promotion candidate for a future Shemot Phase 3 R2 pass.",
            },
        ],
        "cross_book_dupes": [
            {
                "blau_id": 14897,
                "root_ar": "حظاء",
                "note": "Already shipped as חצ'אא (Gen 39:21) in Bereshit Batch 1. Shemot filter caught on incidental mention of 'ספר אברהם לבראשית ושמות'; all verse-anchored citations in this Blau entry are Bereshit.",
            },
        ],
        "_session": "Phase 4 Shemot Batch 1 (apply_phase4_shemot_batch1.py)",
    }

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return {
        "created": True,
        "skip": len(payload["shemot"]["skip"]),
        "borderline": len(payload["shemot"]["borderline"]),
        "phase3_r2_candidates": len(payload["shemot"]["phase3_r2_candidates"]),
        "cross_book_dupes": len(payload["shemot"]["cross_book_dupes"]),
    }


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
    print(f"Deferred file: {deferred_summary}")


if __name__ == "__main__":
    main()

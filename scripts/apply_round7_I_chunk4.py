#!/usr/bin/env python3
"""Phase 2 Round 7 Batch I — chunk 4 (25 candidates).

Adds 17 new lemmas + 8 lane-variant patches + 1 starter-variant patch.

Two notable homographs:
  • עגל (ʿagalah-wagon already adds it as variant; here we add ʿijl-calf
    as a second sense — reader displays both, context disambiguates).
  • אם (am-or-particle; here we add umm-mother as a second sense).

Two scribal-variant patches:
  • הזה onto hadhihi (ז for ד' is Saadianic orthographic variation).
  • זאלך onto dhalik (same ז↔ד' alternation).
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Nouns ----------
    {
        "id": "hasana-merit",
        "lemma_ja": "חסנה",
        "lemma_ar": "حَسَنَة",
        "root": "ḥ-s-n",
        "pos": "noun (f.) / adjective (f., construct)",
        "gloss_en": "(1) a good deed, merit, righteous act; (2) beautiful (fem.sg. of ḥasan)",
        "gloss_he": "(1) זְכוּת, צְדָקָה, מַעֲשֶׂה טוֹב; (2) יָפָה",
        "saadia_note": "Saadia's regular gloss for Hebrew צְדָקָה in the merit sense (Gen 15:6: וכתבהא לה חסנה 'and he counted it to him as a meritorious deed' = וַיַּחְשְׁבֶהָ לּוֹ צְדָקָה). In construct-state usage חסנה' אלמנצ'ר 'beautiful of appearance' renders Heb יְפַת מַרְאֶה (Gen 12:11; 24:16).",
        "source": "lane",
        "variants": [
            "אלחסנה", "ואלחסנה",
            "וחסנה", "באלחסנה",
            "חסנאת", "אלחסנאת", "ואלחסנאת",
            "חסנה'", "חסנה' אלמנצ'ר",
        ],
    },
    {
        "id": "manzar-appearance",
        "lemma_ja": "מנצ'ר",
        "lemma_ar": "مَنْظَر",
        "root": "n-ẓ-r",
        "pos": "noun (m.)",
        "gloss_en": "appearance, sight, look, view; that which is seen",
        "gloss_he": "מַרְאֶה, מַחֲזֶה",
        "saadia_note": "Saadia's regular gloss for Hebrew מַרְאֶה in the recurring formula 'beautiful in appearance' (יְפַת מַרְאֶה → חסנה' אלמנצ'ר; Gen 12:11; 24:16; 29:17, etc.).",
        "source": "lane",
        "variants": [
            "אלמנצ'ר", "ואלמנצ'ר",
            "ומנצ'ר", "באלמנצ'ר",
            "מנצ'רה", "מנצ'רהא",
            "מנאצ'ר", "אלמנאצ'ר",
        ],
    },
    {
        "id": "ijl-calf",
        "lemma_ja": "עגל",
        "lemma_ar": "عِجْل",
        "root": "ʿ-j-l",
        "pos": "noun (m.)",
        "gloss_en": "calf (young of cattle); bullock",
        "gloss_he": "עֵגֶל",
        "notes": "Homograph with ʿagalah/ʿagal 'wagon, cart' (same root ʿ-j-l). Context disambiguates: ʿijl is always animate, the offspring or young of cattle. Saadia uses it for Hebrew עֵגֶל.",
        "saadia_note": "Saadia's regular gloss for Hebrew עֵגֶל (calf) in non-cultic narrative — e.g. Abraham's hospitality (Gen 18:7 עגלא רכ'צ'א וטייבא 'a tender, good calf'); Gen 15:9 (Covenant of the Pieces).",
        "source": "lane",
        "variants": [
            "אלעגל", "ועגל", "באלעגל", "ללעגל",
            "עגלא", "ועגלא",
            "עגול", "אלעגול",
            "עגלין", "אלעגלין", "ועגלין",
        ],
    },
    {
        "id": "qalil-little",
        "lemma_ja": "קליל",
        "lemma_ar": "قَلِيل",
        "root": "q-l-l",
        "pos": "adjective / noun (m.)",
        "gloss_en": "little, few; a small amount, a bit (of)",
        "gloss_he": "מְעַט, מִעוּט",
        "notes": "Often used adverbially: قَلِيلًا (qalīlan) = 'a little, slightly'. Distinct from kathīr 'much, many'.",
        "saadia_note": "Saadia's regular gloss for Hebrew מְעַט — 'a little water' (Gen 18:4 קליל מן מא; Gen 24:17 קליל מאא = מְעַט מַיִם).",
        "source": "lane",
        "variants": [
            "אלקליל", "ואלקליל",
            "וקליל", "בקליל",
            "קלילא", "וקלילא",
            "קלילון", "אלקלילון",
            "קליל מן", "קליל מא",
        ],
    },
    {
        "id": "umm-mother",
        "lemma_ja": "אם",
        "lemma_ar": "أُمّ",
        "root": "ʔ-m-m",
        "pos": "noun (f.)",
        "gloss_en": "mother",
        "gloss_he": "אֵם",
        "notes": "Homograph with am-or-particle (lemma אם, the disjunctive 'or'). Context disambiguates: 'mother' always with possessive suffix or as construct head, 'or' as a sentence-medial particle.",
        "saadia_note": "Saadia's regular gloss for Hebrew אֵם — the matriarchs, the mother-of-a-house, and the recurring 'his mother' / 'your mother' formulas.",
        "source": "lane",
        "variants": [
            "אמה", "אמהא", "אמך", "אמכם", "אמהם", "אמי", "אמנא", "אמכמא", "אמהמא",
            "אלאם", "ואלאם", "באלאם",
            "אמהאת", "אלאמהאת", "ואלאמהאת",
            "בני אם", "בני אמך", "אבן אם",
        ],
    },
    {
        "id": "sijn-prison",
        "lemma_ja": "סגן",
        "lemma_ar": "سِجْن",
        "root": "s-j-n",
        "pos": "noun (m.)",
        "gloss_en": "prison, jail",
        "gloss_he": "בֵּית הַסֹּהַר, כֶּלֶא",
        "saadia_note": "Saadia's regular gloss for Hebrew בֵּית הַסֹּהַר in the Joseph narrative (Gen 39:20-23; 40 passim — אלסגן 'the prison'; רייס אלסגן 'the warden of the prison').",
        "source": "lane",
        "variants": [
            "אלסגן", "ואלסגן",
            "וסגן", "באלסגן", "ללסגן",
            "פי אלסגן", "אלי' אלסגן",
            "רייס אלסגן",
            "סגון", "אלסגון",
        ],
    },
    {
        "id": "makan-place",
        "lemma_ja": "מכאן",
        "lemma_ar": "مَكَان",
        "root": "k-w-n",
        "pos": "noun (m.)",
        "gloss_en": "place, location, spot; (idiomatic) standing, position",
        "gloss_he": "מָקוֹם",
        "notes": "The full-form synonym of moḍiʿ (موضع) which Saadia uses more often in the Pentateuch for Heb מָקוֹם.",
        "saadia_note": "Saadia uses both مكان (mawḍiʿ-like) and موضع interchangeably for Hebrew מָקוֹם. The adverbial 'a place for X' (Deut 1:33 ליצלח לכם מכאנא לנזולכם 'to prepare for you a place for your encampment'; Exod 25:27) takes the accusative-indefinite.",
        "source": "lane",
        "variants": [
            "אלמכאן", "ואלמכאן",
            "מכאנא", "ומכאנא", "במכאן", "באלמכאן",
            "מכאנה", "מכאנהא", "מכאנכם", "מכאנהם",
            "אמכנה", "אלאמכנה", "ואלאמכנה",
        ],
    },
    {
        "id": "baqar-cattle",
        "lemma_ja": "בקר",
        "lemma_ar": "بَقَر",
        "root": "b-q-r",
        "pos": "noun (m., collective)",
        "gloss_en": "cattle (collective); herd, oxen",
        "gloss_he": "בָּקָר",
        "notes": "Masculine collective. Distinct from baqara (lemma בקרה, fem.sg.) 'cow'. Saadia uses bāqar / al-baqar for the collective Heb בָּקָר and baqara for the individual cow.",
        "saadia_note": "Saadia's regular gloss for Hebrew בָּקָר collectively — including in the recurring 'your cattle and your flock' (בְּקָרְךָ וְצֹאנְךָ → בקרך וג'נמך, Deut 12:17, 12:21, 14:23, etc.).",
        "source": "lane",
        "variants": [
            "אלבקר", "ואלבקר", "באלבקר",
            "בקרך", "בקרכם", "בקרהם", "בקרנא", "בקרהא",
            "בקרי", "אבקאר", "אלאבקאר",
        ],
    },
    {
        "id": "yatim-orphan",
        "lemma_ja": "יתים",
        "lemma_ar": "يَتِيم",
        "root": "y-t-m",
        "pos": "noun / adjective (m.)",
        "gloss_en": "orphan; fatherless child",
        "gloss_he": "יָתוֹם",
        "saadia_note": "Saadia's regular gloss for Hebrew יָתוֹם — always in the protected-classes triad 'the stranger, the orphan, and the widow' (אלג'ריב ואליתים ואלארמלה: Deut 10:18; 14:29; 16:11; 16:14; 24:17-21; 26:12-13; 27:19).",
        "source": "lane",
        "variants": [
            "אליתים", "ואליתים",
            "ויתים", "באליתים", "ליתים",
            "אלאיתאם", "ואלאיתאם", "באלאיתאם", "איתאם",
            "יתאמא", "אליתאמא",
        ],
    },
    {
        "id": "hurr-free",
        "lemma_ja": "חר",
        "lemma_ar": "حُرّ",
        "root": "ḥ-r-r",
        "pos": "noun / adjective (m.)",
        "gloss_en": "free, free-born; (as noun) a free person; (in manumission contexts) freed",
        "gloss_he": "בֶּן־חוֹרִין, חָפְשִׁי",
        "saadia_note": "Saadia's regular gloss for Hebrew חָפְשִׁי in the slave-release passages (Deut 15:12-13: אטלקה חרא 'release him as a freedman'; Exod 21:2, 5).",
        "source": "lane",
        "variants": [
            "אלחר", "ואלחר",
            "וחר", "באלחר",
            "חרא", "וחרא",
            "אחראר", "אלאחראר", "ואלאחראר",
            "חרה", "אלחרה", "חראיר", "אלחראיר",
        ],
    },

    # ---------- Verbs ----------
    {
        "id": "waqaʿa-fall",
        "lemma_ja": "וקע",
        "lemma_ar": "وَقَع",
        "root": "w-q-ʿ",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to fall, drop down; to happen, occur, befall; (with ʿalā) to come upon, descend on",
        "gloss_he": "נָפַל, אֵרַע, יָרַד עַל",
        "saadia_note": "Saadia's regular gloss for Hebrew נָפַל both literally (Gen 15:12 וקע סבאת עלי' אברם 'a deep sleep fell upon Abram'; Num 14:5 פוקע מוסי' והרון 'Moses and Aaron fell upon their faces') and idiomatically (וקע וגהך 'your face has fallen' = Gen 4:6).",
        "source": "lane",
        "variants": [
            "וקעת", "וקעו", "ווקע", "פוקע", "פוקעא",
            "ווקעת", "ווקעו",
            "יקע", "ויקע", "תקע",
            "אקע", "נקע",
            "ואקע", "אלואקע", "ואלואקע",
            "וקועא", "אלוקוע",
        ],
    },
    {
        "id": "hadhira-beware",
        "lemma_ja": "חד'ר",
        "lemma_ar": "حَذِر",
        "root": "ḥ-dh-r",
        "pos": "verb (Form I, perfect) / imperative iḥdhar",
        "gloss_en": "to beware, take care, guard oneself (against); (imperative) iḥdhar = 'beware! take care!'",
        "gloss_he": "נִזְהַר, הִשָּׁמֶר",
        "saadia_note": "Saadia's regular gloss for Hebrew הִשָּׁמֶר 'beware!' in admonitions (Gen 24:6 אחד'ר אן תרד אבני 'beware that you not take my son back'; Gen 31:24 אחד'ר אן תכלם יעקב 'beware that you not speak to Jacob anything from good to bad').",
        "source": "lane",
        "variants": [
            "אחד'ר", "ואחד'ר", "פאחד'ר",
            "אחד'רוא", "ואחד'רוא", "פאחד'רוא",
            "יחד'ר", "תחד'ר", "ויחד'ר",
            "חד'רא", "אלחד'ר", "ואלחד'ר",
            "חאד'ר",
        ],
    },
    {
        "id": "zala-deviate",
        "lemma_ja": "זאל",
        "lemma_ar": "زَال",
        "root": "z-w-l",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to turn aside, deviate, swerve; to depart from",
        "gloss_he": "סָר, נָטָה (מן הדרך)",
        "saadia_note": "Saadia's regular gloss for Hebrew סוּר (in 'turn aside from' the way / from the commandment) — especially Deut 17:11, 17:20, 28:14: לא תזול מן אלאמר 'do not turn aside from the commandment'.",
        "source": "lane",
        "variants": [
            "תזול", "לא תזול", "ולא תזול",
            "זאלת", "זאלו",
            "יזול", "ויזול", "פיזול",
            "אזול", "נזול",
            "זאיל", "אלזאיל", "ולא יזול",
        ],
    },
    {
        "id": "baraka-bless",
        "lemma_ja": "בארך",
        "lemma_ar": "بَارَك",
        "root": "b-r-k",
        "pos": "verb (Form III, perfect)",
        "gloss_en": "to bless, invoke blessing on; (with ʿalā or fī) to bless [s.o.]",
        "gloss_he": "בֵּרֵךְ",
        "notes": "Form III bāraka 'to bless' — passive participle mubārak 'blessed' is already in the dict.",
        "saadia_note": "Saadia's regular gloss for Hebrew בֵּרֵךְ — God blessing the patriarchs (Gen 28:3 יבארך עליך 'he will bless you'; Gen 48:16 יבארך פי הד'ין אלג'לאמין 'may he bless these two lads'); the priestly blessing (Num 6:24).",
        "source": "lane",
        "variants": [
            "ובארך", "פבארך",
            "יבארך", "ויבארך", "פיבארך", "תבארך",
            "אבארך", "נבארך",
            "בארכת", "בארכוא", "בארכנא",
            "מבארך",   # also has its own entry — linked
            "תבארכה", "מן תבארכה",
        ],
    },

    # ---------- Function / exclamation ----------
    {
        "id": "labbayka",
        "lemma_ja": "לביך",
        "lemma_ar": "لَبَّيْكَ",
        "root": "l-b-b",
        "pos": "exclamatory response",
        "gloss_en": "'here I am!', 'at your service!', 'I am listening' — the formulaic response to a call",
        "gloss_he": "הִנֵּנִי",
        "notes": "Originally the dual of labb 'one who responds positively/repeatedly'; later frozen as a formulaic response. Used in pilgrimage formulas and in conversational responses.",
        "saadia_note": "Saadia's regular gloss for Hebrew הִנֵּנִי when used as a response to being called by name — the Akedah dialogue (Gen 22:1, 22:7, 22:11), Jacob (Gen 31:11), Moses (Exod 3:4), Samuel (1 Sam 3:4).",
        "source": "lane",
        "variants": [
            "ולביך", "פלביך",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "zoar-place",
        "lemma_ja": "זג'ר",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Zoar — one of the Cities-of-the-Plain; Lot's refuge after the destruction of Sodom (Gen 13:10; 14:2, 8; 19:22-23, 30; Deut 34:3)",
        "gloss_he": "צֹעַר",
        "notes": "Originally Bela (Gen 14:2, 8); renamed Zoar after Lot's refuge. The Arabic-Hebrew correspondence ZGR↔ZOR uses ghain (ג') for the Hebrew ʿayin sound.",
        "saadia_note": "Saadia retains the Hebrew name. The form זג'ר reflects the standard rendering of Hebrew ʿayin into Arabic via ghain (غ).",
        "source": "lane",
        "variants": [
            "וזג'ר", "לזג'ר", "בזג'ר",
            "אלי' זג'ר",
        ],
    },
    {
        "id": "enoch-name",
        "lemma_ja": "חנוך",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Hanoch / Enoch — (1) son of Cain (Gen 4:17-18); (2) son of Jared (Gen 5:18-24), 'who walked with God'; (3) son of Reuben (Gen 46:9; Num 26:5); (4) grandson of Abraham via Midian (Gen 25:4)",
        "gloss_he": "חֲנוֹךְ",
        "saadia_note": "Saadia retains the Hebrew name unchanged. Used for all four scripturally-distinct figures of the same name.",
        "source": "lane",
        "variants": [
            "וחנוך", "לחנוך", "בחנוך",
            "אבן חנוך", "בני חנוך",
        ],
    },
]


VARIANTS_PATCH = {
    "amr-matter":     ["אמרתך", "אמרתכם", "אמרתהם", "אמרתה", "אמרתהא"],
    "akh-brother":    ["אכי'ך", "אכי'ה", "אכי'הא", "אכי'כם", "אכי'הם"],   # scribal yod-apos variant
    "tisʿa-nine":     ["תסע", "ותסע", "פתסע"],   # fem-counted 'nine' / 'ninety' stem
    "khataʾ-sin":     ["כ'טייה", "אלכ'טייה", "וכ'טייה", "כ'טייתה", "כ'טייתהא", "כ'טייתי", "כ'טייתכם", "כ'טייתהם", "כ'טאיא", "אלכ'טאיא"],
    "hadhihi":        ["הזה", "ולהזה", "והזה", "פהזה"],
    "haadha":         ["הזא", "פהזא", "והזא"],
}

STARTER_VARIANTS_PATCH = {
    "dhalik":         ["זאלך", "וזאלך", "פזאלך", "ולזאלך"],
}


def main():
    lane_path = pathlib.Path("data/dictionary-lane.json")
    starter_path = pathlib.Path("data/dictionary-starter.json")
    if not lane_path.exists() or not starter_path.exists():
        print("FATAL: dict files not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
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

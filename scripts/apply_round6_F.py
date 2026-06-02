#!/usr/bin/env python3
"""Phase 2 Round 6 Batch F — head-of-queue hand cleanup.

Adds 11 new lemma entries + 4 variant patches to data/dictionary-lane.json
for the remaining top-15 misses (count 15-17) after Round 5.

Variants targets:
  - sanaa         (לemma צנע)     → add תצנעה  (2ms impf + 3ms obj)
  - bikr-firstborn (לemma בכר)    → add בכ'ורא (his firstborn, alt-orthography)
  - akala-eat     (לemma אכל)     → add תאכלוה (2mp impf + 3ms obj)
  - ʿabd-servant  (לemma עבד)     → add עבדא   (accusative indefinite)

New-lemma rationale:
  - ghasala-wash       (גסל w/ apos)  — root g̲-s-l; verb stem missing entirely
  - sharifa-burning    (שריפה)        — Hebrew loanword used for sacrificial burning
  - thawr-bull         (ת'ור)         — high-value sacrificial vocab
  - ʿada-except        (עדא)          — function word; distinct from sawa-besides (s-w-y)
  - hajj-festival      (חג)           — Saadia's regular gloss for חַג
  - fatir-unleavened   (פטיר)         — classical Arabic for matzah
  - gharasa-drive-out  (גרש)          — Hebrew loan in JA; calque for Heb. גירש
  - muqarrab-offering  (מקרב)         — passive ptcp; Saadia's gloss for קָרְבָּן
  - aṣghar-smaller     (אצג'ר)        — comparative; Saadia's gloss for הַקָּטֹן
  - wahsh-wild         (וחש)          — note: leading ו is root w-, not prefix
  - kayla-lest         (כילא)         — kay + lā compound conjunction
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Verbs ----------
    {
        "id": "ghasala-wash",
        "lemma_ja": "ג'סל",
        "lemma_ar": "غَسَل",
        "root": "gh-s-l",
        "pos": "verb",
        "gloss_en": "to wash, cleanse, rinse (with water)",
        "gloss_he": "רחץ, שטף",
        "source": "lane",
        "variants": [
            "יג'סל", "אג'סל", "תג'סל", "נג'סל",
            "פיג'סל", "ויג'סל",
            "ג'סלו", "ג'סלוא", "וג'סלוא", "פג'סלוא",
            "תג'סלון", "וג'סלהא", "וג'סלה",
            "ג'סלת", "ג'סלתה",
        ],
    },
    {
        "id": "gharasa-drive-out",
        "lemma_ja": "גרש",
        "lemma_ar": "جَرَش",
        "root": "—",
        "pos": "verb",
        "gloss_en": "to drive out, expel, banish",
        "gloss_he": "גירש, הוציא, הבריח",
        "saadia_note": "Saadia uses the Hebrew root גרש directly as a Judeo-Arabic verb. The standard classical Arabic equivalents are ṭarada (طرد) and akhraja (أخرج).",
        "source": "lane",
        "variants": [
            "וגרש", "אגרש", "תגרש", "יגרש", "נגרש",
            "פגרש", "פאגרש", "וגרשו", "וגרשוא",
            "אגרשהם", "אגרשהא", "פגרשהם", "וגרשהם",
            "גרשתהם", "גרשנא", "גרשתה",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "sharifa-burning",
        "lemma_ja": "שריפה",
        "lemma_ar": "شَرِيفَة",
        "root": "—",
        "pos": "noun (f., verbal-noun)",
        "gloss_en": "burning, incineration (especially of a sacrificial animal)",
        "gloss_he": "שריפה (של קרבן)",
        "saadia_note": "Saadia adopts the Hebrew noun שְׂרֵפָה (śərēfā) directly. The classical Arabic equivalents are ḥarq (حرق) and iḥrāq (إحراق).",
        "source": "lane",
        "variants": [
            "ושריפה", "אלשריפה", "באלשריפה",
            "שריפהא", "שריפהם", "ושריפהם", "ושריפהא",
            "שריפתה", "שריפתהא",
        ],
    },
    {
        "id": "thawr-bull",
        "lemma_ja": "ת'ור",
        "lemma_ar": "ثَوْر",
        "root": "th-w-r",
        "pos": "noun (m.)",
        "gloss_en": "bull, ox (adult male of cattle)",
        "gloss_he": "פר, שור",
        "source": "lane",
        "variants": [
            "אלת'ור", "ות'ור", "ואלת'ור",
            "בת'ור", "באלת'ור", "לת'ור", "לאלת'ור",
            "ת'יראן", "אלת'יראן", "ות'יראן", "ואלת'יראן",
        ],
    },
    {
        "id": "hajj-festival",
        "lemma_ja": "חג",
        "lemma_ar": "حَجّ",
        "root": "ḥ-j-j",
        "pos": "noun (m.)",
        "gloss_en": "pilgrimage festival; (broader) festival, feast",
        "gloss_he": "חג",
        "saadia_note": "In classical Arabic ḥajj specifically denotes the pilgrimage. Saadia uses חג as the regular gloss for Hebrew חַג (any of the three pilgrimage festivals Pesach, Shavuot, Sukkot — and by extension any festival).",
        "source": "lane",
        "variants": [
            "וחג", "אלחג", "ואלחג", "לחג", "לאלחג",
            "חגנא", "חגכם", "חגיכם", "חגיהם",
            "חגא", "וחגא",
        ],
    },
    {
        "id": "fatir-unleavened",
        "lemma_ja": "פטיר",
        "lemma_ar": "فَطِير",
        "root": "f-ṭ-r",
        "pos": "noun / adjective (m.)",
        "gloss_en": "unleavened bread; freshly-baked dough that has not risen — matzah",
        "gloss_he": "מצה, לחם לא חמץ",
        "source": "lane",
        "variants": [
            "פטירא", "אלפטיר", "ופטיר", "ואלפטיר",
            "אלפטירא", "ואלפטירא",
            "פטירכם", "פטירכמא", "פטירהם",
        ],
    },
    {
        "id": "muqarrab-offering",
        "lemma_ja": "מקרב",
        "lemma_ar": "مُقَرَّب",
        "root": "q-r-b",
        "pos": "noun / passive participle (m.)",
        "gloss_en": "that which is brought near; (technical) an offering, sacrifice",
        "gloss_he": "קרבן, מנחה",
        "notes": "Form-II passive participle of qarraba 'to bring near'. Active muqarrib = 'one who brings near'; passive muqarrab = 'that which is brought near'.",
        "saadia_note": "Saadia uses muqarrab as the regular technical gloss for Hebrew קָרְבָּן (offering, sacrifice).",
        "source": "lane",
        "variants": [
            "אלמקרב", "ומקרב", "ואלמקרב", "באלמקרב",
            "מקרבכם", "מקרבהם", "מקרבה", "מקרבהא",
            "אלמקרבון", "מקרבון", "אלמקרבין", "מקרבין",
            "מקרבאת", "אלמקרבאת",
        ],
    },
    {
        "id": "wahsh-wild",
        "lemma_ja": "וחש",
        "lemma_ar": "وَحْش",
        "root": "w-ḥ-sh",
        "pos": "noun (m.)",
        "gloss_en": "wild beast, predator, untamed animal (game animals of the open country)",
        "gloss_he": "חיית בר, חית השדה",
        "notes": "Leading ו is the root letter (w-ḥ-sh), NOT the conjunction prefix. Surface form is identical to a hypothetical w-prefixed ḥash.",
        "source": "lane",
        "variants": [
            "אלוחש", "ואלוחש", "באלוחש",
            "וחוש", "אלוחוש", "ואלוחוש",
            "וחושא",
        ],
    },

    # ---------- Adjective ----------
    {
        "id": "aṣghar-smaller",
        "lemma_ja": "אצג'ר",
        "lemma_ar": "أَصْغَر",
        "root": "ṣ-gh-r",
        "pos": "adjective (comparative / superlative)",
        "gloss_en": "smaller, younger; (with article) the smallest, the youngest",
        "gloss_he": "קטן יותר, צעיר יותר; הקטן, הצעיר",
        "saadia_note": "Saadia's regular gloss for Hebrew הַקָּטֹן in narrative passages (e.g. Esau-Jacob; Joseph and his brothers).",
        "source": "lane",
        "variants": [
            "אלאצג'ר", "ואלאצג'ר",
            "אצג'רכם", "אצג'רהם",
            "אצג'ראן",
        ],
    },

    # ---------- Function words ----------
    {
        "id": "ʿada-except",
        "lemma_ja": "עדא",
        "lemma_ar": "عَدَا",
        "root": "ʿ-d-w",
        "pos": "preposition",
        "gloss_en": "except, besides, apart from, with the exception of",
        "gloss_he": "מלבד, חוץ מ-, להוציא",
        "notes": "Distinct from sawa سِوَى (root s-w-y, also 'besides') — both can render Hebrew זוּלָתִי / מִלְּבַד.",
        "source": "lane",
        "variants": ["ועדא", "פעדא"],
    },
    {
        "id": "kayla-lest",
        "lemma_ja": "כילא",
        "lemma_ar": "كَيْلَا",
        "root": "—",
        "pos": "conjunction",
        "gloss_en": "so that not, lest, in order that not",
        "gloss_he": "פן, לבל, כדי שלא",
        "notes": "Compound particle: purposive kay + negative lā. Saadia's regular gloss for Hebrew פֶּן.",
        "source": "lane",
        "variants": ["וכילא", "פכילא"],
    },
]


VARIANTS_PATCH = {
    "sanaa":          ["תצנעה"],
    "bikr-firstborn": ["בכ'ורא"],
    "akala-eat":      ["תאכלוה"],
    "ʿabd-servant":   ["עבדא"],
}


def main():
    path = pathlib.Path("data/dictionary-lane.json")
    if not path.exists():
        print(f"FATAL: {path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    d = json.loads(path.read_text())

    # --- Pass 1: append NEW_ENTRIES ---
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

    # --- Pass 2: extend variants of existing entries ---
    by_id = {e["id"]: e for e in d["entries"]}
    variant_added = 0
    variant_skipped = []
    for entry_id, new_variants in VARIANTS_PATCH.items():
        if entry_id not in by_id:
            variant_skipped.append((entry_id, "id not found"))
            continue
        target = by_id[entry_id]
        existing_variants = target.setdefault("variants", [])
        for v in new_variants:
            if v in existing_variants:
                variant_skipped.append((entry_id, f"already had {v}"))
                continue
            existing_variants.append(v)
            variant_added += 1

    # --- Write back + validate round-trip ---
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    json.loads(path.read_text())  # round-trip check

    print(f"Added {added} new entries. Skipped: {len(skipped)}")
    for s, reason in skipped:
        print(f"  - {s}: {reason}")
    print(f"Added {variant_added} variants. Skipped: {len(variant_skipped)}")
    for s, reason in variant_skipped:
        print(f"  - {s}: {reason}")
    print(f"Total entries now: {len(d['entries'])}")


if __name__ == "__main__":
    main()

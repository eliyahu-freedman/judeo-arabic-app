#!/usr/bin/env python3
"""Phase 2 Round 7 Batch I — chunk 3 (25 candidates).

Adds 17 new lemmas + 6 lane-variant patches + 1 starter-variant patch.

Homograph: bar (count 8) — already in dict as barr-wilderness (= 'desert');
this chunk adds burr-wheat for the grain-offering sense (Num 29:18:
וברהם 'and their grain-offering').
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Function-word / preposition ----------
    {
        "id": "waraʾ-behind",
        "lemma_ja": "ורא",
        "lemma_ar": "وَرَاء",
        "root": "—",
        "pos": "preposition / adverb",
        "gloss_en": "behind, after; following (after); on the far side of",
        "gloss_he": "אַחֲרֵי, מֵאַחוֹר, מֵעֵבֶר",
        "saadia_note": "Saadia uses warāʾ both spatially ('behind' — Num 3:23 ינזלון ורא אלמסכן 'they encamp behind the tabernacle') and as 'after' a person ('Joseph went after his brothers' Gen 37:17). In the figurative sense it renders Hebrew אַחֲרֵי of straying after one's heart (Num 15:39 טאג'יון וראהם 'wandering after them').",
        "source": "lane",
        "variants": [
            "וורא", "ורי",
            "וראה", "וראהם", "וראהמא", "וראך", "וראכם",
            "וראהא", "וראנא", "וראי",
            "מן ורא", "מן וראה",
        ],
    },

    # ---------- Verbs ----------
    {
        "id": "qattara-burn-incense",
        "lemma_ja": "קתר",
        "lemma_ar": "قَتَّر",
        "root": "q-t-r",
        "pos": "verb (Form II, perfect)",
        "gloss_en": "to burn (as incense or sacrifice — sending smoke/aroma up); to fumigate, send up in smoke",
        "gloss_he": "הִקְטִיר",
        "notes": "Form II (قَتَّر) of q-t-r. Imperative wa-qattir = 'and burn (it) up in smoke'. Cognate with Hebrew הִקְטִיר (hifʿil of q-ṭ-r).",
        "saadia_note": "Saadia's regular gloss for Hebrew הִקְטִיר in priestly contexts — the verb covers both burning of the fat on the altar (Num 18:17: וקתר שחמהא 'and burn its fat in smoke') and burning of incense generally (Exod 29:13). The Hebrew and Arabic share the same triliteral root q-ṭ-r.",
        "source": "lane",
        "variants": [
            "וקתר", "פקתר",
            "יקתר", "ויקתר", "פיקתר", "תקתר",
            "אקתר", "נקתר",
            "יקתרון", "וקתרו", "וקתרוא",
            "יקתרה", "ויקתרה", "ויקתרהא",
            "מקתר", "אלמקתר",
            "אקתאר", "אלאקתאר",
        ],
    },
    {
        "id": "nadaha-sprinkle",
        "lemma_ja": "נצ'ח",
        "lemma_ar": "نَضَح",
        "root": "n-ḍ-ḥ",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to sprinkle, spatter (liquid — water, blood, oil — onto a surface or person)",
        "gloss_he": "הִזָּה, נָטַף, זִלֵּף",
        "saadia_note": "Saadia's regular gloss for Hebrew הִזָּה in purification rites — sprinkling of the red-heifer waters (Num 19), of blood in atonement (Lev 4-5), of oil at consecration (Lev 14:7). The blue-fringes formula 'sprinkle with the water of impurity' and the leper's seven sprinklings both use וינצ'ח.",
        "source": "lane",
        "variants": [
            "ינצ'ח", "וינצ'ח", "פינצ'ח",
            "תנצ'ח", "פתנצ'ח", "ותנצ'ח",
            "אנצ'ח", "ננצ'ח",
            "נצ'חת", "ונצ'חת", "נצ'חוא",
            "נאצ'ח", "אלנאצ'ח", "מנצ'וח",
            "ינצ'ח עליה", "ינצ'ח עלי",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "karm-vineyard",
        "lemma_ja": "כרם",
        "lemma_ar": "كَرْم",
        "root": "k-r-m",
        "pos": "noun (m.)",
        "gloss_en": "vineyard; (broader) plantation, orchard",
        "gloss_he": "כֶּרֶם",
        "saadia_note": "Saadia's regular gloss for Hebrew כֶּרֶם (the Hebrew and Arabic words share the root k-r-m). Appears in property-rights and refusal-of-passage passages (Num 16:14; 20:17).",
        "source": "lane",
        "variants": [
            "אלכרם", "ואלכרם",
            "וכרם", "באלכרם", "ללכרם",
            "כרמך", "כרמכם", "כרמהם", "כרמה", "כרמהא",
            "כרום", "אלכרום", "ואלכרום",
        ],
    },
    {
        "id": "faw-mouth",
        "lemma_ja": "פא",
        "lemma_ar": "فَا",
        "root": "f-w-h",
        "pos": "noun (m.)",
        "gloss_en": "mouth (of a person, animal, or an opening — pit, cave, sack)",
        "gloss_he": "פֶּה",
        "notes": "The classical form is fam (فم); the Quranic / poetic / Saadianic form fā (with construct status changes — fū / fā / fī) is used freely in Judeo-Arabic.",
        "saadia_note": "Saadia's regular gloss for Hebrew פֶּה — both anatomical ('the ground opened its mouth', Num 16:30, 16:32) and metaphorical ('the mouth of the sack', etc.).",
        "source": "lane",
        "variants": [
            "פאה", "פאהא", "פאהם", "פאי", "פאך", "פאכם",
            "אלפא", "ואלפא", "באלפא", "לפא", "ללפא",
            "ופא", "פם", "אלפם", "ופם", "באלפם",
        ],
    },
    {
        "id": "burr-wheat",
        "lemma_ja": "בר",
        "lemma_ar": "بُرّ",
        "root": "b-r-r",
        "pos": "noun (m., collective)",
        "gloss_en": "wheat; (in Saadia's sacrificial vocabulary) the grain offering / minḥah",
        "gloss_he": "חיטה; מנחה (קֶמַח סֹלֶת)",
        "notes": "Homograph with barr-wilderness (lemma בר, root b-r-r, sense 'wilderness'). Context disambiguates: burr always appears in food / offering contexts, barr in geographic ones.",
        "saadia_note": "Saadia's regular gloss for Hebrew מִנְחָה in the offering formulas — וברהם ומזאגהם 'their grain-offering and their drink-offering' (Num 29:18 ff., parallel to סֹלֶת). The wheat sense is also used directly for Hebrew דָּגָן / קָמַח in non-cultic passages.",
        "source": "lane",
        "variants": [
            "ברהם", "וברהם", "ברה", "וברה", "ברהא", "וברהא",
            "ברך", "וברך", "ברכם", "וברכם",
            "ברנא", "וברנא",
            "ובר", "באלבר", "באלבר",
        ],
    },
    {
        "id": "ʿayb-defect",
        "lemma_ja": "עיב",
        "lemma_ar": "عَيْب",
        "root": "ʿ-y-b",
        "pos": "noun (m.)",
        "gloss_en": "defect, blemish, fault, imperfection",
        "gloss_he": "מוּם, פְּגָם",
        "saadia_note": "Saadia's regular gloss for Hebrew מוּם — the technical term for the sacrificial-animal blemishes that disqualify an offering (Num 19:2; Deut 15:21; Lev 22; Lev 21 for priests).",
        "source": "lane",
        "variants": [
            "אלעיב", "ואלעיב", "ועיב",
            "באלעיב", "בעיב",
            "עיוב", "אלעיוב", "ואלעיוב",
            "מעיוב", "אלמעיוב", "מעיוב",
            "ולא עיב", "מא ליס פיהא עיב", "פיה עיב",
        ],
    },
    {
        "id": "nabiʿ-spring",
        "lemma_ja": "נביע",
        "lemma_ar": "نَبِيع",
        "root": "n-b-ʿ",
        "pos": "noun (m., verbal-noun / active sense)",
        "gloss_en": "running, flowing (of water — a spring, a fresh source); the act of welling up",
        "gloss_he": "מַעְיָן, מַיִם חַיִּים (זרימה)",
        "saadia_note": "Saadia's regular gloss for Hebrew מַיִם חַיִּים ('running / living water') in purification passages (Num 19:17: מא נביע פי אנא 'running water in a vessel'; Lev 14; Lev 15). The phrase מן נביע דמהא 'from the flow of her blood' renders Heb מִמְּקוֹר דָּמֶיהָ (Lev 12:7).",
        "source": "lane",
        "variants": [
            "אלנביע", "ואלנביע",
            "נביעא", "באלנביע", "ונביע",
            "מא נביע", "מא נביעא",
            "מן נביע",
        ],
    },
    {
        "id": "shamal-north",
        "lemma_ja": "שמאל",
        "lemma_ar": "شَمَال",
        "root": "sh-m-l",
        "pos": "noun (m.) / adverb",
        "gloss_en": "north; the northern direction; (sometimes) left hand",
        "gloss_he": "צָפוֹן",
        "saadia_note": "Saadia's regular gloss for Hebrew צָפוֹן in directional descriptions — especially the layout of the tribes (Num 2:25 פי אלשמאל 'in the north') and the Levitical encampment (Num 3:35).",
        "source": "lane",
        "variants": [
            "אלשמאל", "ואלשמאל",
            "פי אלשמאל", "אלי' אלשמאל", "מן אלשמאל",
            "באלשמאל", "ושמאל",
            "שמאלא",
        ],
    },
    {
        "id": "mubarak-blessed",
        "lemma_ja": "מבארך",
        "lemma_ar": "مُبَارَك",
        "root": "b-r-k",
        "pos": "passive participle (m.)",
        "gloss_en": "blessed, fortunate, made-blessed",
        "gloss_he": "מְבֹרָךְ, בָּרוּךְ",
        "notes": "Form III passive participle of b-r-k. Active form mubārik = 'one who blesses'; passive mubārak = 'the one blessed'.",
        "saadia_note": "Saadia's regular gloss for Hebrew בָּרוּךְ as a stative ascription — most famously the Balaam-pericope formula מן תבארכה מבארך 'whom you bless is blessed' (Num 22:6, 22:12).",
        "source": "lane",
        "variants": [
            "ומבארך", "פמבארך",
            "אלמבארך", "ואלמבארך",
            "מבארכה", "אלמבארכה", "ומבארכה",
            "מבארכין", "אלמבארכין",
            "מבארכא",
        ],
    },
    {
        "id": "ʿagalah-wagon",
        "lemma_ja": "עגלה",
        "lemma_ar": "عَجَلَة",
        "root": "ʿ-j-l",
        "pos": "noun (f.)",
        "gloss_en": "wagon, cart (wheeled vehicle for carrying loads); (broader) any wheeled conveyance",
        "gloss_he": "עֲגָלָה",
        "notes": "Cognate with Hebrew עֲגָלָה — both languages use the same root ʿ-j-l ('haste / round, rolling'). Distinct from ʿijl 'calf' (also ʿ-j-l).",
        "saadia_note": "Saadia's regular gloss for Hebrew עֲגָלָה — the carts donated by the tribal chiefs at the Tabernacle dedication (Num 7:3-8: אלעגל ואלבקר 'the carts and the cattle') and the wagons Joseph sent to fetch Jacob (Gen 45:19, 27; 46:5).",
        "source": "lane",
        "variants": [
            "אלעגלה", "ואלעגלה", "ועגלה",
            "אלעגל", "ואלעגל", "עגל",     # collective / plural surface
            "עגלאת", "אלעגלאת", "ואלעגלאת",
            "באלעגלה", "באלעגל",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "abiram-name",
        "lemma_ja": "אבירם",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Abiram — son of Eliab (Reubenite), co-conspirator with Korah and Dathan in the rebellion against Moses (Num 16; 26:9; Deut 11:6)",
        "gloss_he": "אֲבִירָם בֶּן אֱלִיאָב",
        "saadia_note": "Saadia retains the Hebrew name unchanged. Almost always appears in the pair דתן ואבירם.",
        "source": "lane",
        "variants": [
            "ואבירם", "לאבירם", "באבירם",
            "דתן ואבירם", "ודתן ואבירם",
        ],
    },
    {
        "id": "peor-place",
        "lemma_ja": "פעור",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Peor — (1) the Moabite deity Baal-Peor; (2) the mountain/place of his worship in the plains of Moab (Num 23:28; 25:3, 5, 18; 31:16; Deut 4:3)",
        "gloss_he": "פְּעוֹר — בעל פעור והמקום הקרוי על שמו",
        "saadia_note": "Saadia retains the Hebrew name. Often follows ל or פעור אלצנם ('Peor the idol').",
        "source": "lane",
        "variants": [
            "ופעור", "לפעור", "בפעור",
            "פעור אלצנם", "באל פעור",
        ],
    },
    {
        "id": "hivite-people",
        "lemma_ja": "חויין",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun (gentilic plural)",
        "gloss_en": "Hivites — one of the seven Canaanite peoples; descendants of Hivvi son of Canaan (Gen 10:17)",
        "gloss_he": "הַחִוִּי, הַחִוִּים",
        "notes": "Always plural-gentilic in Saadia (the -iyyīn ending). Frequently appears in the seven-nation list (Exod 13:5; Deut 7:1; Deut 20:17; Gen 10:17).",
        "source": "lane",
        "variants": [
            "אלחויין", "ואלחויין",
            "חוי", "אלחוי", "ואלחוי",
        ],
    },
    {
        "id": "gomorrah-place",
        "lemma_ja": "עמורה",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Gomorrah — the Cities-of-the-Plain that YHWH destroyed alongside Sodom (Gen 10:19; 13:10; 14:2, 8, 10-11; 18:20; 19:24, 28; Deut 29:23; 32:32)",
        "gloss_he": "עֲמוֹרָה",
        "saadia_note": "Saadia retains the Hebrew name unchanged. Always paired with סדום (Sodom).",
        "source": "lane",
        "variants": [
            "ועמורה", "לעמורה", "בעמורה",
            "סדום ועמורה",
        ],
    },
    {
        "id": "nahor-name",
        "lemma_ja": "נחור",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Nahor — (1) Abraham's grandfather (Gen 11:22-25); (2) Abraham's brother, husband of Milcah (Gen 11:26-29; 22:20-23; 24:10, 15, 24, 47)",
        "gloss_he": "נָחוֹר",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ונחור", "לנחור", "בנחור", "אבן נחור",
        ],
    },
    {
        "id": "farkh-young-bird",
        "lemma_ja": "פרך'",
        "lemma_ar": "فَرْخ",
        "root": "f-r-kh",
        "pos": "noun (m.)",
        "gloss_en": "young of a bird, fledgling, chick; pl. firākh = 'young pigeons'",
        "gloss_he": "אֶפְרֹחַ, גוֹזָל",
        "saadia_note": "Saadia's regular gloss for Hebrew בֶּן (in the offering formula 'a young pigeon' בֶּן יוֹנָה → פרך' חמאם, Num 6:10; Lev 12:8; Gen 15:9). Always paired with חמאם 'pigeons'.",
        "source": "lane",
        "variants": [
            "פרך",   # apos-stripped bare form
            "אלפרך'", "ואלפרך'",
            "פרכ'י", "פרכ'ין", "אלפרכ'י", "ופרכ'י",
            "פרך' חמאם", "פרכ'י חמאם",
            "פרוך'", "אלפרוך'",
        ],
    },
]


VARIANTS_PATCH = {
    # Lane-side patches
    "jabal":             ["אלגבל", "ואלגבל", "באלגבל", "גבאל", "אלגבאל", "ואלגבאל", "באלגבאל", "גבל"],
    "amam":              ["אמאמה", "ואמאמה", "אמאמהא", "אמאמהם", "אמאמך", "אמאמכם", "ואמאמך"],
    "ihsa-count":        ["באחצאיהם", "באחצאיהן", "באחצאיכם", "אחצאיהם", "באחצא"],
    "jaza-pass-permit":  ["גאיזין", "אלגאיזין", "ואלגאיזין", "וגאיזין"],
    "duhn-oil":          ["דהנא", "ודהנא"],
    "idha":              ["פאד'י", "אד'י", "ואד'י", "פאד'יא"],
}

STARTER_VARIANTS_PATCH = {
    "kadhalik":          ["כדאך", "וכדאך", "פכדאך"],
}


def main():
    lane_path = pathlib.Path("data/dictionary-lane.json")
    starter_path = pathlib.Path("data/dictionary-starter.json")
    if not lane_path.exists() or not starter_path.exists():
        print("FATAL: dict files not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    d = json.loads(lane_path.read_text())
    ds = json.loads(starter_path.read_text())

    # --- Pass 1: append NEW_ENTRIES (lane) ---
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

    # --- Pass 2: extend lane variants ---
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

    # --- Pass 3: extend starter variants ---
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

    # --- Write back + validate ---
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

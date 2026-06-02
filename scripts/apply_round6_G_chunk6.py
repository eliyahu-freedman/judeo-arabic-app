#!/usr/bin/env python3
"""Phase 2 Round 6 Batch G chunk 6 — long-tail sweep (no API). Final chunk.

17 new lane entries + 6 lane variant patches. Skipped: רת (no context), פרג
(no context, ambiguous). The naqis-defective entry has the wrong id (its
content is actually najis 'unclean', not naqiṣ 'defective') — flag for the
audit pass.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Verbs ----------
    {
        "id": "kashafa-uncover",
        "lemma_ja": "כשף",
        "lemma_ar": "كَشَفَ",
        "root": "k-sh-f",
        "pos": "verb",
        "gloss_en": "to uncover, to reveal, to disclose; to expose what was concealed",
        "gloss_he": "גילה, חשף, גלה",
        "saadia_note": "Saadia uses kashafa as the regular gloss for Hebrew גִּלָּה in 'uncovering nakedness' (ʿerwa) prohibitions (Lev 18; Exod 20:23).",
        "source": "lane",
        "variants": [
            "תכשף", "ויכשף", "אכשף", "נכשף",
            "תכשפן", "תכשפו", "תכשפוא",
            "וכשף", "פכשף", "כשפת",
            "כשפהא", "כשפה", "כשפהמא",
        ],
    },
    {
        "id": "waʿada-promise",
        "lemma_ja": "ועד",
        "lemma_ar": "وَعَدَ",
        "root": "w-ʿ-d",
        "pos": "verb",
        "gloss_en": "to promise, to make a pledge, to give one's word",
        "gloss_he": "הבטיח, הבטיח-ל, נדר",
        "saadia_note": "Saadia uses waʿada as the regular gloss for Hebrew דִּבֶּר / נִשְׁבַּע in the patriarchal-promise formula ('as the LORD has promised', Deut 1:21; 12:20).",
        "source": "lane",
        "variants": [
            "ועדך", "ועדה", "ועדהם", "ועדכם", "ועדנא", "ועדני",
            "יעד", "ויעד", "פיעד", "תעד", "אעד",
            "מועוד", "אלמועוד", "ואלמועוד", "ועד",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "salam-peace",
        "lemma_ja": "סלאם",
        "lemma_ar": "سَلَام",
        "root": "s-l-m",
        "pos": "noun (m.)",
        "gloss_en": "peace, well-being, safety; (in farewell) 'in peace'",
        "gloss_he": "שלום",
        "saadia_note": "In the farewell 'bi-salām' Saadia renders Hebrew בְּשָׁלוֹם (Gen 15:15; Gen 26:29 'we sent you away in peace').",
        "source": "lane",
        "variants": [
            "אלסלאם", "ואלסלאם", "באלסלאם", "בסלאם",
            "סלאמה", "סלאמתה", "סלאמתך", "סלאמתכם", "סלאמתהם",
        ],
    },
    {
        "id": "Hayy-living",
        "lemma_ja": "חי",
        "lemma_ar": "حَيّ",
        "root": "ḥ-y-y",
        "pos": "adjective / noun (m.)",
        "gloss_en": "living, alive; (with article) the Living One — an attribute of God",
        "gloss_he": "חי",
        "saadia_note": "Saadia uses al-ḥayy as the regular gloss for Hebrew חַי in 'God the Living' (e.g. Deut 5:23 'the voice of the living God'; Gen 16:14 'the Well of the Living One who sees').",
        "source": "lane",
        "variants": ["אלחי", "ואלחי", "באלחי", "אחיא", "אלאחיא", "ואלאחיא"],
    },
    {
        "id": "jawhar-stone",
        "lemma_ja": "גוהר",
        "lemma_ar": "جَوْهَر",
        "root": "—",
        "pos": "noun (m.)",
        "gloss_en": "essence, gem, precious stone (especially 'noble' stone); (Saadia) the dressed stone of the Decalogue tablets",
        "gloss_he": "אבן יקרה, גוהר; (אצל סעדיה) אבן הלוחות",
        "saadia_note": "Saadia uses lawḥay jawhar as the regular gloss for Hebrew לוּחֹת הָאֲבָנִים (the stone tablets of the Decalogue, Deut 5:19; 9:9).",
        "source": "lane",
        "variants": ["אלגוהר", "ואלגוהר", "באלגוהר", "וגוהר", "גואהר", "אלגואהר"],
    },
    {
        "id": "maida-table",
        "lemma_ja": "מאידה",
        "lemma_ar": "مَائِدَة",
        "root": "—",
        "pos": "noun (f.)",
        "gloss_en": "table, banquet-table (especially one set with food)",
        "gloss_he": "שולחן (ערוך באוכל)",
        "saadia_note": "Saadia uses al-mā'ida as the regular gloss for Hebrew הַשֻּׁלְחָן — the Tabernacle Table of Showbread (Exod 25:23ff).",
        "source": "lane",
        "variants": [
            "אלמאידה", "ואלמאידה", "באלמאידה", "לאלמאידה",
            "מואיד", "אלמואיד",
        ],
    },
    {
        "id": "kabid-liver",
        "lemma_ja": "כבד",
        "lemma_ar": "كَبِد",
        "root": "k-b-d",
        "pos": "noun (m./f.)",
        "gloss_en": "liver (the organ)",
        "gloss_he": "כבד (האיבר)",
        "saadia_note": "In 'zā'idat al-kabid' Saadia renders Hebrew יוֹתֶרֶת הַכָּבֵד ('the appendage / lobe of the liver', Exod 29:13, 22; Lev 3:4).",
        "source": "lane",
        "variants": ["אלכבד", "ואלכבד", "באלכבד", "כבדה", "אכבאד", "אלאכבאד"],
    },
    {
        "id": "kulwa-kidney",
        "lemma_ja": "כלוה",
        "lemma_ar": "كُلْوَة",
        "root": "k-l-w/y",
        "pos": "noun (f.)",
        "gloss_en": "kidney (the organ; dual: the two kidneys)",
        "gloss_he": "כליה",
        "saadia_note": "Saadia uses al-kulwatayn (dual) as the regular gloss for Hebrew הַכְּלָיֹת (the two kidneys of the sacrificial animal, Exod 29:13; Lev 3:4).",
        "source": "lane",
        "variants": [
            "אלכלוה", "ואלכלוה", "באלכלוה",
            "כלותין", "אלכלותין", "ואלכלותין", "באלכלותין",
            "כליאת", "אלכליאת",
        ],
    },
    {
        "id": "difdaʿ-frog",
        "lemma_ja": "צ'פדע",
        "lemma_ar": "ضِفْدَع",
        "root": "ḍ-f-d-ʿ",
        "pos": "noun (m.)",
        "gloss_en": "a frog",
        "gloss_he": "צפרדע",
        "saadia_note": "Saadia uses al-ḍafādiʿ (broken pl.) as the regular gloss for Hebrew הַצְּפַרְדְּעִים (the Exodus plague of frogs, Exod 7-8).",
        "source": "lane",
        "variants": [
            "אלצ'פדע", "ואלצ'פדע", "באלצ'פדע",
            "צ'פאדע", "אלצ'פאדע", "ואלצ'פאדע", "באלצ'פאדע",
        ],
    },
    {
        "id": "mutaTahhir-purifying",
        "lemma_ja": "מתטהר",
        "lemma_ar": "مُتَطَهِّر",
        "root": "ṭ-h-r",
        "pos": "active participle (m., Form V)",
        "gloss_en": "one who is purifying himself, one undergoing purification rites",
        "gloss_he": "מיטהר, המיטהר",
        "saadia_note": "Saadia uses al-mutaṭahhir as the regular gloss for Hebrew הַמִּטַּהֵר (the leper undergoing post-quarantine purification, Lev 14:7-8).",
        "source": "lane",
        "variants": [
            "אלמתטהר", "ואלמתטהר", "באלמתטהר", "לאלמתטהר",
            "מתטהרין", "אלמתטהרין",
        ],
    },
    {
        "id": "sawʾa-nakedness",
        "lemma_ja": "סות",
        "lemma_ar": "سَوْأَة",
        "root": "s-w-'",
        "pos": "noun (f.)",
        "gloss_en": "shameful part, private parts, nakedness; (idiomatic) shame, disgrace",
        "gloss_he": "ערווה, מבושים",
        "saadia_note": "Saadia uses sawʾa as the regular gloss for Hebrew עֶרְוָה (nakedness, especially in the Lev 18 prohibitions and Exod 20:23 altar-steps).",
        "source": "lane",
        "variants": [
            "אלסות", "ואלסות", "באלסות",
            "סותך", "סותה", "סותהא", "סותהם", "סותכם",
            "וסות", "וסוות", "סוות",
            "סואת", "אלסואת",
        ],
    },
    {
        "id": "ʿadad-number",
        "lemma_ja": "עדד",
        "lemma_ar": "عَدَد",
        "root": "ʿ-d-d",
        "pos": "noun (m.)",
        "gloss_en": "number, count, total, census-figure",
        "gloss_he": "מספר, מנין, פקודים",
        "saadia_note": "Saadia uses ʿadad as the regular gloss for Hebrew הַפְּקֻדִים / מִסְפַּר in census formulas (Num 1; Num 26).",
        "source": "lane",
        "variants": [
            "אלעדד", "ואלעדד", "באלעדד", "עדדה",
            "עדדהם", "עדדכם", "עדדהא", "עדדנא",
            "עדה", "אלעדה", "ואלעדה",
        ],
    },
    {
        "id": "janub-south",
        "lemma_ja": "גנוב",
        "lemma_ar": "جَنُوب",
        "root": "j-n-b",
        "pos": "noun (m.) / adverb",
        "gloss_en": "the south, the southern direction; (in compass formulas) southward",
        "gloss_he": "דרום, נגב",
        "saadia_note": "Saadia uses al-janūb as the regular gloss for Hebrew נֶגֶב / דָּרוֹם (the southward direction, Num 2:10; 10:6).",
        "source": "lane",
        "variants": ["אלגנוב", "ואלגנוב", "באלגנוב", "מהב אלגנוב", "גנובא"],
    },
    {
        "id": "merari-name",
        "lemma_ja": "מררי",
        "lemma_ar": "مَرَارِي",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Merari — third son of Levi; ancestor of the Merarite Levitical clan",
        "gloss_he": "מררי",
        "source": "lane",
        "variants": ["ומררי", "למררי", "במררי", "אלמררי", "אלמרריין", "מרריין"],
    },
    {
        "id": "Hamu-father-in-law",
        "lemma_ja": "חמו",
        "lemma_ar": "حَمُو",
        "root": "ḥ-m-w",
        "pos": "noun (m.)",
        "gloss_en": "father-in-law (the father of one's wife)",
        "gloss_he": "חם, אבי האישה",
        "saadia_note": "Saadia uses ḥamū as the regular gloss for Hebrew חוֹתֵן (especially Jethro, Moses' father-in-law, Exod 18:7; Num 10:29).",
        "source": "lane",
        "variants": ["חמוה", "אלחמו", "ואלחמו", "באלחמו", "חמואיה", "חמוהם"],
    },
    {
        "id": "ghulam-boy",
        "lemma_ja": "ג'לאם",
        "lemma_ar": "غُلَام",
        "root": "gh-l-m",
        "pos": "noun (m.)",
        "gloss_en": "boy, youth, young manservant, lad",
        "gloss_he": "נער, צעיר, משרת",
        "saadia_note": "Saadia uses ghulām as the regular gloss for Hebrew נַעַר (especially the 'servant-lad' Hobab/Joshua and Abraham's servant-lad of Gen 18:7).",
        "source": "lane",
        "variants": [
            "אלג'לאם", "ואלג'לאם", "באלג'לאם", "לאלג'לאם",
            "ג'למאן", "אלג'למאן", "ואלג'למאן",
            "ג'לאמהם", "ג'לאמך",
        ],
    },

    # ---------- Compound entry: ʿidda/ʿAdah homograph ----------
    {
        "id": "ʿAdah-name",
        "lemma_ja": "עדה",
        "lemma_ar": "عَدَة",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Adah — (1) Lamech's first wife (Gen 4:19ff); (2) Esau's Hittite wife (Gen 36:2)",
        "gloss_he": "עדה",
        "notes": "Homograph with the noun ʿidda 'count, number' (see ʿadad-number entry). Context disambiguates.",
        "source": "lane",
        "variants": ["ועדה", "לעדה", "בעדה"],
    },
]


VARIANTS_PATCH = {
    "ʿaqd-covenant":      ["עהדא", "ועהדא", "ועהד"],
    "wajada-find":        ["יוגד", "ויוגד", "פיוגד", "ליוגד"],
    "kana":               ["יכונו", "ויכונו", "פיכונו", "יכונוא", "ויכון"],
    "naqis-defective":    ["פלינגסה", "ליגנס", "ינגסה", "נגסוה", "נגסוהא"],
    "sanaa":              ["תצנעהא", "תצנעוה", "תצנעון"],
    "ʿabd-servant":       ["עבידא", "ועבידא"],
}


def main():
    lane_path = pathlib.Path("data/dictionary-lane.json")
    if not lane_path.exists():
        print(f"FATAL: {lane_path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    d = json.loads(lane_path.read_text())

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

    lane_path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    json.loads(lane_path.read_text())

    print(f"Added {added} new entries. Skipped: {len(skipped)}")
    for s, reason in skipped:
        print(f"  - {s}: {reason}")
    print(f"Added {variant_added} variants. Skipped: {len(variant_skipped)}")
    for s, reason in variant_skipped:
        print(f"  - {s}: {reason}")
    print(f"Total entries now: {len(d['entries'])}")


if __name__ == "__main__":
    main()

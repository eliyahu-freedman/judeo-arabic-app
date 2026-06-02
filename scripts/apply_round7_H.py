#!/usr/bin/env python3
"""Phase 2 Round 7 Batch H — head-of-queue hand cleanup (~22 entries).

Targets the top-25 misses after Round 6 (count 9-14). Adds:

  • 22 new lemma entries (function words, nouns, verbs, proper nouns)
  • 3 variant patches on existing entries:
      laysa            ← אליס      (ʔa-laysa, "is it not?", interrogative)
      mardy-pleasing   ← מרצ'ייא   (marḍiyyan, accusative indef)
      rahala-depart    ← ירחלון    (yarḥalūna, 3mp impf)

Two notable cases:

  • רת'  (count 14 in misses, "no context") and פרג' (count 10) are NOT
    tokenizer artifacts in the usual sense — both are real lemmas whose
    standard form ends in an apostrophe. The tokenizer's stripPunct strips
    trailing ' before lookup, and the report indexed them under their bare
    forms (רת / פרג). Adding the apostrophed lemma plus normalizeFinals
    handles both surface variants.

  • כ'לה is Blau's Saadianic noun خلة "action, case, matter" (Blau §1085).
    Saadia uses it for Hebrew זאת in legal/exhortative formulas
    (Num 16:6: "do this thing"; Gen 42:18: "do this and live").

  • כלב in all 9 attested contexts is Caleb (proper noun), not kalb=dog.
    Entered as caleb-name with a note documenting the homograph.
"""
import json, sys, pathlib

NEW_ENTRIES = [
    # ---------- Bovine / sacrificial vocab ----------
    {
        "id": "ratt-young-bull",
        "lemma_ja": "רת'",
        "lemma_ar": "رتّ",
        "root": "—",
        "pos": "noun (m.)",
        "gloss_en": "young bull, bullock, steer",
        "gloss_he": "פר, עגל זכר צעיר",
        "notes": "Plural ratt-ūt (Blau §1367 notes the form ratt + plural rutūt likely reflects a mistaken pointing tradition; the underlying Arabic etymology is unsettled).",
        "saadia_note": "Saadia's regular gloss for Hebrew פַר (par, 'young bull') in sacrificial passages — distinct from ת'ור (thawr), which translates שׁוֹר ('ox'). Plural רת'ות' / רתות' renders פָּרִים.",
        "source": "lane",
        "variants": [
            "רת",            # bare form (apostrophe-stripped surface)
            "רת'א", "רתא",   # accusative indef "a bull" (Num 15:24)
            "אלרת'", "אלרת",
            "ורת'", "ורת",
            "ברת'", "ברת",
            "רת'ות'", "רתות'", "רתות",
            "אלרת'ות'", "ואלרתות'", "ואלרתות",
            "רת'ין", "רתין",
        ],
    },

    # ---------- Verbs ----------
    {
        "id": "faragha-finish",
        "lemma_ja": "פרג'",
        "lemma_ar": "فَرَغ",
        "root": "f-r-gh",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to finish, complete, conclude (an activity); to be done with",
        "gloss_he": "סיים, גמר, השלים",
        "notes": "Often construed with min ('from') + verbal noun: faragha min al-kalām = 'he finished speaking'.",
        "saadia_note": "Saadia's regular gloss for the participial-temporal Hebrew construction 'when X had finished doing Y' (כְּכַלֹּתוֹ / וַיְכַל) — e.g. ולמא פרג' מוסי' מן נצב אלמסכן (Num 7:1) = 'when Moses had finished setting up the tabernacle.'",
        "source": "lane",
        "variants": [
            "פרג",           # apostrophe-stripped bare form
            "ופרג'", "ופרג",
            "פלמא פרג'", "ולמא פרג'",
            "פרג'ת", "פרגת",
            "פרג'ו", "פרגו",
            "יפרג'", "יפרג",
            "אפרג'", "תפרג'",
            "פרוג", "אלפרוג",
            "מפרוג'", "אלמפרוג'",
        ],
    },
    {
        "id": "ghafara-forgive",
        "lemma_ja": "ג'פר",
        "lemma_ar": "غَفَر",
        "root": "gh-f-r",
        "pos": "verb (Form I, perfect)",
        "gloss_en": "to forgive, pardon, cover over (a fault, sin)",
        "gloss_he": "סלח, מחל, כיפר",
        "notes": "Distinct from the Form-X istaghfara (יסתג'פר 'to seek forgiveness') which is already in the dictionary.",
        "saadia_note": "Saadia's regular gloss for Hebrew סָלַח (e.g. Num 15:28 ויג'פר לה = וְסָלַח לוֹ; Deut 32:43 ויג'פר לבלאדה).",
        "source": "lane",
        "variants": [
            "יג'פר", "ויג'פר",
            "אג'פר", "פאג'פר",
            "תג'פר", "ויג'פרה", "ויג'פרהא",
            "ויג'פר לה", "ויג'פר להם",
            "ג'פרת", "ג'פרתה", "ג'פרנא",
            "מג'פור", "אלמג'פור",
            "ג'פראן", "אלג'פראן",
        ],
    },
    {
        "id": "taqaddama-advance",
        "lemma_ja": "תקדם",
        "lemma_ar": "تَقَدَّم",
        "root": "q-d-m",
        "pos": "verb (Form V, perfect)",
        "gloss_en": "to step forward, advance, come forward, present oneself; to take precedence",
        "gloss_he": "התקדם, ניגש, יצא קדימה",
        "notes": "Form V (تَفَعَّل) of q-d-m. Often used narratively: 'so-and-so came forward (and said/did X).'",
        "saadia_note": "Saadia uses tafriʿ-form taqaddama for Hebrew narrative 'rose up / stood up / came forward' constructions, especially in the Korah pericope (Num 16:1 פתקדם קרח) and in Moses-and-Aaron advancing toward the tent (Num 17:8).",
        "source": "lane",
        "variants": [
            "פתקדם", "ותקדם",
            "פתקדמת", "ותקדמת",
            "פתקדמו", "ותקדמו",
            "יתקדם", "פיתקדם", "ויתקדם",
            "תתקדם", "פתתקדם",
            "אתקדם", "נתקדם",
        ],
    },
    {
        "id": "khalla-let",
        "lemma_ja": "כ'לי",
        "lemma_ar": "خَلَّى",
        "root": "kh-l-w",
        "pos": "verb (Form II, perfect)",
        "gloss_en": "to leave (alone); to let go; to release, dismiss",
        "gloss_he": "הניח, עזב, שילח",
        "notes": "Form II (خَلَّى) of kh-l-w. With 3ms object suffix: khallāhu = 'he left him' / 'he let him alone'.",
        "source": "lane",
        "variants": [
            "כ'לה",          # 3ms pf + 3ms suff: khallāhu
            "כ'לאה", "כ'להא",
            "וכ'לה", "פכ'לה",
            "כ'לית", "כ'ליה",
            "יכ'לי", "ויכ'לי", "תכ'לי",
            "כ'לוא", "וכ'לוא", "פכ'לוא",
        ],
    },
    {
        "id": "satara-cover",
        "lemma_ja": "סתר",
        "lemma_ar": "سَتَر",
        "root": "s-t-r",
        "pos": "verb (Form I, perfect) / noun",
        "gloss_en": "to cover, veil, conceal; (as noun) covering, screen, curtain",
        "gloss_he": "כיסה, הסתיר; כיסוי, מסך, פרוכת",
        "notes": "Both verbal and nominal uses attested. Nominal sitr / satr = 'screen, curtain' — Saadia uses it for the מָסָךְ of the Tabernacle entrance (Num 3:25-26: וסתר באב כ'בא אלמחצ'ר 'and the screen of the door of the Tent of Meeting').",
        "source": "lane",
        "variants": [
            "וסתר",
            "אלסתר", "ואלסתר", "באלסתר",
            "יסתר", "ויסתר", "תסתר",
            "אסתר", "נסתר",
            "סתרת", "סתרהא", "סתרה",
            "מסתור", "מסתורה",
        ],
    },

    # ---------- Nouns ----------
    {
        "id": "asal-honey",
        "lemma_ja": "עסל",
        "lemma_ar": "عَسَل",
        "root": "ʿ-s-l",
        "pos": "noun (m.)",
        "gloss_en": "honey",
        "gloss_he": "דבש",
        "saadia_note": "Saadia's regular gloss for Hebrew דְּבַשׁ — appears in the recurring formula 'a land flowing with milk and honey' (אַרֶץ זָבַת חָלָב וּדְבָשׁ → בלד יפיץ' אללבן ואלעסל).",
        "source": "lane",
        "variants": [
            "אלעסל", "ואלעסל",
            "ועסל", "בעסל", "באלעסל",
            "לעסל", "לאלעסל",
            "עסלא",
        ],
    },
    {
        "id": "dann-flock",
        "lemma_ja": "צ'אן",
        "lemma_ar": "ضَأْن",
        "root": "ḍ-ʾ-n",
        "pos": "noun (collective, m.)",
        "gloss_en": "sheep, flock of sheep (as opposed to goats — ma'z)",
        "gloss_he": "צאן, כבשים",
        "notes": "Often paired with ma'z (goats) in offering passages — Saadia uses the two together to render Hebrew כבשים-ועזים collocations.",
        "saadia_note": "Saadia's gloss for Hebrew כֶּבֶשׂ / כְּבָשִׂים in many sacrificial passages, distinct from kabsh (כבש, individual ram) and ghanam (ג'נם, generic 'flock').",
        "source": "lane",
        "variants": [
            "אלצ'אן", "ואלצ'אן",
            "בצ'אן", "באלצ'אן",
            "וצ'אן", "לצ'אן", "לאלצ'אן",
        ],
    },
    {
        "id": "sahw-inadvert",
        "lemma_ja": "סהו",
        "lemma_ar": "سَهْو",
        "root": "s-h-w",
        "pos": "noun / adverb (m.)",
        "gloss_en": "inadvertence, oversight, unintentional act; (adv. accusative sahwan) inadvertently, by mistake",
        "gloss_he": "שגגה, היסח הדעת; בשוגג",
        "saadia_note": "Saadia's regular gloss for Hebrew שְׁגָגָה (inadvertent sin) in Lev 4 and Num 15:22-28 — especially the adverbial accusative סהוא = 'inadvertently' rendering Heb בִּשְׁגָגָה. The active participle אלסאהי ('the inadvertent one') glosses Heb הַשֹּׁגֵג.",
        "source": "lane",
        "variants": [
            "סהוא",          # accusative adverbial: sahwan
            "אלסהו", "ואלסהו", "בסהו", "באלסהו",
            "וסהו",
            "סאהי", "אלסאהי", "ואלסאהי",
            "סאהיא",
        ],
    },
    {
        "id": "waba-plague",
        "lemma_ja": "ובא",
        "lemma_ar": "وَبَاء",
        "root": "w-b-ʾ",
        "pos": "noun (m.)",
        "gloss_en": "plague, pestilence, epidemic",
        "gloss_he": "מגפה, דֶּבֶר",
        "saadia_note": "Saadia's regular gloss for Hebrew מַגֵּפָה (plague) — most prominently the plague that broke out after Baal Peor (Num 17:13-14: ואנחבס אלובא 'and the plague was stopped') and the plague at the spies' return (Num 14).",
        "source": "lane",
        "variants": [
            "אלובא", "ואלובא",
            "באלובא", "וובא",
            "לאלובא",
        ],
    },
    {
        "id": "isbaʿ-finger",
        "lemma_ja": "אצבע",
        "lemma_ar": "إِصْبَع",
        "root": "ṣ-b-ʿ",
        "pos": "noun (f.)",
        "gloss_en": "finger",
        "gloss_he": "אצבע",
        "saadia_note": "Saadia's gloss for Hebrew אֶצְבַּע. Most frequently appears in the ritual formula 'and he shall dip his finger in the blood' — באצבעה ('with his finger', Num 19:4; Lev 14:16).",
        "source": "lane",
        "variants": [
            "אצבעה", "באצבעה",
            "אצבעי", "באצבעי",
            "אלאצבע", "ואלאצבע",
            "ואצבע", "אצאבע", "אלאצאבע",
            "אצבעך", "באצבעך",
        ],
    },
    {
        "id": "mayyit-dead",
        "lemma_ja": "מיית",
        "lemma_ar": "مَيِّت",
        "root": "m-w-t",
        "pos": "noun / adjective (m.)",
        "gloss_en": "dead (person); a corpse, deceased",
        "gloss_he": "מת, פגר, גופת מת",
        "saadia_note": "Saadia's regular gloss for Hebrew מֵת as a noun (the dead person, the corpse). Distinct from the verbal sense, which Saadia renders with the verb māta (מאת).",
        "source": "lane",
        "variants": [
            "אלמיית", "ואלמיית",
            "במיית", "באלמיית",
            "מייתא",
            "מייתין", "אלמייתין", "ואלמייתין",
            "מותא", "אלמותא", "ואלמותא",   # broken plural: mawtā "the dead"
        ],
    },
    {
        "id": "sayf-sword",
        "lemma_ja": "סיף",
        "lemma_ar": "سَيْف",
        "root": "s-y-f",
        "pos": "noun (m.)",
        "gloss_en": "sword",
        "gloss_he": "חרב",
        "saadia_note": "Saadia's regular gloss for Hebrew חֶרֶב. The phrase בחד אלסיף ('with the edge of the sword') renders Heb לְפִי-חֶרֶב in conquest narratives (e.g. Num 21:24; Gen 34:26).",
        "source": "lane",
        "variants": [
            "אלסיף", "ואלסיף",
            "באלסיף", "בסיף",
            "וסיף", "לסיף", "לאלסיף",
            "סיוף", "אלסיוף", "באלסיוף",
        ],
    },
    {
        "id": "khusuma-quarrel",
        "lemma_ja": "כ'צומה",
        "lemma_ar": "خُصُومَة",
        "root": "kh-ṣ-m",
        "pos": "noun (f., verbal-noun)",
        "gloss_en": "quarrel, dispute, contention; legal contestation",
        "gloss_he": "מריבה, סכסוך, ריב",
        "saadia_note": "Saadia's regular gloss for Hebrew רִיב in disputes between persons or households (e.g. Gen 13:7-8: וכאנת כ'צומה בין רעא מאשיה' אברם 'and there was a quarrel between the herdsmen of Abram's livestock').",
        "source": "lane",
        "variants": [
            "אלכ'צומה", "ואלכ'צומה",
            "וכ'צומה", "באלכ'צומה",
            "כ'צומאת", "אלכ'צומאת",
        ],
    },
    {
        "id": "khilla-matter",
        "lemma_ja": "כ'לה",
        "lemma_ar": "خَلَّة",
        "root": "kh-l-l",
        "pos": "noun (f., post-classical)",
        "gloss_en": "action, deed, case, matter, thing",
        "gloss_he": "מעשה, עניין, דבר",
        "notes": "Post-classical / Judeo-Arabic usage; extensively attested in Saadia (Blau §1085). Distinct from the verb khallā 'to leave alone'.",
        "saadia_note": "Saadia's regular gloss for Hebrew זֹאת / דָּבָר in legal-exhortative formulas: 'do this matter' = אצנעו כ'לה (Num 16:6, Gen 42:18). Blau §1085 documents the pattern across many Saadianic biblical translations.",
        "source": "lane",
        "variants": [
            "כלה",
            "אלכ'לה", "אלכלה",
            "ואלכ'לה", "ואלכלה",
            "באלכ'לה", "באלכלה",
            "וכ'לה", "וכלה",
            "כ'להא", "כלהא",
        ],
    },

    # ---------- Numerals ----------
    {
        "id": "khamsa-five",
        "lemma_ja": "כמסה",
        "lemma_ar": "خَمْسَة",
        "root": "kh-m-s",
        "pos": "numeral",
        "gloss_en": "five (masculine counted)",
        "gloss_he": "חמישה",
        "notes": "Arabic gender polarity: khamsa (with tā' marbūṭa) counts masculine nouns; khams counts feminine. Note JA spelling כמסה lacks the apostrophe-marked خ — scribal convention varies.",
        "source": "lane",
        "variants": [
            "כ'מסה",
            "וכמסה", "וכ'מסה",
            "אלכמסה", "אלכ'מסה",
            "בכמסה", "בכ'מסה",
        ],
    },
    {
        "id": "thamaniya-eight",
        "lemma_ja": "ת'מאניה",
        "lemma_ar": "ثَمَانِيَة",
        "root": "th-m-n",
        "pos": "numeral",
        "gloss_en": "eight (masculine counted)",
        "gloss_he": "שמונה",
        "notes": "Arabic gender polarity: thamāniya (with tā' marbūṭa) counts masculine nouns; thamānin counts feminine.",
        "source": "lane",
        "variants": [
            "ות'מאניה",
            "אלת'אמן", "ואלת'אמן",   # ordinal: the eighth
            "ת'אמן", "ות'אמן",
            "ת'מאנין", "ות'מאנין",   # 80
            "אלת'מאניה", "ואלת'מאניה",
        ],
    },

    # ---------- Function words ----------
    {
        "id": "kam-howmany",
        "lemma_ja": "כם",
        "lemma_ar": "كَم",
        "root": "—",
        "pos": "particle (interrogative)",
        "gloss_en": "how much? how many? how long?",
        "gloss_he": "כמה? עד מתי?",
        "notes": "Interrogative for quantity or duration. In the construction 'ilā kam' = 'until when / how long', it renders Heb עַד-אָנָה (Num 14:11, 14:27 אלי' כם אבקי 'how long shall I endure').",
        "source": "lane",
        "variants": [
            "וכם", "פכם", "אלי' כם",
        ],
    },
    {
        "id": "ulaika-those",
        "lemma_ja": "אולאיך",
        "lemma_ar": "أُولَائِك",
        "root": "—",
        "pos": "demonstrative pronoun (distal pl.)",
        "gloss_en": "those (people/things — distal plural)",
        "gloss_he": "ההם, הללו",
        "notes": "Distal plural demonstrative. The proximal counterpart is hāʾulāʾ (האולאי) 'these'. Saadia uses both regularly.",
        "source": "lane",
        "variants": [
            "ואולאיך", "פאולאיך",
            "אלאואלאיך",
        ],
    },
    {
        "id": "hidha-facing",
        "lemma_ja": "חד'א",
        "lemma_ar": "حِذَاء",
        "root": "ḥ-dh-w",
        "pos": "preposition / adverb",
        "gloss_en": "facing, opposite, parallel to, alongside; over against",
        "gloss_he": "מול, נֹכַח, לְעֻמַּת, כְּנֶגֶד",
        "saadia_note": "Saadia uses ḥidhāʾa as a spatial preposition for 'facing / alongside / opposite' — e.g. Num 2:2 חד'א כ'בא אלמחצ'ר 'facing the Tent of Meeting' (Heb נֶגֶד); Num 25:4 חד'א אלשמס 'in the open, facing the sun' (Heb נֶגֶד הַשָּׁמֶשׁ).",
        "source": "lane",
        "variants": [
            "וחד'א", "פחד'א",
            "חד'אה", "חד'אהא", "חד'אהם",
            "באלחד'א",
        ],
    },

    # ---------- Proper nouns ----------
    {
        "id": "caleb-name",
        "lemma_ja": "כלב",
        "lemma_ar": "كَالِب",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Caleb (son of Jephunneh, spy from the tribe of Judah)",
        "gloss_he": "כָּלֵב בֶּן יְפֻנֶּה",
        "notes": "Homograph with classical Arabic kalb 'dog' (which has root k-l-b). In the Pentateuch's JA tafsir, every attested כלב refers to Caleb — context disambiguates.",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "וכלב", "לכלב", "בכלב",
            "כלבא",
        ],
    },
    {
        "id": "er-name",
        "lemma_ja": "ער",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Er — (1) son of Judah (Gen 38); (2) Ar (or 'Er Moab'), a Moabite city east of the Arnon (Num 21:15, 21:28; Deut 2:9, 2:18, 2:29)",
        "gloss_he": "עֵר — (1) בנו של יהודה; (2) עָר־מוֹאָב, עיר מואבית",
        "notes": "In the Pentateuch the homograph context is almost always the Moabite city Ar, not Judah's firstborn — the latter appears once in Num 26:19. Saadia retains the Hebrew form unchanged for both senses.",
        "source": "lane",
        "variants": [
            "וער", "לער", "בער",
        ],
    },
    {
        "id": "abihu-name",
        "lemma_ja": "אביהוא",
        "lemma_ar": "—",
        "root": "—",
        "pos": "proper noun",
        "gloss_en": "Abihu — second son of Aaron, killed for offering 'strange fire' (Lev 10; Num 3:4, 26:60-61)",
        "gloss_he": "אֲבִיהוּא בֶּן אַהֲרֹן",
        "notes": "Always paired with נדב (Nadab) in the Pentateuchal narrative formulas.",
        "saadia_note": "Saadia retains the Hebrew name unchanged.",
        "source": "lane",
        "variants": [
            "ואביהוא", "לאביהוא", "באביהוא",
        ],
    },
]


VARIANTS_PATCH = {
    # Already-glossed entries that simply need the new surface form.
    "laysa":          ["אליס"],     # ʔa-laysa "is it not?" interrogative
    "mardy-pleasing": ["מרצ'ייא"],  # marḍiyyan, accusative indef
    "rahala-depart":  ["ירחלון"],   # 3mp impf with energetic-style -ūn
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

    # --- Pass 2: extend variants on existing entries ---
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

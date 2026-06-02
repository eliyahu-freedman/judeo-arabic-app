#!/usr/bin/env python3
"""Consolidate the אלממתעה ↔ ממתעה duplicate into a single 2-book TWIST.

Phase 3 R2 follow-on (out-of-scope for R2's promote-in-place-only scope, which
forbade entry removal). The TWIST `אלממתעה` (Gen 38:15/21/22, Tamar pericope) and
the NOTE `ממתעה` (Deut 23:18 prohibition) document the SAME Saadia lexical move —
rendering Heb קְדֵשָׁה/קָדֵשׁ via Ar مُمَتَّعَة (pleasure-object). This script:

  1. Deletes the NOTE entry (lemma_ja=ממתעה, tier=note).
  2. Promotes the TWIST to 2-book: adds Deut 23:18 to verses[], merges variants,
     and rewrites mechanism + blau_dict.sense to fold in the NOTE's theological
     analysis (consecration-stripping / category-delegitimization) and drop the
     stale "see the separate NOTE entry" cross-reference.

Net effect: 124 → 123 entries; tiers 36 twist / 38 note / 50 gloss → 36 / 37 / 50.
Idempotent: re-running is a no-op once the NOTE is gone and Deut 23:18 is present.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIV = ROOT / "data" / "tafsir-divergence.json"

DEUT = {"book": "Devarim", "ch": 23, "v": 18}

NEW_MECHANISM = (
    "Lexical specification (anti-rabbinic / against the targumic neutralization), "
    "documented across a full cross-Pentateuchal arc that binds the NARRATIVE Tamar "
    "pericope (Gen 38:15, 21, 22) to the LEGISLATIVE prohibition (Deut 23:18). The "
    "Targumim and most medieval commentators render קְדֵשָׁה with a generic 'prostitute' "
    "word, effacing the cultic dimension. Saadia, working in an Islamic "
    "juristic-lexicographical milieu where متعة carries technical resonance (the Shia "
    "متعة-marriage contract), instead picks a term that names the cultic-utility category "
    "and deploys it as a stable terminus-technicus wherever the cult-prostitute appears.\n\n"
    "NARRATIVE (Gen 38, Tamar): (1) Gen 38:15 (Heb וַיַּחְשְׁבֶהָ לְזוֹנָה 'and he reckoned her a "
    "harlot' = וחסבהא ממתעה — Saadia reroutes even the generic Heb זוֹנָה through ממתעה, "
    "surfacing the cultic-prostitute category where the Hebrew uses the plain harlot-word); "
    "(2) Gen 38:21 (Heb אַיֵּה הַקְּדֵשָׁה 'where is the cult-prostitute' = אין אלממתעה — the anchor); "
    "(3) Gen 38:22 (Heb לֹא הָיְתָה בָזֶה קְדֵשָׁה = מא כאנת ההנא ממתעה). Within the pericope Saadia treats "
    "the three Heb terms (זוֹנָה / הַקְּדֵשָׁה / קְדֵשָׁה) as a single social-cultic category and uses one "
    "Arabic word for all three.\n\n"
    "LEGISLATIVE (Deut 23:18, the prohibition on an Israelite becoming a קָדֵשׁ/קְדֵשָׁה): Heb "
    "לֹא תִהְיֶה קְדֵשָׁה ... וְלֹא יִהְיֶה קָדֵשׁ = ולא תכון ... ממתעה ... ולא ... ממתע (fem./masc.). Here the move "
    "carries an extra theological charge. The Hebrew names the cult-prostitute through the "
    "CONSECRATION root קדש — the very root that names the Israelite priests' consecration — "
    "conceding that the figure is 'set apart' (even if to the wrong god) and preserving a "
    "structural parallel between Israelite priests and foreign cult-prostitutes as fellow "
    "'consecrated ones'. Saadia REFUSES that consecration-frame: by routing קדש through متع "
    "'to derive pleasure from' he renames the figure by FUNCTION (sexual-utility object) rather "
    "than STATUS (cultic set-apartness). The prohibition therefore works by "
    "category-DELEGITIMIZATION rather than category-EXCLUSION — not 'do not keep Israelite "
    "consecrated-prostitutes' (which would still grant the rival system its "
    "consecration-vocabulary) but 'do not let any Israelite become a pleasure-object'. Saadia's "
    "lexicon will not concede rival cults a consecration-vocabulary even while forbidding them — "
    "exceptional against Heb-Ar pairs where he preserves rival-cult categories (e.g. אֱלִיל = صنم "
    "'idol', the substantive retained).\n\n"
    "The narrative→legislative consistency is the paradigm: one stable Arabic terminus-technicus "
    "ties Tamar's ad-hoc deception to Deuteronomy's standing prohibition, and reads Tamar as "
    "deliberately assuming a recognized cultic identity to claim the right of "
    "levirate-substitution — not as a merely generic harlot."
)

NEW_BLAU_SENSE = (
    "ممتعة / مُمَتَّع 'harlot, temple-prostitute / קְדֵשָׁה־קָדֵשׁ, אדם שנועד לזנות פולחנית' — Blau cites "
    "Saadia on both the Tamar narrative (Gen 38:21: 'איה הקדשה... לא הייתה בזה קדשה' → 'אין "
    "אלממתעה... מא כאנת ההנא ממתעה') and the parallel legislative prohibition (Deut 23:18: 'לא "
    "תהיה קדשה ... ולא יהיה קדש' → 'ולא תכון ... ממתעה ... ולא ... ממתע') — both verses now held in "
    "this entry's verses[]. The R2 cross-pericope scan adds the Gen 38:15 attestation where "
    "Saadia routes Heb זוֹנָה through the same ממתעה terminus. In every case the Heb "
    "consecration/harlot vocabulary is rerouted through the Form II متع pleasure-vocabulary, "
    "preserved from Quranic-register usage."
)


def main():
    payload = json.loads(DIV.read_text(encoding="utf-8"))
    entries = payload["entries"]

    # 1. Delete the NOTE entry (idempotent).
    note_idx = next(
        (i for i, e in enumerate(entries)
         if e.get("lemma_ja") == "ממתעה" and e.get("tier") == "note"),
        None,
    )
    note = entries.pop(note_idx) if note_idx is not None else None

    # 2. Promote the TWIST.
    twist = next(
        e for e in entries
        if e.get("lemma_ja") == "אלממתעה" and e.get("tier") == "twist"
    )

    # 2a. Add Deut 23:18 to verses[] (guard against dup).
    verse_added = False
    if DEUT not in twist["verses"]:
        twist["verses"].append(DEUT)
        verse_added = True

    # 2b. Merge variants from the deleted NOTE (skip dups + the lemma itself).
    added_variants = []
    if note:
        for v in note.get("variants", []):
            if v != twist["lemma_ja"] and v not in twist.get("variants", []):
                twist.setdefault("variants", []).append(v)
                added_variants.append(v)

    # 2c. Rewrite mechanism + blau_dict.sense.
    twist["mechanism"] = NEW_MECHANISM
    twist["blau_dict"]["sense"] = NEW_BLAU_SENSE

    DIV.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    # parse-check
    json.loads(DIV.read_text(encoding="utf-8"))

    print(f"NOTE deleted: {'yes' if note else 'already absent'}")
    print(f"Deut 23:18 added to TWIST verses[]: {verse_added}")
    print(f"Variants merged into TWIST: {added_variants or 'none new'}")
    print(f"TWIST verses now: {twist['verses']}")
    print(f"TWIST variants now: {twist.get('variants')}")
    print(f"Total entries: {len(entries)}")


if __name__ == "__main__":
    main()

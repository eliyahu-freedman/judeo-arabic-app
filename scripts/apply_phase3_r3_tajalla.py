#!/usr/bin/env python3
"""
Phase 3 R3 — new TWIST: the Sinai/Tent تَجَلَّى manifestation-cluster.

The R2 Batch 2 `אורד` mechanism correction empirically isolated this cluster:
Saadia renders the Hebrew theophany verb יָרַד/וַיֵּרֶד יְהוָה ("and the LORD
descended") at the REVELATORY descents (Sinai + Tent of Meeting) with Form V
تَجَلَّى ("manifested Himself," in fire/cloud) — NOT with the Form IV أورد
"dispatch" frame he uses for the PUNITIVE descents of Babel and Sodom (the
separate אורד entry). Two distinct anti-anthropomorphic strategies for one
Hebrew verb.

Verse evidence (read from the repo's Saadia text, not assumed):
  Ex 19:11  יֵרֵד יְהוָה            → יתגלא אללה ... עלי גבל סיני
  Ex 19:18  יָרַד עָלָיו ... בָּאֵשׁ   → תגלא עליה אללה באלנאר
  Ex 19:20  וַיֵּרֶד ... עַל הַר סִינַי → תגלא אללה עלי גבל סיני
  Ex 34:5   וַיֵּרֶד ... בֶּעָנָן       → פתגלא אללה באלג'מאם
  Num 11:25 וַיֵּרֶד ... בֶּעָנָן       → פתגלא אללה פי אלג'מאם
  Num 12:5  וַיֵּרֶד ... בְּעַמּוּד עָנָן → פתגלא אללה בעמוד ג'מאם

Sources: ["lane", "saadia-direct"]. NO "blau-dict" — a full-text search of the
real Blau corpus (~/Tools/arabic-lexicon, blau-judeoarabic) returns 0 hits for
every Form V surface (تجلى/تجلّى/تجل/انجلى), 0 for Form II جلّى, and 0 for the
Hebrew-script JA surfaces Saadia uses (תג'לי/יתג'לי). The root appears only as
Form I (جلو, جلا) in the classical reflect-light / emigrate-exile (גלות/جلاء) /
polish senses — none documenting the theophany-manifestation rendering of Heb
ירד. Per the PHASE3_R1 no-cite-audit rule (cf. the אתון verifier-crash), this
entry does NOT carry a blau_dict block and does NOT cite blau-dict.

Mirrors the NEW_ENTRIES pattern in scripts/apply_phase4_devarim_batch1.py:
build the entry dict, guard against a duplicate lemma, append, write back with
ensure_ascii=False / indent=2 / trailing newline, then parse-check. Idempotent.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIV = ROOT / "data" / "tafsir-divergence.json"
DEFERRED = ROOT / "data" / "_blau_saadia_deferred.json"

NEW_ENTRY = {
    "lemma_ja": "תגלא",
    "variants": ["יתגלא", "פתגלא"],
    "lemma_ar": "تجلّى",
    "root": "ج-ل-و",
    "tier": "twist",
    "classical_en": (
        "Form V تَجَلَّى — reflexive of Form II جَلَّى, from the root ج-ل-و 'to polish, "
        "burnish, make clear; to remove a covering.' Lane (s.v. جلو): جلا 'to cleanse / "
        "polish (a sword) so as to remove its rust'; said of the sky, 'it became free "
        "from clouds, became clear'; انجلى عن 'it became removed or withdrawn from a thing "
        "it had been covering or concealing.' The Form V means 'to become manifest, to "
        "reveal or show oneself, to become unveiled, to become clear.' It is the canonical "
        "Qur'anic verb for divine self-manifestation: Q 7:143, فَلَمَّا تَجَلَّى رَبُّهُ لِلْجَبَلِ "
        "'when his Lord manifested Himself to the mountain' — the Sinai theophany of Moses."
    ),
    "classical_he": (
        "בניין V تَجَلَّى — הרפלקסיב של בניין II جَلَّى, מן השורש ج-ل-و 'לְלַטֵּשׁ, לְמָרֵק, "
        "לְהַבְהִיר; לְהָסִיר כיסוי'. ליין (ערך جلو): جلا 'לְמָרֵק / לְלַטֵּשׁ (חרב) עד הסרת "
        "החלודה'; על השמיים, 'התבהרו מעננים'; انجلى عن 'הוסר / נסוג מדבר שכיסה עליו'. "
        "בניין V פירושו 'להתגלות, לחשוף/להראות את עצמו, להיחשף, להתבהר'. זהו הפועל הקוראני "
        "המובהק להתגלות אלוהית: קוראן ז׳:143, فَلَمَّا تَجَلَّى رَبُّهُ لِلْجَبَلِ 'וכאשר התגלה "
        "ריבונו אל ההר' — התגלות סיני של משה."
    ),
    "saadia_en": (
        "God manifests Himself — Saadia renders the Hebrew theophany verb יָרַד/וַיֵּרֶד "
        "יְהוָה ('and the LORD descended') at the Sinai and Tent-of-Meeting revelations not "
        "with a literal 'descend' verb but with Form V تَجَلَّى ('manifested Himself,' in "
        "fire or cloud). The rendering is anti-anthropomorphic: it refuses to depict God "
        "as physically moving downward through space, recasting the 'descent' as a "
        "manifestation of the divine presence — localized in the fire (אלנאר), the cloud "
        "(אלג'מאם), or the divine light (אלנור) — at the sacred locus."
    ),
    "saadia_he": (
        "האל מתגלה — סעדיה מתרגם את פועל ההתגלות העברי יָרַד/וַיֵּרֶד יְהוָה ('וירד ה׳') "
        "בהתגלויות סיני ואוהל מועד לא בפועל 'ירידה' מילולי אלא בבניין V تَجَلَّى ('התגלה', "
        "באש או בענן). התרגום אנטי-אנתרופומורפי: הוא מסרב לתאר את האל כנע מטה במרחב, "
        "וממסגר את ה'ירידה' כהתגלות הנוכחות האלוהית — הממוקמת באש (אלנאר), בענן (אלג'מאם) "
        "או באור האלוהי (אלנור) — במקום הקדוש."
    ),
    "mechanism": (
        "Anti-anthropomorphic substitution — the theophany counterpart to the אורד "
        "dispatch-frame. Where the Hebrew has YHWH 'come down' (יָרַד/וַיֵּרֶד) to reveal "
        "Himself at a sacred locus, Saadia routes the descent through Form V تَجَلَّى ('to "
        "manifest oneself, become visible/unveiled'), refusing a literal spatial descent of "
        "the deity. This is one of TWO distinct anti-anthropomorphic strategies Saadia "
        "deploys for the single Hebrew verb ירד, split by context: (1) the DISPATCH frame — "
        "Form IV أورد ('to send down, dispatch a directed command,' amr muwajjah) — at the "
        "punitive-investigation descents of Babel (Gen 11:5, 7) and Sodom (Gen 18:21), where "
        "God 'comes down to see' before judgment (handled by the separate אורד entry); and "
        "(2) the MANIFESTATION frame — Form V تَجَلَّى — at the REVELATORY descents, where God "
        "'comes down' to be present and to speak. The manifestation cluster: the Sinai "
        "theophany (Ex 19:11 יֵרֵד יְהוָה → יתגלא אללה; 19:18 יָרַד ... בָּאֵשׁ → תגלא עליה אללה "
        "באלנאר 'manifested ... in the fire'; 19:20 וַיֵּרֶד ... עַל הַר סִינַי → תגלא אללה עלי "
        "גבל סיני) and the second-tablets revelation (Ex 34:5 וַיֵּרֶד ... בֶּעָנָן → פתגלא אללה "
        "באלג'מאם 'manifested ... in the cloud'); and the Tent-of-Meeting / wilderness "
        "theophanies (Num 11:25 וַיֵּרֶד ... בֶּעָנָן → פתגלא אללה פי אלג'מאם; Num 12:5 וַיֵּרֶד "
        "... בְּעַמּוּד עָנָן → פתגלא אללה בעמוד ג'מאם 'manifested ... in a pillar of cloud'). The "
        "manifestation is consistently localized in the fire, the cloud, or the divine light "
        "— the visible token of presence — never in a moving divine body. The lexical choice "
        "carries a precise Islamic-register resonance: تَجَلَّى is the Qur'an's own verb for "
        "God's self-manifestation to the mountain at Sinai (Q 7:143, فَلَمَّا تَجَلَّى رَبُّهُ "
        "لِلْجَبَلِ), so Saadia renders the Pentateuch's Sinai theophany with the very term his "
        "Arabic-reading audience associates with that event. The cross-book consistency "
        "(Shemot + Bamidbar, 6 verses) confirms that تَجَلَّى is Saadia's systematic "
        "terminus-technicus for revelatory divine descent, paradigmatically distinct from the "
        "punitive-dispatch أورد frame. Pedagogically distinctive because the two frames "
        "together show Saadia sorting one Hebrew verb (ירד) into two theologically-typed "
        "Arabic renderings — dispatch-for-judgment vs. manifestation-for-revelation — neither "
        "of which concedes a literal divine descent."
    ),
    "verses": [
        {"book": "Shemot", "ch": 19, "v": 11},
        {"book": "Shemot", "ch": 19, "v": 18},
        {"book": "Shemot", "ch": 19, "v": 20},
        {"book": "Shemot", "ch": 34, "v": 5},
        {"book": "Bamidbar", "ch": 11, "v": 25},
        {"book": "Bamidbar", "ch": 12, "v": 5},
    ],
    "sources": ["lane", "saadia-direct"],
}


def main():
    if not DIV.exists():
        print(f"FATAL: {DIV} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(DIV.read_text(encoding="utf-8"))
    entries = payload["entries"]

    if any(e.get("lemma_ja") == NEW_ENTRY["lemma_ja"] for e in entries):
        print(f"Idempotent no-op: lemma {NEW_ENTRY['lemma_ja']} already present.")
        return

    new_keys = {(v["book"], v["ch"], v["v"]) for v in NEW_ENTRY["verses"]}
    collisions = []
    for e in entries:
        for v in e.get("verses", []):
            if (v["book"], v["ch"], v["v"]) in new_keys:
                collisions.append((e.get("lemma_ja"), v["book"], v["ch"], v["v"]))
    if collisions:
        print(f"WARNING: target verses already covered elsewhere: {collisions}", file=sys.stderr)

    entries.append(NEW_ENTRY)

    DIV.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    json.loads(DIV.read_text(encoding="utf-8"))  # parse-check

    if DEFERRED.exists():
        dpayload = json.loads(DEFERRED.read_text(encoding="utf-8"))
        nca = dpayload.setdefault("no_cite_audit", {})
        if isinstance(nca, dict):
            log = nca.setdefault("phase3_r3_no_blau", [])
            note = (
                "תגלא (تجلّى, Form V) — new R3 TWIST, sources=[lane, saadia-direct], NO blau-dict: "
                "full-text search of the real Blau corpus (blau-judeoarabic) returns 0 hits for every "
                "Form V surface (تجلى/تجلّى/تجل/انجلى), 0 for Form II جلّى, and 0 for the Hebrew-script JA "
                "surfaces (תג'לי/יתג'לי); the root appears only as Form I (جلو/جلا) in the classical "
                "reflect-light / emigrate-exile (גלות/جلاء) / polish senses, none documenting the "
                "theophany-manifestation rendering of Heb ירד. saadia-direct + Lane (Q 7:143 "
                "Sinai-theophany resonance) ground the entry. Shipped via scripts/apply_phase3_r3_tajalla.py."
            )
            if isinstance(log, list):
                # keep a single canonical note (drop any stale earlier wording)
                nca["phase3_r3_no_blau"] = [note]
                DEFERRED.write_text(json.dumps(dpayload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    from collections import Counter
    print("New TWIST added: תגלא (تجلّى) — Sinai/Tent manifestation-cluster, 6 verses.")
    print(f"Total entries: {len(entries)}")
    print("Tiers:", dict(Counter(e.get("tier", "twist") for e in entries)))


if __name__ == "__main__":
    main()

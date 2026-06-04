"""
Phase 4 — Bereshit Batch 4 (final this session).

Two entries surfaced by a looser scan of candidate body_excerpts
(not just citation_lines) for Hebrew verse references.

Tier breakdown:
  - 1 NOTE  — Saadia derives a biblical hapax from an unusual Arabic root
  - 1 GLOSS — winter/autumn (the matching pair to قيظ from batch 1)

After this batch the no-verse-ref pool yields diminishing returns; the
remaining 140+ untriaged candidates are mostly cluster duplicates of
already-mined Blau articles, page-line refs to Saadia's intro footnotes,
or non-Tafsir Geniza/Qirqisani/Maimonides citations. See
PHASE4_BERESHIT_SESSION_NOTES.md for the strategy hand-off.
"""

import json
import pathlib
import sys
from collections import Counter


NEW_ENTRIES = [
    # ---- NOTE — Gen 6:3: divine speech limiting human lifespan -------------
    {
        "lemma_ja": "ינג'מד",
        "variants": ["ינגמד", "ג'מד"],
        "lemma_ar": "يَنغَمِد",
        "root": "غ-م-د",
        "tier": "note",
        "classical_en": "Hebrew יָדוֹן — the classical rabbinic reading 'shall (not) judge / contend with man'",
        "classical_he": "יָדוֹן — הקריאה הקלסית של חז״ל: '(לא) יָדִין / יָרִיב רוחי באדם'",
        "saadia_en": "Saadia derives יָדוֹן from a root meaning 'to be sheathed, settled, fixed' — 'my spirit shall not be sheathed [permanently] in man'",
        "saadia_he": "רס״ג גוזר 'ידון' מ-غمد ('נדן, נרתיק') — 'לא תיעצר רוחי באדם' / 'לא תיקבע בו לעולם'",
        "mechanism": "Saadia tackles the famous hapax יָדוֹן (Gen 6:3) by reaching for Arabic غمد ('scabbard, sheath') as the etymological key. The divine speech becomes a statement about the soul not being permanently sheathed in flesh, rather than a juridical contention. This is the kind of lexical-philosophical move Blau records as the basis for the rendering, citing also Saadia's parallel on Dan 7:9.",
        "verses": [{"book": "Bereshit", "ch": 6, "v": 3}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "غمد",
            "sense": "غمد VII 'to be sheathed, fixed in place' (lit. 'to be put into its scabbard') — Blau attests the rendering citing Saadia on Gen 6:3 explicitly: '[the use] is based on Saadia on Bereshit 6:3 (לא ידון רוחי), derived from נון; Saadia renders accordingly'.",
            "relation": "direct",
        },
    },
    # ---- GLOSS — Gen 8:22: post-flood seasons (winter/autumn pair) ---------
    {
        "lemma_ja": "כ'ריף",
        "variants": ["אלכ'ריף", "כ'וף"],
        "lemma_ar": "خريف",
        "root": "خ-ر-ف",
        "tier": "gloss",
        "classical_en": "winter (Hebrew-shaped usage) — biblical translators stretch خريف from 'autumn' to encompass 'winter/cold-season'",
        "classical_he": "חֹרֶף — מתרגמי המקרא מותחים את 'כ'ריף' ('סתיו') להוראת חורף",
        "saadia_en": "winter",
        "saadia_he": "חורף",
        "mechanism": "Hebrew-shaped lexical extension: classical Arabic خريف means 'autumn', not 'winter', but biblical translators (Saadia included) extend it to render the Hebrew חֹרֶף — the cold-half of the year. Pairs with قيظ for קַיִץ in the same verse, completing the four-season frame.",
        "verses": [{"book": "Bereshit", "ch": 8, "v": 22}],
        "sources": ["blau-dict", "saadia-direct"],
        "blau_dict": {
            "root": "خرف",
            "sense": "خريف 'winter' (under Hebrew influence; classical Arabic = 'autumn') — Blau attests in biblical translation traditions only, citing Saadia on Gen 8:22 and Ps 74:17 (קיץ וחוף = אלקיל ואלכ'ריף).",
            "relation": "direct",
        },
    },
]


def main():
    path = pathlib.Path("data/tafsir-divergence.json")
    if not path.exists():
        print(f"FATAL: {path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    payload = json.loads(path.read_text())

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

    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(path.read_text())

    print(f"Added {added} entries to {path}")
    for s, reason in skipped:
        print(f"  - skipped {s}: {reason}")
    print(f"Total entries now: {len(payload['entries'])}")
    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")


if __name__ == "__main__":
    main()

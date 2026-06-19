#!/usr/bin/env python3
"""Read-only audit: surface forms claimed by BOTH a proper-noun entry and a
common-noun entry in the hand dictionaries — the homograph collisions that let a
proper noun (e.g. Medan/Midian) shadow a common word (e.g. "city").

Most collisions are legitimate homographs (Caleb/dog, Laban/milk) where both
senses belong; the bugs are over-reach cases where a proper-noun entry lists a
common word in its `variants`. The second report flags exactly those: a
proper-noun entry whose variant equals another entry's common-noun lemma.

Run:  python3 scripts/audit_dict_homographs.py
"""
import json, re
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
FINALS = {"ך": "כ", "ם": "מ", "ן": "נ", "ף": "פ", "ץ": "צ"}


def nf(s: str) -> str:
    s = re.sub(r"[֑-ׇ]", "", s or "")
    for a, b in FINALS.items():
        s = s.replace(a, b)
    return s[:-1] if s.endswith("'") else s


def is_pn(e) -> bool:
    return "proper" in (e.get("pos") or "").lower()


def main():
    entries = []
    for f in ("dictionary-starter.json", "dictionary-lane.json"):
        entries += json.loads((DATA / f).read_text())["entries"]

    # normalized form -> entries claiming it (lemma or variant)
    forms: dict[str, list] = {}
    # normalized lemma (common-noun only) -> entry, for the over-reach check
    common_lemma: dict[str, dict] = {}
    for e in entries:
        if not is_pn(e) and e.get("lemma_ja"):
            common_lemma.setdefault(nf(e["lemma_ja"]), e)
        claimed = {e.get("lemma_ja", "")} | set(e.get("variants") or [])
        for c in claimed:
            if c:
                forms.setdefault(nf(c), []).append(e)

    collisions = []
    for f, lst in forms.items():
        pn = [e for e in lst if is_pn(e)]
        com = [e for e in lst if not is_pn(e)]
        if pn and com:
            collisions.append((f, pn, com))

    print(f"=== {len(collisions)} proper-noun ↔ common-noun form collisions ===")
    for f, pn, com in sorted(collisions):
        print(f"  {f}")
        for e in pn:
            print(f"      PN  {e.get('id')}: {e.get('gloss_en','')[:48]}")
        for e in com:
            print(f"      com {e.get('id')}: {e.get('gloss_en','')[:48]}")

    print("\n=== OVER-REACH: proper-noun entries whose VARIANT is a common-noun lemma ===")
    flagged = 0
    for e in entries:
        if not is_pn(e):
            continue
        for v in e.get("variants") or []:
            hit = common_lemma.get(nf(v))
            if hit and nf(v) != nf(e.get("lemma_ja", "")):
                print(f"  {e.get('id')} ({e.get('gloss_en','')[:24]}) lists variant "
                      f"{v!r} == common lemma {hit.get('lemma_ja')!r} "
                      f"({hit.get('gloss_en','')[:30]})")
                flagged += 1
    print(f"  ({flagged} over-reach variant(s) flagged for review)")


if __name__ == "__main__":
    main()

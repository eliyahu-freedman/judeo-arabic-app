#!/usr/bin/env python3
"""One-shot fix for proper-noun entries that shadowed common words in
data/dictionary-lane.json (see the מדן→"Medan" bug in Moreh I:2).

Principle: a variant is removed from a proper-noun entry only when it is
genuinely a different common word; homeless forms are first MOVED to their
correct common entry so word-tap coverage never drops. Legitimate name
homographs (חתי=Hittite, וגד=and-Gad, בחת=in-Heth, מצרי=Egypt) are left alone.

Run:  python3 scripts/fix_propernoun_homographs.py   (writes in place)
"""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "dictionary-lane.json"

ADD = {  # entry id -> variants to add (deduped)
    "qc-m-d-n-אלמדינה": ["מדן", "אלמדן", "מדאין", "אלמדאין", "במדינה", "מדינתהם"],
    "taf-d-675-5": ["יכלבו", "ילכבו", "פכלבוכם", "כלבוכם", "ויכלבהם", "יכלבהם",
                     "וכלבוהם", "אכלבהם"],  # pursue (kalaba) forms wrongly under Caleb
    "taf-h-315-34-3": ["פתבת", "תבת", "תבתלע"],  # swallow (balaʿa) forms wrongly under Bela
}
REMOVE = {  # entry id -> variants to remove
    "midian-name": ["מדינה", "במדינה", "מדינתהם"],          # = city, not Midian
    "sara-name": ["שרא"],                                    # = buy/evil, not Sarah
    "caleb-name": ["יכלבו", "ילכבו", "פכלבוכם", "כלבוכם",
                   "ויכלבהם", "יכלבהם", "וכלבוהם", "אכלבהם"],  # verbs, not Caleb
    "b1-בלע": ["פתבת", "תבת", "תבתלעהם", "תבתלע"],            # verbs, not Bela
}


def main():
    doc = json.loads(DATA.read_text(encoding="utf-8"))
    by_id = {e.get("id"): e for e in doc["entries"]}
    changed = 0

    for eid, adds in ADD.items():
        e = by_id.get(eid)
        if not e:
            raise SystemExit(f"missing entry to add into: {eid}")
        vs = e.setdefault("variants", [])
        for v in adds:
            if v not in vs:
                vs.append(v)
                changed += 1
        print(f"+ {eid}: variants now {len(vs)}")

    for eid, rems in REMOVE.items():
        e = by_id.get(eid)
        if not e:
            raise SystemExit(f"missing entry to remove from: {eid}")
        vs = e.get("variants", [])
        e["variants"] = [v for v in vs if v not in rems]
        removed = len(vs) - len(e["variants"])
        changed += removed
        print(f"- {eid}: removed {removed}, variants now {len(e['variants'])}")

    DATA.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"done; {changed} variant changes")


if __name__ == "__main__":
    main()

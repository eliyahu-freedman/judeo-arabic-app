"""Verify dictionary entries actually resolve through the runtime lookup chain.

For each entry in dictionary-lane.json (or --frags), assert that its lemma_ja and
every variant resolves to a starter/lane hit via the SAME chain lib/lookup.ts uses
(ported in coverage_report.py). Catches entries that would silently never fire at
runtime (e.g. a lemma listed in a form the prefix/finals normalization can't reach).

Deterministic — no model, no lexicon CLI.

Run:  python3 scripts/verify_dict.py                 # whole lane dict
      python3 scripts/verify_dict.py --frags a.json b.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from coverage_report import classify, load_keysets

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def forms(entry: dict) -> list[str]:
    out = [entry["lemma_ja"]]
    out += entry.get("variants", []) or []
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frags", nargs="*", help="check only these fragment files")
    args = ap.parse_args()

    starter, lane, auto = load_keysets()

    if args.frags:
        entries = []
        for f in args.frags:
            entries += json.loads(Path(f).read_text(encoding="utf-8")).get("entries", [])
        label = f"{len(args.frags)} fragment(s)"
    else:
        entries = json.loads((DATA / "dictionary-lane.json").read_text(encoding="utf-8"))["entries"]
        label = "dictionary-lane.json"

    fails = []
    checked = 0
    for e in entries:
        for form in forms(e):
            checked += 1
            c = classify(form, starter, lane, auto)
            if c not in ("starter", "lane"):
                fails.append((e["id"], form, c))

    print(f"verified {checked} surface forms across {len(entries)} entries in {label}")
    if fails:
        print(f"\nFAIL: {len(fails)} forms do not resolve to a hand entry:")
        for eid, form, c in fails[:50]:
            print(f"  [{eid}]  {form!r}  -> {c}")
        raise SystemExit(1)
    print("OK: every lemma_ja + variant resolves through the lookup chain.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Merge workflow-produced aligned pages into data/bahya-bab<BAB>-aligned.json.

Usage: merge_bahya_alignment.py BAB <workflow_output.json> [<more_output.json> ...]

Each input is either:
  - a task-output file with {"result": {"pages": {...}}}, or
  - a bare {"pages": {...}} object.

Pages from later inputs override earlier ones and the existing file. Output
pages are re-ordered to follow the JA page sequence in bahya-bab<BAB>.json.
"""
import json
import os
import sys

BAB = int(sys.argv[1]) if len(sys.argv) > 1 else 1
INPUTS = sys.argv[2:]
DATA = os.path.join(os.path.dirname(__file__), "..", "data")
ALIGNED = os.path.join(DATA, f"bahya-bab{BAB}-aligned.json")


def extract_pages(obj):
    if "result" in obj and isinstance(obj["result"], dict):
        obj = obj["result"]
    return obj.get("pages", {})


def main():
    if not INPUTS:
        sys.exit("usage: merge_bahya_alignment.py BAB <output.json> [...]")

    if os.path.exists(ALIGNED):
        aligned = json.load(open(ALIGNED))
    else:
        aligned = {
            "note": f"Sentence-level JA↔EN alignment of Bahya, Bab {BAB}. "
            f"JA from bahya-bab{BAB}.json; EN from bahya-bab{BAB}-english.json "
            "(Freedman working draft).",
            "pages": {},
        }
    pages = dict(aligned.get("pages", {}))

    added = []
    for path in INPUTS:
        new = extract_pages(json.load(open(path)))
        for k, segs in new.items():
            if k not in pages:
                added.append(k)
            pages[k] = segs

    # order by JA page sequence
    ja = json.load(open(os.path.join(DATA, f"bahya-bab{BAB}.json")))
    order = [p["page_he"] for p in ja["pages"]]
    ordered = {k: pages[k] for k in order if k in pages}
    # keep any stragglers not in the sequence
    for k in pages:
        if k not in ordered:
            ordered[k] = pages[k]

    aligned["pages"] = ordered
    with open(ALIGNED, "w") as f:
        json.dump(aligned, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"merged: {len(ordered)} pages now aligned")
    print(f"newly added this run: {sorted(added)}")
    missing = [k for k in order if k not in ordered]
    print(f"still missing ({len(missing)}): {missing}")


if __name__ == "__main__":
    main()

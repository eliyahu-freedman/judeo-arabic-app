#!/usr/bin/env python3
"""Merge workflow-produced aligned pages into data/bahya-bab1-aligned.json.

Usage: merge_bahya_alignment.py <workflow_output.json> [<more_output.json> ...]

Each input is either:
  - a task-output file with {"result": {"pages": {...}}}, or
  - a bare {"pages": {...}} object.

Pages from later inputs override earlier ones and the existing file. Output
pages are re-ordered to follow the JA page sequence in bahya-bab1.json.
"""
import json
import os
import sys

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
ALIGNED = os.path.join(DATA, "bahya-bab1-aligned.json")


def extract_pages(obj):
    if "result" in obj and isinstance(obj["result"], dict):
        obj = obj["result"]
    return obj.get("pages", {})


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: merge_bahya_alignment.py <output.json> [...]")

    aligned = json.load(open(ALIGNED))
    pages = dict(aligned.get("pages", {}))

    added = []
    for path in sys.argv[1:]:
        new = extract_pages(json.load(open(path)))
        for k, segs in new.items():
            if k not in pages:
                added.append(k)
            pages[k] = segs

    # order by JA page sequence
    ja = json.load(open(os.path.join(DATA, "bahya-bab1.json")))
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

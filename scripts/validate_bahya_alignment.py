#!/usr/bin/env python3
"""Validate data/bahya-bab1-aligned.json against the alignment data contract.

Checks, per page / segment:
  1. Each pair.ja is an exact substring of seg.ja, each pair.en of seg.en
     (the resolver in lib/alignment.ts uses indexOf — a non-substring phrase is
     silently dropped, producing a missing highlight). These are FAILURES.
  2. The page's segments' JA, concatenated and whitespace-stripped, matches the
     source paragraph in bahya-bab1.json (no dropped or garbled JA text).
  3. Coverage warnings: a non-header segment with 0 pairs, or whose pairs cover
     little of the sentence.

Exit code is non-zero if any hard failure (1 or 2) is found.
"""
import json
import os
import re
import sys

DATA = os.path.join(os.path.dirname(__file__), "..", "data")


def strip_ws(s):
    return re.sub(r"\s+", "", s or "")


def main():
    aligned = json.load(open(os.path.join(DATA, "bahya-bab1-aligned.json")))
    ja_src = json.load(open(os.path.join(DATA, "bahya-bab1.json")))
    src_by_page = {p["page_he"]: " ".join(p.get("paragraphs", [])) for p in ja_src["pages"]}

    failures = []
    warnings = []
    pages = aligned.get("pages", {})

    for page_he, segs in pages.items():
        # 1. substring integrity
        concat = []
        for si, seg in enumerate(segs):
            ja, en = seg.get("ja", ""), seg.get("en", "")
            concat.append(ja)
            for pi, pair in enumerate(seg.get("pairs", [])):
                if pair.get("ja", "") not in ja:
                    failures.append(f"{page_he} seg{si} pair{pi}: ja phrase not in segment: {pair.get('ja')!r}")
                if pair.get("en", "") not in en:
                    failures.append(f"{page_he} seg{si} pair{pi}: en phrase not in segment: {pair.get('en')!r}")
            # 3. coverage
            if not seg.get("isHeader") and len(seg.get("pairs", [])) == 0:
                warnings.append(f"{page_he} seg{si}: non-header segment has 0 pairs")
            else:
                covered = sum(len(p.get("ja", "")) for p in seg.get("pairs", []))
                if ja and not seg.get("isHeader") and covered / max(len(strip_ws(ja)), 1) < 0.5:
                    warnings.append(f"{page_he} seg{si}: pairs cover <50% of JA ({covered}/{len(ja)} chars)")

        # 2. JA round-trip vs source
        src = src_by_page.get(page_he)
        if src is None:
            failures.append(f"{page_he}: no matching source page in bahya-bab1.json")
        else:
            got, want = strip_ws("".join(concat)), strip_ws(src)
            if got != want:
                # report a short diff hint
                i = 0
                while i < min(len(got), len(want)) and got[i] == want[i]:
                    i += 1
                failures.append(
                    f"{page_he}: JA concat != source (got {len(got)} chars, want {len(want)}); "
                    f"first diff at {i}: got …{got[i:i+30]!r} want …{want[i:i+30]!r}"
                )

    n_pages = len(pages)
    n_segs = sum(len(s) for s in pages.values())
    n_pairs = sum(len(seg.get("pairs", [])) for s in pages.values() for seg in s)
    print(f"pages aligned: {n_pages}; segments: {n_segs}; pairs: {n_pairs}")

    if warnings:
        print(f"\n{len(warnings)} WARNING(S):")
        for w in warnings:
            print("  ⚠ " + w)
    if failures:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures:
            print("  ✗ " + f)
        sys.exit(1)
    print("\n✓ no substring failures; all pages round-trip to source JA")


if __name__ == "__main__":
    main()

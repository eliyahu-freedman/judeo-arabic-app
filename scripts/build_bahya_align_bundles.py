#!/usr/bin/env python3
"""Build per-page work bundles for a Bahya gate's alignment job.

Usage: build_bahya_align_bundles.py [BAB]   (BAB defaults to 1)

For each JA page that is NOT already aligned, emit a self-contained file
under data/_bahya_align_work/bab<BAB>/<page_he>.json holding the JA paragraph
plus ratio-sliced English and Hebrew *candidates* (reference material for the
authoring agent — the agent does its own sentence-level alignment from the JA).

The English ratio-slice mirrors buildAligned() in app/advanced/bahya/[gate]/page.tsx.
"""
import json
import math
import os
import sys

BAB = int(sys.argv[1]) if len(sys.argv) > 1 else 1
DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT = os.path.join(DATA, "_bahya_align_work", f"bab{BAB}")


def ratio_slice(items, i, n_pages):
    n = len(items)
    start = (n * i) // n_pages
    end = (n * (i + 1)) // n_pages
    return items[start:end]


def load_optional(path, default):
    return json.load(open(path)) if os.path.exists(path) else default


def main():
    ja = json.load(open(os.path.join(DATA, f"bahya-bab{BAB}.json")))
    en = json.load(open(os.path.join(DATA, f"bahya-bab{BAB}-english.json")))
    he = load_optional(
        os.path.join(DATA, f"bahya-bab{BAB}-hebrew.json"), {"paragraphs": []}
    )
    aligned = load_optional(
        os.path.join(DATA, f"bahya-bab{BAB}-aligned.json"), {"pages": {}}
    )

    en_par = en["paragraphs"]
    he_par = he["paragraphs"]
    pages = ja["pages"]
    n_pages = len(pages)
    done = set(aligned.get("pages", {}).keys())

    aligned_pages = aligned.get("pages", {})
    os.makedirs(OUT, exist_ok=True)
    written = []
    for i, p in enumerate(pages):
        page_he = p["page_he"]
        bundle = {
            "page_he": page_he,
            "page_index": i,
            "ja": " ".join(p.get("paragraphs", [])),
            "en_candidate": "\n\n".join(ratio_slice(en_par, i, n_pages)),
            "he_candidate": "\n\n".join(ratio_slice(he_par, i, n_pages)),
            # Existing hand-authored segments (only מד today). The agent must
            # KEEP these verbatim and append segments covering the rest of the
            # paragraph, so the proven exemplar is preserved, not redone.
            "existing_segments": aligned_pages.get(page_he, []),
        }
        with open(os.path.join(OUT, f"{page_he}.json"), "w") as f:
            json.dump(bundle, f, ensure_ascii=False, indent=2)
        written.append(page_he)

    print(f"pages total: {n_pages}; already (partly) aligned: {sorted(done)}")
    print(f"wrote {len(written)} bundles to {OUT}")
    print("page order:", written)


if __name__ == "__main__":
    main()

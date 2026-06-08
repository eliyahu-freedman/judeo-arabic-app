#!/usr/bin/env python3
"""Build per-page work bundles for the Bahya First Gate alignment job.

For each JA page that is NOT already aligned, emit a self-contained file
under data/_bahya_align_work/<page_he>.json holding the JA paragraph plus
ratio-sliced English and Hebrew *candidates* (reference material for the
authoring agent — the agent does its own sentence-level alignment from the JA).

The English ratio-slice mirrors app/advanced/bahya/page.tsx:26-27.
"""
import json
import math
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT = os.path.join(DATA, "_bahya_align_work")


def ratio_slice(items, i, n_pages):
    n = len(items)
    start = (n * i) // n_pages
    end = (n * (i + 1)) // n_pages
    return items[start:end]


def main():
    ja = json.load(open(os.path.join(DATA, "bahya-bab1.json")))
    en = json.load(open(os.path.join(DATA, "bahya-bab1-english.json")))
    he = json.load(open(os.path.join(DATA, "bahya-bab1-hebrew.json")))
    aligned = json.load(open(os.path.join(DATA, "bahya-bab1-aligned.json")))

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

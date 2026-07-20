"""Generate a skeleton aligned JSON for a Bahya gate — no API required.

Usage:
  skeleton_align.py bab7          # → data/bahya-bab7-aligned.json
  skeleton_align.py hakdamah      # → data/bahya-hakdamah-aligned.json
  skeleton_align.py bab8 bab9     # multiple slugs at once

The skeleton assigns English paragraphs to pages proportionally (by JA
character weight), then wraps each page as a single AlignedSegment with
pairs: [].  Edit the output to split segments and add phrase-level pairs.

After running, update app/advanced/bahya/volume.ts:
  import bab7english from "@/data/bahya-bab7-english.json";
  import bab7aligned from "@/data/bahya-bab7-aligned.json";
  // in BAHYA_GATES replace { slug: "bab-7", json: bab7 } with:
  { slug: "bab-7", json: bab7 as GateJson, english: bab7english as EnglishJson, aligned: bab7aligned as AlignedJson },
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def process_slug(slug: str) -> None:
    ja_path = DATA_DIR / f"bahya-{slug}.json"
    en_path = DATA_DIR / f"bahya-{slug}-english.json"
    out_path = DATA_DIR / f"bahya-{slug}-aligned.json"

    if not ja_path.exists():
        print(f"[{slug}] ERROR: {ja_path.name} not found.")
        return
    if not en_path.exists():
        print(f"[{slug}] ERROR: {en_path.name} not found — run md_to_english_json.py first.")
        return

    ja_data = json.loads(ja_path.read_text(encoding="utf-8"))
    en_data = json.loads(en_path.read_text(encoding="utf-8"))
    pages: list[dict] = ja_data["pages"]
    en_paras: list[str] = en_data["paragraphs"]
    n_en = len(en_paras)
    n_pages = len(pages)

    if n_pages == 0:
        print(f"[{slug}] ERROR: no pages in JA JSON.")
        return
    if n_en == 0:
        print(f"[{slug}] WARNING: English JSON has 0 paragraphs — generating empty skeleton.")

    # Weight pages by JA character count so longer pages get more English paras.
    weights = []
    for page in pages:
        char_count = sum(len(p) for p in (page.get("paragraphs") or []))
        weights.append(max(char_count, 1))
    total_weight = sum(weights)

    # Proportional assignment (floor), then distribute remainder to pages with
    # the largest fractional surplus.
    assignments = [0] * n_pages
    fracs: list[tuple[float, int]] = []
    for i, w in enumerate(weights):
        exact = (w / total_weight) * n_en
        assignments[i] = int(exact)
        fracs.append((exact - int(exact), i))

    remainder = n_en - sum(assignments)
    fracs.sort(reverse=True)
    for j in range(remainder):
        assignments[fracs[j][1]] += 1

    # Build aligned pages: one segment per JA page.
    aligned_pages: dict[str, list[dict]] = {}
    en_idx = 0
    for page, n_assigned in zip(pages, assignments):
        key = page["page_he"]
        ja_text = " ".join(page.get("paragraphs") or [])
        en_slice = en_paras[en_idx : en_idx + n_assigned]
        en_idx += n_assigned
        en_text = "\n\n".join(en_slice)
        aligned_pages[key] = [
            {"ja": ja_text, "en": en_text, "isHeader": False, "pairs": []}
        ]

    result = {
        "note": (
            f"Skeleton alignment for bahya-{slug}. "
            f"One segment per JA page; pairs are empty. "
            f"Edit: split segments to paragraph level, then add phrase pairs."
        ),
        "pages": aligned_pages,
    }

    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"[{slug}] wrote skeleton → {out_path.name}  "
        f"({n_pages} pages, {n_en} English paras)"
    )


def main() -> None:
    slugs = sys.argv[1:]
    if not slugs:
        sys.exit(
            "usage: skeleton_align.py <slug> [<slug> ...]   e.g. bab7 hakdamah"
        )
    for slug in slugs:
        process_slug(slug)


if __name__ == "__main__":
    main()

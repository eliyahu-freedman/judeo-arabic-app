#!/usr/bin/env python3
"""
Walk the Emunot v'Deot page chain and emit a structured manifest grouping
pages by maamar + fusul (FJMS parentUnits). Outputs:
  data-source/saadia-emunot/page-manifest.json   — ordered list of pages
  data-source/saadia-emunot/chapter-map.txt       — human-readable chapter breakdown
"""
import json
import os
import re
from pathlib import Path

PAGES_DIR = Path(__file__).parent.parent / "data-source" / "saadia-emunot" / "pages"
OUT_DIR   = PAGES_DIR.parent

# Maamar IDs from toc.json
MAAMAR_IDS = {
    15731: ("intro",   "הקדמה",           "Introduction"),
    15740: ("maamar1", "מאמר א",          "Maamar I: Creation"),
    15746: ("maamar2", "מאמר ב",          "Maamar II: God's Unity"),
    15761: ("maamar3", "מאמר ג",          "Maamar III: Command & Prohibition"),
    15773: ("maamar4", "מאמר ד",          "Maamar IV: Obedience & Free Will"),
    15781: ("maamar5", "מאמר ה",          "Maamar V: Merits & Debts"),
    15790: ("maamar6", "מאמר ו",          "Maamar VI: The Soul"),
    15799: ("maamar7", "מאמר ז",          "Maamar VII: Resurrection"),
    15809: ("maamar8", "מאמר ח",          "Maamar VIII: Salvation"),
    15819: ("maamar9", "מאמר ט",          "Maamar IX: Reward & Punishment"),
    15831: ("maamar10","מאמר י",          "Maamar X: Ethics"),
    15853: ("appendix","נספח",            "Appendix"),
}

# --- Load all pages keyed by curr ---
pages_by_curr: dict[str, dict] = {}
for f in PAGES_DIR.glob("*.json"):
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
        curr = d.get("curr", "")
        if curr:
            pages_by_curr[curr] = d
    except Exception as e:
        print(f"WARN: {f.name}: {e}")

print(f"Loaded {len(pages_by_curr)} pages")

# --- Walk the chain from page א ---
ordered: list[dict] = []
visited: set[str] = set()
# Find start: page with no prev
start = None
for pg in pages_by_curr.values():
    if not pg.get("prev"):
        start = pg["curr"]
        break

if not start:
    raise RuntimeError("Could not find start page (no prev)")

curr_key = start
while curr_key and curr_key not in visited:
    pg = pages_by_curr.get(curr_key)
    if not pg:
        print(f"WARN: missing page {curr_key!r}")
        break
    visited.add(curr_key)
    ordered.append(pg)
    curr_key = pg.get("next", "")

print(f"Chain length: {len(ordered)} pages (of {len(pages_by_curr)} loaded)")

# --- Build manifest: one entry per page ---
manifest = []
for pg in ordered:
    units = pg.get("parentUnits", [])
    maamar_id = int(units[0]) if units else None
    fusul_id  = int(units[1]) if len(units) > 1 else None

    maamar_info = MAAMAR_IDS.get(maamar_id, ("unknown", "?", "?")) if maamar_id else ("unknown", "?", "?")

    manifest.append({
        "page_he":   pg["curr"],
        "maamar_id": maamar_id,
        "maamar_slug": maamar_info[0],
        "maamar_he": maamar_info[1],
        "maamar_en": maamar_info[2],
        "fusul_id":  fusul_id,
        "cleanedText": pg.get("cleanedText", "").replace("\r\n", "\n").strip(),
    })

out_manifest = OUT_DIR / "page-manifest.json"
out_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {out_manifest}")

# --- Build chapter map ---
# Group pages by (maamar_id, fusul_id)
from collections import defaultdict, OrderedDict

# Preserve chapter order by first-seen
chapters: list[tuple] = []  # (maamar_id, fusul_id)
chapter_pages: dict[tuple, list] = defaultdict(list)
for entry in manifest:
    key = (entry["maamar_id"], entry["fusul_id"])
    if key not in chapter_pages:
        chapters.append(key)
    chapter_pages[key].append(entry["page_he"])

# Extract fusul number from cleanedText (looks for "פרק. א." or "פרק א" at start)
def guess_fusul_title(pages_list):
    """Return (num_label, title_hint) from the first page of a fusul."""
    for page_he in pages_list:
        text = pages_by_curr[page_he].get("cleanedText", "")
        # Look for header lines like "פרק. א." or "פרק א" or "פרק ב"
        m = re.search(r'פרק[. ]+([א-ת]+)', text)
        if m:
            return m.group(1)
    return "?"

lines = []
current_maamar = None
fusul_counter = 0
global_chapter = 0

for key in chapters:
    maamar_id, fusul_id = key
    pgs = chapter_pages[key]
    maamar_info = MAAMAR_IDS.get(maamar_id, ("?","?","?"))

    if maamar_id != current_maamar:
        lines.append("")
        lines.append(f"=== {maamar_info[1]} ({maamar_info[2]}) [FJMS id={maamar_id}] ===")
        current_maamar = maamar_id
        fusul_counter = 0

    fusul_counter += 1
    global_chapter += 1
    fusul_he = guess_fusul_title(pgs)
    page_range = f"{pgs[0]}–{pgs[-1]}" if len(pgs) > 1 else pgs[0]
    lines.append(
        f"  ch{global_chapter:03d}  fusul={fusul_id or 'none':>6}  "
        f"he={fusul_he:<4}  pages={page_range}  ({len(pgs)} pp)"
    )

out_map = OUT_DIR / "chapter-map.txt"
out_map.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {out_map}")
print(f"\nTotal chapters: {global_chapter}")

# Print summary by maamar
print("\nChapters per maamar:")
maamar_counts: dict[int, int] = {}
for key in chapters:
    mid, _ = key
    maamar_counts[mid] = maamar_counts.get(mid, 0) + 1
for mid, cnt in maamar_counts.items():
    info = MAAMAR_IDS.get(mid, ("?","?","?"))
    print(f"  {info[1]}: {cnt} fuṣūl")

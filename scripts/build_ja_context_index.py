#!/usr/bin/env python3
"""Build /tmp/ja-context-index.json — for each JA surface token appearing in
the tafsir corpus, list up to 3 example occurrences as (book, chapter, verse,
ja_text).

Mirrors generate_lane_entries.py:build_context_index() but emits a standalone
JSON file for offline (no-API) lookups during the inline Batch G sweep.

The index is keyed by RAW surface (no prefix-strip) so we can look up the
exact surface form returned by coverage_report.py. Each value is a list of up
to 3 hit dicts.
"""
import collections, json, pathlib, re

DATA = pathlib.Path(__file__).resolve().parent.parent / "data"
TOKEN_RE = re.compile(r"[א-ת']+")
MAX_HITS = 3

idx: dict[str, list] = collections.defaultdict(list)

for fp in sorted(DATA.glob("tafsir-*-*.json")):
    name = fp.name
    if "-english" in name or "-alignment" in name:
        continue
    m = re.match(r"tafsir-([a-z]+)-(\d+)\.json$", name)
    if not m:
        continue
    book, ch = m.group(1), int(m.group(2))
    try:
        d = json.loads(fp.read_text(encoding="utf-8"))
    except Exception:
        continue
    for v in d.get("verses", []):
        text = (v.get("ja") or "").strip()
        if not text:
            continue
        vnum = v.get("v")
        seen_in_verse = set()
        for tok in TOKEN_RE.findall(text):
            if tok in seen_in_verse:
                continue
            seen_in_verse.add(tok)
            if len(idx[tok]) < MAX_HITS:
                idx[tok].append({
                    "book": book, "ch": ch, "v": vnum, "text": text,
                })

out_path = pathlib.Path("/tmp/ja-context-index.json")
out_path.write_text(json.dumps(idx, ensure_ascii=False, indent=1))
print(f"Wrote {len(idx)} surface tokens → {out_path}")
print(f"Sample 5 tokens with hit-counts:")
for tok in list(idx.keys())[:5]:
    print(f"  {tok!r:15s} → {len(idx[tok])} hits")

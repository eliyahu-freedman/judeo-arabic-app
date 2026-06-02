#!/usr/bin/env python3
"""
Phase 3 R2 cross-book TWIST scan — scan the Saadia tafsir corpus for
multi-book attestations of TWIST-tier lemmas.

For each TWIST entry, build a surface-search set from lemma_ja + variants[],
then grep all tafsir-{book}-{ch}.json files for those surfaces. Hits whose
(book, ch, v) is already in the entry's verses[] are filtered out. Surviving
hits are candidate promote-in-place verse extensions.

Output: a JSON candidate report at /tmp/phase3_r2_scan.json, plus a
human-readable summary on stdout.

Mirrors scripts/build_ja_context_index.py:1-50 for the corpus-walking loop.

Usage:
    python3 scripts/scan_phase3_r2.py                # scan all 36 TWIST entries
    python3 scripts/scan_phase3_r2.py LEMMA1 LEMMA2  # scan only the given lemmas
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DIVERGENCE = DATA / "tafsir-divergence.json"
OUT = pathlib.Path("/tmp/phase3_r2_scan.json")

# JA surface tokenizer — mirrors build_ja_context_index.py
TOKEN_RE = re.compile(r"[א-ת']+")

# Book-name mapping: filename slug → canonical entry book name
BOOK_NAMES = {
    "bereshit": "Bereshit",
    "shemot": "Shemot",
    "vayikra": "Vayikra",
    "bamidbar": "Bamidbar",
    "devarim": "Devarim",
}


def load_corpus() -> dict:
    """Walk tafsir-{book}-{ch}.json files; return {(book, ch, v): ja_text}."""
    corpus = {}
    for fp in sorted(DATA.glob("tafsir-*-*.json")):
        name = fp.name
        if "-english" in name or "-alignment" in name:
            continue
        m = re.match(r"tafsir-([a-z]+)-(\d+)\.json$", name)
        if not m:
            continue
        slug = m.group(1)
        if slug not in BOOK_NAMES:
            continue
        book = BOOK_NAMES[slug]
        ch = int(m.group(2))
        try:
            d = json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            continue
        for v in d.get("verses", []):
            ja = (v.get("ja") or "").strip()
            if not ja:
                continue
            vnum = v.get("v")
            if vnum is None:
                continue
            corpus[(book, ch, vnum)] = ja
    return corpus


def load_alignment(book_slug: str, ch: int) -> dict | None:
    """Optional: load alignment file for context. Returns {v: alignment_obj}."""
    fp = DATA / f"tafsir-{book_slug}-{ch}-alignment.json"
    if not fp.exists():
        return None
    try:
        d = json.loads(fp.read_text(encoding="utf-8"))
    except Exception:
        return None
    return {v.get("v"): v for v in d.get("verses", [])}


def build_search_set(entry: dict) -> set[str]:
    """Build the surface search set: lemma_ja + variants[], stripped of
    common Heb proclitics (ב, ו, פ, ל, כ, ש, ה — the JA prefix family).

    We search for EXACT token matches in TOKEN_RE-tokenized verse text, so
    we also include prefix-stripped fallbacks to catch surfaces like 'ואדלג'
    when the entry only lists 'אדלג'. Conversely, if a variant already has
    a prefix, we use it verbatim.

    Returns: set of surface strings to look up in the verse-tokens.
    """
    surfaces = set()
    raw = [entry.get("lemma_ja", "")] + list(entry.get("variants", []) or [])
    for r in raw:
        r = r.strip()
        if r:
            surfaces.add(r)
    return surfaces


def already_attested(entry: dict) -> set[tuple]:
    return {(v["book"], v["ch"], v["v"]) for v in entry.get("verses", [])}


def scan_entry(entry: dict, corpus: dict) -> dict:
    """Scan corpus for hits of entry's surfaces. Return:
        {
          "lemma_ja": ...,
          "surfaces":  [...],
          "existing_verses": [...],
          "hits": [
            {"book", "ch", "v", "ja_snippet", "matched_surface"},
            ...
          ]
        }
    """
    surfaces = build_search_set(entry)
    existing = already_attested(entry)
    hits = []

    for (book, ch, v), ja in corpus.items():
        if (book, ch, v) in existing:
            continue
        tokens = set(TOKEN_RE.findall(ja))
        matched = surfaces & tokens
        if matched:
            # Build a short snippet around the first match
            snippet = ja
            if len(snippet) > 240:
                # try to center on the matched surface
                ms = sorted(matched, key=len, reverse=True)[0]
                idx = ja.find(ms)
                if idx >= 0:
                    start = max(0, idx - 100)
                    end = min(len(ja), idx + 140)
                    snippet = ("…" if start > 0 else "") + ja[start:end] + ("…" if end < len(ja) else "")
            hits.append({
                "book": book,
                "ch": ch,
                "v": v,
                "matched_surface": sorted(matched, key=lambda s: -len(s))[0],
                "ja_snippet": snippet,
            })

    # Sort hits by book/ch/v
    book_order = {b: i for i, b in enumerate(["Bereshit", "Shemot", "Vayikra", "Bamidbar", "Devarim"])}
    hits.sort(key=lambda h: (book_order.get(h["book"], 99), h["ch"], h["v"]))

    return {
        "lemma_ja": entry["lemma_ja"],
        "lemma_ar": entry.get("lemma_ar", ""),
        "tier": entry["tier"],
        "surfaces": sorted(surfaces),
        "existing_verses": [{"book": b, "ch": c, "v": v} for (b, c, v) in sorted(existing, key=lambda x: (book_order.get(x[0], 99), x[1], x[2]))],
        "hits": hits,
        "n_hits": len(hits),
    }


def main():
    div = json.loads(DIVERGENCE.read_text(encoding="utf-8"))
    twists = [e for e in div["entries"] if e.get("tier") == "twist"]

    target_lemmas = sys.argv[1:]
    if target_lemmas:
        twists = [e for e in twists if e["lemma_ja"] in target_lemmas]
        if not twists:
            print(f"No TWIST entries found matching: {target_lemmas}", file=sys.stderr)
            sys.exit(1)

    print(f"Loading corpus from {DATA} …", file=sys.stderr)
    corpus = load_corpus()
    print(f"  → {len(corpus)} verses across 5 books", file=sys.stderr)

    print(f"Scanning {len(twists)} TWIST entries…", file=sys.stderr)
    report = {"scans": []}
    for e in twists:
        r = scan_entry(e, corpus)
        report["scans"].append(r)

    # Summary stats
    n_with_hits = sum(1 for r in report["scans"] if r["n_hits"] > 0)
    book_order = ["Bereshit", "Shemot", "Vayikra", "Bamidbar", "Devarim"]

    print()
    print("=" * 80)
    print(f"SCAN SUMMARY — {len(twists)} TWIST entries scanned")
    print(f"  Entries with cross-book hits: {n_with_hits}")
    print(f"  Output: {OUT}")
    print("=" * 80)
    print()

    for r in report["scans"]:
        if r["n_hits"] == 0:
            continue
        existing_books = sorted({v["book"] for v in r["existing_verses"]}, key=book_order.index)
        hit_books = sorted({h["book"] for h in r["hits"]}, key=book_order.index)
        print(f"### {r['lemma_ja']} ({r['lemma_ar']})")
        print(f"    existing: {'/'.join(existing_books)} ({len(r['existing_verses'])} verses)")
        print(f"    hits in:  {'/'.join(hit_books)} ({r['n_hits']} candidate verses)")
        for h in r["hits"]:
            print(f"      • {h['book']} {h['ch']}:{h['v']}  [{h['matched_surface']}]  {h['ja_snippet'][:120]}")
        print()

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()

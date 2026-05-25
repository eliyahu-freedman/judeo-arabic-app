"""Reproducible dictionary-coverage report + authoring queue.

Reads public/corpus-index.json (the committed JA token frequency index) plus the
three dictionary JSONs and tafsir-divergence.json, then classifies every JA token
EXACTLY the way lib/lookup.ts#lookup would at runtime (full composable prefix
chain + normalizeFinals + variants), token-weighted.

Outputs:
  - stdout: token-weighted coverage (hand-only / hand+auto / miss), divergence
    overlay count, and the miss breakdown by bucket.
  - data/coverage-misses.json: misses with count >= MIN_FREQ, sorted desc, each
    with surfaces + a couple of example {ch,v} occurrences + a coarse bucket.
    This is the durable authoring queue (replaces the ephemeral /tmp file).

Run:  python3 scripts/coverage_report.py [--min-freq 10]

No API, fully deterministic.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
PUBLIC = REPO / "public"

PREFIXES = ["ב", "ל", "כ", "פ"]


# --- normalization mirrors lib/lookup.ts -----------------------------------

def strip_punct(tok: str) -> str:
    return tok.strip(".,:;؛،\"' \t\n")


def normalize_finals(s: str) -> str:
    """final<->medial letter fold + trailing-apostrophe strip. Mirrors normalizeFinals."""
    r = (
        s.replace("ך", "כ")
        .replace("ם", "מ")
        .replace("ן", "נ")
        .replace("ף", "פ")
        .replace("ץ", "צ")
    )
    if r.endswith("'"):
        r = r[:-1]
    return r


def normalize_token(raw: str) -> str:
    """Mirrors normalizeToken: strip punct, leading vav, leading al-."""
    t = strip_punct(raw)
    if t.startswith("ו") and len(t) > 1:
        t = t[1:]
    if t.startswith("אל") and len(t) > 2:
        t = t[2:]
    return t


def candidate_chain(raw: str) -> set[str]:
    """Mirrors the composable candidate generation in lib/lookup.ts#lookup."""
    tok = strip_punct(raw)
    tries: set[str] = set()

    def with_al(s: str) -> None:
        if not s:
            return
        tries.add(s)
        if s.startswith("אל") and len(s) > 2:
            tries.add(s[2:])

    with_al(tok)
    after_vav = None
    if tok.startswith("ו") and len(tok) > 1:
        after_vav = tok[1:]
        with_al(after_vav)
    for base in [b for b in (tok, after_vav) if b]:
        for p in PREFIXES:
            if base.startswith(p) and len(base) > 1:
                with_al(base[1:])
    return tries


# --- dictionary key sets ----------------------------------------------------

def load_keysets() -> tuple[set[str], set[str], set[str]]:
    """Return (starter_keys, lane_keys, auto_keys), keys normalizeFinals-folded
    where the runtime folds them (starter/lane), raw lemma for auto."""
    def hand_keys(path: Path) -> set[str]:
        d = json.loads(path.read_text(encoding="utf-8"))
        keys: set[str] = set()
        for e in d["entries"]:
            keys.add(normalize_finals(e["lemma_ja"]))
            for v in e.get("variants", []):
                keys.add(normalize_finals(v))
        return keys

    starter = hand_keys(DATA / "dictionary-starter.json")
    lane = hand_keys(DATA / "dictionary-lane.json")
    auto_d = json.loads((DATA / "dictionary-auto.json").read_text(encoding="utf-8"))
    auto = {e["lemma_ja"] for e in auto_d["entries"]}
    return starter, lane, auto


def load_divergence_keys() -> set[str]:
    d = json.loads((DATA / "tafsir-divergence.json").read_text(encoding="utf-8"))
    keys: set[str] = set()
    for e in d["entries"]:
        keys.add(normalize_finals(e["lemma_ja"]))
        for v in e.get("variants", []):
            keys.add(normalize_finals(v))
    return keys


def classify(surface: str, starter: set[str], lane: set[str], auto: set[str]) -> str:
    cands = candidate_chain(surface)
    norm = cands | {normalize_finals(c) for c in cands}
    if norm & starter:
        return "starter"
    if norm & lane:
        return "lane"
    if normalize_token(surface) in auto:
        return "auto"
    return "miss"


def has_divergence(surface: str, dkeys: set[str]) -> bool:
    cands = candidate_chain(surface)
    norm = cands | {normalize_finals(c) for c in cands}
    return bool(norm & dkeys)


def bucket(surface: str) -> str:
    if any(c in surface for c in "[]{}()0123456789") or len(surface) <= 1:
        return "ocr-junk"
    if surface.startswith("ו"):
        return "w-prefixed"  # may only need a variant on an existing stem
    if "'" in surface:
        return "has-apostrophe"
    return "standard"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-freq", type=int, default=10)
    args = ap.parse_args()

    index = json.loads((PUBLIC / "corpus-index.json").read_text(encoding="utf-8"))
    starter, lane, auto = load_keysets()
    dkeys = load_divergence_keys()

    # Per-surface frequency from occurrences ([ch, v, s_idx]).
    # Classify each distinct surface once (memoized), tally token-weighted.
    cls_cache: dict[str, str] = {}
    div_cache: dict[str, bool] = {}
    tally = Counter()  # classification -> token count
    div_tokens = 0
    miss_surfaces: dict[str, dict] = {}  # surface -> {count, example_occ}

    for key, b in index["tokens"].items():
        surfaces = b["surfaces"]
        per_surface = Counter(occ[2] for occ in b["occurrences"])
        # map a surface index to one example occurrence
        first_occ: dict[int, list] = {}
        for occ in b["occurrences"]:
            first_occ.setdefault(occ[2], occ)
        for s_idx, n in per_surface.items():
            surface = surfaces[s_idx]
            c = cls_cache.get(surface)
            if c is None:
                c = classify(surface, starter, lane, auto)
                cls_cache[surface] = c
            tally[c] += n
            d = div_cache.get(surface)
            if d is None:
                d = has_divergence(surface, dkeys)
                div_cache[surface] = d
            if d:
                div_tokens += n
            if c == "miss":
                rec = miss_surfaces.setdefault(
                    surface, {"count": 0, "examples": [], "bucket": bucket(surface)}
                )
                rec["count"] += n
                if len(rec["examples"]) < 2:
                    occ = first_occ[s_idx]
                    rec["examples"].append({"ch": occ[0], "v": occ[1]})

    total = sum(tally.values())
    hand = tally["starter"] + tally["lane"]
    hand_auto = hand + tally["auto"]
    miss = tally["miss"]

    def pct(n: int) -> str:
        return f"{100 * n / total:.2f}%"

    print(f"total JA tokens classified: {total}")
    print(f"  starter : {tally['starter']:>7}  ({pct(tally['starter'])})")
    print(f"  lane    : {tally['lane']:>7}  ({pct(tally['lane'])})")
    print(f"  auto    : {tally['auto']:>7}  ({pct(tally['auto'])})")
    print(f"  MISS    : {miss:>7}  ({pct(miss)})")
    print(f"hand coverage (starter+lane): {pct(hand)}")
    print(f"total coverage (hand+auto)  : {pct(hand_auto)}")
    print(f"divergence overlay touches  : {div_tokens} tokens ({pct(div_tokens)})")

    # Authoring queue: misses with count >= min-freq, sorted desc.
    queue = sorted(
        (
            {"surface": s, "count": r["count"], "bucket": r["bucket"], "examples": r["examples"]}
            for s, r in miss_surfaces.items()
            if r["count"] >= args.min_freq
        ),
        key=lambda x: -x["count"],
    )
    bucket_counts = Counter(item["bucket"] for item in queue)
    queue_tokens = sum(item["count"] for item in queue)
    print()
    print(f"miss surfaces with count >= {args.min_freq}: {len(queue)} "
          f"({queue_tokens} tokens, {pct(queue_tokens)})")
    for bname, bn in bucket_counts.most_common():
        print(f"  {bname:<14}: {bn}")

    out_path = DATA / "coverage-misses.json"
    out_path.write_text(
        json.dumps(
            {
                "_note": "Authoring queue: JA tokens that resolve to no hand/auto "
                "dict entry, freq >= min_freq. Generated by scripts/coverage_report.py.",
                "min_freq": args.min_freq,
                "total_tokens": total,
                "hand_coverage_pct": round(100 * hand / total, 2),
                "total_coverage_pct": round(100 * hand_auto / total, 2),
                "queue": queue,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"\nwrote {out_path.relative_to(REPO)} ({len(queue)} entries)")


if __name__ == "__main__":
    main()

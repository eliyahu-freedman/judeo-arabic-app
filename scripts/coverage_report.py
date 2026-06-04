#!/usr/bin/env python3
"""
Tafsir dictionary coverage report.

For every chapter file under `data/tafsir-*.json` (excluding the *-english,
*-alignment, *-divergence sidecars), tokenise the `ja` text via the canonical
TS tokeniser at `scripts/_tokenize_ja_cli.ts`, run each word through the same
prefix-strip chain as `lib/lookup.ts:lookup`, and bucket the result as:

  - hand-hit    : matched a lemma or variant in starter or lane
  - auto-hit    : matched the Camel-tools auto dict only (via normalizeToken)
  - miss        : no entry

Writes two artifacts:

  data/coverage-snapshot.json   totals + per-book breakdown + top-500 misses
  data/coverage-misses.json     top-1000 misses bucketed for curation batches

Prints a one-page summary to stdout. Run before/after each Phase 2 curation
round to confirm the delta.

Tokeniser parity is guaranteed by calling the TS CLI rather than re-porting
the regex. Lookup-chain parity is maintained by mirroring the TS chain in
this file; if `lib/lookup.ts` changes, update `lookup()` here in lock-step.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TOKENIZE_CLI = ROOT / "scripts" / "_tokenize_ja_cli.ts"

# Books in canonical order; chapter files are `tafsir-{book}-{N}.json`.
BOOKS = ["bereshit", "shemot", "vayikra", "bamidbar", "devarim"]

# ---------- Dictionary loading ---------------------------------------------

PREFIXES = ("ב", "ל", "כ", "פ")


def strip_punct(tok: str) -> str:
    # Mirrors `stripPunct` in lib/lookup.ts.
    return re.sub(r"^[.,:;؛،\"'\s]+|[.,:;؛،\"'\s]+$", "", tok)


def normalize_finals(s: str) -> str:
    # Mirrors `normalizeFinals` in lib/lookup.ts.
    s = re.sub(r"[֑-ׇ]", "", s)  # drop Hebrew points (niqqud/teʿamim)
    s = (
        s.replace("ך", "כ")
        .replace("ם", "מ")
        .replace("ן", "נ")
        .replace("ף", "פ")
        .replace("ץ", "צ")
    )
    if s.endswith("'"):
        s = s[:-1]
    return s


def normalize_token(raw: str) -> str:
    # Mirrors `normalizeToken` in lib/lookup.ts (used for the auto-dict key).
    t = strip_punct(raw)
    if t.startswith("ו") and len(t) > 1:
        t = t[1:]
    if t.startswith("אל") and len(t) > 2:
        t = t[2:]
    return t


def candidate_chain(raw: str) -> list[str]:
    """Composable candidate chain mirroring `lib/lookup.ts:lookup`."""
    tok = strip_punct(raw)
    if not tok:
        return []

    tries: set[str] = set()

    def with_al(s: str) -> None:
        if not s:
            return
        tries.add(s)
        if s.startswith("אל") and len(s) > 2:
            tries.add(s[2:])

    # Layer 1: the token itself.
    with_al(tok)

    # Layer 2: strip leading ו.
    after_vav: str | None = None
    if tok.startswith("ו") and len(tok) > 1:
        after_vav = tok[1:]
        with_al(after_vav)

    # Layer 3: strip a single-letter prep [ב ל כ פ] from tok and after-vav.
    for base in [tok, after_vav]:
        if not base:
            continue
        for p in PREFIXES:
            if base.startswith(p) and len(base) > 1:
                with_al(base[1:])

    # Final-letter normalisation expansion.
    base_list = list(tries)
    return list({*base_list, *(normalize_finals(t) for t in base_list)})


def load_dict_index(path: Path) -> tuple[set[str], int]:
    """Return (set of normalized lemmas+variants, raw entry count)."""
    obj = json.loads(path.read_text())
    entries = obj.get("entries", [])
    keys: set[str] = set()
    for e in entries:
        lemma = e.get("lemma_ja")
        if lemma:
            keys.add(normalize_finals(lemma))
        for v in e.get("variants", []) or []:
            keys.add(normalize_finals(v))
    return keys, len(entries)


def load_auto_index(path: Path) -> tuple[set[str], int]:
    """Auto dict is keyed by `normalizeToken(rawToken)` against `lemma_ja`."""
    obj = json.loads(path.read_text())
    entries = obj.get("entries", [])
    keys = {e["lemma_ja"] for e in entries if e.get("lemma_ja")}
    return keys, len(entries)


def lookup_bucket(
    raw: str, starter: set[str], lane: set[str], auto: set[str]
) -> str:
    """Return 'hand-starter' | 'hand-lane' | 'auto' | 'miss'."""
    tok = strip_punct(raw)
    if not tok:
        return "miss"
    chain = candidate_chain(raw)
    for c in chain:
        if c in starter:
            return "hand-starter"
    for c in chain:
        if c in lane:
            return "hand-lane"
    if normalize_token(raw) in auto:
        return "auto"
    return "miss"


# ---------- Corpus tokenisation -------------------------------------------


def list_chapter_files() -> list[Path]:
    """All tafsir-*.json source files, sorted, excluding sidecars."""
    out: list[Path] = []
    for p in sorted(DATA.glob("tafsir-*.json")):
        name = p.name
        if (
            name.endswith("-english.json")
            or name.endswith("-alignment.json")
            or name == "tafsir-divergence.json"
        ):
            continue
        out.append(p)
    return out


def chunked(xs: list, n: int) -> Iterable[list]:
    for i in range(0, len(xs), n):
        yield xs[i : i + n]


def tokenise_via_cli(strings: list[str]) -> list[list[str]]:
    """Send strings as JSONL to the TS CLI; return parallel list of word arrays."""
    if not strings:
        return []
    payload = "\n".join(json.dumps({"text": s}) for s in strings) + "\n"
    proc = subprocess.run(
        ["npx", "tsx", str(TOKENIZE_CLI), "--words"],
        input=payload,
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise RuntimeError("tokeniser CLI failed")
    out: list[list[str]] = []
    for line in proc.stdout.splitlines():
        if not line:
            out.append([])
            continue
        out.append(json.loads(line))
    if len(out) != len(strings):
        raise RuntimeError(
            f"CLI returned {len(out)} lines for {len(strings)} inputs"
        )
    return out


def book_of(path: Path) -> str:
    # tafsir-bereshit-12.json -> bereshit
    m = re.match(r"^tafsir-([a-z]+)-\d+\.json$", path.name)
    return m.group(1) if m else "unknown"


# ---------- Miss bucketing ------------------------------------------------


def miss_bucket(tok: str) -> str:
    """Coarse bucket for curation triage."""
    if not tok:
        return "empty"
    if tok.startswith("ו"):
        return "w-prefixed"
    if "'" in tok[:-1]:  # apostrophe inside the word marks a rare consonant
        return "has-apostrophe"
    return "standard"


# ---------- Main ----------------------------------------------------------


def main() -> int:
    # Load dicts.
    starter_keys, starter_n = load_dict_index(DATA / "dictionary-starter.json")
    lane_keys, lane_n = load_dict_index(DATA / "dictionary-lane.json")
    auto_keys, auto_n = load_auto_index(DATA / "dictionary-auto.json")
    sys.stderr.write(
        f"loaded dicts: starter={starter_n} ({len(starter_keys)} keys), "
        f"lane={lane_n} ({len(lane_keys)} keys), auto={auto_n}\n"
    )

    # Gather all `ja` strings per chapter file.
    chapter_files = list_chapter_files()
    sys.stderr.write(f"found {len(chapter_files)} chapter files\n")

    per_book: dict[str, Counter] = {}
    overall = Counter()
    miss_counter: Counter = Counter()
    total_tokens = 0
    total_word_tokens = 0  # excluding empty-after-stripPunct

    for cf in chapter_files:
        book = book_of(cf)
        obj = json.loads(cf.read_text())
        ja_strings = [v.get("ja", "") for v in obj.get("verses", []) if v.get("ja")]
        # Tokenise in chunks to keep stdout pipes manageable.
        for chunk in chunked(ja_strings, 64):
            word_lists = tokenise_via_cli(chunk)
            for words in word_lists:
                for w in words:
                    total_tokens += 1
                    tok = strip_punct(w)
                    if not tok:
                        continue
                    total_word_tokens += 1
                    bucket = lookup_bucket(w, starter_keys, lane_keys, auto_keys)
                    overall[bucket] += 1
                    per_book.setdefault(book, Counter())[bucket] += 1
                    if bucket == "miss":
                        # Key the miss on the stripped surface form so trailing
                        # punctuation doesn't fragment the count.
                        miss_counter[tok] += 1

    # Compose snapshot artifact.
    def pct(n: int, d: int) -> float:
        return round(100 * n / d, 2) if d else 0.0

    def tier_breakdown(counter: Counter) -> dict:
        n = sum(counter.values())
        hand = counter["hand-starter"] + counter["hand-lane"]
        auto_hits = counter["auto"]
        miss = counter["miss"]
        return {
            "tokens": n,
            "hand_starter": counter["hand-starter"],
            "hand_lane": counter["hand-lane"],
            "hand_total": hand,
            "auto": auto_hits,
            "miss": miss,
            "hand_pct": pct(hand, n),
            "auto_pct": pct(auto_hits, n),
            "covered_pct": pct(hand + auto_hits, n),
            "miss_pct": pct(miss, n),
        }

    snapshot = {
        "_generated": "scripts/coverage_report.py",
        "_total_raw_tokens": total_tokens,
        "_total_word_tokens": total_word_tokens,
        "totals": tier_breakdown(overall),
        "by_book": {
            book: tier_breakdown(c)
            for book, c in sorted(per_book.items(), key=lambda kv: BOOKS.index(kv[0]) if kv[0] in BOOKS else 99)
        },
        "top_misses": [
            {"surface": tok, "count": n, "bucket": miss_bucket(tok)}
            for tok, n in miss_counter.most_common(500)
        ],
    }
    (DATA / "coverage-snapshot.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2)
    )

    # Misses file for curation.
    misses_doc = {
        "_generated": "scripts/coverage_report.py",
        "_total_unique_misses": len(miss_counter),
        "_total_miss_occurrences": sum(miss_counter.values()),
        "misses": [
            {"surface": tok, "count": n, "bucket": miss_bucket(tok)}
            for tok, n in miss_counter.most_common(1000)
        ],
    }
    (DATA / "coverage-misses.json").write_text(
        json.dumps(misses_doc, ensure_ascii=False, indent=2)
    )

    # Stdout summary.
    t = snapshot["totals"]
    print(f"\nTafsir dictionary coverage report")
    print(f"=================================")
    print(f"Word tokens (after stripPunct):  {t['tokens']:>7,}")
    print(f"Hand-starter hits:               {t['hand_starter']:>7,}  ({pct(t['hand_starter'], t['tokens'])}%)")
    print(f"Hand-lane hits:                  {t['hand_lane']:>7,}  ({pct(t['hand_lane'], t['tokens'])}%)")
    print(f"Hand TOTAL:                      {t['hand_total']:>7,}  ({t['hand_pct']}%)")
    print(f"Auto (Camel) hits:               {t['auto']:>7,}  ({t['auto_pct']}%)")
    print(f"COVERED:                         {t['hand_total'] + t['auto']:>7,}  ({t['covered_pct']}%)")
    print(f"Misses:                          {t['miss']:>7,}  ({t['miss_pct']}%)")
    print()
    print(f"Per-book hand-coverage:")
    for book in BOOKS:
        if book in snapshot["by_book"]:
            b = snapshot["by_book"][book]
            print(f"  {book:>9}:  hand={b['hand_pct']}%   covered={b['covered_pct']}%   miss={b['miss_pct']}%   ({b['tokens']:,} tokens)")
    print()
    print(f"Unique miss surface forms:       {len(miss_counter):,}")
    print(f"Total miss occurrences:          {sum(miss_counter.values()):,}")
    print()
    print(f"Top 15 misses:")
    for tok, n in miss_counter.most_common(15):
        print(f"  {n:>4}  {tok}  [{miss_bucket(tok)}]")
    print()
    print(f"Wrote {DATA / 'coverage-snapshot.json'}")
    print(f"Wrote {DATA / 'coverage-misses.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Verifier for `data/tafsir-divergence.json`.

Runs three integrity checks across every entry:

1. *Citation resolvability* — every verse in `entry.verses[]` is tokenised
   via the canonical TS tokeniser at `scripts/_tokenize_ja_cli.ts`. At
   least one resulting word, after running the same prefix-strip chain as
   `lib/divergence.ts:lookupDivergence`, must equal the entry's
   `lemma_ja` or one of `entry.variants[]` (after `normalizeFinals`).
   Catches typos in lemma/variants and broken verse pointers.

2. *Sources legend integrity* — every string in `entry.sources[]` must be
   a key in the top-level `_sources` legend object. No zero-source entries.

3. *Per-book relation mix* (Phase 3 quality bar from the plan):
   ≥70% Blau-backed (direct + adjacent), ≥45% direct, ≤30% no-citation,
   *per book*. Currently only enforced as a soft warning — flips to a
   failing assertion once Phase 3 lands its first full book.

Exit code 0 if all entries pass; non-zero with a per-failure report
otherwise. Re-runnable; idempotent.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TOKENIZE_CLI = ROOT / "scripts" / "_tokenize_ja_cli.ts"

PREFIXES = ("ב", "ל", "כ", "פ")


def strip_punct(tok: str) -> str:
    return re.sub(r"^[.,:;؛،\"'\s]+|[.,:;؛،\"'\s]+$", "", tok)


def normalize_finals(s: str) -> str:
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
    t = strip_punct(raw)
    if t.startswith("ו") and len(t) > 1:
        t = t[1:]
    if t.startswith("אל") and len(t) > 2:
        t = t[2:]
    return t


def candidate_chain(raw: str) -> list[str]:
    """Mirror of `lib/lookup.ts:lookup` candidate chain (more permissive than
    `lib/divergence.ts:lookupDivergence` so we accept any chain runtime
    would accept)."""
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

    with_al(tok)
    after_vav: str | None = None
    if tok.startswith("ו") and len(tok) > 1:
        after_vav = tok[1:]
        with_al(after_vav)
    for base in [tok, after_vav]:
        if not base:
            continue
        for p in PREFIXES:
            if base.startswith(p) and len(base) > 1:
                with_al(base[1:])
    base_list = list(tries)
    out = {*base_list, *(normalize_finals(t) for t in base_list)}
    out.add(normalize_token(raw))
    return list(out)


def chapter_path(book: str, ch: int) -> Path:
    return DATA / f"tafsir-{book.lower()}-{ch}.json"


def load_verse_ja(book: str, ch: int, v: int) -> str | None:
    p = chapter_path(book, ch)
    if not p.exists():
        return None
    obj = json.loads(p.read_text())
    for verse in obj.get("verses", []):
        if verse.get("ch") == ch and verse.get("v") == v:
            return verse.get("ja", "")
    return None


def tokenise_via_cli(strings: list[str]) -> list[list[str]]:
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
        out.append(json.loads(line) if line else [])
    if len(out) != len(strings):
        raise RuntimeError(
            f"CLI returned {len(out)} lines for {len(strings)} inputs"
        )
    return out


def main() -> int:
    doc = json.loads((DATA / "tafsir-divergence.json").read_text())
    legend = doc.get("_sources", {})
    if not isinstance(legend, dict):
        print("FAIL: _sources is not an object")
        return 1
    legend_keys = set(legend.keys())
    entries = doc.get("entries", [])

    # Pass 1: collect every (entry, verse) pair to tokenise in one CLI call.
    verse_strings: list[str] = []
    verse_owners: list[tuple[int, dict]] = []  # (entry_index, verse_ref)
    for ei, entry in enumerate(entries):
        for vref in entry.get("verses", []):
            ja = load_verse_ja(vref["book"], vref["ch"], vref["v"])
            if ja is None:
                verse_strings.append("")
                verse_owners.append((ei, vref))
            else:
                verse_strings.append(ja)
                verse_owners.append((ei, vref))

    word_lists = tokenise_via_cli(verse_strings)

    # Pass 2: for each entry, collect every word from every cited verse and
    # check resolvability.
    entry_words: dict[int, list[tuple[dict, str]]] = defaultdict(list)
    missing_verse: list[tuple[int, dict]] = []
    for (ei, vref), words, raw in zip(verse_owners, word_lists, verse_strings):
        if raw == "":
            missing_verse.append((ei, vref))
            continue
        for w in words:
            entry_words[ei].append((vref, w))

    failures: list[str] = []

    # Failures from missing verse sources.
    for ei, vref in missing_verse:
        e = entries[ei]
        failures.append(
            f"  entry #{ei} '{e.get('lemma_ja')}' cites "
            f"{vref['book']} {vref['ch']}:{vref['v']} but chapter file "
            f"or verse not found in data/"
        )

    # Citation resolvability.
    for ei, entry in enumerate(entries):
        lemma = entry.get("lemma_ja", "")
        variants = entry.get("variants", []) or []
        targets = {normalize_finals(lemma)} | {normalize_finals(v) for v in variants}
        # Build the per-verse hit table so we can report unresolved verses.
        verse_hits: dict[tuple[str, int, int], bool] = {}
        for vref, w in entry_words.get(ei, []):
            chain = candidate_chain(w)
            key = (vref["book"], vref["ch"], vref["v"])
            if any(c in targets for c in chain):
                verse_hits[key] = True
            else:
                verse_hits.setdefault(key, False)
        # Every cited verse must have at least one resolving token.
        for vref in entry.get("verses", []):
            key = (vref["book"], vref["ch"], vref["v"])
            if key not in verse_hits:
                continue  # already flagged as missing-verse above
            if not verse_hits[key]:
                failures.append(
                    f"  entry #{ei} '{lemma}' cites {vref['book']} "
                    f"{vref['ch']}:{vref['v']} — no token in that verse "
                    f"resolves to lemma or any of {len(variants)} variants"
                )

    # Sources legend integrity.
    for ei, entry in enumerate(entries):
        sources = entry.get("sources", [])
        if not sources:
            failures.append(
                f"  entry #{ei} '{entry.get('lemma_ja')}' has empty sources[]"
            )
        for s in sources:
            if s not in legend_keys:
                failures.append(
                    f"  entry #{ei} '{entry.get('lemma_ja')}' cites "
                    f"source '{s}' not in _sources legend "
                    f"(legend has: {sorted(legend_keys)})"
                )

    # Per-book relation mix (soft warning for now).
    rel_by_book: dict[str, Counter] = defaultdict(Counter)
    for entry in entries:
        # Single representative book — the first verse's book.
        verses = entry.get("verses", [])
        book = verses[0]["book"] if verses else "?"
        blau = entry.get("blau_dict")
        rel = blau["relation"] if blau else "no-citation"
        rel_by_book[book][rel] += 1

    warnings: list[str] = []
    for book, counter in rel_by_book.items():
        total = sum(counter.values())
        direct = counter["direct"]
        adjacent = counter["adjacent"]
        backed = direct + adjacent
        nocite = counter["no-citation"]
        if total < 5:
            continue  # too few entries to evaluate; skip
        if backed / total < 0.70:
            warnings.append(
                f"  {book}: Blau-backed (direct+adjacent) = "
                f"{backed}/{total} = {round(100*backed/total)}% < 70%"
            )
        if direct / total < 0.45:
            warnings.append(
                f"  {book}: direct-Blau = {direct}/{total} = "
                f"{round(100*direct/total)}% < 45%"
            )
        if nocite / total > 0.30:
            warnings.append(
                f"  {book}: no-citation = {nocite}/{total} = "
                f"{round(100*nocite/total)}% > 30%"
            )

    # Report.
    print(f"Divergence verifier — {len(entries)} entries")
    print(f"=" * 50)
    if failures:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures:
            print(f)
    else:
        print("\nAll citation + sources checks PASS.")

    print(f"\nPer-book relation mix:")
    for book in sorted(rel_by_book.keys()):
        c = rel_by_book[book]
        total = sum(c.values())
        print(
            f"  {book:>9}: total={total}  direct={c['direct']}  "
            f"adjacent={c['adjacent']}  different-sense={c['different-sense']}  "
            f"no-citation={c['no-citation']}"
        )

    if warnings:
        print(f"\n{len(warnings)} WARNING(S) on quality bar (≥70% backed, ≥45% direct, ≤30% no-cite per book ≥5 entries):")
        for w in warnings:
            print(w)
    else:
        print("\nQuality bar: PASS (or insufficient entries per book to evaluate).")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

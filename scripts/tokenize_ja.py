"""Tokenize the JA Tafsir to inform dictionary curation.

Produces a frequency list of (normalized) tokens with their first-seen
verses. Reveals what to gloss first.

Normalization: strip leading vav (ו) and the definite-article prefix
(אל) before counting, so אלסמא, וסמא, וואלסמא all map to "סמא".
This is rough — ignores other prepositional prefixes (ב, ל, כ, etc.) and
verb inflection — but good enough to find what's worth glossing.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "tafsir-bereshit-1.json"

# Strip punctuation, treat maqaf as a separator.
PUNCT_RE = re.compile(r"[.,:;\-־–—!?؟\"]")
WS_RE = re.compile(r"\s+")


def normalize(tok: str) -> str:
    """Strip a leading vav and a leading definite article. Idempotent."""
    while tok.startswith("ו"):
        if len(tok) <= 1:
            break
        tok = tok[1:]
    if tok.startswith("אל") and len(tok) > 2:
        tok = tok[2:]
    return tok


def tokenize(text: str) -> list[str]:
    text = PUNCT_RE.sub(" ", text)
    return [t for t in WS_RE.split(text) if t]


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    counts: Counter[str] = Counter()
    first_seen: dict[str, int] = {}
    raw_to_norm: dict[str, set[str]] = defaultdict(set)
    for verse in data["verses"]:
        tokens = tokenize(verse["ja"])
        for tok in tokens:
            norm = normalize(tok)
            counts[norm] += 1
            raw_to_norm[norm].add(tok)
            first_seen.setdefault(norm, verse["v"])

    print(f"unique normalized tokens: {len(counts)}")
    print(f"top 60 by frequency:")
    print()
    print(f"{'count':>5}  {'first':>5}  {'normalized':<20}  variants")
    print(f"{'-' * 5}  {'-' * 5}  {'-' * 20}  {'-' * 30}")
    for tok, n in counts.most_common(60):
        variants = sorted(raw_to_norm[tok])
        v_str = ", ".join(variants[:4]) + ("..." if len(variants) > 4 else "")
        print(f"{n:>5}  v{first_seen[tok]:<4}  {tok:<20}  {v_str}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Mine all Blau Dictionary (Blau 2006) entries that cite Saadia's Tafsir.

Single mining pass, two downstream consumers:
  - Phase 3 R1 curators filter the output to STRICT-tier candidates (~30 new Twists).
  - Phase 4 tier-classification agent labels MEDIUM / EXPANSIVE / SKIP and
    feeds the surviving entries into data/tafsir-divergence.json with
    tier='note' or tier='gloss'.

Calibration (BLAU_SAADIA_CALIBRATION.md):
  - 1,596 expected hits (23.7% of Blau's 6,736 entries)
  - ~870 confirmed at expansive bar; up to ~1,560 with BORDERLINE upgrades
  - 32 Twists already shipped in data/tafsir-divergence.json

Output: data/_blau_saadia_candidates.json
  - Underscore prefix marks it as scratch / not bundled into the app
  - Stable enough to commit so curators and the verifier share a single artifact

Run from repo root:
  python3 scripts/mine_blau_saadia_candidates.py
"""

from __future__ import annotations

import datetime as _dt
import json
import pathlib
import re
import sqlite3
import sys

LEX_DB = pathlib.Path.home() / "Tools/arabic-lexicon/lex.sqlite"
OUT_PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "_blau_saadia_candidates.json"

# Hebrew abbreviation patterns Blau uses for Saadia. See PHASE3_ROUND1_PROMPT.md
# §"Blau query" for the canonical pattern set.
SAADIA_PATTERNS = [
    "סעדיה",
    "רס״ג",   # gershayim
    "רס\"ג",  # straight quotes
    "רסאג",
]

BODY_EXCERPT_CHARS = 600

# Citation extraction: split body into lines, keep any line that contains a
# Saadia marker. Falls back to short sentence-window when the body has no
# explicit newlines (some OCR'd entries are one long blob).
SAADIA_RE = re.compile("|".join(re.escape(p) for p in SAADIA_PATTERNS))


def extract_saadia_lines(body: str, max_lines: int = 6) -> list[str]:
    """Return up to `max_lines` line-or-sentence snippets that mention Saadia.

    Strategy:
      1. Prefer explicit newline-split lines containing a Saadia marker.
      2. If the body is single-line, scan with a ±120-char window around
         each match so curators see enough context to judge the citation.
    """
    lines: list[str] = []
    seen: set[str] = set()

    for raw in body.splitlines():
        line = raw.strip()
        if line and SAADIA_RE.search(line):
            if line not in seen:
                lines.append(line)
                seen.add(line)
        if len(lines) >= max_lines:
            return lines

    if lines:
        return lines

    # Single-blob fallback: extract a window around each match.
    for m in SAADIA_RE.finditer(body):
        start = max(0, m.start() - 120)
        end = min(len(body), m.end() + 120)
        snippet = body[start:end].replace("\n", " ").strip()
        if snippet and snippet not in seen:
            lines.append(snippet)
            seen.add(snippet)
        if len(lines) >= max_lines:
            break
    return lines


def main() -> int:
    if not LEX_DB.exists():
        print(f"error: lex.sqlite not found at {LEX_DB}", file=sys.stderr)
        return 1

    sql_filter = " OR ".join(f"body LIKE '%{p}%'" for p in SAADIA_PATTERNS)
    query = f"""
        SELECT id, root_ar, root_norm, body
        FROM entries
        WHERE dict='blau' AND ({sql_filter})
        ORDER BY id
    """

    with sqlite3.connect(str(LEX_DB)) as conn:
        rows = conn.execute(query).fetchall()

    candidates: list[dict] = []
    for blau_id, root_ar, root_he, body in rows:
        candidates.append(
            {
                "blau_id": blau_id,
                "root_ar": root_ar or "",
                "root_he": root_he or "",
                "body_excerpt": (body or "")[:BODY_EXCERPT_CHARS].strip(),
                "saadia_citation_lines": extract_saadia_lines(body or ""),
            }
        )

    payload = {
        "_generated": _dt.date.today().isoformat(),
        "_source": "~/Tools/arabic-lexicon/lex.sqlite blau table",
        "_query_patterns": SAADIA_PATTERNS,
        "_total": len(candidates),
        "candidates": candidates,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    no_citation = sum(1 for c in candidates if not c["saadia_citation_lines"])
    print(f"wrote {OUT_PATH.relative_to(pathlib.Path.cwd()) if OUT_PATH.is_relative_to(pathlib.Path.cwd()) else OUT_PATH}")
    print(f"  total candidates: {len(candidates)}")
    print(f"  citation lines extracted on {len(candidates) - no_citation}/{len(candidates)} entries")
    if no_citation:
        print(f"  ({no_citation} entries had no extractable citation snippet — body_excerpt still useful)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

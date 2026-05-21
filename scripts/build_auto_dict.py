"""Generate data/dictionary-auto.json from Lane + Blau for tokens missing from the starter dict.

For each unique normalized JA token in the corpus that isn't already in
dictionary-starter.json, this script tries:

  1. Heuristic root extraction (JA → Arabic → strip long vowels + common prefixes)
     → look up in Lane via root_ar; on hit, take Lane body.
  2. FTS search of the Arabic surface in Blau's body → windowed snippet.
  3. If both miss, the token is omitted from the output (the reader falls back
     to "no entry yet" for those).

Usage:
  python3 scripts/build_auto_dict.py [--corpus tafsir|bahya|both]
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import unicodedata
from itertools import combinations
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
LEX_DIR = Path.home() / "Tools" / "arabic-lexicon"
LEX_DB = LEX_DIR / "lex.sqlite"

sys.path.insert(0, str(LEX_DIR))
from ja_script import ja_to_ar  # noqa: E402
from buckwalter import normalize_ar  # noqa: E402

# -- Tokenization (mirrors lib/lookup.ts + lib/wordState.ts on the TS side) ----

APOS_RE = re.compile("['׳״ʼʹ’‘]")
NIQQUD = set("ְֱֲֳִֵֶַָׇֹֺֻּֽֿׁׂׅׄ")


def normalize_ja(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = APOS_RE.sub("'", text)
    return "".join(c for c in text if c not in NIQQUD)


def normalize_token(raw: str) -> str:
    t = re.sub(r'^[.,:;؛،"\'\s]+|[.,:;؛،"\'\s]+$', "", normalize_ja(raw))
    if t.startswith("ו") and len(t) > 1:
        t = t[1:]
    if t.startswith("אל") and len(t) > 2:
        t = t[2:]
    return t


def is_word_char(c: str) -> bool:
    return ("֐" <= c <= "׿") or c == "'"


def tokenize(text: str) -> list[str]:
    out, buf = [], ""
    for c in text:
        if is_word_char(c):
            buf += c
        else:
            if buf:
                out.append(buf)
                buf = ""
    if buf:
        out.append(buf)
    return out


def collect_corpus_tokens(name: str) -> set[str]:
    paths = []
    if name in ("tafsir", "both"):
        paths.append(DATA / "tafsir-bereshit-1.json")
    if name in ("bahya", "both"):
        paths.append(DATA / "bahya-bab1.json")
    tokens: set[str] = set()
    for p in paths:
        d = json.loads(p.read_text())
        texts: list[str] = []
        if "verses" in d:
            texts = [v["ja"] for v in d["verses"]]
        elif "pages" in d:
            for page in d["pages"]:
                for para in page.get("paragraphs", []):
                    if isinstance(para, str):
                        texts.append(para)
        for text in texts:
            for raw in tokenize(text):
                k = normalize_token(raw)
                if k:
                    tokens.add(k)
    return tokens


# -- Root extraction heuristic ------------------------------------------------

LONG_VOWELS = set("اويىآأإ")
# Common Arabic prefixes/suffixes worth peeling (rough; pruned to high-yield ones)
PREFIXES = ("ال", "و", "ف", "ب", "ل", "ك", "س", "ت", "ي", "ن", "م", "ا")
SUFFIXES = ("ون", "ين", "ات", "ان", "ها", "هم", "هن", "كم", "كن", "ه", "ك", "ي", "ت", "ن", "ة", "ا")


def strip_affixes(s: str) -> list[str]:
    """Generate stem candidates by peeling prefixes/suffixes (one of each at most)."""
    out = {s}
    for p in PREFIXES:
        if s.startswith(p) and len(s) > len(p) + 2:
            out.add(s[len(p):])
    for sfx in SUFFIXES:
        if s.endswith(sfx) and len(s) > len(sfx) + 2:
            out.add(s[: -len(sfx)])
    return list(out)


def root_candidates(stem: str) -> list[str]:
    """Ranked candidate roots for a stem, best (most reliable) first.

    Only emits 3-letter (and a few 4-letter) candidates drawn from the
    CONSONANT SKELETON — i.e. the stem with long vowels (ا و ي ى آ أ إ) removed.
    Full-stem subsequences (which include long vowels as radicals) are NOT
    emitted — those produce too many coincidental matches for surface forms
    that happen to share three letters with an unrelated Lane root. We accept
    fewer hits in exchange for higher precision; weak-root coverage is the
    price.
    """
    no_vowels = "".join(c for c in stem if c not in LONG_VOWELS)
    candidates: list[str] = []
    if len(no_vowels) >= 3:
        for combo in combinations(no_vowels, 3):
            cand = "".join(combo)
            if cand not in candidates:
                candidates.append(cand)
    if len(no_vowels) >= 4:
        for combo in combinations(no_vowels, 4):
            cand = "".join(combo)
            if cand not in candidates:
                candidates.append(cand)
    return candidates[:20]


def is_plausible_root(root: str, surface: str) -> bool:
    """Reject roots that don't actually appear inside the surface form.

    Root letters must appear in the surface in order, AND the surface length
    must be within 4 of the root length (no longer than root + typical
    affixes like al- + plural ون).
    """
    if len(surface) > len(root) + 4:
        return False
    i = 0
    for c in surface:
        if i < len(root) and c == root[i]:
            i += 1
    return i == len(root)


# -- Lane / Blau lookups ------------------------------------------------------


def trim_lane_body(body: str, max_chars: int = 320) -> str:
    """Drop the Buckwalter headword prefix and trim to a readable size.

    Lane TEI text has Buckwalter-encoded Arabic forms inline (e.g. xaloqN,
    A^adamap, qad~ara). They use capital letters / digits in the middle of
    tokens, which is the giveaway. We strip standalone Buckwalter tokens
    where they sit between spaces, but keep parenthetical refs like (S, K)
    intact because they're still useful signals.
    """
    # Start at first "signifies" / "He" / "The" / common English entry openers.
    m = re.search(r"\b(signifies|The act of|denotes|means|He |She |It )", body)
    if m:
        body = body[m.start():]
    # Strip Buckwalter tokens (contain capitals or digits or ~/^ markers) that
    # appear as standalone words. Keep English tokens intact.
    def is_buckwalter(tok: str) -> bool:
        if not tok:
            return False
        # ASCII-only token with at least one capital after the first char OR ~/^/digit
        if any(c in "~^" or c.isdigit() for c in tok):
            return True
        # If token has internal uppercase (e.g. A^adimN, xaloqN), it's BW
        if re.search(r"[a-zA-Z][A-Z]", tok):
            return True
        return False

    cleaned_words = []
    for w in body.split():
        if is_buckwalter(w.strip(",.;:()[]")):
            continue
        cleaned_words.append(w)
    body = " ".join(cleaned_words)
    body = re.sub(r"\s+", " ", body).strip()
    body = re.sub(r"\(\s*[,;]\s*", "(", body)
    body = re.sub(r"\s+\)", ")", body)
    if len(body) > max_chars:
        body = body[:max_chars].rsplit(" ", 1)[0] + " …"
    return body


def lookup_lane(conn: sqlite3.Connection, candidates: list[str], surface: str) -> dict | None:
    for c in candidates:
        if not is_plausible_root(c, surface):
            continue
        norm = normalize_ar(c)
        row = conn.execute(
            "SELECT root_ar, body FROM entries WHERE dict='lane' "
            "AND (root_ar = ? OR root_norm = ?) LIMIT 1",
            (c, norm),
        ).fetchone()
        if row:
            return {"root": row[0], "body": trim_lane_body(row[1])}
    return None


def lookup_blau(conn: sqlite3.Connection, ja_surface: str, context: int = 140) -> str | None:
    """Find the JA surface form inside the Blau corpus body and return a snippet."""
    row = conn.execute(
        "SELECT body FROM entries WHERE dict='blau-judeoarabic' LIMIT 1"
    ).fetchone()
    if not row:
        return None
    body = row[0]
    idx = body.find(ja_surface)
    if idx < 0:
        return None
    a = max(0, idx - context)
    b = min(len(body), idx + len(ja_surface) + context)
    snippet = body[a:b].replace("\n", " ")
    snippet = re.sub(r"\s+", " ", snippet).strip()
    return snippet


# -- Main ---------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", choices=("tafsir", "bahya", "both"), default="tafsir")
    ap.add_argument("--out", default=str(DATA / "dictionary-auto.json"))
    ap.add_argument("--limit", type=int, default=0, help="cap tokens processed (debug)")
    args = ap.parse_args()

    starter = json.loads((DATA / "dictionary-starter.json").read_text())
    starter_keys = {e["lemma_ja"] for e in starter["entries"]}

    tokens = collect_corpus_tokens(args.corpus)
    missing = sorted(tokens - starter_keys)
    if args.limit:
        missing = missing[: args.limit]
    print(f"Corpus: {args.corpus}. Tokens missing from starter: {len(missing)}", file=sys.stderr)

    conn = sqlite3.connect(LEX_DB)
    out_entries = []
    stats = {"lane": 0, "blau": 0, "miss": 0}

    for ja in missing:
        ar = ja_to_ar(ja)
        candidates: list[str] = []
        for stem in strip_affixes(ar):
            for root in root_candidates(stem):
                if root not in candidates:
                    candidates.append(root)
        lane_hit = lookup_lane(conn, candidates, ar)
        if lane_hit:
            out_entries.append({
                "id": f"auto-lane-{ja}",
                "lemma_ja": ja,
                "lemma_ar": ar,
                "root": lane_hit["root"],
                "source": "lane",
                "gloss_en": lane_hit["body"],
                "gloss_he": "",
                "pos": "",
                "notes": "Auto-extracted from Lane's Lexicon by root. Verify before quoting.",
            })
            stats["lane"] += 1
            continue
        # Blau is stored as one unindexed corpus body in our DB; FTS snippets
        # against it are largely noise (frontmatter, bibliography). Skip until
        # we have a properly-indexed Blau lemma table.
        stats["miss"] += 1

    Path(args.out).write_text(
        json.dumps({"entries": out_entries}, ensure_ascii=False, indent=2)
    )
    print(
        f"Lane hits: {stats['lane']}  Blau hits: {stats['blau']}  "
        f"Misses: {stats['miss']}  Wrote: {args.out}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()

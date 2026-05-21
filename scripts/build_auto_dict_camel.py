"""Generate data/dictionary-auto.json from Camel Tools morphological analysis.

Runs in the .venv-camel virtualenv (Python 3.11). For each unique JA token
in the corpus that isn't in the starter dict, transliterate JA → Arabic,
analyze with Camel Tools' MLE morphology (CALIMA MSA), and emit a clean
entry with lemma, root, POS, and English gloss.

Usage:
  source .venv-camel/bin/activate
  python scripts/build_auto_dict_camel.py [--corpus tafsir|bahya|both]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
LEX_DIR = Path.home() / "Tools" / "arabic-lexicon"
sys.path.insert(0, str(LEX_DIR))
from ja_script import ja_to_ar  # noqa: E402

# Tokenization mirrors lib/lookup.ts -------------------------------------------

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


# Gloss cleanup ---------------------------------------------------------------

# Camel glosses look like "seas+[acc.indef.]" or "creator" or
# "moments;times+[acc.indef.]" — keep the head, drop the morphological suffix.
def clean_gloss(g: str) -> str:
    if not g:
        return ""
    g = g.split("+")[0]  # drop +[acc.indef.] etc.
    g = g.replace("_", " ").strip()
    return g


def fmt_root(r: str) -> str:
    # Camel roots are dot-separated: خ.ل.ق → خلق, # marks a weak radical
    return r.replace(".", "").replace("#", "ـ")


# Tokens that are almost certainly Hebrew when they appear in Bahya — proper
# names + the most common Tanakh function words. The list collapses against
# the normalized form (vav and al- already stripped). Extend as more cases
# come to light. We err on the side of caution: an entry that gets suppressed
# will simply show "no entry yet," which is honest about the gap.
HEBREW_SUPPRESS = {
    # Tetragrammaton + common divine names
    "יהוה", "ה", "ה'", "יה",
    # Patriarchs / matriarchs / Mosaic-era names
    "משה", "אהרן", "אברהם", "אברם", "יצחק", "יעקב", "יוסף",
    "שרה", "רבקה", "רחל", "לאה",
    # Other biblical proper nouns common in Bahya quotes
    "דוד", "שלמה", "שמואל", "ישעיהו", "ירמיהו", "יחזקאל",
    "ישראל", "יהודה", "ציון", "ירושלים", "ירושלם", "סיני",
    "מצרים", "כנען",
    # Common Hebrew waw-consecutive verbs (after stripping leading ו)
    "אמר", "יאמר", "יהי", "יעש", "ירא", "קרא", "דבר", "צא", "לך",
    # Hebrew function words that don't share JA usage
    "אשר", "כי",
}


# Main ------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", choices=("tafsir", "bahya", "both"), default="both")
    ap.add_argument("--out", default=str(DATA / "dictionary-auto.json"))
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    starter = json.loads((DATA / "dictionary-starter.json").read_text())
    starter_keys = {e["lemma_ja"] for e in starter["entries"]}

    tokens = collect_corpus_tokens(args.corpus)
    missing = sorted(tokens - starter_keys)
    if args.limit:
        missing = missing[: args.limit]
    print(f"Corpus: {args.corpus}. Missing from starter: {len(missing)}", file=sys.stderr)

    db = MorphologyDB.builtin_db()
    analyzer = Analyzer(db)

    out_entries = []
    stats = {"hit": 0, "miss": 0}

    for ja in missing:
        if len(ja) < 3:
            stats["miss"] += 1
            continue
        if ja in HEBREW_SUPPRESS:
            stats["miss"] += 1
            continue
        ar = ja_to_ar(ja)
        analyses = analyzer.analyze(ar)
        if not analyses:
            stats["miss"] += 1
            continue
        # Pick the first analysis (CALIMA orders by lex frequency roughly).
        # Collect up to 3 distinct gloss heads for richer entries.
        primary = analyses[0]
        seen_glosses = set()
        alternates = []
        for a in analyses:
            g = clean_gloss(a.get("gloss", ""))
            if g and g not in seen_glosses:
                seen_glosses.add(g)
                if len(alternates) < 3:
                    alternates.append(g)
        gloss_combined = "; ".join(alternates) if alternates else clean_gloss(primary.get("gloss", ""))
        out_entries.append({
            "id": f"auto-camel-{ja}",
            "lemma_ja": ja,
            "lemma_ar": primary.get("lex", ar),
            "root": fmt_root(primary.get("root", "")),
            "pos": primary.get("pos", ""),
            "gloss_en": gloss_combined,
            "gloss_he": "",
            "source": "camel",
            "notes": "Camel Tools MSA morphology analyzer. Verify before citing.",
        })
        stats["hit"] += 1

    Path(args.out).write_text(
        json.dumps({"entries": out_entries}, ensure_ascii=False, indent=2)
    )
    print(
        f"Camel hits: {stats['hit']}  Misses: {stats['miss']}  Wrote: {args.out}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()

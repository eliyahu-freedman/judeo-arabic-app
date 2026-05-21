"""Build data/corpus-index.json from the JA Tafsir files.

For every tafsir-*.json under data/, tokenizes each verse's `ja` text using
the same rules as lib/lookup.ts (tokenizeJa + normalizeToken) and emits a
map of normalized token -> {count, occurrences: [{ch, v, surface}]}.

The reader can then load this and answer "how many times does this word
appear, and where?" in O(1) per click.

Run:  python3 scripts/build_corpus_index.py
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
PUBLIC = REPO / "public"

# Hebrew Unicode block. Mirrors `/[֐-׿']/.test(c)` in lib/lookup.ts.
HEB_LO, HEB_HI = "֐", "׿"
NIQQUD = set("ְֱֲֳִֵֶַָׇֹֺֻּֽֿׁׂׅׄ")
APOS_RE = re.compile("['׳״ʼʹ’‘]")
PUNCT_TRIM_RE = re.compile(r'^[.,:;؛،"\'\s]+|[.,:;؛،"\'\s]+$')


def is_word_char(c: str) -> bool:
    return (HEB_LO <= c <= HEB_HI) or c == "'"


def tokenize_ja(text: str) -> list[tuple[str, str]]:
    """Yield (kind, text) pairs, kind in {'word','sep'}. Mirrors tokenizeJa."""
    out: list[tuple[str, str]] = []
    buf = ""
    buf_kind: str | None = None
    for c in text:
        kind = "word" if is_word_char(c) else "sep"
        if kind == buf_kind:
            buf += c
        else:
            if buf:
                out.append((buf_kind or "sep", buf))
            buf = c
            buf_kind = kind
    if buf:
        out.append((buf_kind or "sep", buf))
    return out


def normalize_surface(tok: str) -> str:
    """NFC + unify apostrophes + strip niqqud. Run before normalize_token so
    JA text with stray diacritics still keys correctly."""
    tok = unicodedata.normalize("NFC", tok)
    tok = APOS_RE.sub("'", tok)
    return "".join(c for c in tok if c not in NIQQUD)


def strip_punct(tok: str) -> str:
    return PUNCT_TRIM_RE.sub("", tok)


def normalize_token(raw: str) -> str:
    """Mirrors normalizeToken in lib/lookup.ts."""
    t = strip_punct(normalize_surface(raw))
    if t.startswith("ו") and len(t) > 1:
        t = t[1:]
    if t.startswith("אל") and len(t) > 2:
        t = t[2:]
    return t


BOOK_ORDER = ["Bereshit", "Shemot", "Vayikra", "Bamidbar", "Devarim"]


def sort_key(path: Path) -> tuple[int, int]:
    """Sort tafsir-{book}-{ch}.json by (book index, chapter number)."""
    stem = path.stem  # "tafsir-bereshit-1"
    parts = stem.split("-")
    if len(parts) < 3:
        return (99, 99)
    book_slug = parts[1]
    try:
        ch = int(parts[2])
    except ValueError:
        return (99, 99)
    book_display = book_slug.capitalize()
    bi = BOOK_ORDER.index(book_display) if book_display in BOOK_ORDER else 99
    return (bi, ch)


def build() -> dict:
    # Per key: raw collection (surface -> idx, occurrence triples).
    # Final shape per key: {count, surfaces: [str], occurrences: [[ch,v,sIdx]]}
    raw: dict[str, dict] = {}
    corpora: list[str] = []

    paths = sorted(DATA.glob("tafsir-*.json"), key=sort_key)
    for path in paths:
        # Skip the *-english.json sidecars; only ingest JA files.
        if path.stem.endswith("-english"):
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        book = data.get("book", "?")
        chapter = data.get("chapter", "?")
        corpora.append(f"{book} {chapter}")
        for verse in data.get("verses", []):
            ch = verse.get("ch", chapter)
            v = verse.get("v")
            ja = verse.get("ja", "")
            for kind, text in tokenize_ja(ja):
                if kind != "word":
                    continue
                surface = strip_punct(normalize_surface(text))
                if not surface:
                    continue
                key = normalize_token(text)
                if not key:
                    continue
                bucket = raw.setdefault(
                    key,
                    {"count": 0, "surfaces": [], "_surface_idx": {}, "occurrences": []},
                )
                bucket["count"] += 1
                s_idx = bucket["_surface_idx"].get(surface)
                if s_idx is None:
                    s_idx = len(bucket["surfaces"])
                    bucket["surfaces"].append(surface)
                    bucket["_surface_idx"][surface] = s_idx
                bucket["occurrences"].append([ch, v, s_idx])

    tokens: dict[str, dict] = {}
    for key in sorted(raw):
        b = raw[key]
        tokens[key] = {
            "count": b["count"],
            "surfaces": b["surfaces"],
            "occurrences": b["occurrences"],
        }

    total = sum(b["count"] for b in tokens.values())
    return {
        "corpora": corpora,
        "total_tokens": total,
        "unique_keys": len(tokens),
        "tokens": tokens,
    }


def main() -> None:
    import gzip

    out = build()
    PUBLIC.mkdir(parents=True, exist_ok=True)
    json_path = PUBLIC / "corpus-index.json"
    gz_path = PUBLIC / "corpus-index.json.gz"
    # Compact JSON: this file is generated, not hand-edited, and is large
    # enough that indentation triples its disk + bundle footprint.
    payload = json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n"
    json_path.write_text(payload, encoding="utf-8")
    with gzip.open(gz_path, "wb", compresslevel=9) as fh:
        fh.write(payload.encode("utf-8"))
    json_mb = json_path.stat().st_size / (1024 * 1024)
    gz_mb = gz_path.stat().st_size / (1024 * 1024)
    print(f"wrote {json_path.relative_to(REPO)} ({json_mb:.2f} MB)")
    print(f"wrote {gz_path.relative_to(REPO)} ({gz_mb:.2f} MB gzipped)")
    print(f"  corpora:      {len(out['corpora'])}")
    print(f"  total tokens: {out['total_tokens']}")
    print(f"  unique keys:  {out['unique_keys']}")


if __name__ == "__main__":
    main()

"""Augment data/aramaic-cognates.json with a first Tafsir occurrence for each
Arabic cognate, if Saadia uses the word.

Each entry's `arabic` field is converted to a Judeo-Arabic surface form,
normalized (strip leading vav and definite article), and looked up in the
corpus index. We try several spelling variants because medial alef and
tā-marbūṭa are written inconsistently.

Adds two new fields per entry where a hit is found:
  tafsir_count:  int
  tafsir_first:  { book_slug, book, ch, v, surface }
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "aramaic-cognates.json"
CORPUS = REPO / "public" / "corpus-index.json"

BOOK_SLUG_TO_DISPLAY = {
    "bereshit": "Bereshit", "shemot": "Shemot", "vayikra": "Vayikra",
    "bamidbar": "Bamidbar", "devarim": "Devarim",
}
BOOK_ORDER = ["bereshit", "shemot", "vayikra", "bamidbar", "devarim"]

# Standard Saadia Judeo-Arabic transliteration.
AR_TO_JA = {
    "ب":"ב","ت":"ת","ث":"ת'","ج":"ג","ح":"ח","خ":"כ'",
    "د":"ד","ذ":"ד'","ر":"ר","ز":"ז","س":"ס","ش":"ש",
    "ص":"צ","ض":"צ'","ط":"ט","ظ":"ט'","ع":"ע","غ":"ג'",
    "ف":"פ","ق":"ק","ك":"כ","ل":"ל","م":"מ","ن":"נ",
    "ه":"ה","و":"ו","ي":"י",
    "ا":"א","أ":"א","إ":"א","آ":"אא","ء":"","ؤ":"ו","ئ":"י",
    "ة":"ה","ى":"א",
    " ":" ",
}

ARABIC_DIACRITICS = re.compile(r"[ً-ٰٟـ]")


def to_ja(arabic: str) -> str:
    """Strip diacritics and convert Arabic letters to JA equivalents."""
    s = unicodedata.normalize("NFC", arabic)
    s = ARABIC_DIACRITICS.sub("", s)
    out = []
    for ch in s:
        out.append(AR_TO_JA.get(ch, ""))
    return "".join(out)


def normalize_ja(tok: str) -> str:
    """Match the corpus index's normalization: strip leading vav + leading אל."""
    if tok.startswith("ו") and len(tok) > 1:
        tok = tok[1:]
    if tok.startswith("אל") and len(tok) > 2:
        tok = tok[2:]
    return tok


FINAL_MAP = {"מ": "ם", "נ": "ן", "כ": "ך", "פ": "ף", "צ": "ץ"}


def apply_finals(s: str) -> str:
    """Apply Hebrew final-letter forms at word end.

    Saadia's convention: word-final ض drops the rafe-apostrophe (ארץ', not ארץ'),
    and word-final interdentals (ث/ذ) often drop it too (ת'לאת without final ').
    """
    if not s:
        return s
    # Strip apostrophe on terminal letter when present.
    if len(s) >= 2 and s[-1] == "'":
        s = s[:-1]
    last = s[-1]
    if last in FINAL_MAP:
        s = s[:-1] + FINAL_MAP[last]
    return s


def candidates(arabic: str) -> list[str]:
    """Generate normalized JA lookup keys to try, in priority order."""
    raw = to_ja(arabic).strip()
    # Strip leading article "al-" (الـ) if present in the source Arabic.
    if raw.startswith("אל") and len(raw) > 2:
        raw = raw[2:]
    cands: list[str] = []
    seen = set()

    def add(s: str):
        s = normalize_ja(s)
        if s and s not in seen:
            seen.add(s)
            cands.append(s)

    add(apply_finals(raw))
    add(raw)  # without final-form, just in case
    # Drop medial alefs (Saadia often elides them).
    if "א" in raw[1:]:
        no_alef = raw[0] + raw[1:].replace("א", "")
        add(apply_finals(no_alef))
        add(no_alef)
    # Drop a trailing alef (final long ā often unwritten).
    if raw.endswith("א"):
        add(apply_finals(raw[:-1]))
    # Drop final he (tā-marbūṭa).
    if raw.endswith("ה"):
        add(apply_finals(raw[:-1]))
    # Add a trailing he (Saadia sometimes renders ة or final long-ā as ה).
    add(apply_finals(raw + "ה"))
    if raw.endswith("א"):
        add(apply_finals(raw[:-1] + "ה"))
    return cands


def load_tafsir_files() -> dict[tuple[str, int], dict]:
    """Load every tafsir-{book}-{ch}.json (skip *-english.json) keyed by (slug, ch)."""
    out: dict[tuple[str, int], dict] = {}
    DATA_DIR = REPO / "data"
    for path in sorted(DATA_DIR.glob("tafsir-*.json")):
        if "-english" in path.stem:
            continue
        parts = path.stem.split("-")
        if len(parts) < 3:
            continue
        slug = parts[1]
        try:
            ch = int(parts[2])
        except ValueError:
            continue
        out[(slug, ch)] = json.loads(path.read_text(encoding="utf-8"))
    return out


def build_verse_to_book(files: dict) -> dict[tuple[int, int], list[str]]:
    out: dict[tuple[int, int], list[str]] = defaultdict(list)
    for (slug, _ch), d in files.items():
        for v in d.get("verses", []):
            out[(v["ch"], v["v"])].append(slug)
    return out


def find_verse(files: dict, slug: str, ch: int, v: int) -> dict | None:
    d = files.get((slug, ch))
    if not d:
        return None
    for verse in d.get("verses", []):
        if verse.get("v") == v:
            return verse
    return None


PUNCT_TRIM = re.compile(r"^[.,:;؛،\"'\s]+|[.,:;؛،\"'\s]+$")


def _strip_punct(t: str) -> str:
    return PUNCT_TRIM.sub("", t)


def ja_tokens(text: str) -> list[str]:
    """Token boundaries match the corpus index: whitespace plus . , : ; etc."""
    return [w for w in re.split(r"\s+", text) if w]


def verse_has_token(ja: str, surface: str) -> bool:
    """True iff the JA text has a token whose stripped form equals surface."""
    return any(_strip_punct(t) == surface for t in ja_tokens(ja))


def extract_clause(ja: str, surface: str, max_words: int = 7) -> str:
    """Return the period-delimited clause containing the surface, capped at max_words.

    Token-level match (surface must equal a whole word, not a substring).
    Within a long clause, return a window of tokens around the target."""
    clauses = [c.strip() for c in ja.split(".") if c.strip()]
    for c in clauses:
        words = c.split()
        if not any(_strip_punct(w) == surface for w in words):
            continue
        if len(words) <= max_words:
            return c
        for i, w in enumerate(words):
            if _strip_punct(w) == surface:
                half = max_words // 2
                lo = max(0, i - half)
                hi = min(len(words), lo + max_words)
                lo = max(0, hi - max_words)
                return " ".join(words[lo:hi])
        return " ".join(words[:max_words])
    return " ".join(ja.split()[:max_words])


def trim_hebrew_verse(hebrew: str, max_chars: int = 80) -> str:
    """Hebrew verses can be long. Trim by clause (etnachta-like) — use maqaf and
    common punctuation as soft breakpoints — and cap by character length."""
    if not hebrew:
        return hebrew
    s = hebrew.strip()
    if len(s) <= max_chars:
        return s
    # Try splitting on common clause breakers
    for sep in [" — ", " - ", ", ", "; "]:
        if sep in s:
            head = s.split(sep, 1)[0]
            if len(head) <= max_chars:
                return head + "…"
    return s[:max_chars].rsplit(" ", 1)[0] + "…"


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    tokens = corpus["tokens"]
    files = load_tafsir_files()
    verse_to_book = build_verse_to_book(files)

    hits = 0
    misses: list[tuple[int, str, list[str]]] = []
    for e in data["entries"]:
        arabic = e["arabic"]
        cands = candidates(arabic)
        bucket = None
        chosen = None
        for c in cands:
            if c in tokens:
                bucket = tokens[c]
                chosen = c
                break
        if not bucket:
            misses.append((e["rank"], arabic, cands))
            # Make sure stale fields aren't left behind
            e.pop("tafsir_count", None)
            e.pop("tafsir_n_verses", None)
            e.pop("tafsir_key", None)
            e.pop("tafsir_first", None)
            continue

        # Walk occurrences in document order; pick the first one whose verse
        # actually contains a surface that normalizes to our key. The corpus
        # index only stores (ch, v); two books can share that pair, so we
        # must verify which book's file holds the hit.
        chosen_occ = None
        chosen_slug = None
        chosen_verse = None
        chosen_surface = None
        for occ in bucket["occurrences"]:
            ch, v, s_idx = occ[0], occ[1], occ[2]
            surface = bucket["surfaces"][s_idx]
            candidates_slugs = verse_to_book.get((ch, v), [])
            candidates_slugs = sorted(
                candidates_slugs,
                key=lambda s: BOOK_ORDER.index(s) if s in BOOK_ORDER else 99,
            )
            for slug in candidates_slugs:
                verse = find_verse(files, slug, ch, v)
                if verse and verse_has_token(verse.get("ja", ""), surface):
                    chosen_occ = occ
                    chosen_slug = slug
                    chosen_verse = verse
                    chosen_surface = surface
                    break
            if chosen_occ:
                break

        if not chosen_occ:
            # Couldn't reconcile — keep the lookup metadata but no first link.
            misses.append((e["rank"], arabic, cands))
            e.pop("tafsir_first", None)
            continue

        hits += 1
        ch, v = chosen_occ[0], chosen_occ[1]
        ja_phrase = extract_clause(chosen_verse.get("ja", ""), chosen_surface)
        hebrew_verse = trim_hebrew_verse(chosen_verse.get("hebrew", ""))
        n_verses = len({(o[0], o[1]) for o in bucket["occurrences"]})
        e["tafsir_count"] = bucket["count"]
        e["tafsir_n_verses"] = n_verses
        e["tafsir_key"] = chosen
        e["tafsir_first"] = {
            "book_slug": chosen_slug,
            "book": BOOK_SLUG_TO_DISPLAY.get(chosen_slug, chosen_slug.title()),
            "ch": ch,
            "v": v,
            "surface": chosen_surface,
            "ja_phrase": ja_phrase,
            "hebrew_phrase": hebrew_verse,
        }

    data["_generated"] = "manual + augment_aramaic_cognates.py"
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"hits: {hits}/{len(data['entries'])}")
    if misses:
        print(f"misses ({len(misses)}):")
        for rank, ar, cands in misses:
            print(f"  #{rank:>2} {ar:<10}  tried: {cands}")


if __name__ == "__main__":
    main()

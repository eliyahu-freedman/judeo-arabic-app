"""Parse one parsha from ~/Desktop/Rasag-Parshiot into JSON for the app.

Output schema (one entry per verse):
    {
      "ch": int, "v": int,
      "hebrew": "...",       # biblical Hebrew (לשון הקודש), vowel-pointed
      "ja": "...",            # Saadia Tafsir in Judeo-Arabic (תפסיר)
      "arabic": "...",        # Arabic-script form (ערבית)
      "hebrew_translation": "..."  # Hebrew rendering of the Tafsir (תרגום),
                                   # with embedded rabbinic commentary stripped.
    }

Strategy: scan line-by-line, buffer each `N) <field>:` block until the
next field marker, then post-process. This handles cases where the
content starts on a continuation line after the marker.

Usage:
    python3 scripts/build_tafsir.py                       # Bereshit, all chapters
    python3 scripts/build_tafsir.py --chapter 2           # just ch 2
    python3 scripts/build_tafsir.py --source ~/Desktop/Rasag-Parshiot/02-Noach.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_SOURCE = Path.home() / "Desktop" / "Rasag-Parshiot" / "01-Bereshit.txt"
OUT_DIR = Path(__file__).resolve().parent.parent / "data"

HEB_NUM = {
    "א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5,
    "ו": 6, "ז": 7, "ח": 8, "ט": 9, "י": 10,
    "כ": 20, "ל": 30, "מ": 40, "נ": 50, "ס": 60,
    "ע": 70, "פ": 80, "צ": 90, "ק": 100, "ר": 200,
    "ש": 300, "ת": 400,
}

def gematria(tok: str) -> int:
    return sum(HEB_NUM.get(c, 0) for c in tok)

FIELD_RE = re.compile(
    r"^\s*(\d+)\)\s*(לשון הקודש|תפסיר|ערבית|תרגום)\s*:\s*(.*)$"
)
# Pure (unpointed) Hebrew letters used as numerals — strip vowel points first.
HEB_LETTER = "אבגדהוזחטיכלמנסעפצקרשת" + "ךםןףץ"
NIKKUD_RE = re.compile(r"[֑-ׇ]")  # cantillation + nikkud range

# Verse-locator at the start of a field body.
# In לשון הקודש: "א א " (ch + v, no paren).
# In תפסיר / ערבית / תרגום: "א א) " or just "ב) ".
#
# A Hebrew gematria numeral 1-99 is either:
#   - a single ones-letter (א-ט = 1-9)
#   - a tens-letter (י כ ל מ נ ס ע פ צ = 10..90) optionally followed by a ones-letter
# Bounding the second token this way is critical: the source occasionally omits
# whitespace between the locator and the content (e.g. "ו אוַיְהִי..."), so a
# greedy `[א-ת]{1,2}` would eat content letters.
ONES = "אבגדהוזחט"
TENS = "יכלמנסעפצ"
# Hebrew gematria for 15 and 16 substitutes 'טו'/'טז' to avoid the divine-name
# spellings יה/יו. The reverse spelling 'חי' (= 18, also the word "alive") is
# used in places of יח. These three are the only non-standard 2-letter
# numerals seen across the Rasag-Parshiot source.
NUM_TOKEN = rf"(?:טו|טז|חי|[{TENS}][{ONES}]?|[{ONES}])"
LOCATOR_OPENING = re.compile(rf"^\s*({NUM_TOKEN})(?:\s+({NUM_TOKEN}))?\)?\s*")


def strip_nikkud(s: str) -> str:
    return NIKKUD_RE.sub("", s)


# Parsha-header signal words. If we see any of these BEFORE a verse-locator,
# we know we're looking at a parsha-boundary header (Latin + Hebrew + Arabic
# transliteration) and should hunt for the locator further into the text.
HEADER_SIGNAL_RE = re.compile(
    r"Parash|פר[שׁ]ת|פָּרָשַׁת|חו?מ?ש|חֻמָּשׁ|חוּמַּשׁ|Part [IVX]+|Chapter [A-E]"
)

# A standalone verse-letter marker like " ט) " — gimatria token followed by
# close paren. Used as a fallback locator after the parsha header.
INNER_LOCATOR_RE = re.compile(rf"(?:^|\s)({NUM_TOKEN})\)\s+")


def parse_locator(text: str) -> tuple[int | None, int | None, str]:
    """Return (ch, v, remainder). Either ch or v may be None if not present."""
    bare = strip_nikkud(text)
    m = LOCATOR_OPENING.match(bare)
    if m:
        tok_a = m.group(1)
        tok_b = m.group(2)
        if tok_b is None:
            v = gematria(tok_a)
            ch = None
        else:
            ch = gematria(tok_a)
            v = gematria(tok_b)
        om = LOCATOR_OPENING.match(text)
        remainder = text[om.end():] if om else text
        return ch, v, remainder

    # Fallback: parsha-boundary headers prepend Latin / Hebrew / Arabic text
    # before the locator. Only honor an inner locator if the prefix carries a
    # header signal word — otherwise leave the text untouched.
    inner = INNER_LOCATOR_RE.search(bare)
    if inner and HEADER_SIGNAL_RE.search(bare[: inner.start()]):
        v = gematria(inner.group(1))
        # Match the same on the original (nikkud-preserved) text.
        om = INNER_LOCATOR_RE.search(text)
        remainder = text[om.end():] if om else text
        return None, v, remainder
    return None, None, text


FIELD_KEY = {
    "לשון הקודש": "hebrew",
    "תפסיר": "ja",
    "ערבית": "arabic",
    "תרגום": "hebrew_translation",
}


def parse_file(path: Path) -> list[dict]:
    # Pass 1: gather each (seq, field) block's raw text.
    blocks: list[tuple[int, str, str]] = []
    current: tuple[int, str, list[str]] | None = None

    def flush() -> None:
        if current:
            seq, field, lines = current
            blocks.append((seq, field, " ".join(s for s in lines if s).strip()))

    with path.open(encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            m = FIELD_RE.match(line)
            if m:
                flush()
                seq = int(m.group(1))
                field = m.group(2)
                body = m.group(3).strip()
                current = (seq, field, [body])
            else:
                stripped = line.strip()
                if current and stripped:
                    current[2].append(stripped)
    flush()

    # Pass 2: group by seq.
    by_seq: dict[int, dict[str, str]] = {}
    for seq, field, content in blocks:
        by_seq.setdefault(seq, {})[field] = content

    verses: list[dict] = []
    last_ch = None
    for seq in sorted(by_seq.keys()):
        block = by_seq[seq]
        hebrew_raw = block.get("לשון הקודש", "")
        if not hebrew_raw:
            continue
        ch, v, hebrew = parse_locator(hebrew_raw)
        if ch is None and last_ch is not None:
            ch = last_ch
        if ch is not None:
            last_ch = ch
        if v is None or ch is None:
            continue

        ja_raw = block.get("תפסיר", "")
        _, _, ja = parse_locator(ja_raw)

        ar_raw = block.get("ערבית", "")
        ar_clean = clean_arabic(ar_raw)

        htr_raw = block.get("תרגום", "")
        _, _, htr = parse_locator(htr_raw)

        verses.append({
            "ch": ch, "v": v,
            "hebrew": hebrew.strip(),
            "ja": ja.strip(),
            "arabic": ar_clean.strip(),
            "hebrew_translation": htr.strip(),
        })
    return verses


def clean_hebrew_translation(text: str) -> str:
    """Strip rabbinic-commentary brackets and parens.

    The תרגום field mixes the bare Hebrew rendering of Saadia's JA with
    extensive commentary in [...] and (...). Removed iteratively so nested
    brackets fall away.
    """
    prev = None
    while text != prev:
        prev = text
        text = re.sub(r"\[[^\[\]]*\]", "", text)
        text = re.sub(r"\([^()]*\)", "", text)
    text = re.sub(r"[\[\]()]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s*([,.;])", r"\1", text)
    return text


def clean_arabic(text: str) -> str:
    """Strip leading chapter/parsha-header artifacts from the Arabic body.

    Cases seen in the source:
    - Bereshit ch2 first verse: 'Chapter A2 مَقْطَع 1 ...'
    - Noach v9 (parsha boundary): '102 نَصْ أسْبوعي – نُوحْ 11121 Parashat Noach Chapter A6+ مَقْطَع 9 ...'
    - Shemot 1:1 (book boundary): 'الخُمْسُ الثَّانِي ... Part II of V- exodus Shemot 201 ... Parashat Shemot Chapter B1 مَقْطَع 1 ...'

    Strategy: if a 'Chapter [A-E]\\d+(?:\\+)?\\s*مَ?قْ?طَ?ع\\s+\\d+' marker is
    present anywhere, drop everything up to and including it. Otherwise just
    strip a bare leading verse number.
    """
    # Match 'Chapter <id> <مقطع-with-niqqud> <verse#>', tolerating:
    #   - id forms: 'A2', 'B1', 'A6+', '39', 'C10' (no space before مقطع)
    #   - any niqqud on the مقطع letters
    #   - missing whitespace between id and مقطع
    m = re.search(
        r"Chapter\s*[A-E]?\d+\+?\s*[ء-ۿً-ْ]+\s*\d+\s*",
        text,
    )
    if m:
        text = text[m.end():]
    text = re.sub(r"^\s*\d+\s*", "", text)
    return text.strip()


def clean_ja(text: str) -> str:
    """Strip inline manuscript variants like [ויט'הר] from the JA field."""
    prev = None
    while text != prev:
        prev = text
        text = re.sub(r"\[[^\[\]]*\]\s*", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Parsha file index → Tanakh book name. Add entries as more sources land.
PARSHA_TO_BOOK = {
    1: "Bereshit", 2: "Bereshit", 3: "Bereshit", 4: "Bereshit",
    5: "Bereshit", 6: "Bereshit", 7: "Bereshit", 8: "Bereshit",
    9: "Bereshit", 10: "Bereshit", 11: "Bereshit", 12: "Bereshit",
    13: "Shemot", 14: "Shemot", 15: "Shemot", 16: "Shemot",
    17: "Shemot", 18: "Shemot", 19: "Shemot", 20: "Shemot",
    21: "Shemot", 22: "Shemot", 23: "Shemot",
    24: "Vayikra", 25: "Vayikra", 26: "Vayikra", 27: "Vayikra",
    28: "Vayikra", 29: "Vayikra", 30: "Vayikra", 31: "Vayikra",
    32: "Vayikra", 33: "Vayikra",
    34: "Bamidbar", 35: "Bamidbar", 36: "Bamidbar", 37: "Bamidbar",
    38: "Bamidbar", 39: "Bamidbar", 40: "Bamidbar", 41: "Bamidbar",
    42: "Bamidbar", 43: "Bamidbar",
    44: "Devarim", 45: "Devarim", 46: "Devarim", 47: "Devarim",
    48: "Devarim", 49: "Devarim", 50: "Devarim", 51: "Devarim",
    52: "Devarim", 53: "Devarim", 54: "Devarim",
}


def infer_book(source: Path) -> str:
    m = re.match(r"(\d+)-", source.name)
    if not m:
        return "Bereshit"
    return PARSHA_TO_BOOK.get(int(m.group(1)), "Bereshit")


def write_chapter(verses: list[dict], book: str, chapter: int) -> Path:
    for v in verses:
        v["ja"] = clean_ja(v["ja"])
        v["hebrew_translation"] = clean_hebrew_translation(v["hebrew_translation"])
        v["hebrew"] = re.sub(r"\s+", " ", v["hebrew"]).strip()
        v["arabic"] = re.sub(r"\s+", " ", v["arabic"]).strip()
    out = OUT_DIR / f"tafsir-{book.lower()}-{chapter}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(
            {"book": book, "chapter": chapter, "verses": verses},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                    help="Rasag-Parshiot text file (default: 01-Bereshit.txt)")
    ap.add_argument("--chapter", type=int, default=None,
                    help="Single chapter to extract; if omitted, all chapters in the file are written")
    ap.add_argument("--book", default=None,
                    help="Override book label (default: inferred from source filename)")
    args = ap.parse_args()

    if not args.source.exists():
        print(f"missing source: {args.source}", file=sys.stderr)
        return 1
    book = args.book or infer_book(args.source)
    verses = parse_file(args.source)
    if not verses:
        print("no verses parsed", file=sys.stderr)
        return 2

    chapters = sorted({v["ch"] for v in verses})
    if args.chapter is not None:
        if args.chapter not in chapters:
            print(f"chapter {args.chapter} not in source (found: {chapters})", file=sys.stderr)
            return 3
        chapters = [args.chapter]

    for ch in chapters:
        ch_verses = [v for v in verses if v["ch"] == ch]
        out = write_chapter(ch_verses, book, ch)
        print(f"wrote {len(ch_verses):>3} verses to {out.relative_to(OUT_DIR.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

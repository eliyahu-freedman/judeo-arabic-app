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
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SOURCE = Path.home() / "Desktop" / "Rasag-Parshiot" / "01-Bereshit.txt"
OUT = (
    Path(__file__).resolve().parent.parent / "data" / "tafsir-bereshit-1.json"
)

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
# Bounded to 1-2 chars per token: the source occasionally omits whitespace
# between the locator and the content (e.g. "א יגוַיְהִי..."), so a greedy
# match would over-consume. Tanakh chapters/verses up to 99 fit in 2 letters.
LOCATOR_OPENING = re.compile(
    rf"^\s*([{HEB_LETTER}]{{1,2}})(?:\s+([{HEB_LETTER}]{{1,2}}))?\)?\s*"
)


def strip_nikkud(s: str) -> str:
    return NIKKUD_RE.sub("", s)


def parse_locator(text: str) -> tuple[int | None, int | None, str]:
    """Return (ch, v, remainder). Either ch or v may be None if not present."""
    bare = strip_nikkud(text)
    m = LOCATOR_OPENING.match(bare)
    if not m:
        return None, None, text
    tok_a = m.group(1)
    tok_b = m.group(2)
    if tok_b is None:
        # Single token: probably just the verse number with trailing paren
        # (e.g. "ב) ..."). Caller will inherit ch from elsewhere.
        v = gematria(tok_a)
        ch = None
    else:
        ch = gematria(tok_a)
        v = gematria(tok_b)
    # Strip the same span from the original (preserve nikkud-bearing content).
    # The locator characters are bare Hebrew letters, so we can match the same
    # prefix on the original by recomputing how many original chars correspond.
    # Simpler: also run the regex on the original (it allows the same chars).
    om = LOCATOR_OPENING.match(text)
    remainder = text[om.end():] if om else text
    return ch, v, remainder


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
        ar_clean = re.sub(r"^\s*\d+\s*", "", ar_raw)

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


def clean_ja(text: str) -> str:
    """Strip inline manuscript variants like [ויט'הר] from the JA field."""
    prev = None
    while text != prev:
        prev = text
        text = re.sub(r"\[[^\[\]]*\]\s*", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main() -> int:
    if not SOURCE.exists():
        print(f"missing source: {SOURCE}", file=sys.stderr)
        return 1
    verses = parse_file(SOURCE)
    ch1 = [v for v in verses if v["ch"] == 1]
    if not ch1:
        print("no chapter 1 verses found", file=sys.stderr)
        return 2
    for v in ch1:
        v["ja"] = clean_ja(v["ja"])
        v["hebrew_translation"] = clean_hebrew_translation(v["hebrew_translation"])
        v["hebrew"] = re.sub(r"\s+", " ", v["hebrew"]).strip()
        v["arabic"] = re.sub(r"\s+", " ", v["arabic"]).strip()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {"book": "Bereshit", "chapter": 1, "verses": ch1},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {len(ch1)} verses to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

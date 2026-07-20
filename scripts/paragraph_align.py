"""
Refine skeleton aligned JSON into paragraph-level segments.

Reads the skeleton (one big segment per JA page) and splits each page into
one segment per English paragraph, splitting the JA text at natural Arabic
sentence/clause boundaries. Adds phrase pairs for key technical terms.

Usage:
  paragraph_align.py bab7 bab8 bab9 bab10 hakdamah
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Universal term pairs present across all gates
UNIVERSAL_TERMS: list[tuple[str, str]] = [
    ("יא אכ'י", "my brother"),
    ("קאל אלמולף", "The Author said"),
    ("אלמוסנף", "The Author"),
    ("ג'ל ועז", "(great and exalted)"),
    ("תעאלי", "(exalted)"),
    ("אלכ'אלק", "the Creator"),
    ("כ'אלקה", "his Creator"),
    ("כ'אלקנא", "our Creator"),
    ("אלאנסאן", "the person"),
    ("אלאנסאן", "man"),
    ("אלעבד", "the servant"),
    ("אלמלך", "the king"),
    ("אלנפס", "the soul"),
    ("אלעקל", "the intellect"),
    ("אלקלב", "the heart"),
    ("אלהוי", "passion"),
    ("אלדניא", "the world"),
    ("אלאכ'רה", "the afterlife"),
    ("אלשריעה", "the law"),
    ("אלרב", "the Lord"),
    ("כקולה", "as He said"),
    ("כקול אלולי", "as the pious one said"),
    ("כקול אלחכים", "as the sage said"),
    ("אלג'וארח", "the limbs"),
    ("אלטאעה", "obedience"),
    ("אלנעמה", "blessing"),
    ("אלשכר", "gratitude"),
    ("אלמחאסבה", "self-accounting"),
    ("אלאג'תהאד", "diligence"),
    ("אלאכ'לאץ", "sincerity"),
]

# Per-gate additional term pairs
GATE_TERMS: dict[str, list[tuple[str, str]]] = {
    "hakdamah": [
        ("אלחכמה", "wisdom"),
        ("אלעלום", "the sciences"),
        ("אלנט'ר", "rational investigation"),
        ("אלאצול", "the foundations"),
        ("אלפרוע", "the branches"),
        ("אלמנקול", "received tradition"),
        ("אלמעקול", "rational knowledge"),
        ("פראיץ' אלקלוב", "duties of the heart"),
        ("פראיץ' אלג'וארח", "duties of the limbs"),
        ("אלבאב", "the gate"),
        ("אלאמאנאת", "religious knowledge"),
        ("אלאשראאת", "the Scriptures"),
        ("אלאדלה", "the proofs"),
        ("אלחכים", "the wise one"),
        ("אלאמם", "the peoples"),
    ],
    "bab7": [
        ("אלתובה", "repentance"),
        ("אלנדם", "remorse"),
        ("אלתרך", "cessation"),
        ("אלאסתגפאר", "seeking forgiveness"),
        ("אלצ'מאן", "the pledge"),
        ("אלד'נוב", "the sin"),
        ("אלמד'נב", "the sinner"),
        ("אלמונב", "the penitent"),
        ("שרוט אלתובה", "conditions of repentance"),
        ("אלתאיב", "the penitent one"),
        ("אלצאלח", "the righteous"),
        ("אלמעצייה", "the transgression"),
        ("אלאנאבה", "returning"),
        ("ג'הנם", "Gehinnom"),
    ],
    "bab8": [
        ("אלוג'ה", "the aspect"),
        ("אלאכ'לאץ", "sincerity"),
        ("אלצלאה", "prayer"),
        ("אלכ'שוע", "submission"),
        ("אלנייה", "intention"),
        ("אלמחאסב", "self-accounting"),
        ("אלקיאם", "performing"),
        ("אלמראקבה", "watchfulness"),
        ("אלאטלאע", "awareness"),
        ("אלתפכר", "reflection"),
        ("אלתד'כר", "remembrance"),
        ("אלתוחיד", "monotheism"),
        ("אלאעתראף", "acknowledgment"),
        ("אלמחסוב", "the reckoned one"),
        ("אלחסאב", "the reckoning"),
    ],
    "bab9": [
        ("אלזהד", "abstinence"),
        ("אלזאהד", "the abstinent person"),
        ("אלשהוה", "desire"),
        ("אלקנאעה", "contentment"),
        ("אלמנהי ענה", "the forbidden"),
        ("אלמבאח", "the permitted"),
        ("אלדין", "religion"),
        ("אלתקוי", "piety"),
        ("אלכ'לוה", "solitude"),
        ("אלוחדה", "seclusion"),
        ("אלאמל", "hope"),
        ("אלאנפראד", "separation"),
        ("צ'ביט אלנפס", "restraint of the soul"),
    ],
    "bab10": [
        ("אלמחבה", "love"),
        ("אלמחב", "the lover"),
        ("אלמחבוב", "the Beloved"),
        ("אלכ'וף", "fear"),
        ("אלקרב", "nearness"),
        ("אלאנס", "intimacy"),
        ("אלרצ'א", "pleasure"),
        ("אלוחשה", "loneliness"),
        ("אלזהד", "abstinence"),
        ("אלאמל", "hope"),
        ("אלשוק", "longing"),
        ("אלתשוק", "yearning"),
        ("אלוג'ד", "ecstasy"),
        ("אלתוחד", "solitude with God"),
    ],
}

# Sentence-boundary patterns in Judeo-Arabic (JA written in Hebrew script).
# Each pattern marks the *start* of a new clause/sentence.
# We split just before these markers.
SPLIT_RE = re.compile(
    r"(?<=[,.])\s+(?="
    r"ת'ם\s"          # "then"
    r"|ואמא\s"        # "as for"
    r"|ולד'לך\s"      # "therefore"
    r"|פינבגי\s"      # "it is fitting"
    r"|פקד\s"         # "for indeed"
    r"|וקאל\s"        # "and he said"
    r"|קאל\s"         # "said"
    r"|ואן\s"         # "and if"
    r"|ואלוג'ה\s"     # "the [N]th aspect"
    r"|ואלוג'ה\s"     # variant
    r"|פצל\s"         # section marker
    r"|ואחרי\s"       # "how much more"
    r"|וכד'לך\s"      # "likewise"
    r"|ומן\s"         # "and from"
    r"|ויתמת'ל\s"     # "and we may use as a parable"
    r")",
    re.UNICODE,
)

# Also split at section/opening markers wherever they appear
SECTION_RE = re.compile(
    r"(?=(?:פצל\.?\s*[א-י]|פתיחה))",
    re.UNICODE,
)


def split_ja(ja_text: str, n_parts: int) -> list[str]:
    """Split JA text into ≈n_parts pieces at natural clause boundaries."""
    if n_parts <= 1:
        return [ja_text.strip()]

    # Phase 1: find candidate split positions from patterns
    candidates: list[int] = []

    for m in SECTION_RE.finditer(ja_text):
        if m.start() > 5:
            candidates.append(m.start())

    for m in SPLIT_RE.finditer(ja_text):
        candidates.append(m.end())  # split after the separator whitespace

    candidates = sorted(set(candidates))

    if len(candidates) >= n_parts - 1:
        # Evenly distribute split points
        step = len(candidates) / (n_parts - 1)
        chosen = sorted({candidates[min(int(i * step), len(candidates) - 1)] for i in range(n_parts - 1)})
    elif candidates:
        chosen = candidates
    else:
        # Fall back: split at word boundaries by character position
        total = len(ja_text)
        raw = [int(total * i / n_parts) for i in range(1, n_parts)]
        chosen = []
        for pos in raw:
            left = ja_text.rfind(" ", 0, pos)
            right = ja_text.find(" ", pos)
            if right == -1:
                chosen.append(left if left != -1 else pos)
            elif left == -1:
                chosen.append(right)
            else:
                chosen.append(left if pos - left <= right - pos else right)
        chosen = [p for p in chosen if p > 0]

    # Build parts
    parts: list[str] = []
    prev = 0
    for pos in chosen:
        chunk = ja_text[prev:pos].strip()
        if chunk:
            parts.append(chunk)
        prev = pos
    tail = ja_text[prev:].strip()
    if tail:
        parts.append(tail)

    return parts if parts else [ja_text.strip()]


def find_pairs(ja: str, en: str, slug: str) -> list[dict]:
    """Return term pairs where both the JA term and its EN equivalent appear."""
    terms = UNIVERSAL_TERMS + GATE_TERMS.get(slug, [])
    pairs: list[dict] = []
    en_lower = en.lower()
    for ja_term, en_term in terms:
        if ja_term in ja and en_term.lower() in en_lower:
            pairs.append({"ja": ja_term, "en": en_term})
    # Deduplicate (same ja_term appearing multiple times)
    seen: set[str] = set()
    deduped: list[dict] = []
    for p in pairs:
        if p["ja"] not in seen:
            seen.add(p["ja"])
            deduped.append(p)
    return deduped[:8]  # cap at 8 pairs per segment


MIN_JA_CHARS = 30  # merge segments with JA shorter than this into the next


def _merge_pair(a: dict, b: dict) -> dict:
    merged_ja = (a["ja"] + " " + b["ja"]).strip()
    merged_en = (a["en"] + "\n\n" + b["en"]).strip() if a["en"] else b["en"]
    merged_pairs = a.get("pairs", []) + b.get("pairs", [])
    seen: set[str] = set()
    deduped = []
    for p in merged_pairs:
        if p["ja"] not in seen:
            seen.add(p["ja"])
            deduped.append(p)
    return {
        "ja": merged_ja,
        "en": merged_en,
        "isHeader": a.get("isHeader", False),
        "pairs": deduped[:8],
    }


def merge_short_segments(segs: list[dict]) -> list[dict]:
    """Merge any segment whose JA is very short into an adjacent segment."""
    if len(segs) <= 1:
        return segs
    out: list[dict] = []
    i = 0
    while i < len(segs):
        seg = segs[i]
        if len(seg["ja"]) < MIN_JA_CHARS:
            if i + 1 < len(segs):
                # Merge forward into next segment
                out.append(_merge_pair(seg, segs[i + 1]))
                i += 2
            elif out:
                # Last segment — merge backward into previous
                prev = out.pop()
                out.append(_merge_pair(prev, seg))
                i += 1
            else:
                out.append(seg)
                i += 1
        else:
            out.append(seg)
            i += 1
    return out


def process_slug(slug: str) -> None:
    path = DATA_DIR / f"bahya-{slug}-aligned.json"
    if not path.exists():
        print(f"[{slug}] ERROR: {path.name} not found.")
        return

    skeleton = json.loads(path.read_text(encoding="utf-8"))
    new_pages: dict[str, list[dict]] = {}
    total_segs = 0

    for page_key, segs in skeleton["pages"].items():
        new_segs: list[dict] = []
        for seg in segs:
            ja_full: str = seg.get("ja", "")
            en_full: str = seg.get("en", "")
            is_header: bool = seg.get("isHeader", False)

            # Split EN at paragraph separators
            en_paras = [p.strip() for p in en_full.split("\n\n") if p.strip()]
            n = len(en_paras)

            if n <= 1:
                pairs = find_pairs(ja_full, en_full, slug)
                new_segs.append(
                    {"ja": ja_full, "en": en_full, "isHeader": is_header, "pairs": pairs}
                )
            else:
                ja_parts = split_ja(ja_full, n)

                # Pair JA parts with EN paragraphs.
                # If we have fewer JA parts than EN paragraphs, attach excess EN
                # to the last available JA part.
                for i, en_para in enumerate(en_paras):
                    if i < len(ja_parts):
                        ja_chunk = ja_parts[i]
                    else:
                        ja_chunk = ""  # no corresponding JA found
                    pairs = find_pairs(ja_chunk, en_para, slug)
                    new_segs.append(
                        {"ja": ja_chunk, "en": en_para, "isHeader": False, "pairs": pairs}
                    )

        # Merge any very-short JA segments into the next segment
        new_segs = merge_short_segments(new_segs)

        new_pages[page_key] = new_segs
        total_segs += len(new_segs)

    result = {
        "note": (
            f"Paragraph-level alignment for bahya-{slug}. "
            "One segment per English paragraph; JA split at clause boundaries. "
            "Phrase pairs added for key technical terms. "
            "To add hover precision: split ja into shorter clauses and refine pairs."
        ),
        "pages": new_pages,
    }
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[{slug}] {total_segs} segments across {len(new_pages)} pages → {path.name}")


def main() -> None:
    slugs = sys.argv[1:]
    if not slugs:
        sys.exit("usage: paragraph_align.py <slug> [<slug> ...]")
    for slug in slugs:
        process_slug(slug)


if __name__ == "__main__":
    main()

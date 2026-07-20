"""
Parse ~/Downloads/genizah-research/qirqisani-pipeline/sources/maqala5.txt
(trilingual: Hebrew / Arabic / English, 40 chapters) and emit per-chapter
JSON bundles for the Advanced Library reader.

Outputs (one set per sha'ar 1-40):
  data/qirqisani-m5-sha{N:02d}.json          — GateJson (Arabic paragraphs)
  data/qirqisani-m5-sha{N:02d}-english.json  — EnglishJson (flat English paragraphs)
  data/qirqisani-m5-sha{N:02d}-aligned.json  — AlignedJson (paragraph-level pairs, no phrase hover)

Run from repo root:
  python3 scripts/build_qirqisani_m5_gates.py
"""

import json
import re
import sys
from pathlib import Path

SRC = Path.home() / "Downloads" / "genizah-research" / "qirqisani-pipeline" / "sources" / "maqala5.txt"
OUTDIR = Path(__file__).resolve().parent.parent / "data"

WORK = "Kitāb al-Anwār wa'l-Marāqib"
AUTHOR = "Yaʿqūb al-Qirqisānī (10th c.)"
TRANSLATOR = "Eliyahu Freedman (working draft)"
MAQALA_SUBTITLE = "Discourse V: The Torah's Legal Commandments"


def arabic_frac(text: str) -> float:
    total = sum(1 for c in text if c.isalpha())
    if total == 0:
        return 0.0
    ar = sum(1 for c in text if '؀' <= c <= 'ۿ')
    return ar / total


def hebrew_frac(text: str) -> float:
    total = sum(1 for c in text if c.isalpha())
    if total == 0:
        return 0.0
    he = sum(1 for c in text if '֐' <= c <= '׿' or 'יִ' <= c <= 'ﭏ')
    return he / total


def primary_script(text: str) -> str:
    af = arabic_frac(text)
    hf = hebrew_frac(text)
    if af >= 0.4:
        return "ar"
    if hf >= 0.4:
        return "he"
    return "en"


def clean_para(text: str) -> str:
    text = re.sub(r'^\d+\.\s*', '', text)          # strip leading "N. "
    text = re.sub(r'^\t?•\s*', '', text)            # strip leading "• " or "\t• "
    text = re.sub(r'\{(\d+)\}\s*', '', text)        # strip inline page markers like {498}
    return text.strip()


def parse() -> list[dict]:
    """Return list of chapter dicts:
       {n, title_he, title_ar, title_en, paragraphs: [{num, ar, en}]}
    """
    lines = SRC.read_text(encoding="utf-8").splitlines()

    # Find positions of chapter markers
    marker_re = re.compile(r'^#5\.(\d+)$')
    markers = []  # [(line_index, chapter_n)]
    for i, ln in enumerate(lines):
        m = marker_re.match(ln.strip())
        if m:
            markers.append((i, int(m.group(1))))

    if not markers:
        print("ERROR: no #5.NN markers found", file=sys.stderr)
        sys.exit(1)

    chapters = []
    for k, (mi, chapter_n) in enumerate(markers):
        end_i = markers[k + 1][0] if k + 1 < len(markers) else len(lines)

        # --- extract chapter titles from lines just before the marker ---
        title_he = title_ar = title_en = ""
        j = mi - 1
        while j >= 0 and lines[j].strip() == "":
            j -= 1
        # collect up to 4 non-empty lines going back
        title_lines: list[str] = []
        while j >= 0 and lines[j].strip() != "" and len(title_lines) < 4:
            raw = lines[j].strip()
            # stop at volume-level markers ({N} prefix = these are volume, not chapter titles)
            if re.match(r'^\{?\d+\}', raw) or raw == "A":
                break
            title_lines.insert(0, raw)
            j -= 1

        for tl in title_lines:
            script = primary_script(tl)
            if script == "ar" and not title_ar:
                title_ar = tl
            elif script == "he" and not title_he:
                title_he = tl
            elif script == "en" and not title_en:
                title_en = tl

        # --- extract paragraphs (Arabic + English) from chapter body ---
        # body lines = mi+1 .. end_i
        body = lines[mi + 1:end_i]

        # Map: paragraph_num -> {ar, en}
        para_map: dict[int, dict] = {}

        for ln in body:
            ln_stripped = ln.rstrip()
            if not ln_stripped:
                continue

            # Bullet-prefixed Arabic (chapter 1 style)
            if ln_stripped.startswith("\t•") or ln_stripped.startswith("•"):
                ar_text = clean_para(ln_stripped)
                if ar_text:
                    # Assign to next available number
                    num = (max(para_map.keys()) if para_map else 0) + 1
                    para_map.setdefault(num, {"ar": "", "en": ""})
                    if not para_map[num]["ar"]:
                        para_map[num]["ar"] = ar_text
                continue

            # Numbered paragraph
            m = re.match(r'^(\d+)\.\s+', ln_stripped)
            if m:
                num = int(m.group(1))
                script = primary_script(ln_stripped)
                text = clean_para(ln_stripped)
                if not text:
                    continue
                if script == "ar":
                    para_map.setdefault(num, {"ar": "", "en": ""})
                    if not para_map[num]["ar"]:
                        para_map[num]["ar"] = text
                elif script == "en":
                    para_map.setdefault(num, {"ar": "", "en": ""})
                    if not para_map[num]["en"]:
                        para_map[num]["en"] = text
                # Hebrew paragraphs: skip (not needed in reader)

        paragraphs = [
            {"num": n, "ar": v["ar"], "en": v["en"]}
            for n, v in sorted(para_map.items())
            if v["ar"] or v["en"]
        ]

        chapters.append({
            "n": chapter_n,
            "title_he": title_he,
            "title_ar": title_ar,
            "title_en": title_en,
            "paragraphs": paragraphs,
        })

    return chapters


def ordinal_suffix(n: int) -> str:
    if 11 <= n % 100 <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def emit(chapters: list[dict]) -> None:
    OUTDIR.mkdir(exist_ok=True)
    counts = []
    for ch in chapters:
        n = ch["n"]
        slug = f"qirqisani-m5-sha{n:02d}"

        # Readable section label
        ord_sfx = ordinal_suffix(n)
        if ch["title_en"]:
            # Strip leading "The Nth chapter" prefix, keep topic
            topic = re.sub(r'^The \w+ chapter\s+(regarding|concerning|on|about|of)\s+', '', ch["title_en"], flags=re.I).strip().rstrip(".")
            section = f"Discourse V · Ch. {n}: {topic.capitalize()}"
        else:
            section = f"Discourse V · Chapter {n}"

        section_ja = ch["title_ar"] or f"باب {n}"
        subtitle = MAQALA_SUBTITLE

        arabic_paras = [p["ar"] for p in ch["paragraphs"] if p["ar"]]
        english_paras = [p["en"] for p in ch["paragraphs"] if p["en"]]

        # ---- GateJson ----
        gate = {
            "work": WORK,
            "section": section,
            "section_ja": section_ja,
            "subtitle": subtitle,
            "author": AUTHOR,
            "script": "arabic",
            "pages": [
                {
                    "page_he": str(n),
                    "paragraphs": arabic_paras,
                }
            ],
        }
        (OUTDIR / f"{slug}.json").write_text(
            json.dumps(gate, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # ---- EnglishJson ----
        english_json = {
            "translator": TRANSLATOR,
            "paragraphs": english_paras,
        }
        (OUTDIR / f"{slug}-english.json").write_text(
            json.dumps(english_json, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # ---- AlignedJson (paragraph-level, no phrase hover yet) ----
        # Match Arabic and English 1:1 by index (they're in the same order).
        min_len = min(len(arabic_paras), len(english_paras))
        aligned_segs = [
            {"ja": arabic_paras[i], "en": english_paras[i], "pairs": []}
            for i in range(min_len)
        ]
        # Any Arabic-only extras (no English counterpart yet)
        for i in range(min_len, len(arabic_paras)):
            aligned_segs.append({"ja": arabic_paras[i], "en": "", "pairs": []})

        aligned_json = {
            "pages": {str(n): aligned_segs}
        }
        (OUTDIR / f"{slug}-aligned.json").write_text(
            json.dumps(aligned_json, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        counts.append((n, len(arabic_paras), len(english_paras)))

    print(f"Emitted {len(chapters)} chapter bundles to {OUTDIR}/")
    print(f"{'Ch':>3}  {'Ar paras':>8}  {'En paras':>8}")
    for n, ar, en in counts:
        print(f"{n:>3}  {ar:>8}  {en:>8}")
    missing_en = sum(1 for _, ar, en in counts if ar != en)
    if missing_en:
        print(f"\nWARN: {missing_en} chapter(s) have mismatched Ar/En paragraph counts.")


if __name__ == "__main__":
    if not SRC.exists():
        print(f"ERROR: source not found: {SRC}", file=sys.stderr)
        sys.exit(1)
    chapters = parse()
    print(f"Parsed {len(chapters)} chapters.")
    emit(chapters)

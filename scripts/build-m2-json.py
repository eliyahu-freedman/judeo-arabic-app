#!/usr/bin/env python3
"""
Build M2 base JSON (Arabic JA) from the Cairo 2019 edition of Kitāb al-Anwār.
Also reads English and Hebrew translations from the parallel XLSX.

Source for JA: ~/Downloads/الأنوار والمراقب Arabic ed .txt
  - Babs 1-3 are missing from the Cairo ms.; a stub noting the lacuna is inserted.
  - Bab 27 is also missing from the manuscript; same treatment.
Source for English/Hebrew: qirqisani-maqala2-english/qirqisani_maqala2_parallel.xlsx
  (col 8 = Hebrew translation, col 9 = English translation)

Produces in data/:
  qirqisani-m2-bab{NN}.json          — base (Arabic JA, script: arabic)
  qirqisani-m2-bab{NN}-english.json  — English paragraphs
  qirqisani-m2-bab{NN}-hebrew.json   — Hebrew translation paragraphs
  qirqisani-m2-bab{NN}-aligned.json  — empty alignment stub

Run from repo root:
  python3 scripts/build-m2-json.py
"""

import json
import re
from pathlib import Path

import openpyxl

# ── Paths ─────────────────────────────────────────────────────────────────────
CAIRO = next(
    (p for p in (Path.home() / "Downloads").iterdir()
     if "نوار" in p.name and p.suffix == ".txt"),
    None,
)
XLSX = Path.home() / "Downloads/genizah-research/qirqisani-maqala2-english/qirqisani_maqala2_parallel.xlsx"
OUT_DIR = Path(__file__).parent.parent / "data"

# ── Constants ─────────────────────────────────────────────────────────────────
WORK      = "Kitāb al-Anwār wa'l-Marāqib"
AUTHOR    = "Yaʿqūb al-Qirqisānī (10th c.)"
SUBTITLE  = "Discourse II: Epistemology"
EN_TRANS  = "Eliyahu Freedman (working draft, 2026)"
HE_TRANS  = "Eliyahu Freedman (תרגום עברי-טברנידי, 2026)"

# Absolute byte offset of M2 body start in Cairo file
CAIRO_M2_START = 160804

# Per-bab byte spans relative to CAIRO_M2_START.
# None → bab is missing from the manuscript.
CAIRO_M2_SPANS: dict[int, tuple[int, int] | None] = {
    1:  None,               # missing from ms. (Cairo + Nemoy lacuna)
    2:  None,               # missing from ms.
    3:  None,               # missing from ms.
    4:  (1709, 2796),       # only second half in Cairo; opening in MS only
    5:  (2796, 4953),
    6:  (4953, 12092),
    7:  (12092, 21705),
    8:  (21705, 23722),
    9:  (23722, 40299),
    10: (40299, 65209),
    11: (65209, 83537),
    12: (83537, 94828),
    13: (94828, 107705),
    14: (107705, 115275),
    15: (115275, 126494),
    16: (126494, 128106),
    17: (128106, 136853),
    18: (136853, 149612),
    19: (149612, 151369),
    20: (151369, 153024),
    21: (153024, 155932),
    22: (155932, 168957),
    23: (168957, 176501),
    24: (176501, 181795),
    25: (181795, 183722),
    26: (183722, 184947),
    27: None,               # missing from manuscript
    28: (185100, 199426),
}

LACUNA_NOTE = {
    1:  "[ الباب الأول مفقود من المخطوط ومن طبعة نيموي. النص محفوظ في مخطوط يوفر-عرب. 1689 فقط. ]",
    2:  "[ الباب الثاني مفقود من المخطوط ومن طبعة نيموي. النص محفوظ في مخطوط يوفر-عرب. 1689 فقط. ]",
    3:  "[ الباب الثالث مفقود من المخطوط ومن طبعة نيموي. النص محفوظ في مخطوط يوفر-عرب. 1689 فقط. ]",
    4:  None,  # partial — just extract what Cairo has (second half only)
    27: "[ الباب السابع والعشرون مفقود من المخطوط. (المحقق) ]",
}

# Patterns for lines to drop from Cairo text
RUNHEAD_RE  = re.compile(r'الأنوار\s*والمراقب|الأنواروالمراقب|المقالت\s*الثاني')
PAGEMARK_RE = re.compile(r'^\s*[|\[]?\s*[طص]?\s*[\d٠-٩]+\s*[)\]]?\s*$')
FOOTNOTE_RE = re.compile(r'^\s*[\(（][\d٠-٩]+[\)）]')
# Paragraph-start marker: Eastern Arabic numeral sequence like ٠٢ ٠٣ or ١. ٢. at line start
PARA_NUM_RE = re.compile(r'^[٠١٢٣٤٥٦٧٨٩]\d*[\s\.]')


def is_noise(t: str) -> bool:
    """True for lines that are mostly non-Arabic (OCR noise, page numbers, etc.)."""
    if not t:
        return True
    arabic_chars = sum(1 for c in t if '؀' <= c <= 'ۿ')
    return len(t) > 8 and arabic_chars / max(len(t), 1) < 0.25


def clean_span(text: str) -> list[str]:
    """Clean a raw Cairo M2 text span → list of Arabic paragraph strings.

    Cairo M2 uses Eastern-Arabic paragraph numbers (٠١, ٠٢ …) to mark
    paragraph breaks instead of blank lines.  We split on those markers.
    """
    lines = text.splitlines()
    # Drop bab header lines (first 1-3 short lines with the bab title)
    body_lines: list[str] = []
    skipping_header = True
    for ln in lines:
        t = ln.strip()
        if skipping_header:
            if re.match(r'^الباب', t) or (t and len(t) < 70 and not PARA_NUM_RE.match(t)
                    and re.search(r'^(في |وإفساد|وفي |على |فيما |ومن )', t)):
                continue
            skipping_header = False
        body_lines.append(ln)

    body = '\n'.join(body_lines)

    # Split on paragraph number markers (٠٢ … at start of a line/word)
    # Also split on double-newlines as fallback
    chunks: list[str] = re.split(
        r'(?:^|\n)(?=[٠١٢٣٤٥٦٧٨٩]\d*[\s\.])',
        body, flags=re.MULTILINE
    )
    if len(chunks) <= 1:
        # Fallback: split on double newlines
        chunks = re.split(r'\n{2,}', body)

    paras: list[str] = []
    for chunk in chunks:
        kept: list[str] = []
        for ln in chunk.splitlines():
            t = ln.strip()
            if not t:
                continue
            if RUNHEAD_RE.search(t) and len(t) < 50:
                continue
            if PAGEMARK_RE.match(t):
                continue
            if FOOTNOTE_RE.match(t):
                continue
            if is_noise(t):
                continue
            kept.append(t)
        merged = ' '.join(kept).strip()
        if merged and len(merged) > 15:
            paras.append(merged)
    return paras


def load_xlsx_metadata() -> dict[int, dict]:
    """Read section titles, English, and Hebrew paragraphs from the parallel XLSX."""
    wb = openpyxl.load_workbook(str(XLSX), read_only=True)
    ws = wb.active

    # col 3=Index, col 8=Hebrew translation, col 9=English
    babs: dict[int, dict] = {}
    current_bab = None

    for row in ws.iter_rows(values_only=True):
        idx = row[3]
        he_text = str(row[8]).strip() if row[8] else ""
        en_text = str(row[9]).strip() if row[9] else ""

        if not idx:
            continue
        idx_str = str(idx)

        m_bab = re.match(r'^II\.(\d+)$', idx_str)
        if m_bab:
            current_bab = int(m_bab.group(1))
            babs[current_bab] = {
                "section_en": en_text,
                "section_ja": he_text,   # JA title in Hebrew script from header row
                "paragraphs_he": [],
                "paragraphs_en": [],
            }
            continue

        m_para = re.match(r'^II\.(\d+)\.\d+', idx_str)
        if m_para and current_bab is not None:
            bab_n = int(m_para.group(1))
            if bab_n != current_bab:
                current_bab = bab_n
            if he_text:
                babs[current_bab]["paragraphs_he"].append(he_text)
            if en_text:
                babs[current_bab]["paragraphs_en"].append(en_text)

    return babs


def main() -> None:
    if CAIRO is None:
        raise FileNotFoundError("Cairo edition not found in ~/Downloads/")

    cairo_text = CAIRO.read_text(encoding="utf-8", errors="replace")
    m2 = cairo_text[CAIRO_M2_START:]

    xlsx_data = load_xlsx_metadata()
    print(f"Loaded {len(xlsx_data)} babs from XLSX")

    OUT_DIR.mkdir(exist_ok=True)

    for bab_n in range(1, 29):
        nn = f"{bab_n:02d}"
        meta = xlsx_data.get(bab_n, {})
        section_en = meta.get("section_en", f"Chapter {bab_n}")
        section_ja = meta.get("section_ja", "")

        # ── JA Arabic paragraphs ──────────────────────────────────────────────
        span_info = CAIRO_M2_SPANS[bab_n]
        if span_info is None:
            note = LACUNA_NOTE.get(bab_n, f"[ الباب {bab_n} مفقود من المخطوط ]")
            ja_paras = [note]
        else:
            start, end = span_info
            span = m2[start:end]
            ja_paras = clean_span(span)
            if not ja_paras:
                ja_paras = [f"[ الباب {bab_n}: النص قصير جداً أو مفقود في هذه الطبعة ]"]

        # ── Base file (Arabic JA) ─────────────────────────────────────────────
        base = {
            "work": WORK,
            "section": f"Discourse II · Bab {bab_n}: {section_en}",
            "section_ja": section_ja,
            "subtitle": SUBTITLE,
            "author": AUTHOR,
            "script": "arabic",
            "pages": [{"page_he": str(bab_n), "paragraphs": ja_paras}],
        }
        (OUT_DIR / f"qirqisani-m2-bab{nn}.json").write_text(
            json.dumps(base, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # ── English file ──────────────────────────────────────────────────────
        en_payload = {
            "translator": EN_TRANS,
            "paragraphs": meta.get("paragraphs_en", []),
        }
        (OUT_DIR / f"qirqisani-m2-bab{nn}-english.json").write_text(
            json.dumps(en_payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # ── Hebrew file ───────────────────────────────────────────────────────
        he_payload = {
            "translator": HE_TRANS,
            "paragraphs": meta.get("paragraphs_he", []),
        }
        (OUT_DIR / f"qirqisani-m2-bab{nn}-hebrew.json").write_text(
            json.dumps(he_payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # ── Aligned stub ──────────────────────────────────────────────────────
        (OUT_DIR / f"qirqisani-m2-bab{nn}-aligned.json").write_text(
            json.dumps({"pages": {}}, ensure_ascii=False), encoding="utf-8"
        )

        print(f"  bab{nn}: {len(ja_paras)} JA paras, {len(meta.get('paragraphs_en',[]))} EN, {len(meta.get('paragraphs_he',[]))} HE")

    print(f"\nDone — {28 * 4} files written to {OUT_DIR}")


if __name__ == "__main__":
    main()

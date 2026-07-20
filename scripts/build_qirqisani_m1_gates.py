"""
Extract Maqala I babs 2–19 from the Cairo 2019 Arabic edition of Kitāb al-Anwār
and emit per-bab GateJson files for the Advanced Library reader (JA-only, no
English column yet).

Source: ~/Downloads/الأنوار والمراقب Arabic ed .txt
Output: data/qirqisani-m1-bab{N:02d}.json  for N in 2..19

Run from repo root:
  python3 scripts/build_qirqisani_m1_gates.py
"""

import json
import re
import sys
from pathlib import Path

CAIRO = next(
    (p for p in (Path.home() / "Downloads").iterdir()
     if "نوار" in p.name and p.suffix == ".txt"),
    None,
)

OUTDIR = Path(__file__).resolve().parent.parent / "data"

WORK = "Kitāb al-Anwār wa'l-Marāqib"
AUTHOR = "Yaʿqūb al-Qirqisānī (10th c.)"

# Verified character offsets into the Cairo edition file.
# Key = bab number (1-based); value = start offset of that bab's body.
# Entry 20 = start of Maqala II (acts as end sentinel for bab 19).
CAIRO_BOUNDS: dict[int, int] = {
    1:  34880,  2:  38615,  3:  55245,  4:  98051,
    5: 118945,  6: 120305,  7: 121781,  8: 122647,
    9: 130187, 10: 131350, 11: 138147, 12: 140109,
    13: 140512, 14: 144029, 15: 146689, 16: 148250,
    17: 149365, 18: 150468, 19: 152148, 20: 160804,
}

BAB_TITLES: dict[int, tuple[str, str]] = {
    2:  ("Enumeration of Jewish sects",
         "في ذكر أفاريق اليهود كل فرقة وفرقة"),
    3:  ("Doctrines distinctive to the Rabbanites",
         "فيما تفرد به الربانيون من القول الذي خالفهم فيه جميع أفاريق اليهود"),
    4:  ("Rabbanite non-legal doctrines",
         "في حكاية بعض ما قالوه في غير الوصايا مما يؤول إلى الكفر والإلحاد"),
    5:  ("Samaritan doctrine",
         "في حكاية قول السامرة"),
    6:  ("Sadducee doctrine",
         "في حكاية قول الصدوقية"),
    7:  ("Cave Sect (Maghariyya) doctrine",
         "في حكاية قول المغارية"),
    8:  ("Jesus and Christian doctrine",
         "في ذكر يسوع وحكاية قول النصارى"),
    9:  ("Qurʿiyya (Apocryphal sect)",
         "في حكاية قول القرعية"),
    10: ("Disagreements between Shāmī and Iraqi Rabbanites",
         "في ذكر ما يختلف فيه ربانيو الشأم وربانيو العراق"),
    11: ("Abū ʿĪsā al-Iṣfahānī (ʿĪsawiyya)",
         "في حكاية قول أبي عيسى الإصفهاني"),
    12: ("Yudghan al-Rāʿī (Yudghanites)",
         "في حكاية قول يودغان وهو الراعي"),
    13: ("Anan b. David (Ananites)",
         "في حكاية ما تفرد به عانان رأس الجالوت ومن تابعه"),
    14: ("Benjamin al-Nahāwandī",
         "في ذكر ما تفرد به بنيامين النهاوندي"),
    15: ("Ismaʿīl al-ʿUkbarī's errors",
         "في ذكر مساوئ إسماعيل العكبري"),
    16: ("Abū ʿImrān al-Tiflīsī and Mālik al-Ramlī",
         "في ذكر أبي عمران التفليسي وملك الرملي"),
    17: ("Mishawayh al-ʿUkbarī",
         "في حكاية ما تفرد به ميشويه"),
    18: ("Daniel al-Dāmaghānī",
         "في حكاية ما تفرد به دانيال الدامغاني"),
    19: ("Contemporary disputes among the Karaites",
         "في ذكر ما يختلف فيه القرائين في عصرنا هذا"),
}

# Patterns for lines to drop from bab content
RUNHEAD_RE  = re.compile(r'الأنوار\s*والمراقب|الأنواروالمراقب')
PAGEMARK_RE = re.compile(r'^\s*[|\[]?\s*[طص]?\s*[\d٠-٩]+\s*[)\]]?\s*$')
FOOTNOTE_RE = re.compile(r'^\s*[\(（][\d٠-٩]+[\)）]')


def clean_span(text: str) -> list[str]:
    """Clean a raw Cairo-edition span → list of non-empty paragraph strings."""
    # Split on double-newlines first to get rough paragraphs
    blocks: list[str] = re.split(r'\n{2,}', text)
    paras: list[str] = []
    for block in blocks:
        lines_kept: list[str] = []
        for ln in block.splitlines():
            t = ln.strip()
            if not t:
                continue
            if RUNHEAD_RE.search(t) and len(t) < 40:
                continue
            if PAGEMARK_RE.match(t):
                continue
            if FOOTNOTE_RE.match(t):
                continue
            lines_kept.append(t)
        merged = " ".join(lines_kept).strip()
        if merged and len(merged) > 10:   # skip tiny stubs
            paras.append(merged)
    return paras


def main() -> None:
    if CAIRO is None:
        print("ERROR: could not locate Cairo edition file", file=sys.stderr)
        sys.exit(1)

    content = CAIRO.read_text(encoding="utf-8", errors="replace")
    OUTDIR.mkdir(exist_ok=True)

    built: list[tuple[int, int]] = []
    for bab in range(2, 20):
        start = CAIRO_BOUNDS[bab]
        end   = CAIRO_BOUNDS[bab + 1]
        span  = content[start:end]
        paras = clean_span(span)

        title_en, title_ar = BAB_TITLES.get(bab, (f"Chapter {bab}", ""))

        gate: dict = {
            "work": WORK,
            "section": f"Discourse I · Ch. {bab}: {title_en}",
            "section_ja": title_ar,
            "subtitle": "Discourse I: Sectology",
            "author": AUTHOR,
            "script": "arabic",
            "pages": [
                {
                    "page_he": str(bab),
                    "paragraphs": paras,
                }
            ],
        }

        out = OUTDIR / f"qirqisani-m1-bab{bab:02d}.json"
        out.write_text(json.dumps(gate, ensure_ascii=False, indent=2), encoding="utf-8")
        built.append((bab, len(paras)))

    print(f"Built {len(built)} bab files in {OUTDIR}/")
    for bab, n in built:
        print(f"  bab {bab:2d}: {n} paragraphs")


if __name__ == "__main__":
    main()

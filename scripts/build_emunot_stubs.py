#!/usr/bin/env python3
"""
Build JA-only stub WorkData JSON files for all Emunot v'Deot fuṣūl.
Each maamar's header page (fusul_id=None) is prepended to that maamar's
first fuṣūl. Maamar 1 fuṣūl are left as stubs (English to be authored
interactively); all others get paragraphs[] only.

Output: data/saadia-emunot-m{M}f{N}.json
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT      = Path(__file__).parent.parent
MANIFEST  = ROOT / "data-source" / "saadia-emunot" / "page-manifest.json"
DATA_OUT  = ROOT / "data"

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

# Maamar FJMS id → (maamar number 1-10, slug prefix "m1".."m10", English title)
MAAMAR_META = {
    15740: (1,  "Maamar I: All Created Things Are Newly-Made"),
    15746: (2,  "Maamar II: The Creator Is One"),
    15761: (3,  "Maamar III: Divine Command & Prohibition"),
    15773: (4,  "Maamar IV: Obedience, Free Will & Justice"),
    15781: (5,  "Maamar V: Works, Merits & Recompense"),
    15790: (6,  "Maamar VI: The Soul"),
    15799: (7,  "Maamar VII: Resurrection in This World"),
    15809: (8,  "Maamar VIII: Salvation & Redemption"),
    15819: (9,  "Maamar IX: Reward & Punishment in the World to Come"),
    15831: (10, "Maamar X: The Good Life"),
}

# Fuṣūl titles (slug → English short title for the section field)
FUSUL_TITLES: dict[str, str] = {
    # Maamar 1
    "m1f1": "I:1 · Proof, Not Perception",
    "m1f2": "I:2 · Four Proofs for Creation",
    "m1f3": "I:3 · Twelve Cosmogonies",
    "m1f4": "I:4 · Refutation of All Views",
    "m1f5": "I:5 · Creation from Nothing",
    # Maamar 2
    "m2f1":  "II:1 · One Creator",
    "m2f2":  "II:2 · Not Two Principles",
    "m2f3":  "II:3 · Not a Body",
    "m2f4":  "II:4 · One in All Respects",
    "m2f5":  "II:5 · Unlike His Creatures",
    "m2f6":  "II:6 · Attributes of Action",
    "m2f7":  "II:7 · Divine Names",
    "m2f8":  "II:8 · He Is Living",
    "m2f9":  "II:9 · He Is Powerful",
    "m2f10": "II:10 · He Is Knowing",
    "m2f11": "II:11 · The Three Attributes",
    "m2f12": "II:12 · Apparent Plurality",
    "m2f13": "II:13 · Between Unity & Trinity",
    "m2f14": "II:14 · Against All Dualism",
    # Maamar 3
    "m3f1":  "III:1 · Rational Precepts",
    "m3f2":  "III:2 · Revealed Precepts",
    "m3f3":  "III:3 · Why Revelation Needed",
    "m3f4":  "III:4 · Gratitude & Reverence",
    "m3f5":  "III:5 · Forbidden Acts",
    "m3f6":  "III:6 · The Permitted & Forbidden",
    "m3f7":  "III:7 · Categories of Precepts",
    "m3f8":  "III:8 · The Great Category",
    "m3f9":  "III:9 · The Eighth Category",
    "m3f10": "III:10 · The Tenth Category",
    "m3f11": "III:11 · Concluding Survey",
    # Maamar 4
    "m4f1":  "IV:1 · Human Capacity",
    "m4f2":  "IV:2 · Acts & Omissions",
    "m4f3":  "IV:3 · Punishment & Justice",
    "m4f4":  "IV:4 · Divine Justice",
    "m4f5":  "IV:5 · Free Will Defended",
    "m4f6":  "IV:6 · Foreknowledge & Freedom",
    "m4f7":  "IV:7 · Resolution",
    # Maamar 5
    "m5f1":  "V:1 · Works of Obedience",
    "m5f2":  "V:2 · Works of Disobedience",
    "m5f3":  "V:3 · Mixed Works",
    "m5f4":  "V:4 · Repentance",
    "m5f5":  "V:5 · The Inadvertent",
    "m5f6":  "V:6 · Against Antinomians",
    "m5f7":  "V:7 · Righteous Suffering",
    "m5f8":  "V:8 · Summary",
    # Maamar 6
    "m6f1":  "VI:1 · Soul's Nature",
    "m6f2":  "VI:2 · Between Soul & Body",
    "m6f3":  "VI:3 · Soul's Location",
    "m6f4":  "VI:4 · Soul After Death",
    "m6f5":  "VI:5 · Soul's Origin",
    "m6f6":  "VI:6 · The Divine Portion",
    "m6f7":  "VI:7 · Intermediate State",
    "m6f8":  "VI:8 · Soul's Destiny",
    # Maamar 7
    "m7f1":  "VII:1 · First Redemption",
    "m7f2":  "VII:2 · Proofs from Scripture",
    "m7f3":  "VII:3 · Nature of the Body",
    "m7f4":  "VII:4 · Duration of Life",
    "m7f5":  "VII:5 · The Messianic Era",
    "m7f6":  "VII:6 · The Return to Dust",
    "m7f7":  "VII:7 · Between Eras",
    "m7f8":  "VII:8 · Ninth Category",
    "m7f9":  "VII:9 · Final Matters",
    # Maamar 8
    "m8f1":  "VIII:1 · Four Stages of Redemption",
    "m8f2":  "VIII:2 · Proofs for Redemption",
    "m8f3":  "VIII:3 · The Redeemer's Sign",
    "m8f4":  "VIII:4 · Duration of Exile",
    "m8f5":  "VIII:5 · The Nations",
    "m8f6":  "VIII:6 · Against Despair",
    "m8f7":  "VIII:7 · Prophetic Testimony",
    "m8f8":  "VIII:8 · Divine Promise",
    "m8f9":  "VIII:9 · Summary",
    # Maamar 9
    "m9f1":  "IX:1 · The World to Come",
    "m9f2":  "IX:2 · Proof from Scripture",
    "m9f3":  "IX:3 · Categories of the Next World",
    "m9f4":  "IX:4 · Degrees of Bliss",
    "m9f5":  "IX:5 · The Intermediate State",
    "m9f6":  "IX:6 · Between",
    "m9f7":  "IX:7 · Eternal Fire",
    "m9f8":  "IX:8 · Duration of Punishment",
    "m9f9":  "IX:9 · The Tenth Degree",
    "m9f10": "IX:10 · Final Bliss",
    "m9f11": "IX:11 · Summary",
    # Maamar 10
    "m10f1":  "X:1 · Three Impulses",
    "m10f2":  "X:2 · Rational Soul",
    "m10f3":  "X:3 · The Active Virtues",
    "m10f4":  "X:4 · Humility",
    "m10f5":  "X:5 · Liberality",
    "m10f6":  "X:6 · Courage",
    "m10f7":  "X:7 · Truth",
    "m10f8":  "X:8 · Self-Restraint",
    "m10f9":  "X:9 · Industriousness",
    "m10f10": "X:10 · Justice",
    "m10f11": "X:11 · Avoidance of Harm",
    "m10f12": "X:12 · Love of God",
    "m10f13": "X:13 · Love of Neighbor",
    "m10f14": "X:14 · The Active Life",
    "m10f15": "X:15 · The Contemplative Life",
    "m10f16": "X:16 · Abstinence",
    "m10f17": "X:17 · Fear of God",
    "m10f18": "X:18 · Hope & Trust",
    "m10f19": "X:19 · Submission",
    "m10f20": "X:20 · Closing Exhortation",
}

# Build per-maamar page groups from the manifest
# Step 1: group pages by maamar
maamar_pages: dict[int, list[dict]] = defaultdict(list)
header_pages: dict[int, list[dict]] = defaultdict(list)  # maamar_id → pages with fusul_id=None

for entry in manifest:
    mid = entry["maamar_id"]
    if mid not in MAAMAR_META:
        continue  # intro, appendix — skip
    if entry["fusul_id"] is None:
        header_pages[mid].append(entry)
    else:
        maamar_pages[mid].append(entry)

# Step 2: within each maamar, group by fusul_id in order
def build_fusul_groups(mid: int):
    pages = maamar_pages[mid]
    headers = header_pages.get(mid, [])
    # Pages are already in chain order (manifest preserves chain order)
    groups: list[list[dict]] = []
    current_fusul: int | None = None
    current_pages: list[dict] = []
    for p in pages:
        if p["fusul_id"] != current_fusul:
            if current_pages:
                groups.append(current_pages)
            current_fusul = p["fusul_id"]
            current_pages = []
        current_pages.append(p)
    if current_pages:
        groups.append(current_pages)
    # Prepend header pages to the first group
    if headers and groups:
        groups[0] = headers + groups[0]
    elif headers:
        groups = [headers]
    return groups

def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    # Remove leading "פרק. N." header line
    text = re.sub(r'^פרק[. ]+[א-ת]+[. ]*\n?', '', text).strip()
    return text

# Step 3: emit stub JSON files
written = 0
for mid, (mnum, maamar_en) in sorted(MAAMAR_META.items(), key=lambda x: x[1][0]):
    groups = build_fusul_groups(mid)
    for fi, group in enumerate(groups, start=1):
        slug = f"m{mnum}f{fi}"
        title = FUSUL_TITLES.get(slug, f"{slug} · [title TBD]")
        out_path = DATA_OUT / f"saadia-emunot-{slug}.json"

        pages_out = []
        for p in group:
            text = clean_text(p["cleanedText"])
            paras = [s.strip() for s in re.split(r'\n{2,}', text) if s.strip()]
            if not paras and text:
                paras = [text]
            pages_out.append({
                "page_he": p["page_he"],
                "paragraphs": paras,
            })

        data = {
            "work": "Emunot v'Deot",
            "section": title,
            "section_ja": f"מאמר {'אבגדהוזחטי'[mnum-1]}",
            "subtitle": "כתאב אלאמאנאת ואלאעתקאדאת — The Book of Beliefs and Opinions",
            "author": "Saadia Gaon (882–942)",
            "english_translator": "Eliyahu Freedman (working draft)",
            "source": f"FJMS resourceId 13, Maamar {mnum}, fuṣūl {fi}",
            "pages": pages_out,
        }
        out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        written += 1
        page_range = f"{group[0]['page_he']}–{group[-1]['page_he']}" if len(group) > 1 else group[0]['page_he']
        print(f"  {slug}: {len(group)}pp ({page_range}) → {out_path.name}")

print(f"\nWrote {written} stub files.")

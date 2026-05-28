#!/usr/bin/env python3
"""
One-shot migration: split Saadia-specific commentary out of `notes` and
`gloss_en` and into a new `saadia_note` field on lookup-dictionary entries.

Why: the lookup dictionaries (data/dictionary-starter.json,
data/dictionary-lane.json) feed BOTH the Tafsir reader and the Advanced
library reader (Bahya, Kuzari, Rambam Moreh, Qirqisani, etc.) via
lib/lookup.ts. Until now, Saadia-attribution lived in the `notes` field
or sometimes inside `gloss_en` itself ("(Saadia's gloss for X) Y"), so a
user tapping a word inside Rambam's Moreh would see Saadia-flavored
commentary. The Advanced reader has no business mentioning Saadia.

After this migration:
  - `notes` contains only generic/classical content (no "Saadia", "Tafsir",
    "סעדיה", "תפסיר", "signature rendering", "divergence card", etc.)
  - `saadia_note` contains everything that was Saadia-specific
  - `gloss_en` parentheticals like "(Saadia's gloss for X)" are stripped
  - A small set of entries (mustabhira, jalad) get `scope: "saadia"` because
    their primary gloss is itself a Saadia coinage / semantic shift

Rendering layer:
  - app/tafsir/reader.tsx  → renders both `notes` and `saadia_note`
  - app/advanced/reader.tsx → renders only `notes`, and filters out
    entries with `scope: "saadia"` entirely

Run from repo root: python3 scripts/scope_saadia_notes.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
STARTER_PATH = REPO / "data" / "dictionary-starter.json"
LANE_PATH = REPO / "data" / "dictionary-lane.json"

# Sentence-level needles. If a sentence in `notes` matches any of these
# (case-sensitive for Hebrew, case-insensitive for English), it gets moved
# from `notes` to `saadia_note`.
SAADIA_NEEDLES_EN = re.compile(
    r"saadia|tafsir|signature rendering|signature gloss|signature\b|divergence card|anti-anthropomorphic|anti-mystical|anti-idolatry|stock rendering|saadianic|saadia v\.",
    re.IGNORECASE,
)
SAADIA_NEEDLES_HE_AR = re.compile(r"סעדיה|תפסיר")

# Matches a "; (Saadia ...) trailing-text" segment anywhere in gloss_en —
# the parenthetical (group 1) plus the immediately following sense-fragment
# up to the next `;` or end-of-string (group 2). We strip the entire match
# from gloss_en and lift the captured pieces into saadia_note.
#
# Handles both:
#   "X; (Saadia's gloss for Y) Z"                         (tail)
#   "X; (Saadia's gloss for Y) Z; W"                      (embedded)
#   "X; (Saadia's denominative of najisun 'unclean')"     (no trailing prose)
GLOSS_TAIL_PAT = re.compile(
    r"\s*;\s*\(([^)]*Saadia[^)]*)\)([^;]*)",
    re.IGNORECASE,
)


def split_sentences(text: str) -> list[str]:
    """Split notes-field text into sentences on '. ' boundaries.

    Protects common abbreviations ("e.g.", "i.e.", "cf.", "vol.")
    via sentinel substitution so we don't split mid-citation like
    "(e.g. Num 12:8…)".
    """
    ABBREV = {
        "e.g.": "e\x00g\x00",
        "i.e.": "i\x00e\x00",
        "cf.": "cf\x00",
        "vol.": "vol\x00",
        "esp.": "esp\x00",
        "ch.": "ch\x00",
        "vv.": "vv\x00",
        "v.": "v\x00",
        "vs.": "vs\x00",
    }
    protected = text
    for k, v in ABBREV.items():
        protected = protected.replace(k, v)
    parts = re.split(r"(?<=\.)\s+(?=[A-ZʿʾāīūĀĪŪא-ת])", protected)
    out: list[str] = []
    for p in parts:
        for v, k in {v: k for k, v in ABBREV.items()}.items():
            p = p.replace(v, k)
        p = p.strip()
        if p:
            out.append(p)
    return out


def is_saadia_sentence(sent: str) -> bool:
    return bool(SAADIA_NEEDLES_EN.search(sent) or SAADIA_NEEDLES_HE_AR.search(sent))


def split_notes(notes: str) -> tuple[str, str]:
    """Returns (cleaned_notes, saadia_extract). Either may be empty."""
    sentences = split_sentences(notes)
    classical: list[str] = []
    saadia: list[str] = []
    for s in sentences:
        (saadia if is_saadia_sentence(s) else classical).append(s)
    return " ".join(classical).strip(), " ".join(saadia).strip()


def split_gloss_en(gloss_en: str) -> tuple[str, str]:
    """Strip Saadia-attribution segments from gloss_en. Returns
    (cleaned_gloss, saadia_extract). The Saadia segment may be tail or
    embedded; everything else in gloss_en is preserved verbatim."""
    extracts: list[str] = []

    def collect(m: re.Match[str]) -> str:
        paren_text = m.group(1).strip()
        trailing = m.group(2).strip()
        if trailing:
            extracts.append(f"{paren_text} — {trailing.rstrip('.')}.")
        else:
            extracts.append(f"{paren_text.rstrip('.')}.")
        return ""  # remove the entire matched segment from gloss_en

    cleaned = GLOSS_TAIL_PAT.sub(collect, gloss_en)
    # Collapse double-spaces / leading-semicolons left behind.
    cleaned = re.sub(r"\s*;\s*;\s*", "; ", cleaned)
    cleaned = cleaned.rstrip().rstrip(";").rstrip()
    return cleaned, " ".join(extracts).strip()


def merge_saadia(extract: str, existing: str) -> str:
    """Combine a gloss-extracted Saadia fragment with notes-extracted text."""
    parts = [p.strip() for p in (extract, existing) if p and p.strip()]
    if not parts:
        return ""
    out = " ".join(parts).strip()
    # Make sure the combined string ends with a period
    if out and not out.endswith((".", "!", "?")):
        out += "."
    return out


# Entries whose PRIMARY gloss is itself a Saadia coinage / semantic shift,
# so they should be suppressed entirely in the Advanced reader.
# (jalad glosses רקיע as "firmament" — classical جلد is "skin/hide".
# mustabhira "sea-like" is Saadia's coinage for בהו.)
SAADIA_SCOPED_IDS = {"jalad", "mustabhira"}


def migrate_entries(entries: list[dict]) -> tuple[int, int, int]:
    """Mutate entries in place. Returns (changed, gloss_changed, scoped)."""
    changed = 0
    gloss_changed = 0
    scoped = 0
    for e in entries:
        gloss_en = e.get("gloss_en", "") or ""
        notes = e.get("notes", "") or ""
        new_gloss, gloss_saadia = split_gloss_en(gloss_en)
        new_notes, notes_saadia = split_notes(notes)
        combined_saadia = merge_saadia(gloss_saadia, notes_saadia)

        touched = False
        if new_gloss != gloss_en:
            e["gloss_en"] = new_gloss
            gloss_changed += 1
            touched = True
        if combined_saadia:
            # If there's already a saadia_note (shouldn't happen on first run),
            # preserve it by prepending.
            if e.get("saadia_note"):
                e["saadia_note"] = (e["saadia_note"].rstrip(".") + ". " + combined_saadia).strip()
            else:
                e["saadia_note"] = combined_saadia
            touched = True
        if new_notes != notes:
            if new_notes:
                e["notes"] = new_notes
            elif "notes" in e:
                del e["notes"]
            touched = True
        if e["id"] in SAADIA_SCOPED_IDS and e.get("scope") != "saadia":
            e["scope"] = "saadia"
            scoped += 1
            touched = True

        if touched:
            changed += 1
    return changed, gloss_changed, scoped


def reorder_keys(e: dict) -> dict:
    """Keep a stable field order so git diffs read naturally."""
    order = [
        "id",
        "lemma_ja",
        "lemma_ar",
        "root",
        "pos",
        "gloss_en",
        "gloss_he",
        "notes",
        "saadia_note",
        "scope",
        "source",
        "variants",
    ]
    out = {k: e[k] for k in order if k in e}
    # Anything not in the canonical order goes last (defensive).
    for k, v in e.items():
        if k not in out:
            out[k] = v
    return out


def process(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data["entries"]
    changed, gloss_changed, scoped = migrate_entries(entries)
    data["entries"] = [reorder_keys(e) for e in entries]
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"{path.name}: {changed}/{len(entries)} entries updated "
        f"({gloss_changed} gloss_en rewrites, {scoped} scope:saadia tags)"
    )


def verify(path: Path) -> int:
    """Grep result fields for residual Saadia mentions. Returns hit count."""
    data = json.loads(path.read_text(encoding="utf-8"))
    hits = 0
    for e in data["entries"]:
        for field in ("gloss_en", "gloss_he", "notes"):
            val = e.get(field, "") or ""
            if SAADIA_NEEDLES_EN.search(val) or SAADIA_NEEDLES_HE_AR.search(val):
                print(f"  RESIDUAL: {path.name} id={e['id']} {field}: {val[:120]}")
                hits += 1
    return hits


if __name__ == "__main__":
    process(STARTER_PATH)
    process(LANE_PATH)
    print()
    print("Verification — residual Saadia mentions in cross-text fields:")
    residual = verify(STARTER_PATH) + verify(LANE_PATH)
    print(f"Total residual hits: {residual}")

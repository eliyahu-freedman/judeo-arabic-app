"""Deterministic polish pass over draft English sidecars for the Tafsir reader.

Applies targeted find/replace fixes for systematic translation issues identified
in a corpus audit of the 187 chapter sidecars produced by translate_tafsir_english.py.

Fixes applied:
  1. תכלימא masdar tawkid calques. The model rendered Saadia's masdar absolute
     after כלם as "with a speaking" / ", speaking." / ", speaking to him.".
     Normalize to "directly" — preserves Saadia's distinct verb-emphasis without
     the awkward English calque. Reverse-translatability is preserved: a reader
     who taps תכלימא in the JA sees "directly" and can map back.
  2. "tent of the meeting-place" → "tent of the assembly" (model's dominant
     rendering of אלמחצ'ר, 79× corpus-wide).
  3. "tent of the meeting" → "tent of meeting" (drop extra "the" — English idiom).
  4. "with full speech" → "directly" (one outlier of #1).
  5. רפיעה normalization: prefer "raised-offering" (8 hits) over "elevated-offering"
     (5 hits). Same JA stem ר־פ־ע, same semantic.
  6. Bump _status from "draft" to "revised" and stamp _polish_pass with timestamp.

Run:
    python3 scripts/polish_tafsir_english.py            # apply + report
    python3 scripts/polish_tafsir_english.py --dry-run  # report only
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


# Order matters: longer/more-specific patterns must come first so they don't get
# eaten by a shorter match. Each entry is (description, regex, replacement).
REPLACEMENTS: list[tuple[str, re.Pattern[str], str]] = [
    # תכלימא — masdar tawkid after Saadia's כלם. Replace the calque chunk.
    ("taklīm: ' with a speaking.'", re.compile(r" with a speaking\."), " directly."),
    ("taklīm: ', speaking to him directly.'", re.compile(r", speaking to him directly\."), " directly."),
    ("taklīm: ', speaking to them directly.'", re.compile(r", speaking to them directly\."), " directly."),
    ("taklīm: ', speaking to him.'", re.compile(r", speaking to him\."), " directly."),
    ("taklīm: ', speaking to them.'", re.compile(r", speaking to them\."), " directly."),
    ("taklīm: ', speaking.'", re.compile(r", speaking\."), " directly."),
    ("taklīm: ', with full speech.'", re.compile(r", with full speech\."), " directly."),

    # אלמחצ'ר wording variants — normalize the awkward "meeting-place" hybrids.
    # Keep "tabernacle" and "tent of the assembly" untouched (those are deeper
    # terminology calls best handled in the LLM polish pass).
    ("mahdar: 'tent of the meeting-place'", re.compile(r"tent of the meeting-place"), "tent of the assembly"),
    ("mahdar: 'tent of the meeting'", re.compile(r"tent of the meeting(?!-place)\b"), "tent of meeting"),

    # רפיעה — unify "elevated-offering" → "raised-offering" (dominant rendering).
    ("rafīʿa: 'elevated-offering'", re.compile(r"elevated-offering"), "raised-offering"),
    ("rafīʿa: 'elevated offering'", re.compile(r"elevated offering"), "raised-offering"),
]


def polish_text(text: str, counts: dict[str, int]) -> str:
    new = text
    for label, rx, repl in REPLACEMENTS:
        new, n = rx.subn(repl, new)
        if n:
            counts[label] = counts.get(label, 0) + n
    return new


def polish_file(path: Path, counts: dict[str, int], dry_run: bool) -> bool:
    """Polish one English sidecar. Returns True if the file changed."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    translations = payload.get("translations", {})
    changed = False
    new_trans: dict[str, str] = {}
    for v, en in translations.items():
        new_en = polish_text(en, counts)
        if new_en != en:
            changed = True
        new_trans[v] = new_en
    if changed and not dry_run:
        payload["translations"] = new_trans
        payload["_status"] = "revised"
        payload["_polish_pass"] = str(date.today())
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true",
                    help="Report counts without writing files.")
    ap.add_argument("--book", help="Limit to one book (bereshit/shemot/vayikra/bamidbar/devarim).")
    args = ap.parse_args()

    pattern = "tafsir-*-english.json"
    if args.book:
        pattern = f"tafsir-{args.book.lower()}-*-english.json"

    files = sorted(DATA_DIR.glob(pattern))
    if not files:
        print(f"no sidecar files matched {pattern}", file=sys.stderr)
        return 1

    counts: dict[str, int] = {}
    changed_files = 0
    for f in files:
        if polish_file(f, counts, args.dry_run):
            changed_files += 1

    print(f"{'[dry-run] ' if args.dry_run else ''}Polish pass over {len(files)} chapters.")
    print(f"Files changed: {changed_files}")
    print()
    if not counts:
        print("No matches — corpus already polished.")
        return 0
    print("Replacements applied:")
    for label, _, _ in REPLACEMENTS:
        if label in counts:
            print(f"  {counts[label]:5d}  {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

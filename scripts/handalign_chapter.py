"""Generic offline driver for hand-authored tafsir alignments.

Loads scripts/align_data/{book}_{chapter}.py (which must export an
ALIGNMENTS dict mapping verse-number → list of (he|None, ja, en) triples),
validates each triple against data/tafsir-{book}-{chapter}.json +
-english.json with a per-side sequential cursor (tolerant of non-canonical
Hebrew niqqud order via NFC matching), and writes
data/tafsir-{book}-{chapter}-alignment.json with source-exact HE substrings.

Run:
    python3 scripts/handalign_chapter.py --book shemot --chapter 2
    python3 scripts/handalign_chapter.py --book shemot --chapter 2 --write

Without --write, validates only and reports.
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def load_alignments(book: str, chapter: int) -> dict[int, list[tuple]]:
    mod = importlib.import_module(f"align_data.{book}_{chapter}")
    return mod.ALIGNMENTS


def load_sources(book: str, chapter: int) -> tuple[dict, dict[str, str]]:
    src = json.loads(
        (DATA_DIR / f"tafsir-{book}-{chapter}.json").read_text(encoding="utf-8"),
    )
    en = json.loads(
        (DATA_DIR / f"tafsir-{book}-{chapter}-english.json").read_text(
            encoding="utf-8",
        ),
    )["translations"]
    return src, en


class Side:
    """Per-side matching state: claimed ranges + a forward cursor.

    Mirrors `claim` in lib/alignment.ts so authoring validation matches the
    runtime resolver: prefer the leftmost unclaimed occurrence at/after the
    cursor (advancing it), else fall back to the leftmost unclaimed
    occurrence anywhere (without moving the cursor). The forward preference
    keeps short anchors matching in reading order; the backward fallback lets
    a word reach its counterpart across a word-order crossing.
    """

    def __init__(self) -> None:
        self.claimed: list[tuple[int, int]] = []
        self.cursor = 0

    def _free(self, idx: int, end: int) -> bool:
        return not any(idx < c1 and end > c0 for c0, c1 in self.claimed)

    def claim(self, text: str, needle: str) -> int:
        """Return the start index of the claimed occurrence, or -1."""
        n = len(needle)
        frm = self.cursor
        while True:
            idx = text.find(needle, frm)
            if idx == -1:
                break
            if self._free(idx, idx + n):
                self.claimed.append((idx, idx + n))
                self.cursor = idx + n
                return idx
            frm = idx + 1
        frm = 0
        while True:
            idx = text.find(needle, frm)
            if idx == -1:
                return -1
            if self._free(idx, idx + n):
                self.claimed.append((idx, idx + n))
                return idx
            frm = idx + 1


def claim_he(needle: str, haystack: str, side: Side) -> tuple[int, str | None]:
    """Claim a Hebrew needle tolerant of canonical-combining-mark reorder.

    Sefaria sometimes stores marks non-canonically (e.g. SHIN-DOT before
    HIRIQ). NFC of either form is identical and length-preserving for
    Hebrew (no precomposition), so we match/claim against the NFC form and
    slice from the untouched source — the written JSON then round-trips
    against the raw source for the runtime resolver.
    """
    n_needle = unicodedata.normalize("NFC", needle)
    n_hay = unicodedata.normalize("NFC", haystack)
    idx = side.claim(n_hay, n_needle)
    if idx == -1:
        return -1, None
    return idx, haystack[idx : idx + len(n_needle)]


def validate(
    book: str,
    chapter: int,
) -> tuple[list[str], int, dict[int, list[tuple[str | None, str, str]]]]:
    alignments = load_alignments(book, chapter)
    src, en = load_sources(book, chapter)

    problems: list[str] = []
    total = 0
    resolved: dict[int, list[tuple[str | None, str, str]]] = {}
    by_v = {v["v"]: v for v in src["verses"]}

    for vnum, triples in alignments.items():
        if vnum not in by_v:
            problems.append(f"v{vnum}: not in source")
            continue
        he_full = by_v[vnum]["hebrew"]
        ja_full = by_v[vnum]["ja"]
        en_full = en.get(str(vnum), "")
        he_side, ja_side, en_side = Side(), Side(), Side()
        resolved_v: list[tuple[str | None, str, str]] = []
        for i, (he, ja, en_phrase) in enumerate(triples):
            ji = ja_side.claim(ja_full, ja)
            if ji == -1:
                problems.append(
                    f"v{vnum} pair {i}: JA {ja!r} has no free occurrence "
                    f"in {ja_full!r}",
                )
                continue
            ei = en_side.claim(en_full, en_phrase)
            if ei == -1:
                problems.append(
                    f"v{vnum} pair {i}: EN {en_phrase!r} has no free "
                    f"occurrence in {en_full!r}",
                )
                continue
            he_exact: str | None = None
            if he:
                hi, sliced = claim_he(he, he_full, he_side)
                if hi == -1:
                    problems.append(
                        f"v{vnum} pair {i}: HE {he!r} has no free occurrence "
                        f"in {he_full!r}",
                    )
                    continue
                he_exact = sliced
            resolved_v.append((he_exact, ja, en_phrase))
            total += 1
        resolved[vnum] = resolved_v
    return problems, total, resolved


def write_sidecar(
    book: str,
    chapter: int,
    resolved: dict[int, list[tuple[str | None, str, str]]],
) -> Path:
    out_path = DATA_DIR / f"tafsir-{book}-{chapter}-alignment.json"
    alignments_json: dict[str, list[dict]] = {}
    for vnum, triples in resolved.items():
        rows = []
        for he, ja, en in triples:
            row: dict[str, str] = {"ja": ja, "en": en}
            if he:
                row["he"] = he
            rows.append(row)
        alignments_json[str(vnum)] = rows
    payload = {
        "_note": (
            f"Hebrew↔JA↔EN phrase-triple alignment for {book.title()} "
            f"{chapter}. Hand-authored (no API) via "
            "scripts/handalign_chapter.py + "
            f"scripts/align_data/{book}_{chapter}.py; validated against the "
            "source with independent per-side occurrence claiming."
        ),
        "_status": "draft",
        "_model": "hand-authored",
        "alignments": alignments_json,
    }
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    # Ensure align_data/ is importable when invoked from any cwd.
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    problems, total, resolved = validate(args.book, args.chapter)
    for p in problems:
        print("  ! " + p, file=sys.stderr)
    print(
        f"[{args.book} {args.chapter}] {total} pairs valid; "
        f"{len(problems)} problem(s)",
    )
    if problems:
        return 2
    if args.write:
        out = write_sidecar(args.book, args.chapter, resolved)
        print(f"wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

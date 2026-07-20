"""Generate JA↔EN word-level alignment pairs for Advanced Reader segments via Claude.

Reads a moreh-bab*.json (or any Advanced Reader work JSON) and generates
fine-grained {ja, en} pairs for each aligned segment, then writes them back
into the source file's `aligned[i].pairs` arrays in place.

The same approach as scripts/align_tafsir_english.py but for the Advanced
Reader (JA+EN only, no Hebrew; paragraphs not verses; word-level granularity).

Usage:
    export ANTHROPIC_API_KEY=...
    python3 scripts/align_advanced_reader.py --file data/moreh-bab69.json
    python3 scripts/align_advanced_reader.py --file data/moreh-bab69.json --dry-run
    python3 scripts/align_advanced_reader.py --all   # all moreh-bab*.json files
    python3 scripts/align_advanced_reader.py --all --pattern "bahya-*.json"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 8000

SYSTEM_INSTRUCTIONS = """You are aligning Judeo-Arabic (in Hebrew letters) and English at the word level. The output drives a reader UI: hovering a single JA word highlights its English correspondent, and vice versa.

OUTPUT FORMAT — strict JSON, no preamble, no markdown fences:
{"alignments": {"0": [{"ja": "...", "en": "..."}, ...], "1": [...], ...}}

Keys are segment indices (strings: "0", "1", …) matching the input. Each value is an ordered list of {ja, en} pairs.

Hard rules:

1. SUBSTRING. Each pair's `ja` must appear character-for-character in that segment's JA text, and `en` must appear character-for-character in the English text. No paraphrasing, no normalization, no added or removed characters. Copy verbatim.

2. LEFT-TO-RIGHT ON BOTH SIDES. The validator walks each side with a running cursor. For the N-th pair it looks for `ja` at or after the previous JA cursor, and `en` at or after the previous EN cursor. Pairs MUST therefore appear in increasing position on BOTH sides. Where Arabic word order differs from English (e.g. Arabic verb-initial "יסמון אללה" vs English noun-initial "call God"), bundle that unit as ONE multi-word pair rather than two cross-ordered pairs.

3. GRANULARITY — THIS IS THE MOST CRITICAL RULE. Every pair must be as small as possible: 1 JA word → 1–3 EN words is the target. A user hovers ONE JA word and should see ONE short English correspondent highlight — not a whole clause.

   THE CORE TEST: If Arabic and English share the same left-to-right word order for a stretch, you MUST split that stretch into individual word pairs. Bundling same-order words into one pair is always wrong.

   CONCRETE EXAMPLES OF WHAT NOT TO DO:

   BAD (same word order — must split):
   {"ja": "יהרבון מן הד'ה אלאסמיה ג'דא", "en": "flee from this designation entirely"}
   CORRECT:
   {"ja": "יהרבון", "en": "flee"},
   {"ja": "מן הד'ה אלאסמיה", "en": "from this designation"},
   {"ja": "ג'דא", "en": "entirely"}

   BAD (same word order — must split):
   {"ja": "לאן אלפאעל קד יתקדם פעלה", "en": "since the agent may precede his act"}
   CORRECT:
   {"ja": "לאן", "en": "since"},
   {"ja": "אלפאעל", "en": "the agent"},
   {"ja": "קד יתקדם", "en": "may precede"},
   {"ja": "פעלה", "en": "his act"}

   BAD (same word order — must split):
   {"ja": "האולא אלמשהורון באלמתכלמין", "en": "those well known as the mutakallimūn"}
   CORRECT:
   {"ja": "האולא", "en": "those"},
   {"ja": "אלמשהורון", "en": "well known"},
   {"ja": "באלמתכלמין", "en": "as the mutakallimūn"}

   The ONLY time you may bundle multiple JA words is when their English equivalents appear in reversed or scrambled order (a true word-order inversion that would violate rule 2 if split). Otherwise, always split.

4. PARTIAL COVERAGE IS FINE. Skip connecting particles (ו-, פ-, לא, אן as bare conjunction, etc.) that have no clean EN correspondent, and English glue words ("that there is", bare articles) that have no clean JA anchor. They render as un-highlighted plain text. It is better to skip a word than to stretch a pair.

5. NO `he` FIELD. JA↔EN only — omit Hebrew entirely.

6. EVERY SEGMENT GETS AN ARRAY. Empty array [] is acceptable for a segment you cannot confidently align.

EXAMPLE (one segment, index "0"):
Input JA: "אלפלאספה יסמון אללה אלעלה אלאולי"
Input EN: "The philosophers call God the first cause"
Good output:
{"alignments": {"0": [
  {"ja": "אלפלאספה", "en": "The philosophers"},
  {"ja": "יסמון אללה", "en": "call God"},
  {"ja": "אלעלה אלאולי", "en": "the first cause"}
]}}

BAD (too coarse — never do this):
{"alignments": {"0": [
  {"ja": "אלפלאספה יסמון אללה אלעלה אלאולי", "en": "The philosophers call God the first cause"}
]}}
"""


def build_user_message(segments: list[dict]) -> str:
    lines = [
        "Align each segment below. Return JSON with one key per segment index.",
        "",
        "SEGMENTS:",
        "",
    ]
    for idx, seg in enumerate(segments):
        lines.append(f"--- segment {idx} ---")
        lines.append(f"JA: {seg['ja']}")
        lines.append(f"EN: {seg['en']}")
        lines.append("")
    return "\n".join(lines)


def parse_alignments(text: str) -> dict[str, list[dict]]:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines)
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in reply:\n{text[:400]}")
    obj = json.loads(text[start : end + 1])
    if "alignments" not in obj:
        raise ValueError(f"reply missing 'alignments' key: {list(obj.keys())}")
    return obj["alignments"]


def validate_segment(
    ja: str,
    en: str,
    pairs: list[dict],
    label: str = "",
) -> tuple[list[dict], list[str]]:
    """Forward-cursor validation: drop pairs that fail substring search."""
    kept: list[dict] = []
    dropped: list[str] = []
    ja_cur = en_cur = 0
    for i, p in enumerate(pairs):
        if not isinstance(p, dict) or "ja" not in p or "en" not in p:
            dropped.append(f"pair {i}: malformed {p!r}")
            continue
        jp, ep = p["ja"], p["en"]
        ji = ja.find(jp, ja_cur)
        if ji == -1:
            dropped.append(f"{label} pair {i}: JA {jp!r} not found at/after cursor {ja_cur}")
            continue
        ei = en.find(ep, en_cur)
        if ei == -1:
            dropped.append(f"{label} pair {i}: EN {ep!r} not found at/after cursor {en_cur}")
            continue
        kept.append({"ja": jp, "en": ep})
        ja_cur = ji + len(jp)
        en_cur = ei + len(ep)
    return kept, dropped


def call_claude(user_msg: str) -> str:
    try:
        import anthropic  # type: ignore
    except ImportError:
        print("ERROR: 'anthropic' SDK not installed. Run: pip3 install anthropic", file=sys.stderr)
        sys.exit(2)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set.", file=sys.stderr)
        sys.exit(3)

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[{"type": "text", "text": SYSTEM_INSTRUCTIONS, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
    )
    return "".join(
        block.text for block in resp.content if getattr(block, "type", None) == "text"
    )


def align_file(src_path: Path, dry_run: bool = False) -> int:
    data = json.loads(src_path.read_text(encoding="utf-8"))

    # Collect all alignable segments across all pages
    # Each entry: (page_idx, seg_idx, segment_dict)
    alignable: list[tuple[int, int, dict]] = []
    for pi, page in enumerate(data.get("pages", [])):
        for si, seg in enumerate(page.get("aligned", [])):
            if seg.get("isHeader"):
                continue
            if not seg.get("ja") or not seg.get("en"):
                continue
            alignable.append((pi, si, seg))

    if not alignable:
        print(f"{src_path.name}: no alignable segments found", file=sys.stderr)
        return 0

    print(f"{src_path.name}: {len(alignable)} segment(s) to align", file=sys.stderr)

    if dry_run:
        total_chars = sum(len(s["ja"]) + len(s["en"]) for _, _, s in alignable)
        print(f"[dry-run] system chars: {len(SYSTEM_INSTRUCTIONS):>7,}")
        print(f"[dry-run] total segment chars: {total_chars:>7,}")
        print(f"[dry-run] segments: {len(alignable)}")
        for i, (pi, si, seg) in enumerate(alignable):
            print(f"  seg {i} (page {pi}, seg {si}): JA {len(seg['ja'])} chars, EN {len(seg['en'])} chars")
        return 0

    # Build the segment list for Claude (0-indexed)
    seg_list = [seg for _, _, seg in alignable]
    user_msg = build_user_message(seg_list)

    print(f"calling Claude for {src_path.name}...", file=sys.stderr)
    reply = call_claude(user_msg)

    try:
        raw = parse_alignments(reply)
    except Exception as e:
        debug = src_path.with_suffix(".align-debug.txt")
        debug.write_text(reply, encoding="utf-8")
        print(f"parse failed: {e}; raw → {debug}", file=sys.stderr)
        return 4

    total_kept = total_dropped = 0
    for i, (pi, si, seg) in enumerate(alignable):
        pairs = raw.get(str(i), [])
        label = f"seg {i} (page {pi}, aligned[{si}])"
        kept, dropped = validate_segment(seg["ja"], seg["en"], pairs, label)
        for reason in dropped:
            print(f"  DROPPED — {reason}", file=sys.stderr)
        total_kept += len(kept)
        total_dropped += len(dropped)
        # Write back into the source data
        data["pages"][pi]["aligned"][si]["pairs"] = kept

    src_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {total_kept} pairs ({total_dropped} dropped) → {src_path.relative_to(ROOT)}")
    return 0


def discover_files(pattern: str) -> list[Path]:
    return sorted(DATA_DIR.glob(pattern))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--file", help="Path to a single Advanced Reader JSON file")
    ap.add_argument("--all", action="store_true", help="Run on all moreh-bab*.json files")
    ap.add_argument("--pattern", default="moreh-bab*.json", help="Glob pattern for --all (default: moreh-bab*.json)")
    ap.add_argument("--dry-run", action="store_true", help="Print what would be sent without calling Claude")
    args = ap.parse_args()

    if not args.file and not args.all:
        ap.error("either --file PATH or --all is required")

    if args.file:
        return align_file(Path(args.file).resolve(), dry_run=args.dry_run)

    files = discover_files(args.pattern)
    if not files:
        print(f"no files matching {args.pattern} in {DATA_DIR}", file=sys.stderr)
        return 1
    for f in files:
        rc = align_file(f, dry_run=args.dry_run)
        if rc != 0:
            print(f"halting at {f.name} (rc={rc})", file=sys.stderr)
            return rc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

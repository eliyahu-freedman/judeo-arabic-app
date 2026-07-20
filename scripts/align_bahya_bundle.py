"""Align one full Bahya JA page against its candidate English translation.

Reads bundle files from data/_bahya_align_work/bab{N}/ produced by
build_bahya_align_bundles.py, calls Claude to:
  1. Split the JA page into semantic segments (sentence/clause level)
  2. Assign the corresponding English chunk to each segment
  3. Generate fine-grained JA↔EN phrase pairs within each segment

Output is written to data/_bahya_align_work/bab{N}_out/{page_he}.json in the
format expected by merge_bahya_alignment.py.

Usage:
    export ANTHROPIC_API_KEY=...
    python3 scripts/align_bahya_bundle.py 3          # align all pages of bab 3
    python3 scripts/align_bahya_bundle.py 3 --page קכז   # single page
    python3 scripts/align_bahya_bundle.py 3 --dry-run

Resume: pages that already have an output file are skipped automatically.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

MODEL = "claude-opus-4-8"
MAX_TOKENS = 8000

SYSTEM_INSTRUCTIONS = """You are aligning a page of Judeo-Arabic text (written in Hebrew script) with its English translation. Your output drives a bilingual reader: clicking a JA phrase highlights the English equivalent and vice versa.

You will receive:
  - page_he: the Hebrew-gematria page number (e.g. "קכז")
  - ja: the full JA text of the page as a single string
  - en_candidate: the approximate English translation passage for this page

Your task has three parts:
  1. SEGMENT the JA text into semantic units — sentences and clauses. Each segment must be an EXACT verbatim substring of the full JA text (copy character-for-character, no ellipsis, no edits).
  2. MATCH each JA segment to its English equivalent — a substring of en_candidate. For headers/titles use the matching English title. For prose segments, slice the English so that each segment's English is also an EXACT verbatim substring of en_candidate.
  3. PAIR each segment at the phrase level: produce {ja, en} pairs where ja is an exact substring of that segment's JA and en is an exact substring of that segment's EN.

OUTPUT FORMAT — strict JSON, no preamble, no markdown fences:
{
  "pages": {
    "<page_he>": [
      {
        "ja": "<verbatim JA segment>",
        "en": "<verbatim EN match>",
        "isHeader": true or false,
        "pairs": [
          {"ja": "<verbatim JA phrase>", "en": "<verbatim EN phrase>"},
          ...
        ]
      },
      ...
    ]
  }
}

HARD RULES — violation will break the reader:

1. VERBATIM SUBSTRINGS EVERYWHERE.
   - Each segment's `ja` must appear character-for-character in the input JA text.
   - Each segment's `en` must appear character-for-character in the input en_candidate.
   - Each pair's `ja` must appear character-for-character in that segment's `ja` field.
   - Each pair's `en` must appear character-for-character in that segment's `en` field.
   - No paraphrasing, no normalization, no corrections, no ellipsis.

2. COMPLETE JA COVERAGE. Every character of the full JA text must appear in exactly one segment's `ja` field. The concatenation of all segment `ja` fields (in order) must exactly reproduce the full JA text.

3. LEFT-TO-RIGHT CURSOR FOR PAIRS. Within a segment, the N-th pair's `ja` must start at or after the previous pair's `ja` ends (same for `en`). If Arabic word order differs from English, bundle the inverted phrase as one multi-word pair rather than two cross-ordered pairs.

4. HEADERS. Identify chapter/gate titles (e.g. "אלבאב. אלת'אלת'." or "פתיחה." or "פצל.") as isHeader: true. Headers have pairs: [].

5. GRANULARITY FOR PAIRS. Split as finely as possible:
   - Target: 1-3 JA words ↔ 1-4 EN words per pair.
   - If JA and EN share left-to-right word order for a stretch, split into individual word pairs.
   - Bundle only when word order is inverted (would violate rule 3 if split).
   - Skip connecting particles (ו-, פ-, bare אן, etc.) and English glue words that lack a clean correspondent — partial coverage is fine.

6. EMPTY PAIRS. If you cannot confidently align a segment, set pairs: [].

EXAMPLE:
Input JA (one segment): "קאל, אנה למא שרחנא פי מא תקדם"
Input EN match:          "He said: When, in what has come before, we have set out"
Good pairs:
  {"ja": "קאל", "en": "He said"},
  {"ja": "למא שרחנא", "en": "we have set out"},
  {"ja": "פי מא תקדם", "en": "in what has come before"}

BAD (too coarse):
  {"ja": "קאל, אנה למא שרחנא פי מא תקדם", "en": "He said: When, in what has come before, we have set out"}
"""


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


def parse_response(text: str) -> dict:
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
    return json.loads(text[start : end + 1])


def validate_output(
    bundle: dict,
    output: dict,
) -> tuple[dict, list[str]]:
    """Validate output against bundle. Returns (cleaned_output, errors)."""
    errors: list[str] = []
    page_he = bundle["page_he"]
    full_ja = bundle["ja"]
    en_cand = bundle["en_candidate"]

    pages = output.get("pages", {})
    if page_he not in pages:
        errors.append(f"Missing page key '{page_he}' in output")
        return output, errors

    segments = pages[page_he]
    if not isinstance(segments, list) or not segments:
        errors.append(f"page '{page_he}' has no segments")
        return output, errors

    # Check JA coverage: concatenated segment JA should equal full_ja
    joined_ja = "".join(s.get("ja", "") for s in segments)
    if joined_ja != full_ja:
        # Compute mismatch info
        errors.append(
            f"JA coverage mismatch: joined_len={len(joined_ja)} vs full_len={len(full_ja)}"
        )

    # Validate pairs (forward cursor) and clean up
    for si, seg in enumerate(segments):
        seg_ja = seg.get("ja", "")
        seg_en = seg.get("en", "")
        if seg.get("isHeader"):
            seg["pairs"] = []
            continue
        # Check segment.en is substring of en_candidate (allow loose — don't fail hard)
        if seg_en and en_cand and seg_en not in en_cand:
            errors.append(f"seg {si}: EN not substring of en_candidate: {seg_en[:60]!r}")

        raw_pairs = seg.get("pairs", [])
        kept: list[dict] = []
        ja_cur = en_cur = 0
        for pi, pair in enumerate(raw_pairs):
            if not isinstance(pair, dict) or "ja" not in pair or "en" not in pair:
                errors.append(f"seg {si} pair {pi}: malformed")
                continue
            pj, pe = pair["ja"], pair["en"]
            ji = seg_ja.find(pj, ja_cur)
            if ji == -1:
                errors.append(f"seg {si} pair {pi}: JA {pj!r} not found at cursor {ja_cur}")
                continue
            ei = seg_en.find(pe, en_cur)
            if ei == -1:
                errors.append(f"seg {si} pair {pi}: EN {pe!r} not found at cursor {en_cur}")
                continue
            kept.append({"ja": pj, "en": pe})
            ja_cur = ji + len(pj)
            en_cur = ei + len(pe)
        seg["pairs"] = kept

    return output, errors


def align_page(bundle: dict, out_path: Path, dry_run: bool = False) -> bool:
    """Align one page bundle and write output. Returns True on success."""
    page_he = bundle["page_he"]
    user_msg = (
        f"page_he: {page_he}\n\n"
        f"JA TEXT:\n{bundle['ja']}\n\n"
        f"EN CANDIDATE:\n{bundle['en_candidate']}"
    )

    if dry_run:
        print(f"[dry-run] {page_he}: JA={len(bundle['ja'])} chars, EN={len(bundle['en_candidate'])} chars")
        return True

    print(f"  aligning page {page_he}...", end=" ", flush=True)
    t0 = time.time()
    try:
        raw = call_claude(user_msg)
    except Exception as e:
        print(f"ERROR calling Claude: {e}", file=sys.stderr)
        return False

    try:
        output = parse_response(raw)
    except Exception as e:
        debug_path = out_path.with_suffix(".debug.txt")
        debug_path.write_text(raw, encoding="utf-8")
        print(f"PARSE ERROR: {e}  (debug → {debug_path.name})")
        return False

    output, errors = validate_output(bundle, output)
    elapsed = time.time() - t0

    if errors:
        for err in errors:
            print(f"\n    WARN {page_he}: {err}", file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    seg_count = len(output.get("pages", {}).get(page_he, []))
    pair_count = sum(len(s.get("pairs", [])) for s in output.get("pages", {}).get(page_he, []))
    warn_tag = f" [{len(errors)} warns]" if errors else ""
    print(f"ok — {seg_count} segs / {pair_count} pairs in {elapsed:.1f}s{warn_tag}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("bab", type=int, help="Bab number (3–10)")
    ap.add_argument("--page", help="Align a single page (Hebrew gematria label, e.g. קכז)")
    ap.add_argument("--dry-run", action="store_true", help="Print what would be sent without calling Claude")
    ap.add_argument("--retry-errors", action="store_true", help="Re-run pages that have a .debug.txt file")
    args = ap.parse_args()

    work_dir = DATA_DIR / "_bahya_align_work" / f"bab{args.bab}"
    out_dir = DATA_DIR / "_bahya_align_work" / f"bab{args.bab}_out"

    if not work_dir.exists():
        print(f"ERROR: work dir not found: {work_dir}", file=sys.stderr)
        print("Run: python3 scripts/build_bahya_align_bundles.py {args.bab}", file=sys.stderr)
        return 1

    bundle_files = sorted(work_dir.glob("*.json"))
    if not bundle_files:
        print(f"ERROR: no bundle files in {work_dir}", file=sys.stderr)
        return 1

    if args.page:
        bundle_files = [f for f in bundle_files if f.stem == args.page]
        if not bundle_files:
            print(f"ERROR: page {args.page!r} not found in {work_dir}", file=sys.stderr)
            return 1

    out_dir.mkdir(parents=True, exist_ok=True)

    total = len(bundle_files)
    done = skipped = failed = 0

    print(f"Bab {args.bab}: {total} pages to process → {out_dir}")

    for bundle_path in bundle_files:
        out_path = out_dir / bundle_path.name
        debug_path = out_path.with_suffix(".debug.txt")

        if out_path.exists() and not args.retry_errors:
            skipped += 1
            continue
        if args.retry_errors and not debug_path.exists():
            if out_path.exists():
                skipped += 1
                continue

        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
        ok = align_page(bundle, out_path, dry_run=args.dry_run)
        if ok:
            done += 1
            if debug_path.exists():
                debug_path.unlink()
        else:
            failed += 1

    print(f"\nDone: {done} aligned, {skipped} skipped, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

"""Generate JA↔English phrase-pair alignment for a Tafsir chapter via Claude.

Produces data/tafsir-{book}-{chapter}-alignment.json — used by the Tafsir
reader (app/tafsir/reader.tsx) to highlight corresponding JA when the user
hovers an English word, and vice versa.

Constraints baked into the prompt:

  - Each group is a {ja, en} pair whose `ja` is a literal substring of that
    verse's JA and whose `en` is a literal substring of the English rendering.
  - Groups for a verse must be in matching left-to-right order on BOTH sides
    (so the runtime resolver — which uses a sequential cursor per side —
    finds them deterministically). Where JA and English diverge in word
    order (e.g. JA verb-subject "כ'לק אללה" vs. EN subject-verb "God created"),
    bundle the divergent span as a single multi-word group rather than two
    separately-ordered groups.
  - Coverage need not be exhaustive. Connectors and Saadia paraphrase glue
    (an English "was" with no JA counterpart, a JA פ with no EN counterpart)
    should simply be omitted — they'll render as un-highlighted text.

Usage:
    export ANTHROPIC_API_KEY=...
    pip install anthropic
    python3 scripts/align_tafsir_english.py --book bereshit --chapter 1
    python3 scripts/align_tafsir_english.py --book bereshit --all
    python3 scripts/align_tafsir_english.py --book bereshit --chapter 2 --dry-run

The script validates Claude's reply: every {ja, en} pair must resolve to a
substring on both sides with a running cursor. Bad rows are logged and
dropped rather than aborting the whole chapter.
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

SYSTEM_INSTRUCTIONS = """You are aligning Saadia Gaon's Judeo-Arabic Tafsir to its English rendering at the phrase level. The output drives a reader UI: hovering an English chunk highlights the JA chunk it translates, and vice versa.

OUTPUT FORMAT — STRICT JSON, no preamble, no markdown:
{"alignments": {"1": [{"ja": "...", "en": "..."}, ...], "2": [...], ...}}

For each verse, return an ordered list of phrase pairs. Hard rules:

1. SUBSTRING. Each pair's `ja` value must appear character-for-character in that verse's JA, and `en` must appear character-for-character in the English. No paraphrasing, no normalization, no stripping punctuation. Copy substrings verbatim.

2. LEFT-TO-RIGHT ORDER ON BOTH SIDES. The resolver walks each side with a running cursor — for the N-th pair it looks for `ja` at or after the previous JA cursor, and `en` at or after the previous EN cursor. Pairs must therefore appear in increasing position on both sides. Where JA and English have different word orders inside a unit (e.g. JA "כ'לק אללה" verb-subject vs. EN "God created" subject-verb), bundle that unit as ONE multi-word group ({"ja": "כ'לק אללה", "en": "God created"}) — do NOT split it into two cross-ordered groups.

3. SAADIA PARAPHRASE BUNDLES. Saadia's signature multi-word JA paraphrases that render as multi-word English are single groups:
   - {"ja": "שא אללה אן יכון", "en": "God willed that there be"}
   - {"ja": "וַלַמּא מצ'י' מן אלליל ואלנהאר", "en": "And there passed of night and daytime"}
   - {"ja": "פלִמא עלם אללה", "en": "And when God knew"} or just {"ja": "פלִמא", "en": "And when"} + {"ja": "עלם אללה", "en": "God knew"}
   When in doubt, prefer larger bundles over riskier word-by-word splits.

4. PARTIAL COVERAGE IS FINE. Don't force pairs for connectors that have no counterpart. English "was" with no JA, JA "פ" prefix with no EN word — just omit them. The unmatched runs will render as plain text.

5. PUNCTUATION. Include punctuation INSIDE a phrase if it's tightly bound (e.g. {"en": "“day,”"} for the JA נהארא). Leave free-standing punctuation outside groups.

6. EVERY VERSE GETS AN ARRAY. Empty array `[]` is acceptable for a verse where you can't confidently align anything.

EXAMPLE OUTPUT (Bereshit 1:1-3):
{"alignments": {
  "1": [
    {"ja": "אול מא", "en": "The first thing"},
    {"ja": "כ'לק אללה", "en": "God created"},
    {"ja": "אלסמאואת", "en": "the heavens"},
    {"ja": "ואלארץ'", "en": "and the earth"}
  ],
  "2": [
    {"ja": "ואלארץ'", "en": "And the earth"},
    {"ja": "כאנת", "en": "was"},
    {"ja": "ג'אמרה", "en": "submerged"}
  ],
  "3": [
    {"ja": "שא אללה אן יכון", "en": "God willed that there be"},
    {"ja": "נור", "en": "light"},
    {"ja": "פכאן", "en": "and there was"},
    {"ja": "נור", "en": "light"}
  ]
}}
"""


def build_user_message(book: str, chapter: int) -> str:
    src = json.loads(
        (DATA_DIR / f"tafsir-{book.lower()}-{chapter}.json").read_text(
            encoding="utf-8",
        ),
    )
    en = json.loads(
        (DATA_DIR / f"tafsir-{book.lower()}-{chapter}-english.json").read_text(
            encoding="utf-8",
        ),
    )["translations"]

    lines = [
        f"Align every verse of {src['book']} chapter {src['chapter']}.",
        "Return JSON {\"alignments\": {\"<v>\": [...], ...}} with one entry per verse.",
        "",
        "VERSES:",
        "",
    ]
    for v in src["verses"]:
        vnum = str(v["v"])
        lines.append(f"v.{vnum}")
        lines.append(f"  JA: {v['ja']}")
        lines.append(f"  EN: {en.get(vnum, '')}")
        lines.append("")
    return "\n".join(lines)


def parse_alignments(text: str) -> dict[str, list[dict]]:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines)
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in reply:\n{text[:300]}")
    obj = json.loads(text[start : end + 1])
    if "alignments" not in obj:
        raise ValueError(f"reply missing 'alignments' key: {list(obj.keys())}")
    return obj["alignments"]


def validate_verse(
    ja: str,
    en: str,
    pairs: list[dict],
) -> tuple[list[dict], list[str]]:
    """Drop pairs that don't resolve. Return (kept, dropped-reasons)."""
    kept: list[dict] = []
    dropped: list[str] = []
    ja_cur = en_cur = 0
    for i, p in enumerate(pairs):
        if not isinstance(p, dict) or "ja" not in p or "en" not in p:
            dropped.append(f"pair {i}: malformed {p!r}")
            continue
        ja_phrase = p["ja"]
        en_phrase = p["en"]
        ji = ja.find(ja_phrase, ja_cur)
        if ji == -1:
            dropped.append(
                f"pair {i}: JA {ja_phrase!r} not found at/after cursor {ja_cur}",
            )
            continue
        ei = en.find(en_phrase, en_cur)
        if ei == -1:
            dropped.append(
                f"pair {i}: EN {en_phrase!r} not found at/after cursor {en_cur}",
            )
            continue
        kept.append({"ja": ja_phrase, "en": en_phrase})
        ja_cur = ji + len(ja_phrase)
        en_cur = ei + len(en_phrase)
    return kept, dropped


def call_claude(system_text: str, user_msg: str) -> str:
    try:
        import anthropic  # type: ignore
    except ImportError:
        print(
            "ERROR: 'anthropic' SDK not installed. Run:\n  pip3 install anthropic",
            file=sys.stderr,
        )
        sys.exit(2)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "ERROR: ANTHROPIC_API_KEY not set.",
            file=sys.stderr,
        )
        sys.exit(3)

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[
            {
                "type": "text",
                "text": system_text,
                "cache_control": {"type": "ephemeral"},
            },
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    parts = []
    for block in resp.content:
        if getattr(block, "type", None) == "text":
            parts.append(block.text)
    return "".join(parts)


def write_sidecar(
    book: str,
    chapter: int,
    alignments: dict[str, list[dict]],
) -> Path:
    out_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}-alignment.json"
    payload = {
        "_note": (
            f"JA↔EN phrase-pair alignment for {book.title()} {chapter}, "
            "generated by scripts/align_tafsir_english.py. Used by the Tafsir "
            "reader for hover-coordinated highlighting. Each pair's `ja` and `en` "
            "are verbatim substrings of the verse's JA / english strings; the "
            "runtime walks each side with a sequential cursor."
        ),
        "_status": "draft",
        "_model": MODEL,
        "alignments": alignments,
    }
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return out_path


def align_chapter(book: str, chapter: int) -> int:
    src_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}.json"
    en_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}-english.json"
    if not src_path.exists():
        print(f"missing source: {src_path}", file=sys.stderr)
        return 1
    if not en_path.exists():
        print(f"missing english: {en_path}", file=sys.stderr)
        return 1

    user_msg = build_user_message(book, chapter)
    print(f"calling Claude for {book} {chapter} alignment...", file=sys.stderr)
    reply = call_claude(SYSTEM_INSTRUCTIONS, user_msg)

    try:
        raw_alignments = parse_alignments(reply)
    except Exception as e:
        debug = DATA_DIR / f"tafsir-{book.lower()}-{chapter}-alignment.raw.txt"
        debug.write_text(reply, encoding="utf-8")
        print(f"parse failed: {e}; raw → {debug}", file=sys.stderr)
        return 4

    src = json.loads(src_path.read_text(encoding="utf-8"))
    en_data = json.loads(en_path.read_text(encoding="utf-8"))["translations"]

    cleaned: dict[str, list[dict]] = {}
    total_kept = total_dropped = 0
    for v in src["verses"]:
        vnum = str(v["v"])
        pairs = raw_alignments.get(vnum, [])
        kept, dropped = validate_verse(v["ja"], en_data.get(vnum, ""), pairs)
        cleaned[vnum] = kept
        total_kept += len(kept)
        total_dropped += len(dropped)
        for reason in dropped:
            print(f"  v{vnum} DROPPED — {reason}", file=sys.stderr)

    out = write_sidecar(book, chapter, cleaned)
    print(
        f"wrote {total_kept} pairs ({total_dropped} dropped) → "
        f"{out.relative_to(ROOT)}",
    )
    return 0


def discover_chapters(book: str) -> list[int]:
    prefix = f"tafsir-{book.lower()}-"
    chs = []
    for p in DATA_DIR.iterdir():
        name = p.name
        if not name.startswith(prefix) or not name.endswith(".json"):
            continue
        stem = name[len(prefix) : -len(".json")]
        if not stem.isdigit():
            continue
        chs.append(int(stem))
    return sorted(chs)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--book", required=True)
    ap.add_argument("--chapter", type=int)
    ap.add_argument(
        "--all",
        action="store_true",
        help="Align every chapter in --book that has an English sidecar and no alignment yet.",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="With --all, regenerate even chapters that already have alignment data.",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.all and args.chapter is None:
        ap.error("either --chapter N or --all is required")

    if args.dry_run:
        ch = args.chapter or (discover_chapters(args.book)[:1] or [1])[0]
        user_msg = build_user_message(args.book, ch)
        sys_chars = len(SYSTEM_INSTRUCTIONS)
        print(f"[dry-run] system chars: {sys_chars:>7,}")
        print(f"[dry-run] user chars:   {len(user_msg):>7,}")
        print(f"[dry-run] model:        {MODEL}")
        print()
        print("--- USER MESSAGE PREVIEW (first 1200 chars) ---")
        print(user_msg[:1200])
        return 0

    if args.all:
        chapters = discover_chapters(args.book)
        if not chapters:
            print(f"no source chapters for book={args.book}", file=sys.stderr)
            return 1
        skipped = 0
        for ch in chapters:
            en = DATA_DIR / f"tafsir-{args.book.lower()}-{ch}-english.json"
            if not en.exists():
                skipped += 1
                continue
            out = DATA_DIR / f"tafsir-{args.book.lower()}-{ch}-alignment.json"
            if out.exists() and not args.force:
                skipped += 1
                continue
            rc = align_chapter(args.book, ch)
            if rc != 0:
                print(f"halting --all at {args.book} {ch} (rc={rc})", file=sys.stderr)
                return rc
        print(f"done. skipped {skipped} (no english or already aligned)")
        return 0

    return align_chapter(args.book, args.chapter)


if __name__ == "__main__":
    raise SystemExit(main())

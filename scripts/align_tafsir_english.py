"""Generate Hebrew↔JA↔English phrase-triple alignment for a Tafsir chapter via Claude.

Produces data/tafsir-{book}-{chapter}-alignment.json — used by the Tafsir
reader (app/tafsir/reader.tsx) to highlight the matching Hebrew, JA, and
English chunks together when the user hovers any one of them.

Constraints baked into the prompt:

  - Each group is a {he?, ja, en} triple whose values are literal substrings
    of the verse's Hebrew, JA, and English strings. `he` is optional and
    should be omitted (per triple) where Saadia paraphrased without a clean
    Hebrew anchor.
  - Groups for a verse must be in matching left-to-right order on every
    side (the runtime resolver uses a sequential cursor per side). Where
    word order diverges within a unit, bundle that unit as a single
    multi-word group rather than two cross-ordered groups.
  - Coverage need not be exhaustive. Connectors and paraphrase glue should
    simply be omitted — they'll render as un-highlighted text.

Usage:
    export ANTHROPIC_API_KEY=...
    pip install anthropic
    python3 scripts/align_tafsir_english.py --book bereshit --chapter 1
    python3 scripts/align_tafsir_english.py --book bereshit --all
    python3 scripts/align_tafsir_english.py --book bereshit --chapter 2 --dry-run

The script validates Claude's reply: ja/en must resolve on both sides with
a running cursor (else the whole triple is dropped); he must resolve when
present (else the triple is kept without `he` and the drop is logged). Bad
rows are logged rather than aborting the whole chapter.
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

SYSTEM_INSTRUCTIONS = """You are aligning the biblical Hebrew, Saadia Gaon's Judeo-Arabic Tafsir, and the English rendering at the phrase level. The output drives a reader UI: hovering any chunk on any of the three sides highlights the matching chunks on the other two sides.

OUTPUT FORMAT — STRICT JSON, no preamble, no markdown:
{"alignments": {"1": [{"he": "...", "ja": "...", "en": "..."}, ...], "2": [...], ...}}

For each verse, return an ordered list of phrase triples. Hard rules:

1. SUBSTRING. Each triple's `he` value must appear character-for-character in that verse's Hebrew, `ja` must appear character-for-character in the JA, and `en` must appear character-for-character in the English. No paraphrasing, no normalization, no stripping punctuation or vowel points. Copy substrings verbatim — niqqud and all.

2. LEFT-TO-RIGHT ORDER ON ALL THREE SIDES. The resolver walks each side with a running cursor — for the N-th triple it looks for `he`/`ja`/`en` at or after that side's previous cursor. Triples must therefore appear in increasing position on every side. Where word order differs inside a unit (e.g. Hebrew VS "בָּרָא אֱלֹהִים" vs. English SV "God created"), bundle that unit as ONE multi-word group rather than splitting into two cross-ordered groups.

3. SAADIA PARAPHRASE BUNDLES. Saadia's signature multi-word JA paraphrases that render as multi-word English (and that fuse what was tighter in the Hebrew) are single groups:
   - {"he": "יְהִי", "ja": "שא אללה אן יכון", "en": "God willed that there be"}
   - {"he": "וַיְהִי-עֶרֶב וַיְהִי-בֹקֶר", "ja": "וַלַמּא מצ'י' מן אלליל ואלנהאר", "en": "And there passed of night and daytime"}
   - {"he": "וַיַּרְא אֱלֹהִים", "ja": "עלם אללה", "en": "God knew"} (Saadia's "knew" for "saw")
   When in doubt, prefer larger bundles over riskier word-by-word splits.

4. `he` IS OPTIONAL ON A PER-TRIPLE BASIS. If a JA↔EN pair has no clean Hebrew anchor (Saadia added a connective, paraphrased without a Hebrew counterpart, etc.), OMIT the `he` field on that triple rather than inventing one. Triples without `he` still help JA↔EN highlighting; the Hebrew side just won't light up for that chunk.

5. PARTIAL COVERAGE IS FINE. Don't force triples for connectors that have no counterpart anywhere. English "was" with no JA, JA "פ" prefix with no Hebrew or EN word — just omit them. The unmatched runs will render as plain text.

6. PUNCTUATION & POINTING. Include punctuation INSIDE a phrase if it's tightly bound (e.g. {"en": "“day,”"} for the JA נהארא, {"he": "אֵת הַשָּׁמַיִם"} for "the heavens"). Copy Hebrew niqqud exactly as it appears in the source.

7. EVERY VERSE GETS AN ARRAY. Empty array `[]` is acceptable for a verse where you can't confidently align anything.

EXAMPLE OUTPUT (Bereshit 1:1-3):
{"alignments": {
  "1": [
    {"he": "בְּרֵאשִׁית", "ja": "אול מא", "en": "The first thing"},
    {"he": "בָּרָא אֱלֹהִים", "ja": "כ'לק אללה", "en": "God created"},
    {"he": "אֵת הַשָּׁמַיִם", "ja": "אלסמאואת", "en": "the heavens"},
    {"he": "וְאֵת הָאָרֶץ", "ja": "ואלארץ'", "en": "and the earth"}
  ],
  "2": [
    {"he": "וְהָאָרֶץ", "ja": "ואלארץ'", "en": "And the earth"},
    {"he": "הָיְתָה", "ja": "כאנת", "en": "was"},
    {"he": "תֹהוּ", "ja": "ג'אמרה", "en": "submerged"}
  ],
  "3": [
    {"he": "יְהִי אוֹר", "ja": "שא אללה אן יכון נור", "en": "God willed that there be light"},
    {"he": "וַיְהִי-אוֹר", "ja": "פכאן נור", "en": "there was light"}
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
        lines.append(f"  HE: {v['hebrew']}")
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
    he: str,
    ja: str,
    en: str,
    pairs: list[dict],
) -> tuple[list[dict], list[str]]:
    """Drop pairs that don't resolve. Return (kept, dropped-reasons).

    JA/EN are required on every pair (a pair missing either side is dropped).
    HE is optional: if present but unresolvable, we keep the pair without
    `he` (so the JA↔EN highlight still works) and log the drop.
    """
    kept: list[dict] = []
    dropped: list[str] = []
    he_cur = ja_cur = en_cur = 0
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
        kept_pair: dict = {"ja": ja_phrase, "en": en_phrase}
        he_phrase = p.get("he")
        if isinstance(he_phrase, str) and he_phrase:
            hi = he.find(he_phrase, he_cur)
            if hi == -1:
                dropped.append(
                    f"pair {i}: HE {he_phrase!r} not found at/after cursor {he_cur} "
                    "(JA/EN kept without Hebrew anchor)",
                )
            else:
                kept_pair["he"] = he_phrase
                he_cur = hi + len(he_phrase)
        kept.append(kept_pair)
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
            f"Hebrew↔JA↔EN phrase-triple alignment for {book.title()} {chapter}, "
            "generated by scripts/align_tafsir_english.py. Used by the Tafsir "
            "reader for hover-coordinated highlighting. Each triple's `he`, `ja`, "
            "`en` are verbatim substrings of the verse's Hebrew / JA / English; "
            "the `he` field is optional (omitted where Saadia paraphrased without "
            "a clean Hebrew anchor). The runtime walks each side with a "
            "sequential cursor."
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
        kept, dropped = validate_verse(
            v["hebrew"], v["ja"], en_data.get(vnum, ""), pairs,
        )
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

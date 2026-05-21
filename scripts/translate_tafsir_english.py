"""Translate one chapter of Saadia's JA Tafsir to English via the Claude API.

Goal: produce an English rendering that mirrors the Judeo-Arabic closely enough
for reverse translation — a reader looks at the JA in the Tafsir reader and
uses the English to make sense of the Arabic. This means:

  - Translate the JA, NOT the biblical Hebrew. Saadia's interpretive moves
    (e.g. שא ... אן יכון for ויאמר ... יהי, עלם for וירא, צורה for צלם,
    מסלטא inserted at 'in our image') are part of the source.
  - Where Saadia's JA sense differs from Lane's classical Arabic, follow Blau
    (Dictionary of Medieval Judaeo-Arabic Texts). Gloss table records these.

Inputs (cached on the API side, reused across all chapters):
  - data-source/saadia-gloss-table.json — JA→EN mappings, principles
  - data-source/blau-genesis-notes.json — Blau's verse-by-verse notes for
    Bereshit 1-12 (kapach corrections, ms variants, translation patterns)
  - data/tafsir-bereshit-1-english.json — Bereshit 1 as a worked exemplar
  - data/tafsir-bereshit-1.json — the JA source for that exemplar

Per-chapter input:
  - data/tafsir-{book}-{ch}.json — the JA chapter to translate

Output:
  - data/tafsir-{book}-{ch}-english.json — {translations: {v: english}}
    with _status: "draft" and _model marker

Usage:
    export ANTHROPIC_API_KEY=...
    pip install anthropic
    python3 scripts/translate_tafsir_english.py --book bereshit --chapter 2
    python3 scripts/translate_tafsir_english.py --book bereshit --chapter 2 --dry-run

The --dry-run flag prints the request payload without calling the API. Useful
when calibrating the prompt before paying for tokens.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SOURCE_DIR = ROOT / "data-source"

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 8000

# Sonnet 4.6 pricing (USD per million tokens), as of 2026-02:
PRICE_INPUT_PER_MTOK = 3.00
PRICE_OUTPUT_PER_MTOK = 15.00
PRICE_CACHE_WRITE_PER_MTOK = 3.75   # 1.25× input
PRICE_CACHE_READ_PER_MTOK = 0.30    # 0.10× input

# Persistent cost-meter file. Survives across runs so a multi-book
# pipeline cannot blow past the user's budget by restarting.
COST_METER_PATH = Path.home() / ".cache" / "judeo-arabic-app" / "translation-cost.json"

DEFAULT_COST_CAP_USD = 10.00

SYSTEM_INSTRUCTIONS = """You are translating Saadia Gaon's 10th-century Judeo-Arabic Tafsir (תפסיר) of the Torah into English.

PRIMARY GOAL: the English must mirror the JA closely enough that a reader looking at the JA can use the English to disambiguate the Arabic — reverse-translation. The Tafsir reader on judeo-arabic-app shows the JA above the English; the English's job is to gloss what Saadia wrote, not to reproduce the biblical Hebrew.

CORE PRINCIPLES:

1. **Translate the Judeo-Arabic, not the biblical Hebrew.** Where Saadia interprets or rationalizes, his interpretation IS the source text. Examples of Saadia's signature substitutions you MUST preserve:
   - שא ... אן יכון (for Hebrew ויאמר ... יהי) → "willed that there be ..." — NOT "said, let there be"
   - עלם (for וירא) → "knew" — NOT "saw"
   - צורה (for צלם) → "form" — NOT "image"
   - ריאח אללה (for רוח אלהים) → "the winds of God" (plural) — NOT "spirit of God"
   - פכאן (for ויהי) → "and so it was" / "and there was"
   - מסלטא (Saadia's added word in Gen 1:26-27) → "sovereign" / "having dominion"
   - נפסא נאטקה (for נפש חיה when Adam is ensouled, Gen 2:7) → "a rational soul" or "a speaking soul"
   - וַלַמּא מצ'י' מן אלליל ואלנהאר יום N (for ויהי ערב ויהי בקר יום N) → "And there passed of night and daytime an Nth day"
   - תסתחק אן תמות (for מות תמות) → "you shall deserve to die"
   - חאכמא (added by Saadia at לאמר when speech is a decree) → "decreeing"
   - אוקאת אלנור (Saadia's gloss for "[God called] the light [day]") → "the times of light"

2. **Where Saadia's JA usage differs from Lane's classical Arabic sense, follow Blau.** Examples (the gloss table below lists more):
   - אלגלד = "the firmament / expanse" — NOT Lane's "hard, frozen"
   - דנא ב = "approach" (Aramaic-influenced) — NOT classical "be near"
   - אלי אלדהר = "forever" — NOT "for a generation"

3. **Reverse-translatability.** A careful reader should be able to map most English words back to a JA word in the same verse. Don't smooth toward the biblical Hebrew, don't paraphrase what Saadia phrased tightly, don't add words Saadia didn't write.

4. **Place-name identifications.** Saadia identifies biblical place-names with then-current geography:
   - פישון → "the Nile" (אלניל) — Saadia's identification
   - חוילה → "Zawila" (זוילה) — Maghreb gold center
   - כוש → "Abyssinia" (אלחבשה)
   - חידקל → "the Tigris" (אלדגלה)
   - אשור → "Mosul" (אלמוצל)
   On first occurrence in a chapter, give as "the Nile (Pishon)", "Zawila (Havilah)", etc., so readers can locate the verse. On subsequent occurrences in the same chapter, just "the Nile" / "Zawila".

5. **'אדם' as a proper noun.** From Gen 2:7 onward Saadia uses 'אדם' as a name — translate as "Adam", not "the man" or "the human".

6. **Saadia's 'סאיר' for repeated 'כל'.** When Saadia uses 'סאיר' for the second 'כל' in a verse (a Saadia pattern Blau documents), render as "and the rest of" or "and every other" — preserves the avoidance of literal duplication.

7. **Voice & register.** Light, slightly archaic English; "And God ..." / "And there was ...". Match the voice of the Bereshit 1 exemplar provided below.

OUTPUT FORMAT — STRICT:
Return ONLY a single JSON object with this exact shape, no preamble, no markdown:
{"translations": {"1": "English of v.1", "2": "English of v.2", ...}}

The keys are stringified verse numbers in the chapter. Include EVERY verse provided in the input. Each value is a single line of English (no newlines).
"""


def load_gloss_table() -> dict:
    p = SOURCE_DIR / "saadia-gloss-table.json"
    return json.loads(p.read_text(encoding="utf-8"))


def load_blau_notes() -> dict:
    p = SOURCE_DIR / "blau-genesis-notes.json"
    return json.loads(p.read_text(encoding="utf-8"))


def load_shemot_notes() -> dict:
    p = SOURCE_DIR / "saadia-shemot-notes.json"
    return json.loads(p.read_text(encoding="utf-8"))


def load_exemplar(book: str, chapter: int) -> tuple[dict, dict]:
    src = json.loads((DATA_DIR / f"tafsir-{book}-{chapter}.json").read_text(encoding="utf-8"))
    en = json.loads((DATA_DIR / f"tafsir-{book}-{chapter}-english.json").read_text(encoding="utf-8"))
    return src, en


# Exemplars selected after auditing all 50 Bereshit sidecars + hand-translating Shemot 1:
#   B1     — creation register, anti-anthropomorphic moves, "and there passed of night and daytime"
#   B22    — Akedah dialogue, labbayk, ghulam, place-of-worship, qurbān
#   Shemot 1 — Egypt-genre exemplar: oppression vocab, place-id (Faiyum=Pithom, Ein Shams=Raamses),
#              קום/אהל, ולאה' ד'מה, אעמאל אלצחרא, אלקואבל, אלמת'בר, חגבהן
EXEMPLAR_CHAPTERS = [("bereshit", 1), ("bereshit", 22), ("shemot", 1)]


def format_exemplar(label: str, src: dict, en_map: dict) -> str:
    text = f"{label} (worked example — match this voice):\n\n"
    for v in src["verses"]:
        en = en_map.get(str(v["v"]), "")
        text += f"v.{v['v']}\n  JA: {v['ja']}\n  AR: {v['arabic']}\n  HE: {v['hebrew']}\n  EN: {en}\n\n"
    return text


def build_system_blocks(book: str | None = None) -> list[dict]:
    """Cached system context: instructions + gloss table + Blau Genesis notes + Shemot notes + exemplars.

    Returned as a list of content blocks with cache_control on the heavy ones so
    Claude reuses them across all chapter calls in a session.

    The optional `book` parameter is a hint — Shemot notes are always included since
    they're broadly useful for Exodus-Numbers-Deuteronomy translation regardless.
    """
    gloss = load_gloss_table()
    blau = load_blau_notes()
    shemot = load_shemot_notes()

    exemplar_text = ""
    for ex_book, ch in EXEMPLAR_CHAPTERS:
        src, en = load_exemplar(ex_book, ch)
        label = f"{ex_book.upper()} {ch} EXEMPLAR"
        exemplar_text += format_exemplar(label, src, en["translations"])
        exemplar_text += "\n" + ("=" * 60) + "\n\n"

    return [
        {"type": "text", "text": SYSTEM_INSTRUCTIONS},
        {
            "type": "text",
            "text": "GLOSS TABLE (Saadia-specific JA→EN patterns, principles, Blau-vs-Lane flags):\n\n"
            + json.dumps(gloss, ensure_ascii=False, indent=2),
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": "BLAU NOTES (verse-by-verse, Genesis 1-12; consult before translating any verse in that range):\n\n"
            + json.dumps(blau, ensure_ascii=False, indent=2),
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": "SHEMOT-SPECIFIC NOTES (curated Saadia patterns for Exodus thematic blocks — burning bush, plagues, Decalogue, tabernacle, mishpatim. Largely applicable to Vayikra/Bamidbar/Devarim too):\n\n"
            + json.dumps(shemot, ensure_ascii=False, indent=2),
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": exemplar_text,
            "cache_control": {"type": "ephemeral"},
        },
    ]


def build_user_message(book: str, chapter: int) -> str:
    src_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}.json"
    chapter_data = json.loads(src_path.read_text(encoding="utf-8"))

    lines = [
        f"Translate every verse of {chapter_data['book']} chapter {chapter_data['chapter']}.",
        f"Output JSON: {{\"translations\": {{ ... }}}} with one entry per verse.",
        "",
        "VERSES:",
        "",
    ]
    for v in chapter_data["verses"]:
        lines.append(f"v.{v['v']}")
        lines.append(f"  JA: {v['ja']}")
        lines.append(f"  AR: {v['arabic']}")
        lines.append(f"  HE (biblical, for orientation only — translate the JA): {v['hebrew']}")
        if v.get("hebrew_translation"):
            lines.append(f"  HE-translation (Cairo edition's Hebrew rendering of Saadia, may contain commentary in brackets — ignore commentary): {v['hebrew_translation']}")
        lines.append("")
    return "\n".join(lines)


def parse_translations(text: str) -> dict[str, str]:
    """Extract the {translations: {...}} object from the model's reply.

    The system prompt tells the model to return raw JSON, but be permissive in
    case it wraps in a code fence or adds a preamble.
    """
    text = text.strip()
    # Strip markdown fences if present.
    if text.startswith("```"):
        # Drop first line (```json or ```) and last fence.
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines)
    # Find the outermost { ... } if there's any preamble.
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in reply:\n{text[:300]}")
    obj = json.loads(text[start : end + 1])
    if "translations" not in obj:
        raise ValueError(f"reply missing 'translations' key: {list(obj.keys())}")
    return obj["translations"]


def load_cost_meter() -> dict:
    """Read persistent cost-meter. Returns {'cumulative_usd': float, 'calls': int}."""
    if not COST_METER_PATH.exists():
        return {"cumulative_usd": 0.0, "calls": 0}
    try:
        return json.loads(COST_METER_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"cumulative_usd": 0.0, "calls": 0}


def save_cost_meter(meter: dict) -> None:
    COST_METER_PATH.parent.mkdir(parents=True, exist_ok=True)
    COST_METER_PATH.write_text(json.dumps(meter, indent=2), encoding="utf-8")


def usage_to_cost(usage) -> float:
    """Convert an anthropic Usage object to USD cost for one call."""
    inp = getattr(usage, "input_tokens", 0) or 0
    out = getattr(usage, "output_tokens", 0) or 0
    cache_w = getattr(usage, "cache_creation_input_tokens", 0) or 0
    cache_r = getattr(usage, "cache_read_input_tokens", 0) or 0
    return (
        inp * PRICE_INPUT_PER_MTOK / 1e6
        + out * PRICE_OUTPUT_PER_MTOK / 1e6
        + cache_w * PRICE_CACHE_WRITE_PER_MTOK / 1e6
        + cache_r * PRICE_CACHE_READ_PER_MTOK / 1e6
    )


def call_claude(system_blocks: list[dict], user_msg: str, cost_cap_usd: float) -> tuple[str, float]:
    """Call Claude. Returns (reply_text, this_call_cost_usd).

    Aborts BEFORE the call if the cumulative cost is already at/over the cap.
    Updates the persistent cost meter AFTER the call returns.
    """
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
            "ERROR: ANTHROPIC_API_KEY not set. Export it before running:\n"
            "  export ANTHROPIC_API_KEY=sk-ant-...",
            file=sys.stderr,
        )
        sys.exit(3)

    meter = load_cost_meter()
    if meter["cumulative_usd"] >= cost_cap_usd:
        print(
            f"COST CAP REACHED: cumulative ${meter['cumulative_usd']:.4f} "
            f">= cap ${cost_cap_usd:.2f}. Aborting before next call.\n"
            f"To raise the cap: pass --cost-cap, or edit/delete {COST_METER_PATH}",
            file=sys.stderr,
        )
        sys.exit(5)

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system_blocks,
        messages=[{"role": "user", "content": user_msg}],
    )
    parts = []
    for block in resp.content:
        if getattr(block, "type", None) == "text":
            parts.append(block.text)

    this_cost = usage_to_cost(resp.usage)
    meter["cumulative_usd"] += this_cost
    meter["calls"] += 1
    save_cost_meter(meter)
    print(
        f"  cost: ${this_cost:.4f} this call  |  cumulative: ${meter['cumulative_usd']:.4f} / ${cost_cap_usd:.2f} cap "
        f"(call #{meter['calls']})",
        file=sys.stderr,
    )

    return "".join(parts), this_cost


def write_sidecar(book: str, chapter: int, translations: dict[str, str]) -> Path:
    out_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}-english.json"
    payload = {
        "_note": (
            f"Draft English rendering of Saadia's JA Tafsir on {book.title()} {chapter}, "
            "generated by scripts/translate_tafsir_english.py against the JA "
            "(not the biblical Hebrew). Translation goal: reverse-translatability "
            "for the Tafsir reader — readers should be able to map English back to JA. "
            "Saadia-specific moves preserved per data-source/saadia-gloss-table.json; "
            "Blau's notes (data-source/blau-genesis-notes.json) consulted for Bereshit 1-12."
        ),
        "_status": "draft",
        "_model": MODEL,
        "translations": translations,
    }
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return out_path


def translate_chapter(book: str, chapter: int, system_blocks: list[dict], cost_cap_usd: float) -> int:
    """Translate one chapter. Returns exit code (0 success, 4 parse fail)."""
    src_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}.json"
    if not src_path.exists():
        print(f"missing source chapter: {src_path}", file=sys.stderr)
        return 1

    user_msg = build_user_message(book, chapter)
    print(f"calling Claude for {book} {chapter}...", file=sys.stderr)
    reply, _cost = call_claude(system_blocks, user_msg, cost_cap_usd)
    try:
        translations = parse_translations(reply)
    except Exception as e:
        print(f"failed to parse reply: {e}", file=sys.stderr)
        debug = DATA_DIR / f"tafsir-{book.lower()}-{chapter}-english.raw.txt"
        debug.write_text(reply, encoding="utf-8")
        print(f"raw reply written to {debug}", file=sys.stderr)
        return 4

    src = json.loads(src_path.read_text(encoding="utf-8"))
    expected_vs = {str(v["v"]) for v in src["verses"]}
    got = set(translations.keys())
    missing = expected_vs - got
    extra = got - expected_vs
    if missing:
        print(f"WARNING: missing verses in reply: {sorted(missing, key=int)}", file=sys.stderr)
    if extra:
        print(f"WARNING: unexpected verses in reply: {sorted(extra, key=lambda x: int(x) if x.isdigit() else 9999)}", file=sys.stderr)

    out = write_sidecar(book, chapter, translations)
    print(f"wrote {len(translations)} verses → {out.relative_to(ROOT)}")
    return 0


def discover_chapters(book: str) -> list[int]:
    """Return sorted list of chapter numbers that have source JSON for this book."""
    prefix = f"tafsir-{book.lower()}-"
    chs = []
    for p in DATA_DIR.iterdir():
        name = p.name
        if not name.startswith(prefix) or not name.endswith(".json"):
            continue
        stem = name[len(prefix):-len(".json")]
        # Skip english sidecars and any other dashed suffixes.
        if not stem.isdigit():
            continue
        chs.append(int(stem))
    return sorted(chs)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--book", required=True, help="e.g. bereshit, shemot")
    ap.add_argument("--chapter", type=int,
                    help="Single chapter. Omit (with --all) to run every chapter in the book.")
    ap.add_argument("--all", action="store_true",
                    help="Translate every chapter in --book that doesn't already have an English sidecar.")
    ap.add_argument("--force", action="store_true",
                    help="With --all, re-translate chapters that already have a sidecar.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print the request payload size and the user message preview without calling the API.")
    ap.add_argument("--cost-cap", type=float, default=DEFAULT_COST_CAP_USD,
                    help=f"Hard cap on cumulative USD spend across runs (default ${DEFAULT_COST_CAP_USD:.2f}). "
                         f"The cap survives restarts via {COST_METER_PATH}. Aborts before any call that would cross the cap.")
    ap.add_argument("--reset-cost-meter", action="store_true",
                    help="Reset the persistent cost meter to $0 before running.")
    ap.add_argument("--show-cost", action="store_true",
                    help="Print the current cumulative cost and exit.")
    args = ap.parse_args()

    if args.show_cost:
        meter = load_cost_meter()
        print(f"cumulative: ${meter['cumulative_usd']:.4f}  calls: {meter['calls']}")
        print(f"meter file: {COST_METER_PATH}")
        return 0

    if args.reset_cost_meter:
        save_cost_meter({"cumulative_usd": 0.0, "calls": 0})
        print(f"cost meter reset to $0 at {COST_METER_PATH}", file=sys.stderr)

    if not args.all and args.chapter is None:
        ap.error("either --chapter N or --all is required")

    system_blocks = build_system_blocks()

    if args.dry_run:
        ch = args.chapter if args.chapter is not None else (discover_chapters(args.book)[:1] or [1])[0]
        user_msg = build_user_message(args.book, ch)
        sys_chars = sum(len(b["text"]) for b in system_blocks)
        print(f"[dry-run] system chars: {sys_chars:>7,}  (~{sys_chars//4:,} tokens)")
        print(f"[dry-run] user chars:   {len(user_msg):>7,}  (~{len(user_msg)//4:,} tokens)")
        print(f"[dry-run] model:        {MODEL}")
        print(f"[dry-run] cache blocks: {sum(1 for b in system_blocks if 'cache_control' in b)}")
        print()
        print("--- USER MESSAGE PREVIEW (first 1200 chars) ---")
        print(user_msg[:1200])
        return 0

    if args.all:
        chapters = discover_chapters(args.book)
        if not chapters:
            print(f"no source chapters found for book={args.book}", file=sys.stderr)
            return 1
        skipped = 0
        for ch in chapters:
            out_path = DATA_DIR / f"tafsir-{args.book.lower()}-{ch}-english.json"
            if out_path.exists() and not args.force:
                skipped += 1
                continue
            rc = translate_chapter(args.book, ch, system_blocks, args.cost_cap)
            if rc != 0:
                print(f"halting --all at {args.book} {ch} (rc={rc})", file=sys.stderr)
                return rc
        print(f"done. translated {len(chapters)-skipped}, skipped {skipped} (already had sidecar)")
        meter = load_cost_meter()
        print(f"total cost so far: ${meter['cumulative_usd']:.4f} ({meter['calls']} API calls)")
        return 0

    return translate_chapter(args.book, args.chapter, system_blocks, args.cost_cap)


if __name__ == "__main__":
    raise SystemExit(main())

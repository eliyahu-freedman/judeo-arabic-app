"""Generate Lane-citing dictionary entries for high-frequency JA tokens.

For words whose JA sense matches standard classical Arabic (Lane's territory),
not Saadia-specific or Blau-diverging meanings. Output schema matches the
existing dictionary-starter.json `Entry` shape with `source: "lane"`.

Pipeline:
  1. Read candidates (token + freq) from /tmp/ja-candidates.json
     (produced by mining the tafsir corpus; see in-line mining block).
  2. Skip anything already covered by dictionary-starter.json,
     dictionary-lane.json (this file's output), or tafsir-divergence.json.
  3. For each remaining candidate, attach 1-2 example verses (book+ch+v
     + JA text) so Claude has actual context, not just a bare token.
  4. Batch ~25 candidates per Sonnet 4.6 call. Output is JSON with one
     entry per token.
  5. Merge into data/dictionary-lane.json; preserve prior entries.

Usage:
    export ANTHROPIC_API_KEY=...
    .venv-camel/bin/python3 scripts/generate_lane_entries.py --limit 15
    .venv-camel/bin/python3 scripts/generate_lane_entries.py --limit 200 --batch 25
    .venv-camel/bin/python3 scripts/generate_lane_entries.py --dry-run --limit 5
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 8000

# Sonnet 4.6 pricing per million tokens.
PRICE_IN = 3.00
PRICE_OUT = 15.00
PRICE_CW = 3.75
PRICE_CR = 0.30

COST_METER = Path.home() / ".cache" / "judeo-arabic-app" / "lane-entries-cost.json"


SYSTEM_INSTRUCTIONS = """You are producing dictionary entries for a Judeo-Arabic (JA) reader app aimed at Hebrew readers. The corpus is Saadia Gaon's Tafsir on the Torah, written in Arabic in Hebrew letters (~930 CE).

You will receive a batch of JA tokens with frequency counts and short example contexts. For each token, return ONE entry describing the WORD AS IT FUNCTIONS IN STANDARD CLASSICAL ARABIC. These are Lane's-Lexicon-territory words — common, non-Saadia-specific meanings. Words whose Saadia sense diverges from classical Arabic are handled separately in a divergence file; do NOT cover divergence here.

ENTRY SCHEMA — return strictly this JSON shape:
{
  "id": "kebab-case-unique-slug",          // ascii, e.g. "kana_was", "ibn", "bilad"
  "lemma_ja": "exact JA surface form",     // Hebrew letters, the token as it appears in the corpus
  "lemma_ar": "standard Arabic",           // with diacritics where helpful
  "root": "x-y-z",                         // tri- or quadri-radical, hyphenated, ISO transliteration (e.g. "k-w-n", "b-n-y", "ʕ-l-m")
  "pos": "noun (m.) | noun (f.) | verb | particle | preposition | conjunction | pronoun | adverb | proper noun | ...",
  "gloss_en": "one tight English sense, max ~12 words; semicolons for closely-related sub-senses",
  "gloss_he": "one tight Hebrew sense, max ~10 words; equivalent terminology",
  "source": "lane",
  "notes": "OPTIONAL — only if there's a non-obvious morphological note (e.g. 'plural of X', 'usually with article', 'often + suffix pronoun') OR if the JA orthography is non-standard (gershayim use). Skip the notes field entirely if there's nothing to say."
}

RULES:
- Translate the STANDARD ARABIC sense. If the user thinks Saadia might use the word in a special sense, they will check the divergence file. Your job here is the baseline classical meaning.
- If the surface form is clearly an inflected form (e.g. verb conjugated for 1sg/3pl, noun with pronoun suffix), give the entry FOR THE LEMMA (uninflected base form), and use `notes` to say "1sg perf. of ROOT" etc. Set `lemma_ja` to the surface form as supplied (so lookups hit), but lemma_ar / root / gloss reflect the base.
- For biblical proper names (Pharaoh, Moses, Jacob, Joseph, Aaron, Abraham, Israel, Egypt, etc.), pos = "proper noun"; root = "—"; gloss is the English/Hebrew name; notes can give the Hebrew biblical equivalent (פרעה, משה, etc.).
- For function words (לא, ת'ם, או, קד, הו, אנא, יא, אד'א, חתי, פלמא, ענד, בעד, etc.), pos = "particle" / "conjunction" / "preposition" / "pronoun" / "adverb"; root = "—"; gloss is the function (e.g. "negation; not", "then, thereupon", "or").
- Hebrew gloss should use natural Hebrew vocabulary readers expect from a Tanakh-adjacent register. For function words, give the Hebrew functional equivalent (לא, אז, או, כבר, הוא, אני, הו!, אם/כאשר, עד, כאשר, אצל, אחרי).
- Be sparing with `notes`. Most entries should omit it.
- DO NOT cite Blau in any field. DO NOT mark divergences here. If a token's most common Saadia use diverges from classical Arabic, return source "lane" anyway with the classical sense — divergent senses are tracked elsewhere.
- If a token is genuinely puzzling, you may set "pos": "uncertain" and give your best guess with a note flagging uncertainty.

OUTPUT FORMAT — strict:
Return ONLY a single JSON object: {"entries": [ ... ]}. No preamble, no markdown fences. Include EVERY token in the input, in the same order.
"""


def load_meter() -> dict:
    if not COST_METER.exists():
        return {"cumulative_usd": 0.0, "calls": 0}
    try:
        return json.loads(COST_METER.read_text(encoding="utf-8"))
    except Exception:
        return {"cumulative_usd": 0.0, "calls": 0}


def save_meter(m: dict) -> None:
    COST_METER.parent.mkdir(parents=True, exist_ok=True)
    COST_METER.write_text(json.dumps(m, indent=2), encoding="utf-8")


def usage_cost(usage) -> float:
    inp = getattr(usage, "input_tokens", 0) or 0
    out = getattr(usage, "output_tokens", 0) or 0
    cw = getattr(usage, "cache_creation_input_tokens", 0) or 0
    cr = getattr(usage, "cache_read_input_tokens", 0) or 0
    return inp * PRICE_IN / 1e6 + out * PRICE_OUT / 1e6 + cw * PRICE_CW / 1e6 + cr * PRICE_CR / 1e6


# ---------------- mining / context helpers ----------------

def strip_punct(s: str) -> str:
    return re.sub(r'^[.,:;؛،"\'\s]+|[.,:;؛،"\'\s]+$', '', s)


def normalize(t: str) -> str:
    t = strip_punct(t)
    if t.startswith('ו') and len(t) > 1:
        t = t[1:]
    if t.startswith('אל') and len(t) > 2:
        t = t[2:]
    return t


TOKEN_RE = re.compile(r"[א-ת']+")


def load_covered_keys() -> set[str]:
    """Tokens already covered by starter, prior lane output, or divergence."""
    covered: set[str] = set()
    for fn in ["dictionary-starter.json", "dictionary-lane.json", "tafsir-divergence.json"]:
        p = DATA / fn
        if not p.exists():
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        for e in d.get("entries", []):
            for k in (e.get("lemma_ja"), normalize(e.get("lemma_ja", ""))):
                if k:
                    covered.add(k)
            for v in (e.get("variants") or []):
                covered.add(v)
                covered.add(normalize(v))
    return covered


def build_context_index() -> dict[str, list[tuple[str, int, int, str]]]:
    """Map normalized-token → list of (book, chapter, verse_num, ja_text) hits.

    Limits to first ~3 hits per token to keep prompt size sane.
    """
    idx: dict[str, list[tuple[str, int, int, str]]] = collections.defaultdict(list)
    for fp in sorted(DATA.glob("tafsir-*-*.json")):
        name = fp.name
        if "-english" in name or "-alignment" in name:
            continue
        m = re.match(r"tafsir-([a-z]+)-(\d+)\.json$", name)
        if not m:
            continue
        book, ch = m.group(1), int(m.group(2))
        try:
            d = json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            continue
        for v in d.get("verses", []):
            text = v.get("ja", "") or ""
            vnum = v.get("v")
            for tok in TOKEN_RE.findall(text):
                n = normalize(tok)
                if not n:
                    continue
                if len(idx[n]) < 3:
                    idx[n].append((book, ch, vnum, text))
    return idx


# ---------------- API call ----------------

def build_system_blocks() -> list[dict]:
    return [
        {"type": "text", "text": SYSTEM_INSTRUCTIONS, "cache_control": {"type": "ephemeral"}},
    ]


def build_user_message(batch: list[dict]) -> str:
    lines = [
        "Write Lane-style entries for each of the following JA tokens.",
        "Return JSON: {\"entries\": [ ... ]} with one entry per token, in order.",
        "",
        "TOKENS:",
        "",
    ]
    for item in batch:
        tok = item["token"]
        freq = item["count"]
        ctx = item.get("contexts", [])
        lines.append(f"- {tok}  (freq={freq})")
        for (book, ch, v, text) in ctx[:2]:
            short = text if len(text) <= 140 else text[:140] + "…"
            lines.append(f"    ex {book[:3]} {ch}:{v}  {short}")
        lines.append("")
    return "\n".join(lines)


def call_claude(system_blocks: list[dict], user_msg: str, cost_cap: float) -> tuple[str, float]:
    try:
        import anthropic  # type: ignore
    except ImportError:
        print("ERROR: pip install anthropic", file=sys.stderr); sys.exit(2)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr); sys.exit(3)
    m = load_meter()
    if m["cumulative_usd"] >= cost_cap:
        print(f"COST CAP reached: ${m['cumulative_usd']:.4f} >= ${cost_cap:.2f}", file=sys.stderr); sys.exit(5)
    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system_blocks,
        messages=[{"role": "user", "content": user_msg}],
    )
    text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    cost = usage_cost(resp.usage)
    m["cumulative_usd"] += cost
    m["calls"] += 1
    save_meter(m)
    print(f"  call cost ${cost:.4f}  |  cumulative ${m['cumulative_usd']:.4f} (call #{m['calls']})", file=sys.stderr)
    return text, cost


def parse_entries(text: str) -> list[dict]:
    t = text.strip()
    if t.startswith("```"):
        lines = t.splitlines()
        lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        t = "\n".join(lines)
    s, e = t.find("{"), t.rfind("}")
    if s == -1 or e == -1:
        raise ValueError(f"no JSON in reply:\n{text[:300]}")
    obj = json.loads(t[s : e + 1])
    if "entries" not in obj:
        raise ValueError(f"reply missing 'entries' key: {list(obj.keys())}")
    return obj["entries"]


# ---------------- merge / write ----------------

def load_lane_dict() -> dict:
    p = DATA / "dictionary-lane.json"
    if not p.exists():
        return {
            "_note": "Lane-derived dictionary entries — standard classical Arabic meanings for high-frequency JA tokens in Saadia's Tafsir. Auto-generated by scripts/generate_lane_entries.py; reviewed for accuracy. For Saadia-specific or Blau-divergent senses, see data/tafsir-divergence.json.",
            "_source": "Lane's Lexicon (E.W. Lane, 1863-1893) — public domain. Entries paraphrase the standard classical Arabic meaning; not verbatim quotes from Lane.",
            "entries": [],
        }
    return json.loads(p.read_text(encoding="utf-8"))


def write_lane_dict(d: dict) -> None:
    p = DATA / "dictionary-lane.json"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=15, help="max candidates this run")
    ap.add_argument("--batch", type=int, default=25, help="candidates per API call")
    ap.add_argument("--min-freq", type=int, default=20, help="skip tokens with freq < this")
    ap.add_argument("--min-len", type=int, default=2, help="skip tokens shorter than this")
    ap.add_argument("--candidates-file", default="/tmp/ja-candidates.json")
    ap.add_argument("--cost-cap", type=float, default=5.0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cands_raw = json.loads(Path(args.candidates_file).read_text(encoding="utf-8"))
    covered = load_covered_keys()
    print(f"  covered already: {len(covered)} keys", file=sys.stderr)

    # Filter
    cands = [
        c for c in cands_raw
        if c["count"] >= args.min_freq
        and len(c["token"]) >= args.min_len
        and c["token"] not in covered
    ]
    cands = cands[: args.limit]
    print(f"  pipeline this run: {len(cands)} candidates", file=sys.stderr)
    if not cands:
        print("  nothing to do.", file=sys.stderr)
        return

    # Attach contexts
    ctx_idx = build_context_index()
    for c in cands:
        c["contexts"] = ctx_idx.get(c["token"], [])

    # Dry-run preview
    if args.dry_run:
        sample = build_user_message(cands[: min(5, len(cands))])
        print("--- SAMPLE USER MESSAGE (first 5) ---")
        print(sample)
        print("---")
        return

    # Batch + call
    lane = load_lane_dict()
    existing_ids = {e["id"] for e in lane["entries"]}
    existing_lemmas = {e["lemma_ja"] for e in lane["entries"]}

    system_blocks = build_system_blocks()
    added = 0
    for i in range(0, len(cands), args.batch):
        batch = cands[i : i + args.batch]
        user_msg = build_user_message(batch)
        print(f"\n=== batch {i // args.batch + 1} ({len(batch)} tokens) ===", file=sys.stderr)
        reply, _ = call_claude(system_blocks, user_msg, args.cost_cap)
        try:
            entries = parse_entries(reply)
        except Exception as e:
            print(f"  PARSE FAIL: {e}", file=sys.stderr)
            print("  raw reply:\n", reply[:600], file=sys.stderr)
            continue
        for e in entries:
            if not e.get("id") or not e.get("lemma_ja"):
                continue
            # de-dupe by id + lemma_ja (id-collision can happen for homographs)
            base_id = e["id"]
            suffix = 1
            while e["id"] in existing_ids:
                suffix += 1
                e["id"] = f"{base_id}_{suffix}"
            if e["lemma_ja"] in existing_lemmas and any(
                x for x in lane["entries"] if x["lemma_ja"] == e["lemma_ja"] and x["gloss_en"] == e.get("gloss_en")
            ):
                continue  # exact dup
            if "source" not in e:
                e["source"] = "lane"
            lane["entries"].append(e)
            existing_ids.add(e["id"])
            existing_lemmas.add(e["lemma_ja"])
            added += 1
        write_lane_dict(lane)
        print(f"  batch wrote {len(entries)} entries; running total {len(lane['entries'])}", file=sys.stderr)

    print(f"\nDONE: added {added} new entries; dictionary now has {len(lane['entries'])} entries.", file=sys.stderr)


if __name__ == "__main__":
    main()

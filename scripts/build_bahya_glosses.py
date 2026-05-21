"""Generate per-token contextual glosses for Bahya, Bab 1, via the Claude API.

The problem this fixes: data/dictionary-auto.json was built from Camel Tools'
MSA morphological analyzer. It glosses every occurrence of a lemma the same
way, and the lemma readings themselves are MSA — wrong register for an 11th-
century Andalusian Judeo-Arabic theological text. Example: ג'וה is glossed
"climate / atmosphere" (modern jaww), but in Bahya it is wujūh "aspects /
ways" with a prefixed waw; תוחיד is glossed "unification; standardization;
monotheism", but in Shaʿar ha-Yiḥud it specifically means "(affirming) divine
unity".

The fix: gloss each token in context using the JA sentence + Ibn Tibbon's
Hebrew + the working English (all already aligned in bahya-bab1-aligned.json).
Ibn Tibbon's per-word equivalences function as a gold-standard contextual
key; the LLM's job is mostly to read them off and emit a tidy JSON record.

Inputs:
  data/bahya-bab1-aligned.json — segments with {ja, he, en, isHeader?}

Output:
  data/bahya-bab1-glosses.json — keyed by page → segment index → token list.
  Each token entry: {token, norm, ar, root, pos, gloss_en, gloss_he, note}
  Tokens are emitted in surface order matching the renderer's tokenizer
  (lib/lookup.ts::tokenizeJa), so the reader can index by (page, segIdx,
  tokIdx) without re-tokenizing.

Usage:
    source .venv-camel/bin/activate       # or any venv with anthropic SDK
    export ANTHROPIC_API_KEY=sk-ant-...
    python3 scripts/build_bahya_glosses.py --pages מד          # one page
    python3 scripts/build_bahya_glosses.py                      # all pages
    python3 scripts/build_bahya_glosses.py --dry-run --pages מד # print prompt only

The script is resumable: if data/bahya-bab1-glosses.json already exists, any
page already present is skipped. Delete a page key to force a re-run.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ALIGNED_PATH = DATA / "bahya-bab1-aligned.json"
OUT_PATH = DATA / "bahya-bab1-glosses.json"

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 4000

# Sonnet 4.6 pricing (USD per million tokens), matches translate_tafsir_english.py
PRICE_INPUT_PER_MTOK = 3.00
PRICE_OUTPUT_PER_MTOK = 15.00
PRICE_CACHE_WRITE_PER_MTOK = 3.75
PRICE_CACHE_READ_PER_MTOK = 0.30

COST_METER_PATH = Path.home() / ".cache" / "judeo-arabic-app" / "translation-cost.json"
DEFAULT_COST_CAP_USD = 10.00

# Tokenization that mirrors lib/lookup.ts -------------------------------------

NIQQUD = set(
    "ְֱֲֳִֵֶַָׇ"
    "ֹֺֻֽֿׁׂׅׄ"
)
APOS_RE = re.compile("[׳״’‘ʼʹ]")
WORD_RE = re.compile(r"[֐-׿']+")


def clean_ja(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = APOS_RE.sub("'", text)
    return "".join(c for c in text if c not in NIQQUD)


def tokenize_ja(text: str) -> list[str]:
    return WORD_RE.findall(clean_ja(text))


def normalize_token(tok: str) -> str:
    """Mirror of lib/lookup.ts::normalizeToken — for fallback lemma lookup."""
    t = re.sub(r"^['.,:;؛،\"\s]+|['.,:;؛،\"\s]+$", "", tok)
    if t.startswith("ו") and len(t) > 1:
        t = t[1:]
    if t.startswith("אל") and len(t) > 2:
        t = t[2:]
    return t


# Prompt --------------------------------------------------------------------

SYSTEM = """You are an expert in classical and medieval Judeo-Arabic, specifically the language of Baḥya ibn Paquda's Ḥovot ha-Levavot — 11th-century Andalusian Judeo-Arabic in a theological-philosophical register. You will receive one aligned segment at a time:

  JA  — the original Judeo-Arabic
  HE  — Ibn Tibbon's classical Hebrew translation (Sefaria)
  EN  — a working English translation
  Tokens — a numbered list of JA tokens to gloss, in surface order, exactly as they appear in the JA

For each token, emit a contextual gloss. Use Ibn Tibbon's Hebrew and the English as your primary key to what the token means HERE — they are essentially per-phrase keys for what each JA word does in this sentence.

Output requirements:

1. Return STRICT JSON, nothing else (no markdown fences, no commentary). Schema:
   {"glosses":[
     {"i":1,"token":"<exact JA token>","ar":"<Arabic-script form, no vowels needed>","root":"<3-letter root or empty>","pos":"<noun|verb|prep|conj|pron|adj|adv|particle|proper|formula>","gloss_en":"<1–6 words>","gloss_he":"<1–6 words, vocalized if natural>","note":"<short, only if non-obvious>"},
     ...
   ]}

2. The number of objects MUST match the number of tokens, in the same order, with matching "i" indices starting at 1.

3. Glosses must be CONTEXTUAL, not lemma-generic:
   - תוחיד here = "divine unity / affirming God's oneness" (Heb. יִחוּד), NOT "standardization" and not just "monotheism" in the abstract.
   - וג'וה = "and aspects / and modes" (و + وجوه, plural of wajh; Heb. אָפְנֵי), NOT "and climate".
   - Resolve prefixes inside the gloss when natural ("and …", "by the …", "the …"), but keep "token" as the surface form.

4. JA orthography:
   - The ASCII apostrophe ' is the gershayim representing Arabic ج (ǧ) or ث (ṯ) etc. So כ' = خ, ת' = ث, ג' = ج, ד' = ذ, ז' = ظ, etc. Use the right Arabic letter in "ar".
   - Bahya writes the divine name as אללה (God), הר (with biblical citations), etc. Treat biblical quotations as Hebrew, not Arabic — give a brief English gloss and mark pos="proper" or "formula".

5. Honorifics and formulae:
   - ג'ל ועז after a divine name = jalla wa-ʿazza, "(may He be) magnified and exalted". Pos="formula".
   - ע"ס (after a prophet) = ʿalayhi al-salām, "peace be upon him". Pos="formula".
   - וגו' = "etc." (Heb. abbreviation).
   - Short fixed citation tags should be glossed as such, not parsed word-by-word.

6. Roots: 3 letters, Hebrew letters, no diacritics. Use empty string for particles, prepositions, foreign quotations, and formulae where the root is unhelpful.

7. Keep notes empty unless something genuinely helps a learner (e.g., "Aramaic-influenced sense", "Saadia gloss", "JA orthography for ث"). Do NOT explain obvious cognates.

Quality bar: a careful reader who knows Hebrew but no Arabic should be able to read the gloss_he column down a sentence and reconstruct the meaning of the JA.
"""


def build_user_msg(seg: dict, page_he: str, seg_idx: int, tokens: list[str]) -> str:
    lines = [
        f"Page: {page_he}",
        f"Segment index: {seg_idx}",
        f"Is header: {bool(seg.get('isHeader'))}",
        "",
        f"JA: {seg['ja']}",
        f"HE: {seg['he']}",
        f"EN: {seg['en']}",
        "",
        "Tokens to gloss, in order:",
    ]
    for i, t in enumerate(tokens, start=1):
        lines.append(f"  [{i}] {t}")
    lines.append("")
    lines.append("Return strict JSON only, as specified.")
    return "\n".join(lines)


# Cost meter (shared file with translate_tafsir_english.py) -------------------


def load_cost_meter() -> dict:
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


def call_claude(user_msg: str, cost_cap_usd: float) -> tuple[str, float]:
    try:
        import anthropic  # type: ignore
    except ImportError:
        print("ERROR: 'anthropic' SDK not installed. Run: pip install anthropic", file=sys.stderr)
        sys.exit(2)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set.", file=sys.stderr)
        sys.exit(3)

    meter = load_cost_meter()
    if meter["cumulative_usd"] >= cost_cap_usd:
        print(
            f"COST CAP REACHED: ${meter['cumulative_usd']:.4f} >= ${cost_cap_usd:.2f}",
            file=sys.stderr,
        )
        sys.exit(5)

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
    )
    parts = [b.text for b in resp.content if getattr(b, "type", None) == "text"]
    text = "".join(parts).strip()

    this_cost = usage_to_cost(resp.usage)
    meter["cumulative_usd"] += this_cost
    meter["calls"] += 1
    save_cost_meter(meter)
    print(
        f"  cost: ${this_cost:.4f} | cumulative ${meter['cumulative_usd']:.4f}/${cost_cap_usd:.2f}",
        file=sys.stderr,
    )
    return text, this_cost


# Parsing / validation -------------------------------------------------------


def parse_glosses(reply: str, expected_tokens: list[str]) -> list[dict]:
    # The model is told to emit pure JSON, but be defensive about stray fences.
    s = reply.strip()
    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*|\s*```$", "", s, flags=re.MULTILINE).strip()
    obj = json.loads(s)
    glosses = obj.get("glosses")
    if not isinstance(glosses, list):
        raise ValueError("reply has no 'glosses' list")
    if len(glosses) != len(expected_tokens):
        raise ValueError(
            f"expected {len(expected_tokens)} glosses, got {len(glosses)}"
        )
    out = []
    for idx, (g, want) in enumerate(zip(glosses, expected_tokens), start=1):
        if g.get("token") != want:
            raise ValueError(
                f"token mismatch at i={idx}: expected {want!r}, got {g.get('token')!r}"
            )
        out.append(
            {
                "token": want,
                "norm": normalize_token(want),
                "ar": g.get("ar", ""),
                "root": g.get("root", ""),
                "pos": g.get("pos", ""),
                "gloss_en": g.get("gloss_en", ""),
                "gloss_he": g.get("gloss_he", ""),
                "note": g.get("note", "") or "",
            }
        )
    return out


# Main -----------------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", nargs="*", help="restrict to specific page refs (Hebrew, e.g. מד)")
    ap.add_argument("--cost-cap", type=float, default=DEFAULT_COST_CAP_USD)
    ap.add_argument("--dry-run", action="store_true", help="print prompts; do not call API")
    ap.add_argument("--force", action="store_true", help="re-run pages even if already present")
    args = ap.parse_args()

    aligned = json.loads(ALIGNED_PATH.read_text(encoding="utf-8"))
    pages_data = aligned["pages"]

    existing = {}
    if OUT_PATH.exists():
        existing = json.loads(OUT_PATH.read_text(encoding="utf-8"))
    out_pages: dict = existing.get("pages", {})

    page_refs = args.pages if args.pages else list(pages_data.keys())

    for page_he in page_refs:
        if page_he not in pages_data:
            print(f"skip: page {page_he!r} not in aligned data", file=sys.stderr)
            continue
        if not args.force and page_he in out_pages:
            print(f"skip: page {page_he} already has glosses (use --force to re-run)", file=sys.stderr)
            continue

        print(f"\n=== page {page_he} ===", file=sys.stderr)
        page_out = []
        for seg_idx, seg in enumerate(pages_data[page_he]):
            tokens = tokenize_ja(seg["ja"])
            if not tokens:
                page_out.append({"segment": seg_idx, "tokens": []})
                continue
            user_msg = build_user_msg(seg, page_he, seg_idx, tokens)
            print(f"  seg {seg_idx}: {len(tokens)} tokens", file=sys.stderr)
            if args.dry_run:
                print("--- USER MSG ---")
                print(user_msg)
                print("--- END ---")
                continue
            reply, _cost = call_claude(user_msg, args.cost_cap)
            try:
                gl = parse_glosses(reply, tokens)
            except (json.JSONDecodeError, ValueError) as e:
                print(f"  PARSE ERROR on seg {seg_idx}: {e}", file=sys.stderr)
                print(f"  RAW REPLY:\n{reply}", file=sys.stderr)
                sys.exit(4)
            page_out.append({"segment": seg_idx, "tokens": gl})

        if not args.dry_run:
            out_pages[page_he] = page_out
            payload = {
                "_note": (
                    "Per-token contextual glosses for Bahya, Ḥovot ha-Levavot, Shaʿar "
                    "ha-Yiḥud, generated by scripts/build_bahya_glosses.py from "
                    "bahya-bab1-aligned.json (JA + Ibn Tibbon HE + working EN). The "
                    "reader looks up tokens here first; falls back to dictionary-auto."
                ),
                "_model": MODEL,
                "_status": "draft",
                "pages": out_pages,
            }
            OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"  wrote {OUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()

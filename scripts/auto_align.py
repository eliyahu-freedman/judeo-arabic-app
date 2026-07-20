"""
Automatically generate phrase-pair alignments for Bahya aligned JSON files.

For each segment with fewer than 3 pairs, calls Claude Haiku to extract
5-8 phrase-level JA↔EN correspondences. Validated pairs are merged into
the existing pairs array (deduped, capped at 8).

Usage:
  python3 scripts/auto_align.py bab7 bab8 bab9 bab10 hakdamah
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import os

import anthropic

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# Load .env.local if ANTHROPIC_API_KEY not already set
if not os.environ.get("ANTHROPIC_API_KEY"):
    env_file = ROOT / ".env.local"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

SYSTEM_PROMPT = """\
You are a Judeo-Arabic (Hebrew-script Arabic) scholar helping build a phrase-alignment reader for Bahya ibn Paquda's Chovot HaLevavot (Duties of the Heart).

Given a Judeo-Arabic segment (written in Hebrew letters) and its English translation, identify 5-8 phrase-level correspondences as a JSON array:
[{"ja": "...", "en": "..."}, ...]

Rules:
- The "ja" value MUST appear verbatim as a substring of the JA text provided.
- The "en" value MUST appear verbatim (case-insensitive) as a substring of the EN text provided.
- Prefer phrases of 2-5 words; include key nouns, verbs, epithets, and technical terms.
- Cover different parts of the text — do not cluster all pairs at the beginning.
- Do not return the entire segment as a single pair.
- Return ONLY the JSON array, no other text."""


def call_haiku(client: anthropic.Anthropic, ja: str, en: str) -> list[dict]:
    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        temperature=0,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"JA: {ja}\n\nEN: {en}"}],
    )
    raw = msg.content[0].text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw)


def validate_pairs(pairs: list[dict], ja: str, en: str) -> list[dict]:
    en_lower = en.lower()
    valid = []
    for p in pairs:
        ja_val = p.get("ja", "")
        en_val = p.get("en", "")
        if ja_val and en_val and ja_val in ja and en_val.lower() in en_lower:
            valid.append({"ja": ja_val, "en": en_val})
    return valid


def merge_pairs(existing: list[dict], new: list[dict]) -> list[dict]:
    seen: set[str] = {p["ja"] for p in existing}
    merged = list(existing)
    for p in new:
        if p["ja"] not in seen:
            seen.add(p["ja"])
            merged.append(p)
    return merged[:8]


def process_slug(slug: str, client: anthropic.Anthropic) -> None:
    path = DATA_DIR / f"bahya-{slug}-aligned.json"
    if not path.exists():
        print(f"[{slug}] ERROR: {path.name} not found.")
        return

    data = json.loads(path.read_text(encoding="utf-8"))
    total = calls = enriched = skipped = 0

    for page_key, segs in data["pages"].items():
        for seg in segs:
            total += 1
            ja: str = seg.get("ja", "")
            en: str = seg.get("en", "")
            existing_pairs: list[dict] = seg.get("pairs", [])

            # Skip if already has enough pairs or no content to align
            if len(existing_pairs) >= 3 or not ja.strip() or not en.strip():
                skipped += 1
                continue

            try:
                raw_pairs = call_haiku(client, ja, en)
                valid = validate_pairs(raw_pairs, ja, en)
                seg["pairs"] = merge_pairs(existing_pairs, valid)
                calls += 1
                if seg["pairs"]:
                    enriched += 1
            except Exception as exc:
                print(f"  [{slug}] page {page_key}: API error — {exc}")
                skipped += 1
                time.sleep(1)

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    all_segs = [s for pg in data["pages"].values() for s in pg]
    with_pairs = sum(1 for s in all_segs if s.get("pairs"))
    avg = sum(len(s.get("pairs", [])) for s in all_segs) / max(len(all_segs), 1)
    print(
        f"[{slug}] {total} segs | {calls} API calls | "
        f"{with_pairs}/{total} have pairs | avg {avg:.1f} pairs/seg"
    )


def main() -> None:
    slugs = sys.argv[1:]
    if not slugs:
        sys.exit("usage: auto_align.py <slug> [<slug> ...]")

    client = anthropic.Anthropic()
    for slug in slugs:
        process_slug(slug, client)


if __name__ == "__main__":
    main()

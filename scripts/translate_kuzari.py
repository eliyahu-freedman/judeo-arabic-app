#!/usr/bin/env python3
"""
Translate all Kuzari maqalat from Judeo-Arabic → aligned English using Claude.

For each page not yet in the aligned JSON, calls Claude to produce AlignedSegment[]:
  { ja, en, pairs: [{ja, en}] }   (or { ja, en, isHeader: true } for headers)

Saves incrementally so it can be interrupted and resumed at any time.
After completion, outputs stubs for maqala-2..5 english JSON as well.

Usage:
  python3 scripts/translate_kuzari.py [--maqala N] [--model MODEL]

Options:
  --maqala N    Translate only maqala N (1-5). Default: all.
  --model       Claude model. Default: claude-sonnet-4-6
  --dry-run     Print what would happen without calling the API.
"""
from __future__ import annotations

import anthropic
import argparse
import json
import sys
import time
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"
TRANSLATOR = "Eliyahu Freedman (working draft)"

# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

SYSTEM = """\
You are a scholarly translator rendering Yehuda Halevi's Kitāb al-Khazarī (12th century) \
from Judeo-Arabic (Arabic written in Hebrew characters) into English. Your translations are \
accurate, readable, and preserve the philosophical register of the original.

Produce a JSON ARRAY of "aligned segments." Each segment is one natural unit of text — \
a sentence, a short exchange, or a brief clause group. The format is:

Regular segment:
{
  "ja": "<the exact Judeo-Arabic text of this segment>",
  "en": "<English translation>",
  "pairs": [
    {"ja": "<JA key phrase>", "en": "<English translation of that phrase>"},
    ...
  ]
}

Header / section marker only (no pairs):
{
  "ja": "<header text>",
  "en": "<English translation>",
  "isHeader": true
}

RULES:
- Produce 5–20 segments per page (aim for ~8–14 for a typical page).
- The "pairs" array covers the main semantic phrases of the segment — \
  3 to 6 pairs, each 2–8 JA words. Do NOT try to cover every word; \
  focus on the phrases that carry the meaning.
- Section/chapter markers of the form "מאמר א · סימן ב" → isHeader: true, \
  translate מאמר as "Treatise", סימן as "Section".
- For dialogue, a short speech attribution like "אמר אלחכים" ("the Sage said") \
  may begin a segment, but keep it short — put the actual speech as its own segment.
- Translate consistently: מאמר=Treatise, סימן=Section, חכים=Sage, \
  פילסוף=philosopher, חבר=rabbi, מלך=king, אלכ'זר=the Khazar.
- Output ONLY the raw JSON array. No markdown fences, no commentary.

FEW-SHOT EXAMPLE (page 3 of the text):
Input:
"סילת עמא ענדי מן אלאחתג'אג' עלי מכ'אלפינא מן אלפלאספה ואהל אלאדיאן, ת'ם עלי אלכ'וארג' אלד'ין יכ'אלפון אלג'מהור."

Output segment:
{
  "ja": "סילת עמא ענדי מן אלאחתג'אג' עלי מכ'אלפינא מן אלפלאספה ואהל אלאדיאן, ת'ם עלי אלכ'וארג' אלד'ין יכ'אלפון אלג'מהור.",
  "en": "I was asked about the arguments I have at my disposal against those who differ from us — the philosophers and the followers of other religions — and then against the sectarians who dissent from the majority.",
  "pairs": [
    {"ja": "סילת", "en": "I was asked"},
    {"ja": "מן אלאחתג'אג'", "en": "about the arguments"},
    {"ja": "עלי מכ'אלפינא", "en": "against those who differ from us"},
    {"ja": "מן אלפלאספה ואהל אלאדיאן", "en": "the philosophers and the followers of other religions"},
    {"ja": "עלי אלכ'וארג'", "en": "against the sectarians"},
    {"ja": "יכ'אלפון אלג'מהור", "en": "dissent from the majority"}
  ]
}
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_aligned(path: Path) -> dict[str, list]:
    if path.exists():
        return json.loads(path.read_text()).get("pages", {})
    return {}


def save_aligned(path: Path, pages: dict[str, list]) -> None:
    path.write_text(json.dumps({"pages": pages}, ensure_ascii=False, indent=2))


def translate_page(
    client: anthropic.Anthropic,
    page_he: str,
    paragraphs: list[str],
    model: str,
    maqala: int,
) -> list[dict]:
    ja_text = "\n\n".join(paragraphs)
    msg = client.messages.create(
        model=model,
        max_tokens=4096,
        system=SYSTEM,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Translate the following Judeo-Arabic page from Maqala {maqala} "
                    f"of the Kuzari (page {page_he} in the FJMS edition) "
                    f"into aligned English segments:\n\n{ja_text}"
                ),
            }
        ],
    )
    raw = msg.content[0].text.strip()
    # Strip accidental markdown fences
    if raw.startswith("```"):
        raw = raw[raw.find("\n") + 1 :]
    if raw.endswith("```"):
        raw = raw[: raw.rfind("```")].strip()
    return json.loads(raw)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--maqala", type=int, choices=range(1, 6))
    parser.add_argument("--model", default="claude-sonnet-4-6")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    client = anthropic.Anthropic()
    maqalas = [args.maqala] if args.maqala else [1, 2, 3, 4, 5]

    grand_done = grand_todo = 0

    for maq in maqalas:
        gate_path = DATA / f"kuzari-maqala-{maq}.json"
        aligned_path = DATA / f"kuzari-maqala-{maq}-aligned.json"
        english_path = DATA / f"kuzari-maqala-{maq}-english.json"

        gate = json.loads(gate_path.read_text())
        aligned_pages = load_aligned(aligned_path)

        todo = [p for p in gate["pages"] if p["page_he"] not in aligned_pages]
        done_count = len(gate["pages"]) - len(todo)
        print(
            f"\nMaqala {maq}: {len(todo)} pages to translate "
            f"({done_count} already done, {len(gate['pages'])} total)"
        )
        grand_done += done_count
        grand_todo += len(todo)

        if args.dry_run:
            for p in todo[:3]:
                print(f"  [dry-run] would translate page {p['page_he']}")
            if len(todo) > 3:
                print(f"  ... and {len(todo) - 3} more")
            continue

        for i, page in enumerate(todo):
            page_he = page["page_he"]
            print(
                f"  Page {page_he} ({i + 1}/{len(todo)})...",
                end=" ",
                flush=True,
            )
            try:
                segments = translate_page(
                    client, page_he, page["paragraphs"], args.model, maq
                )
                aligned_pages[page_he] = segments
                print(f"✓  {len(segments)} segments")
                save_aligned(aligned_path, aligned_pages)
            except json.JSONDecodeError as e:
                print(f"JSON ERROR on page {page_he}: {e}")
                print("  Skipping this page and continuing...")
                time.sleep(1)
            except Exception as e:
                print(f"ERROR: {e}")
                print("  Saving progress and aborting maqala.")
                save_aligned(aligned_path, aligned_pages)
                break

        # Create english stub (translator metadata) for maqala 2-5
        if not english_path.exists():
            english_path.write_text(
                json.dumps(
                    {"translator": TRANSLATOR, "paragraphs": []},
                    ensure_ascii=False,
                    indent=2,
                )
            )
            print(f"  Wrote {english_path.name}")

    print(f"\n{'DRY RUN — ' if args.dry_run else ''}Summary: {grand_done} pages already done, {grand_todo} pages translated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

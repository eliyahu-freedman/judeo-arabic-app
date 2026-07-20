#!/usr/bin/env python3
"""translate_emunot.py — Add English aligned segments to JA-only Emunot chapters.

Usage:
  python3 scripts/translate_emunot.py              # translate all ja_only chapters
  python3 scripts/translate_emunot.py --only m2f1  # translate one chapter
  python3 scripts/translate_emunot.py --dry-run    # print JSON, don't write files
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import anthropic

REPO = Path(__file__).parent.parent
DATA = REPO / "data"

# Few-shot examples from m1f1 so the model understands the expected format
EXAMPLE = [
    {
        "ja": "אלמקאלה אלאולי פי אן אלמוג'ודאת כלהא מחדת'ה.",
        "en": "The First Maamar: That All Existing Things Are Newly-Made.",
        "isHeader": True,
        "pairs": [
            {"ja": "אלמקאלה אלאולי", "en": "The First Maamar"},
            {"ja": "אלמוג'ודאת כלהא", "en": "All Existing Things"},
            {"ja": "מחדת'ה", "en": "Are Newly-Made"},
        ],
    },
    {
        "ja": "קאל צאחב אלכתאב, מקדמהֵ הד'ה אלמקאלה אן כל מן יכ'וץ' פיהא ילתמס שיא לם יקע עליה אלעיאן ולא אדרכתה אלחואס,",
        "en": "The author of the book says — a preamble to this maamar: whoever engages in this inquiry seeks something that has not come under direct observation, nor been grasped by the senses;",
        "pairs": [
            {"ja": "קאל צאחב אלכתאב", "en": "The author of the book says"},
            {
                "ja": "לם יקע עליה אלעיאן ולא אדרכתה אלחואס",
                "en": "has not come under direct observation, nor been grasped by the senses",
            },
        ],
    },
    {
        "ja": "לכנה ירום את'באתה מן טריק אלאסתדלאל באלמעקול, והו כיף כאנת אלאשיא קבלנא.",
        "en": "rather, he aims to establish it by way of rational inference — namely: what things were like before us.",
        "pairs": [
            {"ja": "מן טריק אלאסתדלאל באלמעקול", "en": "by way of rational inference"},
            {"ja": "כיף כאנת אלאשיא קבלנא", "en": "what things were like before us"},
        ],
    },
]

SYSTEM = """\
You are translating Saadia Gaon's Kitāb al-Amānāt wa'l-Iʿtiqādāt (Emunot v'Deot, 933 CE) \
from Judeo-Arabic (Hebrew script) into scholarly but accessible English.

Rules:
1. Break the JA text into SHORT segments — one tight sentence or clause per segment \
(aim for ~80–130 JA chars; never lump a full paragraph into one segment).
2. For each segment provide:
   • ja   — the exact JA substring (copy it verbatim; do not modify)
   • en   — clear, flowing English translation (Alter-style precision, no archaism)
   • pairs — 3–6 short JA↔EN phrase pairs for phrase-level hover highlighting
3. Mark standalone section headers (chapter titles, maamar labels) with "isHeader": true.
4. Dots in the JA (e.g. "מאמר. ב:.") are FJMS typographic artifacts — preserve them \
in ja but render the English cleanly (e.g. "Maamar II:").
5. Use the key-term glossary provided; keep technical terms consistent across segments.
6. The JA paragraphs may contain \\n (FJMS line breaks, not paragraph breaks) — \
treat each page block as continuous prose and segment at natural clause boundaries.
7. Return ONLY valid JSON, no markdown fences, no commentary:
{"pages":[{"page_he":"<he>","aligned":[{"ja":"...","en":"...","pairs":[{"ja":"...","en":"..."},...]},...]},...]}
"""


def is_already_translated(chapter: dict) -> bool:
    return any(page.get("aligned") for page in chapter.get("pages", []))


def build_prompt(chapter: dict) -> str:
    parts: list[str] = []

    section = chapter.get("section", "")
    intro = chapter.get("intro", "")
    terms = chapter.get("terms", [])
    pages = chapter["pages"]

    parts.append(f"Chapter: {section}")
    if intro:
        parts.append(f"Context: {intro}")

    if terms:
        parts.append("\nKey terms — use these English glosses consistently:")
        for t in terms:
            line = f"  • {t['ja']}"
            if t.get("translit"):
                line += f" ({t['translit']})"
            line += f' = "{t["gloss"]}"'
            if t.get("note"):
                line += f" — {t['note']}"
            parts.append(line)

    parts.append("\nFormat example (two segments from Maamar I):")
    parts.append(json.dumps(EXAMPLE, ensure_ascii=False, indent=2))

    parts.append(
        "\nNow translate ALL of the following pages. "
        "Return ONLY the JSON object (no explanation)."
    )

    for page in pages:
        page_he = page["page_he"]
        raw = " ".join(
            p.replace("\n", " ").strip() for p in page.get("paragraphs", [])
        )
        parts.append(f"\nPage {page_he}:\n{raw}")

    return "\n".join(parts)


def call_api(client: anthropic.Anthropic, prompt: str) -> dict:
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=8192,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.content[0].text.strip()

    # Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Strip possible markdown fence
    m = re.search(r"```(?:json)?\s*(\{.+?\})\s*```", text, re.DOTALL)
    if m:
        return json.loads(m.group(1))

    # Find outermost {...}
    m = re.search(r"\{.+\}", text, re.DOTALL)
    if m:
        return json.loads(m.group(0))

    raise ValueError(f"Could not parse JSON from model response:\n{text[:400]}")


def merge(chapter: dict, translated: dict) -> dict:
    page_map = {p["page_he"]: p["aligned"] for p in translated["pages"]}

    new_pages = []
    for page in chapter["pages"]:
        he = page["page_he"]
        if he in page_map:
            new_pages.append({"page_he": he, "aligned": page_map[he]})
        else:
            new_pages.append(page)  # keep original if model missed it

    result = {k: v for k, v in chapter.items() if k != "pages"}
    result["pages"] = new_pages
    return result


def segment_count(chapter: dict) -> int:
    return sum(len(p.get("aligned", [])) for p in chapter.get("pages", []))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", metavar="SLUG", help="translate a single chapter (e.g. m2f1)")
    ap.add_argument("--dry-run", action="store_true", help="print output JSON, don't write")
    args = ap.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ANTHROPIC_API_KEY not set")

    client = anthropic.Anthropic(api_key=api_key)

    files = sorted(DATA.glob("saadia-emunot-m*.json"))
    if args.only:
        slug = args.only
        target = DATA / f"saadia-emunot-{slug}.json"
        if not target.exists():
            sys.exit(f"File not found: {target}")
        files = [target]

    total = len(files)
    skipped = 0
    done = 0
    errors = []

    for path in files:
        slug = path.stem.replace("saadia-emunot-", "")
        chapter = json.loads(path.read_text())

        if is_already_translated(chapter):
            print(f"  skip  {slug} (already has aligned)")
            skipped += 1
            continue

        print(f"  ...   {slug}", end=" ", flush=True)
        try:
            prompt = build_prompt(chapter)
            translated = call_api(client, prompt)
            merged = merge(chapter, translated)
            n = segment_count(merged)
            print(f"✓  ({n} segments)")

            if args.dry_run:
                print(json.dumps(merged, ensure_ascii=False, indent=2))
            else:
                path.write_text(json.dumps(merged, ensure_ascii=False, indent=2))
            done += 1

        except Exception as exc:
            print(f"✗  ERROR: {exc}")
            errors.append((slug, str(exc)))

    print(f"\nDone: {done} translated, {skipped} skipped, {len(errors)} errors")
    if errors:
        print("Errors:")
        for slug, msg in errors:
            print(f"  {slug}: {msg}")


if __name__ == "__main__":
    main()

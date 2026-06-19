#!/usr/bin/env python3
"""Build a Judeo-Arabic concordance over the Advanced library (Moreh, Bahya,
Saadia Emunot, Qirqisani, Kuzari) → data/advanced-index.json.

Keyed by `normalize_token` (the Python mirror of lib/lookup.ts:normalizeToken),
so a lemma page's key — normalizeToken(lemma_ja) — looks the entry up directly,
exactly as the Tafsir concordance in lib/lexicon.ts does. Tokenisation uses the
SAME CLI (_tokenize_ja_cli.ts) and the SAME Arabic→JA conversion the reader uses,
inheriting all of coverage_advanced.py's text-extraction logic.

Run:  python3 scripts/build_advanced_index.py
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "scripts"))

from coverage_report import normalize_token, strip_punct, tokenise_via_cli, chunked  # noqa: E402
from coverage_advanced import gather_ja_strings, TEXTS  # noqa: E402

_lex = Path.home() / "Tools" / "arabic-lexicon"
sys.path.insert(0, str(_lex))
import ja_script  # noqa: E402

MOREH_BASE = "/advanced/rambam-moreh-nevukhim"
HEB_POINTS = re.compile(r"[֑-ׇ]")
SNIPPET_CAP = 140  # length of the single sample snippet kept per key
ATT_CAP = 40       # max distinct work-rows stored per key


def work_for(fname: str) -> tuple[str, str]:
    """(display label, reader href) for an Advanced-text filename."""
    m = re.match(r"moreh-bab(\d+)\.json", fname)
    if m:
        n = int(m.group(1))
        return f"Moreh I:{n}", MOREH_BASE if n == 1 else f"{MOREH_BASE}/{n}"
    m = re.match(r"bahya-bab(\d+)\.json", fname)
    if m:
        return f"Bahya · Gate {m.group(1)}", "/advanced/bahya"
    if fname == "bahya-hakdamah.json":
        return "Bahya · Introduction", "/advanced/bahya"
    if fname == "kuzari-maqala1.json":
        return "Kuzari · I", "/advanced/kuzari"
    if fname == "saadia-emunot-intro.json":
        return "Saadia · Emunot (intro)", "/advanced/saadia-emunot-vedeot"
    if fname == "qirqisani-anwar-maqala1.json":
        return "Qirqisani · al-Anwār I", "/advanced/qirqisani-anwar"
    return fname, "/advanced"


def clean_surface(tok: str) -> str:
    return re.sub(r"^[.,:;؛،\"'\s]+|[.,:;؛،\"'\s]+$", "", tok)


def main() -> int:
    # key -> { count, att: { href: {work, href, n} }, sample: {surface, snippet} }
    tokens: dict[str, dict] = {}

    for label, fname, _in_scope, script in TEXTS:
        path = DATA / fname
        if not path.exists():
            continue
        work_label, href = work_for(fname)
        segments: list[str] = []
        gather_ja_strings(json.loads(path.read_text()), segments)

        for chunk in chunked(segments, 64):
            toks_per_seg = tokenise_via_cli(chunk)
            for seg, words in zip(chunk, toks_per_seg):
                snippet = seg.strip()
                if len(snippet) > SNIPPET_CAP:
                    snippet = snippet[:SNIPPET_CAP].rstrip() + "…"
                for w in words:
                    jw = ja_script.ar_to_ja(w) if script == "arabic" else w
                    jw = HEB_POINTS.sub("", jw)
                    if not strip_punct(jw):
                        continue
                    key = normalize_token(jw)
                    if not key:
                        continue
                    surface = clean_surface(jw)
                    bucket = tokens.setdefault(
                        key, {"count": 0, "att": {}, "sample": None}
                    )
                    bucket["count"] += 1
                    a = bucket["att"].get(href)
                    if a:
                        a["n"] += 1
                    else:
                        bucket["att"][href] = {"work": work_label, "href": href, "n": 1}
                    if bucket["sample"] is None:
                        bucket["sample"] = {"surface": surface, "snippet": snippet}

    out_tokens: dict[str, dict] = {}
    for key, b in tokens.items():
        att = sorted(b["att"].values(), key=lambda a: (-a["n"], a["work"]))
        out_tokens[key] = {
            "count": b["count"],
            "att": att[:ATT_CAP],
            "truncated": len(att) > ATT_CAP,
            "sample": b["sample"],
        }

    doc = {
        "_note": "Judeo-Arabic concordance over the Advanced library, keyed by "
                 "normalizeToken. Built by scripts/build_advanced_index.py.",
        "totals": {
            "keys": len(out_tokens),
            "tokens": sum(b["count"] for b in tokens.values()),
        },
        "tokens": out_tokens,
    }
    path = DATA / "advanced-index.json"
    # Compact (no indent): generated artifact, loaded server-side once.
    path.write_text(json.dumps(doc, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {path}: keys={doc['totals']['keys']} tokens={doc['totals']['tokens']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

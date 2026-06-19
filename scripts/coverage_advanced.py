#!/usr/bin/env python3
"""
Advanced-reader dictionary coverage report + 100% gate.

The Tafsir coverage script (`scripts/coverage_report.py`) only scans the
Pentateuch `tafsir-*.json` corpus. This sibling does the same job for the
Advanced library texts (Bahya, Maimonides' Moreh, HaLevi's Kuzari, Saadia's
Emunot), whose vocabulary is largely absent from the Tafsir-tuned dictionary.

For each text it tokenises the Judeo-Arabic via the canonical TS tokeniser
(`scripts/_tokenize_ja_cli.ts`) and runs every word through the same
prefix-strip candidate chain as `lib/lookup.ts:lookup`, bucketing as:

  - hand-starter : matched a lemma/variant in dictionary-starter.json
  - hand-lane    : matched a lemma/variant in dictionary-lane.json
  - miss         : no entry (the Camel auto dict is retired, like the runtime)

Writes `data/coverage-advanced.json` (per-text breakdown + ranked misses) and
prints a summary. Exits non-zero if any IN-SCOPE text is below 100% coverage —
this is the per-text gate (in the spirit of the Tafsir per-book divergence
gates). Out-of-scope texts (Bahya, until its curation phase) are reported but
do not fail the gate.

Lookup-chain parity is maintained by mirroring `lib/lookup.ts`; if that file
changes, update the helpers here in lock-step. (They are copied verbatim from
`scripts/coverage_report.py`.)
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

# Reuse the exact helpers from the Tafsir coverage script so the candidate
# chain and tokeniser bridge can never drift between the two reports.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from coverage_report import (  # noqa: E402
    ROOT,
    DATA,
    strip_punct,
    candidate_chain,
    load_dict_index,
    tokenise_via_cli,
    chunked,
    miss_bucket,
)

# (label, json filename, in_scope?, script). In-scope texts are gated to 100%.
# Arabic-script texts (Qirqisani's al-Anwar) are converted token-by-token to
# Judaeo-Arabic via the toolkit's ar_to_ja before the candidate chain — the
# exact runtime path (lib/arabicToJa.ts → lookup) the reader takes.
TEXTS: list[tuple[str, str, bool, str]] = [
    ("moreh-bab1", "moreh-bab1.json", True, "hebrew"),
    ("moreh-bab2", "moreh-bab2.json", True, "hebrew"),
    ("moreh-bab3", "moreh-bab3.json", True, "hebrew"),
    ("moreh-bab4", "moreh-bab4.json", True, "hebrew"),
    ("moreh-bab5", "moreh-bab5.json", True, "hebrew"),
    ("moreh-bab6", "moreh-bab6.json", True, "hebrew"),
    ("moreh-bab7", "moreh-bab7.json", True, "hebrew"),
    ("moreh-bab8", "moreh-bab8.json", True, "hebrew"),
    ("moreh-bab9", "moreh-bab9.json", True, "hebrew"),
    ("moreh-bab10", "moreh-bab10.json", True, "hebrew"),
    ("moreh-bab11", "moreh-bab11.json", True, "hebrew"),
    ("moreh-bab12", "moreh-bab12.json", True, "hebrew"),
    ("moreh-bab13", "moreh-bab13.json", True, "hebrew"),
    ("moreh-bab14", "moreh-bab14.json", True, "hebrew"),
    ("moreh-bab15", "moreh-bab15.json", True, "hebrew"),
    ("moreh-bab16", "moreh-bab16.json", True, "hebrew"),
    ("moreh-bab17", "moreh-bab17.json", True, "hebrew"),
    ("moreh-bab18", "moreh-bab18.json", True, "hebrew"),
    ("moreh-bab19", "moreh-bab19.json", True, "hebrew"),
    ("moreh-bab20", "moreh-bab20.json", True, "hebrew"),
    ("moreh-bab21", "moreh-bab21.json", True, "hebrew"),
    ("moreh-bab22", "moreh-bab22.json", True, "hebrew"),
    ("moreh-bab23", "moreh-bab23.json", True, "hebrew"),
    ("moreh-bab24", "moreh-bab24.json", True, "hebrew"),
    ("moreh-bab25", "moreh-bab25.json", True, "hebrew"),
    ("moreh-bab26", "moreh-bab26.json", True, "hebrew"),
    ("moreh-bab27", "moreh-bab27.json", True, "hebrew"),
    ("moreh-bab28", "moreh-bab28.json", True, "hebrew"),
    ("kuzari-maqala1", "kuzari-maqala1.json", True, "hebrew"),
    ("saadia-emunot-intro", "saadia-emunot-intro.json", True, "hebrew"),
    ("qirqisani-anwar", "qirqisani-anwar-maqala1.json", True, "arabic"),
    ("bahya-bab1", "bahya-bab1.json", True, "hebrew"),
    ("bahya-hakdamah", "bahya-hakdamah.json", True, "hebrew"),
    ("bahya-bab2", "bahya-bab2.json", True, "hebrew"),
    ("bahya-bab3", "bahya-bab3.json", True, "hebrew"),
    ("bahya-bab4", "bahya-bab4.json", True, "hebrew"),
    ("bahya-bab5", "bahya-bab5.json", True, "hebrew"),
    ("bahya-bab6", "bahya-bab6.json", True, "hebrew"),
    ("bahya-bab7", "bahya-bab7.json", True, "hebrew"),
    ("bahya-bab8", "bahya-bab8.json", True, "hebrew"),
    ("bahya-bab9", "bahya-bab9.json", True, "hebrew"),
    ("bahya-bab10", "bahya-bab10.json", True, "hebrew"),
]

# Arabic→Judaeo-Arabic converter (same map the runtime lib/arabicToJa.ts ports).
_lex = Path.home() / "Tools" / "arabic-lexicon"
sys.path.insert(0, str(_lex))
import ja_script  # noqa: E402


def gather_ja_strings(obj, out: list[str]) -> None:
    """Collect Judeo-Arabic source strings from an Advanced-text JSON.

    Two carriers exist: free-flow `pages[].paragraphs[]` (list of strings, used
    by Bahya) and aligned `pages[].aligned[].ja` / generic `ja`/`text` fields
    (used by Moreh, Kuzari, Saadia Emunot). Walk both.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "paragraphs" and isinstance(v, list):
                out.extend(s for s in v if isinstance(s, str))
            elif k in ("ja", "text") and isinstance(v, str):
                out.append(v)
            else:
                gather_ja_strings(v, out)
    elif isinstance(obj, list):
        for x in obj:
            gather_ja_strings(x, out)


def lookup_bucket_hand(raw: str, starter: set[str], lane: set[str]) -> str:
    """Return 'hand-starter' | 'hand-lane' | 'miss' (no auto tier)."""
    if not strip_punct(raw):
        return "miss"
    chain = candidate_chain(raw)
    for c in chain:
        if c in starter:
            return "hand-starter"
    for c in chain:
        if c in lane:
            return "hand-lane"
    return "miss"


def pct(n: int, d: int) -> float:
    return round(100 * n / d, 2) if d else 0.0


def main() -> int:
    starter_keys, starter_n = load_dict_index(DATA / "dictionary-starter.json")
    lane_keys, lane_n = load_dict_index(DATA / "dictionary-lane.json")
    sys.stderr.write(
        f"loaded dicts: starter={starter_n} ({len(starter_keys)} keys), "
        f"lane={lane_n} ({len(lane_keys)} keys)\n"
    )

    per_text: dict[str, dict] = {}
    failing: list[str] = []

    for label, fname, in_scope, script in TEXTS:
        path = DATA / fname
        if not path.exists():
            sys.stderr.write(f"  skip {label}: {fname} missing\n")
            continue
        strings: list[str] = []
        gather_ja_strings(json.loads(path.read_text()), strings)

        counts = Counter()
        miss_counter: Counter = Counter()
        for chunk in chunked(strings, 64):
            for words in tokenise_via_cli(chunk):
                for w in words:
                    # Arabic-script work: convert the token to JA first (the
                    # reader's lib/arabicToJa path). Key misses on the JA form.
                    jw = ja_script.ar_to_ja(w) if script == "arabic" else w
                    # Drop Hebrew points so vocalized embedded quotes match
                    # their unvocalized lemmas (mirrors lib/lookup candidateForms).
                    jw = re.sub(r"[֑-ׇ]", "", jw)
                    tok = strip_punct(jw)
                    if not tok:
                        continue
                    bucket = lookup_bucket_hand(jw, starter_keys, lane_keys)
                    counts[bucket] += 1
                    if bucket == "miss":
                        miss_counter[tok] += 1

        n = sum(counts.values())
        hand = counts["hand-starter"] + counts["hand-lane"]
        covered_pct = pct(hand, n)
        per_text[label] = {
            "in_scope": in_scope,
            "tokens": n,
            "hand_starter": counts["hand-starter"],
            "hand_lane": counts["hand-lane"],
            "hand_total": hand,
            "miss": counts["miss"],
            "covered_pct": covered_pct,
            "miss_pct": pct(counts["miss"], n),
            "unique_misses": len(miss_counter),
            "misses": [
                {"surface": t, "count": c, "bucket": miss_bucket(t)}
                for t, c in miss_counter.most_common()
            ],
        }
        if in_scope and counts["miss"] > 0:
            failing.append(label)

    snapshot = {
        "_generated": "scripts/coverage_advanced.py",
        "by_text": per_text,
    }
    out_path = DATA / "coverage-advanced.json"
    out_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2))

    # Summary.
    print("\nAdvanced-reader dictionary coverage")
    print("===================================")
    for label, fname, in_scope, script in TEXTS:
        if label not in per_text:
            continue
        d = per_text[label]
        flag = "GATED" if in_scope else "report"
        print(
            f"  {label:22} covered={d['covered_pct']:5.1f}%  "
            f"miss={d['miss']:>4} ({d['unique_misses']} uniq)  "
            f"tokens={d['tokens']:>5}  [{flag}]"
        )
    print(f"\nWrote {out_path}")

    if failing:
        print(
            f"\nGATE FAILED — in-scope text(s) below 100%: {', '.join(failing)}",
            file=sys.stderr,
        )
        for label in failing:
            top = per_text[label]["misses"][:20]
            print(f"\n  top misses for {label}:", file=sys.stderr)
            for m in top:
                print(f"    {m['count']:>3}  {m['surface']}  [{m['bucket']}]", file=sys.stderr)
        return 1

    print("\nGATE PASSED — all in-scope texts at 100% coverage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

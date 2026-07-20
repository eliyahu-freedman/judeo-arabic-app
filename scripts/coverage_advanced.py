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
    ("moreh-bab29", "moreh-bab29.json", True, "hebrew"),
    ("moreh-bab30", "moreh-bab30.json", True, "hebrew"),
    ("moreh-bab31", "moreh-bab31.json", True, "hebrew"),
    ("moreh-bab32", "moreh-bab32.json", True, "hebrew"),
    ("moreh-bab33", "moreh-bab33.json", True, "hebrew"),
    ("moreh-bab34", "moreh-bab34.json", True, "hebrew"),
    ("moreh-bab35", "moreh-bab35.json", True, "hebrew"),
    ("moreh-bab36", "moreh-bab36.json", True, "hebrew"),
    ("moreh-bab37", "moreh-bab37.json", True, "hebrew"),
    ("moreh-bab38", "moreh-bab38.json", True, "hebrew"),
    ("moreh-bab39", "moreh-bab39.json", True, "hebrew"),
    ("moreh-bab40", "moreh-bab40.json", True, "hebrew"),
    ("moreh-bab41", "moreh-bab41.json", True, "hebrew"),
    ("moreh-bab42", "moreh-bab42.json", True, "hebrew"),
    ("moreh-bab43", "moreh-bab43.json", True, "hebrew"),
    ("moreh-bab44", "moreh-bab44.json", True, "hebrew"),
    ("moreh-bab45", "moreh-bab45.json", True, "hebrew"),
    ("moreh-bab46", "moreh-bab46.json", True, "hebrew"),
    ("moreh-bab47", "moreh-bab47.json", True, "hebrew"),
    ("moreh-bab48", "moreh-bab48.json", True, "hebrew"),
    ("moreh-bab49", "moreh-bab49.json", True, "hebrew"),
    ("moreh-bab50", "moreh-bab50.json", True, "hebrew"),
    ("moreh-bab51", "moreh-bab51.json", True, "hebrew"),
    ("moreh-bab52", "moreh-bab52.json", True, "hebrew"),
    ("moreh-bab53", "moreh-bab53.json", True, "hebrew"),
    ("moreh-bab54", "moreh-bab54.json", True, "hebrew"),
    ("moreh-bab55", "moreh-bab55.json", True, "hebrew"),
    ("moreh-bab56", "moreh-bab56.json", True, "hebrew"),
    ("moreh-bab57", "moreh-bab57.json", True, "hebrew"),
    ("moreh-bab58", "moreh-bab58.json", True, "hebrew"),
    ("moreh-bab59", "moreh-bab59.json", True, "hebrew"),
    ("moreh-bab60", "moreh-bab60.json", True, "hebrew"),
    ("moreh-bab61", "moreh-bab61.json", True, "hebrew"),
    ("moreh-bab62", "moreh-bab62.json", True, "hebrew"),
    ("moreh-bab63", "moreh-bab63.json", True, "hebrew"),
    ("moreh-bab64", "moreh-bab64.json", True, "hebrew"),
    ("moreh-bab65", "moreh-bab65.json", True, "hebrew"),
    ("moreh-bab66", "moreh-bab66.json", True, "hebrew"),
    ("moreh-bab67", "moreh-bab67.json", True, "hebrew"),
    ("moreh-bab68", "moreh-bab68.json", True, "hebrew"),
    ("moreh-bab69", "moreh-bab69.json", True, "hebrew"),
    ("moreh-bab70", "moreh-bab70.json", True, "hebrew"),
    ("moreh-bab71", "moreh-bab71.json", True, "hebrew"),
    ("moreh-bab72", "moreh-bab72.json", True, "hebrew"),
    ("moreh-bab73", "moreh-bab73.json", True, "hebrew"),
    ("moreh-bab74", "moreh-bab74.json", True, "hebrew"),
    ("moreh-bab75", "moreh-bab75.json", True, "hebrew"),
    ("moreh-bab76", "moreh-bab76.json", True, "hebrew"),
    ("moreh-p2-bab1", "moreh-p2-bab1.json", True, "hebrew"),
    ("moreh-p2-bab2", "moreh-p2-bab2.json", True, "hebrew"),
    ("moreh-p2-bab3", "moreh-p2-bab3.json", True, "hebrew"),
    ("moreh-p2-bab4", "moreh-p2-bab4.json", True, "hebrew"),
    ("moreh-p2-bab5", "moreh-p2-bab5.json", True, "hebrew"),
    ("moreh-p2-bab6", "moreh-p2-bab6.json", True, "hebrew"),
    ("moreh-p2-bab7", "moreh-p2-bab7.json", True, "hebrew"),
    ("moreh-p2-bab8", "moreh-p2-bab8.json", True, "hebrew"),
    ("moreh-p2-bab9", "moreh-p2-bab9.json", True, "hebrew"),
    ("moreh-p2-bab10", "moreh-p2-bab10.json", True, "hebrew"),
    ("moreh-p2-bab11", "moreh-p2-bab11.json", True, "hebrew"),
    ("moreh-p2-bab12", "moreh-p2-bab12.json", True, "hebrew"),
    ("moreh-p2-bab13", "moreh-p2-bab13.json", True, "hebrew"),
    ("moreh-p2-bab14", "moreh-p2-bab14.json", True, "hebrew"),
    ("moreh-p2-bab15", "moreh-p2-bab15.json", True, "hebrew"),
    ("moreh-p2-bab16", "moreh-p2-bab16.json", True, "hebrew"),
    ("moreh-p2-bab17", "moreh-p2-bab17.json", True, "hebrew"),
    ("moreh-p2-bab18", "moreh-p2-bab18.json", True, "hebrew"),
    ("moreh-p2-bab19", "moreh-p2-bab19.json", True, "hebrew"),
    ("moreh-p2-bab20", "moreh-p2-bab20.json", True, "hebrew"),
    ("moreh-p2-bab21", "moreh-p2-bab21.json", True, "hebrew"),
    ("moreh-p2-bab22", "moreh-p2-bab22.json", True, "hebrew"),
    ("moreh-p2-bab23", "moreh-p2-bab23.json", True, "hebrew"),
    ("moreh-p2-bab24", "moreh-p2-bab24.json", True, "hebrew"),
    ("moreh-p2-bab25", "moreh-p2-bab25.json", True, "hebrew"),
    ("moreh-p2-bab26", "moreh-p2-bab26.json", True, "hebrew"),
    ("moreh-p2-bab27", "moreh-p2-bab27.json", True, "hebrew"),
    ("moreh-p2-bab28", "moreh-p2-bab28.json", True, "hebrew"),
    ("moreh-p2-bab29", "moreh-p2-bab29.json", True, "hebrew"),
    ("moreh-p2-bab30", "moreh-p2-bab30.json", True, "hebrew"),
    ("moreh-p2-bab31", "moreh-p2-bab31.json", True, "hebrew"),
    ("moreh-p2-bab32", "moreh-p2-bab32.json", True, "hebrew"),
    ("moreh-p2-bab33", "moreh-p2-bab33.json", True, "hebrew"),
    ("moreh-p2-bab34", "moreh-p2-bab34.json", True, "hebrew"),
    ("moreh-p2-bab35", "moreh-p2-bab35.json", True, "hebrew"),
    ("moreh-p2-bab36", "moreh-p2-bab36.json", True, "hebrew"),
    ("moreh-p2-bab37", "moreh-p2-bab37.json", True, "hebrew"),
    ("moreh-p2-bab38", "moreh-p2-bab38.json", True, "hebrew"),
    ("moreh-p2-bab39", "moreh-p2-bab39.json", True, "hebrew"),
    ("moreh-p2-bab40", "moreh-p2-bab40.json", True, "hebrew"),
    ("moreh-p2-bab41", "moreh-p2-bab41.json", True, "hebrew"),
    ("moreh-p2-bab42", "moreh-p2-bab42.json", True, "hebrew"),
    ("moreh-p2-bab43", "moreh-p2-bab43.json", True, "hebrew"),
    ("moreh-p2-bab44", "moreh-p2-bab44.json", True, "hebrew"),
    ("moreh-p2-bab45", "moreh-p2-bab45.json", True, "hebrew"),
    ("moreh-p2-bab46", "moreh-p2-bab46.json", True, "hebrew"),
    ("moreh-p2-bab47", "moreh-p2-bab47.json", True, "hebrew"),
    ("moreh-p2-bab48", "moreh-p2-bab48.json", True, "hebrew"),
    ("moreh-p3-bab1", "moreh-p3-bab1.json", True, "hebrew"),
    ("moreh-p3-bab2", "moreh-p3-bab2.json", True, "hebrew"),
    ("moreh-p3-bab3", "moreh-p3-bab3.json", True, "hebrew"),
    ("moreh-p3-bab4", "moreh-p3-bab4.json", True, "hebrew"),
    ("moreh-p3-bab5", "moreh-p3-bab5.json", True, "hebrew"),
    ("moreh-p3-bab6", "moreh-p3-bab6.json", True, "hebrew"),
    ("moreh-p3-bab7", "moreh-p3-bab7.json", True, "hebrew"),
    ("moreh-p3-bab8", "moreh-p3-bab8.json", True, "hebrew"),
    ("moreh-p3-bab9", "moreh-p3-bab9.json", True, "hebrew"),
    ("moreh-p3-bab10", "moreh-p3-bab10.json", True, "hebrew"),
    ("moreh-p3-bab11", "moreh-p3-bab11.json", True, "hebrew"),
    ("moreh-p3-bab12", "moreh-p3-bab12.json", True, "hebrew"),
    ("moreh-p3-bab13", "moreh-p3-bab13.json", True, "hebrew"),
    ("moreh-p3-bab14", "moreh-p3-bab14.json", True, "hebrew"),
    ("moreh-p3-bab15", "moreh-p3-bab15.json", True, "hebrew"),
    ("moreh-p3-bab16", "moreh-p3-bab16.json", True, "hebrew"),
    ("moreh-p3-bab17", "moreh-p3-bab17.json", True, "hebrew"),
    ("moreh-p3-bab18", "moreh-p3-bab18.json", True, "hebrew"),
    ("moreh-p3-bab19", "moreh-p3-bab19.json", True, "hebrew"),
    ("moreh-p3-bab20", "moreh-p3-bab20.json", True, "hebrew"),
    ("moreh-p3-bab21", "moreh-p3-bab21.json", True, "hebrew"),
    ("moreh-p3-bab22", "moreh-p3-bab22.json", True, "hebrew"),
    ("moreh-p3-bab23", "moreh-p3-bab23.json", True, "hebrew"),
    ("moreh-p3-bab24", "moreh-p3-bab24.json", True, "hebrew"),
    ("moreh-p3-bab25", "moreh-p3-bab25.json", True, "hebrew"),
    ("moreh-p3-bab26", "moreh-p3-bab26.json", True, "hebrew"),
    ("moreh-p3-bab27", "moreh-p3-bab27.json", True, "hebrew"),
    ("moreh-p3-bab28", "moreh-p3-bab28.json", True, "hebrew"),
    ("moreh-p3-bab29", "moreh-p3-bab29.json", True, "hebrew"),
    ("moreh-p3-bab30", "moreh-p3-bab30.json", True, "hebrew"),
    ("moreh-p3-bab31", "moreh-p3-bab31.json", True, "hebrew"),
    ("moreh-p3-bab32", "moreh-p3-bab32.json", True, "hebrew"),
    ("moreh-p3-bab33", "moreh-p3-bab33.json", True, "hebrew"),
    ("moreh-p3-bab34", "moreh-p3-bab34.json", True, "hebrew"),
    ("moreh-p3-bab35", "moreh-p3-bab35.json", True, "hebrew"),
    ("moreh-p3-bab36", "moreh-p3-bab36.json", True, "hebrew"),
    ("moreh-p3-bab37", "moreh-p3-bab37.json", True, "hebrew"),
    ("moreh-p3-bab38", "moreh-p3-bab38.json", True, "hebrew"),
    ("moreh-p3-bab39", "moreh-p3-bab39.json", True, "hebrew"),
    ("moreh-p3-bab40", "moreh-p3-bab40.json", True, "hebrew"),
    ("moreh-p3-bab41", "moreh-p3-bab41.json", True, "hebrew"),
    ("moreh-p3-bab42", "moreh-p3-bab42.json", True, "hebrew"),
    ("moreh-p3-bab43", "moreh-p3-bab43.json", True, "hebrew"),
    ("moreh-p3-bab44", "moreh-p3-bab44.json", True, "hebrew"),
    ("moreh-p3-bab45", "moreh-p3-bab45.json", True, "hebrew"),
    ("moreh-p3-bab46", "moreh-p3-bab46.json", True, "hebrew"),
    ("moreh-p3-bab47", "moreh-p3-bab47.json", True, "hebrew"),
    ("moreh-p3-bab48", "moreh-p3-bab48.json", True, "hebrew"),
    ("moreh-p3-bab49", "moreh-p3-bab49.json", True, "hebrew"),
    ("moreh-p3-bab50", "moreh-p3-bab50.json", True, "hebrew"),
    ("moreh-p3-bab51", "moreh-p3-bab51.json", True, "hebrew"),
    ("moreh-p3-bab52", "moreh-p3-bab52.json", True, "hebrew"),
    ("moreh-p3-bab53", "moreh-p3-bab53.json", True, "hebrew"),
    ("moreh-p3-bab54", "moreh-p3-bab54.json", True, "hebrew"),
    ("kuzari-maqala-1", "kuzari-maqala-1.json", True, "hebrew"),
    ("kuzari-maqala-2", "kuzari-maqala-2.json", True, "hebrew"),
    ("kuzari-maqala-3", "kuzari-maqala-3.json", True, "hebrew"),
    ("kuzari-maqala-4", "kuzari-maqala-4.json", True, "hebrew"),
    ("kuzari-maqala-5", "kuzari-maqala-5.json", True, "hebrew"),
    ("saadia-emunot-intro", "saadia-emunot-intro.json", True, "hebrew"),
    # Maqala I – Bab 1 (hand-authored legacy JSON with inline aligned + terms)
    ("qirqisani-m1-bab-1", "qirqisani-anwar-maqala1.json", True, "arabic"),
    # Maqala I – Babs 2-19 (Cairo 2019 Arabic edition)
    ("qirqisani-m1-bab-2", "qirqisani-m1-bab02.json", False, "arabic"),
    ("qirqisani-m1-bab-3", "qirqisani-m1-bab03.json", False, "arabic"),
    ("qirqisani-m1-bab-4", "qirqisani-m1-bab04.json", False, "arabic"),
    ("qirqisani-m1-bab-5", "qirqisani-m1-bab05.json", False, "arabic"),
    ("qirqisani-m1-bab-6", "qirqisani-m1-bab06.json", False, "arabic"),
    ("qirqisani-m1-bab-7", "qirqisani-m1-bab07.json", False, "arabic"),
    ("qirqisani-m1-bab-8", "qirqisani-m1-bab08.json", False, "arabic"),
    ("qirqisani-m1-bab-9", "qirqisani-m1-bab09.json", False, "arabic"),
    ("qirqisani-m1-bab-10", "qirqisani-m1-bab10.json", False, "arabic"),
    ("qirqisani-m1-bab-11", "qirqisani-m1-bab11.json", False, "arabic"),
    ("qirqisani-m1-bab-12", "qirqisani-m1-bab12.json", False, "arabic"),
    ("qirqisani-m1-bab-13", "qirqisani-m1-bab13.json", False, "arabic"),
    ("qirqisani-m1-bab-14", "qirqisani-m1-bab14.json", False, "arabic"),
    ("qirqisani-m1-bab-15", "qirqisani-m1-bab15.json", False, "arabic"),
    ("qirqisani-m1-bab-16", "qirqisani-m1-bab16.json", False, "arabic"),
    ("qirqisani-m1-bab-17", "qirqisani-m1-bab17.json", False, "arabic"),
    ("qirqisani-m1-bab-18", "qirqisani-m1-bab18.json", False, "arabic"),
    ("qirqisani-m1-bab-19", "qirqisani-m1-bab19.json", False, "arabic"),
    # Maqala V – Sha'arim 1-40 (Nemoy trilingual source)
    ("qirqisani-m5-sha-1", "qirqisani-m5-sha01.json", False, "arabic"),
    ("qirqisani-m5-sha-2", "qirqisani-m5-sha02.json", False, "arabic"),
    ("qirqisani-m5-sha-3", "qirqisani-m5-sha03.json", False, "arabic"),
    ("qirqisani-m5-sha-4", "qirqisani-m5-sha04.json", False, "arabic"),
    ("qirqisani-m5-sha-5", "qirqisani-m5-sha05.json", False, "arabic"),
    ("qirqisani-m5-sha-6", "qirqisani-m5-sha06.json", False, "arabic"),
    ("qirqisani-m5-sha-7", "qirqisani-m5-sha07.json", False, "arabic"),
    ("qirqisani-m5-sha-8", "qirqisani-m5-sha08.json", False, "arabic"),
    ("qirqisani-m5-sha-9", "qirqisani-m5-sha09.json", False, "arabic"),
    ("qirqisani-m5-sha-10", "qirqisani-m5-sha10.json", False, "arabic"),
    ("qirqisani-m5-sha-11", "qirqisani-m5-sha11.json", False, "arabic"),
    ("qirqisani-m5-sha-12", "qirqisani-m5-sha12.json", False, "arabic"),
    ("qirqisani-m5-sha-13", "qirqisani-m5-sha13.json", False, "arabic"),
    ("qirqisani-m5-sha-14", "qirqisani-m5-sha14.json", False, "arabic"),
    ("qirqisani-m5-sha-15", "qirqisani-m5-sha15.json", False, "arabic"),
    ("qirqisani-m5-sha-16", "qirqisani-m5-sha16.json", False, "arabic"),
    ("qirqisani-m5-sha-17", "qirqisani-m5-sha17.json", False, "arabic"),
    ("qirqisani-m5-sha-18", "qirqisani-m5-sha18.json", False, "arabic"),
    ("qirqisani-m5-sha-19", "qirqisani-m5-sha19.json", False, "arabic"),
    ("qirqisani-m5-sha-20", "qirqisani-m5-sha20.json", False, "arabic"),
    ("qirqisani-m5-sha-21", "qirqisani-m5-sha21.json", False, "arabic"),
    ("qirqisani-m5-sha-22", "qirqisani-m5-sha22.json", False, "arabic"),
    ("qirqisani-m5-sha-23", "qirqisani-m5-sha23.json", False, "arabic"),
    ("qirqisani-m5-sha-24", "qirqisani-m5-sha24.json", False, "arabic"),
    ("qirqisani-m5-sha-25", "qirqisani-m5-sha25.json", False, "arabic"),
    ("qirqisani-m5-sha-26", "qirqisani-m5-sha26.json", False, "arabic"),
    ("qirqisani-m5-sha-27", "qirqisani-m5-sha27.json", False, "arabic"),
    ("qirqisani-m5-sha-28", "qirqisani-m5-sha28.json", False, "arabic"),
    ("qirqisani-m5-sha-29", "qirqisani-m5-sha29.json", False, "arabic"),
    ("qirqisani-m5-sha-30", "qirqisani-m5-sha30.json", False, "arabic"),
    ("qirqisani-m5-sha-31", "qirqisani-m5-sha31.json", False, "arabic"),
    ("qirqisani-m5-sha-32", "qirqisani-m5-sha32.json", False, "arabic"),
    ("qirqisani-m5-sha-33", "qirqisani-m5-sha33.json", False, "arabic"),
    ("qirqisani-m5-sha-34", "qirqisani-m5-sha34.json", False, "arabic"),
    ("qirqisani-m5-sha-35", "qirqisani-m5-sha35.json", False, "arabic"),
    ("qirqisani-m5-sha-36", "qirqisani-m5-sha36.json", False, "arabic"),
    ("qirqisani-m5-sha-37", "qirqisani-m5-sha37.json", False, "arabic"),
    ("qirqisani-m5-sha-38", "qirqisani-m5-sha38.json", False, "arabic"),
    ("qirqisani-m5-sha-39", "qirqisani-m5-sha39.json", False, "arabic"),
    ("qirqisani-m5-sha-40", "qirqisani-m5-sha40.json", False, "arabic"),
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

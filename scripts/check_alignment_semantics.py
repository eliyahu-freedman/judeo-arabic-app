"""Print the runtime-accurate JA→HE/EN word mapping for a tafsir chapter.

Re-implements the resolver in lib/alignment.ts (independent per-side
occurrence claiming with a forward-preferring cursor and backward fallback)
so you can eyeball that every JA word lights up the correct Hebrew word and
English phrase — the handalign validator only checks findability, not which
occurrence each pair actually lands on. Read-only.

Usage:
    python3 scripts/check_alignment_semantics.py --book vayikra --chapter 18
    python3 scripts/check_alignment_semantics.py --book vayikra --chapter 18 --verse 7
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


class Side:
    """Mirror of `claim` in lib/alignment.ts."""

    def __init__(self) -> None:
        self.claimed: list[tuple[int, int]] = []
        self.cursor = 0

    def _free(self, i: int, e: int) -> bool:
        return not any(i < c1 and e > c0 for c0, c1 in self.claimed)

    def claim(self, text: str, needle: str) -> int:
        n = len(needle)
        frm = self.cursor
        while True:
            i = text.find(needle, frm)
            if i == -1:
                break
            if self._free(i, i + n):
                self.claimed.append((i, i + n))
                self.cursor = i + n
                return i
            frm = i + 1
        frm = 0
        while True:
            i = text.find(needle, frm)
            if i == -1:
                return -1
            if self._free(i, i + n):
                self.claimed.append((i, i + n))
                return i
            frm = i + 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--verse", type=int, default=0, help="0 = all verses")
    args = ap.parse_args()

    al = json.loads(
        (DATA / f"tafsir-{args.book}-{args.chapter}-alignment.json").read_text(
            encoding="utf-8",
        ),
    )["alignments"]
    src = {
        v["v"]: v
        for v in json.loads(
            (DATA / f"tafsir-{args.book}-{args.chapter}.json").read_text(
                encoding="utf-8",
            ),
        )["verses"]
    }
    en = json.loads(
        (DATA / f"tafsir-{args.book}-{args.chapter}-english.json").read_text(
            encoding="utf-8",
        ),
    )["translations"]

    misses = 0
    for vs in sorted(al, key=int):
        vn = int(vs)
        if args.verse and vn != args.verse:
            continue
        if vn not in src:
            print(f"v{vs}: not in source")
            continue
        he_f, ja_f, en_f = src[vn]["hebrew"], src[vn]["ja"], en.get(vs, "")
        hs, js, es = Side(), Side(), Side()
        print(f"==== v{vs} ====")
        for p in al[vs]:
            ji = js.claim(ja_f, p["ja"])
            ei = es.claim(en_f, p["en"])
            ht = "—"
            if p.get("he"):
                hi = hs.claim(he_f, p["he"])
                if hi < 0:
                    ht, misses = "!!MISS", misses + 1
                else:
                    ht = he_f[hi : hi + len(p["he"])]
            jt = ja_f[ji : ji + len(p["ja"])] if ji >= 0 else "!!MISS-JA"
            et = en_f[ei : ei + len(p["en"])] if ei >= 0 else "!!MISS-EN"
            print(f"  JA[{jt}]  HE[{ht}]  EN[{et}]")
    if misses:
        print(f"\n{misses} HE miss(es)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

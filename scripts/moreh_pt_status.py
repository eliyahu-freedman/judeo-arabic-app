#!/usr/bin/env python3
"""Report Portuguese-translation coverage of the Moreh Nevukhim corpus.

The driverless Portuguese pass (see MOREH-PORTUGUESE-GHOST.md) calls this to
decide what to do next. It walks every Moreh chapter on disk, checks for a
matching `-portuguese.json` sidecar, and verifies the sidecar actually covers
every aligned segment / paragraph the source page carries (a partial sidecar
counts as incomplete, so a crashed run gets picked back up and finished).

Chapters are ordered Part I → II → III, ascending, so `--next` always returns
the earliest unfinished chapter — deterministic, resumable, no bookkeeping file.

Usage:
    python3 scripts/moreh_pt_status.py            # summary table
    python3 scripts/moreh_pt_status.py --next     # base name of next TODO chapter (e.g. moreh-bab2)
    python3 scripts/moreh_pt_status.py --next-json # {"base","source","part","chapter","missing_pages"}
    python3 scripts/moreh_pt_status.py --json      # full machine-readable status
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def chapter_files() -> list[tuple[int, int, Path]]:
    """All Moreh source chapters as (part, chapter_num, path), Part I→II→III asc."""
    out: list[tuple[int, int, Path]] = []
    for p in DATA.glob("moreh-bab*.json"):
        m = re.fullmatch(r"moreh-bab(\d+)\.json", p.name)
        if m:
            out.append((1, int(m.group(1)), p))
    for part, pat in ((2, "moreh-p2-bab*.json"), (3, "moreh-p3-bab*.json")):
        for p in DATA.glob(pat):
            m = re.fullmatch(rf"moreh-p{part}-bab(\d+)\.json", p.name)
            if m:
                out.append((part, int(m.group(1)), p))
    out.sort(key=lambda t: (t[0], t[1]))
    return out


def sidecar_path(source: Path) -> Path:
    return source.with_name(source.stem + "-portuguese.json")


def coverage(source: Path) -> dict:
    """Return coverage info for one chapter: total units, translated, missing pages."""
    data = json.loads(source.read_text(encoding="utf-8"))
    pages = data.get("pages", [])
    side = sidecar_path(source)
    pt = {}
    if side.exists():
        try:
            pt = json.loads(side.read_text(encoding="utf-8")).get("pages", {})
        except json.JSONDecodeError:
            pt = {"__corrupt__": True}
    total = done = 0
    missing_pages: list[str] = []
    corrupt = pt.get("__corrupt__") is True
    for page in pages:
        ph = str(page.get("page_he"))
        aligned = page.get("aligned", []) or []
        paras = page.get("paragraphs", []) or []
        units = [s for s in aligned] if aligned else list(paras)
        n = len(units)
        total += n
        if corrupt:
            missing_pages.append(ph)
            continue
        ppt = pt.get(ph, {}) if isinstance(pt, dict) else {}
        pt_arr = (ppt.get("aligned") if aligned else ppt.get("paragraphs")) or []
        page_done = 0
        for i in range(n):
            val = pt_arr[i] if i < len(pt_arr) else None
            if isinstance(val, str) and val.strip():
                page_done += 1
        done += page_done
        if page_done < n:
            missing_pages.append(ph)
    return {
        "exists": side.exists(),
        "corrupt": corrupt,
        "total": total,
        "done": done,
        "complete": (total > 0 and done == total and not corrupt),
        "missing_pages": missing_pages,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", action="store_true", help="print base name of next TODO chapter")
    ap.add_argument("--next-json", action="store_true", help="print JSON descriptor of next TODO chapter")
    ap.add_argument("--json", action="store_true", help="print full status as JSON")
    args = ap.parse_args()

    files = chapter_files()
    rows = []
    next_todo = None
    for part, ch, path in files:
        cov = coverage(path)
        base = path.stem
        row = {"base": base, "source": path.name, "part": part, "chapter": ch, **cov}
        rows.append(row)
        if next_todo is None and not cov["complete"]:
            next_todo = row

    if args.next:
        print(next_todo["base"] if next_todo else "")
        return 0
    if args.next_json:
        print(json.dumps(next_todo or {}, ensure_ascii=False))
        return 0
    if args.json:
        print(json.dumps({"chapters": rows}, ensure_ascii=False, indent=2))
        return 0

    complete = sum(1 for r in rows if r["complete"])
    started = sum(1 for r in rows if r["exists"] and not r["complete"])
    seg_total = sum(r["total"] for r in rows)
    seg_done = sum(r["done"] for r in rows)
    print(f"Moreh Nevukhim — Portuguese coverage")
    print(f"  chapters : {complete}/{len(rows)} complete  ({started} partially started)")
    print(f"  segments : {seg_done}/{seg_total} translated  ({100*seg_done/seg_total:.1f}%)" if seg_total else "  segments : 0")
    if next_todo:
        print(f"  next TODO: {next_todo['base']}  (Part {next_todo['part']}, ch {next_todo['chapter']}, "
              f"{next_todo['done']}/{next_todo['total']} done)")
    else:
        print("  next TODO: — all chapters complete 🎉")
    return 0


if __name__ == "__main__":
    sys.exit(main())

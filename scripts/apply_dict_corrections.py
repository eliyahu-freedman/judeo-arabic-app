#!/usr/bin/env python3
"""Apply semantic-QC corrections to the shared tap-to-define dictionary.

Usage: apply_dict_corrections.py <verdicts.json> [--dry-run]

<verdicts.json> is a list (or {"verdicts":[...]}) of judge verdicts, each:
  {surface, entry_id, verdict, confidence,
   target_lemma_ja, target_lemma_ar, target_root,
   corrected_pos, corrected_gloss_en, corrected_gloss_he, evidence, note}

Only HIGH-confidence verdicts in {wrong_attribution, wrong_pos_or_sense,
hebrew_quote} are auto-applied. `homograph_ambiguous` and MEDIUM/LOW go to
REVISION_SHEET.md for manual accept/reject (no global "best sense" is safe).

Operations (classified per verdict):
  MOVE   — surface belongs to a DIFFERENT lemma (wrong_attribution, or a
           wrong_pos_or_sense whose target_lemma_ja != the shown lemma):
           detach the matched form(s) from the shown entry's variants and
           attach them to the correct entry (found by lemma, or created).
  EDIT   — same lemma, wrong pos/gloss: patch the shown entry's fields.
  RETAG  — embedded Hebrew: detach from the Arabic entry, attach to a
           Hebrew-quote entry (created if absent).

Invariant: every surface detached must land in some entry (lemma or variant),
so coverage never regresses. A post-pass asserts this and reports violations.

The dictionary (data/dictionary-lane.json + -starter.json) is shared by ALL
Advanced texts + the Tafsir reader, so every fix is global.
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from coverage_report import normalize_finals, candidate_chain  # noqa: E402

DATA = os.path.join(ROOT, "data")
LANE = os.path.join(DATA, "dictionary-lane.json")
STARTER = os.path.join(DATA, "dictionary-starter.json")
LEDGER = os.path.join(DATA, "_dict_audit", "judged_ledger.json")
SHEET = os.path.join(ROOT, "REVISION_SHEET.md")

APPLY_VERDICTS = {"wrong_attribution", "wrong_pos_or_sense", "hebrew_quote"}


def nf(s: str) -> str:
    return normalize_finals(s or "")


def cand_norms(surface: str) -> set[str]:
    return {nf(c) for c in candidate_chain(surface)} | {nf(surface)}


def main():
    args = sys.argv[1:]
    dry = "--dry-run" in args
    accept_all = "--accept-all" in args  # apply ALL flagged verdicts (any conf),
    # routing form-homographs to in-place EDIT (user has reviewed REVISION_SHEET).
    args = [a for a in args if a not in ("--dry-run", "--accept-all")]
    if not args:
        sys.exit("usage: apply_dict_corrections.py <verdicts.json> [--dry-run] [--accept-all]")

    raw = json.load(open(args[0]))
    verdicts = raw["verdicts"] if isinstance(raw, dict) else raw

    lane = json.load(open(LANE))
    starter = json.load(open(STARTER))
    # entry id -> (entry, container_list)
    index = {}
    lemma_index = {}  # nf(lemma) -> list[entry]
    for store in (lane, starter):
        for e in store["entries"]:
            index[e["id"]] = (e, store["entries"])
            lemma_index.setdefault(nf(e["lemma_ja"]), []).append(e)

    def find_target(target_lemma_ja):
        for e in lemma_index.get(nf(target_lemma_ja), []):
            return e
        return None

    applied, deferred, problems = [], [], []
    touched_surfaces = set()
    created = []

    def defer(v, why):
        v = dict(v)
        v["_defer_reason"] = why
        deferred.append(v)

    def poscat(p):
        p = (p or "").lower()
        # function words (particle/prep/conjunction/pronoun) collapse to one
        # category so we reuse an existing entry instead of cloning it.
        for kw in ("particle", "prepos", "conjunct", "pronoun"):
            if kw in p:
                return "function"
        for cat in ("verb", "noun", "adject", "adverb", "numeral", "proper"):
            if cat in p:
                return cat
        return p.strip()

    _STOP = {"the", "and", "one", "his", "her", "its", "for", "with", "that",
             "this", "who", "from", "are", "was", "has", "you", "not", "any"}

    def words(s):
        import re as _re
        return {w for w in _re.findall(r"[a-z']+", (s or "").lower())
                if len(w) > 2 and w not in _STOP}

    def find_sense(target_lemma_ja, root, pos, gloss_en):
        """Reuse an existing entry ONLY if it is unambiguously the SAME sense as
        the correction: same lemma AND same pos-category AND the glosses share a
        content word. Otherwise return None → create a fresh entry, so we never
        re-attach a surface to a same-lemma homograph (e.g. שער hair vs perceive;
        עאלם world vs scholar)."""
        for e in lemma_index.get(nf(target_lemma_ja), []):
            if poscat(e.get("pos")) != poscat(pos):
                continue
            if gloss_en and not (words(e.get("gloss_en")) & words(gloss_en)):
                continue
            return e
        return None

    def make_entry(eid, lemma, lemma_ar, root, pos, ge, gh, note):
        e = {"id": eid, "lemma_ja": lemma, "lemma_ar": lemma_ar, "root": root or "—",
             "pos": pos, "gloss_en": ge, "gloss_he": gh, "notes": note,
             "source": "lane", "variants": []}
        lane["entries"].append(e)
        index[eid] = (e, lane["entries"])
        lemma_index.setdefault(nf(lemma), []).append(e)
        created.append(eid)
        return e

    edited_ids = {}  # entry id -> set of gloss_en already merged (avoid dup-append)

    def edit_in_place(entry, v, hebrew):
        """Overwrite an entry's sense (best option when surface == bare lemma, a
        form-homograph that can't be split data-only). Merges glosses if a prior
        verdict already re-glossed this same entry (e.g. ה' and ה collide)."""
        if hebrew:
            entry["pos"] = v.get("corrected_pos") or "Hebrew quote"
            entry["root"] = "—"
        else:
            for f_src, f_dst in [("corrected_pos", "pos"), ("target_root", "root"),
                                 ("target_lemma_ar", "lemma_ar")]:
                if v.get(f_src):
                    entry[f_dst] = v[f_src]
        collision = entry["id"] in edited_ids  # a PRIOR verdict already re-glossed it
        edited_ids.setdefault(entry["id"], set())
        for f_src, f_dst in [("corrected_gloss_en", "gloss_en"), ("corrected_gloss_he", "gloss_he")]:
            new = v.get(f_src)
            if not new:
                continue
            if collision and entry.get(f_dst) and new not in entry[f_dst]:
                entry[f_dst] = f"{entry[f_dst]} / {new}"   # keep both senses (e.g. ה'/ה)
            else:
                entry[f_dst] = new                          # first edit: clean replace

    def target_for(v, surface, s_nf):
        if v.get("verdict") == "hebrew_quote":
            hid = f"heb-{s_nf}"
            return index.get(hid, (None, None))[0] or make_entry(
                hid, surface, "", "—", v.get("corrected_pos") or "Hebrew quote",
                v.get("corrected_gloss_en", ""), v.get("corrected_gloss_he", ""), v.get("evidence", ""))
        t = find_sense(v.get("target_lemma_ja", ""), v.get("target_root"),
                       v.get("corrected_pos"), v.get("corrected_gloss_en"))
        if t is None:
            nid = f"qc-{(v.get('target_root') or 'x').replace(' ', '')}-{s_nf}"
            t = make_entry(nid, v.get("target_lemma_ja", surface), v.get("target_lemma_ar", ""),
                           v.get("target_root", "—"), v.get("corrected_pos", ""),
                           v.get("corrected_gloss_en", ""), v.get("corrected_gloss_he", ""), v.get("evidence", ""))
        return t

    for v in verdicts:
        verd = v.get("verdict")
        conf = v.get("confidence")
        if verd == "ok":
            continue
        if not accept_all and (verd not in APPLY_VERDICTS or conf != "high"):
            defer(v, f"{verd}/{conf}")
            continue

        ref = index.get(v["entry_id"])
        if ref is None:
            problems.append(f"entry id not found: {v['entry_id']} (surface {v['surface']})")
            continue
        src, _ = ref
        surface = v["surface"]
        s_nf = nf(surface)
        src_vars = src.get("variants", []) or []
        in_lemma = s_nf == nf(src["lemma_ja"])
        in_vars = s_nf in {nf(w) for w in src_vars}
        same_lemma = bool(v.get("target_lemma_ja")) and nf(v["target_lemma_ja"]) == nf(src["lemma_ja"])
        same_root = (not v.get("target_root")) or nf(v.get("target_root", "")) == nf(src.get("root", ""))

        # EDIT only when it's a pure refinement of THIS entry's own sense
        # (same lemma + same root) — never when the surface is a homograph that
        # would change the bare lemma's meaning for other texts.
        if verd == "wrong_pos_or_sense" and same_lemma and same_root and not in_lemma:
            for f_src, f_dst in [("corrected_pos", "pos"), ("corrected_gloss_en", "gloss_en"),
                                 ("corrected_gloss_he", "gloss_he")]:
                if v.get(f_src):
                    src[f_dst] = v[f_src]
            touched_surfaces.add(surface)
            applied.append(("EDIT", surface, src["id"], "patched fields"))
            continue

        # Everything else is a MOVE/RETAG of the EXACT surface form. Guard rails:
        #   - the exact full surface must be what's wrongly attached (in_vars);
        #     if it only matched via a shorter stripped candidate, the shorter
        #     form may be legit for src — DEFER (e.g. לבך via בך = Arabic bika).
        #   - never steal a bare lemma (in_lemma) — that's a true form-homograph
        #     we can't split data-only — DEFER.
        # Under --accept-all (user reviewed the sheet) we instead route these:
        #   in_lemma          -> EDIT the entry in place to the corrected sense;
        #   stripped-only      -> ATTACH the full surface to the correct entry
        #                         (full-token precedence), WITHOUT detaching the
        #                         legit shorter form from src.
        if in_lemma or not in_vars:
            if not accept_all:
                defer(v, "bare-lemma or stripped-only match (form-homograph; needs manual/UI)")
                continue
            if in_lemma:
                # Refuse a destructive relabel of an entry that already carries a
                # real (Arabic) sense when the verdict offers NO replacement gloss
                # — e.g. ירא: Hebrew quote here, but Arabic yurā "is seen"
                # elsewhere. Leave it for the sheet rather than break the entry.
                if not (v.get("corrected_gloss_en") or v.get("corrected_gloss_he")):
                    defer(v, "no replacement gloss for a bare-lemma homograph (kept as-is)")
                    continue
                edit_in_place(src, v, hebrew=(verd == "hebrew_quote"))
                touched_surfaces.add(surface)
                applied.append(("EDIT*", surface, src["id"], "in-place (form-homograph)"))
            else:
                tgt = target_for(v, surface, s_nf)
                tvars = tgt.setdefault("variants", [])
                if surface not in tvars:
                    tvars.append(surface)
                touched_surfaces.add(surface)
                applied.append(("ATTACH", surface, src["id"], f"-> {tgt['id']} (kept src)"))
            continue

        # Resolve the target BEFORE mutating src, so a self-move is a no-op.
        if verd == "hebrew_quote":
            heb_id = f"heb-{s_nf}"
            tgt = index.get(heb_id, (None, None))[0]
            tgt_is_new = tgt is None
        else:  # MOVE
            tgt = find_sense(v["target_lemma_ja"], v.get("target_root"),
                             v.get("corrected_pos"), v.get("corrected_gloss_en"))
            tgt_is_new = tgt is None

        if tgt is not None and tgt["id"] == src["id"]:
            defer(v, "target == source (entry already holds the correct sense)")
            continue

        # detach ONLY the exact surface form; src keeps its other forms.
        src["variants"] = [w for w in src_vars if nf(w) != s_nf]
        touched_surfaces.add(surface)

        if tgt_is_new:
            if verd == "hebrew_quote":
                tgt = make_entry(f"heb-{s_nf}", surface, "", "—",
                                 v.get("corrected_pos") or "Hebrew quote",
                                 v.get("corrected_gloss_en", ""), v.get("corrected_gloss_he", ""),
                                 v.get("evidence", ""))
            else:
                new_id = f"qc-{(v.get('target_root') or 'x').replace(' ', '')}-{s_nf}"
                tgt = make_entry(new_id, v["target_lemma_ja"], v.get("target_lemma_ar", ""),
                                 v.get("target_root", "—"), v.get("corrected_pos", ""),
                                 v.get("corrected_gloss_en", ""), v.get("corrected_gloss_he", ""),
                                 v.get("evidence", ""))
        tvars = tgt.setdefault("variants", [])
        if surface not in tvars:
            tvars.append(surface)
        applied.append((verd == "hebrew_quote" and "RETAG" or "MOVE",
                        surface, src["id"], f"-> {tgt['id']}"))

    # ---- no-orphan check: every touched surface still resolves --------------
    all_keys = set(lemma_index.keys())
    for e in lane["entries"] + starter["entries"]:
        for w in e.get("variants", []) or []:
            all_keys.add(nf(w))
    for s in sorted(touched_surfaces):
        if not (cand_norms(s) & all_keys):
            problems.append(f"ORPHAN: surface {s!r} no longer resolves after move")

    print(f"verdicts: {len(verdicts)} | applied: {len(applied)} | "
          f"deferred(review): {len(deferred)} | created entries: {len(created)} | "
          f"problems: {len(problems)}")
    for op, s, sid, info in applied[:60]:
        print(f"  {op:5} {s:<12} from {sid:<22} {info}")
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print("  ✗ " + p)

    if dry:
        print("\n[dry-run] no files written")
        return

    json.dump(lane, open(LANE, "w"), ensure_ascii=False, indent=2)
    json.dump(starter, open(STARTER, "w"), ensure_ascii=False, indent=2)
    write_revision_sheet(deferred)
    update_ledger(applied)
    print(f"\nwrote {LANE}, {STARTER}, {SHEET}")


def write_revision_sheet(deferred):
    lines = ["# Dictionary QC — manual review (homographs + medium/low confidence)\n",
             "Accept = apply by hand; reject = leave as-is. Generated by apply_dict_corrections.py.\n"]
    for v in deferred:
        lines.append(f"\n## `{v['surface']}` — {v['verdict']} ({v['confidence']})")
        lines.append(f"- shown entry: `{v['entry_id']}`")
        if v.get("target_lemma_ja"):
            lines.append(f"- proposed: {v['target_lemma_ja']} / {v.get('corrected_pos','')} / "
                         f"{v.get('corrected_gloss_en','')}")
        lines.append(f"- evidence: {v.get('evidence','')}")
        if v.get("note"):
            lines.append(f"- note: {v['note']}")
    open(SHEET, "w").write("\n".join(lines) + "\n")


def update_ledger(applied):
    if not os.path.exists(LEDGER):
        return
    led = json.load(open(LEDGER))
    table = led.get("ledger", {})
    applied_surfaces = {(s, sid) for _, s, sid, _ in applied}
    for key, rec in table.items():
        surf, eid = key.split("\t", 1)
        if (surf, eid) in applied_surfaces:
            rec["applied"] = True
    json.dump(led, open(LEDGER, "w"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()

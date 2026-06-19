#!/usr/bin/env python3
"""Build a reverse index of every Scripture verse Maimonides cites in Part I.

Scans the English `en` fields of data/moreh-bab{1..28}.json for citations of the
form "(Gen 28:13)", "(1 Sam 2:2)", "(Hag. 2:1)", "(b. Berakhot 31b)", and emits
data/moreh-verse-index.json: per biblical book (Tanakh order), each verse →
the chapters that cite it + a short snippet (Maimonides' own gloss), plus a
Sefaria ref for an outbound link.

Run:  python3 scripts/build_moreh_verse_index.py
"""
import json, re, glob
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# abbrev -> (sefaria_url_book, display_name, tanakh_order)
BOOKS = {
    "Gen": ("Genesis", "Genesis", 1),
    "Exod": ("Exodus", "Exodus", 2),
    "Lev": ("Leviticus", "Leviticus", 3),
    "Num": ("Numbers", "Numbers", 4),
    "Deut": ("Deuteronomy", "Deuteronomy", 5),
    "Josh": ("Joshua", "Joshua", 6),
    "Judg": ("Judges", "Judges", 7),
    "1 Sam": ("I_Samuel", "I Samuel", 8),
    "1 Kgs": ("I_Kings", "I Kings", 10),
    "Isa": ("Isaiah", "Isaiah", 12),
    "Jer": ("Jeremiah", "Jeremiah", 13),
    "Ezek": ("Ezekiel", "Ezekiel", 14),
    "Hos": ("Hosea", "Hosea", 15),
    "Amos": ("Amos", "Amos", 18),
    "Mic": ("Micah", "Micah", 21),
    "Hab": ("Habakkuk", "Habakkuk", 23),
    "Zech": ("Zechariah", "Zechariah", 25),
    "Mal": ("Malachi", "Malachi", 26),
    "Ps": ("Psalms", "Psalms", 27),
    "Prov": ("Proverbs", "Proverbs", 28),
    "Job": ("Job", "Job", 29),
    "Eccl": ("Ecclesiastes", "Ecclesiastes", 33),
    "Lam": ("Lamentations", "Lamentations", 35),
    "Esth": ("Esther", "Esther", 34),
    "1 Chr": ("I_Chronicles", "I Chronicles", 37),
    # Rabbinic
    "Hag.": ("Mishnah_Chagigah", "Mishnah & Talmud", 90),
}

# Standard "(Book ch:v)" — longest abbrevs first so "1 Sam" wins over "Sam".
_keys = sorted(BOOKS.keys(), key=lambda k: -len(k))
STD = re.compile(r"\((" + "|".join(re.escape(k) for k in _keys) + r")\s+(\d+):(\d+)\)")
# Talmud "(b. Tractate 31b)"
TALMUD = re.compile(r"\(b\.\s+([A-Z][A-Za-z]+)\s+(\d+[ab])\)")


def snippet_for(seg, cite_str):
    """Prefer the phrase-pair whose English contains the citation; else the segment."""
    for p in seg.get("pairs", []):
        if cite_str in p.get("en", ""):
            return p["en"]
    return seg.get("en", "")


def main():
    # book_display -> { "v"/"daf" -> {ref, occ:set((n, snippet)) , order, ch, vnum} }
    index = {}
    total_citations = 0

    for f in sorted(glob.glob(str(DATA / "moreh-bab*.json"))):
        n = int(re.search(r"moreh-bab(\d+)\.json", f).group(1))
        d = json.load(open(f, encoding="utf-8"))
        for pg in d["pages"]:
            for seg in pg["aligned"]:
                if seg.get("isHeader"):
                    continue
                en = seg.get("en", "")
                for m in STD.finditer(en):
                    abbr, ch, v = m.group(1), int(m.group(2)), int(m.group(3))
                    url_book, disp, order = BOOKS[abbr]
                    ref = f"{url_book}.{ch}.{v}"
                    label = f"{ch}:{v}"
                    snip = snippet_for(seg, m.group(0))
                    _add(index, disp, order, label, ref, ch, v, n, snip)
                    total_citations += 1
                for m in TALMUD.finditer(en):
                    tract, daf = m.group(1), m.group(2)
                    ref = f"{tract}.{daf}"
                    label = f"b. {tract} {daf}"
                    snip = snippet_for(seg, m.group(0))
                    _add(index, "Mishnah & Talmud", 90, label, ref, 9999, 0, n, snip)
                    total_citations += 1

    # Serialize: book order, verses sorted by (ch, v), occ sorted by chapter.
    out_books = []
    for disp in sorted(index, key=lambda b: index[b]["order"]):
        verses = index[disp]["verses"]
        vlist = []
        for label in sorted(verses, key=lambda L: (verses[L]["ch"], verses[L]["v"], L)):
            ent = verses[label]
            occ = sorted(
                ({"n": n, "snippet": s} for (n, s) in ent["occ"]),
                key=lambda o: o["n"],
            )
            vlist.append({"v": label, "ref": ent["ref"], "occ": occ})
        out_books.append({"book": disp, "order": index[disp]["order"], "verses": vlist})

    doc = {
        "_note": "Reverse index of Scripture citations in Moreh Nevukhim Part I "
                 "(chapters 1-28). Built from the English of data/moreh-bab*.json by "
                 "scripts/build_moreh_verse_index.py.",
        "totals": {
            "books": len(out_books),
            "verses": sum(len(b["verses"]) for b in out_books),
            "citations": total_citations,
        },
        "books": out_books,
    }
    path = DATA / "moreh-verse-index.json"
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path}")
    print(f"books={doc['totals']['books']} verses={doc['totals']['verses']} "
          f"citations={doc['totals']['citations']}")


def _add(index, disp, order, label, ref, ch, v, n, snip):
    book = index.setdefault(disp, {"order": order, "verses": {}})
    ent = book["verses"].setdefault(label, {"ref": ref, "ch": ch, "v": v, "occ": set()})
    ent["occ"].add((n, snip.strip()))


if __name__ == "__main__":
    main()

"""Translate one chapter of Saadia's JA Tafsir to Portuguese via the Claude API.

Portuguese sibling of scripts/translate_tafsir_english.py. Same goal — an
elevated, formal, liturgical Portuguese rendering that mirrors the
Judeo-Arabic closely enough for reverse translation: a reader looks at the JA
in the Tafsir reader and uses the Portuguese to make sense of the Arabic. This
means:

  - Translate the JA, NOT the biblical Hebrew. Saadia's interpretive moves
    (e.g. שא ... אן יכון for ויאמר ... יהי, עלם for וירא, צורה for צלם,
    מסלטא inserted at 'in our image') are part of the source.
  - Where Saadia's JA sense differs from classical Arabic, follow Blau
    (Dictionary of Medieval Judaeo-Arabic Texts).
  - Register: high literary / liturgical Portuguese befitting a Gaonic sage,
    in the manner of the classical Portuguese Bibles (Almeida Revista,
    Figueiredo) but pitched higher — solemn, dignified, lightly archaizing,
    European orthography, enclitic pronouns.

Inputs (cached on the API side, reused across all chapters):
  - data-source/saadia-gloss-table.json — JA→EN sense mappings, principles
    (used as a SEMANTIC reference; the output is Portuguese)
  - data-source/blau-genesis-notes.json — Blau's verse-by-verse notes for
    Bereshit 1-12
  - data/tafsir-bereshit-1-portuguese.json — Bereshit 1 as a worked exemplar
  - data/tafsir-bereshit-1.json — the JA source for that exemplar

Per-chapter input:
  - data/tafsir-{book}-{ch}.json — the JA chapter to translate

Output:
  - data/tafsir-{book}-{ch}-portuguese.json — {translations: {v: portuguese}}
    with _status: "draft" and _model marker

Usage:
    export ANTHROPIC_API_KEY=...
    pip install anthropic
    python3 scripts/translate_tafsir_portuguese.py --book bereshit --chapter 13
    python3 scripts/translate_tafsir_portuguese.py --book shemot --all
    python3 scripts/translate_tafsir_portuguese.py --book bereshit --chapter 2 --dry-run

The --dry-run flag prints the request payload without calling the API. Useful
when calibrating the prompt before paying for tokens.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SOURCE_DIR = ROOT / "data-source"

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 8000

# Sonnet 4.6 pricing (USD per million tokens), as of 2026-02:
PRICE_INPUT_PER_MTOK = 3.00
PRICE_OUTPUT_PER_MTOK = 15.00
PRICE_CACHE_WRITE_PER_MTOK = 3.75   # 1.25× input
PRICE_CACHE_READ_PER_MTOK = 0.30    # 0.10× input

# Persistent cost-meter file. Survives across runs so a multi-book
# pipeline cannot blow past the user's budget by restarting. Kept separate
# from the English meter so the two pipelines account independently.
COST_METER_PATH = Path.home() / ".cache" / "judeo-arabic-app" / "translation-cost-pt.json"

DEFAULT_COST_CAP_USD = 10.00

SYSTEM_INSTRUCTIONS = """Estás a traduzir o Tafsir (תפסיר) judeo-árabe do século X de Saadia Gaon sobre a Torá para PORTUGUÊS LITERÁRIO E LITÚRGICO ELEVADO.

OBJETIVO PRIMORDIAL: o português deve espelhar o judeo-árabe (JA) de tão perto que um leitor, olhando para o JA, possa usar o português para desambiguar o árabe — tradução reversa. O leitor do Tafsir em judeo-arabic-app mostra o JA acima da tradução; a função do português é glosar o que Saadia escreveu, NÃO reproduzir o hebraico bíblico.

REGISTO — CRÍTICO: Português alto, formal, digno e ligeiramente arcaizante, próprio de um Gaon — solene, à maneira das versões bíblicas portuguesas clássicas (João Ferreira de Almeida Revista, Matos Soares / Figueiredo), mas de tom mais elevado e literário. Usa ênclise pronominal (separou-as, chamou-lhe), léxico erudito e cadência digna. EVITA coloquialismos e informalidades brasileiras; prefere a ortografia e a sintaxe europeias. Voz como "E Deus ..." / "E houve ...".

PRINCÍPIOS FUNDAMENTAIS:

1. **Traduz o JUDEO-ÁRABE, não o hebraico bíblico.** Onde Saadia interpreta ou racionaliza, a sua interpretação É o texto-fonte. Substituições caraterísticas de Saadia que DEVES preservar, vertidas no registo elevado:
   - שא ... אן יכון (para o hebraico ויאמר ... יהי) → "quis que houvesse ..." — NÃO "disse: haja ..."
   - עלם (para וירא) → "soube" / "conheceu" — NÃO "viu"
   - צורה (para צלם) → "forma" — NÃO "imagem"
   - ריאח אללה (para רוח אלהים) → "os ventos de Deus" (PLURAL) — NÃO "o espírito de Deus"
   - פכאן (para ויהי) → "e assim foi" / "e houve"
   - מסלטא (palavra acrescentada por Saadia, Gén 1:26-27) → "com domínio" / "senhoreando" / "soberano"
   - נפסא נאטקה (para נפש חיה quando Adão é dotado de alma, Gén 2:7) → "alma racional" / "alma que fala"
   - וַלַמּא מצ'י' מן אלליל ואלנהאר יום N (para ויהי ערב ויהי בקר יום N) → "E, tendo decorrido da noite e do dia, o Nº dia"
   - תסתחק אן תמות (para מות תמות) → "merecerás morrer"
   - חאכמא (acrescentado por Saadia em לאמר quando a fala é um decreto) → "decretando"
   - אוקאת אלנור (glosa de Saadia para "[Deus chamou à] luz [dia]") → "os tempos da luz"

2. **Onde o uso JA de Saadia diverge do árabe clássico, segue o sentido judeo-árabe (Blau).** Exemplos:
   - אלגלד = "o firmamento" / "a expansão" — NÃO "duro, gelado"
   - דנא ב = "aproximar-se" — NÃO "estar perto"
   - אלי אלדהר = "para sempre" — NÃO "por uma geração"

3. **Traduzibilidade reversa.** Um leitor atento deve conseguir mapear a maioria das palavras portuguesas de volta a uma palavra JA no mesmo versículo. Não suavizes para o hebraico bíblico, não parafraseies o que Saadia formulou de modo conciso, não acrescentes palavras que Saadia não escreveu.

4. **Identificações de topónimos.** Saadia identifica topónimos bíblicos com a geografia então corrente. Na PRIMEIRA ocorrência num capítulo dá como "o Nilo (Pishon)" etc.; nas ocorrências seguintes apenas a identificação:
   - פישון → "o Nilo (Pishon)"
   - חוילה → "Zawila (Havilá)"
   - כוש → "a Abissínia (Cuxe)"
   - חידקל → "o Tigre (Hidékel)"
   - אשור → "Mossul (Assur)"

5. **'אדם' como nome próprio.** A partir de Gén 2:7 Saadia usa 'אדם' como nome — traduz "Adão", não "o homem".

6. **O 'סאיר' de Saadia para o 'כל' repetido.** Quando Saadia usa 'סאיר' para o segundo 'כל' de um versículo, verte "e o restante de" / "e todo o mais" — preserva a recusa da duplicação literal.

FORMATO DE SAÍDA — ESTRITO:
Devolve APENAS um único objeto JSON com esta forma exata, sem preâmbulo, sem markdown:
{"translations": {"1": "português do v.1", "2": "português do v.2", ...}}

As chaves são números de versículo em texto. Inclui TODOS os versículos fornecidos. Cada valor é uma única linha de português (sem quebras de linha).
"""


def load_gloss_table() -> dict:
    p = SOURCE_DIR / "saadia-gloss-table.json"
    return json.loads(p.read_text(encoding="utf-8"))


def load_blau_notes() -> dict:
    p = SOURCE_DIR / "blau-genesis-notes.json"
    return json.loads(p.read_text(encoding="utf-8"))


def load_exemplar(book: str, chapter: int) -> tuple[dict, dict]:
    src = json.loads((DATA_DIR / f"tafsir-{book}-{chapter}.json").read_text(encoding="utf-8"))
    pt = json.loads((DATA_DIR / f"tafsir-{book}-{chapter}-portuguese.json").read_text(encoding="utf-8"))
    return src, pt


# Bereshit 1 seeds the register (creation vocabulary, the anti-anthropomorphic
# moves, "E, tendo decorrido da noite e do dia, o Nº dia"). Authored in the
# Bereshit 1-12 pilot; add more exemplars here as later books are calibrated.
EXEMPLAR_CHAPTERS = [("bereshit", 1)]


def format_exemplar(label: str, src: dict, pt_map: dict) -> str:
    text = f"{label} (exemplo trabalhado — segue esta voz):\n\n"
    for v in src["verses"]:
        pt = pt_map.get(str(v["v"]), "")
        text += f"v.{v['v']}\n  JA: {v['ja']}\n  AR: {v['arabic']}\n  HE: {v['hebrew']}\n  PT: {pt}\n\n"
    return text


def build_system_blocks(book: str | None = None) -> list[dict]:
    """Cached system context: instructions + gloss table + Blau notes + exemplars.

    Returned as a list of content blocks with cache_control on the heavy ones so
    Claude reuses them across all chapter calls in a session. The gloss table and
    Blau notes carry English glosses — here they serve as a SEMANTIC reference for
    Saadia's reading; the output register is Portuguese.
    """
    gloss = load_gloss_table()
    blau = load_blau_notes()

    exemplar_text = ""
    for ex_book, ch in EXEMPLAR_CHAPTERS:
        try:
            src, pt = load_exemplar(ex_book, ch)
        except FileNotFoundError:
            # Pilot not yet run for this exemplar — skip rather than abort.
            continue
        label = f"EXEMPLO {ex_book.upper()} {ch}"
        exemplar_text += format_exemplar(label, src, pt["translations"])
        exemplar_text += "\n" + ("=" * 60) + "\n\n"

    blocks = [
        {"type": "text", "text": SYSTEM_INSTRUCTIONS},
        {
            "type": "text",
            "text": "TABELA DE GLOSAS (padrões JA→sentido específicos de Saadia, princípios, sinalizações Blau-vs-Lane; referência semântica — a saída é em português):\n\n"
            + json.dumps(gloss, ensure_ascii=False, indent=2),
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": "NOTAS DE BLAU (versículo a versículo, Génesis 1-12; consulta antes de traduzir qualquer versículo nesse intervalo):\n\n"
            + json.dumps(blau, ensure_ascii=False, indent=2),
            "cache_control": {"type": "ephemeral"},
        },
    ]
    if exemplar_text:
        blocks.append(
            {
                "type": "text",
                "text": exemplar_text,
                "cache_control": {"type": "ephemeral"},
            }
        )
    return blocks


def build_user_message(book: str, chapter: int) -> str:
    src_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}.json"
    chapter_data = json.loads(src_path.read_text(encoding="utf-8"))

    lines = [
        f"Traduz todos os versículos de {chapter_data['book']} capítulo {chapter_data['chapter']}.",
        "Saída JSON: {\"translations\": { ... }} com uma entrada por versículo.",
        "",
        "VERSÍCULOS:",
        "",
    ]
    for v in chapter_data["verses"]:
        lines.append(f"v.{v['v']}")
        lines.append(f"  JA: {v['ja']}")
        lines.append(f"  AR: {v['arabic']}")
        lines.append(f"  HE (bíblico, só para orientação — traduz o JA): {v['hebrew']}")
        if v.get("hebrew_translation"):
            lines.append(f"  HE-tradução (versão hebraica do Cairo do Saadia; pode conter comentário entre parênteses — ignora o comentário): {v['hebrew_translation']}")
        lines.append("")
    return "\n".join(lines)


def parse_translations(text: str) -> dict[str, str]:
    """Extract the {translations: {...}} object from the model's reply.

    The system prompt tells the model to return raw JSON, but be permissive in
    case it wraps in a code fence or adds a preamble.
    """
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines)
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in reply:\n{text[:300]}")
    obj = json.loads(text[start : end + 1])
    if "translations" not in obj:
        raise ValueError(f"reply missing 'translations' key: {list(obj.keys())}")
    return obj["translations"]


def load_cost_meter() -> dict:
    if not COST_METER_PATH.exists():
        return {"cumulative_usd": 0.0, "calls": 0}
    try:
        return json.loads(COST_METER_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"cumulative_usd": 0.0, "calls": 0}


def save_cost_meter(meter: dict) -> None:
    COST_METER_PATH.parent.mkdir(parents=True, exist_ok=True)
    COST_METER_PATH.write_text(json.dumps(meter, indent=2), encoding="utf-8")


def usage_to_cost(usage) -> float:
    inp = getattr(usage, "input_tokens", 0) or 0
    out = getattr(usage, "output_tokens", 0) or 0
    cache_w = getattr(usage, "cache_creation_input_tokens", 0) or 0
    cache_r = getattr(usage, "cache_read_input_tokens", 0) or 0
    return (
        inp * PRICE_INPUT_PER_MTOK / 1e6
        + out * PRICE_OUTPUT_PER_MTOK / 1e6
        + cache_w * PRICE_CACHE_WRITE_PER_MTOK / 1e6
        + cache_r * PRICE_CACHE_READ_PER_MTOK / 1e6
    )


def call_claude(system_blocks: list[dict], user_msg: str, cost_cap_usd: float) -> tuple[str, float]:
    """Call Claude. Returns (reply_text, this_call_cost_usd).

    Aborts BEFORE the call if the cumulative cost is already at/over the cap.
    Updates the persistent cost meter AFTER the call returns.
    """
    try:
        import anthropic  # type: ignore
    except ImportError:
        print(
            "ERROR: 'anthropic' SDK not installed. Run:\n  pip3 install anthropic",
            file=sys.stderr,
        )
        sys.exit(2)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "ERROR: ANTHROPIC_API_KEY not set. Export it before running:\n"
            "  export ANTHROPIC_API_KEY=sk-ant-...",
            file=sys.stderr,
        )
        sys.exit(3)

    meter = load_cost_meter()
    if meter["cumulative_usd"] >= cost_cap_usd:
        print(
            f"COST CAP REACHED: cumulative ${meter['cumulative_usd']:.4f} "
            f">= cap ${cost_cap_usd:.2f}. Aborting before next call.\n"
            f"To raise the cap: pass --cost-cap, or edit/delete {COST_METER_PATH}",
            file=sys.stderr,
        )
        sys.exit(5)

    import anthropic  # type: ignore

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system_blocks,
        messages=[{"role": "user", "content": user_msg}],
    )
    parts = []
    for block in resp.content:
        if getattr(block, "type", None) == "text":
            parts.append(block.text)

    this_cost = usage_to_cost(resp.usage)
    meter["cumulative_usd"] += this_cost
    meter["calls"] += 1
    save_cost_meter(meter)
    print(
        f"  cost: ${this_cost:.4f} this call  |  cumulative: ${meter['cumulative_usd']:.4f} / ${cost_cap_usd:.2f} cap "
        f"(call #{meter['calls']})",
        file=sys.stderr,
    )

    return "".join(parts), this_cost


def write_sidecar(book: str, chapter: int, translations: dict[str, str]) -> Path:
    out_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}-portuguese.json"
    payload = {
        "_note": (
            f"Elevated literary/liturgical Portuguese rendering of Saadia's JA Tafsir on {book.title()} {chapter}, "
            "generated by scripts/translate_tafsir_portuguese.py against the JA "
            "(not the biblical Hebrew). Translation goal: reverse-translatability "
            "for the Tafsir reader — readers should be able to map Portuguese back to JA. "
            "Saadia-specific moves preserved per data-source/saadia-gloss-table.json; "
            "Blau's notes (data-source/blau-genesis-notes.json) consulted for Bereshit 1-12. "
            "Draft pending author revision."
        ),
        "_status": "draft",
        "_model": MODEL,
        "translations": translations,
    }
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return out_path


def translate_chapter(book: str, chapter: int, system_blocks: list[dict], cost_cap_usd: float) -> int:
    src_path = DATA_DIR / f"tafsir-{book.lower()}-{chapter}.json"
    if not src_path.exists():
        print(f"missing source chapter: {src_path}", file=sys.stderr)
        return 1

    user_msg = build_user_message(book, chapter)
    print(f"calling Claude for {book} {chapter}...", file=sys.stderr)
    reply, _cost = call_claude(system_blocks, user_msg, cost_cap_usd)
    try:
        translations = parse_translations(reply)
    except Exception as e:
        print(f"failed to parse reply: {e}", file=sys.stderr)
        debug = DATA_DIR / f"tafsir-{book.lower()}-{chapter}-portuguese.raw.txt"
        debug.write_text(reply, encoding="utf-8")
        print(f"raw reply written to {debug}", file=sys.stderr)
        return 4

    src = json.loads(src_path.read_text(encoding="utf-8"))
    expected_vs = {str(v["v"]) for v in src["verses"]}
    got = set(translations.keys())
    missing = expected_vs - got
    extra = got - expected_vs
    if missing:
        print(f"WARNING: missing verses in reply: {sorted(missing, key=int)}", file=sys.stderr)
    if extra:
        print(f"WARNING: unexpected verses in reply: {sorted(extra, key=lambda x: int(x) if x.isdigit() else 9999)}", file=sys.stderr)

    out = write_sidecar(book, chapter, translations)
    print(f"wrote {len(translations)} verses → {out.relative_to(ROOT)}")
    return 0


def discover_chapters(book: str) -> list[int]:
    prefix = f"tafsir-{book.lower()}-"
    chs = []
    for p in DATA_DIR.iterdir():
        name = p.name
        if not name.startswith(prefix) or not name.endswith(".json"):
            continue
        stem = name[len(prefix):-len(".json")]
        if not stem.isdigit():
            continue
        chs.append(int(stem))
    return sorted(chs)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--book", required=True, help="e.g. bereshit, shemot")
    ap.add_argument("--chapter", type=int,
                    help="Single chapter. Omit (with --all) to run every chapter in the book.")
    ap.add_argument("--all", action="store_true",
                    help="Translate every chapter in --book that doesn't already have a Portuguese sidecar.")
    ap.add_argument("--force", action="store_true",
                    help="With --all, re-translate chapters that already have a sidecar.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print the request payload size and the user message preview without calling the API.")
    ap.add_argument("--cost-cap", type=float, default=DEFAULT_COST_CAP_USD,
                    help=f"Hard cap on cumulative USD spend across runs (default ${DEFAULT_COST_CAP_USD:.2f}). "
                         f"The cap survives restarts via {COST_METER_PATH}. Aborts before any call that would cross the cap.")
    ap.add_argument("--reset-cost-meter", action="store_true",
                    help="Reset the persistent cost meter to $0 before running.")
    ap.add_argument("--show-cost", action="store_true",
                    help="Print the current cumulative cost and exit.")
    args = ap.parse_args()

    if args.show_cost:
        meter = load_cost_meter()
        print(f"cumulative: ${meter['cumulative_usd']:.4f}  calls: {meter['calls']}")
        print(f"meter file: {COST_METER_PATH}")
        return 0

    if args.reset_cost_meter:
        save_cost_meter({"cumulative_usd": 0.0, "calls": 0})
        print(f"cost meter reset to $0 at {COST_METER_PATH}", file=sys.stderr)

    if not args.all and args.chapter is None:
        ap.error("either --chapter N or --all is required")

    system_blocks = build_system_blocks(args.book)

    if args.dry_run:
        ch = args.chapter if args.chapter is not None else (discover_chapters(args.book)[:1] or [1])[0]
        user_msg = build_user_message(args.book, ch)
        sys_chars = sum(len(b["text"]) for b in system_blocks)
        print(f"[dry-run] system chars: {sys_chars:>7,}  (~{sys_chars//4:,} tokens)")
        print(f"[dry-run] user chars:   {len(user_msg):>7,}  (~{len(user_msg)//4:,} tokens)")
        print(f"[dry-run] model:        {MODEL}")
        print(f"[dry-run] cache blocks: {sum(1 for b in system_blocks if 'cache_control' in b)}")
        print()
        print("--- USER MESSAGE PREVIEW (first 1200 chars) ---")
        print(user_msg[:1200])
        return 0

    if args.all:
        chapters = discover_chapters(args.book)
        if not chapters:
            print(f"no source chapters found for book={args.book}", file=sys.stderr)
            return 1
        skipped = 0
        for ch in chapters:
            out_path = DATA_DIR / f"tafsir-{args.book.lower()}-{ch}-portuguese.json"
            if out_path.exists() and not args.force:
                skipped += 1
                continue
            rc = translate_chapter(args.book, ch, system_blocks, args.cost_cap)
            if rc != 0:
                print(f"halting --all at {args.book} {ch} (rc={rc})", file=sys.stderr)
                return rc
        print(f"done. translated {len(chapters)-skipped}, skipped {skipped} (already had sidecar)")
        meter = load_cost_meter()
        print(f"total cost so far: ${meter['cumulative_usd']:.4f} ({meter['calls']} API calls)")
        return 0

    return translate_chapter(args.book, args.chapter, system_blocks, args.cost_cap)


if __name__ == "__main__":
    raise SystemExit(main())

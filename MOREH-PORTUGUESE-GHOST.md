# Moreh Nevukhim → Portuguese — driverless ("ghost") translation plan

A self-driving, cloud-resident loop that renders the whole *Guide of the
Perplexed* (Dalālat al-Ḥāʾirīn / Moreh Nevukhim) into elevated European
Portuguese, chapter by chapter, committing a checkpoint after each one — so it
keeps advancing while you are offline, asleep, or on a plane. Same model as the
Tafsir Portuguese pass; adapted to the Moreh data shape.

**Branch:** `claude/moreh-nevukhim-portuguese-6z87nf`
**Corpus:** 178 chapters (Part I ×76, Part II ×48, Part III ×54), ~1,596
aligned segments. Ordered Part I → II → III, ascending.

---

## How it runs without you (the "ghost")

Each cycle is a **fresh Claude Code web session** fired by a recurring
**Routine (cron trigger)**. Because every firing runs server-side in the cloud,
nothing depends on your laptop or connection. A cycle is fully self-contained
and idempotent — if a session dies mid-chapter, the next one re-reads coverage
from disk and finishes it. Progress is durable because every cycle **commits +
pushes** before it ends.

```
Routine fires ─▶ fresh cloud session ─▶ [THE CYCLE below] ─▶ commit + push ─▶ ends
      ▲                                                                          │
      └──────────────────────── N minutes later ────────────────────────────────┘
```

### THE CYCLE — the exact prompt the Routine fires

> You are the **Moreh Nevukhim Portuguese ghost-runner**. Work autonomously and
> non-interactively — never ask questions; make the reasonable choice and keep
> going.
>
> 1. `cd` to the repo. `git fetch origin claude/moreh-nevukhim-portuguese-6z87nf`
>    and `git checkout` it, then `git reset --hard origin/claude/moreh-nevukhim-portuguese-6z87nf`
>    so you resume from the last checkpoint (never from stale local state).
> 2. Run `python3 scripts/moreh_pt_status.py --next-json`. If it returns `{}`,
>    the corpus is **complete** — post a one-line "Moreh Portuguese complete 🎉"
>    and stop (see *Turning it off*). Otherwise you get the next chapter's
>    `base`, `source`, and `missing_pages`.
> 3. Read `data/<source>` and the worked exemplar `data/moreh-bab1-portuguese.json`.
>    Translate **every** aligned segment (and any free-flow `paragraphs`) on the
>    missing pages into Portuguese, following *The register* below. Author
>    against the **Judeo-Arabic**, not the English.
> 4. Write/extend `data/<base>-portuguese.json` in the sidecar shape (below).
>    Keep any segments already translated; only fill gaps. To go faster you may
>    translate **2–3 chapters** in one cycle if the budget allows.
> 5. `npm run build`. It must succeed (the coverage gate must stay `GATE PASSED`).
>    If the build breaks, fix your JSON (usually a stray quote or a length
>    mismatch) before committing — never push a red build.
> 6. `git add -A && git commit` with a message like
>    `Moreh Portuguese: I:<ch> (ghost checkpoint)` and
>    `git push -u origin claude/moreh-nevukhim-portuguese-6z87nf`
>    (retry on network error: 2s, 4s, 8s, 16s).
> 7. Run `python3 scripts/moreh_pt_status.py` and end your turn with the summary
>    line. Do **not** open a pull request.

Keep each cycle small enough to finish and push within one session — a pushed
checkpoint is worth more than an ambitious unpushed one.

---

## The register (reverse-translation rules)

The Portuguese exists so a reader looking at Maimonides' **Judeo-Arabic** can use
it to make sense of the Arabic — *tradução reversa*. So:

- **Translate the JA, not the English gloss and not the biblical Hebrew.** Track
  the Arabic clause order and diction closely enough to map most Portuguese words
  back to a JA word in the same segment.
- **Register:** high, formal, scholastic **European** Portuguese — dignified,
  lightly archaizing, enclitic pronouns (*seguiu-se-lhes*, *deixámos-te*,
  *se não acha*). Avoid Brazilian colloquialism and orthography. This is
  philosophical prose, not liturgy — precise, not ornate.
- **Preserve Maimonides' technical vocabulary and keep his transliterated terms**
  exactly where the English keeps them, in parentheses on first use:
  - מעני → **noção** (*maʿnā*) — never "significado" loosely
  - תג'סים → **corporalismo / corporeização**; תג'סים אלמחץ' → "corporalismo puro"
  - תנזיה → **exaltação / transcendência** (*tanzīh*)
  - אדראך עקלי → **apreensão intelectual** (*al-idrāk al-ʿaqlī*)
  - צורה נועיה → **forma específica**; צורה טביעיה → "forma natural";
    צורה צנאעיה → "forma artificial"
  - אסם משתרך → **nome equívoco** (*ism mushtarak*); אסם משכך → **nome anfibólico** (*mushakkak*)
  - אלעקל אלאלאהי → **o intelecto divino** (*al-ʿaql al-ilāhī*)
  - אדראך → **apreensão**; עקל → **intelecto**; ג'והר → **substância**;
    מוג'וד → **existente**; פלך אלקמר → "a esfera da lua"
- **Hebrew lemmas under discussion** (צלם, דמות, תאר, …) stay transliterated
  (*ṣelem, demut, to'ar*) — the chapter is *about* those words.
- **Scripture citations:** render the quoted verse in dignified Portuguese and
  keep the reference `(Gén 1:26)`, mirroring the English segment.
- **Do not** smooth toward a standard Portuguese Bible, paraphrase, or add words
  Maimonides did not write.

`data/moreh-bab1-portuguese.json` (I:1) is the **worked exemplar** — match its
voice and its treatment of terms.

---

## Sidecar shape

`data/<base>-portuguese.json`, keyed by `page_he`, arrays parallel to the
source page's `aligned[]` (or `paragraphs[]`). Index *i* is the Portuguese of
source segment *i*; use `null` (or omit the tail) for anything not yet done.

```json
{
  "_status": "draft",
  "_model": "claude",
  "pages": {
    "18": { "aligned": ["<pt of seg 0>", "<pt of seg 1>", "…"] },
    "19": { "aligned": ["…"] }
  }
}
```

`lib/morehPortuguese.ts` threads these onto the chapter at request time
(non-destructively); the reader shows them under a **"Português"** layer chip
(off by default, draft note beneath). Missing entries simply don't render, so
partial chapters are safe to ship.

---

## Arming the Routine (one-time, done by a human or by Claude on request)

Use the Claude Code Remote **Routine / cron trigger** so it fires fresh cloud
sessions on a schedule. Suggested cadence: **every 30 min** (steady, ~1–2
chapters/cycle → Part I in a day or two; whole corpus in ~1–2 weeks). Configure:

- **create_new_session_on_fire: true** — each firing starts clean in this repo's
  cloud environment.
- **prompt:** the *THE CYCLE* block above, verbatim.
- **cron:** `*/30 * * * *` (or hourly `0 * * * *` for a lighter footprint).

Claude can arm this on request via `create_trigger` (needs `list_environments`
to pick the environment id). To watch it: `list_triggers`; to pause/resume:
`update_trigger enabled=false/true`.

## Turning it off

- When `moreh_pt_status.py --next` prints nothing, the corpus is done — the
  cycle self-reports and stops advancing (safe to leave armed; it just no-ops).
- To stop early: `delete_trigger` (or `update_trigger enabled=false`).

## Checking progress by hand

```
python3 scripts/moreh_pt_status.py        # coverage table + next TODO
git log --oneline | grep 'Moreh Portuguese'   # the checkpoint trail
```

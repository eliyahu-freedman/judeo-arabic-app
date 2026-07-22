"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import { lookup, tokenizeJa, type Entry } from "@/lib/lookup";
import { lookupWorkNote, type WorkNote } from "@/lib/workNotes";
import { arabicToJa } from "@/lib/arabicToJa";
import { LAYER_LABELS, type ChapterXrefs, type XrefEntry } from "@/lib/mishnahXrefs";
import {
  resolveVerseAlignment,
  sliceByGroups,
  type AlignmentPair,
  type VerseAlignment,
} from "@/lib/alignment";
import {
  buildTermIndex,
  lookupTerm,
  type TermCard,
  type TermIndex,
  type TermRef,
} from "@/lib/terms";

export type AlignedSegment = {
  ja: string;
  en: string;
  /**
   * Optional elevated/liturgical Portuguese, authored against the JA (not the
   * English) for reverse-translatability. Threaded on from a `-portuguese.json`
   * sidecar by lib/morehPortuguese.ts; rendered under the "Português" layer.
   */
  pt?: string;
  /** Optional Hebrew crib — retained in data but no longer rendered. */
  he?: string;
  isHeader?: boolean;
  /** Sentence-internal JA↔EN phrase pairs that drive the hover highlighter. */
  pairs?: AlignmentPair[];
  /** Authoring hint: which key terms appear here. Marking uses the work-level index. */
  terms?: TermRef[];
  /** Footnote definitions for [^N] markers embedded in `en`. Key is the number as a string. */
  fn?: Record<string, string>;
};

export type WorkPage = {
  page_he: string;
  /** Free-flow JA paragraphs (used when a page has no aligned segments). */
  paragraphs?: string[];
  /** Free-flow English paragraphs paralleling `paragraphs`. */
  english_paragraphs?: string[];
  /** Free-flow Portuguese paragraphs paralleling `paragraphs`. */
  portuguese_paragraphs?: string[];
  aligned?: AlignedSegment[];
};

export type WorkData = {
  work: string;
  section: string;
  subtitle: string;
  author: string;
  english_translator: string;
  /** Optional custom header blurb; falls back to a generic one. */
  intro?: string;
  /**
   * Script of the primary-text column. Defaults to "hebrew" (Judeo-Arabic in
   * Hebrew letters). Set "arabic" for texts whose authoritative edition is in
   * Arabic script (e.g. Qirqisani's al-Anwar, ed. Nemoy) — swaps the JA column
   * to the Amiri Arabic font and relabels the layer chip.
   */
  script?: "hebrew" | "arabic";
  /**
   * Work id used to load this work's per-work Blau overlay (lib/workNotes.ts).
   * When set (e.g. "moreh"), a tapped word that Blau attests with a special
   * Judaeo-Arabic sense for THIS work shows an extra "Blau" note — scoped so it
   * never appears in other works' readers.
   */
  workId?: string;
  /** Work-level key-term cards, surfaced as footnotes in the gloss panel. */
  terms?: TermCard[];
  pages: WorkPage[];
};

/** Which segment+group is currently hovered, scoped by a per-segment key. */
type HoveredGroup = { segId: string; groupId: number; fraction: number | null };

/**
 * Optional multi-chapter navigation. When present, the reader renders an inline
 * chapter index (one chip per chapter, current highlighted) plus a prev/next
 * strip. Generic so any multi-part work can supply it; see
 * `app/advanced/rambam-moreh-nevukhim/chapters.ts`.
 */
export type ReaderNav = {
  /** Short series label, e.g. "Guide of the Perplexed · Part I". */
  label: string;
  /** Ordered chapters for the current part — used for prev/next. */
  chapters: { n: number; title: string; href: string }[];
  currentN: number;
  /** Exact href of the active chapter; required when `groups` is present. */
  activeHref?: string;
  /** Optional index/companion links (e.g. Atlas, Verses) shown above the chips. */
  aux?: { title: string; href: string; external?: boolean }[];
  /** When present, renders chapters as collapsible part groups instead of a flat list. */
  groups?: {
    label: string;
    defaultOpen?: boolean;
    chapters: { n: number; title: string; href: string }[];
  }[];
};

type Lang = "en" | "pt";

// In Portuguese mode the advanced reader becomes a clean translation reader:
// Portuguese fills the same block English does, the chrome is Portuguese, and the
// Judeo-Arabic learning apparatus (tap-to-define, term highlighting, Ibn Tibbon) is off.
const ADV_STRINGS: Record<Lang, {
  layers: string; jaHe: string; jaAr: string; draft: string;
}> = {
  en: {
    layers: "Layers", jaHe: "Judeo-Arabic", jaAr: "Arabic",
    draft: "English is a working draft — alignment is sentence-by-sentence.",
  },
  pt: {
    layers: "Camadas", jaHe: "Judaico-árabe", jaAr: "Árabe",
    draft: "A tradução portuguesa é um rascunho — em revisão.",
  },
};

export function AdvancedReader({
  data,
  nav,
  tibbon,
  tibbonLabel,
  xrefs,
}: {
  data: WorkData;
  nav?: ReaderNav;
  /** Optional chapter-level Hebrew translation shown as a layer. */
  tibbon?: string[];
  /** Label for the Hebrew layer chip (default: "Ibn Tibbon · Hebrew"). */
  tibbonLabel?: string;
  /** Optional mishnah-level cross-references for this chapter. */
  xrefs?: ChapterXrefs;
}) {
  const [showEnglish, setShowEnglish] = useState(true);
  const [showTibbon, setShowTibbon] = useState(false);
  // The Português | English switch only appears when the page actually carries
  // Portuguese from a sidecar (so it's absent on works without a PT translation).
  const hasPortuguese = useMemo(
    () =>
      data.pages.some(
        (p) =>
          p.aligned?.some((s) => !!s.pt) ||
          (p.portuguese_paragraphs?.some((s) => !!s) ?? false),
      ),
    [data.pages],
  );
  const hasTibbon = !!tibbon && tibbon.length > 0;
  const [activeToken, setActiveToken] = useState<string | null>(null);
  const [activeFootnote, setActiveFootnote] = useState<{ n: string; text: string } | null>(null);
  const [hoveredGroup, setHoveredGroup] = useState<HoveredGroup | null>(null);

  // Debounce mouseleave clears by a frame: moving between adjacent tokens of
  // the same group fires leave-then-enter and we don't want a flicker.
  const clearTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const updateHoveredGroup = useCallback((next: HoveredGroup | null) => {
    if (clearTimerRef.current) {
      clearTimeout(clearTimerRef.current);
      clearTimerRef.current = null;
    }
    if (next === null) {
      clearTimerRef.current = setTimeout(() => {
        setHoveredGroup(null);
        clearTimerRef.current = null;
      }, 40);
    } else {
      setHoveredGroup(next);
    }
  }, []);

  const [lang, setLangState] = useState<Lang>("en");
  const t = ADV_STRINGS[lang];
  const ptMode = lang === "pt";
  const applyLang = useCallback((l: Lang) => {
    setLangState(l);
    if (l === "pt") {
      setShowEnglish(true); // "translation" toggle now governs the Portuguese block
      setShowTibbon(false);
      setActiveToken(null);
      setActiveFootnote(null);
    }
  }, []);
  // Shared language preference across the tafsir + advanced readers.
  useEffect(() => {
    const saved =
      typeof window !== "undefined"
        ? window.localStorage.getItem("reader-lang")
        : null;
    if (saved === "pt" && hasPortuguese) applyLang("pt");
  }, [applyLang, hasPortuguese]);
  const setLang = (l: Lang) => {
    applyLang(l);
    if (typeof window !== "undefined")
      window.localStorage.setItem("reader-lang", l);
  };

  const jaFont = data.script === "arabic" ? "font-arabic" : "font-hebrew";
  const termIndex = useMemo(() => buildTermIndex(data.terms), [data.terms]);
  const emptyTermIndex = useMemo(() => buildTermIndex(undefined), []);
  const activeTermIndex = ptMode ? emptyTermIndex : termIndex;
  // For Arabic-script works (Qirqisani's al-Anwar) the dictionary + Blau overlay
  // are Hebrew-letter-keyed, so convert the tapped Arabic token to its
  // Judaeo-Arabic form first. Key terms stay matched on the original token —
  // each work's `terms` are keyed in that work's own script.
  const queryToken =
    activeToken && data.script === "arabic"
      ? arabicToJa(activeToken)
      : activeToken;
  const activeEntries: Entry[] = queryToken ? lookup(queryToken) : [];
  const activeTerm: TermCard | null = activeToken
    ? lookupTerm(termIndex, activeToken)
    : null;
  const activeWorkNote: WorkNote | null = lookupWorkNote(data.workId, queryToken);

  return (
    <div className="max-w-3xl mx-auto px-6 py-10 pb-44">
      <header className="mb-10">
        {hasPortuguese && (
          <div className="mb-4 flex items-center gap-2 text-xs">
            {(["pt", "en"] as Lang[]).map((l, i) => (
              <span key={l} className="flex items-center gap-2">
                {i > 0 && <span className="text-ink/20">|</span>}
                <button
                  type="button"
                  onClick={() => setLang(l)}
                  aria-pressed={lang === l}
                  className={
                    lang === l
                      ? "text-wine font-medium"
                      : "text-ink/40 hover:text-wine transition-colors"
                  }
                >
                  {l === "pt" ? "Português" : "English"}
                </button>
              </span>
            ))}
          </div>
        )}
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Stage 3 · {data.author}
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          {data.work}: <span className="text-wine italic">{data.section}</span>
        </h1>
        <p className="mt-3 text-base text-muted italic">{data.subtitle}</p>
        <p className="mt-4 text-base text-ink/70 leading-relaxed max-w-xl" lang={lang}>
          {ptMode
            ? `${data.work} no judaico-árabe original de ${data.author}, com uma tradução portuguesa (rascunho, em revisão) sob cada trecho.`
            : (data.intro ??
              `${data.work} in the original Judeo-Arabic, with a working English translation by ${data.english_translator}. Hover a phrase to see its English light up; tap any word for a gloss.`)}
        </p>
      </header>

      {nav && <ChapterNav nav={nav} />}

      <div className="sticky top-0 z-10 bg-parchment/90 backdrop-blur supports-[backdrop-filter]:bg-parchment/70 -mx-6 px-6 py-3 border-y border-ink/10 flex flex-wrap items-center gap-2 text-sm">
        <span className="text-[10px] uppercase tracking-[0.25em] text-muted mr-1">
          {t.layers}
        </span>
        <ToggleChip on disabled label={data.script === "arabic" ? t.jaAr : t.jaHe} />
        <ToggleChip
          on={showEnglish}
          onClick={() => setShowEnglish((x) => !x)}
          label={ptMode ? "Português" : "English"}
        />
        {!ptMode && hasTibbon && (
          <ToggleChip
            on={showTibbon}
            onClick={() => setShowTibbon((x) => !x)}
            label={tibbonLabel ?? "Ibn Tibbon"}
          />
        )}
      </div>

      <div
        className={
          hasTibbon && showTibbon
            ? "lg:grid lg:grid-cols-2 lg:gap-8 lg:items-start"
            : undefined
        }
      >
      <article className="mt-10 space-y-10">
        {data.pages.map((page) => (
          <section key={page.page_he}>
            <div className="flex items-center gap-3 mb-5">
              <span className="text-[10px] uppercase tracking-[0.3em] text-muted">
                Page
              </span>
              <span className="font-hebrew text-base text-muted" dir="rtl">
                {page.page_he}
              </span>
              <span className="flex-1 h-px bg-ink/10" />
            </div>
            <div className="rounded-md bg-page border border-ink/10 p-7">
              {page.aligned && page.aligned.length > 0 ? (
                <AlignedSegments
                  pageKey={page.page_he}
                  segments={page.aligned}
                  jaFont={jaFont}
                  showEnglish={showEnglish}
                  ptMode={ptMode}
                  activeToken={ptMode ? null : activeToken}
                  onTap={ptMode ? () => {} : (token) => { setActiveFootnote(null); setActiveToken(token); }}
                  termIndex={activeTermIndex}
                  hoveredGroup={hoveredGroup}
                  onHoverGroup={updateHoveredGroup}
                  chapterXrefs={xrefs}
                  onFnClick={(n, text) => { setActiveToken(null); setActiveFootnote({ n, text }); }}
                />
              ) : (
                <>
                  <div dir="rtl" className="space-y-5">
                    {(page.paragraphs ?? []).map((para, i) => (
                      <p
                        key={i}
                        className={`${jaFont} ja-text text-xl text-ink/90 leading-loose`}
                      >
                        <JaText
                          text={para}
                          activeToken={ptMode ? null : activeToken}
                          onTap={ptMode ? () => {} : setActiveToken}
                          termIndex={activeTermIndex}
                          alignment={null}
                          onHoverGroup={() => {}}
                        />
                      </p>
                    ))}
                  </div>
                  {showEnglish &&
                    (() => {
                      // Portuguese fills the same translation block English does.
                      const paras = ptMode
                        ? page.portuguese_paragraphs
                        : page.english_paragraphs;
                      const has = paras?.some((s) => !!s) ?? false;
                      return has ? (
                        <div
                          dir="ltr"
                          lang={ptMode ? "pt" : undefined}
                          className="mt-5 pt-5 border-t border-ink/10 space-y-3"
                        >
                          {paras!.map((p, j) =>
                            p ? (
                              <p
                                key={j}
                                className="text-[15px] text-ink/80 leading-relaxed"
                              >
                                {p}
                              </p>
                            ) : null,
                          )}
                        </div>
                      ) : null;
                    })()}
                </>
              )}
            </div>
          </section>
        ))}
      </article>
        {hasTibbon && showTibbon && (
          <aside className="mt-10">
            <div className="rounded-md bg-page border border-ink/10 p-7">
              <h2 className="text-[10px] uppercase tracking-[0.3em] text-muted mb-4 pb-1 border-b border-ink/10">
                {tibbonLabel ?? "Ibn Tibbon · Hebrew"}{" "}
                {!tibbonLabel && (
                  <span className="normal-case tracking-normal text-ink/40">
                    (public domain, via Sefaria)
                  </span>
                )}
              </h2>
              <div
                dir="rtl"
                className="font-hebrew text-lg leading-loose text-ink/90 space-y-3"
              >
                {tibbon!.map((s, i) => (
                  <p key={i}>{s}</p>
                ))}
              </div>
              <p className="mt-4 text-[10px] uppercase tracking-[0.25em] text-muted italic">
                Chapter-level — not phrase-aligned to the original.
              </p>
            </div>
          </aside>
        )}
      </div>

      {showEnglish && (
        <p className="mt-6 text-xs uppercase tracking-[0.25em] text-muted text-center italic">
          {t.draft}
        </p>
      )}

      {!ptMode && activeToken && (
        <GlossPanel
          token={activeToken}
          jaFont={jaFont}
          entries={activeEntries}
          term={activeTerm}
          workNote={activeWorkNote}
          onClose={() => setActiveToken(null)}
        />
      )}
      {activeFootnote && (
        <FootnotePanel
          n={activeFootnote.n}
          text={activeFootnote.text}
          onClose={() => setActiveFootnote(null)}
        />
      )}
    </div>
  );
}

/** Inline chapter index + prev/next strip for multi-chapter works. */
function ChapterNav({ nav }: { nav: ReaderNav }) {
  const idx = nav.chapters.findIndex((c) => c.n === nav.currentN);
  const prev = idx > 0 ? nav.chapters[idx - 1] : null;
  const next =
    idx >= 0 && idx < nav.chapters.length - 1 ? nav.chapters[idx + 1] : null;

  const renderChip = (c: { n: number; title: string; href: string }) => {
    const isActive = nav.groups
      ? c.href === nav.activeHref
      : c.n === nav.currentN;
    return isActive ? (
      <span
        key={c.href}
        aria-current="page"
        className="rounded-full px-3 py-1 text-sm bg-wine-100 text-wine-700 border border-wine-200"
      >
        {c.title}
      </span>
    ) : (
      <Link
        key={c.href}
        href={c.href}
        className="rounded-full px-3 py-1 text-sm border border-ink/15 text-ink/70 hover:border-wine/40 hover:text-wine transition-colors"
      >
        {c.title}
      </Link>
    );
  };

  return (
    <nav className="mb-10" aria-label="Chapters">
      <p className="text-[10px] uppercase tracking-[0.3em] text-muted mb-2">
        {nav.label}
      </p>
      {nav.aux && nav.aux.length > 0 && (
        <div className="flex flex-wrap gap-3 mb-3 text-sm">
          {nav.aux.map((a) =>
            a.external ? (
              <a
                key={a.href}
                href={a.href}
                target="_blank"
                rel="noopener noreferrer"
                className="text-wine hover:underline underline-offset-2"
              >
                {a.title}
              </a>
            ) : (
              <Link
                key={a.href}
                href={a.href}
                className="text-wine hover:underline underline-offset-2"
              >
                {a.title}
              </Link>
            ),
          )}
        </div>
      )}
      {nav.groups ? (
        <div className="space-y-1">
          {nav.groups.map((g) => (
            <details
              key={g.label}
              open={g.defaultOpen || undefined}
              className="group/part"
            >
              <summary className="cursor-pointer list-none flex items-center gap-1.5 select-none py-1 text-sm font-medium text-ink/60 hover:text-wine">
                <span className="inline-block text-xs transition-transform duration-150 group-open/part:rotate-90">
                  ▶
                </span>
                {g.label}
              </summary>
              <div className="flex flex-wrap gap-2 pt-2 pb-3">
                {g.chapters.map(renderChip)}
              </div>
            </details>
          ))}
        </div>
      ) : (
        <div className="flex flex-wrap gap-2">
          {nav.chapters.map(renderChip)}
        </div>
      )}
      {(prev || next) && (
        <div className="mt-3 flex justify-between gap-4 text-sm">
          {prev ? (
            <Link href={prev.href} className="text-wine hover:underline">
              ← {prev.title}
            </Link>
          ) : (
            <span />
          )}
          {next ? (
            <Link href={next.href} className="text-wine hover:underline">
              {next.title} →
            </Link>
          ) : (
            <span />
          )}
        </div>
      )}
    </nav>
  );
}

// Back-compat alias while the Bahya page migrates to the new name.
export const BahyaReader = AdvancedReader;
export type BahyaData = WorkData;
export type BahyaPage = WorkPage;

function AlignedSegments({
  pageKey,
  segments,
  jaFont,
  showEnglish,
  ptMode,
  activeToken,
  onTap,
  termIndex,
  hoveredGroup,
  onHoverGroup,
  chapterXrefs,
  onFnClick,
}: {
  pageKey: string;
  segments: AlignedSegment[];
  jaFont: string;
  showEnglish: boolean;
  ptMode: boolean;
  activeToken: string | null;
  onTap: (t: string) => void;
  termIndex: TermIndex;
  hoveredGroup: HoveredGroup | null;
  onHoverGroup: (g: HoveredGroup | null) => void;
  chapterXrefs?: ChapterXrefs;
  onFnClick?: (n: string, text: string) => void;
}) {
  let mishnahCount = 0;
  return (
    <div className="space-y-7">
      <p className="text-[10px] uppercase tracking-[0.3em] text-muted -mt-1 mb-1">
        Aligned sentence by sentence
      </p>
      {segments.map((seg, i) => {
        if (seg.isHeader) mishnahCount++;
        const segXrefs = seg.isHeader ? (chapterXrefs?.[`m${mishnahCount}`] ?? []) : [];
        const segId = `${pageKey}-${i}`;
        const alignment: VerseAlignment | null = seg.pairs?.length
          ? resolveVerseAlignment("", seg.ja, seg.en, seg.pairs)
          : null;
        const hoveredGroupId =
          hoveredGroup?.segId === segId ? hoveredGroup.groupId : null;
        const hoverFraction =
          hoveredGroup?.segId === segId ? hoveredGroup.fraction : undefined;
        const setGroupFromJa = (info: { groupId: number; fraction: number } | null) =>
          onHoverGroup(info === null ? null : { segId, groupId: info.groupId, fraction: info.fraction });
        const setGroupFromEn = (g: number | null) =>
          onHoverGroup(g === null ? null : { segId, groupId: g, fraction: null });
        return (
          <div key={i} className={i > 0 ? "pt-6 border-t border-ink/5" : undefined}>
            <p
              dir="rtl"
              className={`${jaFont} ja-text leading-loose text-ink/90 ${
                seg.isHeader ? "text-2xl text-wine" : "text-xl"
              }`}
            >
              <JaText
                text={seg.ja}
                activeToken={activeToken}
                onTap={onTap}
                termIndex={termIndex}
                alignment={alignment}
                onHoverGroup={setGroupFromJa}
              />
            </p>
            {showEnglish && !ptMode && seg.en && (
              <p
                dir="ltr"
                className="text-[15px] text-ink/80 leading-relaxed mt-2"
              >
                <EnglishText
                  text={seg.en}
                  alignment={alignment}
                  hoveredGroupId={hoveredGroupId}
                  hoverFraction={hoverFraction}
                  onHoverGroup={setGroupFromEn}
                  onFnClick={onFnClick ? (n) => {
                    const text = seg.fn?.[n] ?? "";
                    if (text) onFnClick(n, text);
                  } : undefined}
                />
              </p>
            )}
            {/* Portuguese fills the same block English does (same styling/position). */}
            {showEnglish && ptMode && seg.pt && (
              <p
                dir="ltr"
                lang="pt"
                className="text-[15px] text-ink/80 leading-relaxed mt-2"
              >
                {seg.pt}
              </p>
            )}
            {segXrefs.length > 0 && <SourcesPanel entries={segXrefs} />}
          </div>
        );
      })}
    </div>
  );
}

function SourcesPanel({ entries }: { entries: XrefEntry[] }) {
  return (
    <details className="mt-3 group/xref">
      <summary className="cursor-pointer list-none flex items-center gap-1.5 select-none text-[11px] uppercase tracking-[0.2em] text-wine/60 hover:text-wine transition-colors">
        <span className="inline-block text-[10px] transition-transform duration-150 group-open/xref:rotate-90">
          ▶
        </span>
        Sources · {entries.length}
      </summary>
      <div className="mt-3 space-y-4 border-l-2 border-wine/20 pl-4">
        {entries.map((e, i) => (
          <div key={i}>
            <div className="flex items-baseline gap-2 flex-wrap mb-1">
              <span className="text-[10px] uppercase tracking-[0.2em] text-muted">
                {LAYER_LABELS[e.layer]}
              </span>
              {e.sefaria_ref ? (
                <a
                  href={`https://www.sefaria.org/${encodeURIComponent(e.sefaria_ref).replace(/%20/g, "_")}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-sm text-wine hover:underline underline-offset-2"
                >
                  {e.source} · {e.ref}
                </a>
              ) : (
                <span className="text-sm text-ink/70">
                  {e.source} · {e.ref}
                </span>
              )}
            </div>
            <p className="text-[13px] text-ink/70 leading-relaxed">{e.note}</p>
          </div>
        ))}
      </div>
    </details>
  );
}

function JaText({
  text,
  activeToken,
  onTap,
  termIndex,
  alignment,
  onHoverGroup,
}: {
  text: string;
  activeToken: string | null;
  onTap: (t: string) => void;
  termIndex: TermIndex;
  alignment: VerseAlignment | null;
  onHoverGroup: (info: { groupId: number; fraction: number } | null) => void;
}) {
  const [hoveredIdx, setHoveredIdx] = useState<number | null>(null);
  const tokens = tokenizeJa(text);
  // Precompute each token's char range up front so the render map below
  // doesn't mutate a running offset (react-hooks/immutability).
  const starts: number[] = [];
  let acc = 0;
  for (const t of tokens) {
    starts.push(acc);
    acc += t.text.length;
  }
  return (
    <>
      {tokens.map((t, i) => {
        const tokenStart = starts[i];
        const tokenEnd = tokenStart + t.text.length;
        const jaSpan = alignment
          ? alignment.ja.find((s) => s.start < tokenEnd && s.end > tokenStart) ?? null
          : null;
        const groupForRange = jaSpan?.groupId ?? null;
        const inHover = i === hoveredIdx && groupForRange !== null;
        if (t.kind === "sep") {
          return <span key={i}>{t.text}</span>;
        }
        const isActive = activeToken === t.text;
        const isTerm = lookupTerm(termIndex, t.text) !== null;
        return (
          <button
            key={i}
            type="button"
            onClick={() => onTap(t.text)}
            onMouseEnter={() => {
              setHoveredIdx(i);
              if (groupForRange !== null && jaSpan) {
                const mid = (tokenStart + tokenEnd) / 2;
                const fraction = Math.max(0, Math.min(1,
                  (mid - jaSpan.start) / (jaSpan.end - jaSpan.start)
                ));
                onHoverGroup({ groupId: groupForRange, fraction });
              }
            }}
            onMouseLeave={() => {
              setHoveredIdx(null);
              onHoverGroup(null);
            }}
            title={isTerm ? "Key term — see panel" : undefined}
            className={`inline cursor-pointer rounded-sm transition-colors px-0.5 -mx-0.5
              ${
                isActive
                  ? "bg-wine-100 text-wine-700"
                  : inHover
                    ? "bg-amber-100 text-ink ring-1 ring-amber-300/60"
                    : "hover:bg-wine-50"
              }
              ${
                isTerm && !isActive
                  ? "underline decoration-dotted decoration-wine/60 decoration-1 underline-offset-[6px]"
                  : ""
              }`}
          >
            {t.text}
          </button>
        );
      })}
    </>
  );
}

function proportionalWord(text: string, fraction: number) {
  const charTarget = Math.round(fraction * (text.length - 1));
  let wStart = charTarget, wEnd = charTarget;
  while (wStart > 0 && text[wStart - 1] !== " ") wStart--;
  while (wEnd < text.length && text[wEnd] !== " ") wEnd++;
  return (
    <>
      {wStart > 0 && <span>{text.slice(0, wStart)}</span>}
      <span className="bg-amber-100 ring-1 ring-amber-300/60 text-ink rounded-sm">
        {text.slice(wStart, wEnd)}
      </span>
      {wEnd < text.length && <span>{text.slice(wEnd)}</span>}
    </>
  );
}

function renderWithFnMarkers(
  text: string,
  onFnClick: ((n: string) => void) | undefined,
): React.ReactNode {
  if (!onFnClick || !text.includes("[^")) return text;
  const parts = text.split(/(\[\^\d+\])/g);
  if (parts.length === 1) return text;
  return (
    <>
      {parts.map((part, i) => {
        const m = part.match(/^\[\^(\d+)\]$/);
        if (m) {
          return (
            <sup key={i}>
              <button
                type="button"
                onClick={(e) => { e.stopPropagation(); onFnClick(m[1]); }}
                className="text-wine text-[10px] font-medium hover:underline underline-offset-2 leading-none cursor-pointer"
              >
                {m[1]}
              </button>
            </sup>
          );
        }
        return part ? <span key={i}>{part}</span> : null;
      })}
    </>
  );
}

function EnglishText({
  text,
  alignment,
  hoveredGroupId,
  hoverFraction,
  onHoverGroup,
  onFnClick,
}: {
  text: string;
  alignment: VerseAlignment | null;
  hoveredGroupId: number | null;
  hoverFraction: number | null | undefined;
  onHoverGroup: (groupId: number | null) => void;
  onFnClick?: (n: string) => void;
}) {
  if (!alignment || alignment.en.length === 0) {
    return <>{renderWithFnMarkers(text, onFnClick)}</>;
  }
  const runs = sliceByGroups(text, alignment.en);
  return (
    <>
      {runs.map((r, i) => {
        if (r.groupId === null) {
          return <span key={i}>{renderWithFnMarkers(r.text, onFnClick)}</span>;
        }
        const inHover = r.groupId === hoveredGroupId;
        const showProportional =
          inHover && typeof hoverFraction === "number" && r.text.includes(" ");
        return (
          <span
            key={i}
            onMouseEnter={() => onHoverGroup(r.groupId)}
            onMouseLeave={() => onHoverGroup(null)}
            className={`rounded-sm transition-colors cursor-default ${
              inHover && !showProportional ? "bg-amber-100 ring-1 ring-amber-300/60 text-ink" : ""
            }`}
          >
            {showProportional
              ? proportionalWord(r.text, hoverFraction!)
              : renderWithFnMarkers(r.text, onFnClick)}
          </span>
        );
      })}
    </>
  );
}

function GlossPanel({
  token,
  jaFont,
  entries,
  term,
  workNote,
  onClose,
}: {
  token: string;
  jaFont: string;
  entries: Entry[];
  term: TermCard | null;
  workNote: WorkNote | null;
  onClose: () => void;
}) {
  // The Advanced reader (Bahya, Kuzari, Rambam Moreh, Qirqisani, etc.) must
  // NOT surface Saadia-specific dictionary entries — those have
  // scope:"saadia" because their primary gloss is itself a Saadia coinage
  // (e.g. גלד glossed "firmament" rather than the classical "skin/hide").
  // The Saadia-attribution note field (`saadia_note`) is likewise omitted
  // below: it only renders inside `/tafsir`.
  const visibleEntries = entries.filter((e) => e.scope !== "saadia");
  return (
    <div className="fixed bottom-0 inset-x-0 z-20 bg-page border-t border-wine/20 shadow-[0_-8px_24px_-12px_rgba(114,47,55,0.2)]">
      <div className="max-w-3xl mx-auto px-6 py-5">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-baseline gap-4">
            <span className={`${jaFont} text-3xl text-ink`} dir="rtl">
              {token}
            </span>
            <span className="text-[10px] uppercase tracking-[0.3em] text-muted">
              Tapped word
            </span>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="text-ink/60 hover:text-wine text-2xl leading-none w-8 h-8 flex items-center justify-center rounded-full hover:bg-wine-50 transition-colors"
            aria-label="Close"
          >
            ×
          </button>
        </div>
        {term && <TermBanner term={term} />}
        {workNote && <WorkNoteBanner note={workNote} />}
        {visibleEntries.length === 0 ? (
          <p className="text-sm text-muted mt-2 italic">
            {term
              ? "See the key-term note above. (Not in the starter dictionary.)"
              : "No entry yet in the starter dictionary. (The starter is Bereshit-1-oriented; coverage expands as Lane entries land.)"}
          </p>
        ) : (
          <ul className="space-y-4 mt-2">
            {visibleEntries.map((e) => (
              <li key={e.id} className="border-l-2 border-wine/40 pl-4">
                <div className="flex items-baseline gap-3 flex-wrap">
                  <span className="font-hebrew text-xl text-ink" dir="rtl">
                    {e.lemma_ja}
                  </span>
                  <span className="font-arabic text-lg text-ink/70" dir="rtl">
                    {e.lemma_ar}
                  </span>
                  <span className="text-xs text-muted font-mono">
                    √{e.root}
                  </span>
                  <span className="text-xs text-muted italic">{e.pos}</span>
                </div>
                <p className="text-[15px] text-ink mt-1.5">{e.gloss_en}</p>
                <p
                  className="font-hebrew text-base text-muted mt-0.5"
                  dir="rtl"
                >
                  {e.gloss_he}
                </p>
                {e.notes && (
                  <p className="text-[13px] text-muted mt-2 leading-relaxed italic">
                    {e.notes}
                  </p>
                )}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

function TermBanner({ term }: { term: TermCard }) {
  return (
    <div className="mb-4 rounded-md border border-wine/30 bg-wine-50/60 px-4 py-3">
      <div className="flex items-baseline gap-3 mb-2 flex-wrap">
        <span className="text-[10px] uppercase tracking-[0.3em] text-wine">
          Key term
        </span>
        {term.translit && (
          <span className="text-sm text-ink/80 italic">{term.translit}</span>
        )}
        {term.ar && (
          <span className="font-arabic text-lg text-ink/70" dir="rtl">
            {term.ar}
          </span>
        )}
      </div>
      <p className="text-[15px] text-ink">{term.gloss}</p>
      {term.note && (
        <p className="text-[12.5px] text-muted italic mt-2 leading-relaxed">
          {term.note}
        </p>
      )}
      {term.refs && term.refs.length > 0 && (
        <p className="mt-3 pt-2 border-t border-wine/15 text-[11px] leading-relaxed text-ink/55">
          <span className="uppercase tracking-wider text-ink/40 mr-1">
            Sources:
          </span>
          {term.refs.join(" · ")}
        </p>
      )}
    </div>
  );
}

function WorkNoteBanner({ note }: { note: WorkNote }) {
  return (
    <div className="mb-4 rounded-md border border-ink/20 bg-ink/[0.03] px-4 py-3">
      <div className="flex items-baseline gap-3 mb-2 flex-wrap">
        <span className="text-[10px] uppercase tracking-[0.3em] text-ink/55">
          In this work · Blau
        </span>
        {note.lemma_ar && (
          <span className="font-arabic text-lg text-ink/70" dir="rtl">
            {note.lemma_ar}
          </span>
        )}
        {note.root && note.root !== "—" && (
          <span className="text-xs text-muted font-mono">√{note.root}</span>
        )}
      </div>
      <p className="text-[14px] text-ink leading-relaxed">{note.blau_sense_en}</p>
      {note.blau_sense_he && (
        <p className="font-hebrew text-base text-muted mt-0.5" dir="rtl">
          {note.blau_sense_he}
        </p>
      )}
      {note.attested_in && (
        <p className="mt-3 pt-2 border-t border-ink/10 text-[11px] leading-relaxed text-ink/55">
          <span className="uppercase tracking-wider text-ink/40 mr-1">Source:</span>
          {note.attested_in}
        </p>
      )}
    </div>
  );
}

function FootnotePanel({
  n,
  text,
  onClose,
}: {
  n: string;
  text: string;
  onClose: () => void;
}) {
  return (
    <div className="fixed bottom-0 inset-x-0 z-20 bg-page border-t border-wine/20 shadow-[0_-8px_24px_-12px_rgba(114,47,55,0.2)]">
      <div className="max-w-3xl mx-auto px-6 py-5">
        <div className="flex items-center justify-between mb-3">
          <span className="text-[10px] uppercase tracking-[0.3em] text-muted">
            Note {n}
          </span>
          <button
            type="button"
            onClick={onClose}
            className="text-ink/60 hover:text-wine text-2xl leading-none w-8 h-8 flex items-center justify-center rounded-full hover:bg-wine-50 transition-colors"
            aria-label="Close"
          >
            ×
          </button>
        </div>
        <p className="text-[15px] text-ink/80 leading-relaxed">{text}</p>
      </div>
    </div>
  );
}

function ToggleChip({
  on,
  onClick,
  label,
  disabled,
  hint,
}: {
  on: boolean;
  onClick?: () => void;
  label: string;
  disabled?: boolean;
  hint?: string;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      title={hint}
      className={`px-3 py-1 rounded-full border text-xs uppercase tracking-wider transition-all
        ${
          on
            ? "bg-wine text-page border-wine"
            : "bg-page text-ink/70 border-ink/15"
        }
        ${
          disabled
            ? "opacity-40 cursor-not-allowed"
            : "hover:border-wine/50 hover:text-wine"
        }`}
    >
      {label}
      {hint && <span className="ml-1 opacity-70">({hint})</span>}
    </button>
  );
}

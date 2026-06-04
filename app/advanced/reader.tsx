"use client";

import { useCallback, useMemo, useRef, useState } from "react";
import { lookup, tokenizeJa, type Entry } from "@/lib/lookup";
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
  /** Optional Hebrew crib — retained in data but no longer rendered. */
  he?: string;
  isHeader?: boolean;
  /** Sentence-internal JA↔EN phrase pairs that drive the hover highlighter. */
  pairs?: AlignmentPair[];
  /** Authoring hint: which key terms appear here. Marking uses the work-level index. */
  terms?: TermRef[];
};

export type WorkPage = {
  page_he: string;
  /** Free-flow JA paragraphs (used when a page has no aligned segments). */
  paragraphs?: string[];
  /** Free-flow English paragraphs paralleling `paragraphs`. */
  english_paragraphs?: string[];
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
  /** Work-level key-term cards, surfaced as footnotes in the gloss panel. */
  terms?: TermCard[];
  pages: WorkPage[];
};

/** Which segment+group is currently hovered, scoped by a per-segment key. */
type HoveredGroup = { segId: string; groupId: number };

export function AdvancedReader({ data }: { data: WorkData }) {
  const [showEnglish, setShowEnglish] = useState(true);
  const [activeToken, setActiveToken] = useState<string | null>(null);
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

  const jaFont = data.script === "arabic" ? "font-arabic" : "font-hebrew";
  const termIndex = useMemo(() => buildTermIndex(data.terms), [data.terms]);
  const activeEntries: Entry[] = activeToken ? lookup(activeToken) : [];
  const activeTerm: TermCard | null = activeToken
    ? lookupTerm(termIndex, activeToken)
    : null;

  return (
    <div className="max-w-3xl mx-auto px-6 py-10 pb-44">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Stage 3 · {data.author}
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          {data.work}: <span className="text-wine italic">{data.section}</span>
        </h1>
        <p className="mt-3 text-base text-muted italic">{data.subtitle}</p>
        <p className="mt-4 text-base text-ink/70 leading-relaxed max-w-xl">
          {data.intro ??
            `${data.work} in the original Judeo-Arabic, with a working English translation by ${data.english_translator}. Hover a phrase to see its English light up; tap any word for a gloss.`}
        </p>
      </header>

      <div className="sticky top-0 z-10 bg-parchment/90 backdrop-blur supports-[backdrop-filter]:bg-parchment/70 -mx-6 px-6 py-3 border-y border-ink/10 flex flex-wrap items-center gap-2 text-sm">
        <span className="text-[10px] uppercase tracking-[0.25em] text-muted mr-1">
          Layers
        </span>
        <ToggleChip on disabled label={data.script === "arabic" ? "Arabic" : "Judeo-Arabic"} />
        <ToggleChip
          on={showEnglish}
          onClick={() => setShowEnglish((x) => !x)}
          label="English"
        />
      </div>

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
                  activeToken={activeToken}
                  onTap={setActiveToken}
                  termIndex={termIndex}
                  hoveredGroup={hoveredGroup}
                  onHoverGroup={updateHoveredGroup}
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
                          activeToken={activeToken}
                          onTap={setActiveToken}
                          termIndex={termIndex}
                          alignment={null}
                          hoveredGroupId={null}
                          onHoverGroup={() => {}}
                        />
                      </p>
                    ))}
                  </div>
                  {showEnglish &&
                    (page.english_paragraphs?.length ?? 0) > 0 && (
                      <div
                        dir="ltr"
                        className="mt-5 pt-5 border-t border-ink/10 space-y-3"
                      >
                        {page.english_paragraphs!.map((p, j) => (
                          <p
                            key={j}
                            className="text-[15px] text-ink/80 leading-relaxed"
                          >
                            {p}
                          </p>
                        ))}
                      </div>
                    )}
                </>
              )}
            </div>
          </section>
        ))}
      </article>

      {showEnglish && (
        <p className="mt-6 text-xs uppercase tracking-[0.25em] text-muted text-center italic">
          English is a working draft — alignment is sentence-by-sentence.
        </p>
      )}

      {activeToken && (
        <GlossPanel
          token={activeToken}
          jaFont={jaFont}
          entries={activeEntries}
          term={activeTerm}
          onClose={() => setActiveToken(null)}
        />
      )}
    </div>
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
  activeToken,
  onTap,
  termIndex,
  hoveredGroup,
  onHoverGroup,
}: {
  pageKey: string;
  segments: AlignedSegment[];
  jaFont: string;
  showEnglish: boolean;
  activeToken: string | null;
  onTap: (t: string) => void;
  termIndex: TermIndex;
  hoveredGroup: HoveredGroup | null;
  onHoverGroup: (g: HoveredGroup | null) => void;
}) {
  return (
    <div className="space-y-7">
      <p className="text-[10px] uppercase tracking-[0.3em] text-muted -mt-1 mb-1">
        Aligned sentence by sentence
      </p>
      {segments.map((seg, i) => {
        const segId = `${pageKey}-${i}`;
        const alignment: VerseAlignment | null = seg.pairs?.length
          ? resolveVerseAlignment("", seg.ja, seg.en, seg.pairs)
          : null;
        const hoveredGroupId =
          hoveredGroup?.segId === segId ? hoveredGroup.groupId : null;
        const setGroup = (g: number | null) =>
          onHoverGroup(g === null ? null : { segId, groupId: g });
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
                hoveredGroupId={hoveredGroupId}
                onHoverGroup={setGroup}
              />
            </p>
            {showEnglish && seg.en && (
              <p
                dir="ltr"
                className="text-[15px] text-ink/80 leading-relaxed mt-2"
              >
                <EnglishText
                  text={seg.en}
                  alignment={alignment}
                  hoveredGroupId={hoveredGroupId}
                  onHoverGroup={setGroup}
                />
              </p>
            )}
          </div>
        );
      })}
    </div>
  );
}

function JaText({
  text,
  activeToken,
  onTap,
  termIndex,
  alignment,
  hoveredGroupId,
  onHoverGroup,
}: {
  text: string;
  activeToken: string | null;
  onTap: (t: string) => void;
  termIndex: TermIndex;
  alignment: VerseAlignment | null;
  hoveredGroupId: number | null;
  onHoverGroup: (groupId: number | null) => void;
}) {
  const tokens = tokenizeJa(text);
  let charIdx = 0;
  return (
    <>
      {tokens.map((t, i) => {
        const tokenStart = charIdx;
        const tokenEnd = charIdx + t.text.length;
        charIdx = tokenEnd;
        const groupForRange = alignment
          ? alignment.ja.find((s) => s.start <= tokenStart && s.end >= tokenEnd)
              ?.groupId ?? null
          : null;
        const inHover =
          groupForRange !== null && groupForRange === hoveredGroupId;
        if (t.kind === "sep") {
          return (
            <span key={i} className={inHover ? "bg-amber-100/70" : undefined}>
              {t.text}
            </span>
          );
        }
        const isActive = activeToken === t.text;
        const isTerm = lookupTerm(termIndex, t.text) !== null;
        const groupHandlers =
          groupForRange !== null
            ? {
                onMouseEnter: () => onHoverGroup(groupForRange),
                onMouseLeave: () => onHoverGroup(null),
              }
            : {};
        return (
          <button
            key={i}
            type="button"
            onClick={() => onTap(t.text)}
            {...groupHandlers}
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

function EnglishText({
  text,
  alignment,
  hoveredGroupId,
  onHoverGroup,
}: {
  text: string;
  alignment: VerseAlignment | null;
  hoveredGroupId: number | null;
  onHoverGroup: (groupId: number | null) => void;
}) {
  if (!alignment || alignment.en.length === 0) {
    return <>{text}</>;
  }
  const runs = sliceByGroups(text, alignment.en);
  return (
    <>
      {runs.map((r, i) => {
        if (r.groupId === null) return <span key={i}>{r.text}</span>;
        const inHover = r.groupId === hoveredGroupId;
        return (
          <span
            key={i}
            onMouseEnter={() => onHoverGroup(r.groupId)}
            onMouseLeave={() => onHoverGroup(null)}
            className={`rounded-sm transition-colors cursor-default ${
              inHover ? "bg-amber-100 ring-1 ring-amber-300/60 text-ink" : ""
            }`}
          >
            {r.text}
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
  onClose,
}: {
  token: string;
  jaFont: string;
  entries: Entry[];
  term: TermCard | null;
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

"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { lookup, tokenizeJa, type Entry } from "@/lib/lookup";
import { sliceByGroups, type VerseAlignment } from "@/lib/alignment";
import {
  divergenceTier,
  lookupDivergence,
  type DivergenceEntry,
  type DivergenceTier,
} from "@/lib/divergence";
import {
  uniqueVerses,
  useCorpus,
  variantBreakdown,
  type CorpusEntry,
} from "@/lib/corpus";
import { useWordStates, type WordState } from "@/lib/wordState";
import {
  ALIYAH_LABELS,
  BOOK_DISPLAY,
  BOOK_ORDER,
  parseRange,
  type BookSlug,
} from "@/lib/parsha";

export type Verse = {
  ch: number;
  v: number;
  hebrew: string;
  ja: string;
  arabic: string;
  hebrew_translation: string;
  english: string;
  portuguese: string;
  alignment: VerseAlignment | null;
};

export type TafsirData = {
  book: string;
  chapter: number;
  verses: Verse[];
};

export type ChapterLink = {
  bookSlug: string;
  book: string;
  chapter: number;
};

export type ChapterIndexEntry = {
  bookSlug: string;
  chapter: number;
};

export type ParshaNavEntry = {
  slug: string;
  title: string;
  hebrew: string;
  aliyot: string[];
};

type Lang = "en" | "pt";

// UI chrome strings. In Portuguese mode the reader is a clean translation reader:
// the Judeo-Arabic learning apparatus (tap-to-define, word progress, Advanced) is
// hidden and the Portuguese translation is shown by default.
const STRINGS: Record<Lang, {
  back: string; intro: string; prefaceNew: string; prefaceLink: string;
  prefaceTail: string; draftEn: string; draftPt: string; layers: string;
  hebrew: string; jaTafsir: string; arabicScript: string; hebrewTr: string;
  english: string; portuguese: string; advanced: string;
}> = {
  en: {
    back: "← Tafsir",
    intro:
      "Tap any Judeo-Arabic word for a starter gloss. Hover any phrase to see its matching Hebrew, Judeo-Arabic, and English light up together. Toggle the Arabic-script form, the Hebrew translation, or the English off if you'd rather read without crutches.",
    prefaceNew: "New here? Read ",
    prefaceLink: "Saadia's own preface",
    prefaceTail: " to this book.",
    draftEn: "English translation is a working draft — author revising.",
    draftPt: "A tradução portuguesa é um rascunho — em revisão.",
    layers: "Layers",
    hebrew: "Hebrew", jaTafsir: "JA Tafsir", arabicScript: "Arabic script",
    hebrewTr: "Hebrew translation", english: "English", portuguese: "Português",
    advanced: "Advanced",
  },
  pt: {
    back: "← Tafsir",
    intro:
      "Leia o comentário (tafsir) de Saadia Gaon em português, sob o texto hebraico e o judaico-árabe original. Ative a escrita árabe ou a tradução hebraica como apoio de leitura.",
    prefaceNew: "Novo por aqui? Leia o ",
    prefaceLink: "prefácio do próprio Saadia",
    prefaceTail: " a este livro.",
    draftEn: "English translation is a working draft — author revising.",
    draftPt: "A tradução portuguesa é um rascunho — em revisão.",
    layers: "Camadas",
    hebrew: "Hebraico", jaTafsir: "Tafsir JA", arabicScript: "Escrita árabe",
    hebrewTr: "Tradução hebraica", english: "Inglês", portuguese: "Português",
    advanced: "Avançado",
  },
};

export function TafsirReader({
  data,
  prev,
  next,
  bookSlug,
  chapterIndex,
  parshaList,
}: {
  data: TafsirData;
  prev?: ChapterLink | null;
  next?: ChapterLink | null;
  bookSlug: string;
  chapterIndex: ChapterIndexEntry[];
  parshaList: ParshaNavEntry[];
}) {
  const [showArabic, setShowArabic] = useState(false);
  const [showHebrewTr, setShowHebrewTr] = useState(false);
  const [showEnglish, setShowEnglish] = useState(true);
  const [showPortuguese, setShowPortuguese] = useState(false);
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [activeToken, setActiveToken] = useState<string | null>(null);
  const [hoveredGroup, setHoveredGroup] = useState<{
    verseV: number;
    groupId: number;
  } | null>(null);
  // Debounce mouseleave clears by a frame: moving between adjacent tokens of
  // the same group fires leave-then-enter and we don't want a flicker.
  const clearTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const updateHoveredGroup = useCallback(
    (next: { verseV: number; groupId: number } | null) => {
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
    },
    [],
  );

  const [lang, setLangState] = useState<Lang>("en");
  const t = STRINGS[lang];
  const ptMode = lang === "pt";
  const applyLang = useCallback((l: Lang) => {
    setLangState(l);
    if (l === "pt") {
      setShowPortuguese(true);
      setShowEnglish(false);
      setShowAdvanced(false);
      setActiveToken(null);
    } else {
      setShowEnglish(true);
      setShowPortuguese(false);
    }
  }, []);
  // Restore the reader's language choice across chapters.
  useEffect(() => {
    const saved =
      typeof window !== "undefined"
        ? window.localStorage.getItem("reader-lang")
        : null;
    if (saved === "pt") applyLang("pt");
  }, [applyLang]);
  const setLang = (l: Lang) => {
    applyLang(l);
    if (typeof window !== "undefined")
      window.localStorage.setItem("reader-lang", l);
  };

  const { getState, setState, counts, hydrated } = useWordStates();
  const corpus = useCorpus();
  const activeEntries: Entry[] = activeToken ? lookup(activeToken) : [];
  const activeDivergence: DivergenceEntry | null = activeToken
    ? lookupDivergence(activeToken)
    : null;
  const activeState: WordState = activeToken ? getState(activeToken) : "new";
  const activeCorpus: CorpusEntry | null =
    activeToken && corpus ? corpus.getOccurrences(activeToken) : null;
  const loadedVerseKeys = new Set(data.verses.map((v) => `${v.ch}-${v.v}`));

  return (
    <div className="max-w-3xl mx-auto px-6 py-10 pb-44">
      <header className="mb-10">
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
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-1">
          <Link href="/tafsir" className="hover:text-wine transition-colors">{t.back}</Link>
          {" · "}Saadia Gaon
        </p>
        <h1 className="text-4xl tracking-tight text-ink mt-3">
          {data.book} <span className="text-wine italic">{data.chapter}</span>
        </h1>
        <p className="mt-4 text-base text-ink/70 leading-relaxed max-w-xl" lang={lang}>
          {t.intro}
        </p>
        <div className="mt-3 flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-ink/55">
          {!ptMode && (
            <span>
              {t.prefaceNew}
              <Link href="/learn/saadia-preface" className="text-wine hover:underline">
                {t.prefaceLink}
              </Link>
              {t.prefaceTail}
            </span>
          )}
          {!ptMode && showEnglish && (
            <span className="italic">{t.draftEn}</span>
          )}
          {(ptMode || showPortuguese) && (
            <span className="italic" lang="pt">{t.draftPt}</span>
          )}
        </div>
      </header>

      <TafsirNav
        bookSlug={bookSlug}
        chapter={data.chapter}
        verses={data.verses}
        chapterIndex={chapterIndex}
        parshaList={parshaList}
      />

      <ChapterNav prev={prev} next={next} />


      <div className="sticky top-0 z-10 bg-parchment/90 backdrop-blur supports-[backdrop-filter]:bg-parchment/70 -mx-6 px-6 py-3 border-y border-ink/10 flex flex-wrap items-center gap-2 text-sm">
        <span className="text-[10px] uppercase tracking-[0.25em] text-muted mr-1">
          {t.layers}
        </span>
        <ToggleChip on disabled label={t.hebrew} />
        <ToggleChip on disabled label={t.jaTafsir} />
        <ToggleChip
          on={showArabic}
          onClick={() => setShowArabic((x) => !x)}
          label={t.arabicScript}
        />
        <ToggleChip
          on={showHebrewTr}
          onClick={() => setShowHebrewTr((x) => !x)}
          label={t.hebrewTr}
        />
        {!ptMode && (
          <ToggleChip
            on={showEnglish}
            onClick={() => setShowEnglish((x) => !x)}
            label={t.english}
          />
        )}
        <ToggleChip
          on={showPortuguese}
          onClick={() => setShowPortuguese((x) => !x)}
          label={t.portuguese}
        />
        {!ptMode && (
          <ToggleChip
            on={showAdvanced}
            onClick={() => setShowAdvanced((x) => !x)}
            label={t.advanced}
            hint="tafsir twists"
          />
        )}
        {!ptMode && hydrated && (counts.learning + counts.known) > 0 && (
          <span
            className="ml-auto text-[10px] uppercase tracking-[0.25em] text-muted flex items-center"
            title="Per-word progress saved in your browser"
          >
            <span className="text-amber-700">{counts.learning} learning</span>
            <span className="mx-2 text-ink/20">·</span>
            <span className="text-emerald-700">{counts.known} known</span>
            {counts.due > 0 && (
              <>
                <span className="mx-2 text-ink/20">·</span>
                <Link
                  href="/review"
                  className="text-wine underline-offset-2 hover:underline"
                >
                  {counts.due} due
                </Link>
              </>
            )}
          </span>
        )}
      </div>

      <ol className="mt-10 space-y-6">
        {data.verses.map((verse) => (
          <li
            key={verse.v}
            id={`verse-${verse.ch}-${verse.v}`}
            className="rounded-md bg-page border border-ink/10 p-7 scroll-mt-24"
          >
            <div className="text-[11px] uppercase tracking-[0.25em] text-muted mb-5">
              {data.book} {data.chapter}:{verse.v}
            </div>
            <div dir="rtl" className="space-y-5">
              <p className="font-hebrew text-2xl text-ink leading-loose">
                <HebrewText
                  text={verse.hebrew}
                  alignment={verse.alignment}
                  hoveredGroupId={
                    hoveredGroup?.verseV === verse.v
                      ? hoveredGroup.groupId
                      : null
                  }
                  onHoverGroup={(g) =>
                    updateHoveredGroup(
                      g === null ? null : { verseV: verse.v, groupId: g },
                    )
                  }
                />
              </p>
              <div className="border-r-2 border-wine/60 pr-5">
                <p className="font-hebrew ja-text text-xl text-ink/90 leading-loose">
                  <JaText
                    text={verse.ja}
                    activeToken={ptMode ? null : activeToken}
                    onTap={ptMode ? () => {} : setActiveToken}
                    getState={ptMode ? () => "new" : getState}
                    markDivergence={showAdvanced && !ptMode}
                    alignment={verse.alignment}
                    hoveredGroupId={
                      hoveredGroup?.verseV === verse.v
                        ? hoveredGroup.groupId
                        : null
                    }
                    onHoverGroup={(g) =>
                      updateHoveredGroup(
                        g === null ? null : { verseV: verse.v, groupId: g },
                      )
                    }
                  />
                </p>
              </div>
              {showArabic && verse.arabic && (
                <p className="font-arabic text-xl text-ink/75 leading-loose">
                  {verse.arabic}
                </p>
              )}
              {showHebrewTr && verse.hebrew_translation && (
                <p className="font-hebrew text-lg text-muted italic leading-loose">
                  {verse.hebrew_translation}
                </p>
              )}
            </div>
            {showEnglish && verse.english && (
              <p
                dir="ltr"
                className="mt-5 pt-5 border-t border-ink/10 text-[15px] leading-relaxed text-ink/80"
              >
                <EnglishText
                  text={verse.english}
                  alignment={verse.alignment}
                  hoveredGroupId={
                    hoveredGroup?.verseV === verse.v
                      ? hoveredGroup.groupId
                      : null
                  }
                  onHoverGroup={(g) =>
                    updateHoveredGroup(
                      g === null ? null : { verseV: verse.v, groupId: g },
                    )
                  }
                />
              </p>
            )}
            {showPortuguese && verse.portuguese && (
              <p
                dir="ltr"
                lang="pt"
                className="mt-5 pt-5 border-t border-ink/10 text-[15px] leading-relaxed text-ink/80"
              >
                {verse.portuguese}
              </p>
            )}
          </li>
        ))}
      </ol>

      <div className="mt-10">
        <ChapterNav prev={prev} next={next} />
      </div>

      {!ptMode && activeToken && (
        <GlossPanel
          token={activeToken}
          entries={activeEntries}
          divergence={activeDivergence}
          corpus={activeCorpus}
          corpusReady={corpus !== null}
          corpusLabel={corpus?.label ?? "the Pentateuch"}
          loadedVerseKeys={loadedVerseKeys}
          state={activeState}
          onSetState={(s) => setState(activeToken, s)}
          onClose={() => setActiveToken(null)}
        />
      )}
    </div>
  );
}

const STATE_CLASS: Record<WordState, string> = {
  new: "hover:bg-wine-50",
  learning: "bg-amber-100/70 hover:bg-amber-100",
  known: "hover:bg-wine-50",
  ignored: "text-ink/30 hover:bg-wine-50",
};

function JaText({
  text,
  activeToken,
  onTap,
  getState,
  markDivergence,
  alignment,
  hoveredGroupId,
  onHoverGroup,
}: {
  text: string;
  activeToken: string | null;
  onTap: (t: string) => void;
  getState: (t: string) => WordState;
  markDivergence: boolean;
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
        // For seps inside the currently-hovered group, paint a faint highlight
        // so the group reads as a continuous chunk rather than disjoint words.
        const groupForRange = alignment
          ? alignment.ja.find(
              (s) => s.start <= tokenStart && s.end >= tokenEnd,
            )?.groupId ?? null
          : null;
        if (t.kind === "sep") {
          const inHover =
            groupForRange !== null && groupForRange === hoveredGroupId;
          return (
            <span
              key={i}
              className={inHover ? "bg-amber-100/70" : undefined}
            >
              {t.text}
            </span>
          );
        }
        const isActive = activeToken === t.text;
        const state = getState(t.text);
        // Tier gates the underline: twist + note get a visible mark; gloss is
        // hover-only (tap still surfaces the GlossPanel via onTap → lookup).
        const tier = markDivergence ? divergenceTier(t.text) : null;
        const divergent = tier === "twist" || tier === "note";
        const underlineCls =
          tier === "twist"
            ? "underline decoration-dotted decoration-wine/60 decoration-1 underline-offset-[6px]"
            : tier === "note"
              ? "underline decoration-dotted decoration-ink/30 decoration-1 underline-offset-[6px]"
              : "";
        const tierTitle =
          tier === "twist"
            ? "Tafsir twist — see panel"
            : tier === "note"
              ? "Saadia note — see panel"
              : undefined;
        const inHover =
          groupForRange !== null && groupForRange === hoveredGroupId;
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
            title={tierTitle}
            className={`inline cursor-pointer rounded-sm transition-colors px-0.5 -mx-0.5
              ${
                isActive
                  ? "bg-wine-100 text-wine-700"
                  : inHover
                    ? "bg-amber-100 text-ink ring-1 ring-amber-300/60"
                    : STATE_CLASS[state]
              }
              ${divergent && !isActive ? underlineCls : ""}`}
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

function HebrewText({
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
  if (!alignment || alignment.he.length === 0) {
    return <>{text}</>;
  }
  const runs = sliceByGroups(text, alignment.he);
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
  entries,
  divergence,
  corpus,
  corpusReady,
  corpusLabel,
  loadedVerseKeys,
  state,
  onSetState,
  onClose,
}: {
  token: string;
  entries: Entry[];
  divergence: DivergenceEntry | null;
  corpus: CorpusEntry | null;
  corpusReady: boolean;
  corpusLabel: string;
  loadedVerseKeys: Set<string>;
  state: WordState;
  onSetState: (s: WordState) => void;
  onClose: () => void;
}) {
  // Dismiss on Escape key
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") onClose();
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <div className="fixed bottom-0 left-1/2 -translate-x-1/2 z-20 w-full max-w-3xl bg-page border border-b-0 border-wine/20 rounded-t-md shadow-[0_-8px_24px_-12px_rgba(114,47,55,0.2)]">
      <div className="px-6 py-5">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-baseline gap-4">
            <span className="font-hebrew text-3xl text-ink" dir="rtl">
              {token}
            </span>
            <span className="text-[10px] uppercase tracking-[0.3em] text-muted">
              Tapped word
            </span>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="text-ink/40 hover:text-wine text-2xl leading-none w-8 h-8 flex items-center justify-center rounded-full hover:bg-wine-50 transition-colors"
            aria-label="Close"
          >
            ×
          </button>
        </div>
        <StatePills state={state} onSetState={onSetState} />
        {divergence && <DivergenceBanner d={divergence} />}
        {entries.length === 0 ? (
          <p className="text-sm text-muted mt-2 italic">
            Not in the dictionary yet. The high-frequency Tafsir vocabulary is
            curated by hand; rarer or inflected forms may not resolve.
          </p>
        ) : (
          <ul className="space-y-4 mt-2">
            {entries.map((e) => (
              <li key={e.id} className="border-l-2 border-wine/40 pl-4">
                <div className="flex items-baseline gap-3 flex-wrap">
                  <span className="font-hebrew text-xl text-ink" dir="rtl">
                    {e.lemma_ja}
                  </span>
                  {e.lemma_ar && (
                    <span
                      className="font-arabic text-lg text-ink/70"
                      dir="rtl"
                    >
                      {e.lemma_ar}
                    </span>
                  )}
                  {e.root && (
                    <span className="text-xs text-muted font-mono">
                      √{e.root}
                    </span>
                  )}
                  {e.pos && (
                    <span className="text-xs text-muted italic">{e.pos}</span>
                  )}
                  <SourceBadge source={e.source} />
                </div>
                {e.gloss_en && (
                  <p className="mt-1.5 text-ink text-[15px]">{e.gloss_en}</p>
                )}
                {e.gloss_he && (
                  <p
                    className="font-hebrew text-base text-muted mt-0.5"
                    dir="rtl"
                  >
                    {e.gloss_he}
                  </p>
                )}
                {e.notes && (
                  <p className="text-[12px] text-muted mt-2 leading-relaxed italic">
                    {e.notes}
                  </p>
                )}
                {e.saadia_note && (
                  <p className="text-[12.5px] text-wine/75 mt-2 leading-relaxed">
                    <span className="text-wine font-semibold not-italic">
                      In Saadia&rsquo;s Tafsir:{" "}
                    </span>
                    <span className="italic">{e.saadia_note}</span>
                  </p>
                )}
              </li>
            ))}
          </ul>
        )}
        <Concordance
          corpus={corpus}
          corpusReady={corpusReady}
          corpusLabel={corpusLabel}
          loadedVerseKeys={loadedVerseKeys}
          onJump={onClose}
        />
      </div>
    </div>
  );
}

function SourceBadge({ source }: { source?: Entry["source"] }) {
  if (!source) return null;
  if (source === "lane") {
    return (
      <span
        title="Standard classical Arabic sense — Lane's Lexicon (E.W. Lane, 1863-93) is the canonical English reference. We paraphrase rather than quote verbatim."
        className="text-[10px] uppercase tracking-[0.2em] text-wine/70 border border-wine/30 rounded-sm px-1.5 py-0.5 ml-auto"
      >
        Lane
      </span>
    );
  }
  if (source === "blau") {
    return (
      <span
        title="Judaeo-Arabic sense documented in Joshua Blau's Dictionary of Medieval Judaeo-Arabic Texts (2006)."
        className="text-[10px] uppercase tracking-[0.2em] text-wine border border-wine/40 bg-wine-50 rounded-sm px-1.5 py-0.5 ml-auto"
      >
        Blau
      </span>
    );
  }
  // The "camel" (auto-extracted, unverified) tier has been retired — lookup no
  // longer returns such entries, so no badge is rendered for it.
  return null;
}

function DivergenceBanner({ d }: { d: DivergenceEntry }) {
  const tier: DivergenceTier = d.tier ?? "twist";
  if (tier === "gloss") return <GlossCard d={d} />;
  if (tier === "note") return <SaadiaNoteBanner d={d} />;
  return <TwistBanner d={d} />;
}

function TwistBanner({ d }: { d: DivergenceEntry }) {
  return (
    <div className="mb-4 rounded-md border border-wine/30 bg-wine-50/60 px-4 py-3">
      <div className="flex items-baseline gap-3 mb-2">
        <span className="text-[10px] uppercase tracking-[0.3em] text-wine">
          Tafsir twist
        </span>
        <span className="text-xs text-muted font-mono">√{d.root}</span>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-[auto_1fr] gap-x-4 gap-y-1.5 text-[13.5px]">
        <span className="text-[11px] uppercase tracking-wider text-ink/50 pt-0.5">
          Classical
        </span>
        <span className="text-ink/85">{d.classical_en}</span>
        <span className="text-[11px] uppercase tracking-wider text-wine/80 pt-0.5">
          Saadia
        </span>
        <span className="text-ink">{d.saadia_en}</span>
      </div>
      <p className="text-[12px] text-muted italic mt-2 leading-relaxed">
        {d.mechanism}
      </p>
      <DivergenceSources d={d} />
    </div>
  );
}

// Lighter register for semantic surprises that don't reframe theology.
// One short contrast line, no mechanism essay.
function SaadiaNoteBanner({ d }: { d: DivergenceEntry }) {
  return (
    <div className="mb-4 rounded-md border border-ink/15 bg-ink/5 px-4 py-3">
      <div className="flex items-baseline gap-3 mb-2">
        <span className="text-[10px] uppercase tracking-[0.3em] text-ink/60">
          Saadia note
        </span>
        <span className="text-xs text-muted font-mono">√{d.root}</span>
      </div>
      <p className="text-[13px] text-ink/85 leading-relaxed">
        Saadia picks <span className="font-medium">{d.saadia_en}</span> here;
        classical Arabic would expect{" "}
        <span className="font-medium">{d.classical_en}</span>.
      </p>
      <DivergenceSources d={d} />
    </div>
  );
}

// Compact one-line card for non-obvious Heb→Ar pairings (the ~575 EXPANSIVE
// tier). Surfaces only on tap — no baseline underline on the word. Just the
// equivalence + a small Blau citation.
function GlossCard({ d }: { d: DivergenceEntry }) {
  return (
    <div className="mb-4 rounded-md border border-ink/10 bg-paper px-4 py-2.5">
      <div className="flex items-baseline gap-2 text-[13.5px] flex-wrap">
        <span className="text-ink/70">{d.classical_he}</span>
        <span className="text-ink/40">→</span>
        <span className="font-mono text-ink">{d.lemma_ja}</span>
        <span className="text-ink/55 text-[12px]">
          <span dir="rtl" lang="ar">
            {d.lemma_ar}
          </span>
          {" · "}
          {d.saadia_en}
        </span>
        {d.blau_dict && (
          <span
            className="ml-auto text-[10.5px] uppercase tracking-wider text-ink/40"
            title={d.blau_dict.sense}
          >
            Blau s.v.{" "}
            <span className="font-mono normal-case">{d.blau_dict.root}</span>
          </span>
        )}
      </div>
    </div>
  );
}

function DivergenceSources({ d }: { d: DivergenceEntry }) {
  const hasBlauDict = !!d.blau_dict;
  const blauRelation = d.blau_dict?.relation;
  return (
    <div className="mt-3 pt-2 border-t border-wine/15 text-[11px] leading-relaxed text-ink/55">
      <span className="uppercase tracking-wider text-ink/40 mr-1">
        Sources:
      </span>
      <span>Lane · Saadia direct</span>
      {hasBlauDict && (
        <>
          {" · "}
          <span title={d.blau_dict?.sense}>
            Blau Dict.
            {blauRelation === "direct"
              ? ""
              : blauRelation === "adjacent"
                ? " (adjacent)"
                : " (different sense)"}{" "}
            s.v. <span className="font-mono">{d.blau_dict?.root}</span>
          </span>
        </>
      )}
      {d.blau_festschrift && (
        <>
          {" · "}
          <span title={d.blau_festschrift.note}>
            Blau Festschrift (p. {d.blau_festschrift.page},{" "}
            {d.blau_festschrift.relation === "same-verse-different-lexeme"
              ? "same verse"
              : d.blau_festschrift.relation})
          </span>
        </>
      )}
    </div>
  );
}

function ChapterNav({
  prev,
  next,
}: {
  prev?: ChapterLink | null;
  next?: ChapterLink | null;
}) {
  if (!prev && !next) return null;
  return (
    <nav className="mt-6 flex items-center justify-between text-sm">
      <div className="flex-1">
        {prev ? (
          <Link
            href={`/tafsir/${prev.bookSlug}/${prev.chapter}`}
            className="inline-flex items-baseline gap-2 text-ink/70 hover:text-wine"
            rel="prev"
          >
            <span aria-hidden>←</span>
            <span>
              {prev.book} {prev.chapter}
            </span>
          </Link>
        ) : (
          <span aria-hidden />
        )}
      </div>
      <div className="flex-1 text-right">
        {next ? (
          <Link
            href={`/tafsir/${next.bookSlug}/${next.chapter}`}
            className="inline-flex items-baseline gap-2 text-ink/70 hover:text-wine"
            rel="next"
          >
            <span>
              {next.book} {next.chapter}
            </span>
            <span aria-hidden>→</span>
          </Link>
        ) : (
          <span aria-hidden />
        )}
      </div>
    </nav>
  );
}

function Concordance({
  corpus,
  corpusReady,
  corpusLabel,
  loadedVerseKeys,
  onJump,
}: {
  corpus: CorpusEntry | null;
  corpusReady: boolean;
  corpusLabel: string;
  loadedVerseKeys: Set<string>;
  onJump: () => void;
}) {
  // High-frequency function words (אן, מן, אלד'י…) occur hundreds of times; showing
  // every reference buries the gloss under a wall of chips. Cap and let the user expand.
  const ELSEWHERE_CAP = 24;
  const [showAllElsewhere, setShowAllElsewhere] = useState(false);
  if (!corpusReady) {
    return (
      <p className="text-[11px] uppercase tracking-[0.25em] text-muted mb-4 italic">
        Loading concordance…
      </p>
    );
  }
  if (!corpus || corpus.count === 0) {
    return (
      <p className="text-[11px] uppercase tracking-[0.25em] text-muted mb-4">
        Not found in {corpusLabel}
      </p>
    );
  }
  const verses = uniqueVerses(corpus.occurrences);
  const variants = variantBreakdown(corpus.occurrences);
  const inView = verses.filter((r) => loadedVerseKeys.has(`${r.ch}-${r.v}`));
  const elsewhere = verses.filter((r) => !loadedVerseKeys.has(`${r.ch}-${r.v}`));
  const handleJump = (ch: number, v: number) => {
    onJump();
    requestAnimationFrame(() => {
      document
        .getElementById(`verse-${ch}-${v}`)
        ?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  };
  return (
    <div className="mb-4 border-t border-ink/10 pt-3">
      <p className="text-[11px] uppercase tracking-[0.25em] text-muted mb-2">
        Appears {corpus.count}× across {verses.length}{" "}
        {verses.length === 1 ? "verse" : "verses"} in {corpusLabel}
      </p>
      {variants.length > 1 && (
        <p className="text-[12px] text-ink/70 mb-2" dir="rtl">
          {variants.map((v, i) => (
            <span key={v.surface}>
              {i > 0 && <span className="text-ink/30 mx-1.5">·</span>}
              <span className="font-hebrew">{v.surface}</span>
              <span className="text-muted ms-1">({v.count})</span>
            </span>
          ))}
        </p>
      )}
      {inView.length > 0 && (
        <div className="flex flex-wrap gap-1.5 mb-1.5">
          {inView.map(({ ch, v }) => (
            <button
              key={`${ch}-${v}`}
              type="button"
              onClick={() => handleJump(ch, v)}
              className="text-[11px] font-mono px-2 py-0.5 rounded-sm border border-ink/15 text-ink/70 hover:border-wine/50 hover:text-wine hover:bg-wine-50 transition-colors"
            >
              {ch}:{v}
            </button>
          ))}
        </div>
      )}
      {elsewhere.length > 0 && (
        <div className="flex flex-wrap gap-1.5 items-baseline">
          <span className="text-[10px] uppercase tracking-[0.2em] text-muted">
            Elsewhere:
          </span>
          {(showAllElsewhere ? elsewhere : elsewhere.slice(0, ELSEWHERE_CAP)).map(
            ({ ch, v }) => (
              <span
                key={`${ch}-${v}`}
                title="In a chapter not currently loaded"
                className="text-[11px] font-mono px-2 py-0.5 rounded-sm border border-ink/10 text-ink/40"
              >
                {ch}:{v}
              </span>
            ),
          )}
          {elsewhere.length > ELSEWHERE_CAP && (
            <button
              type="button"
              onClick={() => setShowAllElsewhere((x) => !x)}
              className="text-[11px] px-2 py-0.5 rounded-sm text-wine hover:underline"
            >
              {showAllElsewhere
                ? "show fewer"
                : `+${elsewhere.length - ELSEWHERE_CAP} more`}
            </button>
          )}
        </div>
      )}
    </div>
  );
}

const PILL_LABEL: Record<WordState, string> = {
  new: "New",
  learning: "Learning",
  known: "Known",
  ignored: "Ignore",
};

const PILL_ACTIVE: Record<WordState, string> = {
  new: "bg-ink/80 text-page border-ink/80",
  learning: "bg-amber-600 text-page border-amber-600",
  known: "bg-emerald-700 text-page border-emerald-700",
  ignored: "bg-ink/40 text-page border-ink/40",
};

function StatePills({
  state,
  onSetState,
}: {
  state: WordState;
  onSetState: (s: WordState) => void;
}) {
  const order: WordState[] = ["new", "learning", "known", "ignored"];
  return (
    <div className="flex flex-wrap items-center gap-2 mb-4">
      <span className="text-[10px] uppercase tracking-[0.25em] text-muted mr-1">
        Mark as
      </span>
      {order.map((s) => {
        const active = state === s;
        return (
          <button
            key={s}
            type="button"
            onClick={() => onSetState(s)}
            className={`px-3 py-1 rounded-full border text-xs uppercase tracking-wider transition-all
              ${
                active
                  ? PILL_ACTIVE[s]
                  : "bg-page text-ink/70 border-ink/15 hover:border-wine/50 hover:text-wine"
              }`}
          >
            {PILL_LABEL[s]}
          </button>
        );
      })}
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

function TafsirNav({
  bookSlug,
  chapter,
  verses,
  chapterIndex,
  parshaList,
}: {
  bookSlug: string;
  chapter: number;
  verses: Verse[];
  chapterIndex: ChapterIndexEntry[];
  parshaList: ParshaNavEntry[];
}) {
  const router = useRouter();

  const chaptersByBook = useMemo(() => {
    const m: Record<string, number[]> = {};
    for (const r of chapterIndex) {
      (m[r.bookSlug] ??= []).push(r.chapter);
    }
    for (const k of Object.keys(m)) m[k].sort((a, b) => a - b);
    return m;
  }, [chapterIndex]);

  const verseNumbers = useMemo(() => verses.map((v) => v.v), [verses]);

  const [selBook, setSelBook] = useState<string>(bookSlug);
  const [selChapter, setSelChapter] = useState<number>(chapter);
  const [selParsha, setSelParsha] = useState<string>(
    parshaList[0]?.slug ?? "",
  );
  const [selAliyah, setSelAliyah] = useState<number>(1);

  const goToChapter = (book: string, ch: number) => {
    router.push(`/tafsir/${book}/${ch}`);
  };

  const goToVerse = (v: number) => {
    const el = document.getElementById(`verse-${chapter}-${v}`);
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
  };

  const goToAliyah = (parshaSlug: string, aliyahN: number) => {
    const p = parshaList.find((x) => x.slug === parshaSlug);
    if (!p) return;
    const ref = p.aliyot[aliyahN - 1];
    const range = ref ? parseRange(ref) : null;
    if (!range) return;
    router.push(
      `/tafsir/${range.start.book}/${range.start.ch}#verse-${range.start.ch}-${range.start.v}`,
    );
  };

  const chaptersForSelected = chaptersByBook[selBook] ?? [];
  const selectedParsha = parshaList.find((p) => p.slug === selParsha) ?? null;

  return (
    <div className="mt-2 mb-6 rounded-md border border-ink/10 bg-page/60 p-4">
      <div className="text-[10px] uppercase tracking-[0.25em] text-muted mb-3">
        Navigate
      </div>

      <div className="grid gap-4 sm:grid-cols-[auto_1fr] items-center">
        <div className="text-[11px] uppercase tracking-[0.2em] text-ink/55">
          Tanakh
        </div>
        <div className="flex flex-wrap items-center gap-2 text-sm">
          <NavSelect
            label="Book"
            value={selBook}
            onChange={(b) => {
              setSelBook(b);
              const ch = (chaptersByBook[b] ?? [1])[0] ?? 1;
              setSelChapter(ch);
              goToChapter(b, ch);
            }}
          >
            {BOOK_ORDER.filter((b) => chaptersByBook[b]?.length).map((b) => (
              <option key={b} value={b}>
                {BOOK_DISPLAY[b as BookSlug]}
              </option>
            ))}
          </NavSelect>
          <NavSelect
            label="Chapter"
            value={String(selChapter)}
            onChange={(v) => {
              const ch = Number(v);
              setSelChapter(ch);
              goToChapter(selBook, ch);
            }}
          >
            {chaptersForSelected.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </NavSelect>
          <NavSelect
            label="Verse"
            value=""
            disabled={selBook !== bookSlug || selChapter !== chapter}
            onChange={(v) => goToVerse(Number(v))}
          >
            <option value="">—</option>
            {verseNumbers.map((v) => (
              <option key={v} value={v}>
                {v}
              </option>
            ))}
          </NavSelect>
        </div>

        <div className="text-[11px] uppercase tracking-[0.2em] text-ink/55">
          Parsha
        </div>
        <div className="flex flex-wrap items-center gap-2 text-sm">
          <NavSelect
            label="Parsha"
            value={selParsha}
            onChange={(p) => {
              setSelParsha(p);
              setSelAliyah(1);
              goToAliyah(p, 1);
            }}
          >
            {parshaList.map((p) => (
              <option key={p.slug} value={p.slug}>
                {p.title}
              </option>
            ))}
          </NavSelect>
          <NavSelect
            label="Aliyah"
            value={String(selAliyah)}
            disabled={!selectedParsha}
            onChange={(v) => {
              const n = Number(v);
              setSelAliyah(n);
              goToAliyah(selParsha, n);
            }}
          >
            {ALIYAH_LABELS.map((name, i) => (
              <option key={i} value={i + 1}>
                {i + 1}. {name}
              </option>
            ))}
          </NavSelect>
          {selectedParsha && (
            <span
              dir="rtl"
              className="font-hebrew text-sm text-ink/55 ml-1"
            >
              {selectedParsha.hebrew}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

function NavSelect({
  label,
  value,
  onChange,
  disabled,
  children,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
  disabled?: boolean;
  children: React.ReactNode;
}) {
  return (
    <label
      className={`inline-flex items-center gap-1.5 text-[11px] uppercase tracking-wider ${
        disabled ? "opacity-40" : "text-ink/60"
      }`}
    >
      <span>{label}</span>
      <select
        value={value}
        disabled={disabled}
        onChange={(e) => onChange(e.target.value)}
        className="rounded-sm border border-ink/15 bg-page px-2 py-1 text-sm font-normal normal-case tracking-normal text-ink hover:border-wine/40 focus:border-wine/60 focus:outline-none disabled:cursor-not-allowed"
      >
        {children}
      </select>
    </label>
  );
}

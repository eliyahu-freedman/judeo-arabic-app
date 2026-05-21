"use client";

import Link from "next/link";
import { useState } from "react";
import { lookup, tokenizeJa, type Entry } from "@/lib/lookup";
import {
  uniqueVerses,
  useCorpus,
  variantBreakdown,
  type CorpusEntry,
} from "@/lib/corpus";
import { useWordStates, type WordState } from "@/lib/wordState";

export type Verse = {
  ch: number;
  v: number;
  hebrew: string;
  ja: string;
  arabic: string;
  hebrew_translation: string;
  english: string;
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

export function TafsirReader({
  data,
  prev,
  next,
}: {
  data: TafsirData;
  prev?: ChapterLink | null;
  next?: ChapterLink | null;
}) {
  const [showArabic, setShowArabic] = useState(false);
  const [showHebrewTr, setShowHebrewTr] = useState(false);
  const [showEnglish, setShowEnglish] = useState(false);
  const [activeToken, setActiveToken] = useState<string | null>(null);

  const { getState, setState, counts, hydrated } = useWordStates();
  const corpus = useCorpus();
  const activeEntries: Entry[] = activeToken ? lookup(activeToken) : [];
  const activeState: WordState = activeToken ? getState(activeToken) : "new";
  const activeCorpus: CorpusEntry | null =
    activeToken && corpus ? corpus.getOccurrences(activeToken) : null;
  const loadedVerseKeys = new Set(data.verses.map((v) => `${v.ch}-${v.v}`));

  return (
    <div className="max-w-3xl mx-auto px-6 py-10 pb-44">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Saadia · {data.book} {data.chapter}
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          Tafsir <span className="text-wine italic">Reader</span>
        </h1>
        <p className="mt-4 text-base text-ink/70 leading-relaxed max-w-xl">
          Tap any Judeo-Arabic word for a starter gloss. Toggle the
          Arabic-script form, the Hebrew translation, and English (coming
          soon).
        </p>
        <p className="mt-3 text-xs text-ink/55">
          New here? Read{" "}
          <Link
            href="/learn/saadia-preface"
            className="text-wine hover:underline"
          >
            Saadia&apos;s own preface
          </Link>{" "}
          to this book.
        </p>
      </header>

      <ChapterNav prev={prev} next={next} />


      <div className="sticky top-0 z-10 bg-parchment/90 backdrop-blur supports-[backdrop-filter]:bg-parchment/70 -mx-6 px-6 py-3 border-y border-ink/10 flex flex-wrap items-center gap-2 text-sm">
        <span className="text-[10px] uppercase tracking-[0.25em] text-muted mr-1">
          Layers
        </span>
        <ToggleChip on disabled label="Hebrew" />
        <ToggleChip on disabled label="JA Tafsir" />
        <ToggleChip
          on={showArabic}
          onClick={() => setShowArabic((x) => !x)}
          label="Arabic script"
        />
        <ToggleChip
          on={showHebrewTr}
          onClick={() => setShowHebrewTr((x) => !x)}
          label="Hebrew translation"
        />
        <ToggleChip
          on={showEnglish}
          onClick={() => setShowEnglish((x) => !x)}
          label="English"
          hint="draft"
        />
        {hydrated && (counts.learning + counts.known) > 0 && (
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
                {verse.hebrew}
              </p>
              <div className="border-r-2 border-wine/60 pr-5">
                <p className="font-hebrew ja-text text-xl text-ink/90 leading-loose">
                  <JaText
                    text={verse.ja}
                    activeToken={activeToken}
                    onTap={setActiveToken}
                    getState={getState}
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
                {verse.english}
              </p>
            )}
          </li>
        ))}
      </ol>

      <div className="mt-10">
        <ChapterNav prev={prev} next={next} />
      </div>

      {showEnglish && (
        <p className="mt-6 text-xs uppercase tracking-[0.25em] text-muted text-center italic">
          English is a working draft — author revising
        </p>
      )}

      {activeToken && (
        <GlossPanel
          token={activeToken}
          entries={activeEntries}
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
}: {
  text: string;
  activeToken: string | null;
  onTap: (t: string) => void;
  getState: (t: string) => WordState;
}) {
  const tokens = tokenizeJa(text);
  return (
    <>
      {tokens.map((t, i) => {
        if (t.kind === "sep") return <span key={i}>{t.text}</span>;
        const isActive = activeToken === t.text;
        const state = getState(t.text);
        return (
          <button
            key={i}
            type="button"
            onClick={() => onTap(t.text)}
            className={`inline cursor-pointer rounded-sm transition-colors px-0.5 -mx-0.5
              ${
                isActive
                  ? "bg-wine-100 text-wine-700"
                  : STATE_CLASS[state]
              }`}
          >
            {t.text}
          </button>
        );
      })}
    </>
  );
}

function GlossPanel({
  token,
  entries,
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
  corpus: CorpusEntry | null;
  corpusReady: boolean;
  corpusLabel: string;
  loadedVerseKeys: Set<string>;
  state: WordState;
  onSetState: (s: WordState) => void;
  onClose: () => void;
}) {
  return (
    <div className="fixed bottom-0 inset-x-0 z-20 bg-page border-t border-wine/20 shadow-[0_-8px_24px_-12px_rgba(114,47,55,0.2)]">
      <div className="max-w-3xl mx-auto px-6 py-5">
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
        <Concordance
          corpus={corpus}
          corpusReady={corpusReady}
          corpusLabel={corpusLabel}
          loadedVerseKeys={loadedVerseKeys}
          onJump={onClose}
        />
        {entries.length === 0 ? (
          <p className="text-sm text-muted mt-2 italic">
            No entry yet in the starter dictionary. (The full Blau lexicon
            will be wired in later — this prototype covers high-frequency
            words.)
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
                  {e.source && (
                    <span
                      className="text-[10px] uppercase tracking-[0.2em] text-ink/40 border border-ink/15 rounded-sm px-1.5 py-0.5 ml-auto"
                      title="Auto-extracted; verify before citing"
                    >
                      {e.source}
                    </span>
                  )}
                </div>
                {e.gloss_en && (
                  <p
                    className={`mt-1.5 text-ink ${
                      e.source ? "text-[13px] leading-relaxed" : "text-[15px]"
                    }`}
                  >
                    {e.gloss_en}
                  </p>
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
              </li>
            ))}
          </ul>
        )}
      </div>
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
          {elsewhere.map(({ ch, v }) => (
            <span
              key={`${ch}-${v}`}
              title="In a chapter not currently loaded"
              className="text-[11px] font-mono px-2 py-0.5 rounded-sm border border-ink/10 text-ink/40"
            >
              {ch}:{v}
            </span>
          ))}
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

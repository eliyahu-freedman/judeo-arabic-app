"use client";

import Link from "next/link";
import { useState } from "react";
import { Quiz, type QuizQuestion } from "@/components/Quiz";
import { deckKeyForWord } from "@/lib/deck";
import { useWordStates } from "@/lib/wordState";
import { useProgress } from "@/lib/progress";

export type FirstFiftyEntry = {
  rank: number;
  key: string;
  lemma_ja: string;
  arabic: string;
  en: string;
  he_echo: string;
  group: string;
  note: string;
  root: string;
  count: number;
  n_verses: number;
  first: {
    book_slug: string;
    book: string;
    ch: number;
    v: number;
  } | null;
};

const GROUP_ORDER = ["essentials", "function", "pronouns", "verbs", "names"] as const;
type Group = (typeof GROUP_ORDER)[number];

const GROUP_LABEL: Record<Group, string> = {
  essentials: "Creation-story essentials",
  function: "Function words",
  pronouns: "Pronouns & demonstratives",
  verbs: "Common verbs",
  names: "Names",
};

const GROUP_HINT: Record<Group, string> = {
  essentials: "The first ten content words — God, earth, sky, water, light, darkness. If you read Genesis 1, you'll meet them in the first three verses.",
  function: "The connective tissue of every sentence: 'from', 'in', 'on', 'all', 'and', 'or', 'when'. Most are direct cognates of Hebrew or one short step away.",
  pronouns: "He, she, this, that, who, which. Same letters as Hebrew most of the time — different vowels.",
  verbs: "Said, was, became, created, knew, saw, took, gave. Saadia uses these everywhere.",
  names: "The cast of characters as Saadia writes them — Moshe → Mūsā, Pharaoh → Firʿawn, Israel → Isrāʾīl.",
};

/* ---------------- Quiz generator ---------------- */

function shuffle<T>(arr: T[]): T[] {
  return [...arr].sort(() => Math.random() - 0.5);
}

function pickDistractors(
  pool: FirstFiftyEntry[],
  answer: FirstFiftyEntry,
  valueOf: (e: FirstFiftyEntry) => string,
): FirstFiftyEntry[] {
  const seen = new Set([valueOf(answer)]);
  const out: FirstFiftyEntry[] = [];
  for (const e of shuffle(pool)) {
    const v = valueOf(e);
    if (seen.has(v)) continue;
    seen.add(v);
    out.push(e);
    if (out.length === 3) break;
  }
  return out;
}

type VQType = "word_to_gloss" | "gloss_to_word" | "ar_to_ja";

export function generateVocabQuestion(entries: FirstFiftyEntry[]): QuizQuestion {
  const types: VQType[] = ["word_to_gloss", "gloss_to_word", "ar_to_ja"];
  const type = types[Math.floor(Math.random() * types.length)];
  const answer = entries[Math.floor(Math.random() * entries.length)];
  const reviewKey = deckKeyForWord(answer.lemma_ja);

  if (type === "word_to_gloss") {
    const choices = shuffle([
      answer,
      ...pickDistractors(entries, answer, (e) => e.en),
    ]);
    return {
      promptTop: {
        text: answer.lemma_ja,
        cls: "font-hebrew text-5xl text-ink",
        dir: "rtl",
      },
      promptHint: answer.arabic,
      promptInstruction: "What does this word mean?",
      choices: choices.map((e) => ({
        value: e.en,
        cls: "text-[15px] text-ink",
        dir: "ltr",
      })),
      correctIdx: choices.indexOf(answer),
      explanation: `${answer.lemma_ja} (${answer.arabic}) — ${answer.en}`,
      reviewKey,
    };
  }

  if (type === "gloss_to_word") {
    const choices = shuffle([
      answer,
      ...pickDistractors(entries, answer, (e) => e.lemma_ja),
    ]);
    return {
      promptTop: { text: answer.en, cls: "text-2xl text-ink", dir: "ltr" },
      promptInstruction: "Which Judeo-Arabic word means this?",
      choices: choices.map((e) => ({
        value: e.lemma_ja,
        cls: "font-hebrew text-3xl text-ink",
        dir: "rtl",
      })),
      correctIdx: choices.indexOf(answer),
      explanation: `${answer.en} = ${answer.lemma_ja} (${answer.arabic})`,
      reviewKey,
    };
  }

  // ar_to_ja
  const choices = shuffle([
    answer,
    ...pickDistractors(entries, answer, (e) => e.lemma_ja),
  ]);
  return {
    promptTop: {
      text: answer.arabic,
      cls: "font-arabic text-5xl text-wine",
      dir: "rtl",
    },
    promptInstruction: "How is this written in Judeo-Arabic (Hebrew letters)?",
    choices: choices.map((e) => ({
      value: e.lemma_ja,
      cls: "font-hebrew text-3xl text-ink",
      dir: "rtl",
    })),
    correctIdx: choices.indexOf(answer),
    explanation: `${answer.arabic} → ${answer.lemma_ja} — ${answer.en}`,
    reviewKey,
  };
}

export function First50Cards({ entries }: { entries: FirstFiftyEntry[] }) {
  const [filter, setFilter] = useState<Group | "all">("all");
  const [mode, setMode] = useState<"study" | "quiz">("study");
  const { setState, setItemState, getState, hydrated } = useWordStates();
  const { markLessonDone, touchStreak } = useProgress();
  const groups = GROUP_ORDER.filter((g) => entries.some((e) => e.group === g));

  return (
    <div className="max-w-3xl mx-auto px-6 py-16 pb-32">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          <Link href="/learn" className="hover:text-wine">
            Learn
          </Link>{" "}
          · 50 words
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          Your first <span className="text-wine italic">fifty</span> words.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          Fifty Judeo-Arabic words, picked because they&apos;re the ones
          you&apos;ll see most when you start reading Saadia. Each card has
          the JA form, the Arabic-script equivalent, what it means, and a
          link to the first real verse where it appears. Tap any number to
          jump.
        </p>
      </header>

      <div className="flex gap-2 mb-8">
        <ModeChip on={mode === "study"} onClick={() => setMode("study")}>
          Study
        </ModeChip>
        <ModeChip on={mode === "quiz"} onClick={() => setMode("quiz")}>
          Quiz
        </ModeChip>
      </div>

      {mode === "quiz" ? (
        <div className="rounded-md bg-page border border-ink/10 p-7">
          <p className="text-[13px] text-ink/65 leading-relaxed mb-1">
            Ten quick questions across all fifty words — meaning, recognition,
            and script. Miss some? Add them straight to your spaced-repetition
            review at the end.
          </p>
          <Quiz
            generate={() => generateVocabQuestion(entries)}
            onComplete={() => {
              markLessonDone("first-50");
              touchStreak();
            }}
            onAddMissed={(keys) =>
              keys.forEach((k) => setItemState(k, "learning"))
            }
            addMissedLabel="Add the words you missed to review"
          />
        </div>
      ) : (
        <>
          <div className="flex flex-wrap gap-2 mb-8 text-sm">
            <FilterPill
              on={filter === "all"}
              label={`All ${entries.length}`}
              onClick={() => setFilter("all")}
            />
            {groups.map((g) => (
              <FilterPill
                key={g}
                on={filter === g}
                label={GROUP_LABEL[g]}
                onClick={() => setFilter(g)}
              />
            ))}
          </div>

          {groups.map((g) => {
            if (filter !== "all" && filter !== g) return null;
            const groupEntries = entries.filter((e) => e.group === g);
            return (
              <section key={g} className="mb-12 last:mb-0">
                <h2 className="text-xs uppercase tracking-[0.25em] text-muted mb-2">
                  {GROUP_LABEL[g]}
                </h2>
                <p className="text-[13px] text-ink/65 leading-relaxed max-w-xl mb-5 italic">
                  {GROUP_HINT[g]}
                </p>
                <ol className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {groupEntries.map((e) => (
                    <WordCard
                      key={e.rank}
                      entry={e}
                      learning={hydrated && getState(e.lemma_ja) === "learning"}
                      onAdd={() => setState(e.lemma_ja, "learning")}
                    />
                  ))}
                </ol>
              </section>
            );
          })}
        </>
      )}
    </div>
  );
}

function ModeChip({
  on,
  onClick,
  children,
}: {
  on: boolean;
  onClick: () => void;
  children: React.ReactNode;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`px-4 py-1.5 rounded-md text-xs uppercase tracking-wider transition-all ${
        on ? "bg-ink text-page" : "bg-parchment text-ink/70 hover:text-wine"
      }`}
    >
      {children}
    </button>
  );
}

function WordCard({
  entry,
  learning,
  onAdd,
}: {
  entry: FirstFiftyEntry;
  learning: boolean;
  onAdd: () => void;
}) {
  return (
    <li className="group rounded-md bg-page border border-ink/10 p-5 hover:border-wine/30 transition-colors flex flex-col">
      <div className="flex items-start justify-between mb-3 gap-3">
        <span className="text-[10px] font-mono text-muted">
          #{String(entry.rank).padStart(2, "0")}
        </span>
        {entry.count > 0 && (
          <span
            className="text-[10px] uppercase tracking-[0.2em] text-muted"
            title={`${entry.count} occurrences across ${entry.n_verses} verses`}
          >
            {entry.count}× · {entry.n_verses}v
          </span>
        )}
      </div>

      <div dir="rtl" className="font-hebrew text-3xl text-ink leading-tight">
        {entry.lemma_ja}
      </div>
      <div
        dir="rtl"
        className="font-arabic text-2xl text-ink/70 leading-tight mt-1"
      >
        {entry.arabic}
      </div>

      <div className="mt-4 text-[15px] text-ink leading-relaxed">{entry.en}</div>
      {entry.he_echo && entry.he_echo !== "—" && (
        <div
          dir="rtl"
          className="font-hebrew text-base text-ink/70 mt-1"
          title="Hebrew echo / cognate"
        >
          {entry.he_echo}
        </div>
      )}

      {entry.root && (
        <div className="mt-2 text-[11px] text-muted font-mono">√{entry.root}</div>
      )}
      {entry.note && (
        <p className="mt-3 text-[12px] text-ink/75 leading-relaxed italic">
          {entry.note}
        </p>
      )}

      <div className="mt-4 flex items-center justify-between gap-3">
        {entry.first ? (
          <Link
            href={`/tafsir/${entry.first.book_slug}/${entry.first.ch}#verse-${entry.first.ch}-${entry.first.v}`}
            className="inline-flex items-baseline gap-1.5 text-[12px] text-wine hover:underline"
          >
            <span>
              See in {entry.first.book} {entry.first.ch}:{entry.first.v}
            </span>
            <span aria-hidden>→</span>
          </Link>
        ) : (
          <span />
        )}
        <button
          type="button"
          onClick={onAdd}
          disabled={learning}
          className={`shrink-0 text-[11px] uppercase tracking-wider px-2.5 py-1 rounded-full border transition-colors ${
            learning
              ? "border-amber-300 bg-amber-50 text-amber-700"
              : "border-ink/15 text-ink/60 hover:border-wine/50 hover:text-wine"
          }`}
          title="Add to your spaced-repetition review"
        >
          {learning ? "In review ✓" : "＋ Review"}
        </button>
      </div>
    </li>
  );
}

function FilterPill({
  on,
  label,
  onClick,
}: {
  on: boolean;
  label: string;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`px-3 py-1 rounded-full border text-xs uppercase tracking-wider transition-all ${
        on
          ? "bg-wine text-page border-wine"
          : "bg-page text-ink/70 border-ink/15 hover:border-wine/50 hover:text-wine"
      }`}
    >
      {label}
    </button>
  );
}

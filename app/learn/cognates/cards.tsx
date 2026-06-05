"use client";

import Link from "next/link";
import { useState } from "react";
import { Quiz, type QuizQuestion } from "@/components/Quiz";
import { deckKeyForCognate } from "@/lib/deck";
import { useWordStates } from "@/lib/wordState";
import { useProgress } from "@/lib/progress";

export type CognateEntry = {
  rank: number;
  modern_he: string;
  modern_translit: string;
  modern_en: string;
  arabic: string;
  arabic_translit: string;
  ja_form: string | null;
  story: string;
  group: string;
  count: number;
  n_verses: number;
  first: {
    book_slug: string;
    book: string;
    ch: number;
    v: number;
  } | null;
};

const GROUP_ORDER = [
  "slang",
  "body_parts",
  "family",
  "nature",
  "animals",
  "verbs",
  "false_friends",
] as const;
type Group = (typeof GROUP_ORDER)[number];

const GROUP_LABEL: Record<Group, string> = {
  slang: "Israeli slang from Arabic",
  body_parts: "Body parts",
  family: "Family",
  nature: "Sky, sea, sun",
  animals: "Animals",
  verbs: "Common verbs",
  false_friends: "False friends",
};

const GROUP_HINT: Record<Group, string> = {
  slang:
    "You use these every day. Each one is unmistakably Arabic — vocative particles, dual endings, classical roots. Israeli Hebrew is, in the end, a Mediterranean creole.",
  body_parts:
    "Most are one-to-one. Same three letters, same meaning, slightly different vowels. The mouth and the heart took divergent paths.",
  family:
    "The smallest, oldest words. Two letters apiece — and identical in both languages.",
  nature:
    "Sun, sea, sky, water, stars: same words in both languages. Fire and moon picked different roots — but the Hebrew word for 'lamp' (ner) and the Arabic word for fire (nar) tell on each other.",
  animals:
    "Domestic animals were named once and the names stuck. Kelev / kalb is exactly the same word.",
  verbs:
    "Hearing, writing, eating — the everyday verbs are shared. Sitting is where Arabic and Hebrew diverged.",
  false_friends:
    "Same letters, different meanings. The same Semitic root specialized differently in each language; the result is words that look identical and mean something else.",
};

/* ---------------- Quiz generator ---------------- */

function shuffle<T>(arr: T[]): T[] {
  return [...arr].sort(() => Math.random() - 0.5);
}

function pickDistractors(
  pool: CognateEntry[],
  answer: CognateEntry,
  valueOf: (e: CognateEntry) => string,
): CognateEntry[] {
  const seen = new Set([valueOf(answer)]);
  const out: CognateEntry[] = [];
  for (const e of shuffle(pool)) {
    const v = valueOf(e);
    if (seen.has(v)) continue;
    seen.add(v);
    out.push(e);
    if (out.length === 3) break;
  }
  return out;
}

type CQType = "he_to_ar" | "ar_to_he";

export function generateCognateQuestion(entries: CognateEntry[]): QuizQuestion {
  const types: CQType[] = ["he_to_ar", "ar_to_he"];
  const type = types[Math.floor(Math.random() * types.length)];
  const answer = entries[Math.floor(Math.random() * entries.length)];
  const reviewKey = deckKeyForCognate(answer.rank);

  if (type === "he_to_ar") {
    const choices = shuffle([
      answer,
      ...pickDistractors(entries, answer, (e) => e.arabic),
    ]);
    return {
      promptTop: {
        text: answer.modern_he,
        cls: "font-hebrew text-5xl text-ink",
        dir: "rtl",
      },
      promptHint: `${answer.modern_translit} · ${answer.modern_en}`,
      promptInstruction: "Which Arabic word is this Hebrew word from?",
      choices: choices.map((e) => ({
        value: e.arabic,
        cls: "font-arabic text-3xl text-ink",
        dir: "rtl",
      })),
      correctIdx: choices.indexOf(answer),
      explanation: `${answer.modern_he} ← ${answer.arabic} (${answer.arabic_translit})`,
      reviewKey,
    };
  }

  // ar_to_he
  const choices = shuffle([
    answer,
    ...pickDistractors(entries, answer, (e) => e.modern_he),
  ]);
  return {
    promptTop: {
      text: answer.arabic,
      cls: "font-arabic text-5xl text-wine",
      dir: "rtl",
    },
    promptHint: answer.arabic_translit,
    promptInstruction: "Which Hebrew word do you know from this Arabic one?",
    choices: choices.map((e) => ({
      value: e.modern_he,
      cls: "font-hebrew text-3xl text-ink",
      dir: "rtl",
    })),
    correctIdx: choices.indexOf(answer),
    explanation: `${answer.arabic} → ${answer.modern_he} (${answer.modern_en})`,
    reviewKey,
  };
}

export function CognateCards({ entries }: { entries: CognateEntry[] }) {
  const [filter, setFilter] = useState<Group | "all">("all");
  const [mode, setMode] = useState<"study" | "quiz">("study");
  const { setItemState, getItemState, hydrated } = useWordStates();
  const { markLessonDone, touchStreak } = useProgress();
  const groups = GROUP_ORDER.filter((g) => entries.some((e) => e.group === g));

  return (
    <div className="max-w-3xl mx-auto px-6 py-16 pb-32">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          <Link href="/learn" className="hover:text-wine">
            Learn
          </Link>{" "}
          · cognates
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          You already <span className="text-wine italic">know</span> this.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          Modern Hebrew speakers already know more Arabic than they think.
          Some of it&apos;s ancient — the body parts, the family, the
          ordinary verbs. Some of it&apos;s last Tuesday — yallah, sababa,
          basa. And some of it is where Saadia wrote a thousand years ago.
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
            Match the Hebrew you know to its Arabic source and back. Add the
            ones that trip you up to your review at the end.
          </p>
          <Quiz
            generate={() => generateCognateQuestion(entries)}
            onComplete={() => {
              markLessonDone("cognates");
              touchStreak();
            }}
            onAddMissed={(keys) =>
              keys.forEach((k) => setItemState(k, "learning"))
            }
            addMissedLabel="Add the ones you missed to review"
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
                    <CognateCard
                      key={e.rank}
                      entry={e}
                      learning={
                        hydrated &&
                        getItemState(deckKeyForCognate(e.rank)) === "learning"
                      }
                      onAdd={() =>
                        setItemState(deckKeyForCognate(e.rank), "learning")
                      }
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

function CognateCard({
  entry,
  learning,
  onAdd,
}: {
  entry: CognateEntry;
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
            title={`${entry.count} occurrences across ${entry.n_verses} verses in the Tafsir`}
          >
            {entry.count}× · {entry.n_verses}v
          </span>
        )}
      </div>

      <div className="text-[10px] uppercase tracking-[0.2em] text-muted mb-1">
        You know
      </div>
      <div dir="rtl" className="font-hebrew text-3xl text-ink leading-tight">
        {entry.modern_he}
      </div>
      <div className="text-[13px] text-ink/70 mt-1 font-mono">
        {entry.modern_translit} · {entry.modern_en}
      </div>

      <div className="my-4 border-t border-ink/10" />

      <div className="text-[10px] uppercase tracking-[0.2em] text-muted mb-1">
        It&apos;s Arabic
      </div>
      <div dir="rtl" className="font-arabic text-2xl text-ink/85 leading-tight">
        {entry.arabic}
      </div>
      <div className="text-[13px] text-ink/70 mt-1 font-mono">
        {entry.arabic_translit}
      </div>

      {entry.ja_form && (
        <>
          <div className="text-[10px] uppercase tracking-[0.2em] text-muted mt-4 mb-1">
            Saadia writes it
          </div>
          <div
            dir="rtl"
            className="font-hebrew text-xl text-ink/70 leading-tight"
          >
            {entry.ja_form}
          </div>
        </>
      )}

      {entry.story && (
        <p className="mt-4 text-[13px] text-ink/70 leading-relaxed">
          {entry.story}
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

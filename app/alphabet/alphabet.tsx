"use client";

import { useState } from "react";
import { Quiz, type QuizQuestion } from "@/components/Quiz";
import { deckKeyForLetter } from "@/lib/deck";
import { useWordStates } from "@/lib/wordState";
import { useProgress } from "@/lib/progress";

export type Letter = {
  ja: string;
  ar: string;
  phoneme: string;
  name: string;
  example_ja: string;
  example_ar: string;
  example_translit: string;
  example_gloss: string;
};

export type Lesson = {
  title: string;
  subtitle: string;
  intro: string;
  letters: Letter[];
  notes?: string[];
};

export type AlphabetData = {
  lessons: Record<string, Lesson>;
  future_lessons: { id: string; title: string; status: string }[];
};

type Mode = "study" | "drill";

export function AlphabetUI({ data }: { data: AlphabetData }) {
  const lessonIds = Object.keys(data.lessons);
  const [lessonId, setLessonId] = useState(lessonIds[0]);
  const [mode, setMode] = useState<Mode>("study");

  const ALL_LETTERS: Letter[] = lessonIds.flatMap((id) => data.lessons[id].letters);
  const isAllLessons = lessonId === "all";
  const lessonForDisplay: Lesson =
    isAllLessons
      ? {
          title: "All Lessons",
          subtitle: "Mixed practice across L1–L3",
          intro:
            "Practice questions are pulled from every lesson, with question types chosen to suit each letter.",
          letters: ALL_LETTERS,
        }
      : data.lessons[lessonId];

  return (
    <div className="max-w-3xl mx-auto px-6 py-10">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Stage 1
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          The <span className="text-wine italic">Alphabet</span>
        </h1>
        <p className="mt-4 text-base text-ink/70 leading-relaxed max-w-xl">
          Three lessons on the Hebrew letters used to write Arabic. Study the
          chart, then drill yourself across mixed question types: recognition,
          production, word meaning, and transliteration.
        </p>
      </header>

      <nav className="flex flex-wrap items-center gap-2 mb-6">
        <span className="text-[10px] uppercase tracking-[0.25em] text-muted mr-2">
          Lesson
        </span>
        {lessonIds.map((id) => (
          <button
            key={id}
            onClick={() => {
              setLessonId(id);
              setMode("study");
            }}
            className={`px-3 py-1 rounded-full border text-xs uppercase tracking-wider transition-all
              ${
                lessonId === id
                  ? "bg-wine text-page border-wine"
                  : "bg-page text-ink/70 border-ink/15 hover:border-wine/50 hover:text-wine"
              }`}
          >
            {id}. {data.lessons[id].title}
          </button>
        ))}
        <button
          onClick={() => {
            setLessonId("all");
            setMode("drill");
          }}
          className={`px-3 py-1 rounded-full border text-xs uppercase tracking-wider transition-all
            ${
              isAllLessons
                ? "bg-wine text-page border-wine"
                : "bg-page text-ink/70 border-ink/15 hover:border-wine/50 hover:text-wine"
            }`}
        >
          All · Mixed
        </button>
        {data.future_lessons.map((l) => (
          <button
            key={l.id}
            disabled
            className="px-3 py-1 rounded-full border text-xs uppercase tracking-wider opacity-40 cursor-not-allowed bg-page text-ink/70 border-ink/15"
          >
            {l.id}. {l.title} <span className="opacity-70">(soon)</span>
          </button>
        ))}
      </nav>

      <section className="rounded-md bg-page border border-ink/10 p-7">
        <div className="text-[11px] uppercase tracking-[0.25em] text-muted mb-2">
          {lessonForDisplay.subtitle}
        </div>
        <h2 className="text-2xl text-ink mb-4">{lessonForDisplay.title}</h2>
        <p className="text-[15px] text-ink/75 leading-relaxed">
          {lessonForDisplay.intro}
        </p>

        {!isAllLessons && (
          <div className="flex gap-2 mt-6 mb-2">
            <ModeChip on={mode === "study"} onClick={() => setMode("study")}>
              Study
            </ModeChip>
            <ModeChip on={mode === "drill"} onClick={() => setMode("drill")}>
              Practice
            </ModeChip>
          </div>
        )}

        {mode === "study" && !isAllLessons && (
          <StudyChart
            letters={lessonForDisplay.letters}
            notes={lessonForDisplay.notes}
          />
        )}
        {(mode === "drill" || isAllLessons) && (
          <Drill
            key={lessonId}
            lessonLetters={lessonForDisplay.letters}
            allLetters={ALL_LETTERS}
            lessonId={lessonId}
          />
        )}
      </section>
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
      onClick={onClick}
      className={`px-3 py-1.5 rounded-md text-xs uppercase tracking-wider transition-all
        ${
          on
            ? "bg-ink text-page"
            : "bg-parchment text-ink/70 hover:bg-wine-50 hover:text-wine"
        }`}
    >
      {children}
    </button>
  );
}

function StudyChart({
  letters,
  notes,
}: {
  letters: Letter[];
  notes?: string[];
}) {
  const { setItemState, getItemState, hydrated } = useWordStates();
  return (
    <>
      <ul className="mt-6 grid grid-cols-2 sm:grid-cols-3 gap-3">
        {letters.map((L) => {
          const key = deckKeyForLetter(L.ja);
          const learning = hydrated && getItemState(key) === "learning";
          return (
          <li
            key={L.ja + L.ar + L.name}
            className="rounded-md border border-ink/10 p-3 hover:border-wine/30 hover:bg-wine-50/30 transition-colors group"
          >
            <div className="flex items-baseline justify-between mb-1.5">
              <span
                className="font-hebrew text-3xl text-ink leading-none"
                dir="rtl"
              >
                {L.ja}
              </span>
              <span
                className="font-arabic text-3xl text-wine/80 leading-none"
                dir="rtl"
              >
                {L.ar}
              </span>
            </div>
            <div className="text-xs text-muted mb-1">{L.name}</div>
            <div className="text-xs text-ink/70 font-mono mb-2">/{L.phoneme}/</div>
            <div className="border-t border-ink/10 pt-2 text-[11px]">
              <div className="flex items-baseline gap-2" dir="rtl">
                <span className="font-hebrew text-base text-ink">
                  {L.example_ja}
                </span>
                <span className="font-arabic text-sm text-ink/70">
                  {L.example_ar}
                </span>
              </div>
              <div
                className="font-mono text-ink/80 mt-0.5 tracking-tight"
                dir="ltr"
              >
                {L.example_translit}
              </div>
              <div className="text-ink/75 italic" dir="ltr">
                {L.example_gloss}
              </div>
            </div>
            <button
              type="button"
              onClick={() => setItemState(key, "learning")}
              disabled={learning}
              className={`mt-2 w-full text-[10px] uppercase tracking-wider px-2 py-1 rounded-full border transition-colors ${
                learning
                  ? "border-amber-300 bg-amber-50 text-amber-700"
                  : "border-ink/15 text-ink/55 hover:border-wine/50 hover:text-wine"
              }`}
              title="Add this letter's example word to your review"
            >
              {learning ? "In review ✓" : "＋ Review"}
            </button>
          </li>
          );
        })}
      </ul>
      {notes && notes.length > 0 && (
        <div className="mt-6 border-l-2 border-wine/40 pl-4 space-y-2">
          {notes.map((n, i) => (
            <p key={i} className="text-[13px] text-muted leading-relaxed italic">
              {n}
            </p>
          ))}
        </div>
      )}
    </>
  );
}

/* ---------------- Drill engine ---------------- */

type QType =
  | "letter_to_ar"      // JA letter → Arabic letter
  | "ar_to_letter"      // Arabic letter → JA letter
  | "word_to_gloss"     // JA word → English meaning
  | "word_to_translit"  // JA word → transliteration
  | "ar_word_to_ja";    // Arabic-script word → JA-script word

type Question = {
  type: QType;
  promptTop: { text: string; cls: string; dir?: "rtl" | "ltr" };
  promptHint?: string;
  promptInstruction: string;
  choices: { value: string; cls: string; dir?: "rtl" | "ltr" }[];
  correctIdx: number;
  explanation: string;
  answer: Letter;
};

const ALLOWED_TYPES_BY_LESSON: Record<string, QType[]> = {
  "1": ["letter_to_ar", "ar_to_letter", "word_to_gloss", "word_to_translit"],
  "2": ["letter_to_ar", "ar_to_letter", "word_to_gloss", "word_to_translit"],
  // L3 has only 3 entries, all variations of אל = ال — letter-level
  // questions don't work. Focus on word-level questions.
  "3": ["word_to_gloss", "word_to_translit", "ar_word_to_ja"],
  all: [
    "letter_to_ar",
    "ar_to_letter",
    "word_to_gloss",
    "word_to_translit",
    "ar_word_to_ja",
  ],
};

function pickN<T>(pool: T[], n: number): T[] {
  const shuffled = [...pool].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, n);
}

function distinctByKey<T>(items: T[], key: (t: T) => string): T[] {
  const seen = new Set<string>();
  const out: T[] = [];
  for (const it of items) {
    const k = key(it);
    if (!seen.has(k)) {
      seen.add(k);
      out.push(it);
    }
  }
  return out;
}

function generateQuestion(
  lessonLetters: Letter[],
  allLetters: Letter[],
  lessonId: string,
): Question {
  const types = ALLOWED_TYPES_BY_LESSON[lessonId] ?? ALLOWED_TYPES_BY_LESSON["1"];
  const type = types[Math.floor(Math.random() * types.length)];
  const answer = lessonLetters[Math.floor(Math.random() * lessonLetters.length)];

  const baseShuffle = <T extends { value: string }>(
    correct: T,
    pool: T[],
  ): { values: T[]; correctIdx: number } => {
    const distractorPool = distinctByKey(
      pool.filter((p) => p.value !== correct.value),
      (p) => p.value,
    );
    const distractors = pickN(distractorPool, 3);
    const arr = [correct, ...distractors];
    const shuffled = arr.sort(() => Math.random() - 0.5);
    return { values: shuffled, correctIdx: shuffled.indexOf(correct) };
  };

  if (type === "letter_to_ar") {
    const correct = { value: answer.ar };
    const pool = allLetters.map((l) => ({ value: l.ar }));
    const { values, correctIdx } = baseShuffle(correct, pool);
    return {
      type,
      promptTop: {
        text: answer.ja,
        cls: "font-hebrew text-7xl text-ink",
        dir: "rtl",
      },
      promptInstruction:
        "Which Arabic letter does this Judeo-Arabic letter represent?",
      choices: values.map((v) => ({
        value: v.value,
        cls: "font-arabic text-4xl",
        dir: "rtl",
      })),
      correctIdx,
      explanation: `${answer.name} · /${answer.phoneme}/`,
      answer,
    };
  }

  if (type === "ar_to_letter") {
    const correct = { value: answer.ja };
    const pool = allLetters.map((l) => ({ value: l.ja }));
    const { values, correctIdx } = baseShuffle(correct, pool);
    return {
      type,
      promptTop: {
        text: answer.ar,
        cls: "font-arabic text-7xl text-wine",
        dir: "rtl",
      },
      promptHint: `/${answer.phoneme}/`,
      promptInstruction:
        "Which Hebrew letter writes this Arabic phoneme in Judeo-Arabic?",
      choices: values.map((v) => ({
        value: v.value,
        cls: "font-hebrew text-4xl text-ink",
        dir: "rtl",
      })),
      correctIdx,
      explanation: `${answer.name}`,
      answer,
    };
  }

  if (type === "word_to_gloss") {
    const correct = { value: answer.example_gloss };
    const pool = allLetters.map((l) => ({ value: l.example_gloss }));
    const { values, correctIdx } = baseShuffle(correct, pool);
    return {
      type,
      promptTop: {
        text: answer.example_ja,
        cls: "font-hebrew text-5xl text-ink",
        dir: "rtl",
      },
      promptHint: answer.example_translit,
      promptInstruction: "What does this Judeo-Arabic word mean?",
      choices: values.map((v) => ({
        value: v.value,
        cls: "text-base text-ink italic",
        dir: "ltr",
      })),
      correctIdx,
      explanation: `${answer.example_ja} (${answer.example_ar}) — featuring ${answer.name}`,
      answer,
    };
  }

  if (type === "word_to_translit") {
    const correct = { value: answer.example_translit };
    const pool = allLetters.map((l) => ({ value: l.example_translit }));
    const { values, correctIdx } = baseShuffle(correct, pool);
    return {
      type,
      promptTop: {
        text: answer.example_ja,
        cls: "font-hebrew text-5xl text-ink",
        dir: "rtl",
      },
      promptInstruction: "How is this Judeo-Arabic word transliterated?",
      choices: values.map((v) => ({
        value: v.value,
        cls: "font-mono text-base text-ink",
        dir: "ltr",
      })),
      correctIdx,
      explanation: `${answer.example_ja} = ${answer.example_ar} = "${answer.example_gloss}" — featuring ${answer.name}`,
      answer,
    };
  }

  // ar_word_to_ja
  const correct = { value: answer.example_ja };
  const pool = allLetters.map((l) => ({ value: l.example_ja }));
  const { values, correctIdx } = baseShuffle(correct, pool);
  return {
    type,
    promptTop: {
      text: answer.example_ar,
      cls: "font-arabic text-5xl text-wine",
      dir: "rtl",
    },
    promptHint: `${answer.example_translit} — "${answer.example_gloss}"`,
    promptInstruction:
      "How is this Arabic word written in Judeo-Arabic?",
    choices: values.map((v) => ({
      value: v.value,
      cls: "font-hebrew text-3xl text-ink",
      dir: "rtl",
    })),
    correctIdx,
    explanation: `${answer.example_ja} — featuring ${answer.name}`,
    answer,
  };
}

function Drill({
  lessonLetters,
  allLetters,
  lessonId,
}: {
  lessonLetters: Letter[];
  allLetters: Letter[];
  lessonId: string;
}) {
  const { setItemState } = useWordStates();
  const { markLessonDone, touchStreak } = useProgress();

  const generate = (): QuizQuestion => {
    const q = generateQuestion(lessonLetters, allLetters, lessonId);
    return {
      promptTop: q.promptTop,
      promptHint: q.promptHint,
      promptInstruction: q.promptInstruction,
      choices: q.choices,
      correctIdx: q.correctIdx,
      explanation: q.explanation,
      reviewKey: deckKeyForLetter(q.answer.ja),
    };
  };

  return (
    <Quiz
      generate={generate}
      onComplete={() => {
        markLessonDone("alphabet");
        touchStreak();
      }}
      onAddMissed={(keys) => keys.forEach((k) => setItemState(k, "learning"))}
      addMissedLabel="Add the letters you missed to review"
    />
  );
}

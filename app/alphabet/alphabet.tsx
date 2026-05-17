"use client";

import { useMemo, useState } from "react";

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

type Mode = "study" | "recognition" | "production";

export function AlphabetUI({ data }: { data: AlphabetData }) {
  const lessonIds = Object.keys(data.lessons);
  const [lessonId, setLessonId] = useState(lessonIds[0]);
  const [mode, setMode] = useState<Mode>("study");

  const lesson = data.lessons[lessonId];

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
          Five lessons on the Hebrew letters used to write Arabic. Study the
          chart, then drill yourself on recognition (JA → Arabic) and
          production (Arabic → JA).
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
        {data.future_lessons.map((l) => (
          <button
            key={l.id}
            disabled
            className="px-3 py-1 rounded-full border text-xs uppercase tracking-wider opacity-40 cursor-not-allowed bg-page text-ink/70 border-ink/15"
          >
            {l.id}. {l.title}{" "}
            <span className="opacity-70">(soon)</span>
          </button>
        ))}
      </nav>

      <section className="rounded-md bg-page border border-ink/10 p-7">
        <div className="text-[11px] uppercase tracking-[0.25em] text-muted mb-2">
          {lesson.subtitle}
        </div>
        <h2 className="text-2xl text-ink mb-4">{lesson.title}</h2>
        <p className="text-[15px] text-ink/75 leading-relaxed">{lesson.intro}</p>

        <div className="flex gap-2 mt-6 mb-2">
          <ModeChip on={mode === "study"} onClick={() => setMode("study")}>
            Study
          </ModeChip>
          <ModeChip
            on={mode === "recognition"}
            onClick={() => setMode("recognition")}
          >
            Recognition
          </ModeChip>
          <ModeChip
            on={mode === "production"}
            onClick={() => setMode("production")}
          >
            Production
          </ModeChip>
        </div>

        {mode === "study" && (
          <StudyChart letters={lesson.letters} notes={lesson.notes} />
        )}
        {mode === "recognition" && (
          <RecognitionDrill key={lessonId} letters={lesson.letters} />
        )}
        {mode === "production" && (
          <ProductionDrill key={lessonId} letters={lesson.letters} />
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
  return (
    <>
      <ul className="mt-6 grid grid-cols-2 sm:grid-cols-3 gap-3">
        {letters.map((L) => (
          <li
            key={L.ja + L.ar}
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
            <div className="text-xs text-ink/60 font-mono mb-2">/{L.phoneme}/</div>
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
              <div className="text-ink/60 italic" dir="ltr">
                {L.example_gloss}
              </div>
            </div>
          </li>
        ))}
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

type DrillState = {
  q: number;
  total: number;
  correct: number;
  choices: Letter[];
  answer: Letter;
  selected: number | null;
  done: boolean;
};

function makeDrillState(letters: Letter[]): DrillState {
  const shuffled = [...letters].sort(() => Math.random() - 0.5);
  const answer = shuffled[0];
  const others = shuffled.slice(1, 4);
  const choices = [answer, ...others].sort(() => Math.random() - 0.5);
  return {
    q: 1,
    total: Math.min(letters.length, 10),
    correct: 0,
    choices,
    answer,
    selected: null,
    done: false,
  };
}

function RecognitionDrill({ letters }: { letters: Letter[] }) {
  const [state, setState] = useState<DrillState>(() => makeDrillState(letters));

  const submit = (i: number) => {
    if (state.selected !== null) return;
    const wasCorrect = state.choices[i] === state.answer;
    setState((s) => ({
      ...s,
      selected: i,
      correct: s.correct + (wasCorrect ? 1 : 0),
    }));
  };

  const next = () => {
    if (state.q >= state.total) {
      setState((s) => ({ ...s, done: true }));
      return;
    }
    const fresh = makeDrillState(letters);
    setState((s) => ({
      ...fresh,
      q: s.q + 1,
      total: s.total,
      correct: s.correct,
    }));
  };

  const restart = () => setState(makeDrillState(letters));

  if (state.done) {
    return (
      <DrillSummary
        correct={state.correct}
        total={state.total}
        onRestart={restart}
      />
    );
  }

  return (
    <div className="mt-6">
      <DrillHeader q={state.q} total={state.total} correct={state.correct} />
      <p className="text-sm text-muted mt-4 mb-2">
        Which Arabic letter does this Judeo-Arabic letter represent?
      </p>
      <div className="flex justify-center my-8">
        <div
          dir="rtl"
          className="font-hebrew text-7xl text-ink leading-none"
        >
          {state.answer.ja}
        </div>
      </div>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        {state.choices.map((c, i) => {
          const isPicked = state.selected === i;
          const isAnswer = c === state.answer;
          const showResult = state.selected !== null;
          let cls = "border-ink/15 bg-page hover:border-wine/40";
          if (showResult) {
            if (isAnswer) cls = "border-wine bg-wine-50 text-wine-700";
            else if (isPicked) cls = "border-ink/30 bg-ink/5 text-ink/50 line-through";
            else cls = "border-ink/10 opacity-60";
          }
          return (
            <button
              key={i}
              onClick={() => submit(i)}
              disabled={state.selected !== null}
              className={`rounded-md border p-5 transition-all flex items-center justify-center ${cls}`}
            >
              <span dir="rtl" className="font-arabic text-4xl">
                {c.ar}
              </span>
            </button>
          );
        })}
      </div>
      {state.selected !== null && (
        <div className="mt-5 flex items-center justify-between">
          <p className="text-sm text-muted">
            {state.choices[state.selected] === state.answer
              ? "Correct."
              : "Not quite — the right answer is highlighted."}{" "}
            <span className="text-ink/70">
              {state.answer.name} · /{state.answer.phoneme}/
            </span>
          </p>
          <button
            onClick={next}
            className="px-4 py-2 rounded-md bg-wine text-page text-xs uppercase tracking-wider hover:bg-wine-700 transition-colors"
          >
            {state.q >= state.total ? "Finish" : "Next →"}
          </button>
        </div>
      )}
    </div>
  );
}

function ProductionDrill({ letters }: { letters: Letter[] }) {
  const [state, setState] = useState<DrillState>(() => makeDrillState(letters));

  const submit = (i: number) => {
    if (state.selected !== null) return;
    const wasCorrect = state.choices[i] === state.answer;
    setState((s) => ({
      ...s,
      selected: i,
      correct: s.correct + (wasCorrect ? 1 : 0),
    }));
  };

  const next = () => {
    if (state.q >= state.total) {
      setState((s) => ({ ...s, done: true }));
      return;
    }
    const fresh = makeDrillState(letters);
    setState((s) => ({
      ...fresh,
      q: s.q + 1,
      total: s.total,
      correct: s.correct,
    }));
  };

  const restart = () => setState(makeDrillState(letters));

  if (state.done) {
    return (
      <DrillSummary
        correct={state.correct}
        total={state.total}
        onRestart={restart}
      />
    );
  }

  return (
    <div className="mt-6">
      <DrillHeader q={state.q} total={state.total} correct={state.correct} />
      <p className="text-sm text-muted mt-4 mb-2">
        Which Hebrew letter writes this Arabic phoneme in Judeo-Arabic?
      </p>
      <div className="flex flex-col items-center my-8 gap-2">
        <div
          dir="rtl"
          className="font-arabic text-7xl text-wine leading-none"
        >
          {state.answer.ar}
        </div>
        <div className="text-xs text-muted font-mono">
          /{state.answer.phoneme}/
        </div>
      </div>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        {state.choices.map((c, i) => {
          const isPicked = state.selected === i;
          const isAnswer = c === state.answer;
          const showResult = state.selected !== null;
          let cls = "border-ink/15 bg-page hover:border-wine/40";
          if (showResult) {
            if (isAnswer) cls = "border-wine bg-wine-50 text-wine-700";
            else if (isPicked) cls = "border-ink/30 bg-ink/5 text-ink/50 line-through";
            else cls = "border-ink/10 opacity-60";
          }
          return (
            <button
              key={i}
              onClick={() => submit(i)}
              disabled={state.selected !== null}
              className={`rounded-md border p-5 transition-all flex items-center justify-center ${cls}`}
            >
              <span dir="rtl" className="font-hebrew text-4xl text-ink">
                {c.ja}
              </span>
            </button>
          );
        })}
      </div>
      {state.selected !== null && (
        <div className="mt-5 flex items-center justify-between">
          <p className="text-sm text-muted">
            {state.choices[state.selected] === state.answer
              ? "Correct."
              : "Not quite — the right answer is highlighted."}{" "}
            <span className="text-ink/70">{state.answer.name}</span>
          </p>
          <button
            onClick={next}
            className="px-4 py-2 rounded-md bg-wine text-page text-xs uppercase tracking-wider hover:bg-wine-700 transition-colors"
          >
            {state.q >= state.total ? "Finish" : "Next →"}
          </button>
        </div>
      )}
    </div>
  );
}

function DrillHeader({
  q,
  total,
  correct,
}: {
  q: number;
  total: number;
  correct: number;
}) {
  return (
    <div className="flex items-center justify-between text-xs uppercase tracking-widest text-muted">
      <span>
        Q {q} / {total}
      </span>
      <span>Score: {correct}</span>
    </div>
  );
}

function DrillSummary({
  correct,
  total,
  onRestart,
}: {
  correct: number;
  total: number;
  onRestart: () => void;
}) {
  const pct = Math.round((correct / total) * 100);
  return (
    <div className="mt-8 text-center">
      <div className="text-xs uppercase tracking-[0.3em] text-muted mb-2">
        Result
      </div>
      <div className="text-5xl text-wine font-serif">{pct}%</div>
      <p className="text-sm text-ink/70 mt-2">
        {correct} / {total} correct.
      </p>
      <button
        onClick={onRestart}
        className="mt-6 px-5 py-2 rounded-md bg-wine text-page text-xs uppercase tracking-wider hover:bg-wine-700 transition-colors"
      >
        Practice again
      </button>
    </div>
  );
}

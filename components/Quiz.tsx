"use client";

import { useState } from "react";

// A single multiple-choice question. Generic over content — generators for
// letters, vocabulary, and cognates all produce this shape. `reviewKey` is the
// canonical deck key for the item under test, used by "add the ones you missed".
export type QuizQuestion = {
  promptTop: { text: string; cls: string; dir?: "rtl" | "ltr" };
  promptHint?: string;
  promptInstruction: string;
  choices: { value: string; cls: string; dir?: "rtl" | "ltr" }[];
  correctIdx: number;
  explanation: string;
  reviewKey?: string;
};

export type QuizGenerator = () => QuizQuestion;

type QuizState = {
  q: number;
  total: number;
  correct: number;
  question: QuizQuestion;
  selected: number | null;
  done: boolean;
  missed: string[]; // reviewKeys answered wrong
};

export function Quiz({
  generate,
  total = 10,
  onComplete,
  onAddMissed,
  addMissedLabel = "Add the ones you missed to review",
}: {
  generate: QuizGenerator;
  total?: number;
  onComplete?: (correct: number, total: number, missedKeys: string[]) => void;
  onAddMissed?: (keys: string[]) => void;
  addMissedLabel?: string;
}) {
  const [state, setState] = useState<QuizState>(() => ({
    q: 1,
    total,
    correct: 0,
    question: generate(),
    selected: null,
    done: false,
    missed: [],
  }));

  const submit = (i: number) => {
    if (state.selected !== null) return;
    const wasCorrect = i === state.question.correctIdx;
    setState((s) => ({
      ...s,
      selected: i,
      correct: s.correct + (wasCorrect ? 1 : 0),
      missed:
        !wasCorrect && s.question.reviewKey
          ? [...s.missed, s.question.reviewKey]
          : s.missed,
    }));
  };

  const next = () => {
    if (state.q >= state.total) {
      setState((s) => {
        onComplete?.(s.correct, s.total, s.missed);
        return { ...s, done: true };
      });
      return;
    }
    setState((s) => ({
      ...s,
      q: s.q + 1,
      question: generate(),
      selected: null,
    }));
  };

  const restart = () =>
    setState({
      q: 1,
      total,
      correct: 0,
      question: generate(),
      selected: null,
      done: false,
      missed: [],
    });

  if (state.done) {
    return (
      <QuizSummary
        correct={state.correct}
        total={state.total}
        missed={state.missed}
        onRestart={restart}
        onAddMissed={onAddMissed}
        addMissedLabel={addMissedLabel}
      />
    );
  }

  const q = state.question;

  return (
    <div className="mt-6">
      <div className="flex items-center justify-between text-xs uppercase tracking-widest text-muted">
        <span>
          Q {state.q} / {state.total}
        </span>
        <span>Score: {state.correct}</span>
      </div>

      <p className="text-sm text-muted mt-4 mb-2">{q.promptInstruction}</p>
      <div className="flex flex-col items-center my-8 gap-2">
        <div dir={q.promptTop.dir} className={`${q.promptTop.cls} leading-none`}>
          {q.promptTop.text}
        </div>
        {q.promptHint && (
          <div className="text-xs text-muted font-mono italic">
            {q.promptHint}
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {q.choices.map((c, i) => {
          const isPicked = state.selected === i;
          const isAnswer = i === q.correctIdx;
          const showResult = state.selected !== null;
          let cls = "border-ink/15 bg-page hover:border-wine/40";
          if (showResult) {
            if (isAnswer) cls = "border-wine bg-wine-50 text-wine-700";
            else if (isPicked)
              cls = "border-ink/30 bg-ink/5 text-ink/65 line-through";
            else cls = "border-ink/10 opacity-60";
          }
          return (
            <button
              key={i}
              onClick={() => submit(i)}
              disabled={state.selected !== null}
              className={`rounded-md border p-4 transition-all flex items-center justify-center min-h-[64px] ${cls}`}
            >
              <span dir={c.dir} className={c.cls}>
                {c.value}
              </span>
            </button>
          );
        })}
      </div>

      {state.selected !== null && (
        <div className="mt-5 flex items-start justify-between gap-3">
          <p className="text-sm text-muted flex-1">
            <span className="font-semibold text-ink">
              {state.selected === q.correctIdx
                ? "Correct."
                : "Not quite — answer highlighted."}
            </span>{" "}
            <span className="text-ink/70">{q.explanation}</span>
          </p>
          <button
            onClick={next}
            className="px-4 py-2 rounded-md bg-wine text-page text-xs uppercase tracking-wider hover:bg-wine-700 transition-colors shrink-0"
          >
            {state.q >= state.total ? "Finish" : "Next →"}
          </button>
        </div>
      )}
    </div>
  );
}

function QuizSummary({
  correct,
  total,
  missed,
  onRestart,
  onAddMissed,
  addMissedLabel,
}: {
  correct: number;
  total: number;
  missed: string[];
  onRestart: () => void;
  onAddMissed?: (keys: string[]) => void;
  addMissedLabel: string;
}) {
  const [added, setAdded] = useState(false);
  const pct = Math.round((correct / total) * 100);
  const uniqueMissed = Array.from(new Set(missed));

  return (
    <div className="mt-6 rounded-md bg-parchment border border-ink/10 p-8 text-center">
      <p className="text-xs uppercase tracking-[0.25em] text-muted">Round complete</p>
      <p className="mt-3 text-4xl text-ink tracking-tight">
        {correct} <span className="text-muted text-2xl">/ {total}</span>
      </p>
      <p className="mt-1 text-sm text-muted">{pct}% correct</p>

      <div className="mt-7 flex flex-wrap gap-3 justify-center">
        <button
          onClick={onRestart}
          className="px-4 py-2 rounded-full bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine-700 transition-colors"
        >
          Again
        </button>
        {onAddMissed && uniqueMissed.length > 0 && (
          <button
            onClick={() => {
              onAddMissed(uniqueMissed);
              setAdded(true);
            }}
            disabled={added}
            className="px-4 py-2 rounded-full border border-ink/15 text-ink/70 text-sm uppercase tracking-wider hover:border-wine/50 hover:text-wine transition-colors disabled:opacity-50"
          >
            {added
              ? `Added ${uniqueMissed.length} ✓`
              : `${addMissedLabel} (${uniqueMissed.length})`}
          </button>
        )}
      </div>
    </div>
  );
}

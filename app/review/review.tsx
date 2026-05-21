"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import { Rating, type Grade } from "ts-fsrs";
import { lookup, type Entry } from "@/lib/lookup";
import { useWordStates } from "@/lib/wordState";

export function ReviewSession() {
  const { hydrated, dueKeys, gradeCard, counts } = useWordStates();
  const [queue, setQueue] = useState<string[] | null>(null);
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);

  // Snapshot the due-keys on first hydration so the queue doesn't shift mid-session.
  useEffect(() => {
    if (hydrated && queue === null) {
      setQueue([...dueKeys]);
    }
  }, [hydrated, dueKeys, queue]);

  if (!hydrated || queue === null) {
    return <Shell><Loading /></Shell>;
  }

  if (queue.length === 0) {
    return (
      <Shell>
        <EmptyState
          totalLearning={counts.learning}
          totalKnown={counts.known}
        />
      </Shell>
    );
  }

  if (index >= queue.length) {
    return (
      <Shell>
        <DoneState count={queue.length} />
      </Shell>
    );
  }

  const current = queue[index];
  const entries = lookup(current);

  const onGrade = (grade: Grade) => {
    gradeCard(current, grade);
    setRevealed(false);
    setIndex((i) => i + 1);
  };

  const onSkip = () => {
    setRevealed(false);
    setIndex((i) => i + 1);
  };

  return (
    <Shell>
      <Progress index={index} total={queue.length} />
      <Card
        token={current}
        entries={entries}
        revealed={revealed}
        onReveal={() => setRevealed(true)}
        onGrade={onGrade}
        onSkip={onSkip}
      />
    </Shell>
  );
}

function Shell({ children }: { children: React.ReactNode }) {
  return (
    <div className="max-w-2xl mx-auto px-6 py-10">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Daily practice
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          <span className="italic text-wine">Review</span>
        </h1>
      </header>
      {children}
    </div>
  );
}

function Loading() {
  return <p className="text-muted">Loading…</p>;
}

function EmptyState({
  totalLearning,
  totalKnown,
}: {
  totalLearning: number;
  totalKnown: number;
}) {
  return (
    <div className="rounded-md bg-page border border-ink/10 p-10 text-center">
      <p className="text-ink/80 text-lg leading-relaxed">
        {totalLearning === 0 ? (
          <>
            Nothing to review yet. Open a reader, tap a word, and mark it{" "}
            <span className="text-amber-700 font-medium">Learning</span> to add
            it to your queue.
          </>
        ) : (
          <>
            All caught up. Next review will arrive when the scheduler says so.
          </>
        )}
      </p>
      <p className="mt-6 text-xs uppercase tracking-[0.25em] text-muted">
        {totalLearning} in queue · {totalKnown} known
      </p>
      <div className="mt-8 flex gap-3 justify-center">
        <Link
          href="/tafsir"
          className="px-4 py-2 rounded-full bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine/90 transition-colors"
        >
          Open Tafsir
        </Link>
        <Link
          href="/advanced"
          className="px-4 py-2 rounded-full border border-ink/15 text-ink/70 text-sm uppercase tracking-wider hover:border-wine/50 hover:text-wine transition-colors"
        >
          Open Bahya
        </Link>
      </div>
    </div>
  );
}

function DoneState({ count }: { count: number }) {
  return (
    <div className="rounded-md bg-page border border-ink/10 p-10 text-center">
      <p className="text-3xl tracking-tight text-ink">Done for now.</p>
      <p className="mt-3 text-ink/70">
        {count} {count === 1 ? "word" : "words"} reviewed. Come back when the
        next batch is due.
      </p>
      <div className="mt-8 flex gap-3 justify-center">
        <Link
          href="/"
          className="px-4 py-2 rounded-full bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine/90 transition-colors"
        >
          Home
        </Link>
      </div>
    </div>
  );
}

function Progress({ index, total }: { index: number; total: number }) {
  const pct = Math.round((index / total) * 100);
  return (
    <div className="mb-6">
      <div className="flex justify-between text-[10px] uppercase tracking-[0.25em] text-muted mb-2">
        <span>
          {index + 1} of {total}
        </span>
        <span>{pct}%</span>
      </div>
      <div className="h-1 rounded-full bg-ink/10 overflow-hidden">
        <div
          className="h-full bg-wine transition-all"
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}

function Card({
  token,
  entries,
  revealed,
  onReveal,
  onGrade,
  onSkip,
}: {
  token: string;
  entries: Entry[];
  revealed: boolean;
  onReveal: () => void;
  onGrade: (g: Grade) => void;
  onSkip: () => void;
}) {
  return (
    <div className="rounded-md bg-page border border-ink/10 p-10 min-h-[24rem] flex flex-col">
      <div className="flex-1 flex flex-col items-center justify-center text-center">
        <span
          className="font-hebrew text-5xl sm:text-6xl text-ink leading-tight"
          dir="rtl"
        >
          {token}
        </span>

        {revealed && (
          <div className="mt-10 w-full max-w-md">
            {entries.length === 0 ? (
              <p className="text-sm text-muted italic">
                No dictionary entry — grade from memory.
              </p>
            ) : (
              <ul className="space-y-4" dir="rtl">
                {entries.map((e) => (
                  <li
                    key={e.id}
                    className="border-r-2 border-wine/40 pr-4 pl-2"
                  >
                    <div className="flex items-baseline gap-3 flex-wrap">
                      {e.lemma_ar && (
                        <span className="font-arabic text-lg text-ink/70">
                          {e.lemma_ar}
                        </span>
                      )}
                      {e.root && (
                        <span className="text-xs text-muted font-mono">
                          √{e.root}
                        </span>
                      )}
                      {e.pos && (
                        <span className="text-xs text-muted italic">
                          {e.pos}
                        </span>
                      )}
                      {e.source && (
                        <span
                          className="text-[10px] uppercase tracking-[0.2em] text-ink/70 border border-ink/15 rounded-sm px-1.5 py-0.5 ml-auto"
                          title="Auto-extracted; verify before citing"
                        >
                          {e.source}
                        </span>
                      )}
                    </div>
                    {e.gloss_en && (
                      <p
                        dir="ltr"
                        className={`mt-1.5 text-ink text-left ${
                          e.source
                            ? "text-[13px] leading-relaxed"
                            : "text-[15px]"
                        }`}
                      >
                        {e.gloss_en}
                      </p>
                    )}
                    {e.gloss_he && (
                      <p className="font-hebrew text-base text-muted mt-0.5">
                        {e.gloss_he}
                      </p>
                    )}
                  </li>
                ))}
              </ul>
            )}
          </div>
        )}
      </div>

      <div className="mt-8 pt-6 border-t border-ink/10">
        {!revealed ? (
          <div className="flex gap-3">
            <button
              type="button"
              onClick={onReveal}
              className="flex-1 px-4 py-3 rounded-md bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine/90 transition-colors"
            >
              Show answer
            </button>
            <button
              type="button"
              onClick={onSkip}
              className="px-4 py-3 rounded-md border border-ink/15 text-ink/70 text-sm uppercase tracking-wider hover:border-wine/40 hover:text-wine transition-colors"
              title="Skip without scoring"
            >
              Skip
            </button>
          </div>
        ) : (
          <div className="grid grid-cols-4 gap-2">
            <GradeButton
              label="Again"
              hint="Forgot"
              color="bg-rose-700 hover:bg-rose-800"
              onClick={() => onGrade(Rating.Again)}
            />
            <GradeButton
              label="Hard"
              hint="Recalled with effort"
              color="bg-amber-600 hover:bg-amber-700"
              onClick={() => onGrade(Rating.Hard)}
            />
            <GradeButton
              label="Good"
              hint="Recalled"
              color="bg-emerald-700 hover:bg-emerald-800"
              onClick={() => onGrade(Rating.Good)}
            />
            <GradeButton
              label="Easy"
              hint="Trivial"
              color="bg-sky-700 hover:bg-sky-800"
              onClick={() => onGrade(Rating.Easy)}
            />
          </div>
        )}
      </div>
    </div>
  );
}

function GradeButton({
  label,
  hint,
  color,
  onClick,
}: {
  label: string;
  hint: string;
  color: string;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      title={hint}
      className={`${color} text-page px-3 py-3 rounded-md text-sm uppercase tracking-wider transition-colors flex flex-col items-center`}
    >
      <span>{label}</span>
      <span className="text-[10px] opacity-70 normal-case mt-0.5">{hint}</span>
    </button>
  );
}

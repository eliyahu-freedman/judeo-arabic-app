"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { Rating, type Grade } from "ts-fsrs";
import { type Entry } from "@/lib/lookup";
import { resolveDeckItem, type DeckItem } from "@/lib/deck";
import { useWordStates } from "@/lib/wordState";
import { useProgress } from "@/lib/progress";

export function ReviewSession() {
  const { hydrated, dueKeys, gradeCard, counts } = useWordStates();
  const { touchStreak } = useProgress();
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
  const item = resolveDeckItem(current);

  const onGrade = (grade: Grade) => {
    gradeCard(current, grade);
    touchStreak();
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
        item={item}
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
            Nothing to review yet. Take a lesson and tap{" "}
            <span className="text-amber-700 font-medium">＋ Review</span>, or open
            a reader and mark a word{" "}
            <span className="text-amber-700 font-medium">Learning</span>, to start
            your queue.
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
          href="/learn"
          className="px-4 py-2 rounded-full bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine/90 transition-colors"
        >
          Take a lesson
        </Link>
        <Link
          href="/tafsir"
          className="px-4 py-2 rounded-full border border-ink/15 text-ink/70 text-sm uppercase tracking-wider hover:border-wine/50 hover:text-wine transition-colors"
        >
          Open Tafsir
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
  item,
  revealed,
  onReveal,
  onGrade,
  onSkip,
}: {
  item: DeckItem;
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
          {item.front}
        </span>
        {item.kind === "cognate" && (
          <span className="mt-3 text-xs uppercase tracking-[0.25em] text-muted">
            Cognate
          </span>
        )}
        {item.kind === "letter" && (
          <span className="mt-3 text-xs uppercase tracking-[0.25em] text-muted">
            Letter
          </span>
        )}

        {revealed && (
          <div className="mt-10 w-full max-w-md">
            <CardBack item={item} />
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

function CardBack({ item }: { item: DeckItem }) {
  if (item.kind === "word") {
    return <WordBack entries={item.entries} />;
  }
  if (item.kind === "cognate") {
    const c = item.cognate;
    return (
      <div className="text-center space-y-3">
        <p className="text-2xl text-ink">
          {c.modern_he}{" "}
          <span className="text-base text-muted font-mono">
            ({c.modern_translit})
          </span>
        </p>
        <p dir="ltr" className="text-[15px] text-ink/80 italic">
          {c.modern_en}
        </p>
        <p className="font-arabic text-xl text-wine" dir="rtl">
          {c.arabic}{" "}
          <span className="text-sm text-muted font-sans">
            {c.arabic_translit}
          </span>
        </p>
        <p
          dir="ltr"
          className="text-[13px] text-ink/65 leading-relaxed text-left pt-2 border-t border-ink/10"
        >
          {c.story}
        </p>
      </div>
    );
  }
  if (item.kind === "letter") {
    const l = item.letter;
    return (
      <div className="text-center space-y-2">
        <p className="font-arabic text-4xl text-wine">{l.ar}</p>
        <p className="text-sm text-muted font-mono">/{l.phoneme}/ · {l.name}</p>
        <p className="pt-3 text-[13px] text-ink/70" dir="ltr">
          e.g.{" "}
          <span className="font-hebrew text-lg text-ink" dir="rtl">
            {l.example_ja}
          </span>{" "}
          = {l.example_translit} — &ldquo;{l.example_gloss}&rdquo;
        </p>
      </div>
    );
  }
  return (
    <p className="text-sm text-muted italic">
      No card data — grade from memory.
    </p>
  );
}

function WordBack({ entries }: { entries: Entry[] }) {
  if (entries.length === 0) {
    return (
      <p className="text-sm text-muted italic">
        No dictionary entry — grade from memory.
      </p>
    );
  }
  return (
    <ul className="space-y-4" dir="rtl">
      {entries.map((e) => (
        <li key={e.id} className="border-r-2 border-wine/40 pr-4 pl-2">
          <div className="flex items-baseline gap-3 flex-wrap">
            {e.lemma_ar && (
              <span className="font-arabic text-lg text-ink/70">
                {e.lemma_ar}
              </span>
            )}
            {e.root && (
              <span className="text-xs text-muted font-mono">√{e.root}</span>
            )}
            {e.pos && (
              <span className="text-xs text-muted italic">{e.pos}</span>
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
                e.source ? "text-[13px] leading-relaxed" : "text-[15px]"
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

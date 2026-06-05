"use client";

import Link from "next/link";
import { CURRICULUM } from "@/lib/curriculum";
import { useProgress } from "@/lib/progress";

export function GuidedPath() {
  const { hydrated, lessonsDone, streak } = useProgress();

  const firstIncomplete = CURRICULUM.find((s) => !lessonsDone[s.id]);
  const doneCount = CURRICULUM.filter((s) => lessonsDone[s.id]).length;
  const continueStep = firstIncomplete ?? CURRICULUM[CURRICULUM.length - 1];

  return (
    <section className="mb-14 rounded-md bg-parchment border border-ink/10 p-7">
      <div className="flex items-center justify-between gap-4 mb-1">
        <p className="text-xs uppercase tracking-[0.3em] text-muted">
          Your path
        </p>
        {hydrated && streak.count > 0 && (
          <span
            className="text-xs text-amber-700"
            title={`${streak.count}-day streak`}
          >
            🔥 {streak.count}
          </span>
        )}
      </div>
      <div className="flex items-baseline justify-between gap-4 mb-5">
        <h2 className="text-2xl text-ink">
          {hydrated && doneCount > 0 ? "Pick up where you left off" : "Start here"}
        </h2>
        {hydrated && (
          <span className="text-xs text-muted">
            {doneCount} / {CURRICULUM.length}
          </span>
        )}
      </div>

      <ol className="space-y-1.5">
        {CURRICULUM.map((step, i) => {
          const done = hydrated && lessonsDone[step.id];
          const isCurrent = hydrated && step.id === continueStep.id && !done;
          return (
            <li key={step.id}>
              <Link
                href={step.href}
                className={`flex items-center gap-3 rounded-md px-3 py-2 transition-colors ${
                  isCurrent
                    ? "bg-page border border-wine/30"
                    : "hover:bg-page/60"
                }`}
              >
                <span
                  className={`flex h-6 w-6 shrink-0 items-center justify-center rounded-full text-[11px] ${
                    done
                      ? "bg-emerald-600 text-page"
                      : isCurrent
                        ? "bg-wine text-page"
                        : "bg-ink/10 text-ink/60"
                  }`}
                >
                  {done ? "✓" : i + 1}
                </span>
                <span className="flex-1 min-w-0">
                  <span
                    className={`text-[15px] ${
                      done ? "text-ink/55" : "text-ink"
                    }`}
                  >
                    {step.title}
                  </span>
                  <span className="hidden sm:inline text-[13px] text-muted">
                    {" "}
                    — {step.blurb}
                  </span>
                </span>
                {isCurrent && (
                  <span className="text-[10px] uppercase tracking-wider text-wine shrink-0">
                    Next
                  </span>
                )}
              </Link>
            </li>
          );
        })}
      </ol>

      <div className="mt-5">
        <Link
          href={continueStep.href}
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine-700 transition-colors"
        >
          {hydrated && doneCount > 0 ? "Continue" : "Begin"}
          <span aria-hidden>→</span>
        </Link>
        <span className="ml-3 text-[13px] text-muted">{continueStep.title}</span>
      </div>
    </section>
  );
}

"use client";

import Link from "next/link";
import { useProgress } from "@/lib/progress";

// Homepage returning-user rail: streak + "resume where you left off" + the
// daily-review link. Renders a stable baseline before hydration.
export function ReturningRail() {
  const { hydrated, streak, lastVisited } = useProgress();
  const showStreak = hydrated && streak.count > 0;

  if (!hydrated || (streak.count === 0 && !lastVisited)) return null;

  return (
    <div className="mt-10 pt-6 border-t border-ink/10 text-sm text-ink/70 flex items-center justify-between flex-wrap gap-3">
      <span className="flex items-center gap-3">
        <span>Already practicing?</span>
        {showStreak && (
          <span
            className="text-amber-700"
            title={`${streak.count}-day streak`}
          >
            🔥 {streak.count}-day streak
          </span>
        )}
      </span>
      <span className="flex items-center gap-4">
        {hydrated && lastVisited && (
          <Link
            href={lastVisited.href}
            className="text-ink/70 hover:text-wine tracking-wide"
          >
            Resume: {lastVisited.label} →
          </Link>
        )}
        <Link
          href="/review"
          className="text-wine hover:underline tracking-wide"
        >
          Continue your daily review →
        </Link>
      </span>
    </div>
  );
}

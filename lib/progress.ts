"use client";

import { useCallback, useEffect, useState } from "react";

// Lightweight Stage-1 progress store: which lessons are done, a daily streak,
// and a "resume here" pointer. Mirrors the SSR-safe localStorage pattern in
// lib/wordState.ts. Additive — independent of the FSRS word deck.

export type LastVisited = { label: string; href: string };

export type Progress = {
  lessonsDone: Record<string, true>;
  streak: { count: number; lastActive: string | null }; // lastActive = local YYYY-MM-DD
  lastVisited?: LastVisited;
};

const STORAGE_KEY = "ja-progress-v1";

const EMPTY: Progress = { lessonsDone: {}, streak: { count: 0, lastActive: null } };

function localDayKey(d: Date): string {
  // Local-date key (not UTC) so streaks track the user's own midnight.
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

function load(): Progress {
  if (typeof window === "undefined") return EMPTY;
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return EMPTY;
    const parsed = JSON.parse(raw);
    if (parsed && typeof parsed === "object") {
      return {
        lessonsDone: parsed.lessonsDone ?? {},
        streak: parsed.streak ?? { count: 0, lastActive: null },
        lastVisited: parsed.lastVisited,
      };
    }
    return EMPTY;
  } catch {
    return EMPTY;
  }
}

function save(p: Progress) {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(p));
  } catch {
    // full or disabled
  }
}

export function useProgress() {
  const [progress, setProgress] = useState<Progress>(EMPTY);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    setProgress(load());
    setHydrated(true);
  }, []);

  const markLessonDone = useCallback((id: string) => {
    setProgress((prev) => {
      if (prev.lessonsDone[id]) return prev;
      const next = {
        ...prev,
        lessonsDone: { ...prev.lessonsDone, [id]: true as const },
      };
      save(next);
      return next;
    });
  }, []);

  // Bump the streak on any study activity. Same day → no-op; consecutive day →
  // +1; a gap → reset to 1.
  const touchStreak = useCallback(() => {
    setProgress((prev) => {
      const today = localDayKey(new Date());
      const last = prev.streak.lastActive;
      if (last === today) return prev;
      const yesterday = localDayKey(new Date(Date.now() - 86400000));
      const count = last === yesterday ? prev.streak.count + 1 : 1;
      const next = { ...prev, streak: { count, lastActive: today } };
      save(next);
      return next;
    });
  }, []);

  const setLastVisited = useCallback((v: LastVisited) => {
    setProgress((prev) => {
      const next = { ...prev, lastVisited: v };
      save(next);
      return next;
    });
  }, []);

  return {
    hydrated,
    lessonsDone: progress.lessonsDone,
    streak: progress.streak,
    lastVisited: progress.lastVisited,
    markLessonDone,
    touchStreak,
    setLastVisited,
  };
}

"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { createEmptyCard, fsrs, type Card, type Grade } from "ts-fsrs";
import { normalizeToken } from "./lookup";

export type WordState = "new" | "learning" | "known" | "ignored";

type StoredCard = {
  due: string;
  stability: number;
  difficulty: number;
  elapsed_days: number;
  scheduled_days: number;
  learning_steps: number;
  reps: number;
  lapses: number;
  state: number;
  last_review?: string;
};

export type WordCard = {
  state: WordState;
  fsrs?: StoredCard;
};

const STORAGE_KEY = "ja-word-states-v2";
const V1_KEY = "ja-word-states-v1";

type StateMap = Record<string, WordCard>;

function cardToStored(c: Card): StoredCard {
  return {
    due: c.due.toISOString(),
    stability: c.stability,
    difficulty: c.difficulty,
    elapsed_days: c.elapsed_days,
    scheduled_days: c.scheduled_days,
    learning_steps: c.learning_steps,
    reps: c.reps,
    lapses: c.lapses,
    state: c.state,
    last_review: c.last_review?.toISOString(),
  };
}

function storedToCard(s: StoredCard): Card {
  return {
    due: new Date(s.due),
    stability: s.stability,
    difficulty: s.difficulty,
    elapsed_days: s.elapsed_days,
    scheduled_days: s.scheduled_days,
    learning_steps: s.learning_steps,
    reps: s.reps,
    lapses: s.lapses,
    state: s.state,
    last_review: s.last_review ? new Date(s.last_review) : undefined,
  };
}

function migrateV1(): StateMap | null {
  if (typeof window === "undefined") return null;
  const v1Raw = window.localStorage.getItem(V1_KEY);
  if (!v1Raw) return null;
  try {
    const v1 = JSON.parse(v1Raw) as Record<string, WordState>;
    const v2: StateMap = {};
    for (const [k, state] of Object.entries(v1)) {
      if (state === "learning") {
        v2[k] = { state, fsrs: cardToStored(createEmptyCard()) };
      } else if (state === "known" || state === "ignored") {
        v2[k] = { state };
      }
    }
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(v2));
    window.localStorage.removeItem(V1_KEY);
    return v2;
  } catch {
    return null;
  }
}

function loadFromStorage(): StateMap {
  if (typeof window === "undefined") return {};
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && typeof parsed === "object") return parsed as StateMap;
    }
    return migrateV1() ?? {};
  } catch {
    return {};
  }
}

function saveToStorage(map: StateMap) {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(map));
  } catch {
    // localStorage full or disabled
  }
}

const scheduler = fsrs();

export function useWordStates() {
  const [map, setMap] = useState<StateMap>({});
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    setMap(loadFromStorage());
    setHydrated(true);
  }, []);

  const getState = useCallback(
    (rawToken: string): WordState => {
      const key = normalizeToken(rawToken);
      if (!key) return "new";
      return map[key]?.state ?? "new";
    },
    [map]
  );

  const setState = useCallback((rawToken: string, next: WordState) => {
    const key = normalizeToken(rawToken);
    if (!key) return;
    setMap((prev) => {
      const updated: StateMap = { ...prev };
      if (next === "new") {
        delete updated[key];
      } else if (next === "learning") {
        const existing = prev[key];
        updated[key] = {
          state: "learning",
          fsrs: existing?.fsrs ?? cardToStored(createEmptyCard()),
        };
      } else {
        updated[key] = { state: next };
      }
      saveToStorage(updated);
      return updated;
    });
  }, []);

  const gradeCard = useCallback((canonicalKey: string, grade: Grade) => {
    setMap((prev) => {
      const entry = prev[canonicalKey];
      if (!entry || entry.state !== "learning" || !entry.fsrs) return prev;
      const card = storedToCard(entry.fsrs);
      const result = scheduler.next(card, new Date(), grade);
      const updated: StateMap = {
        ...prev,
        [canonicalKey]: {
          state: "learning",
          fsrs: cardToStored(result.card),
        },
      };
      saveToStorage(updated);
      return updated;
    });
  }, []);

  const dueKeys = useMemo(() => {
    const now = Date.now();
    const out: string[] = [];
    for (const [k, v] of Object.entries(map)) {
      if (
        v.state === "learning" &&
        v.fsrs &&
        new Date(v.fsrs.due).getTime() <= now
      ) {
        out.push(k);
      }
    }
    return out;
  }, [map]);

  const counts = useMemo(() => {
    const c = { learning: 0, known: 0, ignored: 0, due: 0 };
    const now = Date.now();
    for (const v of Object.values(map)) {
      if (v.state === "learning") {
        c.learning++;
        if (v.fsrs && new Date(v.fsrs.due).getTime() <= now) c.due++;
      } else if (v.state === "known") c.known++;
      else if (v.state === "ignored") c.ignored++;
    }
    return c;
  }, [map]);

  return { getState, setState, gradeCard, counts, hydrated, dueKeys };
}

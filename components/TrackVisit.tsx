"use client";

import { useEffect } from "react";
import { useProgress } from "@/lib/progress";

// Drop into a lesson page to record it as the user's "resume here" pointer.
// For browse-only lessons (no quiz to complete), pass `completeId` so the
// guided path can progress past them on a visit. Renders nothing.
export function TrackVisit({
  label,
  href,
  completeId,
}: {
  label: string;
  href: string;
  completeId?: string;
}) {
  const { setLastVisited, markLessonDone } = useProgress();
  useEffect(() => {
    setLastVisited({ label, href });
    if (completeId) markLessonDone(completeId);
  }, [label, href, completeId, setLastVisited, markLessonDone]);
  return null;
}

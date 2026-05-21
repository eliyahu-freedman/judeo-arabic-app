import type { Metadata } from "next";
import { ReviewSession } from "./review";

export const metadata: Metadata = {
  title: "Spaced-Repetition Review",
  description:
    "Words you've marked as Learning in the Tafsir and Bahya readers come back here on a spaced-repetition schedule (FSRS). Grade your recall and the schedule adjusts to surface what you almost-forgot.",
  alternates: { canonical: "/review" },
  robots: { index: false, follow: true },
};

export default function ReviewPage() {
  return <ReviewSession />;
}

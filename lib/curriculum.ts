// The ordered Stage-1 path. `id` matches the key passed to markLessonDone();
// `href` is where the step lives. Used by the guided path on /learn and the
// homepage resume/streak surface.

export type CurriculumStep = {
  id: string;
  title: string;
  href: string;
  blurb: string;
};

export const CURRICULUM: CurriculumStep[] = [
  {
    id: "alphabet",
    title: "The Alphabet",
    href: "/alphabet",
    blurb: "Read Hebrew letters as Arabic sounds.",
  },
  {
    id: "first-50",
    title: "First 50 Words",
    href: "/learn/first-50",
    blurb: "The words you'll meet most in the Tafsir.",
  },
  {
    id: "cognates",
    title: "You Already Know This",
    href: "/learn/cognates",
    blurb: "Modern Hebrew you already speak is Arabic.",
  },
  {
    id: "aramaic-cognates",
    title: "If You Know Onkelos…",
    href: "/learn/aramaic-cognates",
    blurb: "Aramaic bridges straight into Arabic.",
  },
  {
    id: "grammar-article",
    title: "The Definite Article",
    href: "/learn/grammar/article",
    blurb: "אל = ال, and what happens to the sun-letters.",
  },
  {
    id: "grammar-suffixes",
    title: "Pronominal Suffixes",
    href: "/learn/grammar/suffixes",
    blurb: "Why a word you know hides behind an ending.",
  },
  {
    id: "grammar-verbs",
    title: "The Verb Spine",
    href: "/learn/grammar/verbs",
    blurb: "קאל, כאן, and the prefix conjugation.",
  },
  {
    id: "on-ramp",
    title: "Read Your First Verses",
    href: "/learn/on-ramp",
    blurb: "Scaffolded real clauses, into the Tafsir.",
  },
  {
    id: "tafsir",
    title: "Open the Tafsir",
    href: "/tafsir",
    blurb: "Start reading Genesis in Saadia's Arabic.",
  },
];

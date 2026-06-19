// Manifest of the Moreh Nevukhim (Guide of the Perplexed) chapters that have a
// reader. Chapter I:1 keeps the bare canonical URL; I:2–I:4 are sibling routes.
// `buildMorehNav` produces the inline chapter index + prev/next strip rendered
// by AdvancedReader (see ReaderNav in ../reader).

export type MorehChapter = {
  /** Chapter number within Part I. */
  n: number;
  /** URL slug under the base path; "" for I:1 (the canonical landing page). */
  slug: string;
  /** Short title shown on the navigation chip. */
  title: string;
};

export const MOREH_BASE = "/advanced/rambam-moreh-nevukhim";

export const MOREH_CHAPTERS: MorehChapter[] = [
  { n: 1, slug: "", title: "I:1 · Image & Likeness" },
  { n: 2, slug: "2", title: "I:2 · Adam's Sin" },
  { n: 3, slug: "3", title: "I:3 · Temunah & Tavnit" },
  { n: 4, slug: "4", title: "I:4 · Verbs of Seeing" },
  { n: 5, slug: "5", title: "I:5 · Divine Inquiry" },
  { n: 6, slug: "6", title: "I:6 · Ish & Ishah" },
  { n: 7, slug: "7", title: "I:7 · Yalad" },
  { n: 8, slug: "8", title: "I:8 · Makom" },
  { n: 9, slug: "9", title: "I:9 · Kisse" },
  { n: 10, slug: "10", title: "I:10 · Ascend / Descend" },
  { n: 11, slug: "11", title: "I:11 · Yashav" },
  { n: 12, slug: "12", title: "I:12 · Qam" },
  { n: 13, slug: "13", title: "I:13 · ʿAmad" },
  { n: 14, slug: "14", title: "I:14 · Adam" },
  { n: 15, slug: "15", title: "I:15 · Natzav & Yatzav" },
  { n: 16, slug: "16", title: "I:16 · Tzur" },
  { n: 17, slug: "17", title: "I:17 · Concealing Knowledge" },
  { n: 18, slug: "18", title: "I:18 · Karav, Naga, Nagash" },
  { n: 19, slug: "19", title: "I:19 · Male" },
  { n: 20, slug: "20", title: "I:20 · Ram & Nissa" },
  { n: 21, slug: "21", title: "I:21 · ʿAvar" },
  { n: 22, slug: "22", title: "I:22 · Bo" },
  { n: 23, slug: "23", title: "I:23 · Yatza" },
  { n: 24, slug: "24", title: "I:24 · Halakh" },
  { n: 25, slug: "25", title: "I:25 · Shakhan" },
  { n: 26, slug: "26", title: "I:26 · Language of Men" },
  { n: 27, slug: "27", title: "I:27 · Onkelos" },
  { n: 28, slug: "28", title: "I:28 · Regel" },
];

export const morehHref = (slug: string): string =>
  slug ? `${MOREH_BASE}/${slug}` : MOREH_BASE;

/** Build the ReaderNav object for the chapter numbered `currentN`. */
export function buildMorehNav(currentN: number) {
  return {
    label: "Guide of the Perplexed · Part I",
    currentN,
    aux: [
      { title: "Atlas of God-language", href: `${MOREH_BASE}/atlas` },
      { title: "Verses index", href: `${MOREH_BASE}/verses` },
      { title: "Parallel view", href: `${MOREH_BASE}/${currentN}/parallel` },
      {
        title: "Commentators on AlHaTorah ↗",
        href: `https://moreh.alhatorah.org/1/${currentN}`,
        external: true,
      },
    ],
    chapters: MOREH_CHAPTERS.map((c) => ({
      n: c.n,
      title: c.title,
      href: morehHref(c.slug),
    })),
  };
}

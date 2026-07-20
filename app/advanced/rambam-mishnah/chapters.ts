// Manifest for Rambam's Mishnah Commentary in the advanced reader.
// Each tractate's chapters map to slugs under /advanced/rambam-mishnah/{tractate}/{chapter}.
// Add new tractates here as they are translated.

export const MISHNAH_BASE = "/advanced/rambam-mishnah";

export type MishnahTractate = "zeraim-intro" | "avot" | "sanhedrin" | "berakhot" | "avodah-zarah";

export type MishnahChapter = {
  /** URL slug; "intro" for the Shemonah Perakim introduction. */
  slug: string;
  /** Chapter number (0 = intro). */
  n: number;
  /** Short title shown in navigation chips. */
  title: string;
  /** JSON data file basename (without .json), under data/. */
  dataKey: string;
};

export const mishnahHref = (tractate: MishnahTractate, slug: string) =>
  `${MISHNAH_BASE}/${tractate}/${slug}`;

export const AVOT_CHAPTERS: MishnahChapter[] = [
  { slug: "intro", n: 0, title: "Intro · Eight Chapters", dataKey: "rambam-mishnah-avot-intro" },
  { slug: "ch1",   n: 1, title: "Ch 1 · The Pairs",       dataKey: "rambam-mishnah-avot-ch1" },
  { slug: "ch2",   n: 2, title: "Ch 2 · Yohanan ben Zakkai", dataKey: "rambam-mishnah-avot-ch2" },
  { slug: "ch3",   n: 3, title: "Ch 3 · Wisdom & Discipline", dataKey: "rambam-mishnah-avot-ch3" },
  { slug: "ch4",   n: 4, title: "Ch 4 · The Mighty & Rich",   dataKey: "rambam-mishnah-avot-ch4" },
  { slug: "ch5",   n: 5, title: "Ch 5 · Numerical Sayings",   dataKey: "rambam-mishnah-avot-ch5" },
];

export const avotChapterBySlug = Object.fromEntries(
  AVOT_CHAPTERS.map((c) => [c.slug, c])
);

export const avotHref = (slug: string) =>
  `${MISHNAH_BASE}/avot/${slug}`;

export function buildAvotNav(currentSlug: string) {
  return {
    label: "Rambam · Commentary on Avot",
    currentN: AVOT_CHAPTERS.find((c) => c.slug === currentSlug)?.n ?? 0,
    activeHref: avotHref(currentSlug),
    chapters: AVOT_CHAPTERS.map((c) => ({
      n: c.n,
      title: c.title,
      href: avotHref(c.slug),
    })),
  };
}

// ── Sanhedrin ──────────────────────────────────────────────────────────────

export const SANHEDRIN_CHAPTERS: MishnahChapter[] = [
  { slug: "ch1",  n: 1,  title: "Ch 1 · Courts & Jurisdiction",    dataKey: "rambam-mishnah-sanhedrin-ch1"  },
  { slug: "ch2",  n: 2,  title: "Ch 2 · High Priest & King",       dataKey: "rambam-mishnah-sanhedrin-ch2"  },
  { slug: "ch3",  n: 3,  title: "Ch 3 · Financial Courts",         dataKey: "rambam-mishnah-sanhedrin-ch3"  },
  { slug: "ch4",  n: 4,  title: "Ch 4 · Capital vs. Financial",    dataKey: "rambam-mishnah-sanhedrin-ch4"  },
  { slug: "ch5",  n: 5,  title: "Ch 5 · Witness Examination",      dataKey: "rambam-mishnah-sanhedrin-ch5"  },
  { slug: "ch6",  n: 6,  title: "Ch 6 · After the Verdict",        dataKey: "rambam-mishnah-sanhedrin-ch6"  },
  { slug: "ch7",  n: 7,  title: "Ch 7 · Four Modes of Execution",  dataKey: "rambam-mishnah-sanhedrin-ch7"  },
  { slug: "ch8",  n: 8,  title: "Ch 8 · The Rebellious Son",       dataKey: "rambam-mishnah-sanhedrin-ch8"  },
  { slug: "ch9",  n: 9,  title: "Ch 9 · Burning & Strangulation",  dataKey: "rambam-mishnah-sanhedrin-ch9"  },
  { slug: "ch10", n: 10, title: "Ch 10 · Ḥeleq — 13 Principles",  dataKey: "rambam-mishnah-sanhedrin-ch10" },
];

export const sanhedrinChapterBySlug = Object.fromEntries(
  SANHEDRIN_CHAPTERS.map((c) => [c.slug, c])
);

export const sanhedrinHref = (slug: string) =>
  `${MISHNAH_BASE}/sanhedrin/${slug}`;

export function buildSanhedrinNav(currentSlug: string) {
  return {
    label: "Rambam · Commentary on Sanhedrin",
    currentN: SANHEDRIN_CHAPTERS.find((c) => c.slug === currentSlug)?.n ?? 1,
    activeHref: sanhedrinHref(currentSlug),
    chapters: SANHEDRIN_CHAPTERS.map((c) => ({
      n: c.n,
      title: c.title,
      href: sanhedrinHref(c.slug),
    })),
  };
}

// ── Zeraim Introduction ────────────────────────────────────────────────────

export const ZERAIM_INTRO_CHAPTERS: MishnahChapter[] = [
  { slug: "sec1", n: 1, title: "§1 · The Oral Torah",        dataKey: "rambam-mishnah-zeraim-intro-sec1" },
  { slug: "sec2", n: 2, title: "§2 · Chain of Tradition",    dataKey: "rambam-mishnah-zeraim-intro-sec2" },
  { slug: "sec3", n: 3, title: "§3 · The Mishnah",           dataKey: "rambam-mishnah-zeraim-intro-sec3" },
  { slug: "sec4", n: 4, title: "§4 · Talmud & Geonim",       dataKey: "rambam-mishnah-zeraim-intro-sec4" },
  { slug: "sec5", n: 5, title: "§5 · Rambam's Methodology",  dataKey: "rambam-mishnah-zeraim-intro-sec5" },
];

export const zeraim_introChapterBySlug = Object.fromEntries(
  ZERAIM_INTRO_CHAPTERS.map((c) => [c.slug, c])
);

// ── Berakhot ───────────────────────────────────────────────────────────────

export const BERAKHOT_CHAPTERS: MishnahChapter[] = [
  { slug: "ch1", n: 1, title: "Ch 1 · Times of the Shema",        dataKey: "rambam-mishnah-berakhot-ch1" },
  { slug: "ch2", n: 2, title: "Ch 2 · Reading the Shema",          dataKey: "rambam-mishnah-berakhot-ch2" },
  { slug: "ch3", n: 3, title: "Ch 3 · Exemptions from Shema",      dataKey: "rambam-mishnah-berakhot-ch3" },
  { slug: "ch4", n: 4, title: "Ch 4 · Three Daily Prayers",        dataKey: "rambam-mishnah-berakhot-ch4" },
  { slug: "ch5", n: 5, title: "Ch 5 · Kavanah in Prayer",          dataKey: "rambam-mishnah-berakhot-ch5" },
  { slug: "ch6", n: 6, title: "Ch 6 · Blessings over Food",        dataKey: "rambam-mishnah-berakhot-ch6" },
  { slug: "ch7", n: 7, title: "Ch 7 · Grace after Meals",          dataKey: "rambam-mishnah-berakhot-ch7" },
  { slug: "ch8", n: 8, title: "Ch 8 · Beit Shammai & Hillel",      dataKey: "rambam-mishnah-berakhot-ch8" },
  { slug: "ch9", n: 9, title: "Ch 9 · Blessings on Wonders",       dataKey: "rambam-mishnah-berakhot-ch9" },
];

export const berakhot_ChapterBySlug = Object.fromEntries(
  BERAKHOT_CHAPTERS.map((c) => [c.slug, c])
);

// ── Avodah Zarah ───────────────────────────────────────────────────────────

export const AVODAH_ZARAH_CHAPTERS: MishnahChapter[] = [
  { slug: "ch1", n: 1, title: "Ch 1 · Dealings Before Festivals",  dataKey: "rambam-mishnah-avodah-zarah-ch1" },
  { slug: "ch2", n: 2, title: "Ch 2 · Forbidden Items",            dataKey: "rambam-mishnah-avodah-zarah-ch2" },
  { slug: "ch3", n: 3, title: "Ch 3 · Idols & Accessories",        dataKey: "rambam-mishnah-avodah-zarah-ch3" },
  { slug: "ch4", n: 4, title: "Ch 4 · Nullification of Idols",     dataKey: "rambam-mishnah-avodah-zarah-ch4" },
  { slug: "ch5", n: 5, title: "Ch 5 · Wine of Idolaters",          dataKey: "rambam-mishnah-avodah-zarah-ch5" },
];

export const avodahZarah_ChapterBySlug = Object.fromEntries(
  AVODAH_ZARAH_CHAPTERS.map((c) => [c.slug, c])
);

// ── Unified nav (all tractates as collapsible groups) ─────────────────────

export function buildMishnahNav(tractate: MishnahTractate, currentSlug: string) {
  const tractateChapters: MishnahChapter[] =
    tractate === "zeraim-intro"
      ? ZERAIM_INTRO_CHAPTERS
      : tractate === "avot"
      ? AVOT_CHAPTERS
      : tractate === "berakhot"
      ? BERAKHOT_CHAPTERS
      : tractate === "avodah-zarah"
      ? AVODAH_ZARAH_CHAPTERS
      : SANHEDRIN_CHAPTERS;

  const hrefFor = (t: MishnahTractate, slug: string) => mishnahHref(t, slug);

  const groups = [
    ...(ZERAIM_INTRO_CHAPTERS.length > 0
      ? [
          {
            label: "Introduction to the Mishnah (Zeraim)",
            defaultOpen: tractate === "zeraim-intro",
            chapters: ZERAIM_INTRO_CHAPTERS.map((c) => ({
              n: c.n,
              title: c.title,
              href: hrefFor("zeraim-intro", c.slug),
            })),
          },
        ]
      : []),
    {
      label: "Tractate Avodah Zarah",
      defaultOpen: tractate === "avodah-zarah",
      chapters: AVODAH_ZARAH_CHAPTERS.map((c) => ({
        n: c.n,
        title: c.title,
        href: hrefFor("avodah-zarah", c.slug),
      })),
    },
    {
      label: "Tractate Berakhot",
      defaultOpen: tractate === "berakhot",
      chapters: BERAKHOT_CHAPTERS.map((c) => ({
        n: c.n,
        title: c.title,
        href: hrefFor("berakhot", c.slug),
      })),
    },
    {
      label: "Tractate Avot — Eight Chapters + Commentary",
      defaultOpen: tractate === "avot",
      chapters: AVOT_CHAPTERS.map((c) => ({
        n: c.n,
        title: c.title,
        href: hrefFor("avot", c.slug),
      })),
    },
    {
      label: "Tractate Sanhedrin",
      defaultOpen: tractate === "sanhedrin",
      chapters: SANHEDRIN_CHAPTERS.map((c) => ({
        n: c.n,
        title: c.title,
        href: hrefFor("sanhedrin", c.slug),
      })),
    },
  ];

  return {
    label: "Rambam · Commentary on the Mishnah",
    currentN: tractateChapters.find((c) => c.slug === currentSlug)?.n ?? 1,
    activeHref: mishnahHref(tractate, currentSlug),
    chapters: tractateChapters.map((c) => ({
      n: c.n,
      title: c.title,
      href: mishnahHref(tractate, c.slug),
    })),
    groups,
  };
}

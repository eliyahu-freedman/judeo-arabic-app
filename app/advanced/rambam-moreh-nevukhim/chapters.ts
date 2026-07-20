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
  { n: 29, slug: "29", title: "I:29 · Etzev" },
  { n: 30, slug: "30", title: "I:30 · Akhol" },
  { n: 31, slug: "31", title: "I:31 · Limits of Intellect" },
  { n: 32, slug: "32", title: "I:32 · Restraint" },
  { n: 33, slug: "33", title: "I:33 · Teaching Order" },
  { n: 34, slug: "34", title: "I:34 · The Five Causes" },
  { n: 35, slug: "35", title: "I:35 · Incorporeality Taught" },
  { n: 36, slug: "36", title: "I:36 · Anger & Idolatry" },
  { n: 37, slug: "37", title: "I:37 · Panim" },
  { n: 38, slug: "38", title: "I:38 · Achor" },
  { n: 39, slug: "39", title: "I:39 · Lev" },
  { n: 40, slug: "40", title: "I:40 · Ruach" },
  { n: 41, slug: "41", title: "I:41 · Nefesh" },
  { n: 42, slug: "42", title: "I:42 · Ḥayyim & Mawt" },
  { n: 43, slug: "43", title: "I:43 · Kanaf" },
  { n: 44, slug: "44", title: "I:44 · ʿAyin" },
  { n: 45, slug: "45", title: "I:45 · Shemaʿ" },
  { n: 46, slug: "46", title: "I:46 · Organs" },
  { n: 47, slug: "47", title: "I:47 · Limits of Language" },
  { n: 48, slug: "48", title: "I:48 · True Hearing" },
  { n: 49, slug: "49", title: "I:49 · Angels & Sight" },
  { n: 50, slug: "50", title: "I:50 · Belief Defined" },
  { n: 51, slug: "51", title: "I:51 · Attributes Overview" },
  { n: 52, slug: "52", title: "I:52 · Five Attributes" },
  { n: 53, slug: "53", title: "I:53 · Ethical Attributes" },
  { n: 54, slug: "54", title: "I:54 · Attributes of Action" },
  { n: 55, slug: "55", title: "I:55 · No Genus for God" },
  { n: 56, slug: "56", title: "I:56 · Existence & Essence" },
  { n: 57, slug: "57", title: "I:57 · Negative Attributes" },
  { n: 58, slug: "58", title: "I:58 · Negation & Silence" },
  { n: 59, slug: "59", title: "I:59 · Silence as Praise" },
  { n: 60, slug: "60", title: "I:60 · Prayer & Attributes" },
  { n: 61, slug: "61", title: "I:61 · Divine Names" },
  { n: 62, slug: "62", title: "I:62 · The Tetragrammaton" },
  { n: 63, slug: "63", title: "I:63 · Ehyeh Asher Ehyeh" },
  { n: 64, slug: "64", title: "I:64 · Kavod" },
  { n: 65, slug: "65", title: "I:65 · Divine Speech" },
  { n: 66, slug: "66", title: "I:66 · Divine Will" },
  { n: 67, slug: "67", title: "I:67 · Sabbath & Creation" },
  { n: 68, slug: "68", title: "I:68 · Intellect Triunity" },
  { n: 69, slug: "69", title: "I:69 · God as Form" },
  { n: 70, slug: "70", title: "I:70 · Kavod & the Chariot" },
  { n: 71, slug: "71", title: "I:71 · Kalām Critique" },
  { n: 72, slug: "72", title: "I:72 · Universe as Organism" },
  { n: 73, slug: "73", title: "I:73 · Twenty-Five Premises" },
  { n: 74, slug: "74", title: "I:74 · Seven Methods" },
  { n: 75, slug: "75", title: "I:75 · Unity Methods" },
  { n: 76, slug: "76", title: "I:76 · Conclusion" },
];

export const morehHref = (slug: string): string =>
  slug ? `${MOREH_BASE}/${slug}` : MOREH_BASE;

/** Build the ReaderNav object for the chapter numbered `currentN`. */
export function buildMorehNav(currentN: number) {
  const ch = MOREH_CHAPTERS.find((c) => c.n === currentN)!;
  return {
    label: "Guide of the Perplexed · Part I",
    currentN,
    activeHref: morehHref(ch.slug),
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
    groups: [
      {
        label: "Part I · Vocabulary & Negative Theology (76 chapters)",
        defaultOpen: true,
        chapters: MOREH_CHAPTERS.map((c) => ({
          n: c.n,
          title: c.title,
          href: morehHref(c.slug),
        })),
      },
      {
        label: "Part II · Physics, Creation & Prophecy (48 chapters)",
        defaultOpen: false,
        chapters: MOREH_CHAPTERS_II.map((c) => ({
          n: c.n,
          title: c.title,
          href: `${MOREH_BASE}/2/${c.slug}`,
        })),
      },
      {
        label: "Part III · Providence, Law & Perfection (54 chapters)",
        defaultOpen: false,
        chapters: MOREH_CHAPTERS_III.map((c) => ({
          n: c.n,
          title: c.title,
          href: `${MOREH_BASE}/3/${c.slug}`,
        })),
      },
    ],
  };
}

export const MOREH_CHAPTERS_II: MorehChapter[] = [
  { n: 1,  slug: "1",  title: "II:1 · Introduction" },
  { n: 2,  slug: "2",  title: "II:2 · Spheres & Intellects" },
  { n: 3,  slug: "3",  title: "II:3 · Intelligences" },
  { n: 4,  slug: "4",  title: "II:4 · The Spheres" },
  { n: 5,  slug: "5",  title: "II:5 · Sphere Motion" },
  { n: 6,  slug: "6",  title: "II:6 · Angels as Forms" },
  { n: 7,  slug: "7",  title: "II:7 · Motion & Movers" },
  { n: 8,  slug: "8",  title: "II:8 · Celestial Music" },
  { n: 9,  slug: "9",  title: "II:9 · The Overflow" },
  { n: 10, slug: "10", title: "II:10 · The Four Elements" },
  { n: 11, slug: "11", title: "II:11 · The World's Unity" },
  { n: 12, slug: "12", title: "II:12 · Emanation" },
  { n: 13, slug: "13", title: "II:13 · Three Opinions" },
  { n: 14, slug: "14", title: "II:14 · Aristotle on Eternity" },
  { n: 15, slug: "15", title: "II:15 · Not a Necessity" },
  { n: 16, slug: "16", title: "II:16 · No Proof for Eternity" },
  { n: 17, slug: "17", title: "II:17 · No Proof for Creation" },
  { n: 18, slug: "18", title: "II:18 · Creation Argument" },
  { n: 19, slug: "19", title: "II:19 · The Divine Will" },
  { n: 20, slug: "20", title: "II:20 · Infinite Regress" },
  { n: 21, slug: "21", title: "II:21 · Necessary Being" },
  { n: 22, slug: "22", title: "II:22 · Aristotle's Flaws" },
  { n: 23, slug: "23", title: "II:23 · Interpretation" },
  { n: 24, slug: "24", title: "II:24 · Astronomy & Physics" },
  { n: 25, slug: "25", title: "II:25 · Creation Accepted" },
  { n: 26, slug: "26", title: "II:26 · Torah & Creation" },
  { n: 27, slug: "27", title: "II:27 · The World's End" },
  { n: 28, slug: "28", title: "II:28 · Maimonides' View" },
  { n: 29, slug: "29", title: "II:29 · Scripture on Creation" },
  { n: 30, slug: "30", title: "II:30 · The Six Days" },
  { n: 31, slug: "31", title: "II:31 · The Sabbath" },
  { n: 32, slug: "32", title: "II:32 · Prophecy Opinions" },
  { n: 33, slug: "33", title: "II:33 · The Sinai Revelation" },
  { n: 34, slug: "34", title: "II:34 · Intellectual Fitness" },
  { n: 35, slug: "35", title: "II:35 · Moses the Unique" },
  { n: 36, slug: "36", title: "II:36 · Prophecy Defined" },
  { n: 37, slug: "37", title: "II:37 · Prophecy Grades" },
  { n: 38, slug: "38", title: "II:38 · Courage & Vision" },
  { n: 39, slug: "39", title: "II:39 · The Torah Unique" },
  { n: 40, slug: "40", title: "II:40 · Law & Governance" },
  { n: 41, slug: "41", title: "II:41 · Dreams & Visions" },
  { n: 42, slug: "42", title: "II:42 · Angels in Visions" },
  { n: 43, slug: "43", title: "II:43 · Symbolic Visions" },
  { n: 44, slug: "44", title: "II:44 · Touch & Prophecy" },
  { n: 45, slug: "45", title: "II:45 · Eleven Degrees" },
  { n: 46, slug: "46", title: "II:46 · Prophetic Actions" },
  { n: 47, slug: "47", title: "II:47 · Prophetic Hyperbole" },
  { n: 48, slug: "48", title: "II:48 · Divine Causation" },
];

export function buildMorehNavII(currentN: number) {
  return {
    label: "Guide of the Perplexed · Part II",
    currentN,
    activeHref: `${MOREH_BASE}/2/${currentN}`,
    aux: [
      { title: "Atlas of God-language", href: `${MOREH_BASE}/atlas` },
      { title: "Verses index", href: `${MOREH_BASE}/verses` },
      {
        title: "Commentators on AlHaTorah ↗",
        href: `https://moreh.alhatorah.org/2/${currentN}`,
        external: true,
      },
    ],
    chapters: MOREH_CHAPTERS_II.map((c) => ({
      n: c.n,
      title: c.title,
      href: `${MOREH_BASE}/2/${c.slug}`,
    })),
    groups: [
      {
        label: "Part I · Vocabulary & Negative Theology (76 chapters)",
        defaultOpen: false,
        chapters: MOREH_CHAPTERS.map((c) => ({
          n: c.n,
          title: c.title,
          href: morehHref(c.slug),
        })),
      },
      {
        label: "Part II · Physics, Creation & Prophecy (48 chapters)",
        defaultOpen: true,
        chapters: MOREH_CHAPTERS_II.map((c) => ({
          n: c.n,
          title: c.title,
          href: `${MOREH_BASE}/2/${c.slug}`,
        })),
      },
      {
        label: "Part III · Providence, Law & Perfection (54 chapters)",
        defaultOpen: false,
        chapters: MOREH_CHAPTERS_III.map((c) => ({
          n: c.n,
          title: c.title,
          href: `${MOREH_BASE}/3/${c.slug}`,
        })),
      },
    ],
  };
}

export const MOREH_CHAPTERS_III: MorehChapter[] = [
  { n: 1,  slug: "1",  title: "III:1 · The Chariot" },
  { n: 2,  slug: "2",  title: "III:2 · Light & Fire" },
  { n: 3,  slug: "3",  title: "III:3 · The Firmament" },
  { n: 4,  slug: "4",  title: "III:4 · The Chariot Vision" },
  { n: 5,  slug: "5",  title: "III:5 · Ezekiel's Chariot" },
  { n: 6,  slug: "6",  title: "III:6 · The Chariot Allegory" },
  { n: 7,  slug: "7",  title: "III:7 · The Chariot Revealed" },
  { n: 8,  slug: "8",  title: "III:8 · Matter as Evil" },
  { n: 9,  slug: "9",  title: "III:9 · The Brilliant Light" },
  { n: 10, slug: "10", title: "III:10 · Evil as Privation" },
  { n: 11, slug: "11", title: "III:11 · Human Self-Harm" },
  { n: 12, slug: "12", title: "III:12 · Providence & Evil" },
  { n: 13, slug: "13", title: "III:13 · Purpose of the World" },
  { n: 14, slug: "14", title: "III:14 · The Sciences" },
  { n: 15, slug: "15", title: "III:15 · The Possible" },
  { n: 16, slug: "16", title: "III:16 · Providence Opinions" },
  { n: 17, slug: "17", title: "III:17 · Five Opinions" },
  { n: 18, slug: "18", title: "III:18 · Providence & the Mind" },
  { n: 19, slug: "19", title: "III:19 · God's Knowledge" },
  { n: 20, slug: "20", title: "III:20 · Knowledge Equivocal" },
  { n: 21, slug: "21", title: "III:21 · Job & Providence" },
  { n: 22, slug: "22", title: "III:22 · Job Interpreted" },
  { n: 23, slug: "23", title: "III:23 · Job's Resolution" },
  { n: 24, slug: "24", title: "III:24 · The Aqedah" },
  { n: 25, slug: "25", title: "III:25 · Purposes of Torah" },
  { n: 26, slug: "26", title: "III:26 · Reasons for Laws" },
  { n: 27, slug: "27", title: "III:27 · Two Perfections" },
  { n: 28, slug: "28", title: "III:28 · Torah's Two Goals" },
  { n: 29, slug: "29", title: "III:29 · Against Idolatry" },
  { n: 30, slug: "30", title: "III:30 · Prohibition of Idolatry" },
  { n: 31, slug: "31", title: "III:31 · Reasons for Precepts" },
  { n: 32, slug: "32", title: "III:32 · Sacrificial Laws" },
  { n: 33, slug: "33", title: "III:33 · Moral Laws" },
  { n: 34, slug: "34", title: "III:34 · Laws for the Many" },
  { n: 35, slug: "35", title: "III:35 · Fourteen Classes" },
  { n: 36, slug: "36", title: "III:36 · Anti-Idolatry Laws" },
  { n: 37, slug: "37", title: "III:37 · Further Prohibitions" },
  { n: 38, slug: "38", title: "III:38 · Symbols & Signs" },
  { n: 39, slug: "39", title: "III:39 · Agricultural Laws" },
  { n: 40, slug: "40", title: "III:40 · Injuries & Penalties" },
  { n: 41, slug: "41", title: "III:41 · Penal Laws" },
  { n: 42, slug: "42", title: "III:42 · Property Laws" },
  { n: 43, slug: "43", title: "III:43 · Holy Days" },
  { n: 44, slug: "44", title: "III:44 · Sabbath & Festivals" },
  { n: 45, slug: "45", title: "III:45 · Temple Laws" },
  { n: 46, slug: "46", title: "III:46 · Sacrifices & Fasts" },
  { n: 47, slug: "47", title: "III:47 · Priestly Laws" },
  { n: 48, slug: "48", title: "III:48 · Moral Improvements" },
  { n: 49, slug: "49", title: "III:49 · Sexual Laws" },
  { n: 50, slug: "50", title: "III:50 · Secret Reasons" },
  { n: 51, slug: "51", title: "III:51 · The Palace Parable" },
  { n: 52, slug: "52", title: "III:52 · Fear & Love of God" },
  { n: 53, slug: "53", title: "III:53 · Four Perfections" },
  { n: 54, slug: "54", title: "III:54 · Final Perfection" },
];

export function buildMorehNavIII(currentN: number) {
  return {
    label: "Guide of the Perplexed · Part III",
    currentN,
    activeHref: `${MOREH_BASE}/3/${currentN}`,
    aux: [
      { title: "Atlas of God-language", href: `${MOREH_BASE}/atlas` },
      { title: "Verses index", href: `${MOREH_BASE}/verses` },
      {
        title: "Commentators on AlHaTorah ↗",
        href: `https://moreh.alhatorah.org/3/${currentN}`,
        external: true,
      },
    ],
    chapters: MOREH_CHAPTERS_III.map((c) => ({
      n: c.n,
      title: c.title,
      href: `${MOREH_BASE}/3/${c.slug}`,
    })),
    groups: [
      {
        label: "Part I · Vocabulary & Negative Theology (76 chapters)",
        defaultOpen: false,
        chapters: MOREH_CHAPTERS.map((c) => ({
          n: c.n,
          title: c.title,
          href: morehHref(c.slug),
        })),
      },
      {
        label: "Part II · Physics, Creation & Prophecy (48 chapters)",
        defaultOpen: false,
        chapters: MOREH_CHAPTERS_II.map((c) => ({
          n: c.n,
          title: c.title,
          href: `${MOREH_BASE}/2/${c.slug}`,
        })),
      },
      {
        label: "Part III · Providence, Law & Perfection (54 chapters)",
        defaultOpen: true,
        chapters: MOREH_CHAPTERS_III.map((c) => ({
          n: c.n,
          title: c.title,
          href: `${MOREH_BASE}/3/${c.slug}`,
        })),
      },
    ],
  };
}

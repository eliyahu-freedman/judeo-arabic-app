// Manifest for Emunot v'Deot (Kitāb al-Amānāt wal-Iʿtiqādāt) by Saadia Gaon.
// Each chapter = one fuṣūl; 10 collapsible maamar groups in the nav sidebar.
// Chapter I:1 is the first dynamic route; the landing page renders the Intro.

import type { ReaderNav } from "../reader";

export type EmunotChapter = {
  n: number;       // global sequential (1–102)
  slug: string;    // "m1f1" … "m10f20"
  title: string;   // nav chip label
  maamar: number;  // 1–10
};

export const EMUNOT_BASE = "/advanced/saadia-emunot-vedeot";

export const EMUNOT_CHAPTERS: EmunotChapter[] = [
  // ── Maamar I: Creation ─────────────────────────────────────────────────────
  { n: 1,  slug: "m1f1", title: "I:1 · Proof, Not Perception",     maamar: 1 },
  { n: 2,  slug: "m1f2", title: "I:2 · Four Proofs for Creation",  maamar: 1 },
  { n: 3,  slug: "m1f3", title: "I:3 · Twelve Cosmogonies",        maamar: 1 },
  { n: 4,  slug: "m1f4", title: "I:4 · Refutation of All Views",   maamar: 1 },
  { n: 5,  slug: "m1f5", title: "I:5 · Creation from Nothing",     maamar: 1 },
  // ── Maamar II: God's Unity ─────────────────────────────────────────────────
  { n: 6,  slug: "m2f1",  title: "II:1 · One Creator",             maamar: 2 },
  { n: 7,  slug: "m2f2",  title: "II:2 · Not Two Principles",      maamar: 2 },
  { n: 8,  slug: "m2f3",  title: "II:3 · Not a Body",              maamar: 2 },
  { n: 9,  slug: "m2f4",  title: "II:4 · One in All Respects",     maamar: 2 },
  { n: 10, slug: "m2f5",  title: "II:5 · Unlike His Creatures",    maamar: 2 },
  { n: 11, slug: "m2f6",  title: "II:6 · Attributes of Action",    maamar: 2 },
  { n: 12, slug: "m2f7",  title: "II:7 · Divine Names",            maamar: 2 },
  { n: 13, slug: "m2f8",  title: "II:8 · He Is Living",            maamar: 2 },
  { n: 14, slug: "m2f9",  title: "II:9 · He Is Powerful",          maamar: 2 },
  { n: 15, slug: "m2f10", title: "II:10 · He Is Knowing",          maamar: 2 },
  { n: 16, slug: "m2f11", title: "II:11 · The Three Attributes",   maamar: 2 },
  { n: 17, slug: "m2f12", title: "II:12 · Apparent Plurality",     maamar: 2 },
  { n: 18, slug: "m2f13", title: "II:13 · Unity & Trinity",        maamar: 2 },
  { n: 19, slug: "m2f14", title: "II:14 · Against All Dualism",    maamar: 2 },
  // ── Maamar III: Divine Command ─────────────────────────────────────────────
  { n: 20, slug: "m3f1",  title: "III:1 · Rational Precepts",      maamar: 3 },
  { n: 21, slug: "m3f2",  title: "III:2 · Revealed Precepts",      maamar: 3 },
  { n: 22, slug: "m3f3",  title: "III:3 · Why Revelation Needed",  maamar: 3 },
  { n: 23, slug: "m3f4",  title: "III:4 · Gratitude & Reverence",  maamar: 3 },
  { n: 24, slug: "m3f5",  title: "III:5 · Forbidden Acts",         maamar: 3 },
  { n: 25, slug: "m3f6",  title: "III:6 · Permitted & Forbidden",  maamar: 3 },
  { n: 26, slug: "m3f7",  title: "III:7 · Categories",             maamar: 3 },
  { n: 27, slug: "m3f8",  title: "III:8 · The Great Category",     maamar: 3 },
  { n: 28, slug: "m3f9",  title: "III:9 · Eighth Category",        maamar: 3 },
  { n: 29, slug: "m3f10", title: "III:10 · Tenth Category",        maamar: 3 },
  { n: 30, slug: "m3f11", title: "III:11 · Closing Survey",        maamar: 3 },
  // ── Maamar IV: Obedience & Free Will ───────────────────────────────────────
  { n: 31, slug: "m4f1",  title: "IV:1 · Human Capacity",          maamar: 4 },
  { n: 32, slug: "m4f2",  title: "IV:2 · Acts & Omissions",        maamar: 4 },
  { n: 33, slug: "m4f3",  title: "IV:3 · Punishment & Justice",    maamar: 4 },
  { n: 34, slug: "m4f4",  title: "IV:4 · Divine Justice",          maamar: 4 },
  { n: 35, slug: "m4f5",  title: "IV:5 · Free Will Defended",      maamar: 4 },
  { n: 36, slug: "m4f6",  title: "IV:6 · Foreknowledge & Freedom", maamar: 4 },
  { n: 37, slug: "m4f7",  title: "IV:7 · Resolution",              maamar: 4 },
  // ── Maamar V: Works & Merits ───────────────────────────────────────────────
  { n: 38, slug: "m5f1",  title: "V:1 · Works of Obedience",       maamar: 5 },
  { n: 39, slug: "m5f2",  title: "V:2 · Works of Disobedience",    maamar: 5 },
  { n: 40, slug: "m5f3",  title: "V:3 · Mixed Works",              maamar: 5 },
  { n: 41, slug: "m5f4",  title: "V:4 · Repentance",               maamar: 5 },
  { n: 42, slug: "m5f5",  title: "V:5 · The Inadvertent",          maamar: 5 },
  { n: 43, slug: "m5f6",  title: "V:6 · Against Antinomians",      maamar: 5 },
  { n: 44, slug: "m5f7",  title: "V:7 · Righteous Suffering",      maamar: 5 },
  { n: 45, slug: "m5f8",  title: "V:8 · Summary",                  maamar: 5 },
  // ── Maamar VI: The Soul ────────────────────────────────────────────────────
  { n: 46, slug: "m6f1",  title: "VI:1 · Soul's Nature",           maamar: 6 },
  { n: 47, slug: "m6f2",  title: "VI:2 · Between Soul & Body",     maamar: 6 },
  { n: 48, slug: "m6f3",  title: "VI:3 · Soul's Location",         maamar: 6 },
  { n: 49, slug: "m6f4",  title: "VI:4 · Soul After Death",        maamar: 6 },
  { n: 50, slug: "m6f5",  title: "VI:5 · Soul's Origin",           maamar: 6 },
  { n: 51, slug: "m6f6",  title: "VI:6 · The Divine Portion",      maamar: 6 },
  { n: 52, slug: "m6f7",  title: "VI:7 · Intermediate State",      maamar: 6 },
  { n: 53, slug: "m6f8",  title: "VI:8 · Soul's Destiny",          maamar: 6 },
  // ── Maamar VII: Resurrection ───────────────────────────────────────────────
  { n: 54, slug: "m7f1",  title: "VII:1 · First Redemption",       maamar: 7 },
  { n: 55, slug: "m7f2",  title: "VII:2 · Proofs from Scripture",  maamar: 7 },
  { n: 56, slug: "m7f3",  title: "VII:3 · Nature of the Body",     maamar: 7 },
  { n: 57, slug: "m7f4",  title: "VII:4 · Duration of Life",       maamar: 7 },
  { n: 58, slug: "m7f5",  title: "VII:5 · The Messianic Era",      maamar: 7 },
  { n: 59, slug: "m7f6",  title: "VII:6 · The Return to Dust",     maamar: 7 },
  { n: 60, slug: "m7f7",  title: "VII:7 · Between Eras",           maamar: 7 },
  { n: 61, slug: "m7f8",  title: "VII:8 · Ninth Category",         maamar: 7 },
  { n: 62, slug: "m7f9",  title: "VII:9 · Final Matters",          maamar: 7 },
  // ── Maamar VIII: Salvation ─────────────────────────────────────────────────
  { n: 63, slug: "m8f1",  title: "VIII:1 · Four Stages",           maamar: 8 },
  { n: 64, slug: "m8f2",  title: "VIII:2 · Proofs for Redemption", maamar: 8 },
  { n: 65, slug: "m8f3",  title: "VIII:3 · The Redeemer's Sign",   maamar: 8 },
  { n: 66, slug: "m8f4",  title: "VIII:4 · Duration of Exile",     maamar: 8 },
  { n: 67, slug: "m8f5",  title: "VIII:5 · The Nations",           maamar: 8 },
  { n: 68, slug: "m8f6",  title: "VIII:6 · Prophetic Testimony",   maamar: 8 },
  { n: 69, slug: "m8f7",  title: "VIII:7 · Divine Promise",        maamar: 8 },
  { n: 70, slug: "m8f8",  title: "VIII:8 · Against Despair",       maamar: 8 },
  { n: 71, slug: "m8f9",  title: "VIII:9 · Summary",               maamar: 8 },
  // ── Maamar IX: Reward & Punishment ────────────────────────────────────────
  { n: 72, slug: "m9f1",  title: "IX:1 · The World to Come",       maamar: 9 },
  { n: 73, slug: "m9f2",  title: "IX:2 · Scripture on the Next World", maamar: 9 },
  { n: 74, slug: "m9f3",  title: "IX:3 · Categories of Bliss",     maamar: 9 },
  { n: 75, slug: "m9f4",  title: "IX:4 · Degrees of Bliss",        maamar: 9 },
  { n: 76, slug: "m9f5",  title: "IX:5 · The Intermediate State",  maamar: 9 },
  { n: 77, slug: "m9f6",  title: "IX:6 · Between",                 maamar: 9 },
  { n: 78, slug: "m9f7",  title: "IX:7 · Eternal Fire",            maamar: 9 },
  { n: 79, slug: "m9f8",  title: "IX:8 · Duration of Punishment",  maamar: 9 },
  { n: 80, slug: "m9f9",  title: "IX:9 · Tenth Degree",            maamar: 9 },
  { n: 81, slug: "m9f10", title: "IX:10 · Final Bliss",            maamar: 9 },
  { n: 82, slug: "m9f11", title: "IX:11 · Summary",                maamar: 9 },
  // ── Maamar X: Ethics & the Good Life ──────────────────────────────────────
  { n: 83,  slug: "m10f1",  title: "X:1 · Three Impulses",         maamar: 10 },
  { n: 84,  slug: "m10f2",  title: "X:2 · Rational Soul",          maamar: 10 },
  { n: 85,  slug: "m10f3",  title: "X:3 · Active Virtues",         maamar: 10 },
  { n: 86,  slug: "m10f4",  title: "X:4 · Humility",               maamar: 10 },
  { n: 87,  slug: "m10f5",  title: "X:5 · Liberality",             maamar: 10 },
  { n: 88,  slug: "m10f6",  title: "X:6 · Courage",                maamar: 10 },
  { n: 89,  slug: "m10f7",  title: "X:7 · Truth",                  maamar: 10 },
  { n: 90,  slug: "m10f8",  title: "X:8 · Self-Restraint",         maamar: 10 },
  { n: 91,  slug: "m10f9",  title: "X:9 · Industriousness",        maamar: 10 },
  { n: 92,  slug: "m10f10", title: "X:10 · Justice",               maamar: 10 },
  { n: 93,  slug: "m10f11", title: "X:11 · Avoidance of Harm",     maamar: 10 },
  { n: 94,  slug: "m10f12", title: "X:12 · Love of God",           maamar: 10 },
  { n: 95,  slug: "m10f13", title: "X:13 · Love of Neighbor",      maamar: 10 },
  { n: 96,  slug: "m10f14", title: "X:14 · The Active Life",       maamar: 10 },
  { n: 97,  slug: "m10f15", title: "X:15 · The Contemplative Life",maamar: 10 },
  { n: 98,  slug: "m10f16", title: "X:16 · Abstinence",            maamar: 10 },
  { n: 99,  slug: "m10f17", title: "X:17 · Fear of God",           maamar: 10 },
  { n: 100, slug: "m10f18", title: "X:18 · Hope & Trust",          maamar: 10 },
  { n: 101, slug: "m10f19", title: "X:19 · Submission",            maamar: 10 },
  { n: 102, slug: "m10f20", title: "X:20 · Closing Exhortation",   maamar: 10 },
];

const MAAMAR_LABELS: Record<number, string> = {
  1:  "Maamar I · Creation (5 chapters)",
  2:  "Maamar II · God's Unity (14 chapters)",
  3:  "Maamar III · Command & Prohibition (11 chapters)",
  4:  "Maamar IV · Obedience & Free Will (7 chapters)",
  5:  "Maamar V · Works & Merits (8 chapters)",
  6:  "Maamar VI · The Soul (8 chapters)",
  7:  "Maamar VII · Resurrection (9 chapters)",
  8:  "Maamar VIII · Salvation (9 chapters)",
  9:  "Maamar IX · Reward & Punishment (11 chapters)",
  10: "Maamar X · The Good Life (20 chapters)",
};

export const emunotHref = (slug: string): string =>
  `${EMUNOT_BASE}/${slug}`;

function makeGroups(activeSlug: string | null) {
  const maamotNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] as const;
  return maamotNums.map((m) => {
    const chs = EMUNOT_CHAPTERS.filter((c) => c.maamar === m);
    return {
      label: MAAMAR_LABELS[m],
      defaultOpen: chs.some((c) => c.slug === activeSlug),
      chapters: chs.map((c) => ({
        n: c.n,
        title: c.title,
        href: emunotHref(c.slug),
      })),
    };
  });
}

/** Build ReaderNav for a fuṣūl page (slug = "m1f1", "m1f2", …). */
export function buildEmunotNav(slug: string): ReaderNav {
  const ch = EMUNOT_CHAPTERS.find((c) => c.slug === slug)!;
  const idx = EMUNOT_CHAPTERS.indexOf(ch);
  const allChapters = EMUNOT_CHAPTERS.map((c) => ({
    n: c.n,
    title: c.title,
    href: emunotHref(c.slug),
  }));
  return {
    label: "Book of Beliefs and Opinions",
    currentN: ch.n,
    activeHref: emunotHref(slug),
    chapters: allChapters,
    groups: makeGroups(slug),
  };
}

/** Build ReaderNav for the Introduction (landing page, no slug). */
export function buildEmunotNavIntro(): ReaderNav {
  const allChapters = EMUNOT_CHAPTERS.map((c) => ({
    n: c.n,
    title: c.title,
    href: emunotHref(c.slug),
  }));
  // Intro is "before" chapter 1 — give it n=0 so prev/next from the landing
  // page point to m1f1 as "next".
  return {
    label: "Book of Beliefs and Opinions",
    currentN: 0,
    activeHref: EMUNOT_BASE,
    chapters: [
      { n: 0, title: "Introduction", href: EMUNOT_BASE },
      ...allChapters,
    ],
    groups: makeGroups(null),
  };
}

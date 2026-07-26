// Manifest for Emunot v'Deot (Kitāb al-Amānāt wal-Iʿtiqādāt) by Saadia Gaon.
// AUTO-ALIGNED to the manuscript's real chapter (fuṣūl) boundaries: each file =
// one perek, split at the פרק markers in the flowing text (FJMS resourceId 13).
// This manuscript's own numbering skips III:8, VI:3, and IX:4 — preserved here so
// the nav number always matches the פרק heading the reader sees in the text.

import type { ReaderNav } from "../reader";

export type EmunotChapter = {
  n: number;       // global sequential (1–93)
  slug: string;    // "m1c1" … "m10c19"
  title: string;   // nav chip label
  maamar: number;  // 1–10
  perek: number;   // manuscript perek number (may skip)
};

export const EMUNOT_BASE = "/advanced/saadia-emunot-vedeot";

export const EMUNOT_CHAPTERS: EmunotChapter[] = [
  // ── Maamar I: Creation ───────────────────────────────────────────────────
  { n: 1, slug: "m1c1", title: "I:1 · That the World Is Created", maamar: 1, perek: 1 },
  { n: 2, slug: "m1c2", title: "I:2 · Nothing Creates Itself", maamar: 1, perek: 2 },
  { n: 3, slug: "m1c3", title: "I:3 · The Rival Cosmogonies", maamar: 1, perek: 3 },
  { n: 4, slug: "m1c4", title: "I:4 · Objections Resolved", maamar: 1, perek: 4 },
  // ── Maamar II: God's Unity ───────────────────────────────────────────────
  { n: 5, slug: "m2c1", title: "II:1 · The Creator Is One", maamar: 2, perek: 1 },
  { n: 6, slug: "m2c2", title: "II:2 · Against Two Principles", maamar: 2, perek: 2 },
  { n: 7, slug: "m2c3", title: "II:3 · The Twofold Name", maamar: 2, perek: 3 },
  { n: 8, slug: "m2c4", title: "II:4 · Living, Powerful, Knowing", maamar: 2, perek: 4 },
  { n: 9, slug: "m2c5", title: "II:5 · Against the Trinity", maamar: 2, perek: 5 },
  { n: 10, slug: "m2c6", title: "II:6 · Against an Eternal Word", maamar: 2, perek: 6 },
  { n: 11, slug: "m2c7", title: "II:7 · The Four Sects", maamar: 2, perek: 7 },
  { n: 12, slug: "m2c8", title: "II:8 · Describing the Subtle", maamar: 2, perek: 8 },
  { n: 13, slug: "m2c9", title: "II:9 · God and the Ten Categories", maamar: 2, perek: 9 },
  { n: 14, slug: "m2c10", title: "II:10 · Against Anthropomorphism", maamar: 2, perek: 10 },
  { n: 15, slug: "m2c11", title: "II:11 · God Bears No Accidents", maamar: 2, perek: 11 },
  { n: 16, slug: "m2c12", title: "II:12 · Creator Without Body", maamar: 2, perek: 12 },
  { n: 17, slug: "m2c13", title: "II:13 · How the Mind Knows God", maamar: 2, perek: 13 },
  // ── Maamar III: Command & Prohibition ────────────────────────────────────
  { n: 18, slug: "m3c1", title: "III:1 · Why God Commands", maamar: 3, perek: 1 },
  { n: 19, slug: "m3c2", title: "III:2 · The Rational Laws", maamar: 3, perek: 2 },
  { n: 20, slug: "m3c3", title: "III:3 · The Need for Messengers", maamar: 3, perek: 3 },
  { n: 21, slug: "m3c4", title: "III:4 · Validating the Messenger", maamar: 3, perek: 4 },
  { n: 22, slug: "m3c5", title: "III:5 · The Prophet's Own Certainty", maamar: 3, perek: 5 },
  { n: 23, slug: "m3c6", title: "III:6 · The Sacred Books", maamar: 3, perek: 6 },
  { n: 24, slug: "m3c7", title: "III:7 · Against Abrogation", maamar: 3, perek: 7 },
  { n: 25, slug: "m3c9", title: "III:9 · Alleged Proofs of Abrogation", maamar: 3, perek: 9 },
  { n: 26, slug: "m3c10", title: "III:10 · Doubts After the Prophet", maamar: 3, perek: 10 },
  // ── Maamar IV: Obedience & Free Will ─────────────────────────────────────
  { n: 27, slug: "m4c1", title: "IV:1 · Humanity at the Center", maamar: 4, perek: 1 },
  { n: 28, slug: "m4c2", title: "IV:2 · Small Body, Vast Soul", maamar: 4, perek: 2 },
  { n: 29, slug: "m4c3", title: "IV:3 · The Gift of Ability", maamar: 4, perek: 3 },
  { n: 30, slug: "m4c4", title: "IV:4 · God Does Not Compel", maamar: 4, perek: 4 },
  { n: 31, slug: "m4c5", title: "IV:5 · Why Command the Righteous", maamar: 4, perek: 5 },
  { n: 32, slug: "m4c6", title: "IV:6 · Verses on Compulsion Resolved", maamar: 4, perek: 6 },
  // ── Maamar V: Merits & Recompense ────────────────────────────────────────
  { n: 33, slug: "m5c1", title: "V:1 · Merits and Duties", maamar: 5, perek: 1 },
  { n: 34, slug: "m5c2", title: "V:2 · Ranks of the Servants", maamar: 5, perek: 2 },
  { n: 35, slug: "m5c3", title: "V:3 · Why the Righteous Suffer", maamar: 5, perek: 3 },
  { n: 36, slug: "m5c4", title: "V:4 · The Wholly Obedient", maamar: 5, perek: 4 },
  { n: 37, slug: "m5c5", title: "V:5 · The Penitent", maamar: 5, perek: 5 },
  { n: 38, slug: "m5c6", title: "V:6 · When Prayer Is Not Accepted", maamar: 5, perek: 6 },
  { n: 39, slug: "m5c7", title: "V:7 · The Balanced Servant", maamar: 5, perek: 7 },
  { n: 40, slug: "m5c8", title: "V:8 · The Reward of Thoughts", maamar: 5, perek: 8 },
  // ── Maamar VI: The Soul ──────────────────────────────────────────────────
  { n: 41, slug: "m6c1", title: "VI:1 · The Essence of the Soul", maamar: 6, perek: 1 },
  { n: 42, slug: "m6c2", title: "VI:2 · The Soul's True Nature", maamar: 6, perek: 2 },
  { n: 43, slug: "m6c4", title: "VI:4 · Why Soul Joins Body", maamar: 6, perek: 4 },
  { n: 44, slug: "m6c5", title: "VI:5 · Soul and Body as One", maamar: 6, perek: 5 },
  { n: 45, slug: "m6c6", title: "VI:6 · The Appointed Lifespan", maamar: 6, perek: 6 },
  { n: 46, slug: "m6c7", title: "VI:7 · The Soul at Death", maamar: 6, perek: 7 },
  { n: 47, slug: "m6c8", title: "VI:8 · Against Transmigration", maamar: 6, perek: 8 },
  // ── Maamar VII: Resurrection ─────────────────────────────────────────────
  { n: 48, slug: "m7c1", title: "VII:1 · Resurrection in This World", maamar: 7, perek: 1 },
  { n: 49, slug: "m7c2", title: "VII:2 · Doubts About Resurrection", maamar: 7, perek: 2 },
  { n: 50, slug: "m7c3", title: "VII:3 · Verses Seeming to Deny It", maamar: 7, perek: 3 },
  { n: 51, slug: "m7c4", title: "VII:4 · The Tradition's Testimony", maamar: 7, perek: 4 },
  { n: 52, slug: "m7c5", title: "VII:5 · Reassembling the Body", maamar: 7, perek: 5 },
  { n: 53, slug: "m7c6", title: "VII:6 · Into the World to Come", maamar: 7, perek: 6 },
  { n: 54, slug: "m7c7", title: "VII:7 · Who Will Be Raised", maamar: 7, perek: 7 },
  { n: 55, slug: "m7c8", title: "VII:8 · The Blemished Restored", maamar: 7, perek: 8 },
  { n: 56, slug: "m7c9", title: "VII:9 · The Living at Redemption", maamar: 7, perek: 9 },
  // ── Maamar VIII: Redemption ──────────────────────────────────────────────
  { n: 57, slug: "m8c1", title: "VIII:1 · The Promised Redemption", maamar: 8, perek: 1 },
  { n: 58, slug: "m8c2", title: "VIII:2 · Nothing Beyond His Power", maamar: 8, perek: 2 },
  { n: 59, slug: "m8c3", title: "VIII:3 · The Appointed End", maamar: 8, perek: 3 },
  { n: 60, slug: "m8c4", title: "VIII:4 · Converging Reckonings", maamar: 8, perek: 4 },
  { n: 61, slug: "m8c5", title: "VIII:5 · Repentance and the End", maamar: 8, perek: 5 },
  { n: 62, slug: "m8c6", title: "VIII:6 · Messiah son of Joseph", maamar: 8, perek: 6 },
  { n: 63, slug: "m8c7", title: "VIII:7 · Refuting a False Claim", maamar: 8, perek: 7 },
  { n: 64, slug: "m8c8", title: "VIII:8 · Fifteen Refutations", maamar: 8, perek: 8 },
  { n: 65, slug: "m8c9", title: "VIII:9 · The Same Against the Christians", maamar: 8, perek: 9 },
  // ── Maamar IX: Reward & Punishment ───────────────────────────────────────
  { n: 66, slug: "m9c1", title: "IX:1 · The World to Come", maamar: 9, perek: 1 },
  { n: 67, slug: "m9c2", title: "IX:2 · Proofs from Scripture", maamar: 9, perek: 2 },
  { n: 68, slug: "m9c3", title: "IX:3 · Further Scriptural Proofs", maamar: 9, perek: 3 },
  { n: 69, slug: "m9c5", title: "IX:5 · What Reward and Punishment Are", maamar: 9, perek: 5 },
  { n: 70, slug: "m9c6", title: "IX:6 · The Place of Recompense", maamar: 9, perek: 6 },
  { n: 71, slug: "m9c7", title: "IX:7 · Why It Is Eternal", maamar: 9, perek: 7 },
  { n: 72, slug: "m9c8", title: "IX:8 · Degrees of Recompense", maamar: 9, perek: 8 },
  { n: 73, slug: "m9c9", title: "IX:9 · Who Is Punished", maamar: 9, perek: 9 },
  { n: 74, slug: "m9c10", title: "IX:10 · Obligations in the Beyond", maamar: 9, perek: 10 },
  // ── Maamar X: The Good Life ──────────────────────────────────────────────
  { n: 75, slug: "m10c1", title: "X:1 · The Soul's Three Powers", maamar: 10, perek: 1 },
  { n: 76, slug: "m10c2", title: "X:2 · The Harm of a Single Pursuit", maamar: 10, perek: 2 },
  { n: 77, slug: "m10c3", title: "X:3 · Solomon's Search for the Good", maamar: 10, perek: 3 },
  { n: 78, slug: "m10c4", title: "X:4 · The Thirteen Pursuits", maamar: 10, perek: 4 },
  { n: 79, slug: "m10c5", title: "X:5 · Eating and Drinking", maamar: 10, perek: 5 },
  { n: 80, slug: "m10c6", title: "X:6 · Sexual Intercourse", maamar: 10, perek: 6 },
  { n: 81, slug: "m10c7", title: "X:7 · Passionate Love", maamar: 10, perek: 7 },
  { n: 82, slug: "m10c8", title: "X:8 · Amassing Wealth", maamar: 10, perek: 8 },
  { n: 83, slug: "m10c9", title: "X:9 · Children", maamar: 10, perek: 9 },
  { n: 84, slug: "m10c10", title: "X:10 · Settling the World", maamar: 10, perek: 10 },
  { n: 85, slug: "m10c11", title: "X:11 · Long Life", maamar: 10, perek: 11 },
  { n: 86, slug: "m10c12", title: "X:12 · Rule and Leadership", maamar: 10, perek: 12 },
  { n: 87, slug: "m10c13", title: "X:13 · Vengeance", maamar: 10, perek: 13 },
  { n: 88, slug: "m10c14", title: "X:14 · Wisdom", maamar: 10, perek: 14 },
  { n: 89, slug: "m10c15", title: "X:15 · Worship", maamar: 10, perek: 15 },
  { n: 90, slug: "m10c16", title: "X:16 · The Life of Rest", maamar: 10, perek: 16 },
  { n: 91, slug: "m10c17", title: "X:17 · The Error of Exclusivity", maamar: 10, perek: 17 },
  { n: 92, slug: "m10c18", title: "X:18 · The Blending of the Senses", maamar: 10, perek: 18 },
  { n: 93, slug: "m10c19", title: "X:19 · The Balanced Life", maamar: 10, perek: 19 },
];

const MAAMAR_LABELS: Record<number, string> = {
  1: "Maamar I · Creation (4 chapters)",
  2: "Maamar II · God's Unity (13 chapters)",
  3: "Maamar III · Command & Prohibition (9 chapters; ms. skips III:8)",
  4: "Maamar IV · Obedience & Free Will (6 chapters)",
  5: "Maamar V · Merits & Recompense (8 chapters)",
  6: "Maamar VI · The Soul (7 chapters; ms. skips VI:3)",
  7: "Maamar VII · Resurrection (9 chapters)",
  8: "Maamar VIII · Redemption (9 chapters)",
  9: "Maamar IX · Reward & Punishment (9 chapters; ms. skips IX:4)",
  10: "Maamar X · The Good Life (19 chapters)",
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

/** Build ReaderNav for a fuṣūl page (slug = "m1c1", "m1c2", …). */
export function buildEmunotNav(slug: string): ReaderNav {
  const ch = EMUNOT_CHAPTERS.find((c) => c.slug === slug)!;
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

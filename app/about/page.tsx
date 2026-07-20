import type { Metadata } from "next";
import Link from "next/link";
import { corpusStats, fmt } from "@/lib/corpusStats";

export const metadata: Metadata = {
  title: "Methodology & Sources",
  description:
    "Editorial principles, source editions, and a full bibliography for Judeo-Arabic: A Digital Reader & Lexicon — Saadia Gaon's Tafsir and the medieval Hebrew-script Arabic library, with glosses from Lane and Blau.",
  alternates: { canonical: "/about" },
};

/** Bibliography rows — every edition and tool the site draws on. Kept as data
 *  so the table and any future export share one source of truth. */
const BIBLIOGRAPHY: {
  category: string;
  author: string;
  title: string;
  detail: string;
}[] = [
  {
    category: "Tafsir text",
    author: "Saʿadya Gaon (ed. J. Derenbourg)",
    title: "Version arabe du Pentateuque (Œuvres complètes, vol. 1)",
    detail: "Paris, 1893 — base text of the Tafsir reader, via Sefaria.",
  },
  {
    category: "Lexicon",
    author: "E. W. Lane",
    title: "An Arabic-English Lexicon",
    detail:
      "London, 1863–93 — classical-Arabic glosses paraphrased for tap-to-define, from the Perseus TEI edition.",
  },
  {
    category: "Lexicon",
    author: "Joshua Blau (ז״ל)",
    title: "A Dictionary of Mediaeval Judaeo-Arabic Texts",
    detail:
      "Jerusalem, 2006 — source for divergence notes where Judeo-Arabic usage departs from the classical sense.",
  },
  {
    category: "Library text",
    author: "Baḥya ibn Paquda",
    title: "Al-Hidāya ilā Farāʾiḍ al-Qulūb (Ḥovot ha-Levavot)",
    detail:
      "Yahuda edition, with Judah ibn Tibbon's Hebrew — parallel-aligned in the reader, via Sefaria.",
  },
  {
    category: "Library text",
    author: "Moses Maimonides",
    title: "Dalālat al-Ḥāʾirīn (Moreh Nevukhim)",
    detail: "Judeo-Arabic page images, Friedberg Jewish Manuscript Society.",
  },
  {
    category: "Library text",
    author: "Saʿadya Gaon",
    title: "Kitāb al-Amānāt wa-l-Iʿtiqādāt (Emunot ve-Deʿot)",
    detail: "Judeo-Arabic page images, Friedberg Jewish Manuscript Society.",
  },
  {
    category: "Library text",
    author: "Judah Halevi",
    title: "Kitāb al-Khazarī (Kuzari)",
    detail: "Judeo-Arabic page images, Friedberg Jewish Manuscript Society.",
  },
  {
    category: "Library text",
    author: "Yaʿqūb al-Qirqisānī",
    title: "Kitāb al-Anwār wa-l-Marāqib",
    detail: "Karaite witness, included in the Advanced library.",
  },
];

export default function AboutPage() {
  return (
    <article className="mx-auto max-w-3xl px-6 py-16 sm:py-20">
      <p className="label label-accent mb-4">About</p>
      <h1 className="display text-4xl leading-tight sm:text-5xl">
        Methodology &amp; Sources
      </h1>
      <p className="mt-6 text-lg leading-relaxed text-ink/75">
        <em>Judeo-Arabic: A Digital Reader &amp; Lexicon</em> presents the
        Hebrew-script Arabic of the Geonic and medieval period — beginning with
        Saadia Gaon&apos;s Tafsir on the Torah — alongside parallel Hebrew and
        English and a word-by-word lexicon. It is built for Hebrew readers who
        want to read these texts in the original rather than in translation.
      </p>

      {/* Editorial principles */}
      <section className="mt-14">
        <h2 className="display text-2xl text-ink">Editorial principles</h2>
        <div className="mt-6 space-y-5 leading-relaxed text-ink/80">
          <p>
            <strong className="font-semibold">Source-first.</strong> Every text
            is given in its Judeo-Arabic original. Translations are aids, not
            substitutes: the Hebrew column reproduces a received translation
            (ibn Tibbon for Bahya; the Masoretic verse beside the Tafsir), and
            the English is editorial.
          </p>
          <p>
            <strong className="font-semibold">Glosses are provenanced.</strong>{" "}
            Tap-to-define glosses paraphrase Lane&apos;s{" "}
            <em>Arabic-English Lexicon</em> for the classical sense, with a
            separate layer of notes — drawn from Blau&apos;s{" "}
            <em>Dictionary of Mediaeval Judaeo-Arabic Texts</em> — flagging
            where a word carries a specifically Judeo-Arabic or
            Saadianic meaning. The two are kept distinct so a classical gloss is
            never silently presented as a medieval one.
          </p>
          <p>
            <strong className="font-semibold">Alignment is explicit.</strong>{" "}
            The reader aligns the Judeo-Arabic to its translation line by line,
            not paragraph by paragraph, so a reader can always see which Arabic
            words a given rendering answers to.
          </p>
          <p>
            <strong className="font-semibold">Scope and limits.</strong> The
            concordance indexes{" "}
            <span className="font-semibold text-ink">
              {fmt(corpusStats.totalTokens)} words
            </span>{" "}
            across{" "}
            <span className="font-semibold text-ink">
              {corpusStats.chapters} chapters
            </span>{" "}
            of the Tafsir; the lexicon holds{" "}
            <span className="font-semibold text-ink">
              {fmt(corpusStats.dictionaryEntries)} entries
            </span>{" "}
            over{" "}
            <span className="font-semibold text-ink">
              {fmt(corpusStats.uniqueRoots)} roots
            </span>
            . Coverage is hand-curated for the highest-frequency vocabulary
            first; rarer forms may resolve to a root entry rather than an exact
            inflection. This is a living edition, not a closed critical one.
          </p>
        </div>
      </section>

      {/* Bibliography */}
      <section className="mt-14" id="bibliography">
        <h2 className="display text-2xl text-ink">Bibliography &amp; editions</h2>
        <p className="mt-3 text-sm leading-relaxed text-muted">
          The base texts, lexica, and manuscript sources this edition draws on.
        </p>
        <div className="mt-6 overflow-x-auto rounded-sm border border-ink/10 bg-page">
          <table className="scholarly-table">
            <thead>
              <tr>
                <th scope="col">Type</th>
                <th scope="col">Author</th>
                <th scope="col">Work</th>
              </tr>
            </thead>
            <tbody>
              {BIBLIOGRAPHY.map((b) => (
                <tr key={b.author + b.title}>
                  <td className="whitespace-nowrap text-muted">{b.category}</td>
                  <td className="font-semibold text-ink">{b.author}</td>
                  <td>
                    <span className="italic">{b.title}</span>
                    <span className="mt-0.5 block text-xs leading-snug text-muted">
                      {b.detail}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* How to cite & license */}
      <section className="mt-14">
        <h2 className="display text-2xl text-ink">How to cite &amp; license</h2>
        <p className="mt-6 leading-relaxed text-ink/80">
          To cite this site, the suggested form is:
        </p>
        <div className="apparatus mt-4 rounded-sm">
          Eli Freedman, ed.,{" "}
          <em>Judeo-Arabic: A Digital Reader &amp; Lexicon</em>{" "}
          (judeo-arabic-app.vercel.app). Accessed{" "}
          <span className="text-ink/60">[date]</span>.
        </div>
        <p className="mt-6 leading-relaxed text-ink/80">
          Editorial text, translations, glosses, and notes are released under{" "}
          <a
            href="https://creativecommons.org/licenses/by-nc/4.0/"
            className="text-wine underline-offset-2 hover:underline"
          >
            CC BY-NC 4.0
          </a>
          . Source texts and manuscript images remain under the rights of their
          respective editions and holding institutions (see the bibliography
          above). Questions and corrections are welcome at{" "}
          <a
            href="mailto:freedmaneli@gmail.com"
            className="text-wine underline-offset-2 hover:underline"
          >
            freedmaneli@gmail.com
          </a>
          .
        </p>
      </section>

      <div className="mt-16 border-t border-ink/10 pt-6">
        <Link
          href="/"
          className="text-sm font-semibold text-wine underline-offset-4 hover:underline"
        >
          ← Back to the reader
        </Link>
      </div>
    </article>
  );
}

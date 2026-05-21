import type { Metadata } from "next";
import Link from "next/link";
import divergenceData from "@/data/tafsir-divergence.json";
import type { DivergenceEntry } from "@/lib/divergence";

export const metadata: Metadata = {
  title: "In memoriam — Joshua Blau ז״ל (1919–2020)",
  description:
    "This site uses the lexicographical work of Joshua Blau extensively. He passed away before we could ask his permission. This page records what we draw on, where, and with what gratitude.",
  alternates: { canonical: "/about/blau" },
  robots: { index: true, follow: true },
};

const ENTRIES = (divergenceData as { entries: DivergenceEntry[] }).entries;

function entriesByBlauRelation(relation: "direct" | "adjacent" | "different-sense") {
  return ENTRIES.filter((e) => e.blau_dict?.relation === relation);
}

export default function BlauTributePage() {
  const direct = entriesByBlauRelation("direct");
  const adjacent = entriesByBlauRelation("adjacent");
  const different = entriesByBlauRelation("different-sense");

  return (
    <article className="max-w-3xl mx-auto px-6 py-16 pb-32">
      <header className="mb-12">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          About · attribution
        </p>
        <h1 className="text-4xl tracking-tight text-ink leading-tight">
          In memoriam —{" "}
          <span className="text-wine italic">Joshua Blau</span> ז״ל
        </h1>
        <p className="mt-3 text-base text-ink/65 italic">
          Yehoshua (Joshua) Blau · Cluj 22 September 1919 — Jerusalem 20
          October 2020
        </p>
        <p className="mt-4 text-[13px] text-ink/70">
          Selected papers and the festschrift honoring his 70th birthday are
          posted on his Hebrew University Academia page:{" "}
          <a
            href="https://huji.academia.edu/JoshuaBlau"
            target="_blank"
            rel="noopener noreferrer"
            className="text-wine hover:underline"
          >
            huji.academia.edu/JoshuaBlau
          </a>
          .
        </p>
      </header>

      <section className="space-y-5 text-[15.5px] leading-relaxed text-ink/85 mb-12">
        <p>
          This site exists because of his work. The tap-to-define glosses on
          the Tafsir reader, the &ldquo;Tafsir twist&rdquo; cards that flag
          Saadia&apos;s anti-anthropomorphic and philosophical word-choices,
          and much of the medieval Hebrew-script-Arabic vocabulary on
          surrounding pages all draw — to one degree or another — on the
          lexicographical infrastructure Joshua Blau built across seven
          decades.
        </p>
        <p>
          He died in October 2020, in Jerusalem, at age 101. We never had the
          chance to ask him whether he&apos;d want his scholarship used this
          way. This page is what we can do instead: name him plainly, record
          what we draw on, and link to his work where the reader can verify
          and extend.
        </p>
      </section>

      <section className="mb-12">
        <h2 className="text-xs uppercase tracking-[0.3em] text-wine mb-4">
          A very brief sketch
        </h2>
        <div className="space-y-4 text-[15px] leading-relaxed text-ink/80">
          <p>
            Born in Cluj in 1919, Blau came to Mandate Palestine with his
            family in 1938. He took an MA in Hebrew, Arabic, and Biblical
            studies in 1942, and in 1950 completed his doctorate at the
            Hebrew University with a dissertation titled &ldquo;The Grammar
            of Judeo-Arabic&rdquo; — a project he would expand and revise
            for the rest of his life. He taught at the Hebrew University
            from 1957 to 1986, and continued mentoring students as professor
            emeritus into his late nineties.
          </p>
          <p>
            He served as President of the Academy of the Hebrew Language
            from 1981 to 1993, and edited its journal{" "}
            <span className="italic">Leshonenu</span> until 1999. He was
            elected to the Israel Academy of Sciences and Humanities in 1968
            and named a Corresponding Fellow of the British Academy in 1983.
            He received the Israel Prize for Linguistics and Hebrew Language
            in 1985, along with the Ben-Zvi and Rothschild Prizes.
          </p>
          <p>
            His scholarly project was, in the end, a single thing: to make
            the textual world of Arabic-speaking medieval Jews legible. He
            edited Maimonides&apos; responsa, traced the grammatical
            substrate of Christian Arabic, gave &ldquo;Middle Arabic&rdquo;
            a place as a register distinct from both Classical and Modern
            Standard — and over the last decades of his life, assembled a
            dictionary that for the first time gave readers a place to look
            up the medieval Judeo-Arabic words that Saadia, Bahya,
            Maimonides, Yefet ben Eli, and the Geniza letter-writers actually
            used.
          </p>
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-xs uppercase tracking-[0.3em] text-wine mb-4">
          The works this project draws on
        </h2>
        <ul className="space-y-4 text-[14.5px] leading-relaxed text-ink/85">
          <li>
            <span className="italic">
              A Dictionary of Mediaeval Judaeo-Arabic Texts
            </span>
            . Jerusalem: The Israel Academy of Sciences and Humanities and the
            Bialik Institute, 2006. — The principal reference behind the
            tap-to-define glosses and the &ldquo;Tafsir twist&rdquo;
            divergence cards. Where a divergence entry can genuinely be
            anchored in a Blau dictionary entry, we cite the root and gloss
            verbatim.
          </li>
          <li>
            <span className="italic">
              A Grammar of Mediaeval Judaeo-Arabic
            </span>{" "}
            (2nd, rev. ed., Jerusalem: Magnes Press, 1980). — The framework
            for understanding why a verb is in Form II rather than Form I,
            why a feminine accusative ends in –ה, and why Saadia uses Aramaic
            calques where classical Arabic would not.
          </li>
          <li>
            &ldquo;עיונים בתרגום רב סעדיה גאון לבראשית פרקים א-יב&rdquo;
            (Studies in Saadia Gaon&apos;s Translation of Genesis, Chapters
            1–12), in{" "}
            <span className="italic">
              ספר זכרון לרב יוסף בן דוד קאפח זצ&quot;ל
            </span>{" "}
            (Festschrift in memory of R. Yosef Kafiḥ), pp. 309–318. — A
            verse-by-verse commentary on Saadia&apos;s Genesis Tafsir. We
            quote it whenever a Festschrift note treats the same verse as a
            divergence card, even when the lexeme is different — see, e.g.,
            the cross-reference on Gen 3:16.
          </li>
          <li>
            <span className="italic">
              The Emergence and Linguistic Background of Judaeo-Arabic
            </span>{" "}
            (Oxford: Oxford University Press, 1965; 2nd, rev. ed., Jerusalem:
            Ben-Zvi Institute, 1981). — The historical grounding for how
            we describe Judeo-Arabic on{" "}
            <Link href="/what-is-judeo-arabic" className="text-wine hover:underline">
              /what-is-judeo-arabic
            </Link>
            .
          </li>
        </ul>
      </section>

      <section className="mb-12">
        <h2 className="text-xs uppercase tracking-[0.3em] text-wine mb-4">
          Where, exactly, we cite him
        </h2>
        <p className="text-[14.5px] leading-relaxed text-ink/80 mb-5">
          The divergence cards in the Tafsir reader (&ldquo;Advanced
          mode&rdquo;) each carry a{" "}
          <code className="font-mono text-[12.5px]">sources</code> field. Of
          the {ENTRIES.length} entries currently in the set:
        </p>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6 text-[13px]">
          <div className="rounded-md border border-ink/15 bg-page/60 p-4">
            <div className="text-2xl text-wine tabular-nums">
              {direct.length}
            </div>
            <div className="text-[11px] uppercase tracking-wider text-muted mt-1">
              Direct Blau backing
            </div>
            <p className="text-ink/70 mt-2 leading-snug">
              The dictionary entry directly attests the sense the card
              describes.
            </p>
          </div>
          <div className="rounded-md border border-ink/15 bg-page/60 p-4">
            <div className="text-2xl text-ink/80 tabular-nums">
              {adjacent.length}
            </div>
            <div className="text-[11px] uppercase tracking-wider text-muted mt-1">
              Adjacent
            </div>
            <p className="text-ink/70 mt-2 leading-snug">
              Blau treats the root, but in a related (not identical) sense
              or form.
            </p>
          </div>
          <div className="rounded-md border border-ink/15 bg-page/60 p-4">
            <div className="text-2xl text-ink/80 tabular-nums">
              {different.length}
            </div>
            <div className="text-[11px] uppercase tracking-wider text-muted mt-1">
              Different sense
            </div>
            <p className="text-ink/70 mt-2 leading-snug">
              Blau records the word in a different semantic field; the
              divergence is our reading against Lane, not his.
            </p>
          </div>
        </div>

        <details className="text-[14px] leading-relaxed text-ink/80 mt-6">
          <summary className="cursor-pointer text-wine hover:underline text-[13px]">
            See the {direct.length} entries with direct Blau backing
          </summary>
          <ul className="mt-3 space-y-3 ml-2">
            {direct.map((e) => (
              <li key={e.lemma_ja} className="border-l-2 border-wine/30 pl-4">
                <div className="font-mono text-[13px] text-ink/90" dir="rtl">
                  {e.lemma_ja}{" "}
                  <span className="text-muted">· √{e.root}</span>
                </div>
                <div className="text-[13px] text-ink/75 mt-1 leading-snug">
                  Blau,{" "}
                  <span className="italic">Dictionary</span>, s.v.{" "}
                  <span className="font-mono">{e.blau_dict?.root}</span> —{" "}
                  {e.blau_dict?.sense}
                </div>
              </li>
            ))}
          </ul>
        </details>
      </section>

      <section className="mb-12">
        <h2 className="text-xs uppercase tracking-[0.3em] text-wine mb-4">
          Further reading
        </h2>
        <ul className="space-y-3 text-[14px] leading-relaxed text-ink/80">
          <li>
            <a
              href="https://huji.academia.edu/JoshuaBlau"
              target="_blank"
              rel="noopener noreferrer"
              className="text-wine hover:underline"
            >
              Joshua Blau ז״ל on Academia.edu
            </a>{" "}
            — papers and the 70th-birthday festschrift, hosted on his Hebrew
            University Academia page.
          </li>
          <li>
            <a
              href="https://en.wikipedia.org/wiki/Yehoshua_Blau"
              target="_blank"
              rel="noopener noreferrer"
              className="text-wine hover:underline"
            >
              Yehoshua Blau (Wikipedia)
            </a>{" "}
            — biographical overview, with publication list.
          </li>
          <li>
            <a
              href="https://brill.com/view/journals/jjl/8/1-2/article-p1_1.xml"
              target="_blank"
              rel="noopener noreferrer"
              className="text-wine hover:underline"
            >
              &ldquo;In Memoriam, Professor Joshua Blau z&rdquo;l (1919–2020)&rdquo;
            </a>{" "}
            in the{" "}
            <span className="italic">Journal of Jewish Languages</span>{" "}
            8 (2020) — academic memorial.
          </li>
          <li>
            <a
              href="https://www.timesofisrael.com/prof-yehoshua-blau-giant-of-semitic-languages-dies-at-101/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-wine hover:underline"
            >
              &ldquo;Prof. Yehoshua Blau, giant of Semitic languages, dies at
              101&rdquo;
            </a>{" "}
              — <span className="italic">The Times of Israel</span>,
              obituary.
          </li>
          <li>
            <a
              href="https://networks.h-net.org/node/28655/discussions/6611499/passing-professor-joshua-blau"
              target="_blank"
              rel="noopener noreferrer"
              className="text-wine hover:underline"
            >
              &ldquo;Passing of Professor Joshua Blau&rdquo;
            </a>{" "}
            — H-Net announcement with details on his Academia.edu archive
            and his Maimonides responsa edition.
          </li>
        </ul>
      </section>

      <section className="rounded-md bg-wine/5 border border-wine/30 p-6 text-[14px] leading-relaxed text-ink/85">
        <p className="mb-3">
          Scholarly use of a printed reference work falls under standard fair
          use, and any errors in attribution or interpretation are entirely
          ours — Blau&apos;s name appears in this project to credit, not to
          license. If a representative of his estate, the Israel Academy, or
          the Bialik Institute would like a citation revised, an entry
          re-attributed, or the project to engage Blau&apos;s scholarship
          differently, please write:{" "}
          <a
            href="mailto:freedmaneli@gmail.com"
            className="text-wine hover:underline"
          >
            freedmaneli@gmail.com
          </a>
          .
        </p>
        <p className="text-ink/70">
          .יהי זכרו ברוך
        </p>
      </section>
    </article>
  );
}

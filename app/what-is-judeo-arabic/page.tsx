import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "What is Judeo-Arabic? — A short guide for Hebrew readers",
  description:
    "Judeo-Arabic is the Arabic language written in Hebrew letters, used by Jews across the medieval Islamic world for almost everything: Bible translation, philosophy, law, science, poetry, business letters. A short guide to who wrote it, what survives, and why it's worth learning.",
  alternates: { canonical: "/what-is-judeo-arabic" },
  openGraph: { type: "article" },
};

export default function WhatIsJudeoArabicPage() {
  return (
    <article className="max-w-3xl mx-auto px-6 py-16 sm:py-24 pb-32">
      <header className="mb-12">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          A short guide
        </p>
        <h1 className="text-4xl sm:text-5xl tracking-tight text-ink leading-tight">
          What is <span className="text-wine italic">Judeo-Arabic</span>?
        </h1>
        <p className="mt-6 text-lg text-ink/75 leading-relaxed">
          Judeo-Arabic is the Arabic language written in Hebrew letters. For
          roughly a thousand years — from the rise of Islam through the early
          modern period — it was the everyday written language of most of
          world Jewry, from Baghdad to Córdoba, Cairo to Yemen.
        </p>
      </header>

      <section className="mb-12 prose-section">
        <h2 className="text-2xl text-ink mb-4">The one-sentence version</h2>
        <p className="text-[16px] text-ink/85 leading-relaxed">
          When Jews in the Islamic world wrote in Arabic — and they wrote a
          lot — they wrote it in the Hebrew alphabet rather than the Arabic
          one. The language underneath is Arabic; the script on the page is
          Hebrew. That&apos;s the whole trick.
        </p>
        <div
          dir="rtl"
          className="font-hebrew text-2xl text-wine/90 mt-6 leading-loose text-center"
        >
          אול מא כ׳לק אללה. אלסמאואת ואלארץ׳
        </div>
        <p className="text-xs uppercase tracking-widest text-muted mt-2 text-center">
          Saadia, Bereshit 1:1 — &ldquo;The first thing God created: the heavens
          and the earth.&rdquo;
        </p>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl text-ink mb-4">When and where</h2>
        <p className="text-[16px] text-ink/85 leading-relaxed mb-4">
          The conventional dating is{" "}
          <strong>ca. 800 – 1500 CE</strong> for the classical period (with
          Yemenite Jews continuing to write in Judeo-Arabic well into the
          twentieth century). The geographic range is essentially the medieval
          Islamic world: Iraq, Egypt, North Africa, al-Andalus, the Levant,
          Yemen.
        </p>
        <p className="text-[16px] text-ink/85 leading-relaxed">
          Within that range it served as the prestige written language of
          Jewish communities. A Jewish merchant in Fustat (Old Cairo) writing
          to his partner in Aden, a rabbinic court in Qayrawan issuing a
          responsum, Maimonides drafting the <em>Guide of the Perplexed</em>{" "}
          in Cairo — all of them wrote Judeo-Arabic.
        </p>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl text-ink mb-4">Why Hebrew letters?</h2>
        <p className="text-[16px] text-ink/85 leading-relaxed mb-4">
          Three reasons, roughly in order of importance:
        </p>
        <ol className="list-decimal pl-6 space-y-3 text-[16px] text-ink/85 leading-relaxed">
          <li>
            <strong>Scribal training.</strong> Jewish boys learned the Hebrew
            alphabet in school. The Arabic alphabet was something you&apos;d
            pick up if you needed to read state documents or correspond with
            non-Jews — but for in-group writing, Hebrew letters were just
            faster.
          </li>
          <li>
            <strong>Quotation.</strong> Almost any Jewish text quotes Bible
            and Talmud. Switching scripts mid-sentence would be a nightmare,
            so the whole document stays in Hebrew letters and the Hebrew
            quotations just sit there in the same script as the surrounding
            Arabic.
          </li>
          <li>
            <strong>Audience.</strong> Writing in Hebrew letters quietly
            marks the text as Jewish — addressed to other Jews, intelligible
            inside the community.
          </li>
        </ol>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl text-ink mb-4">What was written in it</h2>
        <p className="text-[16px] text-ink/85 leading-relaxed mb-4">
          Almost everything. To name only the genres with surviving canonical
          works:
        </p>
        <ul className="list-disc pl-6 space-y-2 text-[16px] text-ink/85 leading-relaxed">
          <li>
            <strong>Bible translation and commentary</strong> —{" "}
            <Link href="/learn/saadia-story" className="text-wine hover:underline">
              Saadia Gaon&apos;s
            </Link>{" "}
            <em>Tafsir</em> on the Torah (and on most of the rest of Tanakh);
            the Karaite commentaries of Yefet ben Eli and Yeshu‘a ben
            Yehudah; Tanchum Yerushalmi&apos;s lexicons.
          </li>
          <li>
            <strong>Jewish philosophy</strong> — Saadia&apos;s <em>Book of
            Beliefs and Opinions</em>; Bahya ibn Paquda&apos;s{" "}
            <em>Chovot HaLevavot</em>; Yehudah HaLevi&apos;s <em>Kuzari</em>;
            Maimonides&apos; <em>Guide of the Perplexed</em>; the writings
            of Avraham ben HaRambam.
          </li>
          <li>
            <strong>Halakhah</strong> — the Geonim&apos;s responsa from
            Sura and Pumbedita; Hai Gaon&apos;s legal monographs;
            Maimonides&apos; commentary on the Mishnah; the legal works of
            Shmuel ben Hofni.
          </li>
          <li>
            <strong>Karaite legal and theological writing</strong> — Ya‘qub
            al-Qirqisani&apos;s <em>Kitab al-Anwar wal-Maraqib</em>, an
            encyclopedic survey of Jewish sectarian history and law; David
            al-Fasi&apos;s biblical lexicon.
          </li>
          <li>
            <strong>Science, medicine, grammar</strong> — Yonah ibn Janah on
            Hebrew grammar; medical works by Maimonides; star tables and
            calendrical writing.
          </li>
          <li>
            <strong>Letters and documents</strong> — the tens of thousands
            of Cairo Genizah documents that have given us the texture of
            medieval Mediterranean Jewish life: marriage contracts, business
            partnerships, personal letters, court records.
          </li>
        </ul>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl text-ink mb-4">The Cairo Genizah</h2>
        <p className="text-[16px] text-ink/85 leading-relaxed mb-4">
          A staggering proportion of what survives in Judeo-Arabic — perhaps
          the majority of the documentary corpus — comes from a single attic
          room in the Ben Ezra Synagogue in Fustat. The Cairo Genizah held
          roughly 400,000 fragments, dating from the 9th century onward,
          preserved for almost a millennium and dispersed across libraries
          (Cambridge, Oxford, Manchester, JTS, Penn, the Russian National
          Library, and others) starting in the 1890s.
        </p>
        <p className="text-[16px] text-ink/85 leading-relaxed">
          Modern editing of the Judeo-Arabic corpus has happened mostly out
          of the Genizah. The standard reference dictionary for the
          documentary materials is Joshua Blau&apos;s{" "}
          <em>Dictionary of Medieval Judaeo-Arabic Texts</em> (Jerusalem,
          2006), which is what powers the tap-to-define glosses in the
          readers on this site.
        </p>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl text-ink mb-4">
          Why learn Judeo-Arabic today?
        </h2>
        <p className="text-[16px] text-ink/85 leading-relaxed mb-4">
          Because most of the major Jewish books written in the medieval
          Islamic world were written in it — and reading them in translation
          is reading them at one remove. The <em>Kuzari</em>, the{" "}
          <em>Guide</em>, the <em>Chovot HaLevavot</em>, Saadia&apos;s
          Tafsir on Bereshit: all of them are written in a language a
          Hebrew reader can pick up faster than they expect.
        </p>
        <p className="text-[16px] text-ink/85 leading-relaxed">
          The script is already familiar. The vocabulary overlaps with
          Hebrew in the obvious ways and with Aramaic in the slightly
          deeper ones. The hardest part is mostly orthographic conventions
          and a handful of diacritic letters — which is what the{" "}
          <Link href="/alphabet" className="text-wine hover:underline">
            alphabet lessons
          </Link>{" "}
          on this site exist to teach.
        </p>
      </section>

      <section className="mb-12 rounded-md bg-wine/[0.05] border border-wine/30 p-8">
        <h2 className="text-2xl text-ink mb-3">Start reading</h2>
        <p className="text-[16px] text-ink/85 leading-relaxed mb-5">
          The shortest path from here to reading Saadia is about ninety
          minutes of focused work.
        </p>
        <div className="flex flex-wrap gap-4">
          <Link
            href="/alphabet"
            className="inline-flex items-center gap-2 px-5 py-2.5 bg-wine text-page rounded-sm text-sm tracking-wider hover:bg-wine/90 transition-colors"
          >
            Start with the alphabet <span aria-hidden>→</span>
          </Link>
          <Link
            href="/tafsir/bereshit/1"
            className="inline-flex items-center gap-2 px-5 py-2.5 border border-wine/40 text-wine rounded-sm text-sm tracking-wider hover:bg-wine/5 transition-colors"
          >
            Or jump into Saadia <span aria-hidden>→</span>
          </Link>
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl text-ink mb-4">Further reading</h2>
        <ul className="space-y-3 text-[15px] text-ink/80 leading-relaxed">
          <li>
            Joshua Blau, <em>A Grammar of Medieval Judaeo-Arabic</em>{" "}
            (Jerusalem, 2nd ed. 1980). The standard grammar.
          </li>
          <li>
            Joshua Blau, <em>Dictionary of Medieval Judaeo-Arabic Texts</em>{" "}
            (Jerusalem, 2006). The standard dictionary; what the readers on
            this site cite.
          </li>
          <li>
            Esther-Miriam Wagner, <em>Linguistic Variety of Judaeo-Arabic
            in Letters from the Cairo Genizah</em> (Brill, 2010). Excellent
            on the documentary register.
          </li>
          <li>
            Geoffrey Khan, ed.,{" "}
            <em>Encyclopedia of Hebrew Language and Linguistics</em>{" "}
            (Brill). The entries on Judeo-Arabic by Blau, Khan, and others
            are the standard reference articles.
          </li>
          <li>
            Sasson Somekh,{" "}
            <em>Studies in Modern Arabic Prose and Poetry</em> and his
            collected essays on Jewish-Arabic literature, for the modern
            tail of the tradition.
          </li>
        </ul>
      </section>

      <nav className="mt-16 pt-8 border-t border-ink/10 flex flex-wrap items-center gap-x-6 gap-y-2 text-sm">
        <Link href="/" className="text-ink/70 hover:text-wine">
          ← Home
        </Link>
        <Link href="/alphabet" className="text-ink/70 hover:text-wine">
          Alphabet lessons
        </Link>
        <Link
          href="/tafsir/bereshit/1"
          className="text-wine hover:underline ml-auto"
        >
          Open Saadia&apos;s Tafsir →
        </Link>
      </nav>
    </article>
  );
}

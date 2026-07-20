import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "The Library — classical Judeo-Arabic prose",
  description:
    "Classical Judeo-Arabic prose with parallel Hebrew and English: Bahya ibn Paquda, Maimonides, Saadia Gaon, Qirqisani, and Judah Halevi are live; Yefet ben Eli is forthcoming.",
  alternates: { canonical: "/advanced" },
};

type LibraryEntry = {
  href: string | null;
  status: "Live" | "Coming soon";
  author: string;
  title: string;
  blurb: string;
  sample: string;
  /** Script of the `sample` line; defaults to Hebrew-letter Judeo-Arabic. */
  sampleScript?: "hebrew" | "arabic";
};

const library: LibraryEntry[] = [
  {
    href: "/advanced/bahya",
    status: "Live",
    author: "Bahya ibn Paquda",
    title: "Chovot HaLevavot — complete",
    blurb:
      "The complete Duties of the Hearts — Bahya's 11th-century Andalusian classic on the inner life of mitzvot — the introduction and all ten gates in its original Judeo-Arabic, with a tap-to-define dictionary on every word. The First Gate also carries a working English translation with phrase-by-phrase hover highlighting.",
    sample: "כתאב אלהדאיה אלי פראיץ' אלקלוב",
  },
  {
    href: "/advanced/rambam-mishnah",
    status: "Live",
    author: "Moses Maimonides",
    title: "Commentary on the Mishnah",
    blurb:
      "Rambam's Commentary on the Mishnah in its original 12th-century Judeo-Arabic — Tractate Avot with the Eight Chapters (Shemonah Perakim) on the soul and the virtues, and Tractate Sanhedrin including the essay on the 13 Principles of Faith and the World to Come. With working English translations.",
    sample: "שרח אלמשנה",
  },
  {
    href: "/advanced/rambam-moreh-nevukhim",
    status: "Live",
    author: "Moses Maimonides",
    title: "Dalālat al-Ḥā'irīn — Moreh Nevukhim",
    blurb:
      "Rambam's Guide of the Perplexed in its 12th-century Judeo-Arabic original — the whole of Part I (chapters 1–28): from 'image and likeness' and Adam's sin through the equivocal terms of place, throne, ascent, sitting, standing, and motion by which Scripture speaks of God, and on to Onkelos's method of removing corporeality. With a working English translation, phrase-by-phrase hover highlighting, and notes on key terms.",
    sample: "דלאלה אלחאירין",
  },
  {
    href: "/advanced/saadia-emunot-vedeot",
    status: "Live",
    author: "Saadia Gaon",
    title: "Kitāb al-Amānāt — Emunot v'Deot",
    blurb:
      "The opening of Saadia's 10th-century systematic theology — the work that gave Geonic Judaism its philosophical vocabulary: why doubt befalls people in their inquiries and how knowledge dispels it, in the original Judeo-Arabic with a working English translation, phrase-by-phrase hover highlighting, and notes on key terms.",
    sample: "כתאב אלאמאנאת ואלאעתקאדאת",
  },
  {
    href: "/advanced/yefet-ben-eli",
    status: "Coming soon",
    author: "Yefet ben Eli",
    title: "Karaite commentaries on the Bible",
    blurb:
      "The most prolific Karaite exegete of the 10th century, in his lucid Judeo-Arabic prose. Selections from his commentaries on the Pentateuch, Prophets, and Writings.",
    sample: "תפסיר יפת בן עלי",
  },
  {
    href: "/advanced/qirqisani-anwar",
    status: "Live",
    author: "Yaʿqūb al-Qirqisānī",
    title: "Kitāb al-Anwār wa'l-Marāqib",
    blurb:
      "The opening of the great 10th-century Karaite summa — its manifesto that religious obligations must be reached by inquiry and rational speculation (baḥth wa-naẓar), and the truth accepted from whoever holds it. Shown in the original Arabic (ed. Nemoy) with a working English translation, phrase-by-phrase hover highlighting, and notes on key terms.",
    sample: "كتاب الأنوار والمراقب",
    sampleScript: "arabic",
  },
  {
    href: "/advanced/kuzari",
    status: "Live",
    author: "Judah Halevi",
    title: "Kitāb al-Khazarī — The Kuzari",
    blurb:
      "The complete Kuzari — all five maqalat — in its original 12th-century Judeo-Arabic, with a working English translation and phrase-by-phrase hover highlighting throughout. Every word carries a tap-to-define dictionary gloss. Maqala I also includes notes on nine key philosophical terms.",
    sample: "כתאב אלרד ואלדליל פי אלדין אלד'ליל",
  },
];

export default function LibraryIndex() {
  return (
    <div className="max-w-5xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12 max-w-2xl">
        <p className="label mb-3">
          Stage III · The Library
        </p>
        <h1 className="display text-4xl text-ink">
          Classical <span className="text-wine italic">prose</span>.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          Once you can read Saadia, the rest of the Judeo-Arabic library opens
          up. Each text appears with parallel Hebrew and English — and a
          tap-to-define dictionary on the Judeo-Arabic side.
        </p>
      </header>

      <ul className="grid gap-5 lg:grid-cols-2">
        {library.map((t) => {
          const isLive = t.status === "Live";
          const card = (
            <div
              className={`block rounded-md bg-page border p-7 transition-all ${
                isLive
                  ? "border-ink/10 hover:border-wine/40 hover:shadow-md hover:shadow-wine/5 cursor-pointer"
                  : "border-ink/10 opacity-70 hover:opacity-100 hover:border-wine/30"
              }`}
            >
              <div className="flex items-baseline gap-3">
                <span className={`badge ${isLive ? "badge-live" : "badge-muted"}`}>
                  {t.status}
                </span>
              </div>
              <div className="mt-3 text-xs uppercase tracking-[0.18em] text-ink/60">
                {t.author}
              </div>
              <div
                className={`mt-0.5 text-2xl text-ink transition-colors ${
                  isLive ? "group-hover:text-wine" : "group-hover:text-wine/80"
                }`}
              >
                {t.title}
              </div>
              <p className="mt-3 text-[15px] text-ink/70 leading-relaxed">
                {t.blurb}
              </p>
              <div
                dir="rtl"
                className={`${
                  t.sampleScript === "arabic" ? "font-arabic" : "font-hebrew"
                } text-xl text-ink/80 mt-5 leading-loose`}
              >
                {t.sample}
              </div>
            </div>
          );
          return (
            <li key={t.title}>
              {t.href ? (
                <Link href={t.href} className="group block">
                  {card}
                </Link>
              ) : (
                card
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

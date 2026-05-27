import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Stage 3 · The Library — classical Judeo-Arabic prose",
  description:
    "A growing shelf of classical Judeo-Arabic prose with parallel Hebrew and English: Bahya ibn Paquda, Maimonides, Saadia Gaon, Yefet ben Eli, Qirqisani, and Judah Halevi. Bahya's First Gate is live; the others are forthcoming.",
  alternates: { canonical: "/advanced" },
};

type LibraryEntry = {
  href: string | null;
  status: "Live" | "Coming soon";
  author: string;
  title: string;
  blurb: string;
  sample: string;
};

const library: LibraryEntry[] = [
  {
    href: "/advanced/bahya",
    status: "Live",
    author: "Bahya ibn Paquda",
    title: "Chovot HaLevavot — The First Gate",
    blurb:
      "The opening gate of Bahya's 11th-century Andalusian classic on the inner life of mitzvot, in its original Judeo-Arabic alongside Ibn Tibbon's classical Hebrew (Sefaria) and a working English translation. With tap-to-define dictionary.",
    sample: "תוחיד אללה תעאלי",
  },
  {
    href: "/advanced/rambam-moreh-nevukhim",
    status: "Live",
    author: "Moses Maimonides",
    title: "Dalālat al-Ḥā'irīn — Moreh Nevukhim",
    blurb:
      "The opening chapter of Rambam's Guide of the Perplexed in its 12th-century Judeo-Arabic original: why 'image and likeness' (tzelem u-demut) do not mean God has a body. With a working English translation, phrase-by-phrase hover highlighting, and notes on key terms.",
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
    status: "Coming soon",
    author: "Yaʿqūb al-Qirqisānī",
    title: "Kitāb al-Anwār wa'l-Marāqib",
    blurb:
      "The 10th-century Karaite encyclopedia of religious thought, law, and sect-history — a window onto a Judaism that argued in Arabic with Christians, Muslims, and other Jews.",
    sample: "כתאב אלאנואר ואלמראקב",
  },
  {
    href: "/advanced/kuzari",
    status: "Live",
    author: "Judah Halevi",
    title: "Kitāb al-Khazarī — The Kuzari",
    blurb:
      "The opening of Halevi's 12th-century defense of Judaism: the Khazar king's dream and the Aristotelian philosopher's answer, in the original Judeo-Arabic with a working English translation, phrase-by-phrase hover highlighting, and notes on key terms.",
    sample: "כתאב אלרד ואלדליל פי אלדין אלד'ליל",
  },
];

export default function LibraryIndex() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Stage 3 · The Library
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          Classical <span className="text-wine italic">prose</span>.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          Once you can read Saadia, the rest of the Judeo-Arabic library opens
          up. Each text appears with parallel Hebrew and English — and a
          tap-to-define dictionary on the Judeo-Arabic side.
        </p>
      </header>

      <ul className="space-y-5">
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
              <div className="flex items-baseline justify-between">
                <div className="text-xs uppercase tracking-[0.25em] text-muted">
                  {t.status}
                </div>
                <div className="text-xs tracking-wide text-ink/60">
                  {t.author}
                </div>
              </div>
              <div
                className={`mt-1 text-2xl text-ink transition-colors ${
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
                className="font-hebrew text-xl text-ink/80 mt-5 leading-loose"
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

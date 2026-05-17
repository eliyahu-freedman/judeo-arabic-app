import Link from "next/link";

const modules = [
  {
    href: "/alphabet",
    title: "Alphabet",
    subtitle: "Stage 1",
    body: "Five short lessons on how Hebrew letters render Arabic phonemes — including the diacritic letters (ג׳ ד׳ ח׳ ט׳ ת׳), the definite article אל, and orthographic ambiguities. Recognition + production drills.",
  },
  {
    href: "/tafsir",
    title: "Tafsir Reader",
    subtitle: "Stage 2 · Saadia on Bereshit 1",
    body: "Read Saadia's Tafsir verse-by-verse alongside the biblical Hebrew, with toggles for Arabic script, Hebrew translation, and English translation. Tap any Judeo-Arabic word for a Blau lexicon gloss.",
  },
  {
    href: "/advanced",
    title: "Advanced Reader",
    subtitle: "Stage 3 · Bahya's Introduction",
    body: "Read the opening of Bahya ibn Paquda's Chovot HaLevavot in its original Judeo-Arabic, with Hebrew (Ibn Tibbon) and English translations alongside, and the same tap-to-gloss lookup.",
  },
];

export default function Home() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-12 sm:py-20">
      <div className="mb-12 sm:mb-16">
        <h1 className="font-serif text-3xl sm:text-4xl tracking-tight text-stone-900">
          Learn to read Judeo-Arabic
        </h1>
        <p className="mt-4 text-stone-600 leading-relaxed">
          A reader-first introduction for Hebrew readers. Start with the script,
          then read Saadia&apos;s Tafsir on Bereshit, then move on to Bahya&apos;s
          philosophical prose — each text appears with parallel translations and
          a tap-to-define dictionary.
        </p>
      </div>
      <ul className="space-y-4">
        {modules.map((m) => (
          <li key={m.href}>
            <Link
              href={m.href}
              className="block rounded-lg border border-stone-200 bg-white p-6 transition-colors hover:border-stone-400"
            >
              <div className="text-xs uppercase tracking-widest text-stone-500">
                {m.subtitle}
              </div>
              <div className="mt-1 font-serif text-xl text-stone-900">
                {m.title}
              </div>
              <p className="mt-2 text-sm text-stone-600 leading-relaxed">
                {m.body}
              </p>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

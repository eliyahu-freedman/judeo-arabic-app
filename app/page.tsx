import Link from "next/link";

const modules = [
  {
    href: "/alphabet",
    title: "Alphabet",
    subtitle: "Stage 1",
    body: "Five short lessons on how Hebrew letters render Arabic phonemes — the diacritic letters (ג׳ ד׳ ח׳ ט׳ ת׳), the definite article אל, and the orthographic conventions of medieval Judeo-Arabic.",
    sample: "ג׳ · ד׳ · ח׳ · ט׳ · ת׳",
    sampleLang: "he" as const,
  },
  {
    href: "/tafsir",
    title: "Tafsir Reader",
    subtitle: "Stage 2 · Saadia on Bereshit 1",
    body: "Read Saadia's Tafsir verse-by-verse alongside the biblical Hebrew. Tap any Judeo-Arabic word for a starter Blau gloss; toggle Arabic-script, Hebrew translation, and (soon) English.",
    sample: "אול מא כ׳לק אללה",
    sampleLang: "he" as const,
  },
  {
    href: "/advanced",
    title: "Advanced Reader",
    subtitle: "Stage 3 · Bahya, The First Gate",
    body: "The opening gate of Bahya ibn Paquda's Chovot HaLevavot in its original Judeo-Arabic, with Ibn Tibbon's classical Hebrew translation (Sefaria) and a working English translation alongside.",
    sample: "אכ'לאץ תוחיד אלכ'אלק",
    sampleLang: "he" as const,
  },
];

export default function Home() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <section className="mb-16 sm:mb-20">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-4">
          A reader-first introduction
        </p>
        <h1 className="text-4xl sm:text-5xl tracking-tight text-ink leading-tight">
          Learn to read{" "}
          <span className="text-wine italic">Judeo-Arabic</span>.
        </h1>
        <p className="mt-6 text-lg text-ink/75 leading-relaxed max-w-2xl">
          For Hebrew readers: start with the script, read Saadia&apos;s Tafsir
          on Bereshit alongside the biblical text, then move on to Bahya&apos;s
          philosophical prose. Each text appears with parallel translations
          and a tap-to-define dictionary.
        </p>
        <div
          dir="rtl"
          className="font-hebrew text-2xl sm:text-3xl text-wine/90 mt-10 leading-loose"
        >
          אול מא כ׳לק אללה. אלסמאואת ואלארץ׳
        </div>
        <p className="text-xs uppercase tracking-widest text-muted mt-2">
          Saadia, Bereshit 1:1 — &ldquo;The first thing God created: the heavens
          and the earth.&rdquo;
        </p>
      </section>

      <ul className="space-y-5">
        {modules.map((m) => (
          <li key={m.href}>
            <Link
              href={m.href}
              className="group block rounded-md bg-page border border-ink/10 p-7 transition-all hover:border-wine/40 hover:shadow-md hover:shadow-wine/5"
            >
              <div className="text-xs uppercase tracking-[0.25em] text-muted">
                {m.subtitle}
              </div>
              <div className="mt-1 text-2xl text-ink group-hover:text-wine transition-colors">
                {m.title}
              </div>
              <p className="mt-3 text-[15px] text-ink/70 leading-relaxed">
                {m.body}
              </p>
              <div
                dir="rtl"
                className="font-hebrew text-xl text-ink/80 mt-5 leading-loose"
              >
                {m.sample}
              </div>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

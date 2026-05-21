import Link from "next/link";
import data from "@/data/saadia-tafsir-intro.json";

type Section = {
  n: number;
  kind: "title" | "subtitle" | "header" | "body";
  title?: string;
  ja: string;
  en: string;
  en_source: "sefaria-cc0" | "editor" | "sefaria-cc0-completed-by-editor";
};

type IntroData = {
  _note: string;
  _source: string;
  _extracted: string;
  sections: Section[];
};

const ENGLISH_NOTE: Record<Section["en_source"], string> = {
  "sefaria-cc0": "English: Sefaria Community Translation (CC0).",
  editor:
    "English: site editor's translation. Please flag errors — this is the first published English of this paragraph.",
  "sefaria-cc0-completed-by-editor":
    "English: Sefaria CC0 + completion by site editor (Sefaria's text cut off mid-paragraph).",
};

export default function SaadiaPrefacePage() {
  const payload = data as IntroData;
  const titleSections = payload.sections.filter(
    (s) => s.kind === "title" || s.kind === "subtitle",
  );
  const headerSection = payload.sections.find((s) => s.kind === "header");
  const bodySections = payload.sections.filter((s) => s.kind === "body");

  return (
    <div className="max-w-3xl mx-auto px-6 py-16 pb-32">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          <Link href="/learn" className="hover:text-wine">
            Learn
          </Link>{" "}
          · Saadia&apos;s preface
        </p>
        <h1 className="text-4xl tracking-tight text-ink leading-tight">
          Saadia&apos;s own <span className="text-wine italic">preface</span>.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          When Saadia finished translating the Torah into Arabic around the
          year 930, he wrote a short preface explaining what he was doing
          and why. It&apos;s one of the most personal documents in medieval
          Jewish letters. Below, his Judeo-Arabic alongside English — most
          of it being published in English for the first time.
        </p>
      </header>

      {/* Title cluster — small, centered */}
      <section className="my-12 text-center">
        {titleSections.map((s) => (
          <div key={s.n} className="my-1">
            <div
              dir="rtl"
              className={`font-hebrew text-ink leading-loose ${
                s.kind === "title" ? "text-3xl mt-2 mb-3" : "text-lg text-ink/85"
              }`}
            >
              {s.ja}
            </div>
            <div
              className={`text-ink/65 italic ${
                s.kind === "title" ? "text-lg" : "text-sm"
              }`}
            >
              {s.en}
            </div>
          </div>
        ))}
      </section>

      {headerSection && (
        <div className="my-12 text-center">
          <div
            dir="rtl"
            className="font-hebrew text-2xl text-ink leading-loose"
          >
            {headerSection.ja}
          </div>
          <div className="text-base text-ink/65 italic mt-1">
            {headerSection.en}
          </div>
        </div>
      )}

      {/* Body sections */}
      <ol className="space-y-12">
        {bodySections.map((s) => (
          <li key={s.n}>
            {s.title && (
              <h2 className="text-2xl text-ink mb-1">{s.title}</h2>
            )}
            <p className="text-[10px] uppercase tracking-[0.25em] text-muted mb-5">
              §{s.n}
            </p>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div
                dir="rtl"
                className="font-hebrew text-[17px] text-ink/95 leading-loose order-2 md:order-1 md:border-r md:border-ink/10 md:pr-6"
              >
                {s.ja.split(/\n\s*\n/).map((para, i) => (
                  <p key={i} className="mb-4 last:mb-0">
                    {para}
                  </p>
                ))}
              </div>
              <div className="text-[15px] text-ink/85 leading-relaxed order-1 md:order-2">
                {s.en.split(/\n\s*\n/).map((para, i) => (
                  <p key={i} className="mb-4 last:mb-0">
                    {para}
                  </p>
                ))}
              </div>
            </div>

            <p className="mt-5 text-[11px] text-muted italic">
              {ENGLISH_NOTE[s.en_source]}
            </p>
          </li>
        ))}
      </ol>

      {/* Footer attribution + nav */}
      <footer className="mt-16 pt-8 border-t border-ink/10">
        <p className="text-[12px] text-ink/60 leading-relaxed">
          <strong>Sources.</strong> Judeo-Arabic from Joseph Derenbourg&apos;s{" "}
          <em>Œuvres Complètes de R. Saadia ben Iosef al-Fayyoûmî</em> (Paris,
          1893), via Sefaria. English of §0–§6 and the opening of §10 is
          Sefaria&apos;s Community Translation (CC0). English of §7, §8, §9
          and the completion of §10 are by the site editor.
        </p>
        <nav className="mt-6 flex flex-wrap items-center gap-x-6 gap-y-2 text-sm">
          <Link href="/learn" className="text-ink/70 hover:text-wine">
            ← All lessons
          </Link>
          <Link
            href="/learn/saadia-story"
            className="text-ink/70 hover:text-wine"
          >
            ← Who was Saadia?
          </Link>
          <Link
            href="/tafsir/bereshit/1"
            className="text-wine hover:underline ml-auto"
          >
            Open the Tafsir →
          </Link>
        </nav>
      </footer>
    </div>
  );
}

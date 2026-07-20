import type { Metadata } from "next";
import Link from "next/link";
import { M1_GATES, M2_GATES, M3_GATES, M5_GATES } from "./chapters";

export const metadata: Metadata = {
  title: "Qirqisānī, Kitāb al-Anwār wa'l-Marāqib — in Judeo-Arabic",
  description:
    "Yaʿqūb al-Qirqisānī's 10th-century Karaite summa in its original Arabic: Discourses I–III (Sectology, Epistemology, Polemics) and Discourse V (Circumcision + Sabbath law), with a tap-to-define dictionary on every word.",
  alternates: { canonical: "/advanced/qirqisani-anwar" },
};

type SectionProps = {
  title: string;
  subtitle: string;
  gates: typeof M1_GATES;
};

function GateSection({ title, subtitle, gates }: SectionProps) {
  return (
    <section className="mb-14">
      <h2 className="text-2xl font-semibold text-ink mb-1">{title}</h2>
      <p className="text-sm text-ink/60 mb-6">{subtitle}</p>
      <ol className="space-y-2">
        {gates.map((g) => (
          <li key={g.slug}>
            <Link
              href={`/advanced/qirqisani-anwar/${g.slug}`}
              className="group flex items-baseline justify-between gap-3 rounded-md bg-page border border-ink/10 px-5 py-4 transition-all hover:border-wine/40 hover:shadow-md hover:shadow-wine/5"
            >
              <span className="text-base text-ink group-hover:text-wine transition-colors leading-snug">
                {g.section}
                {g.hasEnglish && (
                  <span className="badge badge-live ml-3 align-middle">
                    + English
                  </span>
                )}
                {g.hasHebrew && (
                  <span className="badge badge-live ml-1 align-middle">
                    + Hebrew
                  </span>
                )}
              </span>
              {g.section_ja && (
                <span
                  dir="rtl"
                  className="font-arabic text-base text-ink/65 shrink-0 text-right"
                >
                  {g.section_ja}
                </span>
              )}
            </Link>
          </li>
        ))}
      </ol>
    </section>
  );
}

export default function QirqisaniContents() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="label mb-3">Stage III · The Library</p>
        <h1 className="display text-4xl text-ink">
          Qirqisānī,{" "}
          <span className="text-wine italic">Kitāb al-Anwār</span>.
        </h1>
        <p className="mt-3 text-lg font-arabic text-ink/70" dir="rtl">
          كتاب الأنوار والمراقب
        </p>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          The 10th-century Karaite legal and theological summa of Yaʿqūb
          al-Qirqisānī — Discourse I on sectology, Discourse II on
          epistemology, Discourse III on polemics, and Discourse V on
          circumcision and the Sabbath — in the original Arabic and
          Judeo-Arabic. Every word taps through to a dictionary gloss.
          Chapters marked{" "}
          <span className="badge badge-live inline-block align-middle">
            + English
          </span>{" "}
          or{" "}
          <span className="badge badge-live inline-block align-middle">
            + Hebrew
          </span>{" "}
          carry working translations.
        </p>
      </header>

      <GateSection
        title="Discourse I: Sectology"
        subtitle="Qirqisānī's panorama of Jewish and para-Jewish sects — their doctrines, histories, and debates"
        gates={M1_GATES}
      />

      <GateSection
        title="Discourse II: Epistemology"
        subtitle="Qirqisānī's systematic theology — how knowledge arises, the attributes of God, prophecy, and resurrection"
        gates={M2_GATES}
      />

      <GateSection
        title="Discourse III: Polemics"
        subtitle="Qirqisānī's refutations of Samaritanism, Christianity, and Islam"
        gates={M3_GATES}
      />

      <GateSection
        title="Discourse V: Circumcision and the Sabbath"
        subtitle="Qirqisānī's legal analysis of the two foundational commandments, with Karaite–Rabbanite polemic throughout"
        gates={M5_GATES}
      />

      <p className="mt-10">
        <Link href="/advanced" className="text-sm text-muted hover:text-ink">
          ← Back to the Library
        </Link>
      </p>
    </div>
  );
}

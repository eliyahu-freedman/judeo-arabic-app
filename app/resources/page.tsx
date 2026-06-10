import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Resources — where else to learn Judeo-Arabic",
  description:
    "Curated outside resources for learning Judeo-Arabic: video lectures (Miriam Goldstein, Benjamin Hary, Ofra Tirosh-Becker), dictionaries, oral histories, music, and the closest things to a course in spoken Judeo-Arabic.",
  alternates: { canonical: "/resources" },
  openGraph: { type: "article" },
};

type ResourceLink = {
  title: string;
  href: string;
  note?: string;
  badge?: string;
};

type Section = {
  id: string;
  eyebrow: string;
  title: string;
  intro?: string;
  links: ResourceLink[];
};

const SECTIONS: Section[] = [
  {
    id: "hubs",
    eyebrow: "Start here",
    title: "If you want one place to start",
    intro:
      "These sites are the most complete public hubs for Judeo-Arabic learning materials — videos, audio, sample texts, transliteration charts, keyboards, dictionaries.",
    links: [
      {
        title: "Jewish Language Project — Judeo-Arabic page",
        href: "https://www.jewishlanguages.org/judeo-arabic",
        note: "The single richest public hub. Run by Sarah Bunin Benor (HUC). Sample audio, transliteration charts, a virtual JA keyboard, a JA↔Arabic transliterator, and links to the Oxford School of Rare Jewish Languages course.",
      },
      {
        title: "Endangered Language Alliance — Jewish Languages",
        href: "https://www.elalliance.org/projects/jewish-languages",
        note: "NYC-based documentation work with remaining Judeo-Arabic speakers.",
      },
      {
        title: "Living Tongues Institute — Jewish Languages overview",
        href: "https://livingtongues.org/jewish-languages/",
        note: "Broader survey of endangered Jewish languages, Judeo-Arabic among them.",
      },
    ],
  },
  {
    id: "lectures",
    eyebrow: "Video lectures",
    title: "Scholars on YouTube",
    intro:
      "Free, English-language lectures. Goldstein's Mandel lecture is the best one-hour starting point.",
    links: [
      {
        title:
          "Miriam Goldstein — Judeo-Arabic Literature 101 and Toledot Yeshu among Near Eastern Jews",
        href: "https://www.youtube.com/watch?v=zba-5cVqwWg",
        note: "Pearl and Jack Mandel Lecture in Jewish Studies. The best one-hour intro.",
        badge: "Video · 1 hr",
      },
      {
        title:
          "Miriam Goldstein — Speaking, Reading and Writing Arabic: A Revolution in Jewish History",
        href: "https://www.youtube.com/watch?v=fFyraGHxpuk",
        note: "Companion overview talk.",
        badge: "Video · 1 hr",
      },
      {
        title: "Miriam Goldstein — Jews and Arabic (full playlist)",
        href: "https://www.youtube.com/playlist?list=PLv2rnAORLiVCFGJWVGQpBOvMRsnxOUtnr",
        note: "Multi-part series for going deeper.",
        badge: "Video · series",
      },
      {
        title: "Benjamin Hary — The Language of the Jews of Islam",
        href: "https://www.youtube.com/watch?v=K_sBC5jp40Q",
        note: "Foundational overview by the late Benjamin Hary, who built the field of modern Judeo-Arabic studies.",
        badge: "Video",
      },
      {
        title: "Brad Sabin Hill — Oxford and the Printing of Judeo-Arabic",
        href: "https://www.youtube.com/watch?v=ea3PMqDv050",
        note: "On the surprising printed corpus of Judeo-Arabic, 18th–20th c.",
        badge: "Video",
      },
      {
        title: "Beit Avi Chai — Jews and Arabic series",
        href: "https://www.bac.org.il/videos/?seriesID=969",
        note: "Hebrew-language lectures from Beit Avi Chai's series.",
        badge: "Video · Hebrew",
      },
    ],
  },
  {
    id: "reference",
    eyebrow: "Reading & reference",
    title: "Books, dictionaries, corpora",
    links: [
      {
        title: "E. W. Lane, An Arabic-English Lexicon (Perseus TEI)",
        href: "https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2002.02.0004",
        note: "The 19th-century classical-Arabic reference paraphrased for this site's tap-to-define glosses.",
      },
      {
        title: "Joshua Blau, Dictionary of Medieval Judaeo-Arabic Texts",
        href: "https://magnespress.co.il/",
        note: "The standard dictionary of medieval Judeo-Arabic; consulted for a small set of divergence notes on the Tafsir reader.",
      },
      {
        title: "Assaf Bar-Moshe, Baghdadi Judeo-Arabic (UCL Press)",
        href: "https://uclpress.co.uk/book/baghdadi-judeo-arabic/",
        note: "Modern Baghdadi dialect — free open-access PDF.",
        badge: "Free PDF",
      },
      {
        title: "Jonas Sibony — Moroccan Judeo-Arabic dictionary",
        href: "https://www.jonas-sibony.com/djm/dictionnaire-judeo-marocain/",
        note: "The only free online Moroccan JA dictionary.",
        badge: "Free",
      },
      {
        title: "Bulbul — Judeo-Arabic corpus",
        href: "http://www.bulbul.sk/vwaajl/",
        note: "Searchable text corpus of JA religious and secular literature.",
      },
      {
        title: "Friedberg Jewish Manuscript Society",
        href: "https://fjms.genizah.org/",
        note: "Digitized Judeo-Arabic manuscripts (registration required).",
      },
      {
        title: "Princeton Geniza Project",
        href: "https://geniza.princeton.edu/pgp/",
        note: "Cairo Geniza documents in transcription, many JA.",
        badge: "Free",
      },
      {
        title: "University of Michigan — Judeo-Arabic research guide",
        href: "https://guides.lib.umich.edu/c.php?g=282911&p=6692906",
        note: "Annotated bibliography of dictionaries, grammars, literature surveys.",
      },
    ],
  },
  {
    id: "spoken",
    eyebrow: "Spoken Judeo-Arabic",
    title: "Hearing it — the honest answer",
    intro:
      "There is essentially no Duolingo-style course in spoken Judeo-Arabic. Most living speakers are over 80. The realistic options are oral-history archives (to hear it spoken) and modern Arabic-dialect courses for the underlying vernacular (Iraqi, Moroccan, Yemeni).",
    links: [
      {
        title: "Sephardi Voices",
        href: "https://www.sephardivoices.org.uk/",
        note: "Filmed oral histories. Audio-visual accounts in Judeo-Arabic, Ladino, and Haquetia alongside the main interviews.",
        badge: "Oral history",
      },
      {
        title: "JIMENA Oral History Program",
        href: "https://www.jimena.org/oral-history-program/",
        note: "Mizrahi and Sephardic testimonies from MENA Jews.",
        badge: "Oral history",
      },
      {
        title: "TalkInArabic — Iraqi dialect",
        href: "https://talkinarabic.com/iraqi/",
        note: "Closest practical proxy for spoken Baghdadi Judeo-Arabic.",
      },
      {
        title: "SpeakMoroccan",
        href: "https://speakmoroccan.com/en/",
        note: "Modern Moroccan Darija — the substrate of Moroccan JA.",
      },
      {
        title: "NaTakallam — 1-on-1 private tutors",
        href: "https://natakallam.com/learn-arabic-online-private-sessions/",
        note: "Native tutors in Yemeni, Iraqi, Egyptian, Levantine dialects.",
      },
      {
        title: "Yemen Institute for Arabic Language",
        href: "https://arabiconline.yialarabic.com/",
        note: "Yemeni Arabic online — closest to the vernacular of Yemenite Jews.",
      },
    ],
  },
  {
    id: "music",
    eyebrow: "Music & oral archives",
    title: "Listen",
    links: [
      {
        title: "A-WA — Habib Galbi",
        href: "https://www.youtube.com/watch?v=UIkgu6qThxk",
        note: "Three Yemenite-Israeli sisters, traditional Yemenite Judeo-Arabic poetry set to contemporary beats.",
        badge: "Music",
      },
      {
        title: "Moshe Habusha on Pizmonim.org",
        href: "https://www.pizmonim.org/hazzan.php?hazzan=MHabusha",
        note: "Iraqi-Israeli ḥazzan; piyyutim and JA liturgical recordings.",
        badge: "Music",
      },
      {
        title: "Robert and Molly Freedman Jewish Sound Archive (Penn)",
        href: "https://www.library.upenn.edu/collections/notable/freedman",
        note: "Major sound archive including Judeo-Arabic and Mizrahi/Sephardi music.",
      },
      {
        title: "Diarna — Geo-Museum of Mizrahi Life",
        href: "https://diarna.org",
        note: "The name itself is Judeo-Arabic: \"our homes.\" Photographs, oral histories, mapped to Google Earth.",
      },
    ],
  },
  {
    id: "podcasts",
    eyebrow: "Podcasts",
    title: "Audio you can subscribe to",
    intro:
      "There is no dedicated Judeo-Arabic podcast on Spotify yet. These are the closest things.",
    links: [
      {
        title: "Torah In Motion — Rabbis and Karaites (Goldstein)",
        href: "https://torahinmotion.org/podcasts/the-podcast-of-jewish-ideas/4-rabbis-and-karaites-dr-miriam-goldstein",
        note: "Miriam Goldstein on Karaite-Rabbanite relations.",
        badge: "Podcast",
      },
      {
        title: "Jewish Women's Archive — JIMENA: Mizrahi and Sephardi Voices",
        href: "https://jwa.org/podcasts/canwetalk/episode-63-jimena-mizrahi-and-sephardi-voices",
        note: "Episode 63 of Can We Talk?",
        badge: "Podcast",
      },
    ],
  },
];

function BadgeChip({ children }: { children: React.ReactNode }) {
  return (
    <span className="badge badge-muted ml-2 align-middle">{children}</span>
  );
}

export default function ResourcesPage() {
  return (
    <article className="max-w-3xl mx-auto px-6 py-16 pb-32">
      <header className="mb-12">
        <p className="label mb-3">
          Further afield
        </p>
        <h1 className="display text-4xl text-ink leading-tight">
          Where else to learn{" "}
          <span className="text-wine italic">Judeo-Arabic</span>
        </h1>
        <p className="mt-6 text-lg text-ink/75 leading-relaxed">
          This site is one slice. The list below is everything we&apos;d
          send a serious reader to next — lectures, dictionaries, oral
          histories, songs, and the closest thing to a course in spoken
          Judeo-Arabic. We&apos;ve tried these. Where a resource is
          uneven, we say so.
        </p>
      </header>

      <nav aria-label="On this page" className="mb-12 border-l-2 border-wine/30 pl-4">
        <div className="label mb-2">On this page</div>
        <ul className="text-[13px] text-ink/75 space-y-1">
          {SECTIONS.map((s) => (
            <li key={s.id}>
              <a href={`#${s.id}`} className="hover:text-wine">
                {s.title}
              </a>
            </li>
          ))}
        </ul>
      </nav>

      {SECTIONS.map((section) => (
        <section key={section.id} id={section.id} className="mb-14 scroll-mt-24">
          <p className="label label-accent mb-3">
            {section.eyebrow}
          </p>
          <h2 className="text-2xl text-ink mb-4 leading-snug">
            {section.title}
          </h2>
          {section.intro && (
            <p className="text-[15.5px] leading-relaxed text-ink/80 mb-6">
              {section.intro}
            </p>
          )}
          <ul className="space-y-5">
            {section.links.map((link) => (
              <li
                key={link.href}
                className="border-l border-ink/15 pl-4 hover:border-wine/60 transition-colors"
              >
                <a
                  href={link.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[15px] text-wine hover:underline"
                >
                  {link.title}
                </a>
                {link.badge && <BadgeChip>{link.badge}</BadgeChip>}
                {link.note && (
                  <p className="text-[13.5px] text-ink/70 leading-relaxed mt-1.5">
                    {link.note}
                  </p>
                )}
              </li>
            ))}
          </ul>
        </section>
      ))}

      <section className="rounded-md bg-wine/[0.05] border border-wine/30 p-6 text-[14px] leading-relaxed text-ink/85 mb-12">
        <p className="mb-2">
          Know a resource that belongs on this list? We&apos;d love to
          add it.
        </p>
        <p>
          Write:{" "}
          <a
            href="mailto:freedmaneli@gmail.com"
            className="text-wine hover:underline"
          >
            freedmaneli@gmail.com
          </a>
          .
        </p>
      </section>

      <nav className="mt-16 pt-8 border-t border-ink/10 flex flex-wrap items-center gap-x-6 gap-y-2 text-sm">
        <Link href="/" className="text-ink/70 hover:text-wine">
          ← Home
        </Link>
        <Link
          href="/what-is-judeo-arabic"
          className="text-ink/70 hover:text-wine"
        >
          What is Judeo-Arabic?
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

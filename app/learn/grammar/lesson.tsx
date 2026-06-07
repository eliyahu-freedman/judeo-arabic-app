"use client";

import Link from "next/link";
import { Quiz, type QuizGenerator, type QuizQuestion } from "@/components/Quiz";
import { useProgress } from "@/lib/progress";

export type GrammarExample = {
  ja?: string;
  ar?: string;
  translit?: string;
  en?: string;
  note?: string;
};

export type GrammarSection = {
  heading: string;
  body: string;
  examples?: GrammarExample[];
};

type Kind = "ja" | "ar" | "en";

export type GrammarQuizItem = {
  q: string;
  top?: { text: string; kind: Kind };
  choices: string[];
  choicesKind?: Kind;
  correctIdx: number;
  explanation: string;
};

export type GrammarData = {
  id: string;
  title: string;
  subtitle: string;
  intro: string;
  sections: GrammarSection[];
  quiz: GrammarQuizItem[];
};

const PROMPT_CLS: Record<Kind, { cls: string; dir: "rtl" | "ltr" }> = {
  ja: { cls: "font-hebrew text-5xl text-ink", dir: "rtl" },
  ar: { cls: "font-arabic text-5xl text-wine", dir: "rtl" },
  en: { cls: "text-2xl text-ink", dir: "ltr" },
};

const CHOICE_CLS: Record<Kind, { cls: string; dir: "rtl" | "ltr" }> = {
  ja: { cls: "font-hebrew text-2xl text-ink", dir: "rtl" },
  ar: { cls: "font-arabic text-2xl text-ink", dir: "rtl" },
  en: { cls: "text-[15px] text-ink", dir: "ltr" },
};

function toQuizQuestion(item: GrammarQuizItem): QuizQuestion {
  const choiceKind = item.choicesKind ?? "en";
  const choiceStyle = CHOICE_CLS[choiceKind];
  return {
    promptTop: item.top
      ? { text: item.top.text, ...PROMPT_CLS[item.top.kind] }
      : { text: item.q, cls: "text-xl text-ink", dir: "ltr" },
    promptInstruction: item.top ? item.q : "Choose the correct answer:",
    choices: item.choices.map((c) => ({ value: c, ...choiceStyle })),
    correctIdx: item.correctIdx,
    explanation: item.explanation,
  };
}

// Draw each quiz item once (shuffled), then reshuffle if exhausted.
function makeBankGenerator(items: GrammarQuizItem[]): QuizGenerator {
  let queue: GrammarQuizItem[] = [];
  return () => {
    if (queue.length === 0) {
      queue = [...items].sort(() => Math.random() - 0.5);
    }
    const item = queue.shift()!;
    return toQuizQuestion(item);
  };
}

export function GrammarLesson({
  data,
  backHref = "/learn",
  backLabel = "Learn",
  eyebrowSuffix = "grammar",
}: {
  data: GrammarData;
  backHref?: string;
  backLabel?: string;
  eyebrowSuffix?: string;
}) {
  const { markLessonDone, touchStreak } = useProgress();

  return (
    <div className="max-w-3xl mx-auto px-6 py-16 pb-28">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          <Link href={backHref} className="hover:text-wine">
            {backLabel}
          </Link>{" "}
          · {eyebrowSuffix}
        </p>
        <h1 className="text-4xl tracking-tight text-ink">{data.title}</h1>
        <p dir="rtl" className="font-hebrew text-2xl text-wine/80 mt-2">
          {data.subtitle}
        </p>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          {data.intro}
        </p>
      </header>

      <div className="space-y-10">
        {data.sections.map((s, i) => (
          <section key={i}>
            <h2 className="text-2xl text-ink mb-2">{s.heading}</h2>
            <p className="text-[15px] text-ink/75 leading-relaxed max-w-xl mb-5">
              {s.body}
            </p>
            {s.examples && s.examples.length > 0 && (
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {s.examples.map((e, j) => (
                  <li
                    key={j}
                    className="rounded-md bg-page border border-ink/10 p-4"
                  >
                    <div className="flex items-baseline gap-3 flex-wrap">
                      {e.ja && (
                        <span
                          dir="rtl"
                          className="font-hebrew text-2xl text-ink leading-none"
                        >
                          {e.ja}
                        </span>
                      )}
                      {e.ar && (
                        <span
                          dir="rtl"
                          className="font-arabic text-xl text-ink/60"
                        >
                          {e.ar}
                        </span>
                      )}
                      {e.translit && (
                        <span className="text-[13px] font-mono text-muted">
                          {e.translit}
                        </span>
                      )}
                    </div>
                    {e.en && (
                      <p className="mt-1.5 text-[15px] text-ink" dir="ltr">
                        {e.en}
                      </p>
                    )}
                    {e.note && (
                      <p className="mt-1 text-[12px] text-ink/65 italic leading-relaxed">
                        {e.note}
                      </p>
                    )}
                  </li>
                ))}
              </ul>
            )}
          </section>
        ))}
      </div>

      <section className="mt-14 rounded-md bg-parchment border border-ink/10 p-7">
        <h2 className="text-xs uppercase tracking-[0.25em] text-muted mb-1">
          Check yourself
        </h2>
        <p className="text-[15px] text-ink/75 mb-1">
          A few quick questions on what you just read.
        </p>
        <Quiz
          generate={makeBankGenerator(data.quiz)}
          total={data.quiz.length}
          onComplete={() => {
            markLessonDone(data.id);
            touchStreak();
          }}
        />
      </section>
    </div>
  );
}

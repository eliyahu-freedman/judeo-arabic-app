import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { GrammarLesson, type GrammarData } from "../lesson";
import { TrackVisit } from "@/components/TrackVisit";
import article from "@/data/grammar/article.json";
import suffixes from "@/data/grammar/suffixes.json";
import verbs from "@/data/grammar/verbs.json";

const TOPICS: Record<string, GrammarData> = {
  article: article as GrammarData,
  suffixes: suffixes as GrammarData,
  verbs: verbs as GrammarData,
};

export function generateStaticParams() {
  return Object.keys(TOPICS).map((topic) => ({ topic }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ topic: string }>;
}): Promise<Metadata> {
  const { topic } = await params;
  const data = TOPICS[topic];
  if (!data) return {};
  return {
    title: `${data.title} — Judeo-Arabic grammar`,
    description: data.intro,
    alternates: { canonical: `/learn/grammar/${topic}` },
  };
}

export default async function GrammarPage({
  params,
}: {
  params: Promise<{ topic: string }>;
}) {
  const { topic } = await params;
  const data = TOPICS[topic];
  if (!data) notFound();
  return (
    <>
      <TrackVisit
        label={data.title}
        href={`/learn/grammar/${topic}`}
      />
      <GrammarLesson data={data} />
    </>
  );
}

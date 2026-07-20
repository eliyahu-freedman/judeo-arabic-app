import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { TalmudReader, type DafData } from "@/components/TalmudReader";

const DAPIM = ["2a", "2b", "3a", "3b", "4a", "4b", "5a", "5b"];

export function generateStaticParams() {
  return DAPIM.map((daf) => ({ daf }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ daf: string }>;
}): Promise<Metadata> {
  const { daf } = await params;
  return {
    title: `Bava Metzia ${daf} — Talmud Bavli`,
    description: `Talmud Bavli, Tractate Bava Metzia, daf ${daf} — Hebrew text with English translation.`,
    alternates: { canonical: `/talmud/bava-metzia/${daf}` },
  };
}

export default async function TalmudBMDafPage({
  params,
}: {
  params: Promise<{ daf: string }>;
}) {
  const { daf } = await params;
  if (!DAPIM.includes(daf)) notFound();

  const mod = await import(`@/data/talmud-bava-metzia-${daf}.json`);
  const data = mod.default as unknown as DafData;

  return <TalmudReader data={data} />;
}

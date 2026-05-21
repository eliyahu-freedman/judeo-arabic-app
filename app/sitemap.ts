import type { MetadataRoute } from "next";
import { listChapters } from "@/lib/tafsirIndex";

const SITE_URL = "https://judeo-arabic-app.vercel.app";

const STATIC_ROUTES: { path: string; priority: number; changeFrequency: MetadataRoute.Sitemap[number]["changeFrequency"] }[] = [
  { path: "/", priority: 1.0, changeFrequency: "weekly" },
  { path: "/what-is-judeo-arabic", priority: 0.95, changeFrequency: "monthly" },
  { path: "/alphabet", priority: 0.9, changeFrequency: "monthly" },
  { path: "/tafsir", priority: 0.9, changeFrequency: "weekly" },
  { path: "/advanced", priority: 0.8, changeFrequency: "monthly" },
  { path: "/learn", priority: 0.8, changeFrequency: "monthly" },
  { path: "/learn/first-50", priority: 0.7, changeFrequency: "monthly" },
  { path: "/learn/cognates", priority: 0.7, changeFrequency: "monthly" },
  { path: "/learn/aramaic-cognates", priority: 0.7, changeFrequency: "monthly" },
  { path: "/learn/saadia-story", priority: 0.7, changeFrequency: "monthly" },
  { path: "/learn/saadia-preface", priority: 0.7, changeFrequency: "monthly" },
  { path: "/review", priority: 0.5, changeFrequency: "monthly" },
];

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const now = new Date();
  const staticEntries: MetadataRoute.Sitemap = STATIC_ROUTES.map((r) => ({
    url: `${SITE_URL}${r.path}`,
    lastModified: now,
    changeFrequency: r.changeFrequency,
    priority: r.priority,
  }));

  let chapterEntries: MetadataRoute.Sitemap = [];
  try {
    const chapters = await listChapters();
    chapterEntries = chapters.map((c) => ({
      url: `${SITE_URL}/tafsir/${c.bookSlug}/${c.chapter}`,
      lastModified: now,
      changeFrequency: "monthly",
      priority: 0.6,
    }));
  } catch {
    // listChapters reads from disk at build time; if it fails, fall back to static routes only.
  }

  return [...staticEntries, ...chapterEntries];
}

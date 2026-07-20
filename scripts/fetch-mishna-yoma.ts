import { writeFileSync } from "node:fs";
import { join } from "node:path";

const DATA_DIR = join(import.meta.dirname, "..", "data");

async function main() {
  const url =
    "https://www.sefaria.org/api/texts/Mishnah_Yoma.1?commentary=0&context=0&language=both";
  console.log("Fetching", url);
  const res = await fetch(url, {
    headers: { "User-Agent": "judeo-arabic-app/1.0" },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const raw = await res.json();

  const strip = (s: string) => s.replace(/<[^>]+>/g, "").trim();

  const he: string[] = Array.isArray(raw.he) ? raw.he : [];
  const text: string[] = Array.isArray(raw.text) ? raw.text : [];

  const mishnayot = he.map((heText: string, i: number) => ({
    mishnah: i + 1,
    he: strip(heText),
    en: strip(text[i] ?? ""),
  }));

  const output = {
    tractate: "Yoma",
    tractate_he: "יומא",
    chapter: 1,
    mishnayot,
  };

  const outPath = join(DATA_DIR, "mishna-yoma-1.json");
  writeFileSync(outPath, JSON.stringify(output, null, 2));
  console.log(`Wrote ${mishnayot.length} mishnayot → ${outPath}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});

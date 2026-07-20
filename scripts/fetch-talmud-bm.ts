import { writeFileSync } from "node:fs";
import { join } from "node:path";

const DATA_DIR = join(import.meta.dirname, "..", "data");
const DAPIM = ["2a", "2b", "3a", "3b", "4a", "4b", "5a", "5b"];

type Section = { type: "mishna" | "gemara"; he: string; en: string };

function stripHtml(s: string): string {
  return s.replace(/<[^>]+>/g, "").trim();
}

async function fetchDaf(daf: string): Promise<void> {
  const url = `https://www.sefaria.org/api/texts/Bava_Metzia.${daf}?commentary=0&context=0&language=both`;
  console.log("Fetching", url);
  const res = await fetch(url, {
    headers: { "User-Agent": "judeo-arabic-app/1.0" },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status} for daf ${daf}`);
  const raw = await res.json();

  const heArr: string[] = Array.isArray(raw.he) ? raw.he : [];
  const enArr: string[] = Array.isArray(raw.text) ? raw.text : [];

  // Track section type: before first "גמ׳" marker we're in mishna territory
  // (handles the first daf of a tractate where mishna has no prefix).
  // Once we see a "מתני׳" or "גמ׳" marker we update the running state.
  let currentType: "mishna" | "gemara" = "mishna";

  const sections: Section[] = heArr
    .map((he: string, i: number): Section => {
      // Strip HTML first so markers aren't hidden inside tags
      const stripped = stripHtml(he);
      const cleaned = stripped.trimStart();
      if (/^מתני[׳']/.test(cleaned)) {
        currentType = "mishna";
      } else if (/^גמ[׳']/.test(cleaned) || /^ג[ְּ]+מ/.test(cleaned)) {
        currentType = "gemara";
      }
      return { type: currentType, he: stripped, en: stripHtml(enArr[i] ?? "") };
    })
    .filter((s: Section) => s.he.length > 0);

  const output = {
    tractate: "Bava Metzia",
    tractate_he: "בבא מציעא",
    daf,
    sections,
  };

  const outPath = join(DATA_DIR, `talmud-bava-metzia-${daf}.json`);
  writeFileSync(outPath, JSON.stringify(output, null, 2));
  console.log(`  daf ${daf}: ${sections.length} sections → ${outPath}`);
}

async function main() {
  for (const daf of DAPIM) {
    await fetchDaf(daf);
    // Brief pause to be polite to Sefaria
    await new Promise((r) => setTimeout(r, 400));
  }
  console.log("Done.");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});

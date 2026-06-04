/**
 * Convert Arabic-script text to its Judaeo-Arabic Hebrew-letter form.
 *
 * Faithful TypeScript port of `ja_script.ar_to_ja` from the arabic-lexicon
 * toolkit (~/Tools/arabic-lexicon/ja_script.py). Used so the Advanced reader's
 * Arabic-script works (Qirqisani's al-Anwar, ed. Nemoy) can feed a tapped
 * Arabic token through the SAME Hebrew-keyed dictionary lookup as the
 * Judaeo-Arabic texts: convert → `lookup()` / `lookupWorkNote()`.
 *
 * Convention (Rabbanite-style geresh): ج→ג', خ→כ', ث→ת', ذ→ד', ض→צ', ظ→ט',
 * غ→ע', ع→ע. Final-letter and trailing-geresh differences are absorbed by the
 * lookup's `normalizeFinals` on both sides. The Python coverage script uses the
 * same `ar_to_ja`, so the runtime and the coverage gate stay in lock-step.
 */

const AR_TO_JA: Record<string, string> = {
  "ا": "א", "ب": "ב", "ت": "ת", "ث": "ת'", "ج": "ג'", "ح": "ח",
  "خ": "כ'", "د": "ד", "ذ": "ד'", "ر": "ר", "ز": "ז", "س": "ס",
  "ش": "ש", "ص": "צ", "ض": "צ'", "ط": "ט", "ظ": "ט'", "ع": "ע",
  "غ": "ע'", "ف": "פ", "ق": "ק", "ك": "כ", "ل": "ל", "م": "מ",
  "ن": "נ", "ه": "ה", "و": "ו", "ي": "י", "ى": "י", "ة": "ה",
  "ء": "א", "أ": "א", "إ": "א", "آ": "אא", "ؤ": "ו", "ئ": "י",
};

// Arabic harakat / tatweel / superscript alef — dropped before mapping.
const ARABIC_DIACRITICS = new Set([
  "ُ", "َ", "ّ", "ـ", "ٍ", "ٰ",
  "ٌ", "ِ", "ً", "ْ",
]);

export function arabicToJa(text: string): string {
  let out = "";
  for (const c of text) {
    if (ARABIC_DIACRITICS.has(c)) continue;
    out += AR_TO_JA[c] ?? c;
  }
  return out;
}

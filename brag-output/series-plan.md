# Judeo-Arabic App — Video Series Plan

10 videos. Each self-contained. Each shareable on its own.

---

## Music strategy

None of the bundled tracks are right for this app. Source 2–3 Arabic-flavored tracks before composing:

**Track A — oud solo, contemplative** (for Rambam, Bahya, Saadia's Preface)
- Character: single oud, slow, modal, no percussion
- Source: Freemusicarchive.org → search "oud" → filter CC0 or CC-BY
- Target: something in Maqam Rast or Hijaz, 60–90 BPM

**Track B — maqam ensemble, warm** (for Tafsir, Alphabet, Kuzari, Story)
- Character: oud + qanun or ney, light hand drum, moderate tempo
- Source: Freemusicarchive.org or Pixabay → search "Arabic classical"
- Target: steady, not touristic, not belly-dance

**Track C — silence + single oud sting** (for Moreh Nevukhim reveal, Cognates)
- Character: silence through the main sequence, one resonant oud note on the name reveal
- Can be SFX rather than a music bed

---

## Narration strategy

**Use ElevenLabs for all narrated videos.** Kokoro-82M (Hyperframes built-in) is usable for drafts
but not for final output — ElevenLabs will be noticeably better.

**Strong recommendation: clone your own voice.**
ElevenLabs Professional Voice Cloning takes ~1 minute of clean audio.
For a personal-brand series about your own research and your own app, your voice is the right voice.
If not, their "Liam" or "Daniel" voices work well for scholarly register.

**Workflow per narrated video:**
1. Write the narration script (≤120 words for a 60s video)
2. Generate WAV via ElevenLabs → save to `assets/narration/`
3. Time the visual beats to the narration in GSAP (narration is the primary track)
4. Music bed at low volume underneath (0.10–0.14)
5. SFX on UI interaction moments only

**Narration pace target:** ~130 words/minute, deliberate and warm.
At 60s = ~130 words. At 45s = ~98 words. At 90s = ~195 words.

---

## The 10 Videos

---

### Video 1 — The Overview ✅ DONE
**File:** `brag-output/brag.mp4` (27s)
**Narration:** None — text-only, music bed
**Use:** Launch post, pinned tweet, bio link

---

### Video 2 — The Tafsir Reader
**Duration:** 45s
**Narration:** None — let the text breathe; SFX-driven
**Music:** Track B (warm maqam ensemble)
**Hook:** Saadia's Genesis 1:1 fills the screen. No explanation. Then the cursor appears and starts working through it.
**Arc:**
- 0–5s: Wine bg, full verse in large Hebrew script. Silence, then music fades in.
- 5–12s: Reader opens. Hebrew source above, Tafsir below. Three words tap in sequence (not two).
- 12–25s: English gloss fades in. Parallel panel shows. Hold.
- 25–38s: New verse loads (Genesis 1:2 or a memorable verse from later in Torah). Word tap, different entry.
- 38–45s: Pull back to full reader view. "Saadia Gaon · Tafsir al-Torah · Free" fades in.
**Super:** Show that you can navigate between verses, not just tap one word.

---

### Video 3 — The Alphabet
**Duration:** 60s
**Narration:** Yes (ElevenLabs) — this is a teaching video, narration is essential
**Music:** Track B low under narration
**Hook:** "The Jewish classics were written in Arabic. But not in Arabic letters."
**Script (draft, ~110 words):**
> The Jewish classics were written in Arabic. But not in Arabic letters.
> Judeo-Arabic uses the Hebrew script — the one you already know.
> A handful of diacritics mark the sounds that differ.
> Kaf becomes khaf. Gimel becomes jeem. Tet becomes tha.
> That's it. Five marks. The rest is already yours.
> [beat]
> Once you have the script, you can open Saadia's Torah translation.
> You can read the Guide to the Perplexed in Maimonides' own hand.
> You can sit with Bahya and Halevi and Qirqisani
> in the language they actually thought in.
> The script takes an afternoon. The library lasts a lifetime.
> Judeo-Arabic. Free.
**Arc:** Letter cards animate in as narration describes them. Rule: כ → כ׳, ג → ג׳, ח׳, ט׳, ת׳. Then the library opens.

---

### Video 4 — Moreh Nevukhim (Guide to the Perplexed)
**Duration:** 60s
**Narration:** Yes (ElevenLabs)
**Music:** Track A (oud solo, slow) — fades out before name reveal; oud sting on "Maimonides"
**Hook:** "You've read the Guide to the Perplexed. But you've never read it."
**Script (draft, ~115 words):**
> Maimonides wrote the Guide to the Perplexed in Arabic.
> Not in Hebrew. Not in Aramaic. In Arabic — the intellectual language of his world.
> It was translated into Hebrew within his lifetime. Then into Latin. Then into every European tongue.
> And somewhere in all that translation, something got lost.
> Not the argument. The voice.
> [beat]
> Maimonides was precise, compressed, and ironic in ways that don't survive the journey.
> To read him in Arabic is to sit across the table from a different mind than the one most people have met.
> [beat]
> The Guide to the Perplexed. In the original Judeo-Arabic.
> Free.
**Arc:** Dark bg. Arabic title (דלאלה אלחאירין) materializes. Reader opens to opening passage. Cursor moves through text. Name "Maimonides" appears with oud sting.

---

### Video 5 — Hovot HaLevavot (Duties of the Heart)
**Duration:** 60s
**Narration:** Yes (ElevenLabs)
**Music:** Track A (oud solo) — softer than Rambam video, warmer
**Hook:** "Bahya wrote the Duties of the Heart in Arabic. Most people have read a shadow of it."
**Script (draft, ~105 words):**
> In the eleventh century, a Spanish rabbi named Bahya ibn Paquda set out to write a book about the inner life.
> Not halacha. Not philosophy. The inner life — the duties no one could see or enforce.
> He wrote it in Arabic, because Arabic was the only language with the vocabulary he needed.
> The Hebrew translation came a generation later. It's been that translation, ever since.
> [beat]
> But Bahya's Arabic is something else.
> Warmer than the translation suggests. More intimate.
> More honest about what it costs to live a contemplative life.
> [beat]
> Hovot HaLevavot. In Bahya's own words.
> Free.
**Arc:** Parchment bg. JA title appears. Reader opens. A passage from one of the gates fades in. Slow holds throughout.

---

### Video 6 — The Kuzari
**Duration:** 45s
**Narration:** Yes (ElevenLabs)
**Music:** Track B (maqam ensemble) — slightly more energy than the contemplative videos
**Hook:** "Halevi wrote the Kuzari as a dialogue. In Arabic. The one you know is a translation of a translation."
**Script (draft, ~85 words):**
> The Kuzari is a philosophical dialogue — a rabbi defending Judaism to the king of the Khazars.
> Halevi wrote it in Arabic.
> The Hebrew version most people know passed through two translations before it reached you.
> [beat]
> In the original, the rabbi is sharper. The argument moves differently.
> The irony lands harder.
> [beat]
> We've opened the Kuzari in Judeo-Arabic for the first time in a free digital reader.
> Any Hebrew reader can start today.
**Arc:** Quote from the Kuzari (JA) appears. Reader opens showing the dialogue format. Pull back to library view.

---

### Video 7 — The Lexicon
**Duration:** 45s
**Narration:** None — demo video, SFX-driven
**Music:** Track B low
**Hook:** The search bar. Type a root. Watch the results cascade.
**Arc:**
- 0–5s: Lexicon page loads (recreated). Search bar pulses.
- 5–15s: Type כ׳לק — results populate: entry card with root, POS, glosses, attestations across 6 authors.
- 15–28s: Clear. Type "create" in English — same entry finds it. Show cross-lingual search.
- 28–38s: Click an attestation — jumps to the Tafsir passage in context.
- 38–45s: "8,700 entries. Lane · Blau. Every root in the classical library." fades in.
**Super:** Show that the lexicon is a standalone research tool, not just tap-to-define.

---

### Video 8 — Saadia's Story
**Duration:** 75s
**Narration:** Yes (ElevenLabs) — this is the historical video, narration carries it
**Music:** Track B → fades to Track A oud under the name reveal
**Hook:** "In 928 CE, one rabbi decided that Jews needed to read their Torah in Arabic. He was right."
**Script (draft, ~155 words):**
> In 928 CE, a rabbi named Saadia sat down and translated the entire Torah into Arabic.
> He wasn't translating for non-Jews.
> He was translating for his own community.
> Arabic was the language they lived in, thought in, prayed in.
> And Saadia believed that if Jews couldn't read the Torah in that language, something essential would be lost.
> [beat]
> He called it the Tafsir — the explanation.
> It was so well done that it's still in use today,
> among the small number of Jewish communities that kept their Arabic.
> [beat]
> Saadia didn't stop there. He wrote grammars, legal codes, biblical commentaries, philosophy.
> Two dozen works across every domain of Jewish learning.
> All in Arabic. All in Hebrew letters.
> [beat]
> This is what those letters look like.
> And this is what it feels like to finally read them.
> Saadia Gaon. Free.
**Arc:** Wine bg, manuscript feel throughout. Maps or historical text as atmospheric visuals. Tafsir reader reveal at the end.

---

### Video 9 — Cognates (You Already Know This)
**Duration:** 45s
**Narration:** Yes (ElevenLabs) — conversational, light tone
**Music:** Track B, slightly more energy
**Hook:** "If you know Hebrew, you already know hundreds of Arabic words. You just don't know you know them."
**Script (draft, ~90 words):**
> If you know Hebrew, you already know more Arabic than you think.
> [beat]
> ראש. In Arabic: raas. Head.
> בית. In Arabic: bayt. House.
> שמע. In Arabic: sami'a. To hear.
> [beat]
> The two languages share a root system that goes back three thousand years.
> And Judeo-Arabic, written in Hebrew letters, puts them side by side.
> [beat]
> We built a cognates guide that shows you exactly where the overlap is
> — and exactly where it breaks down.
> You already know more than you think.
> Start here.
**Arc:** Word pairs flash on screen as narration names them. Then cognates page opens showing the full list. Fast pacing relative to the other videos.

---

### Video 10 — Saadia's Preface
**Duration:** 60s
**Narration:** Yes (ElevenLabs) — reads a passage from the preface itself
**Music:** Track A (oud solo), very spare
**Hook:** "Saadia wrote an introduction to his Torah translation. Most of it has never been published in English — until now."
**Script (draft, ~110 words):**
> Before the first verse of Genesis, Saadia Gaon wrote a preface.
> He explained why he was translating the Torah.
> Who it was for. What he hoped it would do.
> [beat — a passage from the preface fades in on screen as narration reads it]
> "I saw that many of the people of our nation had fallen into error
> in what they understood from the Torah —
> and I could not remain silent."
> [beat]
> That preface has been read, in Arabic, by almost no one for a thousand years.
> We've put it online, with an English translation alongside it,
> for the first time.
> [beat]
> Saadia's Preface. In his own words.
**Arc:** Parchment bg throughout. The preface text appears on screen line by line as narration reads it. Very slow reveals. Ends on attribution and URL.

---

## Production order

Recommended sequence based on effort and impact:

1. **Video 8 — Saadia's Story** (highest narrative value, sets up everything else)
2. **Video 3 — The Alphabet** (top of funnel, most shareable for new audiences)
3. **Video 4 — Moreh Nevukhim** (highest prestige, LinkedIn / academic audiences)
4. **Video 2 — The Tafsir** (deepens the launch video)
5. **Video 9 — Cognates** (widest appeal, lightest lift)
6. **Video 5 — Hovot HaLevavot**
7. **Video 6 — The Kuzari**
8. **Video 7 — The Lexicon**
9. **Video 10 — Saadia's Preface**
10. **Video 11 — (future)** Yefet ben Eli, Qirqisani Anwar, etc.

---

## Next steps

- [ ] Source Arabic music tracks (Track A + B from Freemusicarchive)
- [ ] Record or clone voice in ElevenLabs
- [ ] Run `/brag` for Video 8 (Saadia's Story) as the first narrated video
- [ ] Finalize narration scripts for each video before composing

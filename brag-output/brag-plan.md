# Brag Plan: Judeo-Arabic — A Digital Reader & Lexicon

## What is this app?

A free, tap-to-define reader for medieval Judeo-Arabic — Saadia Gaon's Tafsir on the whole Torah plus Bahya, Rambam, Halevi, and Qirqisani in the original Hebrew-script Arabic — built for anyone who knows the Hebrew alphabet.

## The angle

Saadia Gaon translated the Torah into Arabic in 928 CE. It has been sitting, inaccessible, for a thousand years. This app makes it readable. Not a translation. The original. Stage I teaches you the script. Stage II opens the Tafsir verse by verse. Tap any word — the lexicon opens instantly with root, part of speech, and classical glosses from Lane and Blau. The video treats this exactly as seriously as it deserves.

## Hook (first 2–3 seconds)

Full-screen deep wine. The Judeo-Arabic text of Genesis 1:1 — **אול מא כ׳לק אללה** — materializes slowly in parchment cream, as though appearing on a manuscript page. Ghost line beneath it: **אלסמאואת ואלארץ׳**. The label surfaces last, in tiny spaced caps: SAADIA GAON · TAFSIR AL-TORAH · GENESIS 1:1. Nothing else. No narration. The text is the hook.

## Key moments (the middle)

- The hero headline materializes on parchment: "The medieval Judeo-Arabic library, read in the original." — wine accent on "Judeo-Arabic."
- The Tafsir reader: a verse card shows Hebrew at top and the Judeo-Arabic below. A cursor taps a word. The lexicon panel slides open — root, POS, English gloss, Lane reference. The word is alive.
- A second tap opens a different entry. The apparatus reveals itself, quietly.

## Outro / punchline

Scale appears one line at a time: 81,000 words indexed · 8,700 lexicon entries · Saadia · Bahya · Rambam · Halevi. Then the app name, unhurried: **Judeo-Arabic**. Beneath it, the URL. A single deep bell. Fade.

## User flow worth showing

Entry: the manuscript showcase (wine section) — see the Judeo-Arabic text as it actually looks, monumental and strange.
Key action: the Tafsir reader — tap a word in the Judeo-Arabic verse.
Result: the lexicon panel opens — root, part of speech, English gloss, classical source. A thousand-year-old word, defined instantly.

## Tone

- Preset: `polished`
- Creative direction: "ancient manuscript meets modern reader — understated scholarly prestige, slow reveal"
- Interpretation: Slow fades, long holds, generous white space on parchment. No hype. No motion for motion's sake. The text earns its gravity — every reveal gives it room. Typography is serifed and warm. Copy is minimal. The product's audacity is the punchline, not a joke.

## Format: landscape — 1920×1080
## Duration: 20 seconds

## Visual identity (from the project)

- Background (primary): `#faf8f3` (parchment)
- Background (manuscript scene): `#722f37` (wine)
- Accent: `#722f37` (wine)
- Text: `#1c1a17` (ink)
- Muted: `#6b6357`
- Display font: Lora (serif) — for headlines and body copy
- Hebrew/JA script font: Noto Serif Hebrew — for all Judeo-Arabic text
- Strongest visual element: the wine-on-parchment manuscript showcase with giant Judeo-Arabic letterforms

## Share copy (draft)

Saadia Gaon translated the Torah into Arabic in 928 CE. This is what it looks like — and what it feels like when you can finally read it.

## Audio direction

- Role: warm, barely-there scholarly bed — like paper in a quiet library
- Music: `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3` (steady and clean, polished/cinematic)
- Music treatment: Fade in gently over scene 1 (starting ~1.5s in at low volume); hold at 0.22 throughout; begin a slow fade to 0.08 at ~17s; let the final bell SFX ring cleanly over near-silence
- Music cue guidance: Bundled preset available at `~/.claude/skills/brag/assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json`. Strong cues: 8.74s (intensity 0.99) — lock the Tafsir reader entrance; 17.47s (intensity 0.99) — lock the stats reveal; 22.93s (intensity 1.00) — lock the logo/name reveal. Beat grid available for optional sequential stat entrances.
- Audio-reactive treatment: subtle; use music RMS/bass to make the wine manuscript background glow very slightly, and the lexicon panel gain a hair of warm presence on bass hits. No waveform or equalizer visuals.
- SFX posture: sparse, 3–4 total, professional restraint
- Audio-coupled moments:
  - Scene 1 (manuscript materializes): silence breaking into music, no SFX — let the text breathe
  - Scene 3 (cursor tap): `ui/mouseclick1.ogg` or `interface/click_001.ogg` for each word tap — soft, precise
  - Scene 3 (lexicon panel open): `interface/drop_001.ogg` as the panel slides in — gentle landing
  - Scene 4 (name reveal): `impact/impactBell_heavy_000.ogg` — one deep resonant bell, full weight
- Restraint rule: no SFX in scenes 1–2; no stacking; the bell plays once and is not repeated

---

## Storyboard

### Scene 1 — Manuscript — 4s

Full-screen wine red (#722f37). Two lines of Judeo-Arabic appear slowly — not typed, but materializing, like ink surfacing on vellum. Primary: **אול מא כ׳לק אללה** (Noto Serif Hebrew, large, parchment/cream #faf8f3). Ghost line below: **אלסמאואת ואלארץ׳** (same font, parchment/40% opacity). A thin horizontal rule fades in beneath. Then the attribution: SAADIA GAON · TAFSIR AL-TORAH · GENESIS 1:1 — spaced caps, tiny, parchment/40%.
Sequential/interaction: none — a single layered reveal in sequence (primary text first, ghost second, rule third, attribution last), each 0.6–0.8s after the previous. Hold the full composition for 1.5s.
Audio intent: silence breaking into the faintest warm music bed arriving at ~1.5s; the absence of sound makes the text monumental
Audio-coupled idea: none — let silence and the slow reveal carry
Music: barely perceptible warm bed, fading in at 1.5s
Transition mood: very slow crossfade → Scene 2

### Scene 2 — Claim — 4s

Parchment background (#faf8f3). A small label eyebrow fades in first: A DIGITAL READER & LEXICON (spaced caps, wine, tiny). Then the headline materializes: "The medieval Judeo-Arabic library, read in the original." — Lora display, large, ink (#1c1a17), with "Judeo-Arabic" in wine italic. Below, after a beat: a stats line in small spaced muted type: 81,000 words · 8,700 entries · 6 classical works. Hold. Breathe.
Sequential/interaction: yes — eyebrow appears, then headline fades in over 0.5s, then stats line appears; each ~0.8s apart; hold the full card for 2s
Audio intent: warm music bed, steady; the stats line arrival is the audio-coupled moment
Audio-coupled idea: `interface/drop_001.ogg` softly under the stats-line arrival
Music: steady vol-12 at 0.22
Transition mood: soft crossfade → Scene 3

### Scene 3 — The Reader — 8s

Parchment background. A recreated Tafsir verse card appears — white (#ffffff) card with shadow, centered. Top portion: biblical Hebrew in Noto Serif Hebrew, right-aligned. Below: the Judeo-Arabic verse, larger, right-aligned in Noto Serif Hebrew. A cursor enters and taps the word **אללה** — it highlights in wine. The lexicon panel slides in from the right (or below): label LEXICON ENTRY, then root **א-ל-ה**, POS: proper noun, gloss: "God" (English), Lane citation. After 2s, cursor taps a second word — **כ׳לק** (created) — panel updates with root **خ-ل-ق**, gloss: "to create." After 2s, panel fades. The card holds.
Sequential/interaction: yes — simulated cursor taps two words in sequence; each tap triggers a lexicon panel slide-in; cursor is a visible pointer; each panel open is distinct
Audio intent: the interaction sounds make the product feel responsive and alive
Audio-coupled idea: `ui/mouseclick1.ogg` (or `interface/click_001.ogg`) on each cursor tap; `interface/drop_001.ogg` as each panel arrives
Music: steady warm bed
Transition mood: soft crossfade → Scene 4

**Beat-lock note:** target the entrance of the Tafsir card near the 8.74s strong cue (±0.15s).

### Scene 4 — Scale & Name — 4s

Dark parchment or very deep ink background for contrast. Three lines appear one by one in cream/parchment text:
→ 81,000 words indexed
→ 8,700 lexicon entries
→ Saadia · Bahya · Rambam · Halevi
Then, after a beat: the name **Judeo-Arabic** — large, Lora serif, cream — fades in at full weight. Below it: judeo-arabic-app.vercel.app in tiny spaced caps. At the name reveal: `impactBell_heavy_000.ogg`. Music fades to near-silence.
Sequential/interaction: yes — three stat lines arrive one by one, each ~0.5–0.6s apart, then the name arrives after a ~0.5s pause; hold the full card for 1.5s
Audio intent: arrival of each stat line is understated; the name reveal is the payoff — the bell lands there and rings into silence
Audio-coupled idea: optional very soft `interface/drop_001.ogg` on each stat line arrival; `impact/impactBell_heavy_000.ogg` on the name, full volume (0.75)
Music: fading from 0.22 to 0.06 starting at ~17s; nearly inaudible under the bell

**Beat-lock notes:** target stat line sequence near beats at 17.47s–18.56s strong cues (±0.15s); target name reveal near 22.93s strong cue (±0.15s).

---

**Total duration:** 4 + 4 + 8 + 4 = 20 seconds ✓

**Music mood for this video:** warm, scholarly, steady — a soft presence beneath the text, not above it

**Audio summary:** Music enters imperceptibly over the manuscript reveal, holds quietly through the reader, and fades to near-silence as the bell rings on the name — leaving the product's own weight to close the video.

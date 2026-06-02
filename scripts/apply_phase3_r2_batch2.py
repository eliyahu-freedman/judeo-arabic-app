"""
Phase 3 R2 Batch 2 — cross-book TWIST scan, systematic sweep of the remaining
~25 TWIST entries beyond the 11 priority-cluster lemmas covered in B1.

Mirrors scripts/apply_phase3_r2_batch1.py exactly. Promote-in-place only —
no new entries, no tier changes.

Scan results
------------
Source: scripts/scan_phase3_r2.py against all 36 TWIST entries (B1 lemmas
re-scanned post-B1; their already-attested verses correctly filtered out).
Hits triaged against -alignment.json files and tafsir source files. The
homograph rate at TWIST tier is ~50% as observed in B1; B2 maintains this:
of the 13 entries with cross-book hits, 4 ship + 9 are filtered as register-
homographs or mechanism-mismatches.

Promote-in-place — 4 TWIST entries, 11 new verse attestations + 1 mechanism
correction:

  - גוהר      +Shemot 24:12, 31:18, 34:1, 34:4 (Tablets register only;
              skip jeweler-craft homographs at 28:11, 28:17, 31:5, 35:33,
              39:10 — those use the bare classical jewel-sense for אֶבֶן
              not the dual-register move on לֻחֹת)
              (was 5 verses Devarim-only → 9 verses across 2 books;
              2-BOOK GRADUATION — Saadia's Tablets-as-jewel-and-essence
              vocabulary now spans Sinai-Tablets-Shemot + reflective-
              Devarim recap)

  - ג'מר      +Bereshit 8:2 (flood end) + Bereshit 49:25 (Jacob blesses
              Joseph, תהום-blessing) + Shemot 15:5 (Song-of-Sea: deep
              covers them) + Shemot 15:8 (deeps frozen in heart of sea)
              + Devarim 33:13 (Moses blesses Joseph, parallel תהום-
              blessing)
              (was 1 verse Bereshit-only → 6 verses across 3 books;
              3-BOOK GRADUATION — the third 3-book TWIST in the corpus.
              All extensions are Heb תהום → Ar غمر renderings, confirming
              that Saadia's cosmological-abyss vocabulary is systemic
              across creation/flood + Song-of-Sea + patriarchal-blessing
              registers)

  - חגב       +Devarim 31:18 (Heb הַסְתֵּר אַסְתִּיר פָּנַי → Saadia: anti-
              anthropomorphic divine concealment — حجب for divine face-
              hiding, mirroring Gen 7:16 sealing-of-ark)
              (was 1 verse Bereshit-only → 2 verses across 2 books;
              2-BOOK GRADUATION)

  - אתון      +Bereshit 15:7 (Heb אוּר כַּשְׂדִים, the within-book third
              instance of Saadia's midrashic furnace-identification —
              the same Aramaic-loan אַתּוּן used at Gen 11:28, 11:31)
              (was 2 verses → 3 verses, Bereshit-only; within-book
              syncing to the obvious third instance)

Mechanism correction — 1 entry (NO verses[] extension):

  - אורד      EMPIRICAL CORRECTION: B1's mechanism rewrite preserved the
              entry's original prose claim that "the same template appears
              throughout the Tafsir wherever the Hebrew has YHWH coming
              down — Sodom, Sinai, the Tent of Meeting." The B2 scan
              empirically disproves the Sinai/Tent part: at Ex 19:11,
              19:18, 19:20, 34:5 + Num 11:25, 12:5, Saadia consistently
              uses Form V تجلَّى ('manifest in cloud/fire'), NOT the Form
              IV ورد ('dispatch a directed command') that the TWIST
              centers on. The dispatch-frame is bounded to Babel (Gen
              11:5, 11:7) + Sodom (Gen 18:21, shipped in B1) — three
              verses, all Bereshit. The Sinai/Tent verses belong to a
              SEPARATE (potentially new TWIST) for the manifestation-
              vocabulary تجلَّى, deferred to Phase 3 R3.
              Mechanism rewrite scopes the dispatch-frame correctly and
              flags the تجلَّى cluster as a candidate for future work.
              No verses[] change (still 3 verses, Bereshit-only).

Deferred — homograph filters + mechanism-mismatches
---------------------------------------------------
  - אשראף (Ex 16:22, 34:31; Num 1:16, 3:32, 7:2, 7:10, 7:84, 10:4, 16:2,
    31:13) — register-homograph: the TWIST is specifically the ANTI-
    MYTHOLOGICAL reading of בְּנֵי הָאֱלֹהִים at Gen 6:2-4 (refusing the
    angelic-being reading). The 10 cross-book hits are all ROUTINE
    chieftain-vocabulary usage of أشراف for various biblical leader-
    titles (נשיאים, ראשים, זקנים). The lexical-systemic basis is real
    (Saadia HAS this chieftain-vocab available routinely) but adding
    the 10 verses to verses[] would suggest the anti-mythological claim
    extends to them, which it doesn't.
  - מלאיכה Bereshit 19:15 — mechanism-mismatch: the TWIST is rerouting
    Heb אֱלֹהִים (divine beings) → Ar ملائكة (angels) to refuse creaturely
    apotheosis. At Gen 19:15 the Heb is הַמַּלְאָכִים (literal angels-
    sent-to-Lot), and the Ar translation is a direct cognate (Heb מלאך
    ~ Ar ملك). The cognate translation is not the anti-anthropomorphic
    move.
  - בדן Shemot 30:32 — register-homograph: the TWIST is the lexical
    choice of بدن over جلد at Gen 3:21 (animal-skin garments). At Ex
    30:32 Saadia uses بدن for Heb בְּשַׂר אָדָם (human flesh) in the
    anointing-oil prohibition — different Heb counterpart, different
    context. The بدن usage is consistent across the Pentateuch but the
    specific Gen 3:21 mechanism (avoiding جلد to preserve it for רָקִיעַ)
    doesn't extend.
  - קרבאן (72 hits across all 5 books) — register-homograph at scale.
    The TWIST is the anti-anthropomorphic DOUBLE substitution at Gen
    8:21 (verb shifted from יָּרַח 'smelled' to قَبِلَ 'accepted'; object
    shifted from רֵיחַ הַנִּיחֹחַ 'soothing aroma' to אלקרבאן אלמרצ'י
    'pleasing offering'). The 72 cross-book hits are routine offering-
    vocabulary usage of قربان for various biblical sacrifice-terms
    (קרבן, מנחה, עלה, etc.) — most are not anti-anthropomorphic moves.
  - גוהר Shemot 28:11, 28:17, 31:5, 35:33, 39:10 — jeweler-craft
    register-homograph. The TWIST is the DUAL-REGISTER move where גוהר
    operates as both 'jewel' AND 'substance/essence' for Heb לֻחֹת. At
    the breastplate-craft verses Saadia uses גוהר for Heb אֶבֶן in the
    bare jewel-sense (one register only); adding these would dilute
    the dual-register TWIST claim.

(B1-already-deferred lemmas are not re-listed here: שא, גלד, חאכם judicial
cluster, אורד noun-surfaces, אלממתעה ↔ ממתעה duplicate-collision.)

No-hit lemmas (already-saturated single-book entries with no cross-book
attestations of any kind):
  - גאמרה (Gen 1:2 only; the related ג'מר entry covers the cross-book
    reach of the same root)
  - מסתבחרה, ריאח, תהב, אטג'אני, קיאדך, כ'טאך, אכ'תיאר, טאעה, תופי,
    ינג'מד, שמשאר, קרדא, יסיידונך, ד'רקובה, משוובה
  - 15 entries total — all are anchored at unique-context Bereshit
    creation/flood/Babel/Patriarchal verses with no cross-book
    attestations in the tafsir corpus.

Apply pattern
-------------
Mirrors scripts/apply_phase3_r2_batch1.py:
  PROMOTE_IN_PLACE list of 5 entries (4 with extend_verses + 1 mechanism-
  only correction for אורד).
  _patch_promote_in_place() iterates the list; for items with no
  extend_verses but a mechanism_rewrite, the mechanism is still updated
  (handled by adjusting the helper to apply rewrites whenever they're
  provided, even with no added verses).
Fresh "phase3_r2/batch2" namespace in data/_blau_saadia_deferred.json.
"""

import json
import pathlib
import sys
from collections import Counter


# ============================================================================
# CROSS-BOOK PROMOTE-IN-PLACE — extensions to existing TWIST entries
# ============================================================================

PROMOTE_IN_PLACE = [

    # ---- גוהר + Shemot Tablets-verses: 2-book graduation -------------------
    {
        "lemma_ja": "גוהר",
        "extend_verses": [
            {"book": "Shemot", "ch": 24, "v": 12},
            {"book": "Shemot", "ch": 31, "v": 18},
            {"book": "Shemot", "ch": 34, "v": 1},
            {"book": "Shemot", "ch": 34, "v": 4},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Midrashic identification + philosophical vocabulary — now confirmed across the FULL "
            "Pentateuchal Tablets-tradition arc (Shemot + Devarim, 9 verses). Saadia uses a "
            "single Arabic term جوهر that operates on two registers — JEWEL (the rabbinic "
            "tradition of Tablets-of-sapphire, b. Sotah 17a; Tanḥuma Ki Tissa 26) and SUBSTANCE/"
            "ESSENCE (the philosophical claim of Tablets-of-divine-essence, drawing on the kalām/"
            "falsafa technical sense of jawhar as 'substance' or 'essential being'). The dual-"
            "register move renders Heb לֻחֹת so the reader hears BOTH the rabbinic tradition and "
            "the philosophical claim simultaneously. The cross-book arc now spans (1) the Sinai "
            "Tablets-promise at Ex 24:12 ('אֶת-לֻחֹת הָאֶבֶן' → 'לוחי אלגוהר' — the FIRST mention of "
            "the Tablets in scripture, marked from the outset with the dual-register vocabulary); "
            "(2) the giving-of-Tablets pillar at Ex 31:18 ('לֻחֹת אֶבֶן כְּתֻבִים בְּאֶצְבַּע אֱלֹהִים' = "
            "'לוחי גוהר מכתובין בקדרה' אללה' — the divine-finger written register, with the "
            "anthropomorphic 'finger' simultaneously routed through Saadia's standard בקדרה' "
            "anti-anthropomorphic 'by-power-of' substitution); (3) the second-Tablets re-issue at "
            "Ex 34:1 ('פְּסָל-לְךָ שְׁנֵי-לֻחֹת אֲבָנִים' = 'אנחת לוחי גוהר'); (4) Moses descending Sinai "
            "with the second Tablets at Ex 34:4 ('וַיִּקַּח בְּיָדוֹ שְׁנֵי לֻחֹת אֲבָנִים' = 'ואכ'ד' מעה "
            "לוחי אלגוהר'); AND the Devarim retrospective cluster (Deut 5:19, 9:9, 9:10, 10:1, "
            "10:3 — Moses's reflective recount of the Tablets-events). The cross-Pentateuchal "
            "consistency demonstrates that the dual-register Tablets-vocabulary is Saadia's "
            "INVARIANT lexical signature for the Tablets across both the narrative (Shemot) and "
            "the homiletic (Devarim) registers — never deviating into a single-register sense, "
            "even when the surrounding context might invite it. Pedagogically distinctive because "
            "the entry now demonstrates that Saadia treats the Tablets-as-jewel-and-essence as a "
            "fixed terminus-technicus across the entire Sinai-vocabulary system. Distinct from "
            "the breastplate-jeweler usage at Ex 28:11, 28:17, 31:5, 35:33, 39:10, where Saadia "
            "uses جوهر for Heb אֶבֶן in the bare classical jewel-sense (one register only — the "
            "literal jeweler's-craft register, not the dual Tablets-register move) — see the "
            "deferred bucket for those cases."
        ),
        "blau_dict_sense_rewrite": (
            "Blau (Dict. of Medieval Judaeo-Arabic Texts, s.v. גוהר / جوهر) cites the dual-"
            "register sense — both 'jewel/precious stone' (the rabbinic-poetic register) and "
            "'substance/essence' (the falsafa technical sense, Saadia's own Emunot ve-Deot uses "
            "the same term for the philosophical substance-category). The R2 cross-book scan "
            "confirms Saadia deploys this dual-register Arabic term invariantly for biblical "
            "לֻחֹת across BOTH the Shemot Sinai-narrative attestations (Ex 24:12, 31:18, 34:1, "
            "34:4) AND the Devarim retrospective attestations (Deut 5:19, 9:9, 9:10, 10:1, "
            "10:3), making the Tablets-vocabulary a 2-book program with 9 verse attestations."
        ),
    },

    # ---- ג'מר + Bereshit-internal + Shemot + Devarim: 3-book graduation ----
    {
        "lemma_ja": "ג'מר",
        "extend_verses": [
            {"book": "Bereshit", "ch": 8, "v": 2},
            {"book": "Bereshit", "ch": 49, "v": 25},
            {"book": "Shemot", "ch": 15, "v": 5},
            {"book": "Shemot", "ch": 15, "v": 8},
            {"book": "Devarim", "ch": 33, "v": 13},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Lexical-cosmological linkage, now confirmed as a programmatic 3-BOOK invariance for "
            "Heb תְהוֹם → Ar غمر across the entire Pentateuchal cosmological-abyss vocabulary. The "
            "noun-form غمر ('abyss, deep') is the mirror-image of the participle غامرة "
            "('covering') that Saadia uses for Heb תֹהוּ at Gen 1:2 (see the related גאמרה TWIST); "
            "the systematic cross-attestation across 6 verses in 3 books demonstrates that "
            "Saadia treats غمر as the invariant Arabic terminus-technicus for the biblical "
            "cosmological-abyss, regardless of register (cosmogonic / flood / song-of-deliverance "
            "/ patriarchal-blessing): (1) Gen 7:11 — the original flood-anchor: 'נִבְקְעוּ כָּל-"
            "מַעְיְנֹת תְּהוֹם רַבָּה' → 'ובקעת גמיע עיון אלג'מר אלעצ'ים' (the abyss-fountains burst "
            "open — flood as PARTIAL REVERSION of creation, the abyssal waters Saadia placed "
            "beneath the firmament at Gen 1:2 now bursting back up); (2) Gen 8:2 — the flood-"
            "closure pillar: 'וַיִּסָּכְרוּ מַעְיְנֹת תְּהוֹם' = 'ואנסדת עיון אלג'מר' (the same fountains "
            "now stopped up, the cosmological order restored); (3) Gen 49:25 — Jacob's blessing "
            "of Joseph: 'בִּרְכֹת תְּהוֹם רֹבֶצֶת תָּחַת' = 'ברכאת אלג'מר אלראבצה ספלא' ('blessings of "
            "the deep crouching below' — the patriarchal-blessing register imports the cosmo-"
            "logical-abyss vocabulary as a SOURCE OF FERTILITY); (4) Ex 15:5 — Song of the Sea: "
            "'תְּהֹמֹת יְכַסְיֻמוּ' = 'אלג'מר ג'טאהם' ('the deep covered them' — the Egyptians' "
            "destruction as RETURN OF THE ABYSS, mirror of the cosmogonic separation now reversed "
            "for the enemy); (5) Ex 15:8 — Song of the Sea continuation: 'קָפְאוּ תְהֹמֹת בְּלֶב-יָם' = "
            "'וגמדת אלג'מר פי קלב אלבחר' ('and the deep was frozen in the heart of the sea' — the "
            "abyssal-waters' MIRACULOUS SUSPENSION as inverse-creation, a momentary cosmological "
            "stopping-of-time); (6) Deut 33:13 — Moses's blessing of Joseph (the paired-blessing "
            "complement to Gen 49:25): 'מִתְּהוֹם רֹבֶצֶת תָּחַת' = 'מן אלג'מר אלג'איצ'ה אלספלא' ('from "
            "the deep, sunken, lower' — the patriarchal-blessing register's terminus, framed by "
            "the Moses-rewrites-Jacob symmetry). The 3-book cross-Pentateuchal invariance "
            "demonstrates Saadia's most consistent cosmological-vocabulary commitment: every "
            "biblical تهوم is routed through غمر — whether the context is cosmogonic, deluvial, "
            "deliverance-song, or patriarchal-blessing, and whether the abyssal-waters are "
            "framed as primordial-chaos, divine-judgment, source-of-blessing, or instrument-of-"
            "rescue. Blau attests غمر (אגמאר) as the standard JA noun for 'abyss.' Pedagogically "
            "distinctive because the entry now demonstrates the cosmological-vocabulary's "
            "systemic reach across the Pentateuch's full thematic register, making this one of "
            "the broadest cross-book lexical commitments in the corpus."
        ),
        "blau_dict_sense_rewrite": (
            "Blau (Dict. of Medieval Judaeo-Arabic Texts, s.v. غمر) attests غمر as the standard "
            "JA noun for 'abyss / תהום,' citing Saadia's Tafsir at Bereshit 1:2 (אגמאר), Gen "
            "7:11 (the flood-fountains), Ex 15:5/8 (the Song-of-the-Sea deeps), and Deut 33:13 "
            "(the Moses-blessing parallel to Gen 49:25). The R2 cross-Pentateuchal scan "
            "confirms the systematic invariance across all 6 attestations spanning Bereshit "
            "(3 verses: creation-residue at 1:2 plus flood-open/close at 7:11, 8:2, plus "
            "patriarchal-blessing at 49:25) + Shemot (2 verses: Song-of-Sea at 15:5, 15:8) + "
            "Devarim (1 verse: Moses-blesses-Joseph at 33:13), making غمر the invariant Arabic "
            "terminus-technicus for biblical תהום across all 5 Pentateuchal-register contexts."
        ),
    },

    # ---- חגב + Devarim 31:18: 2-book graduation ----------------------------
    {
        "lemma_ja": "חגב",
        "extend_verses": [
            {"book": "Devarim", "ch": 31, "v": 18},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Anti-anthropomorphic divine-concealment vocabulary, now confirmed across 2 books "
            "with the Devarim divine-face-hiding extension. Saadia uses Ar حجب ('to veil, to "
            "screen, to conceal' — the kalām technical term for God's being veiled from creaturely "
            "vision) as his invariant anti-anthropomorphic verb for biblical divine-action that "
            "would otherwise imply a physical-spatial concealment-gesture. The cross-book arc: "
            "(1) Bereshit 7:16 — the ark-sealing pillar: 'וַיִּסְגֹּר ה' בַּעֲדוֹ' = 'וחגב אללה בעאדה' "
            "('and YHWH SCREENED behind him'). The Heb סָגַר ('shut/closed') implies a physical "
            "hand on the ark's door; Saadia routes this through the generic screening-action "
            "حجب, depersonalizing the divine gesture. (2) Devarim 31:18 — the divine-face-hiding "
            "pillar: 'וְאָנֹכִי הַסְתֵּר אַסְתִּיר פָּנַי בַּיּוֹם הַהוּא' = 'אנא מקים עלי' חגב רחמתי ענהם פי "
            "ד'אלך אלזמאן' ('I am persisting in SCREENING my mercy from them at that time'). "
            "Saadia routes BOTH the verb (סָתַר 'hide' → حجب 'screen/veil') AND the object (פָּנַי "
            "'my face' → רחמתי 'my mercy') through anti-anthropomorphic transformations: the Heb "
            "divine-face anthropomorphism is replaced with the abstract divine-mercy attribute, "
            "and the physical hiding-of-face is replaced with the philosophical screening-of-"
            "divine-presence. The Devarim 31:18 attestation thus EXTENDS the مكانيكي 'shut "
            "behind' Gen 7:16 case to the more strongly anthropomorphic 'hide-my-face' divine-"
            "absence case — both routed through the same screening-vocabulary حجب, with the "
            "kalām resonance pulling the verb into Saadia's broader theological discourse of "
            "divine-transcendence. The verb's philosophical weight (kalām: God 'veiled' from "
            "creaturely vision; the standard medieval term for the divine ḥijāb separating "
            "Creator from creation) makes حجب a load-bearing entry in Saadia's anti-anthropo-"
            "morphic vocabulary, used not as a one-off substitution but as a programmatic "
            "translational anchor for ALL biblical concealment-of-divine-presence verbs across "
            "the Pentateuch. Pedagogically distinctive because the cross-book extension surfaces "
            "the entry's broader scope: Saadia uses حجب for biblical divine-action involving "
            "ANY concealment-frame (sealing-of-ark + hiding-of-face), preserving divine "
            "transcendence through a single Arabic philosophical-screening verb."
        ),
        "blau_dict_sense_rewrite": (
            "حجب 'to veil, to screen, to conceal' — Blau attests the kalām-technical sense of "
            "حجب as the standard medieval term for the divine ḥijāb separating Creator from "
            "creation, citing Saadia's Tafsir on Gen 7:16 (וַיִּסְגֹּר → וחגב) and Saadia's own "
            "Emunot ve-Deot for the philosophical extension. The R2 cross-book scan confirms "
            "the Devarim 31:18 attestation (הסתר אסתיר → חגב), demonstrating that Saadia "
            "deploys the same screening-vocabulary across both the ark-sealing (Gen 7:16) and "
            "the divine-face-hiding (Deut 31:18) anti-anthropomorphic categories, making حجب a "
            "2-book program for biblical concealment-of-divine-presence."
        ),
    },

    # ---- אתון + Bereshit 15:7 (within-book third instance) -----------------
    {
        "lemma_ja": "אתון",
        "extend_verses": [
            {"book": "Bereshit", "ch": 15, "v": 7},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Midrashic identification / lexical re-reading, now confirmed across the full "
            "Bereshit Abraham-narrative cluster (3 verses, all Bereshit, anchored on the same "
            "Ur-as-furnace midrashic commitment). Saadia commits to the Bereshit Rabbah 38:13 + "
            "Pirqei De-Rabbi Eliezer 26 tradition that Haran died in Nimrod's furnace and "
            "Abraham was tested there; the Aramaic loanword אַתּוּן (from Daniel 3, where it names "
            "the Babylonian fiery-furnace into which the three companions are cast) is deployed "
            "as a SYSTEMATIC bridge between biblical Heb אוּר ('Ur', the toponym) and the "
            "Aggadic furnace-tradition. The cross-pericope consistency across the three "
            "Patriarchal Abraham-genealogy verses: (1) Gen 11:28 — Haran dies 'in Ur of the "
            "Chaldees' = 'באתון אלכסדאניין' (the Aggadic-furnace; the midrashic claim is that "
            "Haran was burned in Nimrod's trial-furnace before Abraham was rescued); (2) Gen "
            "11:31 — Terah's family migration: 'they went out from Ur of the Chaldees' = 'כ'רגו "
            "מן אתון אלכסדאניין' (they went out from the FURNACE — the toponymic-Ur is fully "
            "absorbed into the midrashic-furnace identification); (3) Gen 15:7 — the divine "
            "self-introduction at the Covenant-Between-the-Pieces: 'אֲנִי ה' אֲשֶׁר הוֹצֵאתִיךָ מֵאוּר "
            "כַּשְׂדִּים' = 'אנא אללה אלד'י אכ'רגתך מן אתון אלכסדאניין' ('I am the deity who brought "
            "you out from the FURNACE of the Chaldees'). The Gen 15:7 attestation is "
            "structurally significant: it is the DIVINE-SPEECH-ACT confirmation of the "
            "midrashic-furnace claim — God himself names the rescue as 'bringing-out-from-the-"
            "furnace,' aligning the foundational covenant-narrative with the Aggadic-furnace "
            "tradition. The cross-pericope consistency confirms that Saadia operates with a "
            "fixed midrashic-lexical commitment: every Pentateuchal mention of אוּר כַּשְׂדִים is "
            "routed through the Aramaic-loan furnace-vocabulary, never as a toponymic-Ur. The "
            "choice is structurally midrashic: the Aramaic-loan אַתּוּן (from Daniel 3:6 ff) is "
            "the linguistic pivot that connects the Patriarchal-narrative to the Babylonian-"
            "exile fiery-furnace tradition, making Abraham's rescue typologically parallel to "
            "the three companions' rescue. Pedagogically distinctive because the entry "
            "demonstrates Saadia's willingness to commit to a controversial Aggadic-tradition "
            "AT THE LEXICAL LEVEL — not just as commentary but as fixed translational choice — "
            "across the full Abraham-foundational-narrative arc. (Note: blau_dict remains None — "
            "this is one of the saadia-direct-only entries explicitly noted in PHASE3_R1's "
            "no-cite-audit; Blau has no entry for the Aramaic-loan אַתּוּן in the JA fiery-furnace "
            "sense.)"
        ),
        # NO blau_dict_sense_rewrite — אתון is saadia-direct-only per PHASE3_R1
        # no-cite-audit (PHASE3_R1_SESSION_NOTES.md:64). Earlier B2 draft fabricated
        # a Blau citation that doesn't exist; corrected on initial verify-gate failure.
    },

    # ---- אורד MECHANISM CORRECTION (no verses[] extension) -----------------
    # The B1 mechanism rewrite preserved the original entry's prose claim that
    # the same template appears at "Sodom, Sinai, the Tent of Meeting." The
    # B2 scan empirically disproves this: at Sinai and Tent of Meeting verses
    # Saadia uses Form V تجلَّى (manifest), NOT Form IV ورد (dispatch). Scope
    # the dispatch-frame correctly: Babel (Gen 11:5, 11:7) + Sodom (Gen 18:21).
    {
        "lemma_ja": "אורד",
        "extend_verses": [],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Anti-anthropomorphic dispatch-frame — paradigmatic Saadia substitution for biblical "
            "divine-descent narratives where YHWH is described as physically 'coming down' "
            "(יָרַד) to investigate-and-act in human space. God does not descend; God dispatches "
            "an 'amr muwajjah' — a 'directed command,' Saadia's anti-anthropomorphic euphemism "
            "for mediated divine intervention. The dispatch-frame applies INVARIANTLY across "
            "the two Bereshit YHWH-comes-down-to-investigate anchors: (1) Babel at Gen 11:5, "
            "11:7 (the original anchors — וַיֵּרֶד ה' לִרְאֹת → אורד אמרא מוגהא ליתאמל: 'I dispatch a "
            "directed command and observe'); (2) Sodom at Gen 18:21 (אֵרֲדָה-נָּא וְאֶרְאֶה → אורד "
            "אמרא מוגהא ואנצר: same Form-IV dispatch-verb + same idiom 'directed command' + same "
            "observation-frame). The cross-narrative consistency within Bereshit confirms "
            "Saadia's programmatic management of divine-descent-to-investigate verses: wherever "
            "the Hebrew has YHWH coming down to observe-and-act in human space (Babel + Sodom), "
            "Saadia routes the move through the impersonal 'directed command' dispatched from "
            "above, preserving divine transcendence. EMPIRICAL SCOPE-CORRECTION (Phase 3 R2 "
            "Batch 2): the previous mechanism prose claimed the dispatch-frame applied to "
            "'Sodom, Sinai, the Tent of Meeting' — but the R2 B2 cross-book scan demonstrates "
            "that this overreached. At the Sinai-descent verses (Ex 19:11, 19:18, 19:20, 34:5) "
            "and the Tent-of-Meeting-descent verses (Num 11:25, 12:5), Saadia consistently uses "
            "Form V تجلَّى ('manifest in cloud/fire') — a SEPARATE anti-anthropomorphic strategy "
            "that routes the divine-descent through a manifestation-frame rather than a "
            "dispatch-frame. The two strategies are structurally distinct: the dispatch-frame "
            "(ورد) is used where the Heb has YHWH descending to INVESTIGATE human action (Babel "
            "+ Sodom); the manifestation-frame (تجلَّى) is used where the Heb has YHWH descending "
            "to MANIFEST presence-and-speech in cultic space (Sinai theophany + Tent of "
            "Meeting). The dispatch-frame is bounded to 3 Bereshit verses (11:5, 11:7, 18:21). "
            "The تجلَّى manifestation cluster is logged as a candidate for a separate future TWIST "
            "entry (Phase 3 R3) — see PHASE3_R2_BATCH2_SESSION_NOTES.md for the empirical "
            "finding. Blau notes that ورد itself is Saadia's standard calque for Hebrew יר״ד "
            "in his Bible translations; the Form-IV causative (the form actually used here) is "
            "the causative of this calqued descent-sense — 'to cause to come down,' i.e., to "
            "dispatch."
        ),
        "blau_dict_sense_rewrite": (
            "Form I: 'to descend / הוריד' — Blau explicitly labels this a 'תרגום שאילה (loan-"
            "translation) from יר״ד in Bible translations,' citing Saadia's Tafsir on Tehillim "
            "28:1 and 49:18 and noting that the calque is widespread in his renderings of Bible "
            "passages. Form IV (the form actually used here) is the causative of this calqued "
            "descent-sense — 'to cause to come down,' i.e., to dispatch. The R2 Batch 2 "
            "empirical scope-correction bounds the dispatch-frame to the Bereshit YHWH-comes-"
            "down-to-INVESTIGATE pillars (Babel at Gen 11:5, 11:7 + Sodom at Gen 18:21); the "
            "Sinai (Ex 19:11, 19:18, 19:20, 34:5) and Tent-of-Meeting (Num 11:25, 12:5) descent "
            "verses use Form V تجلَّى manifestation-vocabulary, a structurally distinct anti-"
            "anthropomorphic strategy. The two strategies cluster the dispatch-frame to "
            "investigation-contexts and the manifestation-frame to cultic-theophany contexts."
        ),
    },
]


# ============================================================================
# DEFERRED — homograph filters + mechanism-mismatches
# ============================================================================

BATCH2_DEFERRED = {
    "skip": [
        # --- gleeful homograph: אשראף routine-chieftain-vocab vs anti-mythological reading
        {
            "lemma": "אשראף",
            "verse_hint": "Shemot 16:22, 34:31; Bamidbar 1:16, 3:32, 7:2, 7:10, 7:84, 10:4, 16:2, 31:13 (10 verses)",
            "reason": (
                "Register-homograph: the TWIST is specifically the ANTI-MYTHOLOGICAL reading of "
                "Heb בְּנֵי הָאֱלֹהִים at Gen 6:2-4 (refusing the angelic-being reading; reducing the "
                "verse to a social-stratification scandal where aristocrats coerce daughters of "
                "commoners). The 10 cross-book hits are all ROUTINE chieftain-vocabulary usage "
                "of أشراف for biblical leader-titles (נְשִׂיאֵי / רָאשֵׁי / זִקְנֵי / שָׂרֵי) in the "
                "Shemot exodus-leadership cluster and the Bamidbar tribal-chieftain cluster. "
                "These don't extend the anti-mythological move (there's no mythological reading "
                "to refute at the Numbers tribal-chieftain verses). The lexical-systemic basis "
                "IS real (Saadia HAS this chieftain-vocab routinely available, which grounds "
                "his anti-mythological move at Gen 6:2-4 in a broader lexical pattern), but "
                "adding the 10 verses to verses[] would suggest the anti-mythological claim "
                "extends to them, diluting the TWIST's specific scope. Consider in Phase 3 R3 "
                "whether the mechanism rewrite should explicitly name the lexical-systemic "
                "basis without extending verses[]."
            ),
        },
        # --- mechanism-mismatch: מלאיכה Bereshit 19:15 direct-cognate vs anti-anthropomorphic
        {
            "lemma": "מלאיכה",
            "verse_hint": "Bereshit 19:15 (angels-at-Sodom)",
            "reason": (
                "Mechanism-mismatch: the TWIST is REROUTING Heb אֱלֹהִים (lesser divine beings, "
                "or the serpent's promise of divinity) → Ar ملائكة 'angels' to close off "
                "creaturely apotheosis. At Gen 19:15 the Heb is הַמַּלְאָכִים (literal angels-sent-"
                "to-Lot, no theological-reroute needed), and the Ar translation is a DIRECT "
                "COGNATE (Heb מלאך ~ Ar ملك). The cognate translation isn't the anti-"
                "anthropomorphic move; it's just routine cognate substitution. Adding the verse "
                "would dilute the TWIST's specific anti-apotheosis claim."
            ),
        },
        # --- register-homograph: בדן Shemot 30:32 different Heb counterpart
        {
            "lemma": "בדן",
            "verse_hint": "Shemot 30:32 (anointing-oil prohibition: על בשר אדם → בדן)",
            "reason": (
                "Register-homograph: the TWIST is the lexical choice of بدن over جلد at Gen "
                "3:21 (Saadia routes Heb עוֹר 'animal-skin garments' through بدن, possibly to "
                "dodge the 'God slaughtered animals' implication, possibly to reserve جلد for "
                "רָקִיעַ 'firmament'). At Ex 30:32 Saadia uses بدن for Heb בְּשַׂר אָדָם ('human "
                "flesh' — anointing-oil prohibition) — different Heb counterpart, different "
                "context. The بدن usage is lexically consistent across the Pentateuch (Saadia "
                "treats بدن as his standard body-vocabulary) but the specific Gen 3:21 mechanism "
                "(avoiding جلد at the animal-skins verse) doesn't apply to Ex 30:32. The "
                "underlying lexical-system consistency could be documented in mechanism prose "
                "as supporting evidence without extending verses[]."
            ),
        },
        # --- register-homograph at scale: קרבאן 72 hits routine offering-vocabulary
        {
            "lemma": "קרבאן",
            "verse_hint": "72 hits across all 5 books (routine offering-vocabulary)",
            "reason": (
                "Register-homograph at scale: the TWIST is the SPECIFIC anti-anthropomorphic "
                "DOUBLE substitution at Gen 8:21 — Saadia replaces BOTH the verb (יָּרַח 'smelled' "
                "→ قَبِلَ 'accepted') AND the object (רֵיחַ הַנִּיחֹחַ 'soothing aroma' → אלקרבאן "
                "אלמרצ'י 'pleasing offering') to avoid the divine-nose anthropomorphism. The "
                "72 cross-book hits are routine offering-vocabulary usage of قربان for various "
                "biblical sacrifice-terms (קרבן, מנחה, עלה, חטאת, אשם, שלמים) across the "
                "Levitical sacrificial system + the Numbers chieftain-offerings cluster + the "
                "Numbers calendar-festivals cluster. Most of these are not anti-anthropomorphic "
                "moves — they're just Saadia's standard offering-vocabulary for any biblical "
                "sacrificial-term. Adding all 72 would dilute the TWIST's specific Gen 8:21 "
                "double-substitution claim. Same homograph-at-scale pattern as Phase 3 R2 "
                "Batch 1's שא (Vayikra 22, 27 human-volitional usage) and גלד (Vayikra 11-15 "
                "literal-skin usage)."
            ),
        },
        # --- register-homograph: גוהר breastplate-craft jeweler usage vs Tablets dual-register
        {
            "lemma": "גוהר",
            "verse_hint": "Shemot 28:11, 28:17, 31:5, 35:33, 39:10 (breastplate jeweler-craft)",
            "reason": (
                "Register-homograph: the TWIST is the DUAL-REGISTER move where גוהר operates as "
                "BOTH 'jewel' AND 'substance/essence' for Heb לֻחֹת. At the breastplate-craft "
                "verses (Ex 28:11 'מעשה חרש אבן', 28:17 'מלאת אבן', 31:5 + 35:33 'בחרשת אבן', "
                "39:10 'ארבעה טורים אבן') Saadia uses גוהר for Heb אֶבֶן in the BARE classical "
                "jeweler's-craft register (one register only — literal precious-stone for the "
                "breastplate). Adding these to the TWIST verses[] would dilute the dual-"
                "register claim by suggesting the philosophical-essence reading applies in the "
                "breastplate-artisan context (it doesn't — Saadia is just using גוהר as his "
                "standard precious-stone vocabulary for cultic-craft passages). The 4 Tablets-"
                "register Shemot verses (24:12, 31:18, 34:1, 34:4) ARE shipped — see "
                "PROMOTE_IN_PLACE above."
            ),
        },
    ],
    "_phase3_r2_b2_outcomes": [
        "Scanned: all 36 TWIST entries (B1 lemmas re-scanned; already-attested verses correctly filtered out).",
        "Promote-in-place ships: 4 verses[]-extension entries (גוהר, ג'מר, חגב, אתון) + 1 mechanism-correction-only entry (אורד), totaling 11 new verse attestations.",
        "Cross-book graduations: ג'מר reaches 3-book attestation (Bereshit + Shemot + Devarim) — the third 3-book TWIST in the corpus, after אדלג + חאכמא in B1. גוהר + חגב reach 2-book attestation.",
        "TWIST 3-book count: was 2 (after B1) → 3 (after B2): אדלג, חאכמא, ג'מר.",
        "TWIST 2-book count: was 1 (after B1, מסלט) → 3 (after B2): מסלט, גוהר, חגב.",
        "TWIST Bereshit-only count: was 30 (after B1) → 27 (after B2): ג'מר + חגב moved out, אתון strengthened within-book.",
        "Empirical correction: the original אורד entry's mechanism prose claimed 'Sodom, Sinai, the Tent of Meeting' all used the same dispatch-frame ورد. The B2 scan shows Sinai/Tent verses actually use Form V تجلَّى manifestation-vocabulary — structurally distinct anti-anthropomorphic strategy. Mechanism corrected; dispatch-frame scoped to Babel + Sodom (3 Bereshit verses). The تجلَّى manifestation cluster is a candidate for a separate future TWIST (Phase 3 R3).",
        "Homograph filters: 5 (אשראף routine chieftain-vocab; מלאיכה direct-cognate; בדן different-Heb-counterpart; קרבאן 72 routine-offering-vocab; גוהר breastplate jeweler-craft).",
        "No-hit lemmas: 15 single-book TWIST entries had zero cross-book attestations (גאמרה, מסתבחרה, ריאח, תהב, אטג'אני, קיאדך, כ'טאך, אכ'תיאר, טאעה, תופי, ינג'מד, שמשאר, קרדא, יסיידונך, ד'רקובה, משוובה) — these are all anchored at unique-context Bereshit creation/flood/Babel/Patriarchal verses with no cross-book attestations in the tafsir corpus.",
        "Phase 3 R2 sweep COMPLETE: B1 (6 entries / 19 verses) + B2 (4 entries / 11 verses + 1 mechanism correction) = 10 entries promoted, 30 new verse attestations, 3 three-book TWISTs + 3 two-book TWISTs + 4 within-book TWIST strengthenings.",
    ],
}


# ============================================================================
# Helpers — mirror scripts/apply_phase3_r2_batch1.py with one tweak:
# allow mechanism rewrites with no extend_verses (for the אורד correction)
# ============================================================================

def _patch_promote_in_place(payload: dict) -> list[dict]:
    """Iterate PROMOTE_IN_PLACE and apply each extension. For each item:
    extend verses[] (dedup on (book, ch, v)), extend variants[] (dedup), and
    rewrite mechanism + blau_dict.sense. For entries with no extend_verses
    but a mechanism_rewrite (B2's אורד correction case), apply the rewrite
    anyway. Returns per-lemma summaries.
    """
    summaries = []
    for spec in PROMOTE_IN_PLACE:
        target_lemma = spec["lemma_ja"]
        for entry in payload["entries"]:
            if entry.get("lemma_ja") != target_lemma:
                continue
            existing_v = {(v["book"], v["ch"], v["v"]) for v in entry.get("verses", [])}
            added_v = []
            for v in spec.get("extend_verses", []):
                key = (v["book"], v["ch"], v["v"])
                if key not in existing_v:
                    entry["verses"].append(v)
                    existing_v.add(key)
                    added_v.append(f"{v['book']} {v['ch']}:{v['v']}")
            existing_var = set(entry.get("variants", []))
            added_var = []
            for var in spec.get("extend_variants", []):
                if var not in existing_var:
                    entry.setdefault("variants", []).append(var)
                    existing_var.add(var)
                    added_var.append(var)
            # B2 tweak: apply mechanism rewrite even if no verses added,
            # to handle the אורד empirical-correction case
            had_mechanism_rewrite = False
            if "mechanism_rewrite" in spec:
                if entry.get("mechanism") != spec["mechanism_rewrite"]:
                    entry["mechanism"] = spec["mechanism_rewrite"]
                    had_mechanism_rewrite = True
            if "blau_dict_sense_rewrite" in spec:
                bd = entry.setdefault("blau_dict", {})
                if bd.get("sense") != spec["blau_dict_sense_rewrite"]:
                    bd["sense"] = spec["blau_dict_sense_rewrite"]
                    had_mechanism_rewrite = True

            if added_v or added_var or had_mechanism_rewrite:
                summaries.append({
                    "lemma": target_lemma,
                    "verses_added": added_v,
                    "variants_added": added_var,
                    "mechanism_rewritten": had_mechanism_rewrite,
                    "total_verses_now": len(entry["verses"]),
                })
            else:
                summaries.append({
                    "lemma": target_lemma,
                    "verses_added": [],
                    "variants_added": [],
                    "mechanism_rewritten": False,
                    "note": "all extensions already present (idempotent re-run)",
                })
            break
        else:
            summaries.append({"lemma": target_lemma, "error": "target lemma not found in divergence file"})
    return summaries


def _update_deferred(deferred_path: pathlib.Path) -> dict:
    """Write Phase 3 R2 Batch 2 entries into _blau_saadia_deferred.json under
    a fresh "phase3_r2/batch2" namespace (idempotent on (lemma, verse_hint)).
    """
    payload = json.loads(deferred_path.read_text())
    ns = payload.setdefault("phase3_r2", {})
    b2 = ns.setdefault("batch2", {})

    added = {"skip": 0}
    for bucket in ("skip",):
        new_items = BATCH2_DEFERRED.get(bucket, [])
        existing = b2.setdefault(bucket, [])
        existing_keys = {(it.get("lemma"), it.get("verse_hint")) for it in existing if isinstance(it, dict)}
        for item in new_items:
            key = (item.get("lemma"), item.get("verse_hint"))
            if key in existing_keys:
                continue
            existing.append(item)
            existing_keys.add(key)
            added[bucket] += 1

    outcomes = b2.setdefault("_phase3_r2_b2_outcomes", [])
    if isinstance(outcomes, list):
        for line in BATCH2_DEFERRED.get("_phase3_r2_b2_outcomes", []):
            if line not in outcomes:
                outcomes.append(line)

    b2.setdefault("_session", "Phase 3 R2 Batch 2 — systematic sweep + אורד mechanism correction (apply_phase3_r2_batch2.py)")

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return {
        "added": added,
        "phase3_r2_batch2_buckets_now": {k: len(v) if isinstance(v, list) else v for k, v in b2.items()},
    }


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    div_path = root / "data" / "tafsir-divergence.json"
    deferred_path = root / "data" / "_blau_saadia_deferred.json"

    if not div_path.exists():
        print(f"FATAL: {div_path} not found — run from judeo-arabic-app root", file=sys.stderr)
        sys.exit(1)
    if not deferred_path.exists():
        print(f"FATAL: {deferred_path} not found", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(div_path.read_text())

    promote_summaries = _patch_promote_in_place(payload)

    div_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(div_path.read_text())  # parse-check

    deferred_summary = _update_deferred(deferred_path)

    print("=" * 76)
    print("Phase 3 R2 Batch 2 — systematic-sweep TWIST scan + אורד mechanism correction")
    print("=" * 76)
    print(f"\nPromote-in-place per-lemma summary:\n{json.dumps(promote_summaries, ensure_ascii=False, indent=2)}")

    n_promoted = sum(1 for s in promote_summaries if s.get("verses_added") or s.get("mechanism_rewritten"))
    n_new_verses = sum(len(s.get("verses_added", [])) for s in promote_summaries)
    print(f"\nPromoted/corrected entries: {n_promoted}/{len(PROMOTE_IN_PLACE)}")
    print(f"New verse extensions: {n_new_verses}")
    print(f"Total divergence entries (unchanged): {len(payload['entries'])}")

    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")

    print(f"\nDeferred file summary: {json.dumps(deferred_summary, ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    main()

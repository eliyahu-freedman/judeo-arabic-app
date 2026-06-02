"""
Phase 3 R2 Batch 1 — cross-book TWIST scan, priority-cluster sweep.

The first promote-in-place batch ever to operate at TWIST tier. Mirrors
scripts/apply_phase4_devarim_batch1.py:PROMOTE_IN_PLACE/_patch_promote_in_place
exactly (no NEW_ENTRIES list — R2 is promote-in-place only).

Scan results
------------
Source: scripts/scan_phase3_r2.py grepping all five tafsir-{book}-{ch}.json
files for each TWIST entry's lemma_ja + variants[]. Hits triaged against the
corresponding -alignment.json files to filter homographs (e.g., שא human-
volitional usage in Vayikra 22; גלד literal-skin in Lev 11-15; חאכמא Devarim
judicial-vocabulary in Deut 17ff). See PHASE3_R2_BATCH1_SESSION_NOTES.md for
the full triage rationale.

Promote-in-place — 6 TWIST entries, 19 new verse attestations
--------------------------------------------------------------
  - אדלג     +Bereshit 20:8, 21:14, 22:3, 26:31, 28:18, 32:1
              +Shemot   8:16, 9:13, 24:4, 32:6, 34:4
              (was 2 verses Bereshit/Bamidbar → 13 verses across 3 books;
              3-BOOK GRADUATION)

  - חאכמא    +Vayikra  20:24
              (was 3 verses Bereshit/Shemot → 4 verses across 3 books;
              3-BOOK GRADUATION — the third 3-book TWIST in the corpus)

  - מסלט     +Bereshit 24:2
              +Shemot   8:18, 21:8
              (was 6 verses Bereshit-only → 9 verses across 2 books;
              2-BOOK GRADUATION)

  - אורד     +Bereshit 18:21        (Sodom-cluster within-book; the existing
              mechanism prose already names "Sodom, Sinai, the Tent of
              Meeting" — this syncs verses[] to the prose)

  - תואעד    +Bereshit 20:18        (Abimelech-wombs threat — within-book
              extension of the anti-anthropomorphic divine-affect →
              divine-warning lexical move)

  - אלממתעה  +Bereshit 38:15, 38:22 (Tamar pericope internal; verses[] now
              spans the full Tamar narrative; the parallel Devarim 23:18
              attestation is BLOCKED by the duplicate NOTE entry ממתעה
              shipped in Phase 4 Devarim Batch 1 — see deferred bucket)

Deferred — homograph filters + duplicate-collision logging
----------------------------------------------------------
  - שא (Vayikra 22:18-21, 27:13-19; Devarim 18:6) — homograph: human-
    volitional usage vs the entry's divine-creation register
  - גלד (Vayikra 11:32, 13:2-48, 15:17) — homograph: literal classical
    "skin" sense vs the entry's "firmness/firmament" calque-extension
  - חאכמא (Shemot 21:6, 22:7, 22:8; Devarim 17:9, 17:12, 21:19, 22:15,
    25:2, 25:7) — homograph: judicial-vocabulary register vs the entry's
    anti-anthropomorphic circumstantial-accusative insertion in divine
    speech-acts
  - אורד Shemot 25:30 / Devarim 23:15, 24:1 — homograph: noun מוגהא
    "(showbread) presented" / אמרא "a matter" rather than the verbal
    Form-IV dispatch-frame
  - אלממתעה Devarim 23:18 — DUPLICATE COLLISION with the NOTE entry
    ממתעה (Phase 4 Devarim Batch 1). The verse is already covered at NOTE
    tier; promoting it into the TWIST verses[] would create double-
    attestation across two entries. Deferred to a future consolidation
    pass (out-of-scope for promote-in-place-only R2).

Apply pattern
-------------
Mirrors scripts/apply_phase4_devarim_batch1.py:
  PROMOTE_IN_PLACE list of 6 entries with extend_verses / extend_variants /
  mechanism_rewrite / blau_dict_sense_rewrite.
  _patch_promote_in_place() iterates the list; per-lemma summaries reported.
Fresh "phase3_r2" namespace in data/_blau_saadia_deferred.json, idempotent.
"""

import json
import pathlib
import sys
from collections import Counter


# ============================================================================
# CROSS-BOOK PROMOTE-IN-PLACE — extensions to existing TWIST entries
# ============================================================================

PROMOTE_IN_PLACE = [

    # ---- אדלג + Shemot (5v) + Bereshit-internal (6v): 3-book graduation ----
    {
        "lemma_ja": "אדלג",
        "extend_verses": [
            {"book": "Bereshit", "ch": 20, "v": 8},
            {"book": "Bereshit", "ch": 21, "v": 14},
            {"book": "Bereshit", "ch": 22, "v": 3},
            {"book": "Bereshit", "ch": 26, "v": 31},
            {"book": "Bereshit", "ch": 28, "v": 18},
            {"book": "Bereshit", "ch": 32, "v": 1},
            {"book": "Shemot", "ch": 8, "v": 16},
            {"book": "Shemot", "ch": 9, "v": 13},
            {"book": "Shemot", "ch": 24, "v": 4},
            {"book": "Shemot", "ch": 32, "v": 6},
            {"book": "Shemot", "ch": 34, "v": 4},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Post-classical semantic shift, now confirmed across the entire Pentateuchal "
            "'rise-early' narrative tradition — 13 verses across THREE books. Saadia uses أَدْلَجَ "
            "(Form IV of دلج, classical 'to travel by night, to set out before dawn') as the "
            "invariant equivalent of Heb הִשְׁכִּים (Hiphil of שכם, 'to rise early in the morning' — "
            "the canonical biblical Patriarchal-and-Mosaic narrative formula for purposive early-"
            "morning departure). Classical Arabic narrows أدلج specifically to NIGHT-travel; "
            "Saadia exploits the post-classical broadening (already attested in Lisān al-ʿArab) "
            "to a generic 'early-morning departure' frame, then deploys it as the systematic "
            "Pentateuchal terminus-technicus. The cross-book attestation arc spans: (1) the full "
            "Bereshit Patriarchal sequence — Abraham at Abimelech's court (20:8) → Abraham casting "
            "out Hagar (21:14) → AKEDAH (22:3 — the canonical 'rose early' verse of the binding) "
            "→ Isaac–Abimelech treaty (26:31) → Jacob at Bethel after the dream (28:18) → Laban "
            "after the Mizpah covenant (32:1) → Abraham overlooking Sodom (19:27, the original "
            "anchor); (2) the Shemot Mosaic plague-and-covenant sequence — Moses at the Nile "
            "before Pharaoh (8:16) → Moses for the hail-plague announcement (9:13) → Moses "
            "building the Sinai-covenant altar (24:4) → the golden-calf morning offerings "
            "(32:6) → Moses ascending Sinai with the second tablets (34:4); (3) the Bamidbar "
            "ma'apilim attempt at the Mt. Hor breach (14:40, the original cross-book anchor). "
            "Across all 13 attestations Heb הִשְׁכִּים/וַיַּשְׁכֵּם is rendered with the same Form IV "
            "أدلج + variants (פאדלג / ואדלג / ואדלגו / פאדלגו), with the standard adverbial-"
            "phrase באלג'דאה ('at-the-dawn') almost always trailing — a fixed Saadyan idiom for "
            "the Heb בַּבֹּקֶר. The cross-Pentateuchal-arc invariance is the strongest evidence "
            "in the corpus that Saadia operates with stable narrative-formula vocabulary: "
            "every 'rose-early' Patriarchal or Mosaic departure receives the same Arabic "
            "lexical signature, regardless of speaker (Abraham, Hagar, Isaac, Jacob, Laban, "
            "Moses, the Israelites) or context (private journey, treaty-ratification, cultic "
            "encounter, military departure). Pedagogically distinctive because the verse-count "
            "(13) and the cross-book breadth (3 books spanning Patriarchal → Mosaic → Wilderness) "
            "make this the single largest narrative-formula promotion in the corpus."
        ),
        "blau_dict_sense_rewrite": (
            "Blau (Dict. of Medieval Judaeo-Arabic Texts, s.v. דלג) explicitly cites Saadia's "
            "Tafsir on Exodus 8:16 — 'השכם בבקר' rendered as 'אדלג באלגדאה' — as the canonical "
            "example of the post-classical semantic transition from 'to travel by night' → 'to "
            "rise early.' Blau notes that the same shift is already attested in classical Arabic "
            "Lisān al-ʿArab, and that Saadia adopts it as his standard equivalent of הִשְׁכִּים. "
            "The R2 cross-book scan confirms the systematic invariance across 13 attestations "
            "spanning Bereshit (7 verses) + Shemot (5 verses) + Bamidbar (1 verse), making "
            "אדלג the broadest narrative-formula calque in the divergence corpus."
        ),
    },

    # ---- חאכמא + Vayikra 20:24: 3-book graduation ----------------------------
    {
        "lemma_ja": "חאכמא",
        "extend_verses": [
            {"book": "Vayikra", "ch": 20, "v": 24},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Anti-anthropomorphic interpretive insertion, now confirmed across THREE books in "
            "the divine-speech register. Saadia inserts the circumstantial-accusative participle "
            "حاكمًا ('as a decreer / acting-as-judge') into divine speech-acts to avoid portraying "
            "God as 'speaking' directly. The construction routes the Heb's bare לאמר / וָאֹמַר "
            "('saying' / 'and I said') through an indirect frame: God doesn't speak — God "
            "judicially-decrees, with حاكمًا naming the modality of the divine speech-act. "
            "Standard Saadianic move documented in saadia-gloss-table.json; built on the well-"
            "attested judicial sense of حكم. The cross-Pentateuchal arc now spans (1) the divine-"
            "blessing speech-act in Bereshit 1:22 (וַיְבָרֶךְ אֹתָם אֱלֹהִים לֵאמֹר → ובארכהם אללה חאכמא — "
            "the FIRST recorded divine speech-act in scripture, marked from the outset with the "
            "non-anthropomorphic frame); (2) the Mosaic-judicial speech-acts in Shemot 2:14 "
            "(וַיֹּאמֶר מִי שָׂמְךָ לְאִישׁ שַׂר וְשֹׁפֵט עָלֵינוּ → אלחאכם — Moses confronted as 'the decreer/judge') "
            "and 22:27 (אֱלֹהִים לֹא תְקַלֵּל וְנָשִׂיא בְעַמְּךָ → לא תהון בחאכם — the elohim-as-judges "
            "passage); AND (3) the Vayikra divine-promise speech-act at 20:24 (וָאֹמַר לָכֶם "
            "אַתֶּם תִּירְשׁוּ אֶת אַדְמָתָם → וקלת לכם חאכמא — 'I said to you, AS DECREER, you shall "
            "possess their land'). The Vayikra 20:24 attestation is structurally significant: "
            "it is the FIRST divine-promise speech-act in the Levitical land-vocabulary register, "
            "and Saadia routes it through exactly the same non-anthropomorphic insertion as "
            "the Bereshit 1:22 creation-blessing. The cross-book consistency confirms that the "
            "circumstantial-accusative חאכמא is not a one-off Bereshit-1 anti-anthropomorphic "
            "move but Saadia's programmatic strategy for the divine speech-act category across "
            "the Pentateuch — wherever YHWH 'says' something covenantally-binding, the insertion "
            "names the modality as judicial-decree rather than vocal-utterance. Distinct from "
            "the bare-form judicial חאכם / אלחאכם used for human judges in Ex 21:6, 22:7-8 and "
            "Deut 17:9ff (different register: judicial-administrative, not divine-speech-modifier; "
            "see Phase 4 Devarim B1 session notes line 158-160). Pedagogically distinctive because "
            "the entry now demonstrates Saadia's systematic management of divine speech-acts "
            "across all three major covenantal speech-modes (blessing, judgment-context, promise-"
            "of-land), spanning Bereshit + Shemot + Vayikra."
        ),
        "blau_dict_sense_rewrite": (
            "Blau (Dict. of Medieval Judaeo-Arabic Texts, s.v. חכם) attests Form III 'to judge / "
            "שפט, דן' alongside Forms I/II/V — the judicial sense Saadia builds on when inserting "
            "the participle حاكمًا at לאמר / וָאֹמַר. Blau does not name the inserted-participle "
            "pattern itself; the divergence here is in Saadia's syntactic deployment of an "
            "otherwise-classical sense. The R2 cross-book scan confirms the systematic invariance "
            "across three covenantal divine-speech-act registers — creation-blessing (Gen 1:22), "
            "Mosaic-judicial framing (Ex 2:14, 22:27), and Levitical land-promise (Lev 20:24) — "
            "and excludes the judicial-administrative חאכם cluster (Ex 21-22, Deut 17ff) as a "
            "distinct register from the divine-speech-act insertion."
        ),
    },

    # ---- מסלט + Shemot (2v) + Bereshit-internal (1v): 2-book graduation ----
    {
        "lemma_ja": "מסלט",
        "extend_verses": [
            {"book": "Bereshit", "ch": 24, "v": 2},
            {"book": "Shemot", "ch": 8, "v": 18},
            {"book": "Shemot", "ch": 21, "v": 8},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Anti-anthropomorphic theological gloss extended into a programmatic dominion-"
            "vocabulary system, now confirmed across TWO books and three semantic registers "
            "(divine-dominion-grant + human-vicegerency + legal-authority). Saadia uses the "
            "Form II passive participle مسلَّط ('one set in authority over, made-dominant') and "
            "its Form V cognate تسلَّط ('to gain mastery, to have legal authority') as the "
            "invariant Pentateuchal vocabulary for the dominion semantic field. The cross-"
            "register arc: (1) the imago-Dei theological core — Heb צֶלֶם is read NOT as visual-"
            "resemblance but as FUNCTIONAL DOMINION (man set-as-master over creation) at Gen "
            "1:26, 1:27, 5:1; the cognate sin-mastery voluntarist account at Gen 4:7 ('sin "
            "couches at the door...you shall rule over it' = יתסלט בה / שאלת תתסלט בה); the "
            "post-flood resumption of dominion at Gen 9:6; the Edenic gender-hierarchy of Gen "
            "3:16 ('he shall rule over you' = יתסלט עליך); (2) the human-vicegerency extension "
            "at Gen 24:2 ('Abraham's senior servant set over all his property' = אלמסלט עלי' "
            "גמיע מאלה — same Form II passive participle for the steward as for the imago-Dei "
            "vicegerent); (3) the Mosaic divine-sovereignty assertion at Ex 8:18 ('that you may "
            "know I am God in the midst of the earth' = אני אללה מסלט עלי' גמיע אלעאלם — Saadia "
            "interpolates مسلَّط to make explicit what בְּקֶרֶב הָאָרֶץ implies: active sovereign "
            "presence-as-dominion); (4) the legal-authority extension at Ex 21:8 (Heb לֹא יִמְשֹׁל "
            "לְמָכְרָהּ 'he has no power to sell her' = לא יתסלט אן יביעהא — Form V deployed for "
            "human-legal-authority). The cross-book consistency confirms that مسلَّط/تسلَّط is "
            "Saadia's systematic Arabic terminus-technicus for the entire Heb מָשַׁל-dominion "
            "vocabulary, applied invariantly whether the dominion is bestowed by God on man "
            "(imago-Dei), by man on man (steward over property; husband over wife), exercised "
            "by God himself (sovereign over the earth), or claimed by humans in legal contexts "
            "(authority over a betrothed slave-woman). The systematic anti-anthropomorphic-and-"
            "lexical-fixity makes this one of Saadia's most consistent translational programs. "
            "Pedagogically distinctive because the cross-register breadth surfaces the entry's "
            "real shape: not an isolated anti-anthropomorphic move at the imago-Dei verses but a "
            "programmatic dominion-vocabulary spanning theology, household-economy, divine-"
            "sovereignty, and legal-authority — all carried by a single Arabic Form II/V pair."
        ),
        "blau_dict_sense_rewrite": (
            "Form V + على (post-classical): to gain mastery over / השתלט; with the idiom تسلط "
            "على = השתלט על. Blau cites Yefet on Habakkuk 3:8 ('the first enemy who gained "
            "mastery over Israel') — same construction Saadia uses in Gen 4:7. The R2 cross-"
            "book scan confirms that Saadia deploys the Form II passive participle مسلَّط and "
            "its Form V cognate consistently across Bereshit (the imago-Dei + Cain + Eve + "
            "Noahide-dominion verses at 1:26, 1:27, 3:16, 4:7, 5:1, 9:6 + the household-steward "
            "verse at 24:2) and Shemot (the divine-sovereignty assertion at 8:18 + the legal-"
            "authority verse at 21:8), making the dominion-vocabulary a 2-book program."
        ),
    },

    # ---- אורד + Bereshit 18:21 (Sodom within-book sync) -----------------------
    {
        "lemma_ja": "אורד",
        "extend_verses": [
            {"book": "Bereshit", "ch": 18, "v": 21},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Anti-anthropomorphic — paradigmatic Saadia substitution, now extended within Bereshit "
            "to the Sodom anti-anthropomorphic anchor that the original mechanism prose already "
            "named. God does not descend; God dispatches an 'amr muwajjah' — a 'directed command,' "
            "Saadia's recurring euphemism for divine intervention in human space. The cross-"
            "narrative arc within Bereshit: (1) Babel at Gen 11:5, 7 (the original anchor — וַיֵּרֶד "
            "ה' לִרְאֹת → אורד אמרא מוגהא: 'I dispatch a directed command and observe'); (2) NOW "
            "ALSO Sodom at Gen 18:21 (אֵרֲדָה-נָּא וְאֶרְאֶה → אורד אמרא מוגהא ואנצר: same Form-IV "
            "dispatch-verb + same idiom 'directed command' + same observation-frame). The "
            "Bereshit 18:21 attestation is the structural pillar the entry's original "
            "mechanism prose names ('the same template appears throughout the Tafsir wherever "
            "the Hebrew has YHWH coming down — Sodom, Sinai, the Tent of Meeting'); the R2 "
            "scan confirms it and syncs verses[] to the prose. The cross-narrative consistency "
            "within Bereshit confirms Saadia's programmatic management of divine-descent verses: "
            "wherever the Hebrew has YHWH coming down (יָרַד) to observe-and-act in human space, "
            "Saadia routes the move through the impersonal 'directed command' (amr muwajjah) "
            "dispatched from above, preserving divine transcendence. Blau notes that ورد itself "
            "is Saadia's standard calque for Hebrew יר״ד in his Bible translations; the "
            "Form-IV causative (the form actually used here) reframes 'descend' as 'cause-to-"
            "descend, dispatch.' Pedagogically distinctive because the entry now demonstrates "
            "the anti-anthropomorphic-dispatch pattern at both the post-flood Babel anchor AND "
            "the pre-destruction Sodom anchor — the two most famous Bereshit verses where the "
            "Hebrew has YHWH 'come down' to investigate human action. (Note: Saadia's Sinai "
            "descent-verses — Ex 19:11, 19:18, 19:20, 34:5 — are candidates for a future R2 "
            "Batch 2 extension into Shemot if the same Form-IV dispatch-verb surfaces.)"
        ),
        "blau_dict_sense_rewrite": (
            "Form I: 'to descend / הוריד' — Blau explicitly labels this a 'תרגום שאילה (loan-"
            "translation) from יר״ד in Bible translations,' citing Saadia's Tafsir on Tehillim "
            "28:1 and 49:18 and noting that the calque is widespread in his renderings of Bible "
            "passages. Form IV (the form actually used here) is the causative of this calqued "
            "descent-sense — 'to cause to come down,' i.e., to dispatch. The R2 cross-narrative "
            "scan confirms the systematic use of the Form-IV dispatch-frame across Bereshit's "
            "two YHWH-descends-to-investigate anchors (Sodom at 18:21 + Babel at 11:5, 11:7)."
        ),
    },

    # ---- תואעד + Bereshit 20:18 (Abimelech-wombs within-book) ---------------
    {
        "lemma_ja": "תואעד",
        "extend_verses": [
            {"book": "Bereshit", "ch": 20, "v": 18},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Anti-anthropomorphic: divine regret/change-of-mind replaced by prophetic warning, "
            "now extended to the divine-restraint frame at the Abimelech-wombs passage. The "
            "Form-III/IV verb وَاعَدَ ('to warn / threaten / decree-doom against') routes biblical "
            "expressions of divine affect (Gen 6:6-7 וַיִּנָּחֶם 'and He regretted') AND of divine "
            "direct biological-action (Gen 20:18 עָצֹר עָצַר ה' בְּעַד כָּל-רֶחֶם 'God had certainly "
            "closed every womb') through the same prophetic-warning frame. The cross-narrative "
            "arc within Bereshit: (1) the flood-decision anti-anthropomorphic anchor at Gen 6:6, "
            "6:7 (Heb וַיִּנָּחֶם 'and YHWH regretted' → תואעדהם, with the prose-prophetic frame "
            "implying the 120-year limit at Gen 6:3 functioned as a probationary warning — God "
            "did not change His mind on Yom Six, He had already announced the deadline); (2) "
            "NOW ALSO Gen 20:18 (Heb 'for YHWH had certainly restrained every womb of Abimelech's "
            "house for the matter of Sarah Abraham's wife' = לאן אללה כאן קד תואעד בחבס כל רחם "
            "לבית אבימלך — 'for God had THREATENED with the closing-up of every womb'). The "
            "Gen 20:18 attestation broadens the mechanism beyond the affective-regret category "
            "to include the direct-biological-intervention category: where the Hebrew has God "
            "directly closing wombs (an act that would imply mechanical-divine-interference in "
            "human biology), Saadia mediates this through the same prophetic-warning frame, "
            "preserving divine transcendence by making the direct biological intervention a "
            "MEDIATED THREAT (the warning materializes through other means rather than as raw "
            "divine biological intervention). The cross-narrative consistency within Bereshit "
            "demonstrates a broader Saadyan principle: when the Hebrew describes God directly "
            "doing something that an anthropomorphic-immanent reading would frame as mechanical "
            "intervention, Saadia routes the action through prophetic-warning vocabulary — "
            "whether the action is affective (regret) or biological (womb-closing). The same "
            "Form III/IV root surfaces in 6:7 ('as I warned them'); Bereshit 20:18 extends "
            "the pattern to the womb-restraint event."
        ),
        "blau_dict_sense_rewrite": (
            "Form I + بـ: 'to prophesy doom / לנבא דבר' (citing Saadia's translations and the "
            "Geonim); Form IV + بـ: 'to promise / threaten / decree' (وعد ٢ل٦١ بها = ניבא דבר; "
            "the prophetic doom-pronouncement and the announcement of an evil are explicitly "
            "merged). Blau's entry directly supports the warning/decreeing-doom sense Saadia "
            "uses here. The R2 cross-narrative scan confirms the warning-frame application "
            "across both the affective (Gen 6:6-7 וַיִּנָּחֶם) and the direct-biological-"
            "intervention (Gen 20:18 עָצַר ה') anti-anthropomorphic categories within Bereshit."
        ),
    },

    # ---- אלממתעה + Bereshit 38:15, 22 (Tamar within-pericope) --------------
    {
        "lemma_ja": "אלממתעה",
        "extend_verses": [
            {"book": "Bereshit", "ch": 38, "v": 15},
            {"book": "Bereshit", "ch": 38, "v": 22},
        ],
        "extend_variants": [],
        "mechanism_rewrite": (
            "Lexical specification (anti-rabbinic / against the targumic neutralization), now "
            "extended across the FULL Tamar pericope (Gen 38:15, 21, 22). The Targumim and most "
            "medieval commentators render קְדֵשָׁה with a generic 'prostitute' word, effacing the "
            "cultic dimension. Saadia, working in an Islamic juristic-lexicographical milieu "
            "where متعة has technical resonance, picks a term that names the cultic category — "
            "and uses it across all three Tamar-pericope attestations: (1) Gen 38:15 (Heb "
            "וַיַּחְשְׁבֶהָ לְזוֹנָה 'and he reckoned her a harlot' = וחסבהא ממתעה — note Saadia "
            "specifically reroutes Heb זוֹנָה through ממתעה, surfacing the cultic-prostitute "
            "category EVEN where the Hebrew uses the generic harlot-word); (2) Gen 38:21 (Heb "
            "אַיֵּה הַקְּדֵשָׁה 'where is the cult-prostitute' = אין אלממתעה — the original anchor); "
            "(3) Gen 38:22 (Heb לֹא הָיְתָה בָזֶה קְדֵשָׁה 'there has been no cult-prostitute here' "
            "= מא כאנת ההנא ממתעה). The cross-verse consistency within the pericope is "
            "structurally significant: Saadia treats the three terms (Heb זוֹנָה / הַקְּדֵשָׁה / "
            "קְדֵשָׁה) as referring to a SINGLE social-cultic category — the temple-prostitute — "
            "and uses the same Arabic terminus-technicus for all three. The same word recurs "
            "again at Deuteronomy 23:18 (the prohibition on Israelite men/women being a "
            "קָדֵשׁ/קְדֵשָׁה — see the separate ממתעה NOTE entry shipped in Phase 4 Devarim "
            "Batch 1), confirming the systematic identification across the Pentateuch. The "
            "cross-pericope consistency demonstrates Saadia's reading: that the foreign cultic-"
            "prostitute category extends backward from Deuteronomy's prohibition to Tamar's "
            "ad-hoc deception — Tamar is read as deliberately assuming a cultic identity to "
            "claim the right of levirate-substitution, NOT as merely a generic harlot."
        ),
        "blau_dict_sense_rewrite": (
            "ممتعة 'harlot, temple-prostitute / קְדֵשָׁה, אישה שנועדה לזנות פולחנית' — Blau cites "
            "Saadia on Gen 38:21 directly ('איה הקדשה... לא הייתה בזה קדשה' → 'אין אלממתעה... "
            "מא כאנת ההנא ממתעה') and the parallel rendering of the prohibition at Deuteronomy "
            "23:18. The R2 cross-pericope scan confirms the additional Gen 38:15 attestation "
            "where Saadia routes Heb זוֹנָה through the same ממתעה terminus, treating the three "
            "Tamar-pericope terms (זוֹנָה / הַקְּדֵשָׁה / קְדֵשָׁה) as referring to a single cultic-"
            "prostitute category. (Note: the Deut 23:18 attestation is currently held by the "
            "separate NOTE entry ממתעה shipped in Phase 4 Devarim Batch 1; consolidating the "
            "Bereshit-TWIST and Devarim-NOTE entries into a single 2-book TWIST is deferred "
            "for a future cleanup pass, since promote-in-place R2 cannot delete entries.)"
        ),
    },
]


# ============================================================================
# DEFERRED — homograph filters, duplicate-collisions, borderlines
# ============================================================================

BATCH1_DEFERRED = {
    "skip": [
        # --- homograph: שא human-volitional vs the TWIST's divine-creation register
        {
            "lemma": "שא",
            "verse_hint": "Vayikra 22:18, 22:21, 27:13, 27:15, 27:19; Devarim 18:6",
            "reason": (
                "Homograph: Ar شاء ('to will') is a generic high-frequency verb. Saadia's TWIST "
                "covers the anti-anthropomorphic creation register (Heb וַיֹּאמֶר אֱלֹהִים יְהִי X → "
                "Saadia: 'the deity *willed* X' at Gen 1:3-24). The Vayikra hits all carry "
                "the human-volitional sense (man wills to bring an offering at Lev 22:18, 22:21; "
                "man wills to redeem at Lev 27:13-19), and the Devarim 18:6 hit carries the "
                "same human-volitional register ('when he wills'). None of these extends the "
                "divine-creation-via-willing claim, so they are not in-scope for promote-in-place."
            ),
        },
        # --- homograph: גלד literal-skin vs the TWIST's firmness/firmament calque
        {
            "lemma": "גלד",
            "verse_hint": "Vayikra 11:32, 13:2-48, 15:17 (11 verses, leprosy + skin/hide laws)",
            "reason": (
                "Homograph: Ar جلد carries the classical 'skin/hide' sense (literal-objective). "
                "Saadia's TWIST is specifically about the calque-EXTENSION of جلد from 'skin' "
                "(classical) to 'firmness/firmament' (Saadia's reading of Heb רָקִיעַ at Gen "
                "1:6-20). The Vayikra Lev 11/13/15 attestations all use جلد in the classical "
                "literal-skin sense (skin-as-leprosy-substrate, skin-as-garment-material). The "
                "TWIST mechanism explicitly hinges on the SEMANTIC STRETCH from skin → firmness; "
                "verses where Saadia uses the unstretched classical sense don't extend the "
                "calque-claim and are not in-scope for promote-in-place."
            ),
        },
        # --- homograph: חאכם judicial-vocabulary vs the TWIST's circumstantial-acc insertion
        {
            "lemma": "חאכם",
            "verse_hint": "Shemot 21:6, 22:7, 22:8; Devarim 17:9, 17:12, 21:19, 22:15, 25:2, 25:7",
            "reason": (
                "Homograph: bare חאכם / אלחאכם is the standard judicial-administrative noun for "
                "'(the) judge' across Saadia's tafsir of legal-administrative passages. The "
                "חאכמא TWIST entry is specifically about the CIRCUMSTANTIAL-ACCUSATIVE PARTICIPLE "
                "(حاكمًا with tanwīn) inserted into divine speech-acts to avoid anthropomorphism — "
                "a syntactic-deployment of the participle, not the bare noun usage. The 9 Shemot/"
                "Devarim hits are all bare-noun judicial usages (Ex 21:6 'bring him to the judge'; "
                "Deut 17:9 'go to the priests and to the judge'); the divine-speech-act register "
                "is structurally distinct (see Phase 4 Devarim B1 session notes line 158-160 for "
                "the explicit register-distinction). Vayikra 20:24 IS the divine-speech-act "
                "register attestation and is shipped (see PROMOTE_IN_PLACE above). The judicial-"
                "vocabulary cluster is a candidate for a separate NEW NOTE entry in Phase 4 "
                "Vayikra/Devarim B2 — out-of-scope for promote-in-place R2."
            ),
        },
        # --- homograph: אורד-cluster noun-surfaces
        {
            "lemma": "אורד (noun-surface hits)",
            "verse_hint": "Shemot 25:30 (מוגהא 'presented' showbread); Devarim 23:15, 24:1 (אמרא 'a matter')",
            "reason": (
                "Homograph: the search set for אורד includes variants 'אמרא' and 'מוגהא' (since "
                "the TWIST's mechanism centers on the idiom 'amr muwajjah' = 'directed command'). "
                "The Shemot 25:30 hit (לֶחֶם פָּנִים תָּמִיד = כ'בזא מוגהא בין ידיי דאימא) uses מוגהא "
                "in the NOUN sense 'presented/turned-toward' (the showbread is 'presented' before "
                "the divine presence); the Devarim 23:15 and 24:1 hits use אמרא in the generic "
                "'matter/thing' sense (קביחא = a wicked thing). Neither is the Form-IV dispatch-"
                "verb register of the TWIST; both are unrelated noun usages."
            ),
        },
        # --- borderline: מסלט Shemot 21:8 yet ya-pronoun edge-case (NOT actually a skip — see PROMOTE)
        # (kept in PROMOTE_IN_PLACE as legal-authority extension; no skip line needed)
        # --- duplicate collision: אלממתעה Devarim 23:18 blocked by NOTE entry
        {
            "lemma": "אלממתעה",
            "verse_hint": "Devarim 23:18",
            "reason": (
                "DUPLICATE COLLISION: Phase 4 Devarim Batch 1 (shipped 2026-05-29) created a "
                "separate NOTE entry with lemma_ja=ממתעה covering Deut 23:18 (the cult-prostitute "
                "prohibition). The TWIST entry's mechanism prose ALREADY identifies Deut 23:18 "
                "as the parallel attestation ('uses the same word again at Deuteronomy 23:18, "
                "confirming the systematic identification'), and Blau's prose explicitly cites "
                "both Gen 38:21 and Deut 23:18 together. Adding Deut 23:18 to the TWIST verses[] "
                "would create double-attestation across two entries (TWIST verses[] + NOTE "
                "verses[] both containing Deut 23:18). Per the user's promote-in-place-only "
                "scope decision (no entry add/remove, no tier changes), the consolidation is "
                "out-of-scope. Deferred for a future cleanup pass: the cleanest resolution is "
                "to delete the NOTE entry and add Deut 23:18 to the TWIST verses[], converting "
                "the TWIST into a 2-book entry. Alternative: keep both entries but cross-link "
                "their mechanisms (currently each entry already cross-references the other in "
                "prose)."
            ),
        },
    ],
    "borderline": [
        # מסלט Shemot 21:8 — borderline mechanism-broadening, shipped with caveat
        {
            "lemma": "מסלט",
            "verse_hint": "Shemot 21:8 (Form V יתסלט: 'he has no power to sell her')",
            "open_question": (
                "Form V תسلَّط extends the entry's lexical family from the divine-dominion + "
                "human-vicegerency registers into the legal-authority register. The Heb verb at "
                "21:8 is מָשַׁל ('to rule, have authority'), which Saadia routes through the same "
                "Form V he uses at Gen 4:7 (sin's rule over Cain) and Gen 3:16 (husband's rule "
                "over wife). The lexical-family invariance is clean (same Form V root), but the "
                "mechanism-frame is broader (legal-authority is neither anti-anthropomorphic nor "
                "imago-Dei vicegerency). Shipped in the PROMOTE_IN_PLACE list with mechanism "
                "rewrite explicitly naming the cross-register breadth (theology + vicegerency + "
                "sovereignty + legal-authority). Worth re-evaluating in Phase 3 R3 whether the "
                "entry's TWIST status should be re-anchored on the broader dominion-vocabulary "
                "program rather than on the anti-anthropomorphic imago-Dei core."
            ),
        },
    ],
    "_phase3_r2_outcomes": [
        # Recap of R2 scan results, archived for downstream batches
        "Scanned: 11 priority-cluster TWIST lemmas (אדלג, חאכמא, קאול, תואעד, אלממתעה, שא, גלד, מסלט, עטל, מקררא, אורד).",
        "Promote-in-place ships: 6 entries (אדלג, חאכמא, מסלט, אורד, תואעד, אלממתעה), 19 verse extensions.",
        "Cross-book graduations: אדלג and חאכמא both reach 3-book attestation (Bereshit + Shemot + {Bamidbar / Vayikra}); מסלט reaches 2-book attestation (Bereshit + Shemot).",
        "TWIST 3-book count: was 0; now 2 (the corpus's first TWIST-tier 3-book entries).",
        "TWIST 2-book count: was 2 (חאכמא at Bereshit+Shemot, אדלג at Bereshit+Bamidbar — both now 3-book); now 1 (מסלט at Bereshit+Shemot).",
        "Bereshit-only TWIST count: was 33; now 30 (אדלג, חאכמא, מסלט moved out; אורד, תואעד, אלממתעה remain Bereshit-only but with strengthened intra-Bereshit verse coverage).",
        "Homograph filters: 4 (שא, גלד, חאכם judicial cluster, אורד noun-surfaces) — see skip[] for register-distinction rationale.",
        "Duplicate collision: אלממתעה ↔ ממתעה NOTE entry (Deut 23:18). Surfaced but deferred — out-of-scope for promote-in-place-only.",
        "Borderline: מסלט Shemot 21:8 Form V legal-authority extension shipped with mechanism-broadening caveat.",
        "קאול, עטל, מקררא: no cross-book hits (קאול scan returned a Bereshit-internal homograph at 20:18 but it didn't pass mechanism-fit — see scan output).",
        "Next: Phase 3 R2 Batch 2 — sweep the remaining ~25 Bereshit-only TWIST entries (excluding the 11 Batch 1 priority lemmas) systematically.",
    ],
}


# ============================================================================
# Helpers — mirror scripts/apply_phase4_devarim_batch1.py
# ============================================================================

def _patch_promote_in_place(payload: dict) -> list[dict]:
    """Iterate PROMOTE_IN_PLACE and apply each cross-book extension to its
    target entry. For each item: extend verses[] (dedup on (book, ch, v)),
    extend variants[] (dedup), and rewrite mechanism + blau_dict.sense.
    Returns a list of per-lemma summaries.
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
            if added_v or added_var:
                if "mechanism_rewrite" in spec:
                    entry["mechanism"] = spec["mechanism_rewrite"]
                if "blau_dict_sense_rewrite" in spec:
                    entry.setdefault("blau_dict", {})["sense"] = spec["blau_dict_sense_rewrite"]
                summaries.append({
                    "lemma": target_lemma,
                    "verses_added": added_v,
                    "variants_added": added_var,
                    "total_verses_now": len(entry["verses"]),
                })
            else:
                summaries.append({
                    "lemma": target_lemma,
                    "verses_added": [],
                    "variants_added": [],
                    "note": "all extensions already present (idempotent re-run)",
                })
            break
        else:
            summaries.append({"lemma": target_lemma, "error": "target lemma not found in divergence file"})
    return summaries


def _update_deferred(deferred_path: pathlib.Path) -> dict:
    """Write Phase 3 R2 Batch 1 entries into _blau_saadia_deferred.json under a
    fresh "phase3_r2" namespace (idempotent on lemma+verse_hint pair).
    """
    payload = json.loads(deferred_path.read_text())
    ns = payload.setdefault("phase3_r2", {})
    b1 = ns.setdefault("batch1", {})

    added = {"skip": 0, "borderline": 0}
    for bucket in ("skip", "borderline"):
        new_items = BATCH1_DEFERRED.get(bucket, [])
        existing = b1.setdefault(bucket, [])
        # Idempotency key: (lemma, verse_hint) since R2 deferred items don't carry blau_id
        existing_keys = {(it.get("lemma"), it.get("verse_hint")) for it in existing if isinstance(it, dict)}
        for item in new_items:
            key = (item.get("lemma"), item.get("verse_hint"))
            if key in existing_keys:
                continue
            existing.append(item)
            existing_keys.add(key)
            added[bucket] += 1

    outcomes = b1.setdefault("_phase3_r2_outcomes", [])
    if isinstance(outcomes, list):
        for line in BATCH1_DEFERRED.get("_phase3_r2_outcomes", []):
            if line not in outcomes:
                outcomes.append(line)

    b1.setdefault("_session", "Phase 3 R2 Batch 1 — priority-cluster TWIST sweep (apply_phase3_r2_batch1.py)")

    deferred_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return {
        "added": added,
        "phase3_r2_batch1_buckets_now": {k: len(v) if isinstance(v, list) else v for k, v in b1.items()},
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

    # Promote-in-place patches (no NEW_ENTRIES list — R2 is promote-in-place only)
    promote_summaries = _patch_promote_in_place(payload)

    div_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    json.loads(div_path.read_text())  # parse-check

    deferred_summary = _update_deferred(deferred_path)

    print("=" * 76)
    print("Phase 3 R2 Batch 1 — promote-in-place TWIST sweep, priority clusters")
    print("=" * 76)
    print(f"\nPromote-in-place per-lemma summary:\n{json.dumps(promote_summaries, ensure_ascii=False, indent=2)}")

    n_promoted = sum(1 for s in promote_summaries if s.get("verses_added"))
    n_new_verses = sum(len(s.get("verses_added", [])) for s in promote_summaries)
    print(f"\nPromoted entries: {n_promoted}/{len(PROMOTE_IN_PLACE)}")
    print(f"New verse extensions: {n_new_verses}")
    print(f"Total divergence entries (unchanged): {len(payload['entries'])}")

    tiers = Counter(e.get("tier", "twist") for e in payload["entries"])
    print(f"Tier distribution: {dict(tiers)}")

    print(f"\nDeferred file summary: {json.dumps(deferred_summary, ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    main()

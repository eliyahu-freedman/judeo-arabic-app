"""Generate aligned JSON for bab3 pages קסג–קסח using correct English paragraphs."""
import json, pathlib

OUT = pathlib.Path("data/_bahya_align_work/bab3_out")
OUT.mkdir(parents=True, exist_ok=True)

def w(page_he, segments):
    p = OUT / f"{page_he}.json"
    data = {"pages": {page_he: segments}}
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {p} — {len(segments)} segs")

# ── קסג ──────────────────────────────────────────────────────────────────
# JA: "מנהא ג'מלה כאפיה תדלך עלי באקיהא ועלי אצ'דאדהא. פאד'א כאן עביד..."
# English: paragraphs [135]-[139 partial]

en135 = "As for the matters that are ugly from the slave, they are the contrary of all that his master approves from him; by their opposites things are discriminated. I have gathered for you of them a sum sufficient to indicate to you the rest of them and their opposites."
en136 = "If, then, the slaves of the people of this world should have approved from them, toward their masters, the like of what we have described — and you know the small worth of their blessing before them — how much, then, are you bound toward God (exalted be He) of the like of what we have described, when you have dealt fairly with Him from yourself for the magnitude of His blessing before you?"
en137 = "**The soul says:** I have understood what you have mentioned, and what you have set forth is sufficient. But explain to me upon how many aspects the differential excellence of obedience to God (exalted be He) is incumbent upon me."
en138 = "The intellect says: The differential excellence of obedience over its bearers varies by the way of generality and particularity of blessing toward them. The blessing upon rational beings is of four kinds."
en139 = '**The first kind** of them is God\'s blessing upon all people in general — namely, their being brought into existence after they were not an existing thing; their being made alive; the bestowing of the bounty upon them of the totality whose mention has gone before in the Second Gate of this book. That is why an obedience is incumbent upon them toward God, a general one — namely the totality of the rational laws by which Adam, Enoch, Noah and his sons, Job and his companions ran, until the era of Moses (peace be upon him). Whoever has bound himself to them in their completeness, in obedience to God, God has bestowed upon him a great blessing beyond the rest of the people, and has singled him out by an additional obedience in this world and an abundant reward for it in the next world — like Abraham, to whom God said: "Fear not, Abram, I am a shield to you, your reward shall be exceedingly great" (Genesis 15:1).'

w("קסג", [
    {
        "ja": "מנהא ג'מלה כאפיה תדלך עלי באקיהא ועלי אצ'דאדהא.",
        "en": "I have gathered for you of them a sum sufficient to indicate to you the rest of them and their opposites.",
        "isHeader": False,
        "pairs": [
            {"ja": "ג'מלה כאפיה", "en": "a sum sufficient"},
            {"ja": "תדלך עלי באקיהא", "en": "to indicate to you the rest of them"},
            {"ja": "ועלי אצ'דאדהא", "en": "and their opposites"},
        ]
    },
    {
        "ja": "פאד'א כאן עביד אהל אלדניא יסתחסן מנהם למואליהם מת'ל מא וצפנא, וקד עלמת צגר קדר נעמהם קבלהם, פכם ילזמך ללה תעאלי מן אמת'אל מא וצפנא אד'א אנצפתה מנך עלי עט'ים נעמה קבלך.",
        "en": en136,
        "isHeader": False,
        "pairs": [
            {"ja": "עביד אהל אלדניא", "en": "the slaves of the people of this world"},
            {"ja": "למואליהם", "en": "toward their masters"},
            {"ja": "מת'ל מא וצפנא", "en": "the like of what we have described"},
            {"ja": "וקד עלמת צגר קדר נעמהם קבלהם", "en": "you know the small worth of their blessing before them"},
            {"ja": "פכם ילזמך ללה תעאלי", "en": "how much, then, are you bound toward God (exalted be He)"},
            {"ja": "אד'א אנצפתה מנך עלי עט'ים נעמה קבלך", "en": "when you have dealt fairly with Him from yourself for the magnitude of His blessing before you"},
        ]
    },
    {
        "ja": "פצל. ו.",
        "en": "Section Six.",
        "isHeader": True,
        "pairs": []
    },
    {
        "ja": "קאלת אלנפס, קד פהמת מא ד'כרתה ופי מא שרחת כפאיה. לכן ביין לי עלי כם וג'ה ילזמני תפאצ'ל אלטאעה ללה תעאלי.",
        "en": "The soul says: I have understood what you have mentioned, and what you have set forth is sufficient. But explain to me upon how many aspects the differential excellence of obedience to God (exalted be He) is incumbent upon me.",
        "isHeader": False,
        "pairs": [
            {"ja": "קאלת אלנפס", "en": "The soul says"},
            {"ja": "קד פהמת מא ד'כרתה", "en": "I have understood what you have mentioned"},
            {"ja": "ופי מא שרחת כפאיה", "en": "what you have set forth is sufficient"},
            {"ja": "ביין לי עלי כם וג'ה", "en": "explain to me upon how many aspects"},
            {"ja": "ילזמני תפאצ'ל אלטאעה ללה תעאלי", "en": "the differential excellence of obedience to God (exalted be He) is incumbent upon me"},
        ]
    },
    {
        "ja": "קאל אלעקל, אן תפאצ'ל אלטאעה עלי אהלהא יכ'תלף מן טריק אלעמום ואלכ'צוץ ללנעמה עליהם, ואלנעמה עלי אלנאטקין עלי ארבעה צ'רוב.",
        "en": "The intellect says: The differential excellence of obedience over its bearers varies by the way of generality and particularity of blessing toward them. The blessing upon rational beings is of four kinds.",
        "isHeader": False,
        "pairs": [
            {"ja": "קאל אלעקל", "en": "The intellect says"},
            {"ja": "תפאצ'ל אלטאעה עלי אהלהא יכ'תלף", "en": "The differential excellence of obedience over its bearers varies"},
            {"ja": "מן טריק אלעמום ואלכ'צוץ", "en": "by the way of generality and particularity"},
            {"ja": "ללנעמה עליהם", "en": "of blessing toward them"},
            {"ja": "אלנעמה עלי אלנאטקין עלי ארבעה צ'רוב", "en": "The blessing upon rational beings is of four kinds"},
        ]
    },
    {
        "ja": "אלצ'רב אלאול מנהא, נעמהֵ אללה עלי ג'מיע אלנאס עאמה, והי איג'אדהם בעד אן לם יכונוא שיא מוג'ודא, ואחיאהם, ואלתפצ'ל עליהם בג'מלהֵ מא תקדם ד'כרה פי אלבאב אלת'אני מן הד'א אלכתאב, ולד'לך תלזמהם ללה ענהא טאעה עאמה והי ג'מלהֵ אלשראיע אלעקליה אלתי ג'רי עליהא אדם וחנוך ונח ובנוה ואיוב ואצחאבה אלי עהד מוסי ע\"ס, פמן אלתזמהא עלי כמאלהא טאעה ללה תפצ'ל אללה עליה בנעמה ג'זילה דון סאיר אלנאס, וכ'צה בטאעה זאידה פי אלדניא וג'זיל אלת'ואב ענהא פי אלאכ'רה, מת'ל אברהם אלד'י קאל אללה לה אל תירא אברם אנכי מגן לך",
        "en": '**The first kind** of them is God\'s blessing upon all people in general — namely, their being brought into existence after they were not an existing thing; their being made alive; the bestowing of the bounty upon them of the totality whose mention has gone before in the Second Gate of this book. That is why an obedience is incumbent upon them toward God, a general one — namely the totality of the rational laws by which Adam, Enoch, Noah and his sons, Job and his companions ran, until the era of Moses (peace be upon him). Whoever has bound himself to them in their completeness, in obedience to God, God has bestowed upon him a great blessing beyond the rest of the people, and has singled him out by an additional obedience in this world and an abundant reward for it in the next world — like Abraham, to whom God said: "Fear not, Abram, I am a shield to you,',
        "isHeader": False,
        "pairs": [
            {"ja": "אלצ'רב אלאול מנהא", "en": "**The first kind** of them"},
            {"ja": "נעמהֵ אללה עלי ג'מיע אלנאס עאמה", "en": "is God's blessing upon all people in general"},
            {"ja": "איג'אדהם בעד אן לם יכונוא שיא מוג'ודא", "en": "their being brought into existence after they were not an existing thing"},
            {"ja": "ואחיאהם", "en": "their being made alive"},
            {"ja": "ולד'לך תלזמהם ללה ענהא טאעה עאמה", "en": "That is why an obedience is incumbent upon them toward God, a general one"},
            {"ja": "ג'מלהֵ אלשראיע אלעקליה", "en": "the totality of the rational laws"},
            {"ja": "פמן אלתזמהא עלי כמאלהא טאעה ללה", "en": "Whoever has bound himself to them in their completeness, in obedience to God"},
            {"ja": "תפצ'ל אללה עליה בנעמה ג'זילה דון סאיר אלנאס", "en": "God has bestowed upon him a great blessing beyond the rest of the people"},
            {"ja": "מת'ל אברהם", "en": "like Abraham"},
            {"ja": "אל תירא אברם אנכי מגן לך", "en": "Fear not, Abram, I am a shield to you,"},
        ]
    },
])

# ── קסד ──────────────────────────────────────────────────────────────────
en139_end = 'your reward shall be exceedingly great" (Genesis 15:1).'
en140 = 'Whoever has disobeyed God in His blessing has fallen from the rank of the rational beings and their excellences to the bottom of the rank of the non-rational animal, and his judgment in this world was the judgment of brutes, as he said: "The enemies of the Lord shall be as the prizing of the lambs" (Psalms 37:20); and his judgment in the next world is the greatest of affliction, as He said: "Your breath is a fire that will consume you" (Isaiah 33:11).'
en141 = '**The second kind**: God\'s blessing upon a tribe among the tribes and a nation among the nations — such as what He bestowed upon the Children of Israel in their being brought out of Egypt and their being brought into the lands of Syria. The Maker (exalted be He) bound them, for this, to an obedience added upon the first obedience — namely, the heard-revealed laws — after His emphatic confirmation of the rational laws and His awakening upon them. Whoever bound himself to them for the sake of God (exalted be He), God singled him out by a blessing for which He bound him to an obedience besides the obedience of his nation and the rest of his tribe — such as we find with the tribe of Levi, when Moses (peace be upon him) said: "Whoever is for the Lord, to me!" and all the sons of Levi gathered to him (Exodus 32:26). God preferred them by an abundant blessing, and singled out from them, for the service of the place of His light, Aaron and his sons, and commanded them with laws added upon the rest of the community — and with the abundant reward of the next world. Whoever of them disobeyed God fell from the two ranks and was punished in both houses, as the Wise One said: "And it shall not be well with the wicked, nor shall he prolong his days, like a shadow which is no shadow, because he does not fear before God" (Ecclesiastes 8:13).'
en142_start = '**The third kind**: God\'s blessing upon a clan from among the clans of the nation — such as the priests and the Levites and the seed of kingship — I mean the House of David (peace be upon him) — and His having bound them, accordingly, to obediences. As for the laws of the priesthood and the Levitical service, they are known and clear in the Book of God. As for the laws of the House of David: the Book\'s saying — "O House of David, thus said the Lord: judge justly in the morning, and deliver the despoiled from the hand of the oppressor"'

w("קסד", [
    {
        "ja": 'שכרך הרבה מאד.',
        "en": 'your reward shall be exceedingly great" (Genesis 15:1).',
        "isHeader": False,
        "pairs": [
            {"ja": "שכרך הרבה מאד", "en": "your reward shall be exceedingly great"},
        ]
    },
    {
        "ja": "פמן עצי אללה בנעמתה סקט מן דרג'הֵ אלנאטקין ופצ'אילהם אלי אספל דרג'הֵ אלחיואן גיר אלנאטק, פכאן חכמה חכם אלבהאים פי אלדניא כקולה ואויבי ה' כיקר כרים, וחכמה פי אלאכ'רה אעט'ם אלבלא כקולה רוחכם אש תאכלכם.",
        "en": en140,
        "isHeader": False,
        "pairs": [
            {"ja": "פמן עצי אללה בנעמתה", "en": "Whoever has disobeyed God in His blessing"},
            {"ja": "סקט מן דרג'הֵ אלנאטקין ופצ'אילהם", "en": "has fallen from the rank of the rational beings and their excellences"},
            {"ja": "אלי אספל דרג'הֵ אלחיואן גיר אלנאטק", "en": "to the bottom of the rank of the non-rational animal"},
            {"ja": "פכאן חכמה חכם אלבהאים פי אלדניא", "en": "and his judgment in this world was the judgment of brutes"},
            {"ja": "וחכמה פי אלאכ'רה אעט'ם אלבלא", "en": "his judgment in the next world is the greatest of affliction"},
        ]
    },
    {
        "ja": "ואלצ'רב אלת'אני נעמהֵ אללה עלי קבילה מן אלקבאיל ואמה מן אלאמם, נחו מא אנעם עלי בני אסראיל פי אכ'ראג'הם מן מצר ואדכ'אלהם בלאד אלשאם, פאלזמהם אלבארי תעאלי עליהא טאעה זאידה עלי אלטאעה אלאולי והי אלשראיע אלסמעיה, בעד תאכידה ותנביהה עלי אלשראיע אלעקליה. פמן אלתזמהא לד'את אללה תעאלי כ'צה אללה בנעמה ילזמה עליהא טאעה סוי טאעהֵ אמתה וסאיר קבילתה, מת'ל מא וג'דנא שבט לוי אד' קאל משה ע\"ס מי לה' אלי ויאספו אליו כל בני לוי, פפצ'להם אללה בנעמה סאבגה, ואכ'תץ מנהם לכ'דמהֵ מחל נורה אהרן ובניה, ואמרהם בשראיע זאידה דון סאיר אלאמה, ובג'זיל ת'ואב אלאכ'רה. ומן עצי אללה מנהם סקט ען אלמרתבתין, ועוקב פי אלדארין, כקול אלחכים וטוב לא יהיה לרשע ולא יאריך ימים כצל אשר איננו ירא מלפני אלהים.",
        "en": en141,
        "isHeader": False,
        "pairs": [
            {"ja": "ואלצ'רב אלת'אני", "en": "**The second kind**"},
            {"ja": "נעמהֵ אללה עלי קבילה מן אלקבאיל ואמה מן אלאמם", "en": "God's blessing upon a tribe among the tribes and a nation among the nations"},
            {"ja": "נחו מא אנעם עלי בני אסראיל פי אכ'ראג'הם מן מצר", "en": "such as what He bestowed upon the Children of Israel in their being brought out of Egypt"},
            {"ja": "פאלזמהם אלבארי תעאלי עליהא טאעה זאידה עלי אלטאעה אלאולי", "en": "The Maker (exalted be He) bound them, for this, to an obedience added upon the first obedience"},
            {"ja": "והי אלשראיע אלסמעיה", "en": "namely, the heard-revealed laws"},
            {"ja": "שבט לוי", "en": "the tribe of Levi"},
            {"ja": "פפצ'להם אללה בנעמה סאבגה", "en": "God preferred them by an abundant blessing"},
            {"ja": "ואכ'תץ מנהם לכ'דמהֵ מחל נורה אהרן ובניה", "en": "singled out from them, for the service of the place of His light, Aaron and his sons"},
            {"ja": "ומן עצי אללה מנהם סקט ען אלמרתבתין", "en": "Whoever of them disobeyed God fell from the two ranks"},
            {"ja": "ועוקב פי אלדארין", "en": "and was punished in both houses"},
        ]
    },
    {
        "ja": "ואלצ'רב אלת'אלת', נעמהֵ אללה עלי עשירה מן ג'מלהֵ עשאיר אלאמה מת'ל אלכהנה ואללויה וזרע המלוכה אעני בית דוד ע\"ס, ואלזאמהם חסב ד'לך טאעאת. ואמא שראיע אלכהונה ואללויה פמעלומה ביינה פי כתאב אללה. ואמא שראיע בית דוד פקול אלכתאב בית דוד כה אמר ה' דינו לבקר משפט והצילו",
        "en": '**The third kind**: God\'s blessing upon a clan from among the clans of the nation — such as the priests and the Levites and the seed of kingship — I mean the House of David (peace be upon him) — and His having bound them, accordingly, to obediences. As for the laws of the priesthood and the Levitical service, they are known and clear in the Book of God. As for the laws of the House of David: the Book\'s saying — "O House of David, thus said the Lord: judge justly in the morning, and deliver the despoiled from the hand of the oppressor"',
        "isHeader": False,
        "pairs": [
            {"ja": "ואלצ'רב אלת'אלת'", "en": "**The third kind**"},
            {"ja": "נעמהֵ אללה עלי עשירה מן ג'מלהֵ עשאיר אלאמה", "en": "God's blessing upon a clan from among the clans of the nation"},
            {"ja": "מת'ל אלכהנה ואללויה וזרע המלוכה", "en": "such as the priests and the Levites and the seed of kingship"},
            {"ja": "אעני בית דוד", "en": "I mean the House of David"},
            {"ja": "שראיע אלכהונה ואללויה פמעלומה ביינה פי כתאב אללה", "en": "the laws of the priesthood and the Levitical service, they are known and clear in the Book of God"},
            {"ja": "שראיע בית דוד", "en": "the laws of the House of David"},
        ]
    },
])

# ── קסה ──────────────────────────────────────────────────────────────────
en142_rest = 'Whoever has perfected them, seeking the satisfaction of God, God has singled him out by a blessing in this world and an abundant reward in the next world. He becomes a chosen prophet, or a guided friend [of God], as the Book said concerning Pinhas: "Then Pinhas stood up and executed judgment, and the plague was stayed; and it was counted to him for righteousness, from generation to generation, forever" (Psalms 106:30–31), and He said: "The priests, the Levites, the sons of Zadok, who kept the charge of My sanctuary when the children of Israel went astray from Me — they shall draw near to Me to serve Me" (Ezekiel 44:15). Whoever of them disobeyed God by it fell from the totality of the high ranks in this world and obtained painful torment in the next world, as you have come to know from the case of Korah and his followers.'
en143 = '**The fourth kind**: God\'s blessing upon a person among the persons of the people, special to him beyond the rest of his clan and his tribe and the rest of the rational beings — such as a chosen prophet, or a friend [of God] appointed as successor for the management of the nation, or a wise man inspired with knowledge, understanding, and counsel, and the like. For every blessing among these, an additional obedience to God (mighty and exalted) is incumbent upon him.'
en144 = 'Whoever has rendered them up — for him is the perpetuity of the totality of the general and particular blessings in this world, and God adds to him strength for it and insight into it — as He said: "The Lord has sworn to David in truth, He will not turn back from it: \'Of the fruit of your body I will set upon your throne; if your sons keep My covenant and My testimony that I will teach them, their sons also forever shall sit upon your throne\'" (Psalms 132:11–12). And the abundant reward in the next world, as the Friend said: "If I had not believed to see the goodness of the Lord in the land of the living!" (Psalms 27:13).'
en145 = 'Whoever has disobeyed God in the blessing with which He singled him out has fallen from the totality of the excellences; the reckoning upon him is the more severe in this world, as He said: "This is what the Lord has spoken, saying: \'I will be sanctified through those near to Me, and before all the people I will be honored\'; and Aaron held his peace" (Leviticus 10:3), and He said: "Only you have I known of all the families of the earth; therefore I will visit upon you all your iniquities" (Amos 3:2). The punishment upon him in the next world is the more emphatic, as He said: "For Tophet is ordained of old, indeed for the king it is prepared" (Isaiah 30:33).'

w("קסה", [
    {
        "ja": "גזול מיד עושק.",
        "en": 'deliver the despoiled from the hand of the oppressor"',
        "isHeader": False,
        "pairs": [
            {"ja": "גזול מיד עושק", "en": "deliver the despoiled from the hand of the oppressor"},
        ]
    },
    {
        "ja": "פמן אסתכמלהא אבתגא רצ'א אללה כ'צה אללה בנעמה פי אלדניא וג'זיל אלת'ואב פי אלאכ'רה, פיכון נביא מצטפי או וליא מרשדא, כקול אלכתאב ען פינחס ויעמד פינחס ויפלל ותעצר המגפה ותחשב לו לצדקה לדור ודור עד עולם, וקאל והכהנים הלוים בני צדוק אשר שמרו את משמרת מקדשי בתעות בני ישראל מעלי המה יקרבו אלי לשרתני. ומן עצי אללה בהא סקט מן ג'מלהֵ אלמראתב אלעליא פי אלדניא וחצל עלי עד'אב אלים פי אלאכ'רה, כמא עלמת מן קצהֵ קרח ותאבעיה.",
        "en": en142_rest,
        "isHeader": False,
        "pairs": [
            {"ja": "פמן אסתכמלהא אבתגא רצ'א אללה", "en": "Whoever has perfected them, seeking the satisfaction of God"},
            {"ja": "כ'צה אללה בנעמה פי אלדניא", "en": "God has singled him out by a blessing in this world"},
            {"ja": "וג'זיל אלת'ואב פי אלאכ'רה", "en": "an abundant reward in the next world"},
            {"ja": "פיכון נביא מצטפי", "en": "He becomes a chosen prophet"},
            {"ja": "או וליא מרשדא", "en": "or a guided friend [of God]"},
            {"ja": "ומן עצי אללה בהא", "en": "Whoever of them disobeyed God by it"},
            {"ja": "סקט מן ג'מלהֵ אלמראתב אלעליא פי אלדניא", "en": "fell from the totality of the high ranks in this world"},
            {"ja": "וחצל עלי עד'אב אלים פי אלאכ'רה", "en": "obtained painful torment in the next world"},
            {"ja": "קצהֵ קרח ותאבעיה", "en": "the case of Korah and his followers"},
        ]
    },
    {
        "ja": "ואלצ'רב אלראבע, נעמהֵ אללה עלי שכ'ץ מן אשכ'אץ אלנאס מכ'צוץ בהא דון סאיר עשירתה וקבילתה וסאיר אלנאטקין, מת'ל נבי מצטפי או ולי מסתכ'לף לתדביר אלאמה, או חכים מלהם אלעלם ואלפהם ואלארי, ומא אשבה ד'לך. פעלי כל נעמה מנהא ילזמה טאעה זאידה ללה ג'ל ועז,",
        "en": en143,
        "isHeader": False,
        "pairs": [
            {"ja": "ואלצ'רב אלראבע", "en": "**The fourth kind**"},
            {"ja": "נעמהֵ אללה עלי שכ'ץ מן אשכ'אץ אלנאס", "en": "God's blessing upon a person among the persons of the people"},
            {"ja": "מכ'צוץ בהא דון סאיר עשירתה וקבילתה וסאיר אלנאטקין", "en": "special to him beyond the rest of his clan and his tribe and the rest of the rational beings"},
            {"ja": "מת'ל נבי מצטפי", "en": "such as a chosen prophet"},
            {"ja": "או ולי מסתכ'לף לתדביר אלאמה", "en": "or a friend [of God] appointed as successor for the management of the nation"},
            {"ja": "או חכים מלהם אלעלם ואלפהם ואלארי", "en": "or a wise man inspired with knowledge, understanding, and counsel"},
            {"ja": "פעלי כל נעמה מנהא ילזמה טאעה זאידה ללה ג'ל ועז", "en": "For every blessing among these, an additional obedience to God (mighty and exalted) is incumbent upon him"},
        ]
    },
    {
        "ja": "פמן ופאהא דאמהֵ לה ג'מלהֵ אלנעם אלעאמה ואלכ'אצה פי אלדניא, וזאדה אללה קוה עליהא ובצירה פיהא, כקולה נשבע ה' לדוד אמת לא ישוב ממנה מפרי בטנך אשית לכסא לך אם ישמרו בניך בריתי ועדותי זו אלמדם גם בניהם עדי עד ישבו לכסא לך. וג'זיל אלת'ואב פי אלאכ'רה כקול אלולי ע\"ס לולי האמנתי לראות בטוב ה' בארץ חיים.",
        "en": en144,
        "isHeader": False,
        "pairs": [
            {"ja": "פמן ופאהא", "en": "Whoever has rendered them up"},
            {"ja": "דאמהֵ לה ג'מלהֵ אלנעם אלעאמה ואלכ'אצה פי אלדניא", "en": "for him is the perpetuity of the totality of the general and particular blessings in this world"},
            {"ja": "וזאדה אללה קוה עליהא ובצירה פיהא", "en": "God adds to him strength for it and insight into it"},
            {"ja": "וג'זיל אלת'ואב פי אלאכ'רה", "en": "And the abundant reward in the next world"},
        ]
    },
    {
        "ja": "ומן עצי אללה באלנעמה אלתי כ'צה בהא סקט ען ג'מלהֵ אלפצ'איל, וכאן אלחסאב עליה אשד תקץ פי אלדניא כקולה הוא אשר דבר ה' לאמר בקרובי אקדש ועל פני כל העם אכבד וידם אהרן, וקאל רק אתכם ידעתי מכל משפחות האדמה על כן אפקד עליכם את כל עונותיכם. וכאן אלעקאב עליה פי אלאכ'רה אבלג כקולה כי ערוך מאתמול תפתה גם הוא למלך הוכן.",
        "en": en145,
        "isHeader": False,
        "pairs": [
            {"ja": "ומן עצי אללה באלנעמה אלתי כ'צה בהא", "en": "Whoever has disobeyed God in the blessing with which He singled him out"},
            {"ja": "סקט ען ג'מלהֵ אלפצ'איל", "en": "has fallen from the totality of the excellences"},
            {"ja": "וכאן אלחסאב עליה אשד תקץ פי אלדניא", "en": "the reckoning upon him is the more severe in this world"},
            {"ja": "וכאן אלעקאב עליה פי אלאכ'רה אבלג", "en": "The punishment upon him in the next world is the more emphatic"},
        ]
    },
])

# ── קסו ──────────────────────────────────────────────────────────────────
en146 = 'By these four kinds, obedience to God is incumbent upon the people. For every blessing God adds upon the human, an obedience for it is incumbent. The evidence for this is that the tithes attach to grain-products, as it is said: "You shall tithe diligently all the produce of your seed" (Deuteronomy 14:22). Whoever God has blessed with a hundred *mudd* of food owes from it ten *mudd* to God; whoever God has blessed with ten *mudd* owes to God a single *mudd*. If the first surrenders to God nine-and-a-half *mudd* and the second surrenders to God a single complete *mudd*, the first deserves the punishment and the second the reward.'
en147 = 'Likewise the speech concerning one who has not been granted a child: the obligations of his circumcision and teaching him the Book of God fall from him. So too whoever is lame — the obligations of pilgrimage fall from him; whoever is sick — there fall from him among the commands of the Law what he has no capacity for. By this analogy, whoever God has singled out by an added blessing is bound by an added obedience and worship in thanksgiving for it.'
en148 = 'That is why the most excellent of the early ones used to fear when a blessing among God\'s blessings in this world came upon them, and would dread it on two grounds: **first**, fear of falling short in rendering up the obedience for it and thanksgiving for it, so that it might become a burden upon them in the next world, as the Friend said: "I have become small by reason of all the kindnesses and all the truth You have done to Your servant" (Genesis 32:11). **And the second ground:** wariness lest [their blessing] be God\'s recompense (exalted be He) for their obedience to Him, so that thereby the reward of their works would be diminished at the return, as the early ones explained "[He] requites those who hate Him to His face, to destroy them" — and in this is sufficiency for you.'
en149 = '**The soul says:** I have understood what you have mentioned. I do not find myself able to render up the rights of God for the general blessing toward the rational beings, much less for what He has singled me out from it. Even if there is in me eagerness and zeal for the performance of an obligation for it, what occurs to my imagination first at the time of its execution is the hope of new blessings from Him; likewise in my thanksgiving to God when I thank Him: I thank Him with my expression for the great blessing He has bestowed upon me, but my care and intent in thanksgiving is the calling-forth of the continuity of the blessing and the increase from it — not the renunciation of increase or perpetuity. If I am at the like of this in my obedience and my thanksgiving to God (exalted be He), out of paucity of purification toward the right of His blessing, what road have I to rendering up the rest of my obedience for the particularities of His blessing upon me? Guide me, then, to the minimum that is binding upon me of obedience to God for it, by which I may earn the perpetuity of it.'

w("קסו", [
    {
        "ja": "כעלי הד'ה אלצ'רוב אלארבעה ילזם אלנאס טאעהֵ אללה, כל מא זאד אללה עלי אלאנסאן נעמה לזמה עליהא טאעה. ומן אלדליל עלי ד'לך אן אלמעשרות תלזם אלגלאת כקולה עשר תעשר את כל תבואת זרעך, פמן אנעם אללה עליה במאיהֵ מדי מן טעאם לזמה מנהא עשרה אמדא ללה, ומן אנעם אללה עליה בעשרה אמדא לזמה ללה מנהא מדי ואחד. פאן אכ'רג' אלאוול ללה תסעה אמדא ונצף ואכ'רג' אלאכ'ר ללה מדיא ואחדא כאמלא כאן אלאוול מסתוג'ב אלעקאב ואלת'אני מסתוג'ב אלת'ואב.",
        "en": en146,
        "isHeader": False,
        "pairs": [
            {"ja": "כעלי הד'ה אלצ'רוב אלארבעה", "en": "By these four kinds"},
            {"ja": "ילזם אלנאס טאעהֵ אללה", "en": "obedience to God is incumbent upon the people"},
            {"ja": "כל מא זאד אללה עלי אלאנסאן נעמה לזמה עליהא טאעה", "en": "For every blessing God adds upon the human, an obedience for it is incumbent"},
            {"ja": "אלמעשרות תלזם אלגלאת", "en": "the tithes attach to grain-products"},
            {"ja": "פמן אנעם אללה עליה במאיהֵ מדי מן טעאם לזמה מנהא עשרה אמדא ללה", "en": "Whoever God has blessed with a hundred *mudd* of food owes from it ten *mudd* to God"},
            {"ja": "כאן אלאוול מסתוג'ב אלעקאב ואלת'אני מסתוג'ב אלת'ואב", "en": "the first deserves the punishment and the second the reward"},
        ]
    },
    {
        "ja": "וכד'לך אלקול פי מן לם ירזק ולדא סקט ענה לואזם אלמילה פיה ותעלימה כתאב אללה, וכד'לך מן כאן בה ערג' סקט ענה לואזם אלחג', ומן כאן מריצ'א סקטת ענה מן אואמר אלשריעה מא לא טאקה לה בהא, ועלי הד'א אלקיאס ילזם מן כ'צה אללה בנעמה זאידה אן תלזמה טאעה ועבאדה שכרא עליהא.",
        "en": en147,
        "isHeader": False,
        "pairs": [
            {"ja": "מן לם ירזק ולדא סקט ענה לואזם אלמילה", "en": "one who has not been granted a child: the obligations of his circumcision"},
            {"ja": "מן כאן בה ערג' סקט ענה לואזם אלחג'", "en": "whoever is lame — the obligations of pilgrimage fall from him"},
            {"ja": "ומן כאן מריצ'א סקטת ענה מן אואמר אלשריעה מא לא טאקה לה בהא", "en": "whoever is sick — there fall from him among the commands of the Law what he has no capacity for"},
            {"ja": "ועלי הד'א אלקיאס", "en": "By this analogy"},
            {"ja": "ילזם מן כ'צה אללה בנעמה זאידה אן תלזמה טאעה ועבאדה", "en": "whoever God has singled out by an added blessing is bound by an added obedience and worship"},
        ]
    },
    {
        "ja": "ולד'לך כאן אפאצ'ל אלאואיל יכ'אפון אד'א ורדת עליהם נעמה מן נעם אללה פי אלדניא ויפזעון מנהא לוג'הין, אחדהמא כ'וף אלתקציר פי תופיהֵ אלטאעה ענהא ואלשכר עליהא, פתכון ובאלא עליהם פי אלאכ'רה, כקול אלולי קטנתי מכל החסדים ומכל האמת אשר עשית את עבדך. ואלוג'ה אלת'אני חד'רא אן תכון מכאפאהֵ אללה תעאלי להם עלי טאעתהם לה פינקץ בד'לך ת'ואב אעמאלהם פי אלמעאד, כמא פסר אלאואיל ומשלם לשונאיו אל פניו להאבידו, ופי הד'א כפאיה לך.",
        "en": en148,
        "isHeader": False,
        "pairs": [
            {"ja": "כאן אפאצ'ל אלאואיל יכ'אפון", "en": "the most excellent of the early ones used to fear"},
            {"ja": "אד'א ורדת עליהם נעמה מן נעם אללה פי אלדניא", "en": "when a blessing among God's blessings in this world came upon them"},
            {"ja": "ויפזעון מנהא לוג'הין", "en": "would dread it on two grounds"},
            {"ja": "אחדהמא כ'וף אלתקציר פי תופיהֵ אלטאעה ענהא", "en": "**first**, fear of falling short in rendering up the obedience for it"},
            {"ja": "פתכון ובאלא עליהם פי אלאכ'רה", "en": "it might become a burden upon them in the next world"},
            {"ja": "ואלוג'ה אלת'אני", "en": "**And the second ground:**"},
            {"ja": "חד'רא אן תכון מכאפאהֵ אללה תעאלי להם עלי טאעתהם", "en": "wariness lest [their blessing] be God's recompense (exalted be He) for their obedience to Him"},
            {"ja": "פינקץ בד'לך ת'ואב אעמאלהם פי אלמעאד", "en": "the reward of their works would be diminished at the return"},
        ]
    },
    {
        "ja": "קאלת אלנפס קד פהמת מא ד'כרת, ומא אג'דני קאדרה עלי תופיהֵ חקוק אללה עלי אלנעמה אלשאמלה ללנאטקין פצ'לא עלי מא כ'צני בה מנהא, ואן כאן מני חרץ ונשאט עלי",
        "en": "**The soul says:** I have understood what you have mentioned. I do not find myself able to render up the rights of God for the general blessing toward the rational beings, much less for what He has singled me out from it. Even if there is in me eagerness and zeal for",
        "isHeader": False,
        "pairs": [
            {"ja": "קאלת אלנפס", "en": "**The soul says:**"},
            {"ja": "קד פהמת מא ד'כרת", "en": "I have understood what you have mentioned"},
            {"ja": "ומא אג'דני קאדרה עלי תופיהֵ חקוק אללה", "en": "I do not find myself able to render up the rights of God"},
            {"ja": "עלי אלנעמה אלשאמלה ללנאטקין", "en": "for the general blessing toward the rational beings"},
            {"ja": "פצ'לא עלי מא כ'צני בה מנהא", "en": "much less for what He has singled me out from it"},
            {"ja": "ואן כאן מני חרץ ונשאט עלי", "en": "Even if there is in me eagerness and zeal for"},
        ]
    },
])

# ── קסז ──────────────────────────────────────────────────────────────────
# JA starts with continuation of soul's speech from קסו, then intellect replies
en149_cont = "the performance of an obligation for it, what occurs to my imagination first at the time of its execution is the hope of new blessings from Him; likewise in my thanksgiving to God when I thank Him: I thank Him with my expression for the great blessing He has bestowed upon me, but my care and intent in thanksgiving is the calling-forth of the continuity of the blessing and the increase from it — not the renunciation of increase or perpetuity. If I am at the like of this in my obedience and my thanksgiving to God (exalted be He), out of paucity of purification toward the right of His blessing, what road have I to rendering up the rest of my obedience for the particularities of His blessing upon me? Guide me, then, to the minimum that is binding upon me of obedience to God for it, by which I may earn the perpetuity of it."
en150 = "The intellect says: As for what you have complained of, of the paucity of your purification in your obedience and your thanksgiving to your Lord, and that your expression is the expression of one who gives thanks but your intent in it the intent of one craving, and that within your inward is the increase from the blessing and the desire for its perpetuity — this is for three failings. **The first** is the intensity of your love for yourself and your eagerness to draw the blessings to her; you do not move a foot toward obedience to God or to obedience of anyone other than Him except that your intent is the enjoyment by pleasures. I have set down for you at the beginning of my treatment of you that you should strive with all your effort in the rejection of this blameworthy trait from yourself; by that I hope for the setting-right of you. **The second failing** — your ignorance of the bounty of the Creator (exalted be He) upon you, so that it falls to your imagination that you will not reach His blessing except by craving it from Him. He has already bestowed bounty upon you of what is in your knowledge and of what is not in your knowledge — and you do not consider the desire of the one who first did this for you. Would you not — had you repelled this imagination from yourself — have purified your obedience and your thanksgiving to Him in your inward, and would not what you hope for have become more emphatic and more obligatory for you on account of this?"

w("קסז", [
    {
        "ja": "אדא פריצ'ה ענהא אנמא יסבק אלי והמי ענד תנפיד'הא רג'א נעמה מסתאנפה מנה, וכד'לך פי שכרי ללה אד'א שכרתה אנמא אשכרה בלפט'י עלי עט'ים מא אנעם עליי, והמתי וגרצ'י פי אלשכר אסתדעא אלדואם ללנעמה ואלזיאדה מנהא, לא אליאס ען זיאדהֵ אלנעמה ודואמהא, פאד'א כנת עלי מת'ל הד'א פי טאעתי ושכרי ללה תעאלי מן קלהֵ אלאכ'לאץ לחק נעמתה, כיף אלסביל לי אלי תופיהֵ סאיר טאעתה עלי כ'צוציאת נעמה עליי, פארשדני אלי אקל מא ילזמני מן אלטאעה ללה עליהא אלתי אסתוג'ב בהא דואמהא.",
        "en": en149_cont,
        "isHeader": False,
        "pairs": [
            {"ja": "אנמא יסבק אלי והמי ענד תנפיד'הא רג'א נעמה מסתאנפה מנה", "en": "what occurs to my imagination first at the time of its execution is the hope of new blessings from Him"},
            {"ja": "אנמא אשכרה בלפט'י עלי עט'ים מא אנעם עליי", "en": "I thank Him with my expression for the great blessing He has bestowed upon me"},
            {"ja": "והמתי וגרצ'י פי אלשכר אסתדעא אלדואם ללנעמה ואלזיאדה מנהא", "en": "my care and intent in thanksgiving is the calling-forth of the continuity of the blessing and the increase from it"},
            {"ja": "לא אליאס ען זיאדהֵ אלנעמה ודואמהא", "en": "not the renunciation of increase or perpetuity"},
            {"ja": "מן קלהֵ אלאכ'לאץ לחק נעמתה", "en": "out of paucity of purification toward the right of His blessing"},
            {"ja": "פארשדני אלי אקל מא ילזמני מן אלטאעה ללה עליהא אלתי אסתוג'ב בהא דואמהא", "en": "Guide me, then, to the minimum that is binding upon me of obedience to God for it, by which I may earn the perpetuity of it"},
        ]
    },
    {
        "ja": "קאל אלעקל, אמא מא שכותה מן קלהֵ אכ'לאצך פי טאעתך ושכרך לרבך, ואן לפט'ך לפט' שאכר וקצדך פיה קצד ראגב, ואן פי צ'מירך אלאזדיאד מן אלנעמה ואלרגבה פי דואמהא, פלת'לאת' כ'לאל.",
        "en": "The intellect says: As for what you have complained of, of the paucity of your purification in your obedience and your thanksgiving to your Lord, and that your expression is the expression of one who gives thanks but your intent in it the intent of one craving, and that within your inward is the increase from the blessing and the desire for its perpetuity — this is for three failings.",
        "isHeader": False,
        "pairs": [
            {"ja": "קאל אלעקל", "en": "The intellect says"},
            {"ja": "אמא מא שכותה מן קלהֵ אכ'לאצך פי טאעתך ושכרך לרבך", "en": "As for what you have complained of, of the paucity of your purification in your obedience and your thanksgiving to your Lord"},
            {"ja": "לפט'ך לפט' שאכר וקצדך פיה קצד ראגב", "en": "your expression is the expression of one who gives thanks but your intent in it the intent of one craving"},
            {"ja": "ואן פי צ'מירך אלאזדיאד מן אלנעמה ואלרגבה פי דואמהא", "en": "within your inward is the increase from the blessing and the desire for its perpetuity"},
            {"ja": "פלת'לאת' כ'לאל", "en": "this is for three failings"},
        ]
    },
    {
        "ja": "אחדהא, שדהֵ מחבתך לנפסך וחרצך עלי אסתג'לאב אלנעם אליהא, פלא תנקלין קדמא אלי טאעהֵ אללה ואלי טאעהֵ גירה אלא וגרצ'ך אלתנעם באללד'את, וקד קדמת לך פי אוול עלאג'י לך אן תסעי בג'הדך פי נפי הד'א אלכ'לק אלמד'מום ענך, פבד'לך ארג'ו אלאצלאח לך.",
        "en": "**The first** is the intensity of your love for yourself and your eagerness to draw the blessings to her; you do not move a foot toward obedience to God or to obedience of anyone other than Him except that your intent is the enjoyment by pleasures. I have set down for you at the beginning of my treatment of you that you should strive with all your effort in the rejection of this blameworthy trait from yourself; by that I hope for the setting-right of you.",
        "isHeader": False,
        "pairs": [
            {"ja": "אחדהא", "en": "**The first**"},
            {"ja": "שדהֵ מחבתך לנפסך", "en": "the intensity of your love for yourself"},
            {"ja": "וחרצך עלי אסתג'לאב אלנעם אליהא", "en": "your eagerness to draw the blessings to her"},
            {"ja": "פלא תנקלין קדמא אלי טאעהֵ אללה", "en": "you do not move a foot toward obedience to God"},
            {"ja": "אלא וגרצ'ך אלתנעם באללד'את", "en": "except that your intent is the enjoyment by pleasures"},
            {"ja": "פבד'לך ארג'ו אלאצלאח לך", "en": "by that I hope for the setting-right of you"},
        ]
    },
    {
        "ja": "ואלכ'לה אלת'אניה ג'הלך ען פצ'ל אלכ'אלק תעאלי עליך, פיקע פי והמך אנך לא תצלי אלי נעמתה אלא ברגבתך אליה פיהא, וקד תפצ'ל עליך במא פי עלמך ובמא פי גיר עלמך, ואנת לא תעקלין ברגבהֵ מן פעל ד'לך בו אולא, לית שערי פלו נפית ענך הד'א אלוהם לכ'לצת טאעתך ושכרך לה פי צ'מירך, וכאן מא תרג'ינה אוכד ואוג'ב מנה לך ענד ד'לך.",
        "en": "**The second failing** — your ignorance of the bounty of the Creator (exalted be He) upon you, so that it falls to your imagination that you will not reach His blessing except by craving it from Him. He has already bestowed bounty upon you of what is in your knowledge and of what is not in your knowledge — and you do not consider the desire of the one who first did this for you. Would you not — had you repelled this imagination from yourself — have purified your obedience and your thanksgiving to Him in your inward, and would not what you hope for have become more emphatic and more obligatory for you on account of this?",
        "isHeader": False,
        "pairs": [
            {"ja": "ואלכ'לה אלת'אניה", "en": "**The second failing**"},
            {"ja": "ג'הלך ען פצ'ל אלכ'אלק תעאלי עליך", "en": "your ignorance of the bounty of the Creator (exalted be He) upon you"},
            {"ja": "פיקע פי והמך אנך לא תצלי אלי נעמתה אלא ברגבתך", "en": "so that it falls to your imagination that you will not reach His blessing except by craving it"},
            {"ja": "וקד תפצ'ל עליך במא פי עלמך ובמא פי גיר עלמך", "en": "He has already bestowed bounty upon you of what is in your knowledge and of what is not in your knowledge"},
            {"ja": "לו נפית ענך הד'א אלוהם לכ'לצת טאעתך ושכרך לה פי צ'מירך", "en": "had you repelled this imagination from yourself — have purified your obedience and your thanksgiving to Him in your inward"},
            {"ja": "וכאן מא תרג'ינה אוכד ואוג'ב מנה לך ענד ד'לך", "en": "would not what you hope for have become more emphatic and more obligatory for you on account of this"},
        ]
    },
])

# ── קסח ──────────────────────────────────────────────────────────────────
en151 = "**The third failing** — your ignorance of yourself and the state of her management. You see her as worthy of the highest of blessings, and never cease being eager for them; whenever something of them reaches you, your ambition aspires to what is beyond, and you do not see the Creator (exalted be He) as worthy of the most emphatic of obediences. So that, if there be obedience from you, you reckon it as a favor from you toward Him — what is your knowledge of your poverty for Him and His freedom-from-need-of-you? If you removed this ignorance from yourself, and looked with the clear eye, and knew that the Creator (exalted be He) who created you is more solicitous for you than yourself, and more knowing of what is right for you of blessings and what is not right, you would be satisfied and content with what comes to you of them; and your thanksgiving to Him for them would grow great in purification, and you would not attach your hope to what would distract you from discriminating what came to you of them and rendering up the right of God for them. What you have not been worthy of, you must inevitably attain to when you have earned it by your obedience — not when you have hoped for it by attaching your ambition."
en152 = "As for what you have asked concerning the minimum that is incumbent toward God (exalted be He) of obedience by which the perpetuity of His blessing upon the human is earned — there are ten concepts."
en153 = "**Among them**: that he should not make [the blessing] a cause of disobedience to Him."
en154 = "**Among them**: that he should mention the blessing of God upon him with his tongue, and multiply for it praise and thanksgiving in his heart and the outward of his expression."
en155 = "**Among them**: that he should not deny it nor reckon it too little."
en156 = "**Among them**: that he should not attribute it to other than God if it was at the hand of an intermediary — thanking the intermediaries and being heedless of thanksgiving to God for it."
en157 = "**Among them**: that he should not boast in it and let it fall to his imagination that he has taken it by his strength and his subtlety, or by his desert of it."
en158 = "**Among them**: that it should not fall to his imagination that he perpetuates it by his prudence, and that it perishes from him when he is heedless and squanders it."

w("קסח", [
    {
        "ja": "ואלכ'לה אלת'אלת'ה, ג'הלך בנפסך ובחאל תדבירה, פאנת תרינהא אהלא לארפע אלנעם, פלא תזאלין ראגבה פיהא, כל מא חצל לך מנהא שי טמחת המתך אלי מא פוק ד'לך, ולא תרין אלכ'אלק תעאלי אהלא לאוכד אלטאעאת מנך, פאן כאנת מנך טאעה תחסבינהא תפצ'לא מנך עליה, מא עלמך בפקרך אליה וגנאיה ענך. פלו כשפת הד'א אלג'הל ענך ונט'רת בעין ג'ליה, ועלמת אן אלכ'אלק תעאלי אלד'י כ'לקך אנט'ר לך מנך ואערף מנך במא יצלח לך מן אלנעם ובמא לא יצלח לרצ'ית וקנעת במא ורדך מנהא, ועט'ם שכרך לה עליהא מכ'לצה, ולם תעלקי רג'אך במא ישגלך ען תמייז מא חצל לך מנהא ותופיהֵ חק אללה ענהא, ומא כנת לה אהלא לא בד לך מן אלוצול אליה אד'א אסתוג'בתה בטאעתך, לא אד'א רג'ותה בתעלק המתך.",
        "en": en151,
        "isHeader": False,
        "pairs": [
            {"ja": "ואלכ'לה אלת'אלת'ה", "en": "**The third failing**"},
            {"ja": "ג'הלך בנפסך ובחאל תדבירה", "en": "your ignorance of yourself and the state of her management"},
            {"ja": "פאנת תרינהא אהלא לארפע אלנעם", "en": "You see her as worthy of the highest of blessings"},
            {"ja": "כל מא חצל לך מנהא שי טמחת המתך אלי מא פוק ד'לך", "en": "whenever something of them reaches you, your ambition aspires to what is beyond"},
            {"ja": "ולא תרין אלכ'אלק תעאלי אהלא לאוכד אלטאעאת מנך", "en": "you do not see the Creator (exalted be He) as worthy of the most emphatic of obediences"},
            {"ja": "פאן כאנת מנך טאעה תחסבינהא תפצ'לא מנך עליה", "en": "if there be obedience from you, you reckon it as a favor from you toward Him"},
            {"ja": "פלו כשפת הד'א אלג'הל ענך", "en": "If you removed this ignorance from yourself"},
            {"ja": "ועלמת אן אלכ'אלק תעאלי אלד'י כ'לקך אנט'ר לך מנך", "en": "and knew that the Creator (exalted be He) who created you is more solicitous for you than yourself"},
            {"ja": "לרצ'ית וקנעת במא ורדך מנהא", "en": "you would be satisfied and content with what comes to you of them"},
            {"ja": "ועט'ם שכרך לה עליהא מכ'לצה", "en": "your thanksgiving to Him for them would grow great in purification"},
            {"ja": "ומא כנת לה אהלא לא בד לך מן אלוצול אליה אד'א אסתוג'בתה בטאעתך", "en": "What you have not been worthy of, you must inevitably attain to when you have earned it by your obedience"},
            {"ja": "לא אד'א רג'ותה בתעלק המתך", "en": "not when you have hoped for it by attaching your ambition"},
        ]
    },
    {
        "ja": "פצל. ז.",
        "en": "Section Seven.",
        "isHeader": True,
        "pairs": []
    },
    {
        "ja": "ואמא מא סאלת ען אקל מא ילזם ללה תעאלי מן אלטאעה, אלתי יסתוג'ב בהא דואם נעמתה עלי אלאנסאן, פעשרה מעאן.",
        "en": en152,
        "isHeader": False,
        "pairs": [
            {"ja": "ואמא מא סאלת ען אקל מא ילזם ללה תעאלי מן אלטאעה", "en": "As for what you have asked concerning the minimum that is incumbent toward God (exalted be He) of obedience"},
            {"ja": "אלתי יסתוג'ב בהא דואם נעמתה עלי אלאנסאן", "en": "by which the perpetuity of His blessing upon the human is earned"},
            {"ja": "פעשרה מעאן", "en": "there are ten concepts"},
        ]
    },
    {
        "ja": "מנהא אן לא יג'עלהא סבבא לעציאנה.",
        "en": en153,
        "isHeader": False,
        "pairs": [
            {"ja": "מנהא אן לא יג'עלהא סבבא לעציאנה", "en": "that he should not make [the blessing] a cause of disobedience to Him"},
        ]
    },
    {
        "ja": "ומנהא אן יד'כר נעמהֵ אללה עליה בלסאנה, ויכת'ר לה אלחמד ואלשכר בקלבה וט'אהר לפט'ה.",
        "en": en154,
        "isHeader": False,
        "pairs": [
            {"ja": "אן יד'כר נעמהֵ אללה עליה בלסאנה", "en": "that he should mention the blessing of God upon him with his tongue"},
            {"ja": "ויכת'ר לה אלחמד ואלשכר בקלבה", "en": "and multiply for it praise and thanksgiving in his heart"},
            {"ja": "וט'אהר לפט'ה", "en": "the outward of his expression"},
        ]
    },
    {
        "ja": "ומנהא אן לא יכפר בהא ויסתקלהא.",
        "en": en155,
        "isHeader": False,
        "pairs": [
            {"ja": "אן לא יכפר בהא", "en": "that he should not deny it"},
            {"ja": "ויסתקלהא", "en": "nor reckon it too little"},
        ]
    },
    {
        "ja": "ומנהא אלא ינסבהא אלי גירה אן כאנת עלי ידי ואסטה, פישכר אלוסאיט ויגפל ען שכר אללה עליהא.",
        "en": en156,
        "isHeader": False,
        "pairs": [
            {"ja": "אן לא ינסבהא אלי גירה", "en": "that he should not attribute it to other than God"},
            {"ja": "אן כאנת עלי ידי ואסטה", "en": "if it was at the hand of an intermediary"},
            {"ja": "פישכר אלוסאיט", "en": "thanking the intermediaries"},
            {"ja": "ויגפל ען שכר אללה עליהא", "en": "being heedless of thanksgiving to God for it"},
        ]
    },
    {
        "ja": "ומנהא אן לא יתפאכ'ר בהא ויקע בוהמה אנה אכ'ד'הא בקוותה ולטפה, או באסתחקאקה להא.",
        "en": en157,
        "isHeader": False,
        "pairs": [
            {"ja": "אן לא יתפאכ'ר בהא", "en": "that he should not boast in it"},
            {"ja": "ויקע בוהמה אנה אכ'ד'הא בקוותה ולטפה", "en": "let it fall to his imagination that he has taken it by his strength and his subtlety"},
            {"ja": "או באסתחקאקה להא", "en": "or by his desert of it"},
        ]
    },
    {
        "ja": "ומנהא אלא יקע בוהמה אנה יסתדימהא בחזמה, ואנהא תתלף ענה",
        "en": "**Among them**: that it should not fall to his imagination that he perpetuates it by his prudence, and that it perishes from him",
        "isHeader": False,
        "pairs": [
            {"ja": "אן לא יקע בוהמה אנה יסתדימהא בחזמה", "en": "that it should not fall to his imagination that he perpetuates it by his prudence"},
            {"ja": "ואנהא תתלף ענה", "en": "and that it perishes from him"},
        ]
    },
])

print("All 6 pages written.")

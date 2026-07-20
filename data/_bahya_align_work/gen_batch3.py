"""Generate alignment JSON for bab3 pages קלט–קמד."""
import json, pathlib

OUT = pathlib.Path(__file__).parent / "bab3_out"
OUT.mkdir(exist_ok=True)

# ── PAGE קלט (page_index 12) ───────────────────────────────────────────────
# JA: tail of 7th reason (intellect-obedience secure) + transition to merits of
# the Law + first of seven reasons + Prov 22:17-21
pages_kuf_lamed_tet = [
  {
    "ja": "תנקאד אליהא אלא בעד אמאתהֵ אלשהואת אלג'סמאניה, וגלבהֵ אלעקל עליהא ותצריפה להא עלי חכמתה ואראדתה, פלד'לך צארת הד'ה אלטאעה מנה מאמונהֵ אלזלל, וצאחבהא מעצום מן אלכ'טא, כקול אלכתאב לא יאונה לצדיק כל און.",
    "en": "the soul is not led toward it except after the mortifying of the corporeal appetites and the overcoming of the intellect over it and its deployment of the soul according to its wisdom and its will. That is why this obedience has come to be safe from missteps, and its bearer is preserved from error, as the Book says: \"No iniquity will befall the righteous\" (Proverbs 12:21).",
    "isHeader": False,
    "pairs": [
      {"ja": "תנקאד אליהא אלא בעד אמאתהֵ אלשהואת אלג'סמאניה", "en": "the soul is not led toward it except after the mortifying of the corporeal appetites"},
      {"ja": "וגלבהֵ אלעקל עליהא", "en": "and the overcoming of the intellect over it"},
      {"ja": "ותצריפה להא עלי חכמתה ואראדתה", "en": "and its deployment of the soul according to its wisdom and its will"},
      {"ja": "פלד'לך צארת הד'ה אלטאעה מנה מאמונהֵ אלזלל", "en": "That is why this obedience has come to be safe from missteps"},
      {"ja": "וצאחבהא מעצום מן אלכ'טא", "en": "and its bearer is preserved from error"},
    ]
  },
  {
    "ja": " ואמא פצ'איל אלשריעה פקד ינבגי אן אשרח מנהא מא חצ'רני, פאקול אן וג'וה אלצ'רוריאת אלדאעיה אלי אלתנביה אלשריעי איצ'א סבעה.",
    "en": "As for the excellences of the Law, it is fitting that I explicate what is at hand to me. I say that the aspects of necessities calling for the scriptural awakening are also seven.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואמא פצ'איל אלשריעה", "en": "As for the excellences of the Law"},
      {"ja": "פקד ינבגי אן אשרח מנהא מא חצ'רני", "en": "it is fitting that I explicate what is at hand to me"},
      {"ja": "פאקול אן וג'וה אלצ'רוריאת אלדאעיה אלי אלתנביה אלשריעי איצ'א סבעה", "en": "I say that the aspects of necessities calling for the scriptural awakening are also seven"},
    ]
  },
  {
    "ja": " אחדהא, אן אלאנסאן מולף מן נפס וג'סד, ופי אכ'לאקה כ'לק יבעת'ה עלי אלהמל פי אללד'את, ואלאסתגראק פי צ'רוב אלשהואת אלבהימיה, וטרח זמאם אלעקל ענה.",
    "en": "The first — the human is composed of soul and body; in his traits is a trait that drives him to indulgence in pleasures, immersion in the various brutish appetites, and the throwing off of the bridle of intellect from himself.",
    "isHeader": False,
    "pairs": [
      {"ja": "אחדהא", "en": "The first"},
      {"ja": "אן אלאנסאן מולף מן נפס וג'סד", "en": "the human is composed of soul and body"},
      {"ja": "ופי אכ'לאקה כ'לק יבעת'ה עלי אלהמל פי אללד'את", "en": "in his traits is a trait that drives him to indulgence in pleasures"},
      {"ja": "ואלאסתגראק פי צ'רוב אלשהואת אלבהימיה", "en": "immersion in the various brutish appetites"},
      {"ja": "וטרח זמאם אלעקל ענה", "en": "and the throwing off of the bridle of intellect from himself"},
    ]
  },
  {
    "ja": " ופיה איצ'א כ'לק ידעיה אלי אלזהד פי אלדניא, ותרך אלעמארה להא, לתקלב אחואלה פיהא, ותואתר אלאפאת ואלאחזאן עליהא, ונזועה אלי אלעאלם אלעקלי אלאעלי.",
    "en": "There is in him also a trait that summons him to renunciation of the world, and the abandoning of populating it, on account of the turning of conditions therein, the continuity of injuries and griefs over it, and his yearning toward the upper rational world.",
    "isHeader": False,
    "pairs": [
      {"ja": "ופיה איצ'א כ'לק ידעיה אלי אלזהד פי אלדניא", "en": "There is in him also a trait that summons him to renunciation of the world"},
      {"ja": "ותרך אלעמארה להא", "en": "and the abandoning of populating it"},
      {"ja": "לתקלב אחואלה פיהא", "en": "on account of the turning of conditions therein"},
      {"ja": "ותואתר אלאפאת ואלאחזאן עליהא", "en": "the continuity of injuries and griefs over it"},
      {"ja": "ונזועה אלי אלעאלם אלעקלי אלאעלי", "en": "and his yearning toward the upper rational world"},
    ]
  },
  {
    "ja": " וכלא אלראיין גיר מחמודין, לאן אחדהמא יקוד אלי פסאד נט'אם הד'א אלעאלם, ואלת'אני יקוד אלי פסאד חאל אלאנסאן פי אלדניא ואלאכ'רה.",
    "en": "Both views are unpraiseworthy: one of them leads to the corruption of the order of this world; the second leads to the corruption of the state of the human in this world and the next.",
    "isHeader": False,
    "pairs": [
      {"ja": "וכלא אלראיין גיר מחמודין", "en": "Both views are unpraiseworthy"},
      {"ja": "אחדהמא יקוד אלי פסאד נט'אם הד'א אלעאלם", "en": "one of them leads to the corruption of the order of this world"},
      {"ja": "ואלת'אני יקוד אלי פסאד חאל אלאנסאן פי אלדניא ואלאכ'רה", "en": "the second leads to the corruption of the state of the human in this world and the next"},
    ]
  },
  {
    "ja": " פכאן מן לטף אלכ'אלק תעאלי ועט'ים נעמתה עלי אלאנסאן, באן מן עליה במא יצלח בה אמרה ותנתט'ם אחואלה פי אלדארין בקאנון וסט בין אלעקל ואלשהוה, והי אלשריעה אלצאדקה אלחאפט'ה ללעדל אלט'אהר ואלבאטן, אלתי תופי אלאנסאן קסטה מן שהואתה פי הד'ה אלדניא, ותחפט' עליה ת'ואבה פי אלאכ'רה, כמא קאל אלכתאב הט אזנך ושמע דברי חכמים ולבך תשית לדעתי, כי נעים כי תשמרם בבטנך יכונו יחדיו על שפתיך, להיות בה' מבטחך הודעתיך היום אף אתה, הלא כתבתי לך שלישים במעצות ודעת, להודיעך קשט דברי אמת להשיב אמרים אמת לשלחיך.",
    "en": "So it was from the subtlety of the Creator (exalted be He) and the magnitude of His blessing upon the human that He favored him with what would set his matter aright, and order his states in both houses, by a middle canon between intellect and appetite — namely the truthful Law, the guardian of the outward and inward justice, which gives the human his portion of his appetites in this world and preserves for him his reward in the next, as the Book says: \"Incline your ear, and hear the words of the wise\" (Proverbs 22:17–21).",
    "isHeader": False,
    "pairs": [
      {"ja": "פכאן מן לטף אלכ'אלק תעאלי", "en": "So it was from the subtlety of the Creator (exalted be He)"},
      {"ja": "ועט'ים נעמתה עלי אלאנסאן", "en": "and the magnitude of His blessing upon the human"},
      {"ja": "באן מן עליה במא יצלח בה אמרה", "en": "that He favored him with what would set his matter aright"},
      {"ja": "ותנתט'ם אחואלה פי אלדארין", "en": "and order his states in both houses"},
      {"ja": "בקאנון וסט בין אלעקל ואלשהוה", "en": "by a middle canon between intellect and appetite"},
      {"ja": "והי אלשריעה אלצאדקה אלחאפט'ה ללעדל אלט'אהר ואלבאטן", "en": "namely the truthful Law, the guardian of the outward and inward justice"},
      {"ja": "אלתי תופי אלאנסאן קסטה מן שהואתה פי הד'ה אלדניא", "en": "which gives the human his portion of his appetites in this world"},
      {"ja": "ותחפט' עליה ת'ואבה פי אלאכ'רה", "en": "and preserves for him his reward in the next"},
    ]
  },
]

# ── PAGE קמ (page_index 13) ────────────────────────────────────────────────
# JA: 2nd reason (Law needs prophecy to specify limits) + 3rd reason (not
# universal) + 4th reason intro
pages_kuf_mem = [
  {
    "ja": "ואלוג'ה אלת'אני, אן אלתנביה אלעקלי לא יחד ואג'באת אעמאל אלטאעה ללה מן צלאה וציאם וצדקה וזכאה ופעל אלג'מיל, ולא יצל בה אלאנסאן אלי עלם חדוד אלעקובאת אלתי תלזם אלמקצר פי אלטאעה, פאחתאג' אלי תוקיף ותחדיד פי ג'מיע ד'לך בטריק אלשריעה והדאיהֵ אלנבוה, לינתט'ם לנא אלגרץ' אלמקצוד מנא באג'תמאעהמא, והי טאעהֵ אללה עז וג'ל, כקול אלכתאב והאלהים עשה שייראו מלפניו.",
    "en": "The second reason — the rational awakening does not delimit the obligatory acts of obedience to God — prayer, fasting, charity, alms-giving, and beautiful acts — nor does the human reach by it knowledge of the limits of the punishments incumbent on the one who falls short in obedience. So one had need of an instituted, delimited authority in all of this, by way of the Law and the guidance of prophecy, so that the goal intended of us would be ordered by their being combined — namely, obedience to God (mighty and exalted), as the Book said: \"And God has so made it that men should fear before Him\" (Ecclesiastes 3:14).",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלוג'ה אלת'אני", "en": "The second reason"},
      {"ja": "אן אלתנביה אלעקלי לא יחד ואג'באת אעמאל אלטאעה ללה", "en": "the rational awakening does not delimit the obligatory acts of obedience to God"},
      {"ja": "מן צלאה וציאם וצדקה וזכאה ופעל אלג'מיל", "en": "prayer, fasting, charity, alms-giving, and beautiful acts"},
      {"ja": "ולא יצל בה אלאנסאן אלי עלם חדוד אלעקובאת אלתי תלזם אלמקצר פי אלטאעה", "en": "nor does the human reach by it knowledge of the limits of the punishments incumbent on the one who falls short in obedience"},
      {"ja": "פאחתאג' אלי תוקיף ותחדיד פי ג'מיע ד'לך בטריק אלשריעה והדאיהֵ אלנבוה", "en": "So one had need of an instituted, delimited authority in all of this, by way of the Law and the guidance of prophecy"},
      {"ja": "לינתט'ם לנא אלגרץ' אלמקצוד מנא באג'תמאעהמא", "en": "so that the goal intended of us would be ordered by their being combined"},
      {"ja": "והי טאעהֵ אללה עז וג'ל", "en": "namely, obedience to God (mighty and exalted)"},
    ]
  },
  {
    "ja": " ואלוג'ה אלת'אלת', אן אלתנביה אלעקלי גיר עאם לג'מיע אלמכלפין לקצר המם בעצ'הם ותפאצ'ל תמייזהם בעץ' עלי בעץ', ואלתנביה אלשריעי עאם לכל מן חצלת פיה שרוט אלתכליף עלי אלתסאוי, ואן אכ'תלפת קבולהם לה עלי מא קדמנא פי אכ'ר אלבאב אלאול מן הד'א אלכתאב.",
    "en": "The third reason — rational awakening is not general to all who are charged with obligation, on account of the shortness of the energies of some of them and the differential measure of the discernment of some over others. The scriptural awakening is general to all in whom the conditions of moral charge have come about, on a basis of equality, even though their reception of it differs (as we have set out at the end of the First Gate of this book).",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלוג'ה אלת'אלת'", "en": "The third reason"},
      {"ja": "אן אלתנביה אלעקלי גיר עאם לג'מיע אלמכלפין", "en": "rational awakening is not general to all who are charged with obligation"},
      {"ja": "לקצר המם בעצ'הם ותפאצ'ל תמייזהם בעץ' עלי בעץ'", "en": "on account of the shortness of the energies of some of them and the differential measure of the discernment of some over others"},
      {"ja": "ואלתנביה אלשריעי עאם לכל מן חצלת פיה שרוט אלתכליף עלי אלתסאוי", "en": "The scriptural awakening is general to all in whom the conditions of moral charge have come about, on a basis of equality"},
    ]
  },
  {
    "ja": " וקד ילחק אלאנסאן אלתקציר פי בעץ' אחואלה ויפצ'ל פי בעצ'הא, פיכ'תלף תנביה אלעקל פיה באכ'תלאף תמייזה.",
    "en": "The human may fall short in some of his states and excel in others, so that the awakening of the intellect varies in him according to the variation of his discernment.",
    "isHeader": False,
    "pairs": [
      {"ja": "וקד ילחק אלאנסאן אלתקציר פי בעץ' אחואלה", "en": "The human may fall short in some of his states"},
      {"ja": "ויפצ'ל פי בעצ'הא", "en": "and excel in others"},
      {"ja": "פיכ'תלף תנביה אלעקל פיה באכ'תלאף תמייזה", "en": "so that the awakening of the intellect varies in him according to the variation of his discernment"},
    ]
  },
  {
    "ja": " ואלתנביה אלשריעי גיר מכ'תלף פי ד'אתה, בל צורתה צורה ואחדה ללצבי ואלחדת' ואלכהל ואלשיך' ואלעאקל ואלג'אהל, ויכ'תלף אלתאת'יר אלד'י יכון ענה פי ג'מיע מא ד'כרנא עלי מא וצפנא, כקול אלכתאב פי עמום אלתנביה אלשריעי לג'מיע אלאמה הקהל את העם האנשים והנשים והטף וגרך אשר בשעריך, וקאל בבוא כל ישראל לראות את פני ה' אלהיך במקום אשר יבחר תקרא את התורה הזאת נגד כל ישראל באזניהם.",
    "en": "The scriptural awakening does not vary in itself; rather, its form is one and the same for the child, the youth, the man in his prime, the old man, the man of intellect, and the ignorant — though the effect of it differs according to what we have described in the whole of what has been mentioned, as the Book said concerning the general sweep of scriptural awakening for the whole community: \"Assemble the people — the men and the women, and the children, and your stranger that is within your gates\" (Deuteronomy 31:12).",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלתנביה אלשריעי גיר מכ'תלף פי ד'אתה", "en": "The scriptural awakening does not vary in itself"},
      {"ja": "בל צורתה צורה ואחדה ללצבי ואלחדת' ואלכהל ואלשיך' ואלעאקל ואלג'אהל", "en": "rather, its form is one and the same for the child, the youth, the man in his prime, the old man, the man of intellect, and the ignorant"},
      {"ja": "ויכ'תלף אלתאת'יר אלד'י יכון ענה", "en": "though the effect of it differs"},
    ]
  },
  {
    "ja": " ואלוג'ה אלראבע, מן אלצ'רוריאת אלדאעיה",
    "en": "The fourth reason — among the necessities calling",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלוג'ה אלראבע", "en": "The fourth reason"},
      {"ja": "מן אלצ'רוריאת אלדאעיה", "en": "among the necessities calling"},
    ]
  },
]

# ── PAGE קמא (page_index 14) ───────────────────────────────────────────────
# JA: 4th reason (special blessings to Israel) + 5th reason (Law as prologue to
# intellect-awakening)
pages_kuf_mem_alef = [
  {
    "ja": "אלי אלשריעה, אן מן אלמעלום אן אלטאעאת תלזם אלנאס עלי חסב תפאצ'ל אלנעם עליהם, ופי כל עצר תחדת' אסבאב לקום דון קום תודי אלי אכ'תצאצהם בנעמה מן אללה תעאלי, פיתבע ד'לך אכ'תצאץ אלזיאדה פי אלטאעה לה ג'ל ועז מנהם דון סאיר אלאמם, ולא סביל אלי מערפהֵ ד'לך בטריק אלעקל פקט.",
    "en": "for the Law: it is known that obediences bind people according to the differential measure of blessings upon them. In every age, occasions arise for one people that occur for no other, leading to the singling-out of them in a blessing from God (exalted be He). The singling-out of an increase of obedience to God (mighty and exalted) on their part — beyond the rest of the nations — follows from this. There is no road to the knowledge of this by the way of intellect alone.",
    "isHeader": False,
    "pairs": [
      {"ja": "אן מן אלמעלום אן אלטאעאת תלזם אלנאס עלי חסב תפאצ'ל אלנעם עליהם", "en": "it is known that obediences bind people according to the differential measure of blessings upon them"},
      {"ja": "ופי כל עצר תחדת' אסבאב לקום דון קום", "en": "In every age, occasions arise for one people that occur for no other"},
      {"ja": "תודי אלי אכ'תצאצהם בנעמה מן אללה תעאלי", "en": "leading to the singling-out of them in a blessing from God (exalted be He)"},
      {"ja": "פיתבע ד'לך אכ'תצאץ אלזיאדה פי אלטאעה לה ג'ל ועז מנהם דון סאיר אלאמם", "en": "The singling-out of an increase of obedience to God (mighty and exalted) on their part — beyond the rest of the nations — follows from this"},
      {"ja": "ולא סביל אלי מערפהֵ ד'לך בטריק אלעקל פקט", "en": "There is no road to the knowledge of this by the way of intellect alone"},
    ]
  },
  {
    "ja": " לאכ'תצאץ אמתנא בכ'רוג'הם מן מצר, ושק אלבחר, ומא יתלוהא מן אלנעם אלתי לא חאג'ה בנא אלי ד'כרהא לשהרתהא ווצ'וחהא, פאכ'תצנא אללה תעאלי דון סאיר אלאמם בטאעה אלזמנא בהא שכרא לה, ת'ם אועדנא עלי אלתזאמהא מן אלת'ואב אלעאג'ל ואלאג'ל מא לא יחצי כת'רה תפצ'לא עלינא ואחסאנא אלינא, וג'מיע ד'לך לא יצח אלא באלשריעה, כקול אלכתאב אתם ראיתם אשר עשיתי למצרים ואשא אתכם על כנפי נשרים ואביא אתכם אלי, ועתה אם שמוע תשמעו בקלי ושמרתם את בריתי והייתם לי סגולה מכל העמים כי לי כל הארץ, ואתם תהיו לי ממלכת כהנים וגוי קדוש.",
    "en": "owing to our nation's being singled out in the exodus from Egypt, the splitting of the sea, and what follows of the blessings whose mention we need not undertake, on account of their fame and clarity. God (exalted be He) singled us out beyond the rest of the nations by an obedience for which He bound us as a thanksgiving to Him; then He promised us, for binding ourselves to it, of the near and far reward what cannot be numbered, of bounty toward us and beneficence to us; and the whole of this is not valid except by the Law, as the Book said: \"You have seen what I did to the Egyptians, and I bore you on eagles' wings, and brought you to Myself. So now, if you will indeed hear My voice, and keep My covenant, then you shall be My treasured possession from among all the peoples, for all the earth is Mine; and you shall be to Me a kingdom of priests and a holy nation\" (Exodus 19:4–6).",
    "isHeader": False,
    "pairs": [
      {"ja": "לאכ'תצאץ אמתנא בכ'רוג'הם מן מצר", "en": "owing to our nation's being singled out in the exodus from Egypt"},
      {"ja": "ושק אלבחר", "en": "the splitting of the sea"},
      {"ja": "פאכ'תצנא אללה תעאלי דון סאיר אלאמם בטאעה אלזמנא בהא שכרא לה", "en": "God (exalted be He) singled us out beyond the rest of the nations by an obedience for which He bound us as a thanksgiving to Him"},
      {"ja": "ת'ם אועדנא עלי אלתזאמהא מן אלת'ואב אלעאג'ל ואלאג'ל", "en": "then He promised us, for binding ourselves to it, of the near and far reward"},
      {"ja": "וג'מיע ד'לך לא יצח אלא באלשריעה", "en": "and the whole of this is not valid except by the Law"},
    ]
  },
  {
    "ja": " ואלוג'ה אלכ'אמס, אן אלתנביה אלשריעי הו מקדמה ומדכ'ל אלי תנביה אלעקל ודליל עליה, מן קבל חאג'הֵ אלאנסאן פי צבאיה אלי סיאסה ותדביר יקמע שהואתה אלי אן יקוי ויצח עקלה, וכד'לך אלנסא וצ'עפא אלעקול מן אלרג'אל לא ינקאדון אלי תדביר אלעקל לצ'עף זמאמה ות'קאפה להם, פדעת אלצ'רורה אלי תדביר וסט יחתמלונה ולא יתעד'ר עליהם אלוקוף עליה, ולד'לך וצ'עת אלשריעה עלי קטבי אלרהבה ואלרגבה.",
    "en": "The fifth reason — the scriptural awakening is the prologue and the gateway to the awakening of the intellect, and an evidence for it — in view of the human's need in his infancy for governance and management to suppress his appetites until his intellect grows strong and sound, and so too the women and those weak of intellect among the men, who are not led by the management of the intellect, on account of the weakness of its bridle and reining-in over them. Necessity called for a middle management which they could endure and to which their understanding would not be impossible. That is why the Law was laid down upon the two poles of awe and longing.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלוג'ה אלכ'אמס", "en": "The fifth reason"},
      {"ja": "אן אלתנביה אלשריעי הו מקדמה ומדכ'ל אלי תנביה אלעקל ודליל עליה", "en": "the scriptural awakening is the prologue and the gateway to the awakening of the intellect, and an evidence for it"},
      {"ja": "מן קבל חאג'הֵ אלאנסאן פי צבאיה אלי סיאסה ותדביר יקמע שהואתה", "en": "in view of the human's need in his infancy for governance and management to suppress his appetites"},
      {"ja": "אלי אן יקוי ויצח עקלה", "en": "until his intellect grows strong and sound"},
      {"ja": "פדעת אלצ'רורה אלי תדביר וסט יחתמלונה", "en": "Necessity called for a middle management which they could endure"},
      {"ja": "ולד'לך וצ'עת אלשריעה עלי קטבי אלרהבה ואלרגבה", "en": "That is why the Law was laid down upon the two poles of awe and longing"},
    ]
  },
  {
    "ja": " פמן לם יקצר פי",
    "en": "Whoever has not fallen short in",
    "isHeader": False,
    "pairs": [
      {"ja": "פמן לם יקצר פי", "en": "Whoever has not fallen short in"},
    ]
  },
]

# ── PAGE קמב (page_index 15) ───────────────────────────────────────────────
# JA: conclusion of 5th reason (reward of righteous) + 6th reason (Law contains
# scripturals + rationals together)
pages_kuf_mem_bet = [
  {
    "ja": "לואזם אלשריעה כאן פי דרג'הֵ אלאכ'יאר ואלאבראר, ואסתוג'ב אלת'ואב אלעאג'ל ואלאג'ל, ומן ארתקי מנהא אלי אלטאעה אלתי תכון ען אלתנביה אלעקלי חצל פי דרג'הֵ אלאנביא וצפוהֵ אללה אלאוליא, וכאן ת'ואבה פי אלדניא אלסרור באלאלתד'אד' בטאעהֵ אללה, כמא קאל אלנבי ע\"ס נמצאו דבריך ואוכלם ויהי דברך לי לששון ולשמחת לבבי כי נקרא שמך עלי ה' אלהי צבאות.",
    "en": "the requirements of the Law is in the rank of the good ones and the pious, and has earned the near and far reward. Whoever ascends from these to the obedience that comes about through the rational awakening attains the rank of the prophets and the pure ones of God, the friends — and his reward in this world is the joy of taking delight in obedience to God, as the Prophet (peace be upon him) said: \"Your words were found, and I ate them, and Your word was to me the joy and gladness of my heart, for Your name is called upon me, O Lord, God of hosts\" (Jeremiah 15:16).",
    "isHeader": False,
    "pairs": [
      {"ja": "לואזם אלשריעה כאן פי דרג'הֵ אלאכ'יאר ואלאבראר", "en": "the requirements of the Law is in the rank of the good ones and the pious"},
      {"ja": "ואסתוג'ב אלת'ואב אלעאג'ל ואלאג'ל", "en": "and has earned the near and far reward"},
      {"ja": "ומן ארתקי מנהא אלי אלטאעה אלתי תכון ען אלתנביה אלעקלי", "en": "Whoever ascends from these to the obedience that comes about through the rational awakening"},
      {"ja": "חצל פי דרג'הֵ אלאנביא וצפוהֵ אללה אלאוליא", "en": "attains the rank of the prophets and the pure ones of God, the friends"},
      {"ja": "וכאן ת'ואבה פי אלדניא אלסרור באלאלתד'אד' בטאעהֵ אללה", "en": "and his reward in this world is the joy of taking delight in obedience to God"},
    ]
  },
  {
    "ja": " וקאל ישמח צדיק בה' וחסה בו ויתהללו כל ישרי לב, וקאל אור זרוע לצדיק ולישרי לב שמחה.",
    "en": "And he said: \"The righteous shall rejoice in the Lord and take refuge in Him, and all the upright in heart shall glory\" (Psalms 64:11), and he said: \"Light is sown for the righteous, and gladness for the upright in heart\" (Psalms 97:11).",
    "isHeader": False,
    "pairs": []
  },
  {
    "ja": " ות'ואבה פי אלאכ'רה אלאתצאל באלנור אלאעלי אלד'י לא יצח לנא וצפה ולא יסוג לנא תמת'ילה, כקול אלכתאב אם בדרכי תלך ואם את משמרתי תשמר וגם אתה תדין את ביתי וגם תשמור את חצרי ונתתי לך מהלכים בין העומדים האלה, וקאל מה רב טובך אשר צפנת ליראיך פעלת לחוסים בך נגד בני אדם, וקאל עין לא ראתה אלהים זולתך יעשה למחכה לו.",
    "en": "And his reward in the next world is communion with the highest light, of which it is not valid for us to give description nor permitted us to give likeness, as the Book said: \"If you walk in My ways, and if you keep My charge, then you shall judge My house and shall also keep My courts, and I will give you free access among these who stand\" (Zechariah 3:7), and he said: \"How great is Your goodness which You have stored up for those who fear You\" (Psalms 31:20), and he said: \"Eye has not seen a God beside You who works for him that waits for Him\" (Isaiah 64:3).",
    "isHeader": False,
    "pairs": [
      {"ja": "ות'ואבה פי אלאכ'רה אלאתצאל באלנור אלאעלי", "en": "And his reward in the next world is communion with the highest light"},
      {"ja": "אלד'י לא יצח לנא וצפה ולא יסוג לנא תמת'ילה", "en": "of which it is not valid for us to give description nor permitted us to give likeness"},
    ]
  },
  {
    "ja": " ואלוג'ה אלסאדס, אן אלשריעה קד אחתות עלי מעאן לא יצח ללעקל וג'ה וג'ובהא והי אלסמעיאת, ועלי ג'מל מן אצול אלעקליאת, ואנמא וג'ב ד'לך לאן אלכ'לק אלד'ין ורדת עליהם אלשריעה כאנוא פי חאל גלבהֵ אלשהואת אלבהימיה עליהם, פצ'עפת לד'לך עקולהם ותמייזהם ען כת'יר מן אלעקליאת, פחמלתהם אלשריעה פי ד'לך מחמלא ואחדא, וצארת אלעקליאת ואלסמעיאת ענדהם סוא פי אלתנביה עליהא.",
    "en": "The sixth reason — the Law has urged upon concepts whose obligation is not validated for the intellect — these being the scripturals; and upon a totality of the roots of the rationals. This was necessary because the peoples upon whom the Law arrived were in the state of being overcome by brutish appetites, and on this account their intellects and their discernment of much of the rationals had weakened. So the Law took them upon one path, and the rationals and the scripturals became equal among them in the awakening to them.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלוג'ה אלסאדס", "en": "The sixth reason"},
      {"ja": "אן אלשריעה קד אחתות עלי מעאן לא יצח ללעקל וג'ה וג'ובהא והי אלסמעיאת", "en": "the Law has urged upon concepts whose obligation is not validated for the intellect — these being the scripturals"},
      {"ja": "ועלי ג'מל מן אצול אלעקליאת", "en": "and upon a totality of the roots of the rationals"},
      {"ja": "ואנמא וג'ב ד'לך לאן אלכ'לק אלד'ין ורדת עליהם אלשריעה כאנוא פי חאל גלבהֵ אלשהואת אלבהימיה עליהם", "en": "This was necessary because the peoples upon whom the Law arrived were in the state of being overcome by brutish appetites"},
      {"ja": "פצ'עפת לד'לך עקולהם ותמייזהם ען כת'יר מן אלעקליאת", "en": "and on this account their intellects and their discernment of much of the rationals had weakened"},
      {"ja": "פחמלתהם אלשריעה פי ד'לך מחמלא ואחדא", "en": "So the Law took them upon one path"},
    ]
  },
  {
    "ja": " פמן קוי עקלה ותמייזה אנתבה אליהא ואלזמהא נפסה ללוג'הין, ומן צ'עף עקלה ען מערפהֵ וג'ובהא עליה אלזמהא נפסה מן ג'ההֵ אלשריעה פקט וחמלהא מחמל אלסמעיאת,",
    "en": "Whoever has strengthened his intellect and his discernment has awakened to them and bound himself to both, on the two grounds; whoever's intellect is too weak to know their obligation upon him binds himself to them by the way of the Law alone, taking them in the path of the scripturals —",
    "isHeader": False,
    "pairs": [
      {"ja": "פמן קוי עקלה ותמייזה אנתבה אליהא ואלזמהא נפסה ללוג'הין", "en": "Whoever has strengthened his intellect and his discernment has awakened to them and bound himself to both, on the two grounds"},
      {"ja": "ומן צ'עף עקלה ען מערפהֵ וג'ובהא עליה", "en": "whoever's intellect is too weak to know their obligation upon him"},
      {"ja": "אלזמהא נפסה מן ג'ההֵ אלשריעה פקט וחמלהא מחמל אלסמעיאת", "en": "binds himself to them by the way of the Law alone, taking them in the path of the scripturals"},
    ]
  },
]

# ── PAGE קמג (page_index 16) ───────────────────────────────────────────────
# JA: end of 6th reason (Prov 3:17) + 7th reason (Law via prophet's signs) +
# blessings/Levites/priests + Hosea quote + last line (page ends mid-sentence)
pages_kuf_mem_gimel = [
  {
    "ja": "וכאן ד'לך צלאחא ללג'מיע כקולה דרכיה דרכי נעם וכל נתיבותיה שלום.",
    "en": "and that is welfare for all, as He said: \"Her ways are ways of pleasantness, and all her paths are peace\" (Proverbs 3:17).",
    "isHeader": False,
    "pairs": [
      {"ja": "וכאן ד'לך צלאחא ללג'מיע", "en": "and that is welfare for all"},
    ]
  },
  {
    "ja": " ואלוג'ה אלסאבע, אן אלשריעה חאצלה לנא בתוסט אנסאן תט'הר עלי ידיה אעלאם ובראהין יסתוי ג'מיע אלנאס פיהא מן ג'ההֵ חואסהם, לא יקדרון עלי דפעהא, פיצח להם מא יאתי בה ען אללה תעאלי בבראהין חסיה ועקליה, והי זיאדה עלי מא פטרוא עליה פי אצל אלכ'לקה ואלג'בלה מן אלתנביה אלעקלי.",
    "en": "The seventh reason — the Law is granted us by the mediation of a man at whose hands signs and demonstrations are manifest, in which all people are equal from the side of their senses, unable to repel them. So that which he brings from God (exalted be He) becomes valid for them by sensory and rational demonstrations — this being an addition to what they have been stamped-by-nature with in the root of creation and constitution from the rational awakening.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלוג'ה אלסאבע", "en": "The seventh reason"},
      {"ja": "אן אלשריעה חאצלה לנא בתוסט אנסאן", "en": "the Law is granted us by the mediation of a man"},
      {"ja": "תט'הר עלי ידיה אעלאם ובראהין", "en": "at whose hands signs and demonstrations are manifest"},
      {"ja": "יסתוי ג'מיע אלנאס פיהא מן ג'ההֵ חואסהם, לא יקדרון עלי דפעהא", "en": "in which all people are equal from the side of their senses, unable to repel them"},
      {"ja": "פיצח להם מא יאתי בה ען אללה תעאלי בבראהין חסיה ועקליה", "en": "So that which he brings from God (exalted be He) becomes valid for them by sensory and rational demonstrations"},
      {"ja": "והי זיאדה עלי מא פטרוא עליה פי אצל אלכ'לקה ואלג'בלה מן אלתנביה אלעקלי", "en": "this being an addition to what they have been stamped-by-nature with in the root of creation and constitution from the rational awakening"},
    ]
  },
  {
    "ja": " פמן אעתבר נעם אללה תעאלי עליה אלד'י יסתוי פיהא מע ג'מיע אלכ'לק איקן בוג'וב אלתזאם טאעהֵ אללה בג'מיע צנוף אלעקליאת, פאד'א אעתבר נעם אללה תעאלי עליה אלתי כ'ץ אללה בהא אהלה וקבילתה מן ג'מלהֵ אלקבאיל איקן בוג'וב אלשראיע אלסמעיה עליה מן דון סאיר אלאמם.",
    "en": "Whoever reflects on God's blessings (exalted be He) upon him in which he is equal with all creatures becomes certain of the obligation of binding himself to obedience to God by all the kinds of rational obligations. And when he reflects on God's blessings upon him with which God has singled out his people and his tribe from the totality of tribes, he becomes certain of the obligation of the scriptural laws upon him beyond the rest of the nations.",
    "isHeader": False,
    "pairs": [
      {"ja": "פמן אעתבר נעם אללה תעאלי עליה אלד'י יסתוי פיהא מע ג'מיע אלכ'לק", "en": "Whoever reflects on God's blessings (exalted be He) upon him in which he is equal with all creatures"},
      {"ja": "איקן בוג'וב אלתזאם טאעהֵ אללה בג'מיע צנוף אלעקליאת", "en": "becomes certain of the obligation of binding himself to obedience to God by all the kinds of rational obligations"},
      {"ja": "פאד'א אעתבר נעם אללה תעאלי עליה אלתי כ'ץ אללה בהא אהלה וקבילתה", "en": "And when he reflects on God's blessings upon him with which God has singled out his people and his tribe"},
      {"ja": "איקן בוג'וב אלשראיע אלסמעיה עליה מן דון סאיר אלאמם", "en": "he becomes certain of the obligation of the scriptural laws upon him beyond the rest of the nations"},
    ]
  },
  {
    "ja": " וכד'לך אד'א אעתבר נעם אללה תעאלי עליה אלתי כ'ץ בהא עשירתה דון סאיר אלעשאיר מת'ל אללויה ואלכהנה איקן בוג'וב אלשראיע אלתי כ'ץ אללה בהא עשירתה, ולד'לך תג'ד שראיע אלכהנה ארבע ועשרין באזא ארבע ועשרין פצ'ילה אנעם אללה תעאלי בהא עלי אלכהנים, והי ארבע ועשרון מתנות כהנה.",
    "en": "And likewise, when he reflects on God's blessings (exalted be He) upon him with which God has singled out his clan beyond the rest of the clans — such as the Levites and the priests — he becomes certain of the obligation of the laws with which God has singled out his clan. That is why you find the priestly laws are twenty-four, in parallel to the twenty-four excellences with which God (exalted be He) bestowed blessing upon the priests — namely the twenty-four priestly gifts.",
    "isHeader": False,
    "pairs": [
      {"ja": "אד'א אעתבר נעם אללה תעאלי עליה אלתי כ'ץ בהא עשירתה דון סאיר אלעשאיר מת'ל אללויה ואלכהנה", "en": "when he reflects on God's blessings (exalted be He) upon him with which God has singled out his clan beyond the rest of the clans — such as the Levites and the priests"},
      {"ja": "איקן בוג'וב אלשראיע אלתי כ'ץ אללה בהא עשירתה", "en": "he becomes certain of the obligation of the laws with which God has singled out his clan"},
      {"ja": "ולד'לך תג'ד שראיע אלכהנה ארבע ועשרין", "en": "That is why you find the priestly laws are twenty-four"},
      {"ja": "והי ארבע ועשרון מתנות כהנה", "en": "namely the twenty-four priestly gifts"},
    ]
  },
  {
    "ja": " ועלי הד'א אלקיאס ילזם כל מן כ'צה אללה תעאלי בנעמה דון סאיר אלנאס אן ילזם נפסה ללה תעאלי טאעה יכ'תץ בהא דון סאיר אלנאס, מע אג'תהאדה פי אלטאעה אלתי תעמה מעהם עלי חסב טאקתה ואדראכה, שכרא ללה תעאלי עלי מא כ'צה מן נעמתה, פיכון ד'לך סבב דואמהא לה ואלזיאדה עליהא, ואלת'ואב עלי טאעתה פי אלאג'ל, ולא יכון כמן קיל פיה וכסף הרביתי לה וזהב עשו לבעל.",
    "en": "By this analogy, every man whom God (exalted be He) has singled out by a blessing beyond the rest of the people is bound to bind himself to God (exalted be He) in an obedience by which he is singled out beyond the rest of the people — together with his striving in the obedience that includes him with them according to his capacity and his apprehension — as thanksgiving to God (exalted be He) for what He has singled him out by of His blessing. This will be a cause of its enduring for him and of his receiving an increase upon it, and of reward for his obedience in the long term, so that he is not like the one of whom it was said: \"And I increased silver for her, and gold they made for Baal\" (Hosea 2:10).",
    "isHeader": False,
    "pairs": [
      {"ja": "ועלי הד'א אלקיאס ילזם כל מן כ'צה אללה תעאלי בנעמה דון סאיר אלנאס", "en": "By this analogy, every man whom God (exalted be He) has singled out by a blessing beyond the rest of the people"},
      {"ja": "אן ילזם נפסה ללה תעאלי טאעה יכ'תץ בהא דון סאיר אלנאס", "en": "is bound to bind himself to God (exalted be He) in an obedience by which he is singled out beyond the rest of the people"},
      {"ja": "שכרא ללה תעאלי עלי מא כ'צה מן נעמתה", "en": "as thanksgiving to God (exalted be He) for what He has singled him out by of His blessing"},
      {"ja": "פיכון ד'לך סבב דואמהא לה ואלזיאדה עליהא", "en": "This will be a cause of its enduring for him and of his receiving an increase upon it"},
      {"ja": "ואלת'ואב עלי טאעתה פי אלאג'ל", "en": "and of reward for his obedience in the long term"},
    ]
  },
  {
    "ja": " ומן קצר פי מא יכ'צה מן אלנעמה ען אלטאעה",
    "en": "Whoever falls short in what is singled out for him of blessing — in obedience for it —",
    "isHeader": False,
    "pairs": [
      {"ja": "ומן קצר פי מא יכ'צה מן אלנעמה ען אלטאעה", "en": "Whoever falls short in what is singled out for him of blessing — in obedience for it —"},
    ]
  },
]

# ── PAGE קמד (page_index 17) ───────────────────────────────────────────────
# JA: conclusion of 7th reason (falls from rational rank / Isaiah / Psalms) +
# Fasl 4 header + definition of scriptural awakening + Law's three categories +
# duties of the heart (page ends mid-list)
pages_kuf_mem_dalet = [
  {
    "ja": "עליהא חמלה ד'לך עלי אלתקציר פימא יכ'ץ עשירתה, ת'ם פימא יכ'ץ קבילתה ותרך אלשריעה, ואד'א לם ילתזם אלשריעה לם ילתזם ואג'באת אלעקליאת, ואד'א לם ילתזם מא אדי אליה אלעקל מע אמכאנה לה ונבאהתה אליה סקט ען מרתבהֵ אלחיואן אלנאטק, וכאנת אלבהאים אהדי מנה, כקולה ידע שור קונהו וחמור אבוס בעליו ישראל לא ידע עמי לא התבונן, וכאן סבילה סביל מן קיל פיה כי רשעים יאבדו ואויבי ה' כיקר כרים כלו בעשן כלו.",
    "en": "that falling short carries him to falling short in what is singled out for his clan, then in what is singled out for his tribe, and the abandoning of the Law. And when he does not bind himself to the Law, he does not bind himself to the obligatory rationals; and when he does not bind himself to what the intellect has led him to — despite its having been within his power and his being awakened to it — he falls from the rank of the rational animal, and the brutes are more guided than he, as it is said: \"The ox knows its owner, and the ass its master's crib; Israel does not know, My people does not consider\" (Isaiah 1:3); and his path is the path of the one of whom it is said: \"For the wicked shall perish, and the enemies of the Lord shall be as the prizing of the lambs — in smoke shall they consume away\" (Psalms 37:20).",
    "isHeader": False,
    "pairs": [
      {"ja": "עליהא חמלה ד'לך עלי אלתקציר פימא יכ'ץ עשירתה, ת'ם פימא יכ'ץ קבילתה ותרך אלשריעה", "en": "that falling short carries him to falling short in what is singled out for his clan, then in what is singled out for his tribe, and the abandoning of the Law"},
      {"ja": "ואד'א לם ילתזם אלשריעה לם ילתזם ואג'באת אלעקליאת", "en": "And when he does not bind himself to the Law, he does not bind himself to the obligatory rationals"},
      {"ja": "ואד'א לם ילתזם מא אדי אליה אלעקל מע אמכאנה לה ונבאהתה אליה", "en": "and when he does not bind himself to what the intellect has led him to — despite its having been within his power and his being awakened to it"},
      {"ja": "סקט ען מרתבהֵ אלחיואן אלנאטק", "en": "he falls from the rank of the rational animal"},
      {"ja": "וכאנת אלבהאים אהדי מנה", "en": "and the brutes are more guided than he"},
    ]
  },
  {
    "ja": " פצל. ד.",
    "en": "Chapter Four.",
    "isHeader": True,
    "pairs": []
  },
  {
    "ja": " וקד ינבגי לנא אן נביין צורהֵ אלתנביה אלשריעי, ואקסאם אלשריעה, ומנאזל אהל אלעלם פיהא, ומראתבהם פי אעתקאדהם פיהא ואלתזאמהם להא.",
    "en": "It is fitting for us to explain the form of the scriptural awakening, the divisions of the Law, the stations of the people of knowledge in it, and their ranks in their conviction of it and their binding themselves to it.",
    "isHeader": False,
    "pairs": [
      {"ja": "וקד ינבגי לנא אן נביין צורהֵ אלתנביה אלשריעי", "en": "It is fitting for us to explain the form of the scriptural awakening"},
      {"ja": "ואקסאם אלשריעה", "en": "the divisions of the Law"},
      {"ja": "ומנאזל אהל אלעלם פיהא", "en": "the stations of the people of knowledge in it"},
      {"ja": "ומראתבהם פי אעתקאדהם פיהא ואלתזאמהם להא", "en": "and their ranks in their conviction of it and their binding themselves to it"},
    ]
  },
  {
    "ja": " פנקול, אן אלתנביה אלשריעי וחי ירד מן אללה עז וג'ל עלי שכ'ץ מן אשכ'אץ אלנאס במא יסתחסנה מנה מן אלטאעה לה, לית'יבה עלי אלתזאמהא ת'ואבא עאג'לא ואג'לא פי אלדארין תפצ'לא וג'ודא ואחסאנא.",
    "en": "We say: the scriptural awakening is a revelation that descends from God (mighty and exalted) upon one person from among the people, with what God deems good of obedience to Him, to reward him for binding himself to it with a near and far reward in both houses, out of bounty, generosity, and beneficence.",
    "isHeader": False,
    "pairs": [
      {"ja": "אן אלתנביה אלשריעי וחי ירד מן אללה עז וג'ל", "en": "the scriptural awakening is a revelation that descends from God (mighty and exalted)"},
      {"ja": "עלי שכ'ץ מן אשכ'אץ אלנאס", "en": "upon one person from among the people"},
      {"ja": "במא יסתחסנה מנה מן אלטאעה לה", "en": "with what God deems good of obedience to Him"},
      {"ja": "לית'יבה עלי אלתזאמהא ת'ואבא עאג'לא ואג'לא פי אלדארין", "en": "to reward him for binding himself to it with a near and far reward in both houses"},
      {"ja": "תפצ'לא וג'ודא ואחסאנא", "en": "out of bounty, generosity, and beneficence"},
    ]
  },
  {
    "ja": " ואלשריעה תקסם אעמאל אלנאס ת'לאת'ה אקסאם, אמר, ונהי, ומבאח.",
    "en": "The Law divides the acts of people into three categories: command, prohibition, and permitted.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלשריעה תקסם אעמאל אלנאס ת'לאת'ה אקסאם", "en": "The Law divides the acts of people into three categories"},
      {"ja": "אמר, ונהי, ומבאח", "en": "command, prohibition, and permitted"},
    ]
  },
  {
    "ja": " פאלאמר ינקסם קסמין, מנהא פראיץ' אלקלוב, והי אלאשיא אלתי תצח באלאעתקאד, מת'ל אלתוחיד, ואלאכ'לאץ ללה תעאלי, ואלתוכל עליה, ואלאסתסלאם אליה, ואלרצ'א בקצ'איה, ואלאימאן בנביה, ואלתחקק באלשריעה, ואלכ'וף מן אללה, ואלחפט' לשראיעה ואלתפכר פי",
    "en": "The command divides into two kinds: among them the duties of the heart — these being the things that are valid through conviction, such as affirming the unity of God, purification-of-action toward God (exalted be He), reliance upon Him, submission to Him, contentment with His decrees, faith in His prophet, verifying-the-reality of the Law, fear of God, and the guarding of His laws — and the contemplation of",
    "isHeader": False,
    "pairs": [
      {"ja": "פאלאמר ינקסם קסמין", "en": "The command divides into two kinds"},
      {"ja": "מנהא פראיץ' אלקלוב", "en": "among them the duties of the heart"},
      {"ja": "והי אלאשיא אלתי תצח באלאעתקאד", "en": "these being the things that are valid through conviction"},
      {"ja": "מת'ל אלתוחיד", "en": "such as affirming the unity of God"},
      {"ja": "ואלאכ'לאץ ללה תעאלי", "en": "purification-of-action toward God (exalted be He)"},
      {"ja": "ואלתוכל עליה", "en": "reliance upon Him"},
      {"ja": "ואלאסתסלאם אליה", "en": "submission to Him"},
      {"ja": "ואלרצ'א בקצ'איה", "en": "contentment with His decrees"},
      {"ja": "ואלאימאן בנביה", "en": "faith in His prophet"},
      {"ja": "ואלתחקק באלשריעה", "en": "verifying-the-reality of the Law"},
      {"ja": "ואלכ'וף מן אללה", "en": "fear of God"},
      {"ja": "ואלחפט' לשראיעה", "en": "and the guarding of His laws"},
    ]
  },
]

# ── WRITE OUTPUT FILES ─────────────────────────────────────────────────────
pages_data = {
    "קלט": pages_kuf_lamed_tet,
    "קמ": pages_kuf_mem,
    "קמא": pages_kuf_mem_alef,
    "קמב": pages_kuf_mem_bet,
    "קמג": pages_kuf_mem_gimel,
    "קמד": pages_kuf_mem_dalet,
}

for page_he, segments in pages_data.items():
    out = {"pages": {page_he: segments}}
    path = OUT / f"{page_he}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    total_pairs = sum(len(s.get("pairs", [])) for s in segments)
    print(f"wrote {path.name}: {len(segments)} segs / {total_pairs} pairs")

print("done")

"""Hand-authored word-level alignment triples for Bamidbar chapter 33."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: אֵלֶּה מַסְעֵי בְנֵי-יִשְׂרָאֵל אֲשֶׁר יָצְאוּ מֵאֶרֶץ מִצְרַיִם--לְצִבְאֹתָם בְּיַד-מֹשֶׁה וְאַהֲרֹן
        # JA: והד'א מראחל בני אסראיל. אד' כ'רגו מן בלד מצר עלי' גיושהם. ביד מוסי' והרון
        # EN: And these are the stages of the sons of Israel when they went out from the land of Egypt, according to their hosts, by the hand of Moses and Aaron.
        ("אֵלֶּה", "והד'א", "And these are"),
        ("מַסְעֵי", "מראחל", "the stages of"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("אֲשֶׁר יָצְאוּ", "אד' כ'רגו", "when they went out"),
        ("מֵאֶרֶץ", "מן בלד", "from the land of"),
        ("מִצְרַיִם", "מצר", "Egypt,"),
        ("לְצִבְאֹתָם", "עלי' גיושהם", "according to their hosts,"),
        ("בְּיַד-מֹשֶׁה", "ביד מוסי'", "by the hand of Moses"),
        ("וְאַהֲרֹן", "והרון", "and Aaron."),
    ],
    2: [
        # HE: וַיִּכְתֹּב מֹשֶׁה אֶת-מוֹצָאֵיהֶם לְמַסְעֵיהֶם--עַל-פִּי יְהוָה וְאֵלֶּה מַסְעֵיהֶם לְמוֹצָאֵיהֶם
        # JA: פכתב מוסי' כ'רוגהם. עלי' מראחלהם עלי' קול אללה. והד'א מראחלהם לכ'רוגהם
        # EN: And Moses wrote down their going out, stage by stage, at the word of God. And these are their stages of their going out.
        ("וַיִּכְתֹּב", "פכתב", "And Moses wrote down"),
        ("מֹשֶׁה", "מוסי'", "their going out,"),
        ("אֶת-מוֹצָאֵיהֶם", "כ'רוגהם", "stage by stage,"),
        ("לְמַסְעֵיהֶם", "עלי' מראחלהם", "at the word of"),
        ("עַל-פִּי יְהוָה", "עלי' קול אללה", "God."),
        ("וְאֵלֶּה", "והד'א", "And these are"),
        ("מַסְעֵיהֶם", "מראחלהם", "their stages of"),
        ("לְמוֹצָאֵיהֶם", "לכ'רוגהם", "their going out."),
    ],
    3: [
        # HE: וַיִּסְעוּ מֵרַעְמְסֵס בַּחֹדֶשׁ הָרִאשׁוֹן בַּחֲמִשָּׁה עָשָׂר יוֹם לַחֹדֶשׁ הָרִאשׁוֹן מִמָּחֳרַת הַפֶּסַח יָצְאוּ בְנֵי-יִשְׂרָאֵל בְּיָד רָמָה--לְעֵינֵי כָּל-מִצְרָיִם
        # JA: ורחלו מן עין שמס פי אלשהר אלאוול. פי אליום אלכ'אמס עשר. וד'אלך מן ג'ד אלפסח. כ'רגו בני אסראיל ביד רפיעה. בחצ'רה' גמיע אלמצריון
        # EN: And they set out from Ein Shams (Raamses) in the first month, on the fifteenth day — that being the day after the Passover. The sons of Israel went out with a raised hand, in the presence of all the Egyptians,
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵרַעְמְסֵס", "מן עין שמס", "from Ein Shams (Raamses)"),
        ("בַּחֹדֶשׁ הָרִאשׁוֹן", "פי אלשהר אלאוול", "in the first month,"),
        ("בַּחֲמִשָּׁה עָשָׂר יוֹם", "פי אליום אלכ'אמס עשר", "on the fifteenth day —"),
        ("מִמָּחֳרַת הַפֶּסַח", "וד'אלך מן ג'ד אלפסח", "that being the day after the Passover."),
        ("יָצְאוּ", "כ'רגו", "went out"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "The sons of Israel"),
        ("בְּיָד רָמָה", "ביד רפיעה", "with a raised hand,"),
        ("לְעֵינֵי כָּל-מִצְרָיִם", "בחצ'רה' גמיע אלמצריון", "in the presence of all the Egyptians,"),
    ],
    4: [
        # HE: וּמִצְרַיִם מְקַבְּרִים אֵת אֲשֶׁר הִכָּה יְהוָה בָּהֶם--כָּל-בְּכוֹר וּבֵאלֹהֵיהֶם עָשָׂה יְהוָה שְׁפָטִים
        # JA: והם ידפנון. אלד'י קתל אללה פיהם כל בכר. וצנע אחכאמא במעבודאתהם
        # EN: while they were burying those whom God had slain among them — every firstborn — and He had executed judgments upon their deities.
        ("וּמִצְרַיִם", "והם", "while they were"),
        ("מְקַבְּרִים", "ידפנון", "burying"),
        ("אֵת אֲשֶׁר הִכָּה", "אלד'י קתל", "those whom"),
        ("יְהוָה", "אללה", "God had slain"),
        ("בָּהֶם", "פיהם", "among them —"),
        ("כָּל-בְּכוֹר", "כל בכר", "every firstborn —"),
        ("וּבֵאלֹהֵיהֶם", "וצנע אחכאמא במעבודאתהם", "and He had executed judgments upon their deities."),
    ],
    5: [
        # HE: וַיִּסְעוּ בְנֵי-יִשְׂרָאֵל מֵרַעְמְסֵס וַיַּחֲנוּ בְּסֻכֹּת
        # JA: ורחלו בני אסראיל מן עין שמס. ונזלו פי סכות
        # EN: And the sons of Israel set out from Ein Shams and encamped at Sukkoth.
        ("וַיִּסְעוּ בְנֵי-יִשְׂרָאֵל", "ורחלו בני אסראיל", "And the sons of Israel set out"),
        ("מֵרַעְמְסֵס", "מן עין שמס", "from Ein Shams"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּסֻכֹּת", "פי סכות", "at Sukkoth."),
    ],
    6: [
        # HE: וַיִּסְעוּ מִסֻּכֹּת וַיַּחֲנוּ בְאֵתָם אֲשֶׁר בִּקְצֵה הַמִּדְבָּר
        # JA: ורחלו מן ת'ם. ונזלו פי איתם. פי טרף אלברייה
        # EN: And they set out from Sukkoth and encamped at Etham, at the edge of the wilderness.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִסֻּכֹּת", "מן ת'ם", "from Sukkoth"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְאֵתָם", "פי איתם", "at Etham,"),
        ("אֲשֶׁר בִּקְצֵה הַמִּדְבָּר", "פי טרף אלברייה", "at the edge of the wilderness."),
    ],
    7: [
        # HE: וַיִּסְעוּ מֵאֵתָם וַיָּשָׁב עַל-פִּי הַחִירֹת אֲשֶׁר עַל-פְּנֵי בַּעַל צְפוֹן וַיַּחֲנוּ לִפְנֵי מִגְדֹּל
        # JA: ורחלו מנהא. ורגעו אלי' פואה' אלחירות. אלתי בחצ'רה' בעל צפון. ונזלו בין ידי מגדול
        # EN: And they set out from Etham and turned back to the mouth of the Hiroth, which is before Baal-Zephon, and they encamped before Migdol.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵאֵתָם", "מנהא", "from Etham"),
        ("וַיָּשָׁב", "ורגעו", "and turned back"),
        ("עַל-פִּי הַחִירֹת", "אלי' פואה' אלחירות", "to the mouth of the Hiroth,"),
        ("אֲשֶׁר עַל-פְּנֵי", "אלתי בחצ'רה'", "which is before"),
        ("בַּעַל צְפוֹן", "בעל צפון", "Baal-Zephon,"),
        ("וַיַּחֲנוּ", "ונזלו", "and they encamped"),
        ("לִפְנֵי מִגְדֹּל", "בין ידי מגדול", "before Migdol."),
    ],
    8: [
        # HE: וַיִּסְעוּ מִפְּנֵי הַחִירֹת וַיַּעַבְרוּ בְתוֹךְ-הַיָּם הַמִּדְבָּרָה וַיֵּלְכוּ דֶּרֶךְ שְׁלֹשֶׁת יָמִים בְּמִדְבַּר אֵתָם וַיַּחֲנוּ בְּמָרָה
        # JA: ורחלו מן ת'ם. ועברו פי וסט אלבחר פי אלברייה. ת'ם סארו. מסאפה' ת'לאת'ה' אייאם פי ברייה' איתם. ונזלו פי אלמרירה
        # EN: And they set out from the mouth of the Hiroth and crossed through the midst of the sea into the wilderness; then they traveled a distance of three days in the wilderness of Etham, and encamped at the Bitterness.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִפְּנֵי הַחִירֹת", "מן ת'ם", "from the mouth of the Hiroth"),
        ("וַיַּעַבְרוּ", "ועברו", "and crossed"),
        ("בְתוֹךְ-הַיָּם", "פי וסט אלבחר", "through the midst of the sea"),
        ("הַמִּדְבָּרָה", "פי אלברייה", "into the wilderness;"),
        (None, "ת'ם", "then"),
        ("וַיֵּלְכוּ", "סארו", "they traveled"),
        ("דֶּרֶךְ שְׁלֹשֶׁת יָמִים", "מסאפה' ת'לאת'ה' אייאם", "a distance of three days"),
        ("בְּמִדְבַּר אֵתָם", "פי ברייה' איתם", "in the wilderness of Etham,"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּמָרָה", "פי אלמרירה", "at the Bitterness."),
    ],
    9: [
        # HE: וַיִּסְעוּ מִמָּרָה וַיָּבֹאוּ אֵילִמָה וּבְאֵילִם שְׁתֵּים עֶשְׂרֵה עֵינֹת מַיִם וְשִׁבְעִים תְּמָרִים--וַיַּחֲנוּ-שָׁם
        # JA: ורחלו מנהא. וגאו אלי' אילים. וכאן פיהא. את'ני עשר עין מא. וסבעין נכ'לה פנזלו הנאך
        # EN: And they set out from the Bitterness and came to Elim — and in it were twelve springs of water and seventy palm-trees — and they encamped there.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִמָּרָה", "מנהא", "from the Bitterness"),
        ("וַיָּבֹאוּ", "וגאו", "and came"),
        ("אֵילִמָה", "אלי' אילים", "to Elim —"),
        ("וּבְאֵילִם", "וכאן פיהא", "and in it were"),
        ("שְׁתֵּים עֶשְׂרֵה עֵינֹת מַיִם", "את'ני עשר עין מא", "twelve springs of water"),
        ("וְשִׁבְעִים תְּמָרִים", "וסבעין נכ'לה", "and seventy palm-trees —"),
        ("וַיַּחֲנוּ-שָׁם", "פנזלו הנאך", "and they encamped there."),
    ],
    10: [
        # HE: וַיִּסְעוּ מֵאֵילִם וַיַּחֲנוּ עַל-יַם-סוּף
        # JA: ורחלו מנהא. ונזלו עלי' בחר אלקלזם
        # EN: And they set out from Elim and encamped by the Sea of Qulzum (Red Sea).
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵאֵילִם", "מנהא", "from Elim"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("עַל-יַם-סוּף", "עלי' בחר אלקלזם", "by the Sea of Qulzum (Red Sea)."),
    ],
    11: [
        # HE: וַיִּסְעוּ מִיַּם-סוּף וַיַּחֲנוּ בְּמִדְבַּר-סִין
        # JA: ורחלו מנהא. ונזלו פי ברייה' סין
        # EN: And they set out from the Sea of Qulzum and encamped in the wilderness of Sin.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִיַּם-סוּף", "מנהא", "from the Sea of Qulzum"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּמִדְבַּר-סִין", "פי ברייה' סין", "in the wilderness of Sin."),
    ],
    12: [
        # HE: וַיִּסְעוּ מִמִּדְבַּר-סִין וַיַּחֲנוּ בְּדָפְקָה
        # JA: פרחלו מנהא. ונזלו פי דפקה
        # EN: And they set out from the wilderness of Sin and encamped at Dophkah.
        ("וַיִּסְעוּ", "פרחלו", "And they set out"),
        ("מִמִּדְבַּר-סִין", "מנהא", "from the wilderness of Sin"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּדָפְקָה", "פי דפקה", "at Dophkah."),
    ],
    13: [
        # HE: וַיִּסְעוּ מִדָּפְקָה וַיַּחֲנוּ בְּאָלוּשׁ
        # JA: ורחלו מנהא. ונזלו פי אלוש
        # EN: And they set out from Dophkah and encamped at Alush.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִדָּפְקָה", "מנהא", "from Dophkah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּאָלוּשׁ", "פי אלוש", "at Alush."),
    ],
    14: [
        # HE: וַיִּסְעוּ מֵאָלוּשׁ וַיַּחֲנוּ בִּרְפִידִם וְלֹא-הָיָה שָׁם מַיִם לָעָם לִשְׁתּוֹת
        # JA: ורחלו מנהא. ונזלו פי רפידים. ולם יכון ת'ם מאא. לאלקום ישרבונה
        # EN: And they set out from Alush and encamped at Rephidim; and there was no water there for the people to drink.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵאָלוּשׁ", "מנהא", "from Alush"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בִּרְפִידִם", "פי רפידים", "at Rephidim;"),
        ("וְלֹא-הָיָה שָׁם מַיִם", "ולם יכון ת'ם מאא", "and there was no water there"),
        ("לָעָם", "לאלקום", "for the people"),
        ("לִשְׁתּוֹת", "ישרבונה", "to drink."),
    ],
    15: [
        # HE: וַיִּסְעוּ מֵרְפִידִם וַיַּחֲנוּ בְּמִדְבַּר סִינָי
        # JA: ורחלו מנהא. ונזלו פי ברייה' סיני
        # EN: And they set out from Rephidim and encamped in the wilderness of Sinai.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵרְפִידִם", "מנהא", "from Rephidim"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּמִדְבַּר סִינָי", "פי ברייה' סיני", "in the wilderness of Sinai."),
    ],
    16: [
        # HE: וַיִּסְעוּ מִמִּדְבַּר סִינָי וַיַּחֲנוּ בְּקִבְרֹת הַתַּאֲוָה
        # JA: ורחלו מנהא. ונזלו פי קבור אלמתשהיין
        # EN: And they set out from the wilderness of Sinai and encamped at the Graves of the Desirous.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִמִּדְבַּר סִינָי", "מנהא", "from the wilderness of Sinai"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּקִבְרֹת הַתַּאֲוָה", "פי קבור אלמתשהיין", "at the Graves of the Desirous."),
    ],
    17: [
        # HE: וַיִּסְעוּ מִקִּבְרֹת הַתַּאֲוָה וַיַּחֲנוּ בַּחֲצֵרֹת
        # JA: ורחלו מנהא. ונזלו פי חצרות
        # EN: And they set out from the Graves of the Desirous and encamped at Hazeroth.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִקִּבְרֹת הַתַּאֲוָה", "מנהא", "from the Graves of the Desirous"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בַּחֲצֵרֹת", "פי חצרות", "at Hazeroth."),
    ],
    18: [
        # HE: וַיִּסְעוּ מֵחֲצֵרֹת וַיַּחֲנוּ בְּרִתְמָה
        # JA: ורחלו מנהא. ונזלו פי רתמה
        # EN: And they set out from Hazeroth and encamped at Rithmah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵחֲצֵרֹת", "מנהא", "from Hazeroth"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּרִתְמָה", "פי רתמה", "at Rithmah."),
    ],
    19: [
        # HE: וַיִּסְעוּ מֵרִתְמָה וַיַּחֲנוּ בְּרִמֹּן פָּרֶץ
        # JA: ורחלו מנהא. ונזלו פי רמון פרץ
        # EN: And they set out from Rithmah and encamped at Rimmon-Perez.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵרִתְמָה", "מנהא", "from Rithmah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּרִמֹּן פָּרֶץ", "פי רמון פרץ", "at Rimmon-Perez."),
    ],
    20: [
        # HE: וַיִּסְעוּ מֵרִמֹּן פָּרֶץ וַיַּחֲנוּ בְּלִבְנָה
        # JA: ורחלו מנהא. ונזלו פי לבנה
        # EN: And they set out from Rimmon-Perez and encamped at Libnah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵרִמֹּן פָּרֶץ", "מנהא", "from Rimmon-Perez"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּלִבְנָה", "פי לבנה", "at Libnah."),
    ],
    21: [
        # HE: וַיִּסְעוּ מִלִּבְנָה וַיַּחֲנוּ בְּרִסָּה
        # JA: ורחלו מנהא. ונזלו פי רסה
        # EN: And they set out from Libnah and encamped at Rissah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִלִּבְנָה", "מנהא", "from Libnah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּרִסָּה", "פי רסה", "at Rissah."),
    ],
    22: [
        # HE: וַיִּסְעוּ מֵרִסָּה וַיַּחֲנוּ בִּקְהֵלָתָה
        # JA: ורחלו מנהא. ונזלו פי קהלת
        # EN: And they set out from Rissah and encamped at Kehelath.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵרִסָּה", "מנהא", "from Rissah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בִּקְהֵלָתָה", "פי קהלת", "at Kehelath."),
    ],
    23: [
        # HE: וַיִּסְעוּ מִקְּהֵלָתָה וַיַּחֲנוּ בְּהַר-שָׁפֶר
        # JA: ורחלו מנהא. ונזלו פי גבל שפר
        # EN: And they set out from Kehelath and encamped at Mount Shepher.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִקְּהֵלָתָה", "מנהא", "from Kehelath"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּהַר-שָׁפֶר", "פי גבל שפר", "at Mount Shepher."),
    ],
    24: [
        # HE: וַיִּסְעוּ מֵהַר-שָׁפֶר וַיַּחֲנוּ בַּחֲרָדָה
        # JA: ורחלו מנהא. ונזלו פי חרדה
        # EN: And they set out from Mount Shepher and encamped at Haradah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵהַר-שָׁפֶר", "מנהא", "from Mount Shepher"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בַּחֲרָדָה", "פי חרדה", "at Haradah."),
    ],
    25: [
        # HE: וַיִּסְעוּ מֵחֲרָדָה וַיַּחֲנוּ בְּמַקְהֵלֹת
        # JA: ורחלו מנהא. ונזלו פי מקהלות
        # EN: And they set out from Haradah and encamped at Makheloth.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵחֲרָדָה", "מנהא", "from Haradah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּמַקְהֵלֹת", "פי מקהלות", "at Makheloth."),
    ],
    26: [
        # HE: וַיִּסְעוּ מִמַּקְהֵלֹת וַיַּחֲנוּ בְּתָחַת
        # JA: ורחלו מנהא. ונזלו פי תחת
        # EN: And they set out from Makheloth and encamped at Tahath.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִמַּקְהֵלֹת", "מנהא", "from Makheloth"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּתָחַת", "פי תחת", "at Tahath."),
    ],
    27: [
        # HE: וַיִּסְעוּ מִתָּחַת וַיַּחֲנוּ בְּתָרַח
        # JA: ורחלו מנהא. ונזלו פי תרח
        # EN: And they set out from Tahath and encamped at Terah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִתָּחַת", "מנהא", "from Tahath"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּתָרַח", "פי תרח", "at Terah."),
    ],
    28: [
        # HE: וַיִּסְעוּ מִתָּרַח וַיַּחֲנוּ בְּמִתְקָה
        # JA: ורחלו מנהא. ונזלו פי מתקה
        # EN: And they set out from Terah and encamped at Mithkah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִתָּרַח", "מנהא", "from Terah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּמִתְקָה", "פי מתקה", "at Mithkah."),
    ],
    29: [
        # HE: וַיִּסְעוּ מִמִּתְקָה וַיַּחֲנוּ בְּחַשְׁמֹנָה
        # JA: ורחלו מנהא. ונזלו פי חשמונה
        # EN: And they set out from Mithkah and encamped at Hashmonah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִמִּתְקָה", "מנהא", "from Mithkah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּחַשְׁמֹנָה", "פי חשמונה", "at Hashmonah."),
    ],
    30: [
        # HE: וַיִּסְעוּ מֵחַשְׁמֹנָה וַיַּחֲנוּ בְּמֹסֵרוֹת
        # JA: ורחלו מנהא. ונזלו פי מוסרות
        # EN: And they set out from Hashmonah and encamped at Moseroth.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵחַשְׁמֹנָה", "מנהא", "from Hashmonah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּמֹסֵרוֹת", "פי מוסרות", "at Moseroth."),
    ],
    31: [
        # HE: וַיִּסְעוּ מִמֹּסֵרוֹת וַיַּחֲנוּ בִּבְנֵי יַעֲקָן
        # JA: ורחלו מנהא. ונזלו פי בני יעקן
        # EN: And they set out from Moseroth and encamped at Bene-Yaakan.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִמֹּסֵרוֹת", "מנהא", "from Moseroth"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בִּבְנֵי יַעֲקָן", "פי בני יעקן", "at Bene-Yaakan."),
    ],
    32: [
        # HE: וַיִּסְעוּ מִבְּנֵי יַעֲקָן וַיַּחֲנוּ בְּחֹר הַגִּדְגָּד
        # JA: ורחלו מנהא. ונזלו פי חור גדגד
        # EN: And they set out from Bene-Yaakan and encamped at Hor-Haggidgad.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִבְּנֵי יַעֲקָן", "מנהא", "from Bene-Yaakan"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּחֹר הַגִּדְגָּד", "פי חור גדגד", "at Hor-Haggidgad."),
    ],
    33: [
        # HE: וַיִּסְעוּ מֵחֹר הַגִּדְגָּד וַיַּחֲנוּ בְּיָטְבָתָה
        # JA: ורחלו מנהא. ונזלו פי יטבתא
        # EN: And they set out from Hor-Haggidgad and encamped at Yotbathah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵחֹר הַגִּדְגָּד", "מנהא", "from Hor-Haggidgad"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּיָטְבָתָה", "פי יטבתא", "at Yotbathah."),
    ],
    34: [
        # HE: וַיִּסְעוּ מִיָּטְבָתָה וַיַּחֲנוּ בְּעַבְרֹנָה
        # JA: ורחלו מנהא. ונזלו פי עברונה
        # EN: And they set out from Yotbathah and encamped at Abronah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִיָּטְבָתָה", "מנהא", "from Yotbathah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּעַבְרֹנָה", "פי עברונה", "at Abronah."),
    ],
    35: [
        # HE: וַיִּסְעוּ מֵעַבְרֹנָה וַיַּחֲנוּ בְּעֶצְיֹן גָּבֶר
        # JA: ורחלו מנהא. ונזלו פי עציון גבר
        # EN: And they set out from Abronah and encamped at Ezion-Gaber.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵעַבְרֹנָה", "מנהא", "from Abronah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּעֶצְיֹן גָּבֶר", "פי עציון גבר", "at Ezion-Gaber."),
    ],
    36: [
        # HE: וַיִּסְעוּ מֵעֶצְיֹן גָּבֶר וַיַּחֲנוּ בְמִדְבַּר-צִן הִוא קָדֵשׁ
        # JA: ורחלו מנהא. ונזלו פי ברייה' צין הי רקים
        # EN: And they set out from Ezion-Gaber and encamped in the wilderness of Zin — that is Reqem.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵעֶצְיֹן גָּבֶר", "מנהא", "from Ezion-Gaber"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְמִדְבַּר-צִן", "פי ברייה' צין", "in the wilderness of Zin —"),
        ("הִוא קָדֵשׁ", "הי רקים", "that is Reqem."),
    ],
    37: [
        # HE: וַיִּסְעוּ מִקָּדֵשׁ וַיַּחֲנוּ בְּהֹר הָהָר בִּקְצֵה אֶרֶץ אֱדוֹם
        # JA: ורחלו מנהא. ונזלו פי גבל הור. פי טרף בלד אדום
        # EN: And they set out from Reqem and encamped at Mount Hor, at the edge of the land of Edom.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִקָּדֵשׁ", "מנהא", "from Reqem"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּהֹר הָהָר", "פי גבל הור", "at Mount Hor,"),
        ("בִּקְצֵה אֶרֶץ אֱדוֹם", "פי טרף בלד אדום", "at the edge of the land of Edom."),
    ],
    38: [
        # HE: וַיַּעַל אַהֲרֹן הַכֹּהֵן אֶל-הֹר הָהָר עַל-פִּי יְהוָה--וַיָּמָת שָׁם בִּשְׁנַת הָאַרְבָּעִים לְצֵאת בְּנֵי-יִשְׂרָאֵל מֵאֶרֶץ מִצְרַיִם בַּחֹדֶשׁ הַחֲמִישִׁי בְּאֶחָד לַחֹדֶשׁ
        # JA: פצעד הרון אלאמאם. אלי' גבל הור. ומאת ת'ם באמר אללה פי סנה' אלארבעין. לכ'רוג בני אסראיל מן בלד מצר. פי אליום אלאוול מן אלשהר אלכ'אמס
        # EN: And Aaron the imām ascended to Mount Hor, and died there at the command of God, in the fortieth year of the going out of the sons of Israel from the land of Egypt, on the first day of the fifth month.
        ("וַיַּעַל", "פצעד", "And Aaron the imām ascended"),
        ("אַהֲרֹן הַכֹּהֵן", "הרון אלאמאם", "to Mount Hor,"),
        ("אֶל-הֹר הָהָר", "אלי' גבל הור", "and died there"),
        ("וַיָּמָת שָׁם", "ומאת ת'ם", "at the command of"),
        ("עַל-פִּי יְהוָה", "באמר אללה", "God,"),
        ("בִּשְׁנַת הָאַרְבָּעִים", "פי סנה' אלארבעין", "in the fortieth year"),
        ("לְצֵאת בְּנֵי-יִשְׂרָאֵל", "לכ'רוג בני אסראיל", "of the going out of the sons of Israel"),
        ("מֵאֶרֶץ מִצְרַיִם", "מן בלד מצר", "from the land of Egypt,"),
        ("בְּאֶחָד לַחֹדֶשׁ", "פי אליום אלאוול", "on the first day of the"),
        ("בַּחֹדֶשׁ הַחֲמִישִׁי", "מן אלשהר אלכ'אמס", "fifth month."),
    ],
    39: [
        # HE: וְאַהֲרֹן בֶּן-שָׁלֹשׁ וְעֶשְׂרִים וּמְאַת שָׁנָה בְּמֹתוֹ בְּהֹר הָהָר
        # JA: וכאן להרון. מאיה ות'לאת'ה ועשרין סנה. למא מאת הנאך
        # EN: And Aaron was a hundred and twenty-three years old when he died there.
        ("וְאַהֲרֹן", "וכאן להרון", "And Aaron was"),
        ("בֶּן-שָׁלֹשׁ וְעֶשְׂרִים וּמְאַת שָׁנָה", "מאיה ות'לאת'ה ועשרין סנה", "a hundred and twenty-three years old"),
        ("בְּמֹתוֹ", "למא מאת", "when he died"),
        ("בְּהֹר הָהָר", "הנאך", "there."),
    ],
    40: [
        # HE: וַיִּשְׁמַע הַכְּנַעֲנִי מֶלֶךְ עֲרָד וְהוּא-יֹשֵׁב בַּנֶּגֶב בְּאֶרֶץ כְּנָעַן--בְּבֹא בְּנֵי יִשְׂרָאֵל
        # JA: ת'ם סמע אלכנאעני מלך ערד. והו סאכן פי אלדארום פי בלד כנעאן במגי בני אסראיל
        # EN: Then the Canaanite, the king of Arad — who was dwelling in the south in the land of Canaan — heard of the coming of the sons of Israel.
        (None, "ת'ם", "Then"),
        ("וַיִּשְׁמַע", "סמע", "heard"),
        ("הַכְּנַעֲנִי", "אלכנאעני", "the Canaanite,"),
        ("מֶלֶךְ עֲרָד", "מלך ערד", "the king of Arad —"),
        ("וְהוּא-יֹשֵׁב", "והו סאכן", "who was dwelling"),
        ("בַּנֶּגֶב", "פי אלדארום", "in the south"),
        ("בְּאֶרֶץ כְּנָעַן", "פי בלד כנעאן", "in the land of Canaan —"),
        ("בְּבֹא בְּנֵי יִשְׂרָאֵל", "במגי בני אסראיל", "of the coming of the sons of Israel."),
    ],
    41: [
        # HE: וַיִּסְעוּ מֵהֹר הָהָר וַיַּחֲנוּ בְּצַלְמֹנָה
        # JA: ת'ם רחלו מן גבל הור. ונזלו פי צלמונה
        # EN: Then they set out from Mount Hor and encamped at Zalmonah.
        ("וַיִּסְעוּ", "ת'ם רחלו", "Then they set out"),
        ("מֵהֹר הָהָר", "מן גבל הור", "from Mount Hor"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּצַלְמֹנָה", "פי צלמונה", "at Zalmonah."),
    ],
    42: [
        # HE: וַיִּסְעוּ מִצַּלְמֹנָה וַיַּחֲנוּ בְּפוּנֹן
        # JA: ורחלו מנהא. ונזלו פי פונון
        # EN: And they set out from Zalmonah and encamped at Punon.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִצַּלְמֹנָה", "מנהא", "from Zalmonah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּפוּנֹן", "פי פונון", "at Punon."),
    ],
    43: [
        # HE: וַיִּסְעוּ מִפּוּנֹן וַיַּחֲנוּ בְּאֹבֹת
        # JA: ורחלו מנהא. ונזלו פי אובות
        # EN: And they set out from Punon and encamped at Oboth.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִפּוּנֹן", "מנהא", "from Punon"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּאֹבֹת", "פי אובות", "at Oboth."),
    ],
    44: [
        # HE: וַיִּסְעוּ מֵאֹבֹת וַיַּחֲנוּ בְּעִיֵּי הָעֲבָרִים בִּגְבוּל מוֹאָב
        # JA: ורחלו מנהא. ונזלו פי עיי אלמגאז. פי תכ'ם מואב
        # EN: And they set out from Oboth and encamped at Iye ha-Maʿaz, on the border of Moab.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵאֹבֹת", "מנהא", "from Oboth"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּעִיֵּי הָעֲבָרִים", "פי עיי אלמגאז", "at Iye ha-Maʿaz,"),
        ("בִּגְבוּל מוֹאָב", "פי תכ'ם מואב", "on the border of Moab."),
    ],
    45: [
        # HE: וַיִּסְעוּ מֵעִיִּים וַיַּחֲנוּ בְּדִיבֹן גָּד
        # JA: ורחלו מנהא. ונזלו פי דיבון גד
        # EN: And they set out from Iye ha-Maʿaz and encamped at Dibon-Gad.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵעִיִּים", "מנהא", "from Iye ha-Maʿaz"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּדִיבֹן גָּד", "פי דיבון גד", "at Dibon-Gad."),
    ],
    46: [
        # HE: וַיִּסְעוּ מִדִּיבֹן גָּד וַיַּחֲנוּ בְּעַלְמֹן דִּבְלָתָיְמָה
        # JA: ורחלו מנהא. ונזלו פי עלמון דבלתים
        # EN: And they set out from Dibon-Gad and encamped at Almon-Diblathaimah.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מִדִּיבֹן גָּד", "מנהא", "from Dibon-Gad"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּעַלְמֹן דִּבְלָתָיְמָה", "פי עלמון דבלתים", "at Almon-Diblathaimah."),
    ],
    47: [
        # HE: וַיִּסְעוּ מֵעַלְמֹן דִּבְלָתָיְמָה וַיַּחֲנוּ בְּהָרֵי הָעֲבָרִים לִפְנֵי נְבוֹ
        # JA: ורחלו מנהא. ונזלו פי גבאל אלעבריין. בין ידי נבו
        # EN: And they set out from Almon-Diblathaimah and encamped at the mountains of the Hebrews, before Nebo.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵעַלְמֹן דִּבְלָתָיְמָה", "מנהא", "from Almon-Diblathaimah"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּהָרֵי הָעֲבָרִים", "פי גבאל אלעבריין", "at the mountains of the Hebrews,"),
        ("לִפְנֵי נְבוֹ", "בין ידי נבו", "before Nebo."),
    ],
    48: [
        # HE: וַיִּסְעוּ מֵהָרֵי הָעֲבָרִים וַיַּחֲנוּ בְּעַרְבֹת מוֹאָב עַל יַרְדֵּן יְרֵחוֹ
        # JA: ורחלו מנהא. ונזלו פי בידאת מואב. עלי' ארדן יריחא
        # EN: And they set out from the mountains of the Hebrews and encamped in the open country of Moab, by the Jordan of Jericho.
        ("וַיִּסְעוּ", "ורחלו", "And they set out"),
        ("מֵהָרֵי הָעֲבָרִים", "מנהא", "from the mountains of the Hebrews"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּעַרְבֹת מוֹאָב", "פי בידאת מואב", "in the open country of Moab,"),
        ("עַל יַרְדֵּן יְרֵחוֹ", "עלי' ארדן יריחא", "by the Jordan of Jericho."),
    ],
    49: [
        # HE: וַיַּחֲנוּ עַל-הַיַּרְדֵּן מִבֵּית הַיְשִׁמֹת עַד אָבֵל הַשִּׁטִּים בְּעַרְבֹת מוֹאָב
        # JA: פנזלו עלי' אלארדן מן בית ישימות. אלי' מרג שטין. וד'אלך פי בידאת מואב
        # EN: And they encamped by the Jordan, from Beth-Jeshimoth to the meadow of the Acacias — that being in the open country of Moab.
        ("וַיַּחֲנוּ", "פנזלו", "And they encamped"),
        ("עַל-הַיַּרְדֵּן", "עלי' אלארדן", "by the Jordan,"),
        ("מִבֵּית הַיְשִׁמֹת", "מן בית ישימות", "from Beth-Jeshimoth"),
        ("עַד אָבֵל הַשִּׁטִּים", "אלי' מרג שטין", "to the meadow of the Acacias —"),
        ("בְּעַרְבֹת מוֹאָב", "וד'אלך פי בידאת מואב", "that being in the open country of Moab."),
    ],
    50: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה בְּעַרְבֹת מוֹאָב עַל-יַרְדֵּן יְרֵחוֹ לֵאמֹר
        # JA: פכלם אללה מוסי' פי בידאת מואב. עלי' ארדן יריחא תכלימא
        # EN: And God spoke to Moses in the open country of Moab, by the Jordan of Jericho directly.
        ("וַיְדַבֵּר", "פכלם", "And God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי'", "in the open country of"),
        ("בְּעַרְבֹת מוֹאָב", "פי בידאת מואב", "Moab,"),
        ("עַל-יַרְדֵּן יְרֵחוֹ", "עלי' ארדן יריחא", "by the Jordan of Jericho"),
        ("לֵאמֹר", "תכלימא", "directly."),
    ],
    51: [
        # HE: דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם כִּי אַתֶּם עֹבְרִים אֶת-הַיַּרְדֵּן אֶל-אֶרֶץ כְּנָעַן
        # JA: מר בני אסראיל וקל להם. אנכם גאיזין אלארדן אלי' בלד כנעאן
        # EN: Command the sons of Israel and say to them: You are crossing the Jordan into the land of Canaan.
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("כִּי אַתֶּם", "אנכם", "You are"),
        ("עֹבְרִים", "גאיזין", "crossing"),
        ("אֶת-הַיַּרְדֵּן", "אלארדן", "the Jordan"),
        ("אֶל-אֶרֶץ כְּנָעַן", "אלי' בלד כנעאן", "into the land of Canaan."),
    ],
    52: [
        # HE: וְהוֹרַשְׁתֶּם אֶת-כָּל-יֹשְׁבֵי הָאָרֶץ מִפְּנֵיכֶם וְאִבַּדְתֶּם אֵת כָּל-מַשְׂכִּיֹּתָם וְאֵת כָּל-צַלְמֵי מַסֵּכֹתָם תְּאַבֵּדוּ וְאֵת כָּל-בָּמוֹתָם תַּשְׁמִידוּ
        # JA: פאקרצ'ו גמיע אהל אלבלד מן בין ידיכם. ואבידו גמיע מזכ'רפאתהם. ואצנאם מסבוכאתהם. וביעהם תנפד'ון
        # EN: And drive out all the inhabitants of the land from before you, and destroy all their ornaments and their graven idols; and their temples of worship you shall demolish.
        ("וְהוֹרַשְׁתֶּם", "פאקרצ'ו", "And drive out"),
        ("אֶת-כָּל-יֹשְׁבֵי הָאָרֶץ", "גמיע אהל אלבלד", "all the inhabitants of the land"),
        ("מִפְּנֵיכֶם", "מן בין ידיכם", "from before you,"),
        ("וְאִבַּדְתֶּם", "ואבידו", "and destroy"),
        ("אֵת כָּל-מַשְׂכִּיֹּתָם", "גמיע מזכ'רפאתהם", "all their ornaments"),
        ("וְאֵת כָּל-צַלְמֵי מַסֵּכֹתָם תְּאַבֵּדוּ", "ואצנאם מסבוכאתהם", "and their graven idols;"),
        ("וְאֵת כָּל-בָּמוֹתָם תַּשְׁמִידוּ", "וביעהם תנפד'ון", "and their temples of worship you shall demolish."),
    ],
    53: [
        # HE: וְהוֹרַשְׁתֶּם אֶת-הָאָרֶץ וִישַׁבְתֶּם-בָּהּ כִּי לָכֶם נָתַתִּי אֶת-הָאָרֶץ לָרֶשֶׁת אֹתָהּ
        # JA: פאד'א קרצ'תמוהם אסכנו אלבלד. פקד אעטיתכם אייאה לתחוזוהו
        # EN: And when you have driven them out, settle the land — for I have given it to you that you may possess it.
        ("וְהוֹרַשְׁתֶּם", "פאד'א קרצ'תמוהם", "And when you have driven them out,"),
        ("וִישַׁבְתֶּם-בָּהּ", "אסכנו אלבלד", "settle the land —"),
        ("כִּי לָכֶם", "פקד אעטיתכם", "for I have given it to you"),
        ("נָתַתִּי אֶת-הָאָרֶץ", "אייאה", "that you may"),
        ("לָרֶשֶׁת אֹתָהּ", "לתחוזוהו", "possess it."),
    ],
    54: [
        # HE: וְהִתְנַחַלְתֶּם אֶת-הָאָרֶץ בְּגוֹרָל לְמִשְׁפְּחֹתֵיכֶם לָרַב תַּרְבּוּ אֶת-נַחֲלָתוֹ וְלַמְעַט תַּמְעִיט אֶת-נַחֲלָתוֹ--אֶל אֲשֶׁר-יֵצֵא לוֹ שָׁמָּה הַגּוֹרָל לוֹ יִהְיֶה לְמַטּוֹת אֲבֹתֵיכֶם תִּתְנֶחָלוּ
        # JA: ותווזעוה באסהם לעשאירכם. לאלכת'יר כת'רו נחלתה ולאלקליל קללוהא. מן כ'רג לה אלסהם פי אי מוצ'ע כאן לה. ועלי' אסבאט אבאיכם תתוזעונה
        # EN: And you shall apportion it by equal shares among your clans: for the numerous enlarge his portion, and for the few reduce it. To whomever his share falls, in whatever place it may be, that shall be his; according to the tribes of your fathers you shall apportion it.
        ("וְהִתְנַחַלְתֶּם", "ותווזעוה", "And you shall apportion it"),
        ("בְּגוֹרָל", "באסהם", "by equal shares"),
        ("לְמִשְׁפְּחֹתֵיכֶם", "לעשאירכם", "among your clans:"),
        ("לָרַב תַּרְבּוּ אֶת-נַחֲלָתוֹ", "לאלכת'יר כת'רו נחלתה", "for the numerous enlarge his portion,"),
        ("וְלַמְעַט תַּמְעִיט אֶת-נַחֲלָתוֹ", "ולאלקליל קללוהא", "and for the few reduce it."),
        ("אֶל אֲשֶׁר-יֵצֵא לוֹ שָׁמָּה הַגּוֹרָל", "מן כ'רג לה אלסהם פי אי מוצ'ע כאן לה", "To whomever his share falls, in whatever place it may be, that shall be his;"),
        ("לְמַטּוֹת אֲבֹתֵיכֶם תִּתְנֶחָלוּ", "ועלי' אסבאט אבאיכם תתוזעונה", "according to the tribes of your fathers you shall apportion it."),
    ],
    55: [
        # HE: וְאִם-לֹא תוֹרִישׁוּ אֶת-יֹשְׁבֵי הָאָרֶץ מִפְּנֵיכֶם--וְהָיָה אֲשֶׁר תּוֹתִירוּ מֵהֶם לְשִׂכִּים בְּעֵינֵיכֶם וְלִצְנִינִם בְּצִדֵּיכֶם וְצָרְרוּ אֶתְכֶם--עַל-הָאָרֶץ אֲשֶׁר אַתֶּם יֹשְׁבִים בָּהּ
        # JA: ואן לם תקרצ'ו אהל אלבלד מן בין ידיכם. פיציר מא תבקונה מנהם. כאבר פי עיונכם. וכמסאל פי גנובכם. ויצ'איקונכם פי אלבלד. אלד'י אנתם מקימין פיה
        # EN: But if you do not drive out the inhabitants of the land from before you, then whatever you leave of them shall become like fine needles in your eyes and like thick thorns in your sides, and they shall press hard upon you in the land in which you are settled.
        ("וְאִם-לֹא תוֹרִישׁוּ", "ואן לם תקרצ'ו", "But if you do not drive out"),
        ("אֶת-יֹשְׁבֵי הָאָרֶץ", "אהל אלבלד", "the inhabitants of the land"),
        ("מִפְּנֵיכֶם", "מן בין ידיכם", "from before you,"),
        ("וְהָיָה אֲשֶׁר תּוֹתִירוּ מֵהֶם", "פיציר מא תבקונה מנהם", "then whatever you leave of them shall become"),
        ("לְשִׂכִּים בְּעֵינֵיכֶם", "כאבר פי עיונכם", "like fine needles in your eyes"),
        ("וְלִצְנִינִם בְּצִדֵּיכֶם", "וכמסאל פי גנובכם", "and like thick thorns in your sides,"),
        ("וְצָרְרוּ אֶתְכֶם", "ויצ'איקונכם", "and they shall press hard upon you"),
        ("עַל-הָאָרֶץ אֲשֶׁר אַתֶּם יֹשְׁבִים בָּהּ", "פי אלבלד. אלד'י אנתם מקימין פיה", "in the land in which you are settled."),
    ],
    56: [
        # HE: וְהָיָה כַּאֲשֶׁר דִּמִּיתִי לַעֲשׂוֹת לָהֶם--אֶעֱשֶׂה לָכֶם
        # JA: פאכון כמא קצדת. אן אצנע בהם אצנע בכם
        # EN: And it shall be: just as I intended to do to them, so shall I do to you.
        ("וְהָיָה", "פאכון", "And it shall be:"),
        ("כַּאֲשֶׁר דִּמִּיתִי", "כמא קצדת", "just as I intended"),
        ("לַעֲשׂוֹת לָהֶם", "אן אצנע בהם", "to do to them,"),
        ("אֶעֱשֶׂה לָכֶם", "אצנע בכם", "so shall I do to you."),
    ],
}

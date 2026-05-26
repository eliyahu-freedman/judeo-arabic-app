"""Hand-authored word-level alignment triples for Bamidbar chapter 30."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיֹּאמֶר מֹשֶׁה אֶל-בְּנֵי יִשְׂרָאֵל כְּכֹל אֲשֶׁר-צִוָּה יְהוָה אֶת-מֹשֶׁה
        # JA: ת'ם קאל מוסי' לבני אסראיל. כגמיע מא אמרה אללה בה
        # EN: Then Moses said to the sons of Israel all that God had commanded him.
        (None, "ת'ם", "Then"),
        ("וַיֹּאמֶר", "קאל", "Moses said"),
        ("מֹשֶׁה", "מוסי'", "to the sons of"),
        ("אֶל-בְּנֵי", "לבני", "Israel"),
        ("יִשְׂרָאֵל", "אסראיל", "all that"),
        ("כְּכֹל אֲשֶׁר-צִוָּה", "כגמיע מא אמרה", "God had commanded"),
        ("יְהוָה אֶת-מֹשֶׁה", "אללה בה", "him."),
    ],
    2: [
        # HE: וַיְדַבֵּר מֹשֶׁה אֶל-רָאשֵׁי הַמַּטּוֹת לִבְנֵי יִשְׂרָאֵל לֵאמֹר זֶה הַדָּבָר אֲשֶׁר צִוָּה יְהוָה
        # JA: ת'ם כלם מוסי' רויסא אלאסבאט. אלד'י לבני אסראיל קאילא. הד'א אלאמר. אלד'י אמר אללה בה
        # EN: Then Moses spoke to the heads of the tribes of the sons of Israel, saying: 'This is the matter which God has commanded.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "Moses spoke"),
        ("מֹשֶׁה", "מוסי'", "to the heads of"),
        ("אֶל-רָאשֵׁי", "רויסא", "the tribes of"),
        ("הַמַּטּוֹת", "אלאסבאט", "the sons of"),
        ("לִבְנֵי יִשְׂרָאֵל", "אלד'י לבני אסראיל", "Israel,"),
        ("לֵאמֹר", "קאילא", "saying:"),
        ("זֶה", "הד'א", "'This is"),
        ("הַדָּבָר", "אלאמר", "the matter"),
        ("אֲשֶׁר צִוָּה", "אלד'י אמר", "which God has"),
        ("יְהוָה", "אללה בה", "commanded."),
    ],
    3: [
        # HE: אִישׁ כִּי-יִדֹּר נֶדֶר לַיהוָה אוֹ-הִשָּׁבַע שְׁבֻעָה לֶאְסֹר אִסָּר עַל-נַפְשׁוֹ--לֹא יַחֵל דְּבָרוֹ כְּכָל-הַיֹּצֵא מִפִּיו יַעֲשֶׂה
        # JA: אי רגל נד'ר נד'רא ללה. או חלף ימינא ליעקד עקדא עלי' נפסה. פלא יבד'ל קולה. פכל מא כ'רג מן פאה יעמל
        # EN: Any man who vows a vow to God, or swears an oath to bind a commitment upon himself — he shall not dishonor his word; all that came out of his mouth he shall do.
        ("אִישׁ", "אי רגל", "Any man"),
        ("כִּי-יִדֹּר", "נד'ר", "who vows"),
        ("נֶדֶר", "נד'רא", "a vow"),
        ("לַיהוָה", "ללה", "to God,"),
        ("אוֹ-הִשָּׁבַע", "או חלף", "or swears"),
        ("שְׁבֻעָה", "ימינא", "an oath"),
        ("לֶאְסֹר", "ליעקד", "to bind"),
        ("אִסָּר", "עקדא", "a commitment"),
        ("עַל-נַפְשׁוֹ", "עלי' נפסה", "upon himself —"),
        ("לֹא יַחֵל", "פלא יבד'ל", "he shall not dishonor"),
        ("דְּבָרוֹ", "קולה", "his word;"),
        ("כְּכָל-הַיֹּצֵא", "פכל מא כ'רג", "all that came out of"),
        ("מִפִּיו", "מן פאה", "his mouth"),
        ("יַעֲשֶׂה", "יעמל", "he shall do."),
    ],
    4: [
        # HE: וְאִשָּׁה כִּי-תִדֹּר נֶדֶר לַיהוָה וְאָסְרָה אִסָּר בְּבֵית אָבִיהָ בִּנְעֻרֶיהָ
        # JA: ואייה' אמראה נד'רת נד'רא ללה. או עקדת עקדא. פי בית אביהא פי חאל צבאיהא
        # EN: And any woman who vows a vow to God, or binds a commitment, while in her father's house, in the time of her youth —
        ("וְאִשָּׁה", "ואייה' אמראה", "And any woman"),
        ("כִּי-תִדֹּר", "נד'רת", "who vows"),
        ("נֶדֶר", "נד'רא", "a vow"),
        ("לַיהוָה", "ללה", "to God,"),
        ("וְאָסְרָה", "או עקדת", "or binds"),
        ("אִסָּר", "עקדא", "a commitment,"),
        ("בְּבֵית", "פי בית", "while in her father's"),
        ("אָבִיהָ", "אביהא", "house,"),
        ("בִּנְעֻרֶיהָ", "פי חאל צבאיהא", "in the time of her youth —"),
    ],
    5: [
        # HE: וְשָׁמַע אָבִיהָ אֶת-נִדְרָהּ וֶאֱסָרָהּ אֲשֶׁר אָסְרָה עַל-נַפְשָׁהּ וְהֶחֱרִישׁ לָהּ אָבִיהָ--וְקָמוּ כָּל-נְדָרֶיהָ וְכָל-אִסָּר אֲשֶׁר-אָסְרָה עַל-נַפְשָׁהּ יָקוּם
        # JA: פסמע אביהא נד'רהא. ועקדהא אלד'י עקדתה עלי' נפסהא ואמסך ענהא. פקד ת'בת גמיע נד'ורהא. וכל עקד עקדתה עלי' נפסהא
        # EN: and her father hears her vow and her commitment which she has bound upon herself, and holds back from her — then all her vows are established, and every commitment she has bound upon herself stands.
        ("וְשָׁמַע", "פסמע", "and her father hears"),
        ("אָבִיהָ", "אביהא", "her vow"),
        ("אֶת-נִדְרָהּ", "נד'רהא", "and her commitment"),
        ("וֶאֱסָרָהּ", "ועקדהא", "which she has bound"),
        ("אֲשֶׁר אָסְרָה", "אלד'י עקדתה", "upon herself,"),
        ("עַל-נַפְשָׁהּ", "עלי' נפסהא", "and holds back"),
        ("וְהֶחֱרִישׁ לָהּ אָבִיהָ", "ואמסך ענהא", "from her —"),
        ("וְקָמוּ", "פקד ת'בת", "then all her vows are established,"),
        ("כָּל-נְדָרֶיהָ", "גמיע נד'ורהא", "and every commitment"),
        ("וְכָל-אִסָּר", "וכל עקד", "she has bound"),
        ("אֲשֶׁר-אָסְרָה", "עקדתה", "upon herself"),
        ("עַל-נַפְשָׁהּ יָקוּם", "עלי' נפסהא", "stands."),
    ],
    6: [
        # HE: וְאִם-הֵנִיא אָבִיהָ אֹתָהּ בְּיוֹם שָׁמְעוֹ--כָּל-נְדָרֶיהָ וֶאֱסָרֶיהָ אֲשֶׁר-אָסְרָה עַל-נַפְשָׁהּ לֹא יָקוּם וַיהוָה יִסְלַח-לָהּ כִּי-הֵנִיא אָבִיהָ אֹתָהּ
        # JA: ואן אנתהרהא אביהא פי יום סמע בד'אלך. פכל נדורהא ועקודהא. אלד'י עקדתה עלי' נפסהא גי'ר ת'אבת. ואללה יג'פר להא. אד' אנתהרהא אביהא
        # EN: But if her father rebukes her on the day he hears of it, then all her vows and her commitments which she has bound upon herself are not established; and God will forgive her, since her father rebuked her.
        ("וְאִם-הֵנִיא", "ואן אנתהרהא", "But if her father rebukes her"),
        ("אָבִיהָ", "אביהא", "on the day"),
        ("בְּיוֹם שָׁמְעוֹ", "פי יום סמע בד'אלך", "he hears of it,"),
        ("כָּל-נְדָרֶיהָ", "פכל נדורהא", "then all her vows"),
        ("וֶאֱסָרֶיהָ", "ועקודהא", "and her commitments"),
        ("אֲשֶׁר-אָסְרָה", "אלד'י עקדתה", "which she has bound"),
        ("עַל-נַפְשָׁהּ", "עלי' נפסהא", "upon herself"),
        ("לֹא יָקוּם", "גי'ר ת'אבת", "are not established;"),
        ("וַיהוָה", "ואללה", "and God will"),
        ("יִסְלַח-לָהּ", "יג'פר להא", "forgive her,"),
        ("כִּי-הֵנִיא", "אד' אנתהרהא", "since her father"),
        ("אָבִיהָ אֹתָהּ", "אביהא", "rebuked her."),
    ],
    7: [
        # HE: וְאִם-הָיוֹ תִהְיֶה לְאִישׁ וּנְדָרֶיהָ עָלֶיהָ אוֹ מִבְטָא שְׂפָתֶיהָ אֲשֶׁר אָסְרָה עַל-נַפְשָׁהּ
        # JA: ואן צארת לרגל. ונד'ורהא עליהא. או לפץ' שפתיהא. אלד'י עקדתה עלי' נפסהא
        # EN: And if she becomes a man's wife, while her vows are upon her, or the utterance of her lips which she has bound upon herself —
        ("וְאִם-הָיוֹ תִהְיֶה", "ואן צארת", "And if she becomes"),
        ("לְאִישׁ", "לרגל", "a man's wife,"),
        ("וּנְדָרֶיהָ", "ונד'ורהא", "while her vows"),
        ("עָלֶיהָ", "עליהא", "are upon her,"),
        ("אוֹ מִבְטָא", "או לפץ'", "or the utterance of"),
        ("שְׂפָתֶיהָ", "שפתיהא", "her lips"),
        ("אֲשֶׁר אָסְרָה", "אלד'י עקדתה", "which she has bound"),
        ("עַל-נַפְשָׁהּ", "עלי' נפסהא", "upon herself —"),
    ],
    8: [
        # HE: וְשָׁמַע אִישָׁהּ בְּיוֹם שָׁמְעוֹ וְהֶחֱרִישׁ לָהּ וְקָמוּ נְדָרֶיהָ וֶאֱסָרֶהָ אֲשֶׁר-אָסְרָה עַל-נַפְשָׁהּ--יָקֻמוּ
        # JA: פסמע בעלהא. פי יום סמע ואמסך ענהא. פקד ת'בת נד'ורהא ועקודהא. אלד'י עקדת עלי' נפסהא
        # EN: and her husband hears, on the day he hears of it, and holds back from her — then her vows and her commitments which she has bound upon herself are established.
        ("וְשָׁמַע", "פסמע", "and her husband hears,"),
        ("אִישָׁהּ", "בעלהא", "on the day"),
        ("בְּיוֹם שָׁמְעוֹ", "פי יום סמע", "he hears of it,"),
        ("וְהֶחֱרִישׁ לָהּ", "ואמסך ענהא", "and holds back from her —"),
        ("וְקָמוּ", "פקד ת'בת", "then her vows"),
        ("נְדָרֶיהָ", "נד'ורהא", "and her commitments"),
        ("וֶאֱסָרֶהָ", "ועקודהא", "which she has bound"),
        ("אֲשֶׁר-אָסְרָה", "אלד'י עקדת", "upon herself"),
        ("עַל-נַפְשָׁהּ--יָקֻמוּ", "עלי' נפסהא", "are established."),
    ],
    9: [
        # HE: וְאִם בְּיוֹם שְׁמֹעַ אִישָׁהּ יָנִיא אוֹתָהּ וְהֵפֵר אֶת-נִדְרָהּ אֲשֶׁר עָלֶיהָ וְאֵת מִבְטָא שְׂפָתֶיהָ אֲשֶׁר אָסְרָה עַל-נַפְשָׁהּ--וַיהוָה יִסְלַח-לָהּ
        # JA: ואן אנתהרהא בעלהא פי יום סמע בד'אלך. ופסך' נד'ורהא אלד'י עליהא. ולפץ' שפתיהא. אלד'י עקדתה עלי' נפסהא. ואללה יג'פר להא
        # EN: But if her husband rebukes her on the day he hears of it, and annuls her vows which are upon her and the utterance of her lips which she has bound upon herself — then God will forgive her.
        ("וְאִם", "ואן", "But if"),
        ("בְּיוֹם שְׁמֹעַ", "בעלהא פי יום סמע", "her husband rebukes her on the day"),
        ("אִישָׁהּ יָנִיא אוֹתָהּ", "אנתהרהא", "he hears of it,"),
        ("וְהֵפֵר", "ופסך'", "and annuls"),
        ("אֶת-נִדְרָהּ", "נד'ורהא", "her vows"),
        ("אֲשֶׁר עָלֶיהָ", "אלד'י עליהא", "which are upon her"),
        ("וְאֵת מִבְטָא", "ולפץ'", "and the utterance of"),
        ("שְׂפָתֶיהָ", "שפתיהא", "her lips"),
        ("אֲשֶׁר אָסְרָה", "אלד'י עקדתה", "which she has bound"),
        ("עַל-נַפְשָׁהּ", "עלי' נפסהא", "upon herself —"),
        ("וַיהוָה", "ואללה", "then God will"),
        ("יִסְלַח-לָהּ", "יג'פר להא", "forgive her."),
    ],
    10: [
        # HE: וְנֵדֶר אַלְמָנָה וּגְרוּשָׁה--כֹּל אֲשֶׁר-אָסְרָה עַל-נַפְשָׁהּ יָקוּם עָלֶיהָ
        # JA: ונד'ר אלארמלה ואלמטלקה. פגמיע מא עקדתה עלי' נפסהא פת'אבת עליהא
        # EN: And the vow of a widow or a divorced woman — all that she has bound upon herself is established upon her.
        ("וְנֵדֶר", "ונד'ר", "And the vow of"),
        ("אַלְמָנָה", "אלארמלה", "a widow"),
        ("וּגְרוּשָׁה", "ואלמטלקה", "or a divorced woman —"),
        ("כֹּל אֲשֶׁר-אָסְרָה", "פגמיע מא עקדתה", "all that she has bound"),
        ("עַל-נַפְשָׁהּ", "עלי' נפסהא", "upon herself"),
        ("יָקוּם", "פת'אבת", "is established"),
        ("עָלֶיהָ", "עליהא", "upon her."),
    ],
    11: [
        # HE: וְאִם-בֵּית אִישָׁהּ נָדָרָה אוֹ-אָסְרָה אִסָּר עַל-נַפְשָׁהּ בִּשְׁבֻעָה
        # JA: ואן כאן פי בית זוגהא נד'רת. או עקדת עקדא. עלי' נפסהא בימין
        # EN: And if she was in her husband's house when she vowed, or bound a commitment upon herself by oath —
        ("וְאִם-בֵּית", "ואן כאן פי בית", "And if she was in her husband's"),
        ("אִישָׁהּ", "זוגהא", "house"),
        ("נָדָרָה", "נד'רת", "when she vowed,"),
        ("אוֹ-אָסְרָה", "או עקדת", "or bound"),
        ("אִסָּר", "עקדא", "a commitment"),
        ("עַל-נַפְשָׁהּ", "עלי' נפסהא", "upon herself"),
        ("בִּשְׁבֻעָה", "בימין", "by oath —"),
    ],
    12: [
        # HE: וְשָׁמַע אִישָׁהּ וְהֶחֱרִשׁ לָהּ לֹא הֵנִיא אֹתָהּ--וְקָמוּ כָּל-נְדָרֶיהָ וְכָל-אִסָּר אֲשֶׁר-אָסְרָה עַל-נַפְשָׁהּ יָקוּם
        # JA: פסמע בעלהא ואמסך ענהא. ולם ינתהרהא. פקד ת'בת גמיע נדורהא. וכל עקד עקדתה עלי' נפסהא
        # EN: and her husband heard, and held back from her, and did not rebuke her — then all her vows and every commitment she has bound upon herself are established.
        ("וְשָׁמַע", "פסמע", "and her husband heard,"),
        ("אִישָׁהּ", "בעלהא", "and held back"),
        ("וְהֶחֱרִשׁ לָהּ", "ואמסך ענהא", "from her,"),
        ("לֹא הֵנִיא אֹתָהּ", "ולם ינתהרהא", "and did not rebuke her —"),
        ("וְקָמוּ", "פקד ת'בת", "then all her vows"),
        ("כָּל-נְדָרֶיהָ", "גמיע נדורהא", "and every commitment"),
        ("וְכָל-אִסָּר", "וכל עקד", "she has bound"),
        ("אֲשֶׁר-אָסְרָה", "עקדתה", "upon herself"),
        ("עַל-נַפְשָׁהּ יָקוּם", "עלי' נפסהא", "are established."),
    ],
    13: [
        # HE: וְאִם-הָפֵר יָפֵר אֹתָם אִישָׁהּ בְּיוֹם שָׁמְעוֹ--כָּל-מוֹצָא שְׂפָתֶיהָ לִנְדָרֶיהָ וּלְאִסַּר נַפְשָׁהּ לֹא יָקוּם אִישָׁהּ הֲפֵרָם וַיהוָה יִסְלַח-לָהּ
        # JA: ואן פסך' ד'אלך בעלהא פי יום סמע בה. פכל מא כ'רג מן שפתיהא. מן נד'ור ועקוד עלי' נפסהא פג'יר ת'אבת. ולמא פסכ'הם בעלהא. פאללה יג'פר להא
        # EN: But if her husband annuls that on the day he hears of it, then all that came forth from her lips, of vows and commitments upon herself, is not established — for her husband has annulled them; and God will forgive her.
        ("וְאִם-הָפֵר יָפֵר", "ואן פסך'", "But if her husband annuls"),
        ("אֹתָם אִישָׁהּ", "ד'אלך בעלהא", "that"),
        ("בְּיוֹם שָׁמְעוֹ", "פי יום סמע בה", "on the day he hears of it,"),
        ("כָּל-מוֹצָא", "פכל מא כ'רג", "then all that came forth from"),
        ("שְׂפָתֶיהָ", "מן שפתיהא", "her lips,"),
        ("לִנְדָרֶיהָ", "מן נד'ור", "of vows"),
        ("וּלְאִסַּר נַפְשָׁהּ", "ועקוד עלי' נפסהא", "and commitments upon herself,"),
        ("לֹא יָקוּם", "פג'יר ת'אבת", "is not established —"),
        ("אִישָׁהּ הֲפֵרָם", "ולמא פסכ'הם בעלהא", "for her husband has annulled them;"),
        ("וַיהוָה", "פאללה", "and God will"),
        ("יִסְלַח-לָהּ", "יג'פר להא", "forgive her."),
    ],
    14: [
        # HE: כָּל-נֵדֶר וְכָל-שְׁבֻעַת אִסָּר לְעַנֹּת נָפֶשׁ--אִישָׁהּ יְקִימֶנּוּ וְאִישָׁהּ יְפֵרֶנּוּ
        # JA: כד'אך כל נד'ר. וכל ימין בעקד לעד'אב אלנפס. בעלהא ית'בת ד'אלך ובעלהא יבטלה
        # EN: So it is with every vow and every sworn oath of commitment for the affliction of the soul — her husband may establish it, or her husband may annul it.
        (None, "כד'אך", "So it is with"),
        ("כָּל-נֵדֶר", "כל נד'ר", "every vow"),
        ("וְכָל-שְׁבֻעַת", "וכל ימין", "and every sworn oath of"),
        ("אִסָּר", "בעקד", "commitment"),
        ("לְעַנֹּת נָפֶשׁ", "לעד'אב אלנפס", "for the affliction of the soul —"),
        ("אִישָׁהּ יְקִימֶנּוּ", "בעלהא ית'בת ד'אלך", "her husband may establish it,"),
        ("וְאִישָׁהּ יְפֵרֶנּוּ", "ובעלהא יבטלה", "or her husband may annul it."),
    ],
    15: [
        # HE: וְאִם-הַחֲרֵשׁ יַחֲרִישׁ לָהּ אִישָׁהּ מִיּוֹם אֶל-יוֹם וְהֵקִים אֶת-כָּל-נְדָרֶיהָ אוֹ אֶת-כָּל-אֱסָרֶיהָ אֲשֶׁר עָלֶיהָ--הֵקִים אֹתָם כִּי-הֶחֱרִשׁ לָהּ בְּיוֹם שָׁמְעוֹ
        # JA: ואן אמסך ענהא מן יום אלי' יום. פקד ת'בת גמיע נד'ורהא ועקודהא אלד'י עליהא. ת'בתהם. למא אמסך ענהא. פי יום סמע בד'אלך
        # EN: And if he holds back from her from day to day, then he has established all her vows and commitments which are upon her — has established them — by virtue of his holding back from her on the day he heard of it.
        ("וְאִם-הַחֲרֵשׁ יַחֲרִישׁ", "ואן אמסך", "And if he holds back"),
        ("לָהּ אִישָׁהּ", "ענהא", "from her"),
        ("מִיּוֹם אֶל-יוֹם", "מן יום אלי' יום", "from day to day,"),
        ("וְהֵקִים", "פקד ת'בת", "then he has established"),
        ("אֶת-כָּל-נְדָרֶיהָ", "גמיע נד'ורהא", "all her vows"),
        ("אוֹ אֶת-כָּל-אֱסָרֶיהָ", "ועקודהא", "and commitments"),
        ("אֲשֶׁר עָלֶיהָ", "אלד'י עליהא", "which are upon her —"),
        ("הֵקִים אֹתָם", "ת'בתהם", "has established them —"),
        ("כִּי-הֶחֱרִשׁ לָהּ", "למא אמסך ענהא", "by virtue of his holding back from her"),
        ("בְּיוֹם שָׁמְעוֹ", "פי יום סמע בד'אלך", "on the day he heard of it."),
    ],
    16: [
        # HE: וְאִם-הָפֵר יָפֵר אֹתָם אַחֲרֵי שָׁמְעוֹ--וְנָשָׂא אֶת-עֲו‍ֹנָהּ
        # JA: ואן פסך' ד'אלך בעד מא סמע בה. פקד חמל וזרהא
        # EN: But if he annuls them after he has heard of them, then he has borne her guilt.
        ("וְאִם-הָפֵר יָפֵר", "ואן פסך'", "But if he annuls them"),
        ("אֹתָם", "ד'אלך", "after"),
        ("אַחֲרֵי שָׁמְעוֹ", "בעד מא סמע בה", "he has heard of them,"),
        ("וְנָשָׂא", "פקד חמל", "then he has borne"),
        ("אֶת-עֲו‍ֹנָהּ", "וזרהא", "her guilt."),
    ],
    17: [
        # HE: אֵלֶּה הַחֻקִּים אֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה בֵּין אִישׁ לְאִשְׁתּוֹ--בֵּין-אָב לְבִתּוֹ בִּנְעֻרֶיהָ בֵּית אָבִיהָ
        # JA: הד'ה אלרסום. אלד'י אמר אללה בהא מוסי'. פי מא בין אלרגל וזוגתה דאימא. ופי מא בין אלאב ואבנתה. פי חאל צבאיהא והי פי מנזלה
        # EN: These are the statutes which God commanded Moses, concerning what is between a man and his wife always, and concerning what is between a father and his daughter, in the time of her youth while she is in his household.'
        ("אֵלֶּה", "הד'ה", "These are"),
        ("הַחֻקִּים", "אלרסום", "the statutes"),
        ("אֲשֶׁר צִוָּה", "אלד'י אמר", "which God commanded"),
        ("יְהוָה", "אללה", "Moses,"),
        ("אֶת-מֹשֶׁה", "בהא מוסי'", "concerning what is between"),
        ("בֵּין אִישׁ", "פי מא בין אלרגל", "a man"),
        ("לְאִשְׁתּוֹ", "וזוגתה", "and his wife"),
        ("בֵּין-אָב", "דאימא. ופי מא בין אלאב", "always, and concerning what is between a father"),
        ("לְבִתּוֹ", "ואבנתה", "and his daughter,"),
        ("בִּנְעֻרֶיהָ", "פי חאל צבאיהא", "in the time of her youth"),
        ("בֵּית אָבִיהָ", "והי פי מנזלה", "while she is in his household.'"),
    ],
}

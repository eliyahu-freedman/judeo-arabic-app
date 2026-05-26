"""Hand-authored word-level alignment triples for Bamidbar chapter 27."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַתִּקְרַבְנָה בְּנוֹת צְלָפְחָד בֶּן-חֵפֶר בֶּן-גִּלְעָד בֶּן-מָכִיר בֶּן-מְנַשֶּׁה לְמִשְׁפְּחֹת מְנַשֶּׁה בֶן-יוֹסֵף וְאֵלֶּה שְׁמוֹת בְּנֹתָיו--מַחְלָה נֹעָה וְחָגְלָה וּמִלְכָּה וְתִרְצָה
        # JA: פתקדמן בנאת צלפחד. אבן חפר ן' גלעד ו' מכיר ן' מנשה. מן עשאיר מנשה ן' יוסף אלתי אסמאיהן. מחלה נועה. וחגלה ומלכה ותרצה
        # EN: And the daughters of Zelophehad came forward — son of Hepher, son of Gilead, son of Machir, son of Manasseh, from the clans of Manasseh son of Joseph — whose names were: Mahlah, Noa, Hoglah, Milcah, and Tirzah.
        ("וַתִּקְרַבְנָה", "פתקדמן", "And the daughters of Zelophehad came forward"),
        ("בְּנוֹת צְלָפְחָד", "בנאת צלפחד", "— son of Hepher,"),
        ("בֶּן-חֵפֶר", "אבן חפר", "son of Gilead,"),
        ("בֶּן-גִּלְעָד", "ן' גלעד", "son of Machir,"),
        ("בֶּן-מָכִיר", "ו' מכיר", "son of Manasseh,"),
        ("בֶּן-מְנַשֶּׁה", "ן' מנשה", "from the clans of"),
        ("לְמִשְׁפְּחֹת", "מן עשאיר", "Manasseh son of"),
        ("מְנַשֶּׁה בֶן-יוֹסֵף", "מנשה ן' יוסף", "Joseph —"),
        ("וְאֵלֶּה שְׁמוֹת", "אלתי אסמאיהן", "whose names were:"),
        ("מַחְלָה נֹעָה", "מחלה נועה", "Mahlah, Noa,"),
        ("וְחָגְלָה וּמִלְכָּה", "וחגלה ומלכה", "Hoglah, Milcah,"),
        ("וְתִרְצָה", "ותרצה", "and Tirzah."),
    ],
    2: [
        # HE: וַתַּעֲמֹדְנָה לִפְנֵי מֹשֶׁה וְלִפְנֵי אֶלְעָזָר הַכֹּהֵן וְלִפְנֵי הַנְּשִׂיאִם וְכָל-הָעֵדָה--פֶּתַח אֹהֶל-מוֹעֵד לֵאמֹר
        # JA: פקמן בין ידי מוסי' ואלעזר אלאמאם. ואלאשראף וסאיר אלגמאעה. ענד באב כ'בא אלמחצ'ר קאילאת
        # EN: And they stood before Moses and Eleazar the imām, and the nobles and the rest of the congregation, at the entrance of the tent of the assembly, saying:
        ("וַתַּעֲמֹדְנָה", "פקמן", "And they stood"),
        ("לִפְנֵי מֹשֶׁה", "בין ידי מוסי'", "before Moses"),
        ("וְלִפְנֵי אֶלְעָזָר", "ואלעזר", "and Eleazar"),
        ("הַכֹּהֵן", "אלאמאם", "the imām,"),
        ("וְלִפְנֵי הַנְּשִׂיאִם", "ואלאשראף", "and the nobles"),
        ("וְכָל-הָעֵדָה", "וסאיר אלגמאעה", "and the rest of the congregation,"),
        ("פֶּתַח", "ענד באב", "at the entrance of"),
        ("אֹהֶל-מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly,"),
        ("לֵאמֹר", "קאילאת", "saying:"),
    ],
    3: [
        # HE: אָבִינוּ מֵת בַּמִּדְבָּר וְהוּא לֹא-הָיָה בְּתוֹךְ הָעֵדָה הַנּוֹעָדִים עַל-יְהוָה בַּעֲדַת-קֹרַח כִּי-בְחֶטְאוֹ מֵת וּבָנִים לֹא-הָיוּ לוֹ
        # JA: אן אבינא מאת פי גמלה' אלגמאעה. אלד'י תגמעו עלי' אללה מע קרח. לאנה מאת בכ'טייתה. ולם יכ'לף בנין
        # EN: 'Our father died in the wilderness, and he was not among the body of the congregation who gathered against God with Korah — for he died in his own sin — and he left no sons.
        (None, "אן", "'Our father"),
        ("אָבִינוּ", "אבינא", "died"),
        ("מֵת", "מאת", "in the wilderness,"),
        ("בַּמִּדְבָּר", "פי גמלה'", "and he was not among"),
        ("הָעֵדָה", "אלגמאעה", "the body of the congregation"),
        ("הַנּוֹעָדִים", "אלד'י תגמעו", "who gathered"),
        ("עַל-יְהוָה", "עלי' אללה", "against God"),
        ("בַּעֲדַת-קֹרַח", "מע קרח", "with Korah —"),
        ("כִּי-בְחֶטְאוֹ", "לאנה", "for he died"),
        ("מֵת", "מאת בכ'טייתה", "in his own sin —"),
        ("וּבָנִים לֹא-הָיוּ לוֹ", "ולם יכ'לף בנין", "and he left no sons."),
    ],
    4: [
        # HE: לָמָּה יִגָּרַע שֵׁם-אָבִינוּ מִתּוֹךְ מִשְׁפַּחְתּוֹ כִּי אֵין לוֹ בֵּן תְּנָה-לָּנוּ אֲחֻזָּה בְּתוֹךְ אֲחֵי אָבִינוּ
        # JA: פלם ינקץ אסם אבינא מן בין עשירתה. אד' ליס לה אבן. בל אעטנא נחלה. פי מא בין אעמאמנא
        # EN: Why should our father's name be diminished from among his clan, since he has no son? Give us a portion of inheritance among our uncles.'
        (None, "פלם", "Why should"),
        ("לָמָּה יִגָּרַע", "ינקץ", "our father's name be diminished"),
        ("שֵׁם-אָבִינוּ", "אסם אבינא", "from among"),
        ("מִתּוֹךְ מִשְׁפַּחְתּוֹ", "מן בין עשירתה", "his clan,"),
        ("כִּי אֵין לוֹ בֵּן", "אד' ליס לה אבן", "since he has no son?"),
        ("תְּנָה-לָּנוּ", "בל אעטנא", "Give us"),
        ("אֲחֻזָּה", "נחלה", "a portion of inheritance"),
        ("בְּתוֹךְ אֲחֵי אָבִינוּ", "פי מא בין אעמאמנא", "among our uncles.'"),
    ],
    5: [
        # HE: וַיַּקְרֵב מֹשֶׁה אֶת-מִשְׁפָּטָן לִפְנֵי יְהוָה
        # JA: פרפע מוסי' חכמהן אלי' אללה
        # EN: And Moses brought their case before God.
        ("וַיַּקְרֵב", "פרפע", "And Moses brought"),
        ("מֹשֶׁה", "מוסי'", "their case"),
        ("אֶת-מִשְׁפָּטָן", "חכמהן", "before"),
        ("לִפְנֵי יְהוָה", "אלי' אללה", "God."),
    ],
    6: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם קאל אללה למוסי קאילא
        # EN: Then God said to Moses, saying:
        (None, "ת'ם", "Then"),
        ("וַיֹּאמֶר יְהוָה", "קאל אללה", "God said"),
        ("אֶל-מֹשֶׁה", "למוסי", "to Moses,"),
        ("לֵּאמֹר", "קאילא", "saying:"),
    ],
    7: [
        # HE: כֵּן בְּנוֹת צְלָפְחָד דֹּבְרֹת--נָתֹן תִּתֵּן לָהֶם אֲחֻזַּת נַחֲלָה בְּתוֹךְ אֲחֵי אֲבִיהֶם וְהַעֲבַרְתָּ אֶת-נַחֲלַת אֲבִיהֶן לָהֶן
        # JA: נעמא קאלן בנאת צלפחד. אעטהן חוז נחלה. פי מא בין אעמאמהן. ואנקל נחלה' אביהן להן
        # EN: 'Rightly have the daughters of Zelophehad spoken. Give them possession of an inheritance among their uncles, and transfer their father's inheritance to them.
        ("כֵּן", "נעמא", "'Rightly"),
        ("דֹּבְרֹת", "קאלן", "have the daughters of Zelophehad spoken."),
        ("בְּנוֹת צְלָפְחָד", "בנאת צלפחד", "Give them"),
        ("נָתֹן תִּתֵּן לָהֶם", "אעטהן", "possession of"),
        ("אֲחֻזַּת", "חוז", "an inheritance"),
        ("נַחֲלָה", "נחלה", "among their uncles,"),
        ("בְּתוֹךְ אֲחֵי אֲבִיהֶם", "פי מא בין אעמאמהן", "and transfer"),
        ("וְהַעֲבַרְתָּ", "ואנקל", "their father's"),
        ("אֶת-נַחֲלַת אֲבִיהֶן", "נחלה' אביהן", "inheritance"),
        ("לָהֶן", "להן", "to them."),
    ],
    8: [
        # HE: וְאֶל-בְּנֵי יִשְׂרָאֵל תְּדַבֵּר לֵאמֹר אִישׁ כִּי-יָמוּת וּבֵן אֵין לוֹ--וְהַעֲבַרְתֶּם אֶת-נַחֲלָתוֹ לְבִתּוֹ
        # JA: ומר בני אסראיל וקל להם. אי רגל מאת. וליס לה אבן פאנקלו נחלתה לאבנתה
        # EN: And command the sons of Israel and say to them: Any man who dies and has no son — transfer his inheritance to his daughter.
        ("וְאֶל-בְּנֵי יִשְׂרָאֵל", "ומר בני אסראיל", "And command the sons of Israel"),
        ("תְּדַבֵּר", "וקל", "and say"),
        ("לֵאמֹר", "להם", "to them:"),
        ("אִישׁ", "אי רגל", "Any man"),
        ("כִּי-יָמוּת", "מאת", "who dies"),
        ("וּבֵן אֵין לוֹ", "וליס לה אבן", "and has no son —"),
        ("וְהַעֲבַרְתֶּם", "פאנקלו", "transfer"),
        ("אֶת-נַחֲלָתוֹ", "נחלתה", "his inheritance"),
        ("לְבִתּוֹ", "לאבנתה", "to his daughter."),
    ],
    9: [
        # HE: וְאִם-אֵין לוֹ בַּת--וּנְתַתֶּם אֶת-נַחֲלָתוֹ לְאֶחָיו
        # JA: ואן לם תכון לה אבנה פאעטו נחלתה לאכ'ותה
        # EN: And if he has no daughter, give his inheritance to his brothers.
        ("וְאִם-אֵין לוֹ בַּת", "ואן לם תכון לה אבנה", "And if he has no daughter,"),
        ("וּנְתַתֶּם", "פאעטו", "give"),
        ("אֶת-נַחֲלָתוֹ", "נחלתה", "his inheritance"),
        ("לְאֶחָיו", "לאכ'ותה", "to his brothers."),
    ],
    10: [
        # HE: וְאִם-אֵין לוֹ אַחִים--וּנְתַתֶּם אֶת-נַחֲלָתוֹ לַאֲחֵי אָבִיו
        # JA: ואן לם יכון לה אכ'וה. פאעטוהא לאעמאמה
        # EN: And if he has no brothers, give it to his uncles.
        ("וְאִם-אֵין לוֹ אַחִים", "ואן לם יכון לה אכ'וה", "And if he has no brothers,"),
        ("וּנְתַתֶּם", "פאעטוהא", "give it"),
        ("לַאֲחֵי אָבִיו", "לאעמאמה", "to his uncles."),
    ],
    11: [
        # HE: וְאִם-אֵין אַחִים לְאָבִיו--וּנְתַתֶּם אֶת-נַחֲלָתוֹ לִשְׁאֵרוֹ הַקָּרֹב אֵלָיו מִמִּשְׁפַּחְתּוֹ וְיָרַשׁ אֹתָהּ וְהָיְתָה לִבְנֵי יִשְׂרָאֵל לְחֻקַּת מִשְׁפָּט כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה
        # JA: ואן לם יכון לה אעמאם. פאעטוהא לנסיבה אלאקרב אליה מן עשירתה ויחוזהא. ויכון ד'אלך לבני אסראיל רסם אלחכם. כמא אמר אללה מוסי'
        # EN: And if he has no uncles, give it to the kinsman nearest to him from his clan, and he shall possess it. And this shall be for the sons of Israel a binding rule of judgment, as God commanded Moses.'
        ("וְאִם-אֵין אַחִים לְאָבִיו", "ואן לם יכון לה אעמאם", "And if he has no uncles,"),
        ("וּנְתַתֶּם", "פאעטוהא", "give it"),
        ("לִשְׁאֵרוֹ", "לנסיבה", "to the kinsman"),
        ("הַקָּרֹב אֵלָיו", "אלאקרב אליה", "nearest to him"),
        ("מִמִּשְׁפַּחְתּוֹ", "מן עשירתה", "from his clan,"),
        ("וְיָרַשׁ אֹתָהּ", "ויחוזהא", "and he shall possess it."),
        ("וְהָיְתָה", "ויכון ד'אלך", "And this shall be"),
        ("לִבְנֵי יִשְׂרָאֵל", "לבני אסראיל", "for the sons of Israel"),
        ("לְחֻקַּת מִשְׁפָּט", "רסם אלחכם", "a binding rule of judgment,"),
        ("כַּאֲשֶׁר צִוָּה", "כמא אמר", "as God commanded"),
        ("יְהוָה אֶת-מֹשֶׁה", "אללה מוסי'", "Moses.'"),
    ],
    12: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה עֲלֵה אֶל-הַר הָעֲבָרִים הַזֶּה וּרְאֵה אֶת-הָאָרֶץ אֲשֶׁר נָתַתִּי לִבְנֵי יִשְׂרָאֵל
        # JA: ולמא קאל אללה למוסי'. אצעד אלי' גבל אלעבריין הד'א. ואנצ'ר אלבלד. אלד'י אנא מעטיה לבני אסראיל
        # EN: And when God said to Moses: 'Ascend this mountain of the Abarim, and look upon the land which I am giving to the sons of Israel —
        ("וַיֹּאמֶר יְהוָה", "ולמא קאל אללה", "And when God said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses:"),
        ("עֲלֵה", "אצעד", "'Ascend"),
        ("אֶל-הַר הָעֲבָרִים", "אלי' גבל אלעבריין", "this mountain of the Abarim,"),
        ("הַזֶּה", "הד'א", "and look upon"),
        ("וּרְאֵה", "ואנצ'ר", "the land"),
        ("אֶת-הָאָרֶץ", "אלבלד", "which I am giving"),
        ("אֲשֶׁר נָתַתִּי לִבְנֵי יִשְׂרָאֵל", "אלד'י אנא מעטיה לבני אסראיל", "to the sons of Israel —"),
    ],
    13: [
        # HE: וְרָאִיתָה אֹתָהּ וְנֶאֱסַפְתָּ אֶל-עַמֶּיךָ גַּם-אָתָּה כַּאֲשֶׁר נֶאֱסַף אַהֲרֹן אָחִיךָ
        # JA: פאד'א אבצרתאה. אנצ'ם אלי' קומך אנת איצ'א כמא אנצ'ם הרון אכ'יך
        # EN: when you have seen it, you too shall be joined to your people, just as Aaron your brother was joined.'
        ("וְרָאִיתָה אֹתָהּ", "פאד'א אבצרתאה", "when you have seen it,"),
        ("וְנֶאֱסַפְתָּ", "אנצ'ם", "you too shall be joined"),
        ("אֶל-עַמֶּיךָ", "אלי' קומך", "to your people,"),
        ("גַּם-אָתָּה", "אנת איצ'א", "just as"),
        ("כַּאֲשֶׁר נֶאֱסַף", "כמא אנצ'ם", "Aaron"),
        ("אַהֲרֹן", "הרון", "your brother"),
        ("אָחִיךָ", "אכ'יך", "was joined.'"),
    ],
    14: [
        # HE: כַּאֲשֶׁר מְרִיתֶם פִּי בְּמִדְבַּר-צִן בִּמְרִיבַת הָעֵדָה לְהַקְדִּישֵׁנִי בַמַּיִם לְעֵינֵיהֶם הֵם מֵי-מְרִיבַת קָדֵשׁ מִדְבַּר-צִן
        # JA: כמי' כ'אלפתמא אמרי פי ברייה' צין. ענד כ'צומה' אלגמאעה. ולם תקדסאני בד'אלך אלמא בחצ'רתהם. ולד'אלך סמי מא כ'צומה' רקים פי ברייה' צין
        # EN: — 'As you two transgressed My command in the wilderness of Zin, at the strife of the congregation, and did not sanctify Me at that water in their presence' — and that is why it was called: the water of the strife of Kadesh, in the wilderness of Zin.
        ("כַּאֲשֶׁר מְרִיתֶם", "כמי' כ'אלפתמא", "'As you two transgressed"),
        ("פִּי", "אמרי", "My command"),
        ("בְּמִדְבַּר-צִן", "פי ברייה' צין", "in the wilderness of Zin,"),
        ("בִּמְרִיבַת הָעֵדָה", "ענד כ'צומה' אלגמאעה", "at the strife of the congregation,"),
        ("לְהַקְדִּישֵׁנִי", "ולם תקדסאני", "and did not sanctify Me"),
        ("בַמַּיִם", "בד'אלך אלמא", "at that water"),
        ("לְעֵינֵיהֶם", "בחצ'רתהם", "in their presence' —"),
        (None, "ולד'אלך", "and that is why"),
        ("הֵם מֵי-מְרִיבַת", "סמי מא כ'צומה'", "it was called: the water of the strife of"),
        ("קָדֵשׁ", "רקים", "Kadesh,"),
        ("מִדְבַּר-צִן", "פי ברייה' צין", "in the wilderness of Zin."),
    ],
    15: [
        # HE: וַיְדַבֵּר מֹשֶׁה אֶל-יְהוָה לֵאמֹר
        # JA: פקאל מוסי'. בין ידי אללה קאילא
        # EN: And Moses spoke before God, saying:
        ("וַיְדַבֵּר", "פקאל", "And Moses spoke"),
        ("מֹשֶׁה", "מוסי'", "before"),
        ("אֶל-יְהוָה", "בין ידי אללה", "God,"),
        ("לֵאמֹר", "קאילא", "saying:"),
    ],
    16: [
        # HE: יִפְקֹד יְהוָה אֱלֹהֵי הָרוּחֹת לְכָל-בָּשָׂר אִישׁ עַל-הָעֵדָה
        # JA: אן שית יא רב. יא אלאה ארואח כל בשרי. פאסתכ'לף רגלא עלי' אלגמאעה
        # EN: 'If it be Your will, O Lord — O God of the spirits of all flesh — appoint a man over the congregation,
        (None, "אן שית", "'If it be Your will,"),
        ("יְהוָה", "יא רב", "O Lord —"),
        ("אֱלֹהֵי", "יא אלאה", "O God of"),
        ("הָרוּחֹת", "ארואח", "the spirits of"),
        ("לְכָל-בָּשָׂר", "כל בשרי", "all flesh —"),
        ("יִפְקֹד", "פאסתכ'לף", "appoint"),
        ("אִישׁ", "רגלא", "a man"),
        ("עַל-הָעֵדָה", "עלי' אלגמאעה", "over the congregation,"),
    ],
    17: [
        # HE: אֲשֶׁר-יֵצֵא לִפְנֵיהֶם וַאֲשֶׁר יָבֹא לִפְנֵיהֶם וַאֲשֶׁר יוֹצִיאֵם וַאֲשֶׁר יְבִיאֵם וְלֹא תִהְיֶה עֲדַת יְהוָה כַּצֹּאן אֲשֶׁר אֵין-לָהֶם רֹעֶה
        # JA: יכ'רג בין אידיהם. וידכ'ל בין אידיהם. ויכ'רגהם וידכ'להם. ולא יבקו גמאעה' אללה . כג'נם ליס להא ראעי
        # EN: who shall go out among them and come in among them, and shall lead them out and bring them in, so that the congregation of God shall not remain like a flock that has no shepherd.'
        ("אֲשֶׁר-יֵצֵא", "יכ'רג", "who shall go out"),
        ("לִפְנֵיהֶם", "בין אידיהם", "among them"),
        ("וַאֲשֶׁר יָבֹא", "וידכ'ל", "and come in"),
        ("לִפְנֵיהֶם", "בין אידיהם", "among them,"),
        ("וַאֲשֶׁר יוֹצִיאֵם", "ויכ'רגהם", "and shall lead them out"),
        ("וַאֲשֶׁר יְבִיאֵם", "וידכ'להם", "and bring them in,"),
        ("וְלֹא תִהְיֶה", "ולא יבקו", "so that the congregation of God shall not remain"),
        ("עֲדַת יְהוָה", "גמאעה' אללה", "like a flock"),
        ("כַּצֹּאן", "כג'נם", "that has"),
        ("אֲשֶׁר אֵין-לָהֶם רֹעֶה", "ליס להא ראעי", "no shepherd.'"),
    ],
    18: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה קַח-לְךָ אֶת-יְהוֹשֻׁעַ בִּן-נוּן--אִישׁ אֲשֶׁר-רוּחַ בּוֹ וְסָמַכְתָּ אֶת-יָדְךָ עָלָיו
        # JA: פקאל אללה למוסי. כ'ד' לך יהושע אבן נון. פאנה רגל פיה פצ'ל. ואסנד ידך עליה
        # EN: And God said to Moses: 'Take for yourself Joshua son of Nun — for he is a man in whom there is distinction — and lay your hand upon him.
        ("וַיֹּאמֶר", "פקאל", "And God said"),
        ("יְהוָה", "אללה", "to Moses:"),
        ("אֶל-מֹשֶׁה", "למוסי", "'Take for yourself"),
        ("קַח-לְךָ", "כ'ד' לך", "Joshua"),
        ("אֶת-יְהוֹשֻׁעַ", "יהושע", "son of Nun —"),
        ("בִּן-נוּן", "אבן נון", "for he is a man"),
        ("אִישׁ", "פאנה רגל", "in whom there is"),
        ("אֲשֶׁר-רוּחַ בּוֹ", "פיה פצ'ל", "distinction —"),
        ("וְסָמַכְתָּ", "ואסנד", "and lay"),
        ("אֶת-יָדְךָ", "ידך", "your hand"),
        ("עָלָיו", "עליה", "upon him."),
    ],
    19: [
        # HE: וְהַעֲמַדְתָּ אֹתוֹ לִפְנֵי אֶלְעָזָר הַכֹּהֵן וְלִפְנֵי כָּל-הָעֵדָה וְצִוִּיתָה אֹתוֹ לְעֵינֵיהֶם
        # JA: ואוקפה בין ידי אלעזר אלאמאם. וסאיר אלגמאעה. ואמרה בחצ'רתהם
        # EN: And set him before Eleazar the imām and the rest of the congregation, and charge him in their presence.
        ("וְהַעֲמַדְתָּ אֹתוֹ", "ואוקפה", "And set him"),
        ("לִפְנֵי אֶלְעָזָר", "בין ידי אלעזר", "before Eleazar"),
        ("הַכֹּהֵן", "אלאמאם", "the imām"),
        ("וְלִפְנֵי כָּל-הָעֵדָה", "וסאיר אלגמאעה", "and the rest of the congregation,"),
        ("וְצִוִּיתָה אֹתוֹ", "ואמרה", "and charge him"),
        ("לְעֵינֵיהֶם", "בחצ'רתהם", "in their presence."),
    ],
    20: [
        # HE: וְנָתַתָּה מֵהוֹדְךָ עָלָיו--לְמַעַן יִשְׁמְעוּ כָּל-עֲדַת בְּנֵי יִשְׂרָאֵל
        # JA: ואגעל עליה מן בהאיך לכי תקבל מנה גמאעה' בני אסראיל
        # EN: And place upon him some of your splendor, so that the congregation of the sons of Israel may accept from him.
        ("וְנָתַתָּה", "ואגעל", "And place"),
        ("עָלָיו", "עליה", "upon him"),
        ("מֵהוֹדְךָ", "מן בהאיך", "some of your splendor,"),
        ("לְמַעַן", "לכי", "so that"),
        ("יִשְׁמְעוּ", "תקבל מנה", "may accept from him"),
        ("כָּל-עֲדַת", "גמאעה'", "the congregation of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
    ],
    21: [
        # HE: וְלִפְנֵי אֶלְעָזָר הַכֹּהֵן יַעֲמֹד וְשָׁאַל לוֹ בְּמִשְׁפַּט הָאוּרִים לִפְנֵי יְהוָה עַל-פִּיו יֵצְאוּ וְעַל-פִּיו יָבֹאוּ הוּא וְכָל-בְּנֵי-יִשְׂרָאֵל אִתּוֹ--וְכָל-הָעֵדָה
        # JA: וליכון וקופה בין ידי אלעזר אלאמאם. חתי יסאל פי חואיגה. בהיאה' אלאנואר בין ידי אללה . וען אמרה יכ'רגו וידכ'לו. הו ובני אסראיל מעה וסאיר אלגמאעה
        # EN: And his station shall be to stand before Eleazar the imām, that he may inquire for what he needs through the splendor of the Lights before God; and at his command they shall go out and come in — he and the sons of Israel with him, and the rest of the congregation.'
        ("וְלִפְנֵי אֶלְעָזָר", "וליכון וקופה בין ידי אלעזר", "And his station shall be to stand before Eleazar"),
        ("הַכֹּהֵן", "אלאמאם", "the imām,"),
        ("יַעֲמֹד", "חתי יסאל", "that he may inquire"),
        ("וְשָׁאַל לוֹ", "פי חואיגה", "for what he needs"),
        ("בְּמִשְׁפַּט הָאוּרִים", "בהיאה' אלאנואר", "through the splendor of the Lights"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God;"),
        ("עַל-פִּיו", "וען אמרה", "and at his command"),
        ("יֵצְאוּ", "יכ'רגו", "they shall go out"),
        ("וְעַל-פִּיו יָבֹאוּ", "וידכ'לו", "and come in —"),
        ("הוּא", "הו", "he"),
        ("וְכָל-בְּנֵי-יִשְׂרָאֵל אִתּוֹ", "ובני אסראיל מעה", "and the sons of Israel with him,"),
        ("וְכָל-הָעֵדָה", "וסאיר אלגמאעה", "and the rest of the congregation.'"),
    ],
    22: [
        # HE: וַיַּעַשׂ מֹשֶׁה כַּאֲשֶׁר צִוָּה יְהוָה אֹתוֹ וַיִּקַּח אֶת-יְהוֹשֻׁעַ וַיַּעֲמִדֵהוּ לִפְנֵי אֶלְעָזָר הַכֹּהֵן וְלִפְנֵי כָּל-הָעֵדָה
        # JA: פצנע מוסי'. כמא אמרה אללה . אן אכ'ד' יהושע. ואוקפה בין ידי אלעזר אלאמאם. וסאיר אלגמאעה
        # EN: And Moses did as God had commanded him: he took Joshua, and set him before Eleazar the imām and the rest of the congregation.
        ("וַיַּעַשׂ", "פצנע", "And Moses did"),
        ("מֹשֶׁה", "מוסי'", "as God had commanded him:"),
        ("כַּאֲשֶׁר צִוָּה", "כמא אמרה", "he took"),
        ("יְהוָה", "אללה", "Joshua,"),
        ("וַיִּקַּח", "אן אכ'ד'", "and set him"),
        ("אֶת-יְהוֹשֻׁעַ", "יהושע", "before"),
        ("וַיַּעֲמִדֵהוּ", "ואוקפה", "Eleazar"),
        ("לִפְנֵי אֶלְעָזָר", "בין ידי אלעזר", "the imām"),
        ("הַכֹּהֵן", "אלאמאם", "and the rest of"),
        ("וְלִפְנֵי כָּל-הָעֵדָה", "וסאיר אלגמאעה", "the congregation."),
    ],
    23: [
        # HE: וַיִּסְמֹךְ אֶת-יָדָיו עָלָיו וַיְצַוֵּהוּ כַּאֲשֶׁר דִּבֶּר יְהוָה בְּיַד-מֹשֶׁה
        # JA: ואסנד ידיה עליה ואמרה כמי' קאל אללה לה
        # EN: And he laid his hands upon him, and charged him as God had said to him.
        ("וַיִּסְמֹךְ", "ואסנד", "And he laid"),
        ("אֶת-יָדָיו", "ידיה", "his hands"),
        ("עָלָיו", "עליה", "upon him,"),
        ("וַיְצַוֵּהוּ", "ואמרה", "and charged him"),
        ("כַּאֲשֶׁר דִּבֶּר", "כמי' קאל", "as God"),
        ("יְהוָה", "אללה", "had said"),
        ("בְּיַד-מֹשֶׁה", "לה", "to him."),
    ],
}

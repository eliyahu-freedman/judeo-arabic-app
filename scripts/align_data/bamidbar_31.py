"""Hand-authored word-level alignment triples for Bamidbar chapter 31."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "spoke"),
        ("יְהוָה", "אללה", "God"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "directly."),
    ],
    2: [
        # HE: נְקֹם נִקְמַת בְּנֵי יִשְׂרָאֵל מֵאֵת הַמִּדְיָנִים אַחַר תֵּאָסֵף אֶל-עַמֶּיךָ
        # JA: אנתקם נקמה' בני אסראיל. מן אלמדיאניין. בעד ד'אלך תנצ'ם אלי' קומך
        # EN: 'Exact the vengeance of the sons of Israel upon the Midianites; after that, you shall be gathered to your people.'
        ("נְקֹם", "אנתקם", "'Exact"),
        ("נִקְמַת", "נקמה'", "the vengeance of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("מֵאֵת הַמִּדְיָנִים", "מן אלמדיאניין", "upon the Midianites;"),
        ("אַחַר", "בעד ד'אלך", "after that,"),
        ("תֵּאָסֵף", "תנצ'ם", "you shall be gathered"),
        ("אֶל-עַמֶּיךָ", "אלי' קומך", "to your people.'"),
    ],
    3: [
        # HE: וַיְדַבֵּר מֹשֶׁה אֶל-הָעָם לֵאמֹר הֵחָלְצוּ מֵאִתְּכֶם אֲנָשִׁים לַצָּבָא וְיִהְיוּ עַל-מִדְיָן לָתֵת נִקְמַת-יְהוָה בְּמִדְיָן
        # JA: פכלם מוסי' קומה קאילא. גרדו מנכם. רגאלא לאלגיש. יג'זו אלי' מדין ליחל נקמה אללה בהם
        # EN: And Moses spoke to his people, saying: 'Detach from among you men for the army, to campaign against Midian, that the vengeance of God may fall upon them.'
        ("וַיְדַבֵּר", "פכלם", "And Moses spoke"),
        ("מֹשֶׁה", "מוסי'", "to his people,"),
        ("אֶל-הָעָם", "קומה", "saying:"),
        ("לֵאמֹר", "קאילא", "'Detach"),
        ("הֵחָלְצוּ", "גרדו", "from among you"),
        ("מֵאִתְּכֶם", "מנכם", "men"),
        ("אֲנָשִׁים", "רגאלא", "for the army,"),
        ("לַצָּבָא", "לאלגיש", "to campaign"),
        ("וְיִהְיוּ עַל-מִדְיָן", "יג'זו אלי' מדין", "against Midian,"),
        ("לָתֵת", "ליחל", "that"),
        ("נִקְמַת-יְהוָה", "נקמה אללה", "the vengeance of God"),
        ("בְּמִדְיָן", "בהם", "may fall upon them.'"),
    ],
    4: [
        # HE: אֶלֶף לַמַּטֶּה אֶלֶף לַמַּטֶּה--לְכֹל מַטּוֹת יִשְׂרָאֵל תִּשְׁלְחוּ לַצָּבָא
        # JA: אלף מן כל סבט. מן אסבאט בני אסראיל. תבעתו בהם לאלג'זו
        # EN: 'A thousand from each tribe, from the tribes of the sons of Israel, you shall send forth for the campaign.'
        ("אֶלֶף", "אלף", "'A thousand"),
        ("לַמַּטֶּה", "מן כל סבט", "from each tribe,"),
        ("לְכֹל מַטּוֹת", "מן אסבאט", "from the tribes of"),
        ("יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("תִּשְׁלְחוּ", "תבעתו בהם", "you shall send forth"),
        ("לַצָּבָא", "לאלג'זו", "for the campaign.'"),
    ],
    5: [
        # HE: וַיִּמָּסְרוּ מֵאַלְפֵי יִשְׂרָאֵל אֶלֶף לַמַּטֶּה--שְׁנֵים-עָשָׂר אֶלֶף חֲלוּצֵי צָבָא
        # JA: פאנמאז מן אלוף בני אסראיל. אלף מן כל סבט. פצארו את'ני עשר אלף מגרדין לאלג'זו
        # EN: And there were singled out from the thousands of the sons of Israel, a thousand from each tribe; and they became twelve thousand equipped for the campaign.
        ("וַיִּמָּסְרוּ", "פאנמאז", "And there were singled out"),
        ("מֵאַלְפֵי", "מן אלוף", "from the thousands of"),
        ("יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("אֶלֶף", "אלף", "a thousand"),
        ("לַמַּטֶּה", "מן כל סבט", "from each tribe;"),
        (None, "פצארו", "and they became"),
        ("שְׁנֵים-עָשָׂר אֶלֶף", "את'ני עשר אלף", "twelve thousand"),
        ("חֲלוּצֵי צָבָא", "מגרדין לאלג'זו", "equipped for the campaign."),
    ],
    6: [
        # HE: וַיִּשְׁלַח אֹתָם מֹשֶׁה אֶלֶף לַמַּטֶּה לַצָּבָא אֹתָם וְאֶת-פִּינְחָס בֶּן-אֶלְעָזָר הַכֹּהֵן לַצָּבָא וּכְלֵי הַקֹּדֶשׁ וַחֲצֹצְרוֹת הַתְּרוּעָה בְּיָדוֹ
        # JA: פבעת' בהם מוסי'. ובפינחס אבן אלעזר אלאמאם לאלג'זו. ואניה' אלקדס. ואבואק אלתגליב פי ידה
        # EN: And Moses sent them forth — and Phinehas son of Eleazar the imām with them for the campaign — with the sacred vessels and the rallying trumpets in his hand.
        ("וַיִּשְׁלַח", "פבעת'", "And Moses sent"),
        ("אֹתָם", "בהם", "them forth —"),
        ("מֹשֶׁה", "מוסי'", "and Phinehas"),
        ("פִּינְחָס", "ובפינחס", "son of Eleazar"),
        ("בֶּן-אֶלְעָזָר", "אבן אלעזר", "the imām"),
        ("הַכֹּהֵן", "אלאמאם", "with them"),
        ("לַצָּבָא", "לאלג'זו", "for the campaign —"),
        ("וּכְלֵי הַקֹּדֶשׁ", "ואניה' אלקדס", "with the sacred vessels"),
        ("וַחֲצֹצְרוֹת הַתְּרוּעָה", "ואבואק אלתגליב", "and the rallying trumpets"),
        ("בְּיָדוֹ", "פי ידה", "in his hand."),
    ],
    7: [
        # HE: וַיִּצְבְּאוּ עַל-מִדְיָן כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה וַיַּהַרְגוּ כָּל-זָכָר
        # JA: פג'זו אלי' מדין. כמא אמר אללה מוסי'. וקתלו כל ד'כר
        # EN: And they campaigned against Midian, as God had commanded Moses, and they slew every male.
        ("וַיִּצְבְּאוּ", "פג'זו", "And they campaigned"),
        ("עַל-מִדְיָן", "אלי' מדין", "against Midian,"),
        ("כַּאֲשֶׁר", "כמא", "as"),
        ("צִוָּה יְהוָה", "אמר אללה", "God had commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses,"),
        ("וַיַּהַרְגוּ", "וקתלו", "and they slew"),
        ("כָּל-זָכָר", "כל ד'כר", "every male."),
    ],
    8: [
        # HE: וְאֶת-מַלְכֵי מִדְיָן הָרְגוּ עַל-חַלְלֵיהֶם אֶת-אֱוִי וְאֶת-רֶקֶם וְאֶת-צוּר וְאֶת-חוּר וְאֶת-רֶבַע--חֲמֵשֶׁת מַלְכֵי מִדְיָן וְאֵת בִּלְעָם בֶּן-בְּעוֹר הָרְגוּ בֶּחָרֶב
        # JA: וקתלו כ'מסה מלוך מדין מע קתלאהם. אוי ורקם וצור וחור ורבע. ואיצ'א בלעם אבן בעור. קתלוה באלסיף
        # EN: And they slew the five kings of Midian together with their slain — Evi, and Rekem, and Zur, and Hur, and Reba — and also Balaam son of Beor they slew with the sword.
        ("וְאֶת-מַלְכֵי", "וקתלו כ'מסה מלוך", "And they slew the five kings of"),
        ("מִדְיָן", "מדין", "Midian"),
        ("עַל-חַלְלֵיהֶם", "מע קתלאהם", "together with their slain —"),
        ("אֶת-אֱוִי", "אוי", "Evi,"),
        ("וְאֶת-רֶקֶם", "ורקם", "and Rekem,"),
        ("וְאֶת-צוּר", "וצור", "and Zur,"),
        ("וְאֶת-חוּר", "וחור", "and Hur,"),
        ("וְאֶת-רֶבַע", "ורבע", "and Reba —"),
        (None, "ואיצ'א", "and also"),
        ("בִּלְעָם", "בלעם", "Balaam"),
        ("בֶּן-בְּעוֹר", "אבן בעור", "son of Beor"),
        ("הָרְגוּ", "קתלוה", "they slew"),
        ("בֶּחָרֶב", "באלסיף", "with the sword."),
    ],
    9: [
        # HE: וַיִּשְׁבּוּ בְנֵי-יִשְׂרָאֵל אֶת-נְשֵׁי מִדְיָן וְאֶת-טַפָּם וְאֵת כָּל-בְּהֶמְתָּם וְאֶת-כָּל-מִקְנֵהֶם וְאֶת-כָּל-חֵילָם בָּזָזוּ
        # JA: וסבא בני אסראיל נסא מדין ואטפאלהם. וגמיע בהאימהם ומואשיהם. ואת'את'הם ג'נמו
        # EN: And the sons of Israel took captive the women of Midian and their children; and all their beasts and their livestock, and their furnishings they plundered.
        ("וַיִּשְׁבּוּ", "וסבא", "And the sons of Israel took captive"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the women of Midian"),
        ("אֶת-נְשֵׁי מִדְיָן", "נסא מדין", "and their children;"),
        ("וְאֶת-טַפָּם", "ואטפאלהם", "and all their beasts"),
        ("וְאֵת כָּל-בְּהֶמְתָּם", "וגמיע בהאימהם", "their livestock,"),
        ("וְאֶת-כָּל-מִקְנֵהֶם", "ומואשיהם", "their furnishings"),
        ("וְאֶת-כָּל-חֵילָם בָּזָזוּ", "ואת'את'הם ג'נמו", "they plundered."),
    ],
    10: [
        # HE: וְאֵת כָּל-עָרֵיהֶם בְּמוֹשְׁבֹתָם וְאֵת כָּל-טִירֹתָם--שָׂרְפוּ בָּאֵשׁ
        # JA: וגמיע קראהם. מע מסאכנהם וקצורהם. אחרקוהא באלנאר
        # EN: And all their towns, together with their dwellings and their palaces, they burned with fire.
        ("וְאֵת כָּל-עָרֵיהֶם", "וגמיע קראהם", "And all their towns,"),
        ("בְּמוֹשְׁבֹתָם", "מע מסאכנהם", "together with their dwellings"),
        ("וְאֵת כָּל-טִירֹתָם", "וקצורהם", "and their palaces,"),
        ("שָׂרְפוּ", "אחרקוהא", "they burned"),
        ("בָּאֵשׁ", "באלנאר", "with fire."),
    ],
    11: [
        # HE: וַיִּקְחוּ אֶת-כָּל-הַשָּׁלָל וְאֵת כָּל-הַמַּלְקוֹחַ--בָּאָדָם וּבַבְּהֵמָה
        # JA: ואכ'דו גמיע אלסלב ואלפי. מן אלנאס ואלבהאים
        # EN: And they took all the spoil and the fay — from the people and the beasts.
        ("וַיִּקְחוּ", "ואכ'דו", "And they took"),
        ("אֶת-כָּל-הַשָּׁלָל", "גמיע אלסלב", "all the spoil"),
        ("וְאֵת כָּל-הַמַּלְקוֹחַ", "ואלפי", "and the fay —"),
        ("בָּאָדָם", "מן אלנאס", "from the people"),
        ("וּבַבְּהֵמָה", "ואלבהאים", "and the beasts."),
    ],
    12: [
        # HE: וַיָּבִאוּ אֶל-מֹשֶׁה וְאֶל-אֶלְעָזָר הַכֹּהֵן וְאֶל-עֲדַת בְּנֵי-יִשְׂרָאֵל אֶת-הַשְּׁבִי וְאֶת-הַמַּלְקוֹחַ וְאֶת-הַשָּׁלָל--אֶל-הַמַּחֲנֶה אֶל-עַרְבֹת מוֹאָב אֲשֶׁר עַל-יַרְדֵּן יְרֵחוֹ
        # JA: וגאו אלי' מוסי'. ואלי אלעזר אלאמאם וגמאעה' בני אסראיל. באלסבי ואלפי ואלנהב אלי' אלעסכר. אלי' בידאת מואב. אלתי עלי' ארדן יריחא
        # EN: And they came to Moses, and to Eleazar the imām, and to the assembly of the sons of Israel, with the captives and the fay and the plunder, to the encampment — to the wilderness plain of Moab, which is by the Jordan of Jericho.
        ("וַיָּבִאוּ", "וגאו", "And they came"),
        ("אֶל-מֹשֶׁה", "אלי' מוסי'", "to Moses,"),
        ("וְאֶל-אֶלְעָזָר הַכֹּהֵן", "ואלי אלעזר אלאמאם", "and to Eleazar the imām,"),
        ("וְאֶל-עֲדַת בְּנֵי-יִשְׂרָאֵל", "וגמאעה' בני אסראיל", "and to the assembly of the sons of Israel,"),
        ("אֶת-הַשְּׁבִי", "באלסבי", "with the captives"),
        ("וְאֶת-הַמַּלְקוֹחַ", "ואלפי", "and the fay"),
        ("וְאֶת-הַשָּׁלָל", "ואלנהב", "and the plunder,"),
        ("אֶל-הַמַּחֲנֶה", "אלי' אלעסכר", "to the encampment —"),
        ("אֶל-עַרְבֹת מוֹאָב", "אלי' בידאת מואב", "to the wilderness plain of Moab,"),
        ("אֲשֶׁר עַל-יַרְדֵּן", "אלתי עלי' ארדן", "which is by the Jordan of"),
        ("יְרֵחוֹ", "יריחא", "Jericho."),
    ],
    13: [
        # HE: וַיֵּצְאוּ מֹשֶׁה וְאֶלְעָזָר הַכֹּהֵן וְכָל-נְשִׂיאֵי הָעֵדָה--לִקְרָאתָם אֶל-מִחוּץ לַמַּחֲנֶה
        # JA: פכ'רג מוסי' ואלעזר אלאמאם. וסאיר אשראף אלגמאעה תלקאהם. אלי' כ'ארג אלעסכר
        # EN: And Moses and Eleazar the imām, and the rest of the chiefs of the assembly, went out to meet them, outside the encampment.
        ("וַיֵּצְאוּ", "פכ'רג", "And Moses"),
        ("מֹשֶׁה", "מוסי'", "and Eleazar the imām,"),
        ("וְאֶלְעָזָר הַכֹּהֵן", "ואלעזר אלאמאם", "and the rest of"),
        ("וְכָל-נְשִׂיאֵי הָעֵדָה", "וסאיר אשראף אלגמאעה", "the chiefs of the assembly,"),
        ("לִקְרָאתָם", "תלקאהם", "went out to meet them,"),
        ("אֶל-מִחוּץ", "אלי' כ'ארג", "outside"),
        ("לַמַּחֲנֶה", "אלעסכר", "the encampment."),
    ],
    14: [
        # HE: וַיִּקְצֹף מֹשֶׁה עַל פְּקוּדֵי הֶחָיִל שָׂרֵי הָאֲלָפִים וְשָׂרֵי הַמֵּאוֹת הַבָּאִים מִצְּבָא הַמִּלְחָמָה
        # JA: פסכ'ט מוסי'. עלי' אלמווכלין באלגיש. רויסא אלאלוף ורויסא אלמיין. אלגאיין מן אלחרב
        # EN: And Moses was wrathful with those entrusted over the army — the commanders of the thousands and the commanders of the hundreds — who were coming from the battle.
        ("וַיִּקְצֹף", "פסכ'ט", "And Moses was wrathful"),
        ("מֹשֶׁה", "מוסי'", "with those entrusted"),
        ("עַל פְּקוּדֵי הֶחָיִל", "עלי' אלמווכלין באלגיש", "over the army —"),
        ("שָׂרֵי הָאֲלָפִים", "רויסא אלאלוף", "the commanders of the thousands"),
        ("וְשָׂרֵי הַמֵּאוֹת", "ורויסא אלמיין", "and the commanders of the hundreds —"),
        ("הַבָּאִים", "אלגאיין", "who were coming"),
        ("מִצְּבָא הַמִּלְחָמָה", "מן אלחרב", "from the battle."),
    ],
    15: [
        # HE: וַיֹּאמֶר אֲלֵיהֶם מֹשֶׁה הַחִיִּיתֶם כָּל-נְקֵבָה
        # JA: פקאל להם מוסי'. הל אסתבקיתם כל אנתי'
        # EN: And Moses said to them: 'Have you let every female live?'
        ("וַיֹּאמֶר", "פקאל", "And Moses said"),
        ("אֲלֵיהֶם", "להם", "to them:"),
        ("מֹשֶׁה", "מוסי'", "'Have you let"),
        ("הַחִיִּיתֶם", "הל אסתבקיתם", "every female"),
        ("כָּל-נְקֵבָה", "כל אנתי'", "live?'"),
    ],
    16: [
        # HE: הֵן הֵנָּה הָיוּ לִבְנֵי יִשְׂרָאֵל בִּדְבַר בִּלְעָם לִמְסָר-מַעַל בַּיהוָה עַל-דְּבַר-פְּעוֹר וַתְּהִי הַמַּגֵּפָה בַּעֲדַת יְהוָה
        # JA: אליס הן כנן לבני אסראיל בקול בלעם. חתי אוקען נכת'א באללה בסבב פעור. פחל אלובא בגמאעה' אללה
        # EN: 'Were not these the ones who were to the sons of Israel, by the word of Balaam, until they brought about a breach of faith with God on account of Peor — and so the pestilence fell upon the assembly of God?'
        ("הֵן הֵנָּה", "אליס הן", "'Were not these"),
        ("הָיוּ לִבְנֵי יִשְׂרָאֵל", "כנן לבני אסראיל", "the ones who were to the sons of Israel,"),
        ("בִּדְבַר בִּלְעָם", "בקול בלעם", "by the word of Balaam,"),
        ("לִמְסָר-מַעַל", "חתי אוקען נכת'א", "until they brought about a breach of faith"),
        ("בַּיהוָה", "באללה", "with God"),
        ("עַל-דְּבַר-פְּעוֹר", "בסבב פעור", "on account of Peor —"),
        (None, "פחל", "and so"),
        ("וַתְּהִי הַמַּגֵּפָה", "אלובא", "the pestilence fell upon"),
        ("בַּעֲדַת יְהוָה", "בגמאעה' אללה", "the assembly of God?'"),
    ],
    17: [
        # HE: וְעַתָּה הִרְגוּ כָל-זָכָר בַּטָּף וְכָל-אִשָּׁה יֹדַעַת אִישׁ לְמִשְׁכַּב זָכָר--הֲרֹגוּ
        # JA: ואלאן. אקתלו כל ד'כר מן אלאטפאל. וכל אמראה. קד ערפת מצ'אגעה' אלרגאל אקתלוהא
        # EN: 'And now: kill every male among the children, and every woman who has known the lying with men — kill her.'
        ("וְעַתָּה", "ואלאן", "'And now:"),
        ("הִרְגוּ", "אקתלו", "kill"),
        ("כָל-זָכָר", "כל ד'כר", "every male"),
        ("בַּטָּף", "מן אלאטפאל", "among the children,"),
        ("וְכָל-אִשָּׁה", "וכל אמראה", "and every woman"),
        ("יֹדַעַת", "קד ערפת", "who has known"),
        ("לְמִשְׁכַּב זָכָר", "מצ'אגעה' אלרגאל", "the lying with men —"),
        ("הֲרֹגוּ", "אקתלוהא", "kill her.'"),
    ],
    18: [
        # HE: וְכֹל הַטַּף בַּנָּשִׁים אֲשֶׁר לֹא-יָדְעוּ מִשְׁכַּב זָכָר--הַחֲיוּ לָכֶם
        # JA: וסאיר אטפאל אלנסא. אלד'י לם יערפן מצ'אגעה' אלרגאל. אסתבקוהן לכם
        # EN: 'And the rest of the female children, who have not known the lying with men — let them live for yourselves.'
        ("וְכֹל הַטַּף", "וסאיר אטפאל", "'And the rest of the female children,"),
        ("בַּנָּשִׁים", "אלנסא", "who have not known"),
        ("אֲשֶׁר לֹא-יָדְעוּ", "אלד'י לם יערפן", "the lying with men —"),
        ("מִשְׁכַּב זָכָר", "מצ'אגעה' אלרגאל", "let them live"),
        ("הַחֲיוּ לָכֶם", "אסתבקוהן לכם", "for yourselves.'"),
    ],
    19: [
        # HE: וְאַתֶּם חֲנוּ מִחוּץ לַמַּחֲנֶה--שִׁבְעַת יָמִים כֹּל הֹרֵג נֶפֶשׁ וְכֹל נֹגֵעַ בֶּחָלָל תִּתְחַטְּאוּ בַּיּוֹם הַשְּׁלִישִׁי וּבַיּוֹם הַשְּׁבִיעִי--אַתֶּם וּשְׁבִיכֶם
        # JA: ואנתם. פאנזלו כ'ארג אלעסכר סבעה' אייאם. כל מן קתל נפסא וכל מן דנא בקתיל. תתד'כו פי אליום אלת'אלת' ופי אליום אלסאבע. אנתם וסביכם
        # EN: 'And as for you — encamp outside the encampment seven days; every one who has slain a person, and every one who has approached a slain man, shall be purified on the third day and on the seventh day — you and your captives.'
        ("וְאַתֶּם", "ואנתם", "'And as for you —"),
        ("חֲנוּ", "פאנזלו", "encamp"),
        ("מִחוּץ לַמַּחֲנֶה", "כ'ארג אלעסכר", "outside the encampment"),
        ("שִׁבְעַת יָמִים", "סבעה' אייאם", "seven days;"),
        ("כֹּל הֹרֵג נֶפֶשׁ", "כל מן קתל נפסא", "every one who has slain a person,"),
        ("וְכֹל נֹגֵעַ בֶּחָלָל", "וכל מן דנא בקתיל", "and every one who has approached a slain man,"),
        ("תִּתְחַטְּאוּ", "תתד'כו", "shall be purified"),
        ("בַּיּוֹם הַשְּׁלִישִׁי", "פי אליום אלת'אלת'", "on the third day"),
        ("וּבַיּוֹם הַשְּׁבִיעִי", "ופי אליום אלסאבע", "and on the seventh day —"),
        ("אַתֶּם", "אנתם", "you"),
        ("וּשְׁבִיכֶם", "וסביכם", "and your captives.'"),
    ],
    20: [
        # HE: וְכָל-בֶּגֶד וְכָל-כְּלִי-עוֹר וְכָל-מַעֲשֵׂה עִזִּים וְכָל-כְּלִי-עֵץ--תִּתְחַטָּאוּ
        # JA: וכל ת'וב ואניה מן גלוד. ומעמול מן מרעזא ואניה' כ'שב. תד'כוה
        # EN: 'And every garment and every vessel of leather, and anything made of fine soft wool and vessels of wood — purify them.'
        ("וְכָל-בֶּגֶד", "וכל ת'וב", "'And every garment"),
        ("וְכָל-כְּלִי-עוֹר", "ואניה מן גלוד", "and every vessel of leather,"),
        ("וְכָל-מַעֲשֵׂה עִזִּים", "ומעמול מן מרעזא", "and anything made of fine soft wool"),
        ("וְכָל-כְּלִי-עֵץ", "ואניה' כ'שב", "and vessels of wood —"),
        ("תִּתְחַטָּאוּ", "תד'כוה", "purify them.'"),
    ],
    21: [
        # HE: וַיֹּאמֶר אֶלְעָזָר הַכֹּהֵן אֶל-אַנְשֵׁי הַצָּבָא הַבָּאִים לַמִּלְחָמָה זֹאת חֻקַּת הַתּוֹרָה אֲשֶׁר-צִוָּה יְהוָה אֶת-מֹשֶׁה
        # JA: ת'ם קאל אלעזר אלאמאם לאלרגאל אלג'זאה. אלגאיין מן אלחרב. הד'א רסם אלשריעה. אלתי אמר אללה בהא מוסי'
        # EN: Then Eleazar the imām said to the men, the warriors, who were coming from the battle: 'This is the ordinance of the law which God commanded Moses.'
        (None, "ת'ם", "Then"),
        ("וַיֹּאמֶר", "קאל", "Eleazar the imām said"),
        ("אֶלְעָזָר הַכֹּהֵן", "אלעזר אלאמאם", "to the men,"),
        ("אֶל-אַנְשֵׁי הַצָּבָא", "לאלרגאל אלג'זאה", "the warriors,"),
        ("הַבָּאִים", "אלגאיין", "who were coming"),
        ("לַמִּלְחָמָה", "מן אלחרב", "from the battle:"),
        ("זֹאת", "הד'א", "'This is"),
        ("חֻקַּת הַתּוֹרָה", "רסם אלשריעה", "the ordinance of the law"),
        ("אֲשֶׁר-צִוָּה יְהוָה", "אלתי אמר אללה", "which God commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses.'"),
    ],
    22: [
        # HE: אַךְ אֶת-הַזָּהָב וְאֶת-הַכָּסֶף אֶת-הַנְּחֹשֶׁת אֶת-הַבַּרְזֶל אֶת-הַבְּדִיל וְאֶת-הָעֹפָרֶת
        # JA: אמא אלד'הב ואלפצה. ואלנחאס ואלחדיד. ואלקלעי ואלאסרב
        # EN: 'As for the gold and the silver, the copper and the iron, the tin and the lead —'
        ("אַךְ", "אמא", "'As for"),
        ("אֶת-הַזָּהָב", "אלד'הב", "the gold"),
        ("וְאֶת-הַכָּסֶף", "ואלפצה", "and the silver,"),
        ("אֶת-הַנְּחֹשֶׁת", "ואלנחאס", "the copper"),
        ("אֶת-הַבַּרְזֶל", "ואלחדיד", "and the iron,"),
        ("אֶת-הַבְּדִיל", "ואלקלעי", "the tin"),
        ("וְאֶת-הָעֹפָרֶת", "ואלאסרב", "and the lead —'"),
    ],
    23: [
        # HE: כָּל-דָּבָר אֲשֶׁר-יָבֹא בָאֵשׁ תַּעֲבִירוּ בָאֵשׁ וְטָהֵר--אַךְ בְּמֵי נִדָּה יִתְחַטָּא וְכֹל אֲשֶׁר לֹא-יָבֹא בָּאֵשׁ תַּעֲבִירוּ בַמָּיִם
        # JA: פכל שי ימכן אן ידכ'ל פי אלנאר. אמרוה באלנאר ויטהר. ואיצ'א יד'כא במא אלנצ'ח. וכל מא לא ידכ'ל. פי אלנאר אמרוה באלמא
        # EN: 'every thing that can enter into fire — pass it through the fire and it shall be clean; and it shall also be purified with the water of sprinkling. And everything that cannot enter into fire — pass it through the water.'
        ("כָּל-דָּבָר", "פכל שי", "'every thing"),
        ("אֲשֶׁר-יָבֹא בָאֵשׁ", "ימכן אן ידכ'ל פי אלנאר", "that can enter into fire —"),
        ("תַּעֲבִירוּ בָאֵשׁ", "אמרוה באלנאר", "pass it through the fire"),
        ("וְטָהֵר", "ויטהר", "and it shall be clean;"),
        (None, "ואיצ'א", "and it shall also be"),
        ("אַךְ בְּמֵי נִדָּה", "יד'כא במא אלנצ'ח", "purified with the water of sprinkling."),
        ("וְכֹל אֲשֶׁר לֹא-יָבֹא", "וכל מא לא ידכ'ל", "And everything that cannot enter into"),
        (None, "פי אלנאר", "fire —"),
        ("תַּעֲבִירוּ בַמָּיִם", "אמרוה באלמא", "pass it through the water.'"),
    ],
    24: [
        # HE: וְכִבַּסְתֶּם בִּגְדֵיכֶם בַּיּוֹם הַשְּׁבִיעִי וּטְהַרְתֶּם וְאַחַר תָּבֹאוּ אֶל-הַמַּחֲנֶה
        # JA: ואגסלו ת'יאבכם פי אליום אלסאבע ואטהרו. ובעד ד'אלך תדכ'לו אלי' אלעסכר
        # EN: 'And wash your garments on the seventh day, and be clean; and after that you shall enter the encampment.'
        ("וְכִבַּסְתֶּם", "ואגסלו", "'And wash"),
        ("בִּגְדֵיכֶם", "ת'יאבכם", "your garments"),
        ("בַּיּוֹם הַשְּׁבִיעִי", "פי אליום אלסאבע", "on the seventh day,"),
        ("וּטְהַרְתֶּם", "ואטהרו", "and be clean;"),
        ("וְאַחַר", "ובעד ד'אלך", "and after that"),
        ("תָּבֹאוּ", "תדכ'לו", "you shall enter"),
        ("אֶל-הַמַּחֲנֶה", "אלי' אלעסכר", "the encampment.'"),
    ],
    25: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: פקאל אללה למוסי קאילא
        # EN: And God said to Moses, saying:
        ("וַיֹּאמֶר", "פקאל", "And"),
        ("יְהוָה", "אללה", "God"),
        ("אֶל-מֹשֶׁה", "למוסי", "to Moses,"),
        ("לֵּאמֹר", "קאילא", "saying:"),
    ],
    26: [
        # HE: שָׂא אֵת רֹאשׁ מַלְקוֹחַ הַשְּׁבִי בָּאָדָם וּבַבְּהֵמָה--אַתָּה וְאֶלְעָזָר הַכֹּהֵן וְרָאשֵׁי אֲבוֹת הָעֵדָה
        # JA: ארפע גמלה' פי אלסבי. מן אלנאס ואלבהאים. אנת ואלעזר אלאמאם. ורויסא אבא אלגמאעה
        # EN: 'Take up the total count of what is in the captivity — of people and of beasts — you and Eleazar the imām and the heads of the fathers of the assembly.'
        ("שָׂא", "ארפע", "'Take up"),
        ("אֵת רֹאשׁ מַלְקוֹחַ הַשְּׁבִי", "גמלה' פי אלסבי", "the total count of what is in the captivity —"),
        ("בָּאָדָם", "מן אלנאס", "of people"),
        ("וּבַבְּהֵמָה", "ואלבהאים", "and of beasts —"),
        ("אַתָּה", "אנת", "you"),
        ("וְאֶלְעָזָר הַכֹּהֵן", "ואלעזר אלאמאם", "and Eleazar the imām"),
        ("וְרָאשֵׁי אֲבוֹת הָעֵדָה", "ורויסא אבא אלגמאעה", "and the heads of the fathers of the assembly.'"),
    ],
    27: [
        # HE: וְחָצִיתָ אֶת-הַמַּלְקוֹחַ בֵּין תֹּפְשֵׂי הַמִּלְחָמָה הַיֹּצְאִים לַצָּבָא--וּבֵין כָּל-הָעֵדָה
        # JA: ואקסם ד'אלך. בין אהל אלחרב. אלד'ין כ'רגו לאלג'זו. ובין סאיר אלגמאעה
        # EN: 'And divide it between the men of war who went out for the campaign, and the rest of the assembly.'
        ("וְחָצִיתָ", "ואקסם", "'And divide"),
        ("אֶת-הַמַּלְקוֹחַ", "ד'אלך", "it"),
        ("בֵּין תֹּפְשֵׂי הַמִּלְחָמָה", "בין אהל אלחרב", "between the men of war"),
        ("הַיֹּצְאִים", "אלד'ין כ'רגו", "who went out"),
        ("לַצָּבָא", "לאלג'זו", "for the campaign,"),
        ("וּבֵין כָּל-הָעֵדָה", "ובין סאיר אלגמאעה", "and the rest of the assembly.'"),
    ],
    28: [
        # HE: וַהֲרֵמֹתָ מֶכֶס לַיהוָה מֵאֵת אַנְשֵׁי הַמִּלְחָמָה הַיֹּצְאִים לַצָּבָא--אֶחָד נֶפֶשׁ מֵחֲמֵשׁ הַמֵּאוֹת מִן-הָאָדָם וּמִן-הַבָּקָר וּמִן-הַחֲמֹרִים וּמִן-הַצֹּאן
        # JA: וארפע מכסא ללה. מן אהל אלחרב אלכ'ארגין לאלג'זו. ראסא ואחדא. מן כל כ'מס מאיה. מן אלנאס ואלבקר. ואלחמיר ואלג'נם
        # EN: 'And levy a tax for God from the men of war who went out for the campaign: one head from every five hundred, of the people, and of the cattle, and of the donkeys, and of the flock.'
        ("וַהֲרֵמֹתָ", "וארפע", "'And levy"),
        ("מֶכֶס", "מכסא", "a tax"),
        ("לַיהוָה", "ללה", "for God"),
        ("מֵאֵת אַנְשֵׁי הַמִּלְחָמָה", "מן אהל אלחרב", "from the men of war"),
        ("הַיֹּצְאִים", "אלכ'ארגין", "who went out"),
        ("לַצָּבָא", "לאלג'זו", "for the campaign:"),
        ("אֶחָד נֶפֶשׁ", "ראסא ואחדא", "one head"),
        ("מֵחֲמֵשׁ הַמֵּאוֹת", "מן כל כ'מס מאיה", "from every five hundred,"),
        ("מִן-הָאָדָם", "מן אלנאס", "of the people,"),
        ("וּמִן-הַבָּקָר", "ואלבקר", "and of the cattle,"),
        ("וּמִן-הַחֲמֹרִים", "ואלחמיר", "and of the donkeys,"),
        ("וּמִן-הַצֹּאן", "ואלג'נם", "and of the flock.'"),
    ],
    29: [
        # HE: מִמַּחֲצִיתָם תִּקָּחוּ וְנָתַתָּה לְאֶלְעָזָר הַכֹּהֵן תְּרוּמַת יְהוָה
        # JA: כ'דו ד'אלך מן קסמהם רפיעה ללה. ואדפעו ד'אלך לאלעזר אלאמאם
        # EN: 'Take that from their portion as an elevation-gift for God, and deliver it to Eleazar the imām.'
        ("מִמַּחֲצִיתָם תִּקָּחוּ", "כ'דו ד'אלך מן קסמהם", "'Take that from their portion"),
        ("תְּרוּמַת יְהוָה", "רפיעה ללה", "as an elevation-gift for God,"),
        ("וְנָתַתָּה", "ואדפעו ד'אלך", "and deliver it"),
        ("לְאֶלְעָזָר הַכֹּהֵן", "לאלעזר אלאמאם", "to Eleazar the imām.'"),
    ],
    30: [
        # HE: וּמִמַּחֲצִת בְּנֵי-יִשְׂרָאֵל תִּקַּח אֶחָד אָחֻז מִן-הַחֲמִשִּׁים מִן-הָאָדָם מִן-הַבָּקָר מִן-הַחֲמֹרִים וּמִן-הַצֹּאן--מִכָּל-הַבְּהֵמָה וְנָתַתָּה אֹתָם לַלְוִיִּם שֹׁמְרֵי מִשְׁמֶרֶת מִשְׁכַּן יְהוָה
        # JA: וכ'ד' מן קסם בני אסראיל ואחדא מן כ'מסין. מן אלנאס ואלבקר. ואלחמיר ואלג'נם וסאיר אלבהאים. ואדפע ד'אלך אלי' אלליואניין. חאפצ'י מחפץ' מסכן אללה
        # EN: 'And from the portion of the sons of Israel, take one from every fifty — of the people, and of the cattle, and of the donkeys, and of the flock, and the rest of the beasts — and deliver it to the Levites, the keepers of the charge of the tabernacle of God.'
        ("וּמִמַּחֲצִת בְּנֵי-יִשְׂרָאֵל", "וכ'ד' מן קסם בני אסראיל", "'And from the portion of the sons of Israel,"),
        ("תִּקַּח אֶחָד", "ואחדא", "take one"),
        ("מִן-הַחֲמִשִּׁים", "מן כ'מסין", "from every fifty —"),
        ("מִן-הָאָדָם", "מן אלנאס", "of the people,"),
        ("מִן-הַבָּקָר", "ואלבקר", "and of the cattle,"),
        ("מִן-הַחֲמֹרִים", "ואלחמיר", "and of the donkeys,"),
        ("וּמִן-הַצֹּאן", "ואלג'נם", "and of the flock,"),
        ("מִכָּל-הַבְּהֵמָה", "וסאיר אלבהאים", "and the rest of the beasts —"),
        ("וְנָתַתָּה אֹתָם", "ואדפע ד'אלך אלי'", "and deliver it to"),
        ("לַלְוִיִּם", "אלליואניין", "the Levites,"),
        ("שֹׁמְרֵי מִשְׁמֶרֶת", "חאפצ'י מחפץ'", "the keepers of the charge of"),
        ("מִשְׁכַּן יְהוָה", "מסכן אללה", "the tabernacle of God.'"),
    ],
    31: [
        # HE: וַיַּעַשׂ מֹשֶׁה וְאֶלְעָזָר הַכֹּהֵן כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה
        # JA: פצנע מוסי'. ואלעזר אלאמאם. כמא אמר אללה מוסי'
        # EN: And Moses and Eleazar the imām did as God had commanded Moses.
        ("וַיַּעַשׂ", "פצנע", "And Moses"),
        ("מֹשֶׁה", "מוסי'", "and Eleazar"),
        ("וְאֶלְעָזָר הַכֹּהֵן", "ואלעזר אלאמאם", "the imām did"),
        ("כַּאֲשֶׁר", "כמא", "as"),
        ("צִוָּה יְהוָה", "אמר אללה", "God had commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses."),
    ],
    32: [
        # HE: וַיְהִי הַמַּלְקוֹחַ--יֶתֶר הַבָּז אֲשֶׁר בָּזְזוּ עַם הַצָּבָא צֹאן שֵׁשׁ-מֵאוֹת אֶלֶף וְשִׁבְעִים אֶלֶף--וַחֲמֵשֶׁת אֲלָפִים
        # JA: וכאן אלפי. ג'מלה' אלג'נימה. אלתי ג'נמהא אלקום אלג'זאה. עדד אלג'נם. סת מאיה' אלף. וכמסה וסבעין אלפא
        # EN: And the fay — the total of the plunder which the raiding people had plundered — the number of the flock: six hundred thousand and seventy-five thousand.
        ("וַיְהִי הַמַּלְקוֹחַ", "וכאן אלפי", "And the fay —"),
        ("יֶתֶר הַבָּז", "ג'מלה' אלג'נימה", "the total of the plunder"),
        ("אֲשֶׁר בָּזְזוּ", "אלתי ג'נמהא", "which"),
        ("עַם הַצָּבָא", "אלקום אלג'זאה", "the raiding people had plundered —"),
        ("צֹאן", "עדד אלג'נם", "the number of the flock:"),
        ("שֵׁשׁ-מֵאוֹת אֶלֶף", "סת מאיה' אלף", "six hundred thousand"),
        ("וְשִׁבְעִים אֶלֶף", "וכמסה וסבעין אלפא", "and seventy-five thousand."),
    ],
    33: [
        # HE: וּבָקָר שְׁנַיִם וְשִׁבְעִים אָלֶף
        # JA: ועדד אלבקר. את'נין וסבעין אלפא
        # EN: And the number of the cattle: seventy-two thousand.
        ("וּבָקָר", "ועדד אלבקר", "And the number of the cattle:"),
        ("שְׁנַיִם", "את'נין", "seventy-two"),
        ("וְשִׁבְעִים אָלֶף", "וסבעין אלפא", "thousand."),
    ],
    34: [
        # HE: וַחֲמֹרִים אֶחָד וְשִׁשִּׁים אָלֶף
        # JA: ועדד אלחמיר. ואחד וסתין אלפא
        # EN: And the number of the donkeys: sixty-one thousand.
        ("וַחֲמֹרִים", "ועדד אלחמיר", "And the number of the donkeys:"),
        ("אֶחָד", "ואחד", "sixty-one"),
        ("וְשִׁשִּׁים אָלֶף", "וסתין אלפא", "thousand."),
    ],
    35: [
        # HE: וְנֶפֶשׁ אָדָם--מִן-הַנָּשִׁים אֲשֶׁר לֹא-יָדְעוּ מִשְׁכַּב זָכָר כָּל-נֶפֶשׁ שְׁנַיִם וּשְׁלֹשִׁים אָלֶף
        # JA: ומן אלנאס. מן אלנסא. אלתי לם יערפן מצ'אגעה' אלרגאל. את'נין ות'לאת'ין אלפא
        # EN: And from the people, from the women who had not known the lying with men: thirty-two thousand.
        ("וְנֶפֶשׁ אָדָם", "ומן אלנאס", "And from the people,"),
        ("מִן-הַנָּשִׁים", "מן אלנסא", "from the women"),
        ("אֲשֶׁר לֹא-יָדְעוּ", "אלתי לם יערפן", "who had not known"),
        ("מִשְׁכַּב זָכָר", "מצ'אגעה' אלרגאל", "the lying with men:"),
        ("שְׁנַיִם", "את'נין", "thirty-two"),
        ("וּשְׁלֹשִׁים אָלֶף", "ות'לאת'ין אלפא", "thousand."),
    ],
    36: [
        # HE: וַתְּהִי הַמֶּחֱצָה--חֵלֶק הַיֹּצְאִים בַּצָּבָא מִסְפַּר הַצֹּאן שְׁלֹשׁ-מֵאוֹת אֶלֶף וּשְׁלֹשִׁים אֶלֶף וְשִׁבְעַת אֲלָפִים וַחֲמֵשׁ מֵאוֹת
        # JA: פכאן נצף ד'אלך. והו נציב אלד'י כ'רגו לאלג'זו. עדד אלג'נם. ת'לאת' מאיה אלף. וסבעה ות'לאת'ין אלפא וכ'מס מאיה
        # EN: And the half thereof — being the portion of those who went out for the campaign — the number of the flock: three hundred thousand and thirty-seven thousand and five hundred.
        ("וַתְּהִי הַמֶּחֱצָה", "פכאן נצף ד'אלך", "And the half thereof —"),
        ("חֵלֶק הַיֹּצְאִים", "והו נציב אלד'י כ'רגו", "being the portion of those who went out"),
        ("בַּצָּבָא", "לאלג'זו", "for the campaign —"),
        ("מִסְפַּר הַצֹּאן", "עדד אלג'נם", "the number of the flock:"),
        ("שְׁלֹשׁ-מֵאוֹת אֶלֶף", "ת'לאת' מאיה אלף", "three hundred thousand"),
        ("וּשְׁלֹשִׁים אֶלֶף", "וסבעה ות'לאת'ין אלפא", "and thirty-seven thousand"),
        ("וְשִׁבְעַת אֲלָפִים וַחֲמֵשׁ מֵאוֹת", "וכ'מס מאיה", "and five hundred."),
    ],
    37: [
        # HE: וַיְהִי הַמֶּכֶס לַיהוָה מִן-הַצֹּאן--שֵׁשׁ מֵאוֹת חָמֵשׁ וְשִׁבְעִים
        # JA: פכאן עדד אלמכס ללה מן אלג'נם. סת מאיה וכמסה וסבעין ראסא
        # EN: And the number of the tax for God from the flock was six hundred and seventy-five head.
        ("וַיְהִי הַמֶּכֶס", "פכאן עדד אלמכס", "And the number of the tax"),
        ("לַיהוָה", "ללה", "for God"),
        ("מִן-הַצֹּאן", "מן אלג'נם", "from the flock"),
        ("שֵׁשׁ מֵאוֹת", "סת מאיה", "was six hundred"),
        ("חָמֵשׁ וְשִׁבְעִים", "וכמסה וסבעין ראסא", "and seventy-five head."),
    ],
    38: [
        # HE: וְהַבָּקָר--שִׁשָּׁה וּשְׁלֹשִׁים אָלֶף וּמִכְסָם לַיהוָה שְׁנַיִם וְשִׁבְעִים
        # JA: ואד' אלבקר סתה ות'לאת'ין אלפא. פמכסהם ללה את'נין וסבעין
        # EN: And the number of the cattle: thirty-six thousand; and their tax for God: seventy-two.
        ("וְהַבָּקָר", "ואד' אלבקר", "And the number of the cattle:"),
        ("שִׁשָּׁה וּשְׁלֹשִׁים אָלֶף", "סתה ות'לאת'ין אלפא", "thirty-six thousand;"),
        ("וּמִכְסָם", "פמכסהם", "and their tax"),
        ("לַיהוָה", "ללה", "for God:"),
        ("שְׁנַיִם וְשִׁבְעִים", "את'נין וסבעין", "seventy-two."),
    ],
    39: [
        # HE: וַחֲמֹרִים שְׁלֹשִׁים אֶלֶף וַחֲמֵשׁ מֵאוֹת וּמִכְסָם לַיהוָה אֶחָד וְשִׁשִּׁים
        # JA: ואד' אלחמיר. ת'לאת'ין אלפא וכ'מס מאיה. פמכסהם ללה ואחד וסתין
        # EN: And the number of the donkeys: thirty thousand and five hundred; and their tax for God: sixty-one.
        ("וַחֲמֹרִים", "ואד' אלחמיר", "And the number of the donkeys:"),
        ("שְׁלֹשִׁים אֶלֶף", "ת'לאת'ין אלפא", "thirty thousand"),
        ("וַחֲמֵשׁ מֵאוֹת", "וכ'מס מאיה", "and five hundred;"),
        ("וּמִכְסָם", "פמכסהם", "and their tax"),
        ("לַיהוָה", "ללה", "for God:"),
        ("אֶחָד וְשִׁשִּׁים", "ואחד וסתין", "sixty-one."),
    ],
    40: [
        # HE: וְנֶפֶשׁ אָדָם שִׁשָּׁה עָשָׂר אָלֶף וּמִכְסָם לַיהוָה--שְׁנַיִם וּשְׁלֹשִׁים נָפֶשׁ
        # JA: ואד' נפוס אלנאס. סתה' עשר אלפא. פמכסהם ללה. את'נין ות'לאת'ין נפסא
        # EN: And the number of persons: sixteen thousand; and their tax for God: thirty-two persons.
        ("וְנֶפֶשׁ אָדָם", "ואד' נפוס אלנאס", "And the number of persons:"),
        ("שִׁשָּׁה עָשָׂר אָלֶף", "סתה' עשר אלפא", "sixteen thousand;"),
        ("וּמִכְסָם", "פמכסהם", "and their tax"),
        ("לַיהוָה", "ללה", "for God:"),
        ("שְׁנַיִם וּשְׁלֹשִׁים נָפֶשׁ", "את'נין ות'לאת'ין נפסא", "thirty-two persons."),
    ],
    41: [
        # HE: וַיִּתֵּן מֹשֶׁה אֶת-מֶכֶס תְּרוּמַת יְהוָה לְאֶלְעָזָר הַכֹּהֵן--כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה
        # JA: פדפע מוסי'. אלמכס אלמרפוע ללה. אלי' אלעזר אלאמאם. כמא אמרה אללה
        # EN: And Moses delivered the tax levied for God to Eleazar the imām, as God had commanded him.
        ("וַיִּתֵּן", "פדפע", "And Moses delivered"),
        ("מֹשֶׁה", "מוסי'", "the tax"),
        ("אֶת-מֶכֶס תְּרוּמַת יְהוָה", "אלמכס אלמרפוע ללה", "levied for God"),
        ("לְאֶלְעָזָר הַכֹּהֵן", "אלי' אלעזר אלאמאם", "to Eleazar the imām,"),
        ("כַּאֲשֶׁר", "כמא", "as"),
        ("צִוָּה יְהוָה אֶת-מֹשֶׁה", "אמרה אללה", "God had commanded him."),
    ],
    42: [
        # HE: וּמִמַּחֲצִית בְּנֵי יִשְׂרָאֵל אֲשֶׁר חָצָה מֹשֶׁה מִן-הָאֲנָשִׁים הַצֹּבְאִים
        # JA: ומן קסם בני אסראיל אלד'י קסם מוסי'. מן אלקום אלג'זאה
        # EN: And from the count of the portion of the sons of Israel which Moses had divided from the raiding people —
        ("וּמִמַּחֲצִית", "ומן קסם", "And from the count of the portion of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("אֲשֶׁר חָצָה", "אלד'י קסם", "which"),
        ("מֹשֶׁה", "מוסי'", "Moses had divided"),
        ("מִן-הָאֲנָשִׁים הַצֹּבְאִים", "מן אלקום אלג'זאה", "from the raiding people —"),
    ],
    43: [
        # HE: וַתְּהִי מֶחֱצַת הָעֵדָה מִן-הַצֹּאן--שְׁלֹשׁ-מֵאוֹת אֶלֶף וּשְׁלֹשִׁים אֶלֶף שִׁבְעַת אֲלָפִים וַחֲמֵשׁ מֵאוֹת
        # JA: פכאן ד'אלך מן אלג'נם. ת'לאת' מאיה' אלף. וסבעה ות'לאת'ין אלפא וכ'מס מאיה
        # EN: that was, from the flock: three hundred thousand and thirty-seven thousand and five hundred;
        ("וַתְּהִי מֶחֱצַת הָעֵדָה", "פכאן ד'אלך", "that was,"),
        ("מִן-הַצֹּאן", "מן אלג'נם", "from the flock:"),
        ("שְׁלֹשׁ-מֵאוֹת אֶלֶף", "ת'לאת' מאיה' אלף", "three hundred thousand"),
        ("וּשְׁלֹשִׁים אֶלֶף", "וסבעה ות'לאת'ין אלפא", "and thirty-seven thousand"),
        ("שִׁבְעַת אֲלָפִים וַחֲמֵשׁ מֵאוֹת", "וכ'מס מאיה", "and five hundred;"),
    ],
    44: [
        # HE: וּבָקָר שִׁשָּׁה וּשְׁלֹשִׁים אָלֶף
        # JA: ומן אלבקר. סתה ות'לאת'ין אלפא
        # EN: and from the cattle: thirty-six thousand;
        ("וּבָקָר", "ומן אלבקר", "and from the cattle:"),
        ("שִׁשָּׁה", "סתה", "thirty-six"),
        ("וּשְׁלֹשִׁים אָלֶף", "ות'לאת'ין אלפא", "thousand;"),
    ],
    45: [
        # HE: וַחֲמֹרִים שְׁלֹשִׁים אֶלֶף וַחֲמֵשׁ מֵאוֹת
        # JA: ומן אלחמיר. ת'לאת'ין אלפא וכ'מס מאיה
        # EN: and from the donkeys: thirty thousand and five hundred;
        ("וַחֲמֹרִים", "ומן אלחמיר", "and from the donkeys:"),
        ("שְׁלֹשִׁים אֶלֶף", "ת'לאת'ין אלפא", "thirty thousand"),
        ("וַחֲמֵשׁ מֵאוֹת", "וכ'מס מאיה", "and five hundred;"),
    ],
    46: [
        # HE: וְנֶפֶשׁ אָדָם שִׁשָּׁה עָשָׂר אָלֶף
        # JA: ומן נפוס אלנאס. סתה' עשר אלפא
        # EN: and from the persons: sixteen thousand —
        ("וְנֶפֶשׁ אָדָם", "ומן נפוס אלנאס", "and from the persons:"),
        ("שִׁשָּׁה עָשָׂר", "סתה' עשר", "sixteen"),
        ("אָלֶף", "אלפא", "thousand —"),
    ],
    47: [
        # HE: וַיִּקַּח מֹשֶׁה מִמַּחֲצִת בְּנֵי-יִשְׂרָאֵל אֶת-הָאָחֻז אֶחָד מִן-הַחֲמִשִּׁים--מִן-הָאָדָם וּמִן-הַבְּהֵמָה וַיִּתֵּן אֹתָם לַלְוִיִּם שֹׁמְרֵי מִשְׁמֶרֶת מִשְׁכַּן יְהוָה כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה
        # JA: פאכ'ד' מוסי' מן ד'אלך. ואחדא מן כל כ'מסין. מן אלנאס ואלבהאים. ודפעהא אלי' אלליוניין. חאפצ'י מחפץ' מסכן אללה. כמא אמרה
        # EN: Moses took from that one from every fifty, of the people and the beasts, and delivered it to the Levites, the keepers of the charge of the tabernacle of God, as He had commanded him.
        ("וַיִּקַּח", "פאכ'ד'", "Moses took"),
        ("מֹשֶׁה", "מוסי'", "from that"),
        ("מִמַּחֲצִת בְּנֵי-יִשְׂרָאֵל", "מן ד'אלך", "one from every fifty,"),
        ("אֶת-הָאָחֻז אֶחָד", "ואחדא", "of the people"),
        ("מִן-הַחֲמִשִּׁים", "מן כל כ'מסין", "and the beasts,"),
        ("מִן-הָאָדָם", "מן אלנאס", "and delivered it"),
        ("וּמִן-הַבְּהֵמָה", "ואלבהאים", "to the Levites,"),
        ("וַיִּתֵּן אֹתָם לַלְוִיִּם", "ודפעהא אלי' אלליוניין", "the keepers of the charge of"),
        ("שֹׁמְרֵי מִשְׁמֶרֶת", "חאפצ'י מחפץ'", "the tabernacle of God,"),
        ("מִשְׁכַּן יְהוָה", "מסכן אללה", "as He had commanded"),
        ("כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה", "כמא אמרה", "him."),
    ],
    48: [
        # HE: וַיִּקְרְבוּ אֶל-מֹשֶׁה הַפְּקֻדִים אֲשֶׁר לְאַלְפֵי הַצָּבָא--שָׂרֵי הָאֲלָפִים וְשָׂרֵי הַמֵּאוֹת
        # JA: ת'ם תקדם אלי' מוסי' אלמווכלין באלוף אלגיש. רויסא אלאלוף ורויסא אלמיין
        # EN: Then those entrusted over the thousands of the army — the commanders of the thousands and the commanders of the hundreds — came forward to Moses,
        (None, "ת'ם", "Then"),
        ("וַיִּקְרְבוּ", "תקדם", "those entrusted"),
        ("אֶל-מֹשֶׁה", "אלי' מוסי'", "over the thousands of the army —"),
        ("הַפְּקֻדִים", "אלמווכלין", "the commanders of the thousands"),
        ("אֲשֶׁר לְאַלְפֵי הַצָּבָא", "באלוף אלגיש", "and the commanders of the hundreds —"),
        ("שָׂרֵי הָאֲלָפִים", "רויסא אלאלוף", "came forward"),
        ("וְשָׂרֵי הַמֵּאוֹת", "ורויסא אלמיין", "to Moses,"),
    ],
    49: [
        # HE: וַיֹּאמְרוּ אֶל-מֹשֶׁה עֲבָדֶיךָ נָשְׂאוּ אֶת-רֹאשׁ אַנְשֵׁי הַמִּלְחָמָה אֲשֶׁר בְּיָדֵנוּ וְלֹא-נִפְקַד מִמֶּנּוּ אִישׁ
        # JA: פקאלו למוסי. אן עבידך רפעו. ג'מלה' אהל אלחרב אלד'ין מענא. ולם י'פקד מנא רגל
        # EN: and said to Moses: 'Your servants have tallied the total of the men of war who are with us, and not a man is missing from us.'
        ("וַיֹּאמְרוּ", "פקאלו", "and said"),
        ("אֶל-מֹשֶׁה", "למוסי", "to Moses:"),
        (None, "אן", "'Your servants"),
        ("עֲבָדֶיךָ", "עבידך", "have tallied"),
        ("נָשְׂאוּ", "רפעו", "the total of"),
        ("אֶת-רֹאשׁ אַנְשֵׁי הַמִּלְחָמָה", "ג'מלה' אהל אלחרב", "the men of war"),
        ("אֲשֶׁר בְּיָדֵנוּ", "אלד'ין מענא", "who are with us,"),
        ("וְלֹא-נִפְקַד", "ולם י'פקד", "and not a man is missing"),
        ("מִמֶּנּוּ אִישׁ", "מנא רגל", "from us.'"),
    ],
    50: [
        # HE: וַנַּקְרֵב אֶת-קָרְבַּן יְהוָה אִישׁ אֲשֶׁר מָצָא כְלִי-זָהָב אֶצְעָדָה וְצָמִיד טַבַּעַת עָגִיל וְכוּמָז--לְכַפֵּר עַל-נַפְשֹׁתֵינוּ לִפְנֵי יְהוָה
        # JA: וקד קדמנא קרבאן אללה אי רגל מנא וגד אניה' ד'הב מן דמלג וסואר. וחלקה ותרכי וחקאב. לנסתג'פר ען נפוסנא בין ידי אללה
        # EN: 'And we have brought forward the offering of God — every man among us who found golden vessels: armlets and bracelets, rings and earrings and girdles — to seek forgiveness for our souls before God.'
        ("וַנַּקְרֵב", "וקד קדמנא", "'And we have brought forward"),
        ("אֶת-קָרְבַּן יְהוָה", "קרבאן אללה", "the offering of God —"),
        ("אִישׁ אֲשֶׁר מָצָא", "אי רגל מנא וגד", "every man among us who found"),
        ("כְלִי-זָהָב", "אניה' ד'הב", "golden vessels:"),
        ("אֶצְעָדָה", "מן דמלג", "armlets"),
        ("וְצָמִיד", "וסואר", "and bracelets,"),
        ("טַבַּעַת", "וחלקה", "rings"),
        ("עָגִיל", "ותרכי", "and earrings"),
        ("וְכוּמָז", "וחקאב", "and girdles —"),
        ("לְכַפֵּר", "לנסתג'פר", "to seek forgiveness"),
        ("עַל-נַפְשֹׁתֵינוּ", "ען נפוסנא", "for our souls"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God.'"),
    ],
    51: [
        # HE: וַיִּקַּח מֹשֶׁה וְאֶלְעָזָר הַכֹּהֵן אֶת-הַזָּהָב--מֵאִתָּם כֹּל כְּלִי מַעֲשֶׂה
        # JA: פקבץ' מוסי' ואלעזר אלאמאם. ד'אלך אלד'הב מנהם. כל אניה מצווג'ה
        # EN: And Moses and Eleazar the imām received that gold from them — every wrought vessel.
        ("וַיִּקַּח", "פקבץ'", "And Moses"),
        ("מֹשֶׁה", "מוסי'", "and Eleazar the imām"),
        ("וְאֶלְעָזָר הַכֹּהֵן", "ואלעזר אלאמאם", "received"),
        ("אֶת-הַזָּהָב", "ד'אלך אלד'הב", "that gold"),
        ("מֵאִתָּם", "מנהם", "from them —"),
        ("כֹּל כְּלִי מַעֲשֶׂה", "כל אניה מצווג'ה", "every wrought vessel."),
    ],
    52: [
        # HE: וַיְהִי כָּל-זְהַב הַתְּרוּמָה אֲשֶׁר הֵרִימוּ לַיהוָה--שִׁשָּׁה עָשָׂר אֶלֶף שְׁבַע-מֵאוֹת וַחֲמִשִּׁים שָׁקֶל מֵאֵת שָׂרֵי הָאֲלָפִים וּמֵאֵת שָׂרֵי הַמֵּאוֹת
        # JA: פכאן כל ד'הב אלרפיעה. אלד'י רפעו ללה. סתה' עשר אלף. וסבע מאיה וכ'מסין מת'קאל. מן רויסא אלאלוף. ומן רויסא אלמיין
        # EN: And all the gold of the elevation-gifts which they raised up for God was sixteen thousand seven hundred and fifty weights, from the commanders of the thousands and from the commanders of the hundreds.
        ("וַיְהִי כָּל-זְהַב הַתְּרוּמָה", "פכאן כל ד'הב אלרפיעה", "And all the gold of the elevation-gifts"),
        ("אֲשֶׁר הֵרִימוּ", "אלד'י רפעו", "which they raised up"),
        ("לַיהוָה", "ללה", "for God"),
        ("שִׁשָּׁה עָשָׂר אֶלֶף", "סתה' עשר אלף", "was sixteen thousand"),
        ("שְׁבַע-מֵאוֹת וַחֲמִשִּׁים שָׁקֶל", "וסבע מאיה וכ'מסין מת'קאל", "seven hundred and fifty weights,"),
        ("מֵאֵת שָׂרֵי הָאֲלָפִים", "מן רויסא אלאלוף", "from the commanders of the thousands"),
        ("וּמֵאֵת שָׂרֵי הַמֵּאוֹת", "ומן רויסא אלמיין", "and from the commanders of the hundreds."),
    ],
    53: [
        # HE: אַנְשֵׁי הַצָּבָא בָּזְזוּ אִישׁ לוֹ
        # JA: אמא סאיר אהל אלג'זו. פמא ג'נמוה כל ואחד כאן לה
        # EN: As for the rest of the men of the campaign — whatever each one had plundered belonged to him.
        ("אַנְשֵׁי הַצָּבָא", "אמא סאיר אהל אלג'זו", "As for the rest of the men of the campaign —"),
        (None, "פמא ג'נמוה", "whatever"),
        ("בָּזְזוּ", "כל ואחד", "each one had plundered"),
        ("אִישׁ לוֹ", "כאן לה", "belonged to him."),
    ],
    54: [
        # HE: וַיִּקַּח מֹשֶׁה וְאֶלְעָזָר הַכֹּהֵן אֶת-הַזָּהָב מֵאֵת שָׂרֵי הָאֲלָפִים וְהַמֵּאוֹת וַיָּבִאוּ אֹתוֹ אֶל-אֹהֶל מוֹעֵד זִכָּרוֹן לִבְנֵי-יִשְׂרָאֵל לִפְנֵי יְהוָה
        # JA: ולמא אכ'ד' מוסי'. ואלעזר אלאמאם אלד'הב. מן רויסא אלאלוף ואלמיין. אתו בה אלי' כ'בא אלמחצ'ר. ד'כרא לבני אסראיל בין ידי אללה
        # EN: And when Moses and Eleazar the imām had received the gold from the commanders of the thousands and the hundreds, they brought it to the tent of the assembly, as a memorial for the sons of Israel before God.
        ("וַיִּקַּח", "ולמא אכ'ד'", "And when Moses"),
        ("מֹשֶׁה", "מוסי'", "and Eleazar the imām"),
        ("וְאֶלְעָזָר הַכֹּהֵן", "ואלעזר אלאמאם", "had received"),
        ("אֶת-הַזָּהָב", "אלד'הב", "the gold"),
        ("מֵאֵת שָׂרֵי הָאֲלָפִים", "מן רויסא אלאלוף", "from the commanders of the thousands"),
        ("וְהַמֵּאוֹת", "ואלמיין", "and the hundreds,"),
        ("וַיָּבִאוּ אֹתוֹ", "אתו בה", "they brought it"),
        ("אֶל-אֹהֶל מוֹעֵד", "אלי' כ'בא אלמחצ'ר", "to the tent of the assembly,"),
        ("זִכָּרוֹן", "ד'כרא", "as a memorial"),
        ("לִבְנֵי-יִשְׂרָאֵל", "לבני אסראיל", "for the sons of Israel"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God."),
    ],
}

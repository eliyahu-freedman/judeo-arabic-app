"""Hand-authored word-level alignment triples for Bamidbar chapter 25."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיֵּשֶׁב יִשְׂרָאֵל בַּשִּׁטִּים וַיָּחֶל הָעָם לִזְנוֹת אֶל-בְּנוֹת מוֹאָב
        # JA: ת'ם אקאם אל אסראיל פי שטין. פבדא אלקום. אן יזאנו בנאת מואב
        # EN: Then Israel settled in Shittim, and the people began to commit fornication with the daughters of Moab.
        (None, "ת'ם", "Then"),
        ("וַיֵּשֶׁב", "אקאם", "settled"),
        ("יִשְׂרָאֵל", "אל אסראיל", "Israel"),
        ("בַּשִּׁטִּים", "פי שטין", "in Shittim,"),
        ("וַיָּחֶל", "פבדא", "and the people began"),
        ("הָעָם", "אלקום", "to commit"),
        ("לִזְנוֹת", "אן יזאנו", "fornication"),
        ("אֶל-בְּנוֹת", "בנאת", "with the daughters of"),
        ("מוֹאָב", "מואב", "Moab."),
    ],
    2: [
        # HE: וַתִּקְרֶאןָ לָעָם לְזִבְחֵי אֱלֹהֵיהֶן וַיֹּאכַל הָעָם וַיִּשְׁתַּחֲווּ לֵאלֹהֵיהֶן
        # JA: פדעין באלקום. לד'באיח מעבודאתהן. פאכלו מנהא. וסגדו להא
        # EN: And they invited the people to the sacrifices of their objects of worship, and they ate of them and bowed down to them.
        ("וַתִּקְרֶאןָ", "פדעין", "And they invited"),
        ("לָעָם", "באלקום", "the people"),
        ("לְזִבְחֵי", "לד'באיח", "to the sacrifices of"),
        ("אֱלֹהֵיהֶן", "מעבודאתהן", "their objects of worship,"),
        ("וַיֹּאכַל הָעָם", "פאכלו", "and they ate"),
        (None, "מנהא", "of them"),
        ("וַיִּשְׁתַּחֲווּ", "וסגדו", "and bowed down"),
        ("לֵאלֹהֵיהֶן", "להא", "to them."),
    ],
    3: [
        # HE: וַיִּצָּמֶד יִשְׂרָאֵל לְבַעַל פְּעוֹר וַיִּחַר-אַף יְהוָה בְּיִשְׂרָאֵל
        # JA: פלאזם אל אסראיל פעור אלצנם. פאשתד ג'צ'ב אללה עלי'הם
        # EN: And the house of Israel attached itself to Pe'or the idol, and the anger of God intensified against them.
        ("וַיִּצָּמֶד", "פלאזם", "And the house of"),
        ("יִשְׂרָאֵל", "אל אסראיל", "Israel attached itself"),
        ("לְבַעַל פְּעוֹר", "פעור", "Pe'or"),
        (None, "אלצנם", "the idol,"),
        ("וַיִּחַר-אַף", "פאשתד ג'צ'ב", "and the anger of"),
        ("יְהוָה", "אללה", "God"),
        ("בְּיִשְׂרָאֵל", "עלי'הם", "intensified against them."),
    ],
    4: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה קַח אֶת-כָּל-רָאשֵׁי הָעָם וְהוֹקַע אוֹתָם לַיהוָה נֶגֶד הַשָּׁמֶשׁ וְיָשֹׁב חֲרוֹן אַף-יְהוָה מִיִּשְׂרָאֵל
        # JA: פקאל אללה למוסי. כ'ד' גמיע רויסא אלקום. ואצלבהם ללה חד'א אלשמס. וירגע שדה' ג'צ'ב אללה מן אל אסראיל
        # EN: And God said to Moses: 'Take all the chiefs of the people, and crucify them before God facing the sun — that the intensity of God's anger may turn away from the house of Israel.'
        ("וַיֹּאמֶר", "פקאל", "And"),
        ("יְהוָה", "אללה", "God said"),
        ("אֶל-מֹשֶׁה", "למוסי", "to Moses:"),
        ("קַח", "כ'ד'", "'Take"),
        ("אֶת-כָּל-רָאשֵׁי", "גמיע רויסא", "all the chiefs of"),
        ("הָעָם", "אלקום", "the people,"),
        ("וְהוֹקַע", "ואצלבהם", "and crucify them"),
        ("לַיהוָה", "ללה", "before God"),
        ("נֶגֶד הַשָּׁמֶשׁ", "חד'א אלשמס", "facing the sun —"),
        ("וְיָשֹׁב", "וירגע", "that the intensity of God's anger may turn away"),
        ("חֲרוֹן אַף-יְהוָה", "שדה' ג'צ'ב אללה", "from the house of"),
        ("מִיִּשְׂרָאֵל", "מן אל אסראיל", "Israel.'"),
    ],
    5: [
        # HE: וַיֹּאמֶר מֹשֶׁה אֶל-שֹׁפְטֵי יִשְׂרָאֵל הִרְגוּ אִישׁ אֲנָשָׁיו הַנִּצְמָדִים לְבַעַל פְּעוֹר
        # JA: פקאל מוסי' לחכאמהם. יקתל כל רגל מן פי נאחיתה. מן מלאזמי פעור אלצנם
        # EN: And Moses said to their judges: 'Let every man in his district kill whoever is attached to Pe'or the idol.'
        ("וַיֹּאמֶר", "פקאל", "And"),
        ("מֹשֶׁה", "מוסי'", "Moses said"),
        ("אֶל-שֹׁפְטֵי יִשְׂרָאֵל", "לחכאמהם", "to their judges:"),
        ("הִרְגוּ", "יקתל", "'Let every man in his district"),
        ("אִישׁ אֲנָשָׁיו", "כל רגל מן פי נאחיתה", "kill whoever"),
        ("הַנִּצְמָדִים", "מן מלאזמי", "is attached to"),
        ("לְבַעַל פְּעוֹר", "פעור", "Pe'or"),
        (None, "אלצנם", "the idol.'"),
    ],
    6: [
        # HE: וְהִנֵּה אִישׁ מִבְּנֵי יִשְׂרָאֵל בָּא וַיַּקְרֵב אֶל-אֶחָיו אֶת-הַמִּדְיָנִית לְעֵינֵי מֹשֶׁה וּלְעֵינֵי כָּל-עֲדַת בְּנֵי-יִשְׂרָאֵל וְהֵמָּה בֹכִים פֶּתַח אֹהֶל מוֹעֵד
        # JA: ואד'א ברגל מן בני אסראיל קד אקבל. וקדם אלי' מא בינהם אמראה מדיאנייה. בחצ'רה' מוסי' וגמאעתהם. והם יבכון. ענד באב כ'בא אלמחצ'ר
        # EN: And behold, a man from the sons of Israel had come forward, and brought among them a Midianite woman — in the presence of Moses and their whole assembly, who were weeping at the door of the tent of the convocation.
        ("וְהִנֵּה", "ואד'א", "And behold,"),
        ("אִישׁ מִבְּנֵי יִשְׂרָאֵל", "ברגל מן בני אסראיל", "a man from the sons of Israel"),
        ("בָּא", "קד אקבל", "had come forward,"),
        ("וַיַּקְרֵב", "וקדם", "and brought"),
        ("אֶל-אֶחָיו", "אלי' מא בינהם", "among them"),
        ("אֶת-הַמִּדְיָנִית", "אמראה מדיאנייה", "a Midianite woman —"),
        ("לְעֵינֵי מֹשֶׁה", "בחצ'רה' מוסי'", "in the presence of Moses"),
        ("וּלְעֵינֵי כָּל-עֲדַת בְּנֵי-יִשְׂרָאֵל", "וגמאעתהם", "and their whole assembly,"),
        ("וְהֵמָּה בֹכִים", "והם יבכון", "who were weeping"),
        ("פֶּתַח", "ענד באב", "at the door of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the convocation."),
    ],
    7: [
        # HE: וַיַּרְא פִּינְחָס בֶּן-אֶלְעָזָר בֶּן-אַהֲרֹן הַכֹּהֵן וַיָּקָם מִתּוֹךְ הָעֵדָה וַיִּקַּח רֹמַח בְּיָדוֹ
        # JA: פלמא ראא פינחס אבן אלעזר. אבן הרון אלאמאם. קאם מן וסט אלגמאעה. ואכ'ד' רמחא פי ידה
        # EN: And when Phinehas son of Eleazar son of Aaron the priest saw, he arose from the midst of the assembly, and took a spear in his hand.
        ("וַיַּרְא", "פלמא ראא", "And when"),
        ("פִּינְחָס", "פינחס", "Phinehas"),
        ("בֶּן-אֶלְעָזָר", "אבן אלעזר", "son of Eleazar"),
        ("בֶּן-אַהֲרֹן", "אבן הרון", "son of Aaron"),
        ("הַכֹּהֵן", "אלאמאם", "the priest saw,"),
        ("וַיָּקָם", "קאם", "he arose"),
        ("מִתּוֹךְ הָעֵדָה", "מן וסט אלגמאעה", "from the midst of the assembly,"),
        ("וַיִּקַּח", "ואכ'ד'", "and took"),
        ("רֹמַח", "רמחא", "a spear"),
        ("בְּיָדוֹ", "פי ידה", "in his hand."),
    ],
    8: [
        # HE: וַיָּבֹא אַחַר אִישׁ-יִשְׂרָאֵל אֶל-הַקֻּבָּה וַיִּדְקֹר אֶת-שְׁנֵיהֶם--אֵת אִישׁ יִשְׂרָאֵל וְאֶת-הָאִשָּׁה אֶל-קֳבָתָהּ וַתֵּעָצַר הַמַּגֵּפָה מֵעַל בְּנֵי יִשְׂרָאֵל
        # JA: פדכ'ל וראה אלי' אלקבה. וטענהמא גמיעא. אלרגל ואלאמראה פי בטנהא. ואנחבס אלובא. ען בני אסראיל
        # EN: And he went in after him into the chamber, and thrust both of them through — the man and the woman through her belly — and the pestilence was checked from the sons of Israel.
        ("וַיָּבֹא", "פדכ'ל", "And he went in"),
        ("אַחַר", "וראה", "after him"),
        ("אֶל-הַקֻּבָּה", "אלי' אלקבה", "into the chamber,"),
        ("וַיִּדְקֹר", "וטענהמא", "and thrust both of them"),
        ("אֶת-שְׁנֵיהֶם", "גמיעא", "through —"),
        ("אֵת אִישׁ יִשְׂרָאֵל", "אלרגל", "the man"),
        ("וְאֶת-הָאִשָּׁה", "ואלאמראה", "and the woman"),
        ("אֶל-קֳבָתָהּ", "פי בטנהא", "through her belly —"),
        ("וַתֵּעָצַר הַמַּגֵּפָה", "ואנחבס אלובא", "and the pestilence was checked"),
        ("מֵעַל בְּנֵי יִשְׂרָאֵל", "ען בני אסראיל", "from the sons of Israel."),
    ],
    9: [
        # HE: וַיִּהְיוּ הַמֵּתִים בַּמַּגֵּפָה--אַרְבָּעָה וְעֶשְׂרִים אָלֶף
        # JA: וכאן עדד מן מאת בד'אלך אלובא. ארבעה ועשרין אלפא
        # EN: And the number of those who died in that pestilence was twenty-four thousand.
        ("וַיִּהְיוּ", "וכאן", "And the number of"),
        ("הַמֵּתִים", "עדד מן מאת", "those who died"),
        ("בַּמַּגֵּפָה", "בד'אלך אלובא", "in that pestilence"),
        (None, "ארבעה", "was twenty-four"),
        ("אַרְבָּעָה וְעֶשְׂרִים אָלֶף", "ועשרין אלפא", "thousand."),
    ],
    10: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה . מוסי' תכלימא
        # EN: Then God spoke to Moses, saying:
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God"),
        ("יְהוָה", "אללה", "spoke"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses,"),
        ("לֵּאמֹר", "תכלימא", "saying:"),
    ],
    11: [
        # HE: פִּינְחָס בֶּן-אֶלְעָזָר בֶּן-אַהֲרֹן הַכֹּהֵן הֵשִׁיב אֶת-חֲמָתִי מֵעַל בְּנֵי-יִשְׂרָאֵל בְּקַנְאוֹ אֶת-קִנְאָתִי בְּתוֹכָם וְלֹא-כִלִּיתִי אֶת-בְּנֵי-יִשְׂרָאֵל בְּקִנְאָתִי
        # JA: אן פנחס אבן אלעזר אבן הרון אלאמאם. רד חמייתי ען בני אסראיל. במא ג'אר לי פי מא בינהם. חתי' לא אפניהם בעקאבי
        # EN: 'Phinehas son of Eleazar son of Aaron the priest has turned back My wrath from the sons of Israel, in that he was zealous for My sake among them, so that I did not destroy them with My punishment.
        (None, "אן", "'"),
        ("פִּינְחָס", "פנחס", "Phinehas"),
        ("בֶּן-אֶלְעָזָר", "אבן אלעזר", "son of Eleazar"),
        ("בֶּן-אַהֲרֹן", "אבן הרון", "son of Aaron"),
        ("הַכֹּהֵן", "אלאמאם", "the priest"),
        ("הֵשִׁיב", "רד", "has turned back"),
        ("אֶת-חֲמָתִי", "חמייתי", "My wrath"),
        ("מֵעַל בְּנֵי-יִשְׂרָאֵל", "ען בני אסראיל", "from the sons of Israel,"),
        ("בְּקַנְאוֹ אֶת-קִנְאָתִי", "במא ג'אר לי", "in that he was zealous for My sake"),
        ("בְּתוֹכָם", "פי מא בינהם", "among them,"),
        ("וְלֹא-כִלִּיתִי", "חתי' לא אפניהם", "so that I did not destroy them"),
        ("בְּקִנְאָתִי", "בעקאבי", "with My punishment."),
    ],
    12: [
        # HE: לָכֵן אֱמֹר הִנְנִי נֹתֵן לוֹ אֶת-בְּרִיתִי שָׁלוֹם
        # JA: לד'אלך קל לה. האנא מעטיה עהדי סלאמא
        # EN: Therefore say to him: Behold, I am giving him My covenant of peace.
        ("לָכֵן", "לד'אלך", "Therefore"),
        ("אֱמֹר", "קל", "say"),
        (None, "לה", "to him:"),
        ("הִנְנִי", "האנא", "Behold,"),
        ("נֹתֵן לוֹ", "מעטיה", "I am giving him"),
        ("אֶת-בְּרִיתִי", "עהדי", "My covenant of"),
        ("שָׁלוֹם", "סלאמא", "peace."),
    ],
    13: [
        # HE: וְהָיְתָה לּוֹ וּלְזַרְעוֹ אַחֲרָיו בְּרִית כְּהֻנַּת עוֹלָם--תַּחַת אֲשֶׁר קִנֵּא לֵאלֹהָיו וַיְכַפֵּר עַל-בְּנֵי יִשְׂרָאֵל
        # JA: ותכון לה ולנסלה בעדה. עהד אמאמה' אלדהר. בדל מא ג'אר לרבה. וכפר ען בני אסראיל
        # EN: And it shall be for him and for his offspring after him a covenant of everlasting priesthood — in recompense for his zeal for his Lord, whereby he made atonement for the sons of Israel.'
        ("וְהָיְתָה", "ותכון", "And it shall be"),
        ("לּוֹ", "לה", "for him"),
        ("וּלְזַרְעוֹ", "ולנסלה", "and for his offspring"),
        ("אַחֲרָיו", "בעדה", "after him"),
        ("בְּרִית כְּהֻנַּת", "עהד אמאמה'", "a covenant of everlasting"),
        ("עוֹלָם", "אלדהר", "priesthood —"),
        ("תַּחַת אֲשֶׁר", "בדל מא", "in recompense for"),
        ("קִנֵּא", "ג'אר", "his zeal"),
        ("לֵאלֹהָיו", "לרבה", "for his Lord,"),
        ("וַיְכַפֵּר", "וכפר", "whereby he made atonement"),
        ("עַל-בְּנֵי יִשְׂרָאֵל", "ען בני אסראיל", "for the sons of Israel.'"),
    ],
    14: [
        # HE: וְשֵׁם אִישׁ יִשְׂרָאֵל הַמֻּכֶּה אֲשֶׁר הֻכָּה אֶת-הַמִּדְיָנִית--זִמְרִי בֶּן-סָלוּא נְשִׂיא בֵית-אָב לַשִּׁמְעֹנִי
        # JA: וכאן אסם אלרגל אלאסראילי אלמקתול. אלד'י קתל מע אלמדיאנייה. זמרי אבן סלוא. שריף בית אביה אלשמעוני
        # EN: And the name of the Israelite man who was slain, who was killed with the Midianite woman, was Zimri son of Salu, a noble of his father's house among the Simeonites.
        ("וְשֵׁם", "וכאן אסם", "And the name of"),
        ("אִישׁ יִשְׂרָאֵל", "אלרגל אלאסראילי", "the Israelite man"),
        ("הַמֻּכֶּה", "אלמקתול", "who was slain,"),
        ("אֲשֶׁר הֻכָּה", "אלד'י קתל", "who was killed"),
        ("אֶת-הַמִּדְיָנִית", "מע אלמדיאנייה", "with the Midianite woman,"),
        (None, "זמרי", "was Zimri"),
        ("זִמְרִי בֶּן-סָלוּא", "אבן סלוא", "son of Salu,"),
        ("נְשִׂיא", "שריף", "a noble of"),
        ("בֵית-אָב", "בית אביה", "his father's house"),
        ("לַשִּׁמְעֹנִי", "אלשמעוני", "among the Simeonites."),
    ],
    15: [
        # HE: וְשֵׁם הָאִשָּׁה הַמֻּכָּה הַמִּדְיָנִית כָּזְבִּי בַת-צוּר רֹאשׁ אֻמּוֹת בֵּית-אָב בְּמִדְיָן הוּא
        # JA: ואסם אלאמראה אלמקתולה. אלמדיאנייה כזבי אבנה' צור. והו רייס אהל בית אמתה במדין
        # EN: And the name of the slain Midianite woman was Cozbi daughter of Zur — he being the head of the people of his nation's household in Midian.
        ("וְשֵׁם", "ואסם", "And the name of"),
        ("הָאִשָּׁה הַמֻּכָּה", "אלאמראה אלמקתולה", "the slain"),
        ("הַמִּדְיָנִית", "אלמדיאנייה", "Midianite woman"),
        ("כָּזְבִּי", "כזבי", "was Cozbi"),
        ("בַת-צוּר", "אבנה' צור", "daughter of Zur —"),
        ("הוּא", "והו", "he being"),
        ("רֹאשׁ אֻמּוֹת", "רייס אהל", "the head of the people of"),
        ("בֵּית-אָב", "בית אמתה", "his nation's household"),
        ("בְּמִדְיָן", "במדין", "in Midian."),
    ],
    16: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses, saying:
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God"),
        ("יְהוָה", "אללה", "spoke"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses,"),
        ("לֵּאמֹר", "תכלימא", "saying:"),
    ],
    17: [
        # HE: צָרוֹר אֶת-הַמִּדְיָנִים וְהִכִּיתֶם אוֹתָם
        # JA: חאצר אלמדיאניין. חתי תקתלהם
        # EN: 'Besiege the Midianites until you have killed them —
        ("צָרוֹר", "חאצר", "'Besiege"),
        ("אֶת-הַמִּדְיָנִים", "אלמדיאניין", "the Midianites"),
        ("וְהִכִּיתֶם אוֹתָם", "חתי תקתלהם", "until you have killed them —"),
    ],
    18: [
        # HE: כִּי צֹרְרִים הֵם לָכֶם בְּנִכְלֵיהֶם אֲשֶׁר-נִכְּלוּ לָכֶם עַל-דְּבַר-פְּעוֹר וְעַל-דְּבַר כָּזְבִּי בַת-נְשִׂיא מִדְיָן אֲחֹתָם הַמֻּכָּה בְיוֹם-הַמַּגֵּפָה עַל-דְּבַר-פְּעוֹר
        # JA: לאנהם אעדא לכם. באג'תיאלהם. אלד'י אג'תאלוכם בסבב פעור. ובסבב כזבי אבנה' שריף מדין אכ'תהם. אלמקתולה פי יום אלובא בסבב פעור
        # EN: for they are enemies to you, through their treachery with which they have treacherously dealt against you by reason of Pe'or, and by reason of Cozbi daughter of the noble of Midian their kinswoman, who was slain on the day of the pestilence on account of Pe'or.'
        ("כִּי", "לאנהם", "for they are enemies"),
        ("צֹרְרִים הֵם", "אעדא", "to you,"),
        ("לָכֶם", "לכם", "through their treachery"),
        ("בְּנִכְלֵיהֶם", "באג'תיאלהם", "with which they have treacherously dealt against you"),
        ("אֲשֶׁר-נִכְּלוּ לָכֶם", "אלד'י אג'תאלוכם", "by reason of Pe'or,"),
        ("עַל-דְּבַר-פְּעוֹר", "בסבב פעור", "and by reason of"),
        ("וְעַל-דְּבַר", "ובסבב", "Cozbi"),
        ("כָּזְבִּי", "כזבי", "daughter of the noble of Midian"),
        ("בַת-נְשִׂיא מִדְיָן", "אבנה' שריף מדין", "their kinswoman,"),
        ("אֲחֹתָם", "אכ'תהם", "who was slain"),
        ("הַמֻּכָּה", "אלמקתולה", "on the day of"),
        ("בְיוֹם-הַמַּגֵּפָה", "פי יום אלובא", "the pestilence"),
        ("עַל-דְּבַר-פְּעוֹר", "בסבב פעור", "on account of Pe'or.'"),
    ],
}

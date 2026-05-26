"""Hand-authored word-level alignment triples for Bamidbar chapter 23."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיֹּאמֶר בִּלְעָם אֶל-בָּלָק בְּנֵה-לִי בָזֶה שִׁבְעָה מִזְבְּחֹת וְהָכֵן לִי בָּזֶה שִׁבְעָה פָרִים וְשִׁבְעָה אֵילִים
        # JA: פקאל לה. אבן לי ההנא סבעה מד'אבחא. ואעד לי ההנא. סבעה רת'ות' וסבעה כבאש
        # EN: And he said to him: 'Build me here seven altars, and prepare for me here seven bulls and seven rams.'
        ("וַיֹּאמֶר", "פקאל", "And he said"),
        ("בִּלְעָם", "לה", "to him:"),
        ("בְּנֵה-לִי", "אבן לי", "'Build me"),
        ("בָזֶה", "ההנא", "here"),
        ("שִׁבְעָה", "סבעה", "seven"),
        ("מִזְבְּחֹת", "מד'אבחא", "altars,"),
        ("וְהָכֵן לִי", "ואעד לי", "and prepare for me"),
        (None, "ההנא", "here"),
        ("שִׁבְעָה פָרִים", "סבעה רת'ות'", "seven bulls"),
        ("וְשִׁבְעָה אֵילִים", "וסבעה כבאש", "and seven rams.'"),
    ],
    2: [
        # HE: וַיַּעַשׂ בָּלָק כַּאֲשֶׁר דִּבֶּר בִּלְעָם וַיַּעַל בָּלָק וּבִלְעָם פָּר וָאַיִל בַּמִּזְבֵּחַ
        # JA: פצנע ד'אלך. וקרבא. ת'ורא וכבשא עלי' כל מד'בח
        # EN: And he did so; and the two of them offered there a bull and a ram upon each altar.
        ("וַיַּעַשׂ בָּלָק", "פצנע", "And he did"),
        ("כַּאֲשֶׁר דִּבֶּר בִּלְעָם", "ד'אלך", "so;"),
        ("וַיַּעַל בָּלָק וּבִלְעָם", "וקרבא", "and the two of them offered there"),
        ("פָּר", "ת'ורא", "a bull"),
        ("וָאַיִל", "וכבשא", "and a ram"),
        ("בַּמִּזְבֵּחַ", "עלי' כל מד'בח", "upon each altar."),
    ],
    3: [
        # HE: וַיֹּאמֶר בִּלְעָם לְבָלָק הִתְיַצֵּב עַל-עֹלָתֶךָ וְאֵלְכָה אוּלַי יִקָּרֵה יְהוָה לִקְרָאתִי וּדְבַר מַה-יַּרְאֵנִי וְהִגַּדְתִּי לָךְ וַיֵּלֶךְ שֶׁפִי
        # JA: ת'ם קאל לה. קף ענד קרבאנך. ואמצ'י אנא. פלעל יואפיני אמר אללה. ואי קול לקנניה אכ'ברתך בה. פמצ'א פי הדו
        # EN: Then he said to him: 'Stand by your offering, while I go on — perhaps the decree of God will come to meet me; and whatever word God instructs me with, I will tell you of it.' And he went in stillness.
        (None, "ת'ם", "Then"),
        ("וַיֹּאמֶר", "קאל", "he said"),
        ("בִּלְעָם לְבָלָק", "לה", "to him:"),
        ("הִתְיַצֵּב", "קף", "'Stand"),
        ("עַל-עֹלָתֶךָ", "ענד קרבאנך", "by your offering,"),
        ("וְאֵלְכָה", "ואמצ'י אנא", "while I go on —"),
        ("אוּלַי", "פלעל", "perhaps"),
        ("יִקָּרֵה יְהוָה", "יואפיני אמר אללה", "the decree of God will come to meet me;"),
        ("וּדְבַר מַה-יַּרְאֵנִי", "ואי קול לקנניה", "and whatever word God instructs me with,"),
        ("וְהִגַּדְתִּי לָךְ", "אכ'ברתך בה", "I will tell you of it.'"),
        ("וַיֵּלֶךְ", "פמצ'א", "And he went"),
        ("שֶׁפִי", "פי הדו", "in stillness."),
    ],
    4: [
        # HE: וַיִּקָּר אֱלֹהִים אֶל-בִּלְעָם וַיֹּאמֶר אֵלָיו אֶת-שִׁבְעַת הַמִּזְבְּחֹת עָרַכְתִּי וָאַעַל פָּר וָאַיִל בַּמִּזְבֵּחַ
        # JA: פואפא אמר אללה בלעם. וקאל יא רב. אני קד נצ'דת סבעה מד'אבח. וקרבת ת'ורא וכבשא עלי' כל מד'בח
        # EN: And the decree of God came to Balaam; and he said: 'O Lord! I have already arranged seven altars, and offered there a bull and a ram upon each altar.'
        ("וַיִּקָּר אֱלֹהִים", "פואפא אמר אללה", "And the decree of God came"),
        ("אֶל-בִּלְעָם", "בלעם", "to Balaam;"),
        ("וַיֹּאמֶר אֵלָיו", "וקאל יא רב", "and he said: 'O Lord!"),
        ("אֶת-שִׁבְעַת הַמִּזְבְּחֹת", "אני קד נצ'דת סבעה מד'אבח", "I have already arranged seven altars,"),
        ("עָרַכְתִּי וָאַעַל", "וקרבת", "and offered there"),
        ("פָּר", "ת'ורא", "a bull"),
        ("וָאַיִל", "וכבשא", "and a ram"),
        ("בַּמִּזְבֵּחַ", "עלי' כל מד'בח", "upon each altar.'"),
    ],
    5: [
        # HE: וַיָּשֶׂם יְהוָה דָּבָר בְּפִי בִלְעָם וַיֹּאמֶר שׁוּב אֶל-בָּלָק וְכֹה תְדַבֵּר
        # JA: פלקנה אללה כלאמא. וקאל. ארגע אלי' בלק וקל כד'א
        # EN: Then God instructed him with a word, and said: 'Return to Balak and speak thus.'
        ("וַיָּשֶׂם יְהוָה", "פלקנה אללה", "Then God instructed him"),
        ("דָּבָר בְּפִי בִלְעָם", "כלאמא", "with a word,"),
        ("וַיֹּאמֶר", "וקאל", "and said:"),
        ("שׁוּב", "ארגע", "'Return"),
        ("אֶל-בָּלָק", "אלי' בלק", "to Balak"),
        ("וְכֹה תְדַבֵּר", "וקל כד'א", "and speak thus.'"),
    ],
    6: [
        # HE: וַיָּשָׁב אֵלָיו וְהִנֵּה נִצָּב עַל-עֹלָתוֹ--הוּא וְכָל-שָׂרֵי מוֹאָב
        # JA: פרגע אלי'ה. פאד'א בה ואקף ענד קרבאנה. הו וגמיע רויסא מואב
        # EN: So he returned to him — and behold, he was standing by his offering, he and all the chiefs of Moab.
        ("וַיָּשָׁב", "פרגע", "So he returned"),
        ("אֵלָיו", "אלי'ה", "to him —"),
        ("וְהִנֵּה", "פאד'א בה", "and behold,"),
        ("נִצָּב", "ואקף", "he was standing"),
        ("עַל-עֹלָתוֹ", "ענד קרבאנה", "by his offering,"),
        ("הוּא", "הו", "he"),
        ("וְכָל-שָׂרֵי", "וגמיע רויסא", "and all the chiefs of"),
        ("מוֹאָב", "מואב", "Moab."),
    ],
    7: [
        # HE: וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר מִן-אֲרָם יַנְחֵנִי בָלָק מֶלֶךְ-מוֹאָב מֵהַרְרֵי-קֶדֶם--לְכָה אָרָה-לִּי יַעֲקֹב וּלְכָה זֹעֲמָה יִשְׂרָאֵל
        # JA: פצ'רב מת'לה וקאל. מן ארם. סיירני בלק מלך מואב מן גבאל אלמשרק קאילא. תעאל אלען לי אל יעקוב. וד'ם אל אסראיל
        # EN: And he spoke his parable and said: 'From Aram, Balak king of Moab brought me, from the mountains of the east, saying: Come, curse for me the house of Jacob, and bring reproach upon the house of Israel.'
        ("וַיִּשָּׂא מְשָׁלוֹ", "פצ'רב מת'לה", "And he spoke his parable"),
        ("וַיֹּאמַר", "וקאל", "and said:"),
        ("מִן-אֲרָם", "מן ארם", "'From Aram,"),
        ("יַנְחֵנִי", "סיירני", "brought me,"),
        ("בָלָק", "בלק", "Balak"),
        ("מֶלֶךְ-מוֹאָב", "מלך מואב", "king of Moab"),
        ("מֵהַרְרֵי-קֶדֶם", "מן גבאל אלמשרק", "from the mountains of the east,"),
        ("לְכָה אָרָה-לִּי", "קאילא. תעאל אלען לי", "saying: Come, curse for me"),
        ("יַעֲקֹב", "אל יעקוב", "the house of Jacob,"),
        ("וּלְכָה זֹעֲמָה", "וד'ם", "and bring reproach upon"),
        ("יִשְׂרָאֵל", "אל אסראיל", "the house of Israel.'"),
    ],
    8: [
        # HE: מָה אֶקֹּב לֹא קַבֹּה אֵל וּמָה אֶזְעֹם לֹא זָעַם יְהוָה
        # JA: מא אסב. מן לם יסבה אלטאיק. ומא אד'ם. מן לם יד'מה אללה
        # EN: 'How shall I curse him whom the All-Powerful has not cursed? And how shall I reproach him whom God has not reproached?'
        ("מָה אֶקֹּב", "מא אסב", "'How shall I curse him"),
        ("לֹא קַבֹּה", "מן לם יסבה", "whom"),
        ("אֵל", "אלטאיק", "the All-Powerful has not cursed?"),
        ("וּמָה אֶזְעֹם", "ומא אד'ם", "And how shall I reproach him"),
        ("לֹא זָעַם", "מן לם יד'מה", "whom"),
        ("יְהוָה", "אללה", "God has not reproached?'"),
    ],
    9: [
        # HE: כִּי-מֵרֹאשׁ צֻרִים אֶרְאֶנּוּ וּמִגְּבָעוֹת אֲשׁוּרֶנּוּ הֶן-עָם לְבָדָד יִשְׁכֹּן וּבַגּוֹיִם לֹא יִתְחַשָּׁב
        # JA: ואנא אראה מן רוס אלגבאל. ואלמחה מן אליפאע. אנה שעב סיסכן פרדא. ולא יחסב מע סאיר אלאמם
        # EN: 'For I see him from the tops of the mountains, and I discern him from the heights — that he is a people who shall dwell alone, and shall not be reckoned among the rest of the nations.'
        ("כִּי-מֵרֹאשׁ", "ואנא אראה", "'For I see him"),
        ("צֻרִים אֶרְאֶנּוּ", "מן רוס אלגבאל", "from the tops of the mountains,"),
        ("וּמִגְּבָעוֹת", "ואלמחה", "and I discern him"),
        ("אֲשׁוּרֶנּוּ", "מן אליפאע", "from the heights —"),
        ("הֶן-עָם", "אנה שעב", "that he is a people"),
        ("לְבָדָד יִשְׁכֹּן", "סיסכן פרדא", "who shall dwell alone,"),
        ("וּבַגּוֹיִם", "ולא יחסב מע", "and shall not be reckoned among"),
        ("לֹא יִתְחַשָּׁב", "סאיר אלאמם", "the rest of the nations.'"),
    ],
    10: [
        # HE: מִי מָנָה עֲפַר יַעֲקֹב וּמִסְפָּר אֶת-רֹבַע יִשְׂרָאֵל תָּמֹת נַפְשִׁי מוֹת יְשָׁרִים וּתְהִי אַחֲרִיתִי כָּמֹהוּ
        # JA: יא מן יעד נסל יעקוב. ויחצי ד'רייה' אל אסראיל אסאלך אן אמות מות אלמסתקימין. ותכון אכ'רתי מת'להם
        # EN: 'O who can count the offspring of Jacob, and number the descendants of the house of Israel! I ask that I may die the death of the upright, and that my end may be like theirs.'
        ("מִי מָנָה", "יא מן יעד", "'O who can count"),
        ("עֲפַר יַעֲקֹב", "נסל יעקוב", "the offspring of Jacob,"),
        ("וּמִסְפָּר", "ויחצי", "and number"),
        ("אֶת-רֹבַע יִשְׂרָאֵל", "ד'רייה' אל אסראיל", "the descendants of the house of Israel!"),
        ("תָּמֹת נַפְשִׁי", "אסאלך אן אמות", "I ask that I may die"),
        ("מוֹת יְשָׁרִים", "מות אלמסתקימין", "the death of the upright,"),
        ("וּתְהִי אַחֲרִיתִי", "ותכון אכ'רתי", "and that my end may be"),
        ("כָּמֹהוּ", "מת'להם", "like theirs.'"),
    ],
    11: [
        # HE: וַיֹּאמֶר בָּלָק אֶל-בִּלְעָם מֶה עָשִׂיתָ לִי לָקֹב אֹיְבַי לְקַחְתִּיךָ וְהִנֵּה בֵּרַכְתָּ בָרֵךְ
        # JA: קאל בלק לבלעם. מא ד'א צנעת בי. דעותך לתסב אעדאי. פאדא בך תבארך פיהם
        # EN: Balak said to Balaam: 'What have you done to me? I invited you to curse my enemies — and behold, you have blessed them!'
        ("וַיֹּאמֶר בָּלָק", "קאל בלק", "Balak said"),
        ("אֶל-בִּלְעָם", "לבלעם", "to Balaam:"),
        ("מֶה עָשִׂיתָ לִי", "מא ד'א צנעת בי", "'What have you done to me?"),
        ("לָקֹב אֹיְבַי", "דעותך לתסב אעדאי", "I invited you to curse my enemies —"),
        ("וְהִנֵּה", "פאדא בך", "and behold,"),
        ("בֵּרַכְתָּ בָרֵךְ", "תבארך פיהם", "you have blessed them!'"),
    ],
    12: [
        # HE: וַיַּעַן וַיֹּאמַר הֲלֹא אֵת אֲשֶׁר יָשִׂים יְהוָה בְּפִי--אֹתוֹ אֶשְׁמֹר לְדַבֵּר
        # JA: פאגאבה קאילא. אלא אן מא ילקנניה אללה אחפצה ואקולה
        # EN: He answered, saying: 'Only that which God instructs me with — that I preserve and speak.'
        ("וַיַּעַן", "פאגאבה", "He answered,"),
        ("וַיֹּאמַר", "קאילא", "saying:"),
        ("הֲלֹא", "אלא אן", "'Only"),
        ("אֲשֶׁר יָשִׂים", "מא ילקנניה", "that which"),
        ("יְהוָה", "אללה", "God instructs me with —"),
        ("אֹתוֹ אֶשְׁמֹר לְדַבֵּר", "אחפצה ואקולה", "that I preserve and speak.'"),
    ],
    13: [
        # HE: וַיֹּאמֶר אֵלָיו בָּלָק לְךָ-נָּא אִתִּי אֶל-מָקוֹם אַחֵר אֲשֶׁר תִּרְאֶנּוּ מִשָּׁם--אֶפֶס קָצֵהוּ תִרְאֶה וְכֻלּוֹ לֹא תִרְאֶה וְקָבְנוֹ-לִי מִשָּׁם
        # JA: קאל לה בלק. תעאל מעי. אלי' מוצ'ע אכ'ר תנצ'רה מן ת'ם. לכנך תנצ'ר בעצ'ה ולא כלה. פתסבה לי מן ת'ם
        # EN: Balak said to him: 'Come with me to another place, from which you will see him — yet you will see part of him and not all of him — and curse him for me from there.'
        ("וַיֹּאמֶר אֵלָיו בָּלָק", "קאל לה בלק", "Balak said to him:"),
        ("לְךָ-נָּא אִתִּי", "תעאל מעי", "'Come with me"),
        ("אֶל-מָקוֹם אַחֵר", "אלי' מוצ'ע אכ'ר", "to another place,"),
        ("אֲשֶׁר תִּרְאֶנּוּ מִשָּׁם", "תנצ'רה מן ת'ם", "from which you will see him —"),
        ("אֶפֶס קָצֵהוּ תִרְאֶה", "לכנך תנצ'ר בעצ'ה", "yet you will see part of him"),
        ("וְכֻלּוֹ לֹא תִרְאֶה", "ולא כלה", "and not all of him —"),
        ("וְקָבְנוֹ-לִי", "פתסבה לי", "and curse him for me"),
        ("מִשָּׁם", "מן ת'ם", "from there.'"),
    ],
    14: [
        # HE: וַיִּקָּחֵהוּ שְׂדֵה צֹפִים אֶל-רֹאשׁ הַפִּסְגָּה וַיִּבֶן שִׁבְעָה מִזְבְּחֹת וַיַּעַל פָּר וָאַיִל בַּמִּזְבֵּחַ
        # JA: פאכ'ד' אלי' אלצ'יעה. אלמשרפה אלי' ראס אלקלעה. פבנא הנאך סבעה מד'אבח. וקרב ת'ורא וכבשא עלי' כל מד'בח
        # EN: And he took him to the estate overlooking the top of the citadel; and he built there seven altars, and offered there a bull and a ram upon each altar.
        ("וַיִּקָּחֵהוּ", "פאכ'ד'", "And he took him"),
        ("שְׂדֵה צֹפִים", "אלי' אלצ'יעה", "to the estate"),
        ("אֶל-רֹאשׁ", "אלמשרפה אלי' ראס", "overlooking the top of"),
        ("הַפִּסְגָּה", "אלקלעה", "the citadel;"),
        ("וַיִּבֶן", "פבנא הנאך", "and he built there"),
        ("שִׁבְעָה מִזְבְּחֹת", "סבעה מד'אבח", "seven altars,"),
        ("וַיַּעַל", "וקרב", "and offered there"),
        ("פָּר", "ת'ורא", "a bull"),
        ("וָאַיִל", "וכבשא", "and a ram"),
        ("בַּמִּזְבֵּחַ", "עלי' כל מד'בח", "upon each altar."),
    ],
    15: [
        # HE: וַיֹּאמֶר אֶל-בָּלָק הִתְיַצֵּב כֹּה עַל-עֹלָתֶךָ וְאָנֹכִי אִקָּרֶה כֹּה
        # JA: קאל לבלק. קף ההנא ענד קראבינך. ואנא אתלקא אלי' ההנא
        # EN: He said to Balak: 'Stand here by your offering, while I go to receive over there.'
        ("וַיֹּאמֶר", "קאל", "He said"),
        ("אֶל-בָּלָק", "לבלק", "to Balak:"),
        ("הִתְיַצֵּב", "קף", "'Stand"),
        ("כֹּה", "ההנא", "here"),
        ("עַל-עֹלָתֶךָ", "ענד קראבינך", "by your offering,"),
        ("וְאָנֹכִי", "ואנא", "while I"),
        ("אִקָּרֶה", "אתלקא", "go to receive"),
        ("כֹּה", "אלי' ההנא", "over there.'"),
    ],
    16: [
        # HE: וַיִּקָּר יְהוָה אֶל-בִּלְעָם וַיָּשֶׂם דָּבָר בְּפִיו וַיֹּאמֶר שׁוּב אֶל-בָּלָק וְכֹה תְדַבֵּר
        # JA: פואפא אמר אללה בלעם. פלקנה כלאמא. וקאל ארג'ע לבלק וקל כד'א
        # EN: And the decree of God came to Balaam; and He instructed him with a word, and said: 'Return to Balak and speak thus.'
        ("וַיִּקָּר יְהוָה", "פואפא אמר אללה", "And the decree of God came"),
        ("אֶל-בִּלְעָם", "בלעם", "to Balaam;"),
        ("וַיָּשֶׂם דָּבָר בְּפִיו", "פלקנה כלאמא", "and He instructed him with a word,"),
        ("וַיֹּאמֶר", "וקאל", "and said:"),
        ("שׁוּב", "ארג'ע", "'Return"),
        ("אֶל-בָּלָק", "לבלק", "to Balak"),
        ("וְכֹה תְדַבֵּר", "וקל כד'א", "and speak thus.'"),
    ],
    17: [
        # HE: וַיָּבֹא אֵלָיו וְהִנּוֹ נִצָּב עַל-עֹלָתוֹ וְשָׂרֵי מוֹאָב אִתּוֹ וַיֹּאמֶר לוֹ בָּלָק מַה-דִּבֶּר יְהוָה
        # JA: פגא אליה. ואד'אה ואקף ענד קרבאנה. ורויסא מואב מעה. קאל לה מא ד'א קאל אללה
        # EN: So he came to him — and behold, he was standing by his offering, and the chiefs of Moab with him. And he said to him: 'What has God said?'
        ("וַיָּבֹא", "פגא", "So he came"),
        ("אֵלָיו", "אליה", "to him —"),
        ("וְהִנּוֹ", "ואד'אה", "and behold,"),
        ("נִצָּב", "ואקף", "he was standing"),
        ("עַל-עֹלָתוֹ", "ענד קרבאנה", "by his offering,"),
        ("וְשָׂרֵי מוֹאָב", "ורויסא מואב", "and the chiefs of Moab"),
        ("אִתּוֹ", "מעה", "with him."),
        ("וַיֹּאמֶר לוֹ בָּלָק", "קאל לה", "And he said to him:"),
        ("מַה-דִּבֶּר יְהוָה", "מא ד'א קאל אללה", "'What has God said?'"),
    ],
    18: [
        # HE: וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר קוּם בָּלָק וּשְׁמָע הַאֲזִינָה עָדַי בְּנוֹ צִפֹּר
        # JA: פצ'רב מת'לה וקאל. קום יא בלק ואסמע. ואנצת לקולי יא אבן צפור
        # EN: And he spoke his parable and said: 'Arise, O Balak, and hear! Give ear to my words, O son of Zippor!'
        ("וַיִּשָּׂא מְשָׁלוֹ", "פצ'רב מת'לה", "And he spoke his parable"),
        ("וַיֹּאמַר", "וקאל", "and said:"),
        ("קוּם", "קום", "'Arise,"),
        ("בָּלָק", "יא בלק", "O Balak,"),
        ("וּשְׁמָע", "ואסמע", "and hear!"),
        ("הַאֲזִינָה עָדַי", "ואנצת לקולי", "Give ear to my words,"),
        ("בְּנוֹ צִפֹּר", "יא אבן צפור", "O son of Zippor!'"),
    ],
    19: [
        # HE: לֹא אִישׁ אֵל וִיכַזֵּב וּבֶן-אָדָם וְיִתְנֶחָם הַהוּא אָמַר וְלֹא יַעֲשֶׂה וְדִבֶּר וְלֹא יְקִימֶנָּה
        # JA: ליס אלטאיק כאלנאס פיכד'ב. ולא כבני אדם פינדם. אתראה יקול ולא יפעל. או יתכלם ולא יקום בה
        # EN: 'The All-Powerful is not like men that He should lie, nor like the sons of Adam that He should repent. Do you think He would say and not act, or speak and not fulfill it?'
        ("לֹא אִישׁ אֵל", "ליס אלטאיק", "'The All-Powerful is not"),
        ("וִיכַזֵּב", "כאלנאס פיכד'ב", "like men that He should lie,"),
        ("וּבֶן-אָדָם", "ולא כבני אדם", "nor like the sons of Adam"),
        ("וְיִתְנֶחָם", "פינדם", "that He should repent."),
        ("הַהוּא אָמַר", "אתראה יקול", "Do you think He would say"),
        ("וְלֹא יַעֲשֶׂה", "ולא יפעל", "and not act,"),
        ("וְדִבֶּר", "או יתכלם", "or speak"),
        ("וְלֹא יְקִימֶנָּה", "ולא יקום בה", "and not fulfill it?'"),
    ],
    20: [
        # HE: הִנֵּה בָרֵךְ לָקָחְתִּי וּבֵרֵךְ וְלֹא אֲשִׁיבֶנָּה
        # JA: אלא אן ברכאת קבלתהא. פאבארך פיהם ולא ארדהא
        # EN: 'Indeed, blessings I have received — and so I bless them, and I shall not reverse it.'
        ("הִנֵּה", "אלא אן", "'Indeed,"),
        ("בָרֵךְ לָקָחְתִּי", "ברכאת קבלתהא", "blessings I have received —"),
        ("וּבֵרֵךְ", "פאבארך פיהם", "and so I bless them,"),
        ("וְלֹא אֲשִׁיבֶנָּה", "ולא ארדהא", "and I shall not reverse it.'"),
    ],
    21: [
        # HE: לֹא-הִבִּיט אָוֶן בְּיַעֲקֹב וְלֹא-רָאָה עָמָל בְּיִשְׂרָאֵל יְהוָה אֱלֹהָיו עִמּוֹ וּתְרוּעַת מֶלֶךְ בּוֹ
        # JA: ממא לא יבצר ג'לא פי אל יעקוב. ולא דג'לא פי אל אסראיל. פאללה רבהם מעהם. וצחאבה' אלמלך להם
        # EN: 'Whereby no iniquity is seen in the house of Jacob, nor deceit in the house of Israel — for God is their Lord with them, and the companionship of the King is theirs.'
        ("לֹא-הִבִּיט אָוֶן", "ממא לא יבצר ג'לא", "'Whereby no iniquity is seen"),
        ("בְּיַעֲקֹב", "פי אל יעקוב", "in the house of Jacob,"),
        ("וְלֹא-רָאָה עָמָל", "ולא דג'לא", "nor deceit"),
        ("בְּיִשְׂרָאֵל", "פי אל אסראיל", "in the house of Israel —"),
        ("יְהוָה אֱלֹהָיו", "פאללה רבהם", "for God is their Lord"),
        ("עִמּוֹ", "מעהם", "with them,"),
        ("וּתְרוּעַת מֶלֶךְ", "וצחאבה' אלמלך", "and the companionship of the King"),
        ("בּוֹ", "להם", "is theirs.'"),
    ],
    22: [
        # HE: אֵל מוֹצִיאָם מִמִּצְרָיִם--כְּתוֹעֲפֹת רְאֵם לוֹ
        # JA: אלטאיק אלמכ'רגהם מן מצר. כארק אלרים מאנע ענהם
        # EN: 'The All-Powerful who brought them out of Egypt — like the vigilance of the wild ox, prevailing over them.'
        ("אֵל", "אלטאיק", "'The All-Powerful"),
        ("מוֹצִיאָם", "אלמכ'רגהם", "who brought them out"),
        ("מִמִּצְרָיִם", "מן מצר", "of Egypt —"),
        ("כְּתוֹעֲפֹת", "כארק", "like the vigilance of"),
        ("רְאֵם לוֹ", "אלרים מאנע ענהם", "the wild ox, prevailing over them.'"),
    ],
    23: [
        # HE: כִּי לֹא-נַחַשׁ בְּיַעֲקֹב וְלֹא-קֶסֶם בְּיִשְׂרָאֵל כָּעֵת יֵאָמֵר לְיַעֲקֹב וּלְיִשְׂרָאֵל מַה-פָּעַל אֵל
        # JA: ולא טיירה תחיך פי אל יעקוב. ולא קאסומה ת'וות'ר פי אל אסראיל. ואנמא יקאל להם. מא צנע אלטאיק פקט
        # EN: 'And no omen can take hold in the house of Jacob, nor divination take effect in the house of Israel — rather, what the All-Powerful has done alone is what is declared to them.'
        ("כִּי לֹא-נַחַשׁ", "ולא טיירה", "'And no omen"),
        (None, "תחיך", "can take hold"),
        ("בְּיַעֲקֹב", "פי אל יעקוב", "in the house of Jacob,"),
        ("וְלֹא-קֶסֶם", "ולא קאסומה", "nor divination"),
        (None, "ת'וות'ר", "take effect"),
        ("בְּיִשְׂרָאֵל", "פי אל אסראיל", "in the house of Israel —"),
        ("כָּעֵת יֵאָמֵר", "ואנמא יקאל להם", "rather, what"),
        ("לְיַעֲקֹב וּלְיִשְׂרָאֵל", "מא צנע", "the All-Powerful has done"),
        ("מַה-פָּעַל אֵל", "אלטאיק פקט", "alone is what is declared to them.'"),
    ],
    24: [
        # HE: הֶן-עָם כְּלָבִיא יָקוּם וְכַאֲרִי יִתְנַשָּׂא לֹא יִשְׁכַּב עַד-יֹאכַל טֶרֶף וְדַם-חֲלָלִים יִשְׁתֶּה
        # JA: והו שעב כלבו יקום. וכאסד ירתפע. אלד'י לא ינצ'גע אלי' אן יאכל פריסה. וישרב דם אלצרעא
        # EN: 'For it is a people that rises like a lioness, and lifts itself up like a lion — that does not lie down until it has eaten its prey and drunk the blood of the slain.'
        ("הֶן-עָם", "והו שעב", "'For it is a people"),
        ("כְּלָבִיא יָקוּם", "כלבו יקום", "that rises like a lioness,"),
        ("וְכַאֲרִי", "וכאסד", "and lifts itself up"),
        ("יִתְנַשָּׂא", "ירתפע", "like a lion —"),
        ("לֹא יִשְׁכַּב", "אלד'י לא ינצ'גע", "that does not lie down"),
        ("עַד-יֹאכַל", "אלי' אן יאכל", "until it has eaten"),
        ("טֶרֶף", "פריסה", "its prey"),
        ("וְדַם-חֲלָלִים יִשְׁתֶּה", "וישרב דם אלצרעא", "and drunk the blood of the slain.'"),
    ],
    25: [
        # HE: וַיֹּאמֶר בָּלָק אֶל-בִּלְעָם גַּם-קֹב לֹא תִקֳּבֶנּוּ גַּם-בָּרֵךְ לֹא תְבָרְכֶנּוּ
        # JA: קאל לה בלק. אד' לא תסבה סבא. פלא תבארכה ברכה
        # EN: Balak said to him: 'Since you will not curse him with a curse, then do not bless him with a blessing either.'
        ("וַיֹּאמֶר בָּלָק", "קאל לה בלק", "Balak said to him:"),
        ("גַּם-קֹב", "אד' לא תסבה", "'Since you will not curse him"),
        ("לֹא תִקֳּבֶנּוּ", "סבא", "with a curse,"),
        ("גַּם-בָּרֵךְ לֹא תְבָרְכֶנּוּ", "פלא תבארכה ברכה", "then do not bless him with a blessing either.'"),
    ],
    26: [
        # HE: וַיַּעַן בִּלְעָם וַיֹּאמֶר אֶל-בָּלָק הֲלֹא דִּבַּרְתִּי אֵלֶיךָ לֵאמֹר כֹּל אֲשֶׁר-יְדַבֵּר יְהוָה אֹתוֹ אֶעֱשֶׂה
        # JA: פאגאבה קאילא. אלם אקול לך. אן כל מא יקולה אללה אצנעה
        # EN: He answered him, saying: 'Did I not already tell you that whatever God says — that I shall do?'
        ("וַיַּעַן בִּלְעָם", "פאגאבה", "He answered him,"),
        ("וַיֹּאמֶר אֶל-בָּלָק", "קאילא", "saying:"),
        ("הֲלֹא דִּבַּרְתִּי אֵלֶיךָ", "אלם אקול לך", "'Did I not already tell you"),
        ("לֵאמֹר כֹּל אֲשֶׁר-יְדַבֵּר", "אן כל מא יקולה", "that whatever"),
        ("יְהוָה", "אללה", "God says —"),
        ("אֹתוֹ אֶעֱשֶׂה", "אצנעה", "that I shall do?'"),
    ],
    27: [
        # HE: וַיֹּאמֶר בָּלָק אֶל-בִּלְעָם לְכָה-נָּא אֶקָּחֲךָ אֶל-מָקוֹם אַחֵר אוּלַי יִישַׁר בְּעֵינֵי הָאֱלֹהִים וְקַבֹּתוֹ לִי מִשָּׁם
        # JA: קאל תעאל אכ'ד'ך. אלי' מוצע אכ'ר. פלעל אן יסהל ענד אללה. פתסבה לי מן הנאך
        # EN: He said: 'Come, let me take you to another place — perhaps it may be easy before God, and you shall curse him for me from there.'
        ("וַיֹּאמֶר בָּלָק", "קאל", "He said:"),
        ("לְכָה-נָּא", "תעאל", "'Come,"),
        ("אֶקָּחֲךָ", "אכ'ד'ך", "let me take you"),
        ("אֶל-מָקוֹם אַחֵר", "אלי' מוצע אכ'ר", "to another place —"),
        ("אוּלַי", "פלעל אן", "perhaps"),
        ("יִישַׁר", "יסהל", "it may be easy"),
        ("בְּעֵינֵי הָאֱלֹהִים", "ענד אללה", "before God,"),
        ("וְקַבֹּתוֹ לִי", "פתסבה לי", "and you shall curse him for me"),
        ("מִשָּׁם", "מן הנאך", "from there.'"),
    ],
    28: [
        # HE: וַיִּקַּח בָּלָק אֶת-בִּלְעָם רֹאשׁ הַפְּעוֹר הַנִּשְׁקָף עַל-פְּנֵי הַיְשִׁימֹן
        # JA: פאכ'דה. אלי' ראס אלראביה. אלמטלעה עלי' וגה אלסמאוא
        # EN: And he took him to the top of Peor, which overlooks the face of the vast expanse.
        ("וַיִּקַּח בָּלָק", "פאכ'דה", "And he took him"),
        ("אֶת-בִּלְעָם", "אלי' ראס", "to the top of"),
        ("רֹאשׁ הַפְּעוֹר", "אלראביה", "Peor,"),
        ("הַנִּשְׁקָף", "אלמטלעה", "which overlooks"),
        ("עַל-פְּנֵי", "עלי' וגה", "the face of"),
        ("הַיְשִׁימֹן", "אלסמאוא", "the vast expanse."),
    ],
    29: [
        # HE: וַיֹּאמֶר בִּלְעָם אֶל-בָּלָק בְּנֵה-לִי בָזֶה שִׁבְעָה מִזְבְּחֹת וְהָכֵן לִי בָּזֶה שִׁבְעָה פָרִים וְשִׁבְעָה אֵילִם
        # JA: קאל. אבן לי ההנא סבעה מד'אבח. ואעד לי ההנא סבעה רתות' וסבעה כבאש
        # EN: He said: 'Build me here seven altars, and prepare for me here seven bulls and seven rams.'
        ("וַיֹּאמֶר בִּלְעָם", "קאל", "He said:"),
        ("בְּנֵה-לִי", "אבן לי", "'Build me"),
        ("בָזֶה", "ההנא", "here"),
        ("שִׁבְעָה מִזְבְּחֹת", "סבעה מד'אבח", "seven altars,"),
        ("וְהָכֵן לִי", "ואעד לי", "and prepare for me"),
        (None, "ההנא", "here"),
        ("שִׁבְעָה פָרִים", "סבעה רתות'", "seven bulls"),
        ("וְשִׁבְעָה אֵילִם", "וסבעה כבאש", "and seven rams.'"),
    ],
    36: [
        # HE: ַיַּעַשׂ בָּלָק כַּאֲשֶׁר אָמַר בִּלְעָם וַיַּעַל פָּר וָאַיִל בַּמִּזְבֵּחַ
        # JA: פצנע כמא קאל לה בלעם. וקרב ת'ורא וכבשא עלי' כל מד'בחא
        # EN: And he did as Balaam had told him; and he offered there a bull and a ram upon each altar.
        ("ַיַּעַשׂ בָּלָק", "פצנע", "And he did"),
        ("כַּאֲשֶׁר אָמַר בִּלְעָם", "כמא קאל לה בלעם", "as Balaam had told him;"),
        ("וַיַּעַל", "וקרב", "and he offered there"),
        ("פָּר", "ת'ורא", "a bull"),
        ("וָאַיִל", "וכבשא", "and a ram"),
        ("בַּמִּזְבֵּחַ", "עלי' כל מד'בחא", "upon each altar."),
    ],
}

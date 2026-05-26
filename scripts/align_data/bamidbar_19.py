"""Hand-authored word-level alignment triples for Bamidbar chapter 19."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה וְאֶל-אַהֲרֹן לֵאמֹר
        # JA: ת'ם כלם אללה מוסי' והרון תכלימא
        # EN: Then God spoke to Moses and Aaron directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to"),
        ("אֶל-מֹשֶׁה", "מוסי'", "Moses"),
        ("וְאֶל-אַהֲרֹן", "והרון", "and Aaron"),
        ("לֵאמֹר", "תכלימא", "directly."),
    ],
    2: [
        # HE: זֹאת חֻקַּת הַתּוֹרָה אֲשֶׁר-צִוָּה יְהוָה לֵאמֹר דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְיִקְחוּ אֵלֶיךָ פָרָה אֲדֻמָּה תְּמִימָה אֲשֶׁר אֵין-בָּהּ מוּם אֲשֶׁר לֹא-עָלָה עָלֶיהָ עֹל
        # JA: הד'א רסם אלשריעה. אלתי אמר אללה בהא קאילא. מר בני אסראיל. באן יאתוך בבקרה צפרא צחיחה. מא ליס פיהא עיב. מא לם יטלע עליה ניר
        # EN: This is the statute of the law which God commanded, saying: 'Instruct the sons of Israel that they bring you a yellow cow, sound, in which there is no blemish, upon which no yoke has come up.'
        ("זֹאת", "הד'א", "This is"),
        ("חֻקַּת", "רסם", "the statute of"),
        ("הַתּוֹרָה", "אלשריעה", "the law"),
        ("אֲשֶׁר-צִוָּה", "אלתי אמר", "which God commanded,"),
        ("יְהוָה", "אללה", "saying:"),
        ("לֵאמֹר", "בהא קאילא", "'Instruct"),
        ("דַּבֵּר", "מר", "the sons of"),
        ("אֶל-בְּנֵי", "בני", "Israel"),
        ("יִשְׂרָאֵל", "אסראיל", "that they bring you"),
        ("וְיִקְחוּ אֵלֶיךָ", "באן יאתוך", "a yellow"),
        ("פָרָה אֲדֻמָּה", "בבקרה צפרא", "cow,"),
        ("תְּמִימָה", "צחיחה", "sound,"),
        ("אֲשֶׁר אֵין-בָּהּ מוּם", "מא ליס פיהא עיב", "in which there is no blemish,"),
        ("אֲשֶׁר לֹא-עָלָה עָלֶיהָ עֹל", "מא לם יטלע עליה ניר", "upon which no yoke has come up.'"),
    ],
    3: [
        # HE: וּנְתַתֶּם אֹתָהּ אֶל-אֶלְעָזָר הַכֹּהֵן וְהוֹצִיא אֹתָהּ אֶל-מִחוּץ לַמַּחֲנֶה וְשָׁחַט אֹתָהּ לְפָנָיו
        # JA: ואדפעוהא לאלעזר אלאמאם. ויכ'רגהא אלי' כ'ארג אלעסכר. ויד'בחהא בחצ'רתה
        # EN: 'And deliver her to Eleazar the priest, and he shall bring her out to outside the camp, and he shall slaughter her in his presence.'
        ("וּנְתַתֶּם אֹתָהּ", "ואדפעוהא", "'And deliver her"),
        ("אֶל-אֶלְעָזָר", "לאלעזר", "to Eleazar"),
        ("הַכֹּהֵן", "אלאמאם", "the priest,"),
        ("וְהוֹצִיא אֹתָהּ", "ויכ'רגהא", "and he shall bring her out"),
        ("אֶל-מִחוּץ", "אלי' כ'ארג", "to outside"),
        ("לַמַּחֲנֶה", "אלעסכר", "the camp,"),
        ("וְשָׁחַט אֹתָהּ", "ויד'בחהא", "and he shall slaughter her"),
        ("לְפָנָיו", "בחצ'רתה", "in his presence.'"),
    ],
    4: [
        # HE: וְלָקַח אֶלְעָזָר הַכֹּהֵן מִדָּמָהּ--בְּאֶצְבָּעוֹ וְהִזָּה אֶל-נֹכַח פְּנֵי אֹהֶל-מוֹעֵד מִדָּמָהּ--שֶׁבַע פְּעָמִים
        # JA: ויאכד' מן דמהא באצבעה. וינצח מקאבל וגה כ'בא אלמחצ'ר. מנה סבע מראר
        # EN: 'And he shall take of her blood with his finger, and shall sprinkle, facing the entrance of the tent of the appointed meeting, from it, seven times.'
        ("וְלָקַח", "ויאכד'", "'And he shall take"),
        ("אֶלְעָזָר הַכֹּהֵן", "מן דמהא", "of her blood"),
        ("מִדָּמָהּ", "באצבעה", "with his finger,"),
        ("בְּאֶצְבָּעוֹ", "וינצח", "and shall sprinkle,"),
        ("וְהִזָּה אֶל-נֹכַח", "מקאבל", "facing"),
        ("פְּנֵי אֹהֶל-מוֹעֵד", "וגה כ'בא אלמחצ'ר", "the entrance of the tent of the appointed meeting,"),
        ("מִדָּמָהּ", "מנה", "from it,"),
        ("שֶׁבַע", "סבע", "seven"),
        ("פְּעָמִים", "מראר", "times.'"),
    ],
    5: [
        # HE: וְשָׂרַף אֶת-הַפָּרָה לְעֵינָיו אֶת-עֹרָהּ וְאֶת-בְּשָׂרָהּ וְאֶת-דָּמָהּ עַל-פִּרְשָׁהּ יִשְׂרֹף
        # JA: ויאמר באחראקהא בחצ'רתה. מע גלדהא ולחמהא. ודמהא ופרת'הא
        # EN: 'And he shall give the order that she be burned in his presence, with her hide and her flesh, and her blood and her dung.'
        ("וְשָׂרַף אֶת-הַפָּרָה", "ויאמר באחראקהא", "'And he shall give the order that she be burned"),
        ("לְעֵינָיו", "בחצ'רתה", "in his presence,"),
        ("אֶת-עֹרָהּ", "מע גלדהא", "with her hide"),
        ("וְאֶת-בְּשָׂרָהּ", "ולחמהא", "and her flesh,"),
        ("וְאֶת-דָּמָהּ", "ודמהא", "and her blood"),
        ("עַל-פִּרְשָׁהּ יִשְׂרֹף", "ופרת'הא", "and her dung.'"),
    ],
    6: [
        # HE: וְלָקַח הַכֹּהֵן עֵץ אֶרֶז וְאֵזוֹב--וּשְׁנִי תוֹלָעַת וְהִשְׁלִיךְ אֶל-תּוֹךְ שְׂרֵפַת הַפָּרָה
        # JA: ויאכד' עוד ארז. וצעתר וצבג' קרמז. וירמי ד'אלך פי וסט חריקהא
        # EN: 'And the priest shall take a cedar-wood staff, and hyssop, and scarlet dye, and shall cast these into the midst of her burning.'
        ("וְלָקַח הַכֹּהֵן", "ויאכד'", "'And the priest shall take"),
        ("עֵץ אֶרֶז", "עוד ארז", "a cedar-wood staff,"),
        ("וְאֵזוֹב", "וצעתר", "and hyssop,"),
        ("וּשְׁנִי תוֹלָעַת", "וצבג' קרמז", "and scarlet dye,"),
        ("וְהִשְׁלִיךְ", "וירמי ד'אלך", "and shall cast these"),
        ("אֶל-תּוֹךְ", "פי וסט", "into the midst of"),
        ("שְׂרֵפַת הַפָּרָה", "חריקהא", "her burning.'"),
    ],
    7: [
        # HE: וְכִבֶּס בְּגָדָיו הַכֹּהֵן וְרָחַץ בְּשָׂרוֹ בַּמַּיִם וְאַחַר יָבֹא אֶל-הַמַּחֲנֶה וְטָמֵא הַכֹּהֵן עַד-הָעָרֶב
        # JA: ויג'סל הד'א אלאמאם ת'יאבה. וירחץ' בדנה באלמא. ובעד ד'אלך ידכ'ל אלי' אלעסכר. וינגס אלי' אלליל
        # EN: 'And this priest shall wash his garments, and shall rinse his body with water; and after that he shall enter into the camp, and he shall be impure until the evening.'
        ("וְכִבֶּס בְּגָדָיו הַכֹּהֵן", "ויג'סל הד'א אלאמאם ת'יאבה", "'And this priest shall wash his garments,"),
        ("וְרָחַץ בְּשָׂרוֹ", "וירחץ' בדנה", "and shall rinse his body"),
        ("בַּמַּיִם", "באלמא", "with water;"),
        ("וְאַחַר", "ובעד ד'אלך", "and after that"),
        ("יָבֹא", "ידכ'ל", "he shall enter"),
        ("אֶל-הַמַּחֲנֶה", "אלי' אלעסכר", "into the camp,"),
        ("וְטָמֵא הַכֹּהֵן", "וינגס", "and he shall be impure"),
        ("עַד-הָעָרֶב", "אלי' אלליל", "until the evening.'"),
    ],
    8: [
        # HE: וְהַשֹּׂרֵף אֹתָהּ--יְכַבֵּס בְּגָדָיו בַּמַּיִם וְרָחַץ בְּשָׂרוֹ בַּמָּיִם וְטָמֵא עַד-הָעָרֶב
        # JA: ואלמחרקהא. יג'סל ת'איבה. וירחץ' בדנה באלמא. וינגס אלי' אלמג'יב
        # EN: 'And he who burns her shall wash his garments, and shall rinse his body with water, and shall be impure until sunset.'
        ("וְהַשֹּׂרֵף אֹתָהּ", "ואלמחרקהא", "'And he who burns her"),
        ("יְכַבֵּס בְּגָדָיו בַּמַּיִם", "יג'סל ת'איבה", "shall wash his garments,"),
        ("וְרָחַץ בְּשָׂרוֹ", "וירחץ' בדנה", "and shall rinse his body"),
        ("בַּמָּיִם", "באלמא", "with water,"),
        ("וְטָמֵא", "וינגס", "and shall be impure"),
        ("עַד-הָעָרֶב", "אלי' אלמג'יב", "until sunset.'"),
    ],
    9: [
        # HE: וְאָסַף אִישׁ טָהוֹר אֵת אֵפֶר הַפָּרָה וְהִנִּיחַ מִחוּץ לַמַּחֲנֶה בְּמָקוֹם טָהוֹר וְהָיְתָה לַעֲדַת בְּנֵי-יִשְׂרָאֵל לְמִשְׁמֶרֶת לְמֵי נִדָּה--חַטָּאת הִוא
        # JA: ויגמע רגל טאהר. רמאד אלבקרה. ויצ'עה כ'ארג אלעסכר פי מוצ'ע טאהר. ותכון לגמאעה' בני אסראיל מחפוצ'א. למא אלנצ'ח והי ד'כוה
        # EN: 'And a ritually pure man shall gather the ashes of the cow, and shall place them outside the camp in a pure place; and it shall be kept for the congregation of the sons of Israel, for the water of sprinkling — it is a purification-offering.'
        ("וְאָסַף", "ויגמע", "'And a ritually pure man shall gather"),
        ("אִישׁ טָהוֹר", "רגל טאהר", "the ashes of"),
        ("אֵת אֵפֶר הַפָּרָה", "רמאד אלבקרה", "the cow,"),
        ("וְהִנִּיחַ", "ויצ'עה", "and shall place them"),
        ("מִחוּץ לַמַּחֲנֶה", "כ'ארג אלעסכר", "outside the camp"),
        ("בְּמָקוֹם טָהוֹר", "פי מוצ'ע טאהר", "in a pure place;"),
        ("וְהָיְתָה", "ותכון", "and it shall be kept"),
        ("לַעֲדַת בְּנֵי-יִשְׂרָאֵל", "לגמאעה' בני אסראיל", "for the congregation of the sons of Israel,"),
        ("לְמִשְׁמֶרֶת", "מחפוצ'א", "for"),
        ("לְמֵי נִדָּה", "למא אלנצ'ח", "the water of sprinkling —"),
        ("חַטָּאת הִוא", "והי ד'כוה", "it is a purification-offering.'"),
    ],
    10: [
        # HE: וְכִבֶּס הָאֹסֵף אֶת-אֵפֶר הַפָּרָה אֶת-בְּגָדָיו וְטָמֵא עַד-הָעָרֶב וְהָיְתָה לִבְנֵי יִשְׂרָאֵל וְלַגֵּר הַגָּר בְּתוֹכָם--לְחֻקַּת עוֹלָם
        # JA: ויג'סל אלגאמע רמאדהא ת'יאבה. וינגס אלי' אלליל. ותכון לבני אסראיל. ולאלג'ריב. אלדכ'יל פי מא בינהם רסם אלדהר
        # EN: 'And he who gathers her ashes shall wash his garments, and shall be impure until the evening.' And it shall be for the sons of Israel, and for the stranger who dwells among them, a perpetual statute forever.
        ("וְכִבֶּס", "ויג'סל", "'And he who gathers her ashes"),
        ("הָאֹסֵף אֶת-אֵפֶר הַפָּרָה", "אלגאמע רמאדהא", "shall wash his garments,"),
        ("אֶת-בְּגָדָיו", "ת'יאבה", "and shall be impure"),
        ("וְטָמֵא", "וינגס", "until the evening.'"),
        ("עַד-הָעָרֶב", "אלי' אלליל", "And it shall be for"),
        ("וְהָיְתָה לִבְנֵי יִשְׂרָאֵל", "ותכון לבני אסראיל", "the sons of Israel,"),
        ("וְלַגֵּר", "ולאלג'ריב", "and for the stranger"),
        ("הַגָּר בְּתוֹכָם", "אלדכ'יל פי מא בינהם", "who dwells among them,"),
        ("לְחֻקַּת עוֹלָם", "רסם אלדהר", "a perpetual statute forever."),
    ],
    11: [
        # HE: הַנֹּגֵעַ בְּמֵת לְכָל-נֶפֶשׁ אָדָם--וְטָמֵא שִׁבְעַת יָמִים
        # JA: ומן דנא במיית מן גמיע אנפס אלנאס. פלינגס סבעה' אייאם
        # EN: And whoever approaches a dead person from among all the souls of mankind shall be impure for seven days.
        ("הַנֹּגֵעַ", "ומן דנא", "And whoever approaches"),
        ("בְּמֵת", "במיית", "a dead person"),
        ("לְכָל-נֶפֶשׁ", "מן גמיע אנפס", "from among all the souls of"),
        ("אָדָם", "אלנאס", "mankind"),
        ("וְטָמֵא", "פלינגס", "shall be impure"),
        ("שִׁבְעַת יָמִים", "סבעה' אייאם", "for seven days."),
    ],
    12: [
        # HE: הוּא יִתְחַטָּא-בוֹ בַּיּוֹם הַשְּׁלִישִׁי וּבַיּוֹם הַשְּׁבִיעִי--יִטְהָר וְאִם-לֹא יִתְחַטָּא בַּיּוֹם הַשְּׁלִישִׁי וּבַיּוֹם הַשְּׁבִיעִי--לֹא יִטְהָר
        # JA: והו יתד'כא מנה. פי אליום אלת'אלת' ואלסאבע פיטהר. ואן לם יתד'כא מנה. פיהמא לא יטהר
        # EN: He shall purify himself from it on the third day and the seventh day, and then he shall be pure; but if he does not purify himself from it on both of them, he shall not be pure.
        ("הוּא", "והו", "He"),
        ("יִתְחַטָּא-בוֹ", "יתד'כא מנה", "shall purify himself from it"),
        ("בַּיּוֹם הַשְּׁלִישִׁי", "פי אליום אלת'אלת'", "on the third day"),
        ("וּבַיּוֹם הַשְּׁבִיעִי", "ואלסאבע", "and the seventh day,"),
        ("יִטְהָר", "פיטהר", "and then he shall be pure;"),
        ("וְאִם-לֹא יִתְחַטָּא", "ואן לם יתד'כא מנה", "but if he does not purify himself from it"),
        ("בַּיּוֹם הַשְּׁלִישִׁי וּבַיּוֹם הַשְּׁבִיעִי", "פיהמא", "on both of them,"),
        ("לֹא יִטְהָר", "לא יטהר", "he shall not be pure."),
    ],
    13: [
        # HE: כָּל-הַנֹּגֵעַ בְּמֵת בְּנֶפֶשׁ הָאָדָם אֲשֶׁר-יָמוּת וְלֹא יִתְחַטָּא אֶת-מִשְׁכַּן יְהוָה טִמֵּא--וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא מִיִּשְׂרָאֵל כִּי מֵי נִדָּה לֹא-זֹרַק עָלָיו טָמֵא יִהְיֶה--עוֹד טֻמְאָתוֹ בוֹ
        # JA: פכל מן דנא. במיית מן נפוס אלנאס אלד'י ימות ולא יתד'כא. פקד נגס מסכן אללה אד' דכ'לה. וינקטע ד'אלך אלאנסאן מן אל אסראיל. אד' מא אלנצ'ח. לם ירש עלי'ה פהו נגס לד'אלך. ונגאסתה עלי'ה אבדא
        # EN: So every one who approaches a dead person from among the souls of mankind who dies, and does not purify himself — he has defiled the dwelling of God when he entered it; and that person shall be cut off from the house of Israel, since the water of sprinkling was not sprinkled upon him, and he is therefore impure, and his impurity remains upon him always.
        ("כָּל-הַנֹּגֵעַ", "פכל מן דנא", "So every one who approaches"),
        ("בְּמֵת", "במיית", "a dead person"),
        ("בְּנֶפֶשׁ הָאָדָם", "מן נפוס אלנאס", "from among the souls of mankind"),
        ("אֲשֶׁר-יָמוּת", "אלד'י ימות", "who dies,"),
        ("וְלֹא יִתְחַטָּא", "ולא יתד'כא", "and does not purify himself —"),
        ("אֶת-מִשְׁכַּן יְהוָה טִמֵּא", "פקד נגס מסכן אללה אד' דכ'לה", "he has defiled the dwelling of God when he entered it;"),
        ("וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא", "וינקטע ד'אלך אלאנסאן", "and that person shall be cut off"),
        ("מִיִּשְׂרָאֵל", "מן אל אסראיל", "from the house of Israel,"),
        ("כִּי מֵי נִדָּה", "אד' מא אלנצ'ח", "since the water of sprinkling"),
        ("לֹא-זֹרַק עָלָיו", "לם ירש עלי'ה", "was not sprinkled upon him,"),
        ("טָמֵא יִהְיֶה", "פהו נגס לד'אלך", "and he is therefore impure,"),
        ("עוֹד טֻמְאָתוֹ בוֹ", "ונגאסתה עלי'ה אבדא", "and his impurity remains upon him always."),
    ],
    14: [
        # HE: זֹאת הַתּוֹרָה אָדָם כִּי-יָמוּת בְּאֹהֶל כָּל-הַבָּא אֶל-הָאֹהֶל וְכָל-אֲשֶׁר בָּאֹהֶל יִטְמָא שִׁבְעַת יָמִים
        # JA: והד'ה אלשריעה. אי אנסאן מאת פי כ'בא. פכל מא פיה וכל מן דכ'ל אלי'ה. ינגס סבעה' אייאם
        # EN: And this is the law: any person who dies in a tent — all that is in it and all who enter into it shall be impure for seven days.
        ("זֹאת", "והד'ה", "And this is"),
        ("הַתּוֹרָה", "אלשריעה", "the law:"),
        ("אָדָם כִּי-יָמוּת", "אי אנסאן מאת", "any person who dies"),
        ("בְּאֹהֶל", "פי כ'בא", "in a tent —"),
        ("כָּל-הַבָּא אֶל-הָאֹהֶל", "פכל מא פיה", "all that is in it"),
        ("וְכָל-אֲשֶׁר בָּאֹהֶל", "וכל מן דכ'ל אלי'ה", "and all who enter into it"),
        ("יִטְמָא", "ינגס", "shall be impure"),
        ("שִׁבְעַת יָמִים", "סבעה' אייאם", "for seven days."),
    ],
    15: [
        # HE: וְכֹל כְּלִי פָתוּחַ אֲשֶׁר אֵין-צָמִיד פָּתִיל עָלָיו--טָמֵא הוּא
        # JA: וכל אנא כ'זף מפתוח. אלד'י ליס לה צ'מאם מקייד. פהו נגס
        # EN: And every open earthenware vessel that has no stopper fastened upon it is impure.
        ("וְכֹל", "וכל", "And every"),
        ("כְּלִי", "אנא", "earthenware vessel"),
        ("פָתוּחַ", "כ'זף מפתוח", "open"),
        ("אֲשֶׁר אֵין-צָמִיד", "אלד'י ליס לה צ'מאם", "that has no stopper"),
        ("פָּתִיל עָלָיו", "מקייד", "fastened upon it"),
        ("טָמֵא הוּא", "פהו נגס", "is impure."),
    ],
    16: [
        # HE: וְכֹל אֲשֶׁר-יִגַּע עַל-פְּנֵי הַשָּׂדֶה בַּחֲלַל-חֶרֶב אוֹ בְמֵת אוֹ-בְעֶצֶם אָדָם אוֹ בְקָבֶר--יִטְמָא שִׁבְעַת יָמִים
        # JA: וכל מן דנא עלי' וגה אלצחרא. בקתיל סיף או מיית. או עצ'ם אנסאן או קבר. ינגס סבעה' אייאם
        # EN: And every one who approaches upon the face of the wilderness — one slain by the sword, or a dead person, or a human bone, or a grave — shall be impure for seven days.
        ("וְכֹל אֲשֶׁר-יִגַּע", "וכל מן דנא", "And every one who approaches"),
        ("עַל-פְּנֵי הַשָּׂדֶה", "עלי' וגה אלצחרא", "upon the face of the wilderness —"),
        ("בַּחֲלַל-חֶרֶב", "בקתיל סיף", "one slain by the sword,"),
        ("אוֹ בְמֵת", "או מיית", "or a dead person,"),
        ("אוֹ-בְעֶצֶם אָדָם", "או עצ'ם אנסאן", "or a human bone,"),
        ("אוֹ בְקָבֶר", "או קבר", "or a grave —"),
        ("יִטְמָא", "ינגס", "shall be impure"),
        ("שִׁבְעַת יָמִים", "סבעה' אייאם", "for seven days."),
    ],
    17: [
        # HE: וְלָקְחוּ לַטָּמֵא מֵעֲפַר שְׂרֵפַת הַחַטָּאת וְנָתַן עָלָיו מַיִם חַיִּים אֶל-כֶּלִי
        # JA: וליוכ'ד' לה. מן רמאד חריק אלבקרה. ויצב עלי'ה. מא נביע פי אנא
        # EN: And there shall be taken for him some of the ashes of the burning of the cow, and spring water shall be poured over it into a vessel.
        ("וְלָקְחוּ", "וליוכ'ד'", "And there shall be taken"),
        ("לַטָּמֵא", "לה", "for him"),
        ("מֵעֲפַר", "מן רמאד", "some of the ashes of"),
        ("שְׂרֵפַת הַחַטָּאת", "חריק אלבקרה", "the burning of the cow,"),
        ("וְנָתַן עָלָיו", "ויצב עלי'ה", "and spring water shall be poured over it"),
        ("מַיִם חַיִּים", "מא נביע", "into"),
        ("אֶל-כֶּלִי", "פי אנא", "a vessel."),
    ],
    18: [
        # HE: וְלָקַח אֵזוֹב וְטָבַל בַּמַּיִם אִישׁ טָהוֹר וְהִזָּה עַל-הָאֹהֶל וְעַל-כָּל-הַכֵּלִים וְעַל-הַנְּפָשׁוֹת אֲשֶׁר הָיוּ-שָׁם וְעַל-הַנֹּגֵעַ בַּעֶצֶם אוֹ בֶחָלָל אוֹ בַמֵּת אוֹ בַקָּבֶר
        # JA: ואליאכ'ד' רגל טאהר שייא מן צעתר. ויג'מסה פי ד'אלך אלמא. וינצ'ח עלי' אלכ'בא ועלי' גמיע אלאניה. ועלי' אלנפוס אלד'י כאנת ת'ם. ועלי' אלדאני. באל עצ'ם או באלקתיל. או אלמיית או אלקבר
        # EN: And a ritually pure man shall take some hyssop, and dip it in that water, and shall sprinkle upon the tent, and upon all the vessels, and upon the persons who were there, and upon the one who drew near to a bone, or to the slain, or to the dead, or to the grave.
        ("וְלָקַח אֵזוֹב", "ואליאכ'ד' רגל טאהר שייא מן צעתר", "And a ritually pure man shall take some hyssop,"),
        ("וְטָבַל בַּמַּיִם", "ויג'מסה פי ד'אלך אלמא", "and dip it in that water,"),
        ("אִישׁ טָהוֹר", "וינצ'ח", "and shall sprinkle"),
        ("וְהִזָּה עַל-הָאֹהֶל", "עלי' אלכ'בא", "upon the tent,"),
        ("וְעַל-כָּל-הַכֵּלִים", "ועלי' גמיע אלאניה", "and upon all the vessels,"),
        ("וְעַל-הַנְּפָשׁוֹת אֲשֶׁר הָיוּ-שָׁם", "ועלי' אלנפוס אלד'י כאנת ת'ם", "and upon the persons who were there,"),
        ("וְעַל-הַנֹּגֵעַ", "ועלי' אלדאני", "and upon the one who drew near"),
        ("בַּעֶצֶם", "באל עצ'ם", "to a bone,"),
        ("אוֹ בֶחָלָל", "או באלקתיל", "or to the slain,"),
        ("אוֹ בַמֵּת", "או אלמיית", "or to the dead,"),
        ("אוֹ בַקָּבֶר", "או אלקבר", "or to the grave."),
    ],
    19: [
        # HE: וְהִזָּה הַטָּהֹר עַל-הַטָּמֵא בַּיּוֹם הַשְּׁלִישִׁי וּבַיּוֹם הַשְּׁבִיעִי וְחִטְּאוֹ בַּיּוֹם הַשְּׁבִיעִי וְכִבֶּס בְּגָדָיו וְרָחַץ בַּמַּיִם וְטָהֵר בָּעָרֶב
        # JA: כדאך ינצ'ח אלטאהר עלי' אלנגס. פי אליום אלת'לאת' ואלסאבע. פאד'א ד'כאה פי אליום אלסאבע. ג'סל ת'יאבה. ורחץ' באלמא וטהר באלעשי
        # EN: So the pure man shall sprinkle upon the impure on the third day and the seventh day; and when he has purified him on the seventh day, he shall wash his garments and rinse himself with water, and shall be pure at evening.
        (None, "כדאך", "So"),
        ("וְהִזָּה הַטָּהֹר", "ינצ'ח אלטאהר", "the pure man shall sprinkle"),
        ("עַל-הַטָּמֵא", "עלי' אלנגס", "upon the impure"),
        ("בַּיּוֹם הַשְּׁלִישִׁי", "פי אליום אלת'לאת'", "on the third day"),
        ("וּבַיּוֹם הַשְּׁבִיעִי", "ואלסאבע", "and the seventh day;"),
        ("וְחִטְּאוֹ בַּיּוֹם הַשְּׁבִיעִי", "פאד'א ד'כאה פי אליום אלסאבע", "and when he has purified him on the seventh day,"),
        ("וְכִבֶּס בְּגָדָיו", "ג'סל ת'יאבה", "he shall wash his garments"),
        ("וְרָחַץ בַּמַּיִם", "ורחץ' באלמא", "and rinse himself with water,"),
        ("וְטָהֵר בָּעָרֶב", "וטהר באלעשי", "and shall be pure at evening."),
    ],
    20: [
        # HE: וְאִישׁ אֲשֶׁר-יִטְמָא וְלֹא יִתְחַטָּא וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא מִתּוֹךְ הַקָּהָל כִּי אֶת-מִקְדַּשׁ יְהוָה טִמֵּא מֵי נִדָּה לֹא-זֹרַק עָלָיו--טָמֵא הוּא
        # JA: ואי רגל תנגס בד'אלך ולם יתד'כא. פינקטע ד'אלך אלאנסאן מן בין אלגוק. למא נגס מקדס אללה אד' דכ'לה. ולם ינצ'ח עלי'ה מן מא אלנצ'ח פהו נגס
        # EN: But any man who has become impure by this and has not purified himself — that person shall be cut off from among the assembly, since he has defiled the sanctuary of God when he entered it, and the water of sprinkling was not sprinkled upon him; he is impure.
        ("וְאִישׁ", "ואי רגל", "But any man"),
        ("אֲשֶׁר-יִטְמָא", "תנגס בד'אלך", "who has become impure by this"),
        ("וְלֹא יִתְחַטָּא", "ולם יתד'כא", "and has not purified himself —"),
        ("וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא", "פינקטע ד'אלך אלאנסאן", "that person shall be cut off"),
        ("מִתּוֹךְ הַקָּהָל", "מן בין אלגוק", "from among the assembly,"),
        ("כִּי", "למא", "since"),
        ("אֶת-מִקְדַּשׁ יְהוָה טִמֵּא", "נגס מקדס אללה אד' דכ'לה", "he has defiled the sanctuary of God when he entered it,"),
        ("מֵי נִדָּה", "ולם ינצ'ח עלי'ה מן מא אלנצ'ח", "and the water of sprinkling was not sprinkled upon him;"),
        ("לֹא-זֹרַק עָלָיו", "פהו נגס", "he is impure."),
    ],
    21: [
        # HE: וְהָיְתָה לָהֶם לְחֻקַּת עוֹלָם וּמַזֵּה מֵי-הַנִּדָּה יְכַבֵּס בְּגָדָיו וְהַנֹּגֵעַ בְּמֵי הַנִּדָּה יִטְמָא עַד-הָעָרֶב
        # JA: ויכון להם דא'לך רסם אלדהר. ונאצ'ח מא אלנצ'ח יג'סל ת'יאבה. ומן לאמס מא אלנצ'ח. ינגס אלי' אלליל
        # EN: And this shall be for them a perpetual statute forever. And the one who sprinkles the water of sprinkling shall wash his garments; and whoever touches the water of sprinkling shall be impure until the evening.
        ("וְהָיְתָה לָהֶם", "ויכון להם", "And this shall be for them"),
        ("לְחֻקַּת עוֹלָם", "דא'לך רסם אלדהר", "a perpetual statute forever."),
        ("וּמַזֵּה", "ונאצ'ח", "And the one who sprinkles"),
        ("מֵי-הַנִּדָּה", "מא אלנצ'ח", "the water of sprinkling"),
        ("יְכַבֵּס בְּגָדָיו", "יג'סל ת'יאבה", "shall wash his garments;"),
        ("וְהַנֹּגֵעַ", "ומן לאמס", "and whoever touches"),
        ("בְּמֵי הַנִּדָּה", "מא אלנצ'ח", "the water of sprinkling"),
        ("יִטְמָא", "ינגס", "shall be impure"),
        ("עַד-הָעָרֶב", "אלי' אלליל", "until the evening."),
    ],
    22: [
        # HE: וְכֹל אֲשֶׁר-יִגַּע-בּוֹ הַטָּמֵא יִטְמָא וְהַנֶּפֶשׁ הַנֹּגַעַת תִּטְמָא עַד-הָעָרֶב
        # JA: וכל מא לאמסה אלנגס ינגס. פאן כאן אנסאן דנא בה ינגס אלי' אלליל
        # EN: And whatever the impure person touches shall become impure; and if a person approached it, he shall be impure until the evening.
        ("וְכֹל אֲשֶׁר-יִגַּע-בּוֹ", "וכל מא לאמסה", "And whatever"),
        ("הַטָּמֵא", "אלנגס", "the impure person touches"),
        ("יִטְמָא", "ינגס", "shall become impure;"),
        ("וְהַנֶּפֶשׁ הַנֹּגַעַת", "פאן כאן אנסאן דנא בה", "and if a person approached it,"),
        ("תִּטְמָא", "ינגס", "he shall be impure"),
        ("עַד-הָעָרֶב", "אלי' אלליל", "until the evening."),
    ],
}

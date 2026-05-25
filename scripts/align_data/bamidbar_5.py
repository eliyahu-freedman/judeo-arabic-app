"""Hand-authored word-level alignment triples for Bamidbar chapter 5."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה לֵּאמֹר", "מוסי' תכלימא", "directly."),
    ],
    2: [
        # צַו אֶת-בְּנֵי יִשְׂרָאֵל וִישַׁלְּחוּ מִן-הַמַּחֲנֶה כָּל-צָרוּעַ וְכָל-זָב וְכֹל טָמֵא לָנָפֶשׁ
        # JA: מר בני אסראיל. באן ינפו מן אלעסכר. כל אברץ וכל ד'איב. וכל נגס במיית
        # EN: Command the sons of Israel that they drive out from the camp every leper, and every one with a discharge, and every one made impure by a corpse.
        ("צַו", "מר", "Command"),
        ("אֶת-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel"),
        ("וִישַׁלְּחוּ", "באן ינפו", "that they drive out"),
        ("מִן-הַמַּחֲנֶה", "מן אלעסכר", "from the camp"),
        ("כָּל-צָרוּעַ", "כל אברץ", "every leper,"),
        ("וְכָל-זָב", "וכל ד'איב", "and every one with a discharge,"),
        ("וְכֹל טָמֵא", "וכל נגס", "and every one made impure"),
        ("לָנָפֶשׁ", "במיית", "by a corpse."),
    ],
    3: [
        # מִזָּכָר עַד-נְקֵבָה תְּשַׁלֵּחוּ אֶל-מִחוּץ לַמַּחֲנֶה תְּשַׁלְּחוּם וְלֹא יְטַמְּאוּ אֶת-מַחֲנֵיהֶם אֲשֶׁר אֲנִי שֹׁכֵן בְּתוֹכָם
        # JA: מן ד'כר אלי' אנת'י תנפוהם. אלי' כ'ארג אלעסכר. ולא ינגסו עסכרהם. אלד'י אנא סאכנה פי מא בינהם
        # EN: From male to female you shall drive them out, to the outside of the camp, that they not defile their camp, in which I dwell among them.
        ("מִזָּכָר", "מן ד'כר", "From male"),
        ("עַד-נְקֵבָה", "אלי' אנת'י", "to female"),
        ("תְּשַׁלֵּחוּ", "תנפוהם", "you shall drive them out,"),
        ("אֶל-מִחוּץ", "אלי' כ'ארג", "to the outside of"),
        ("לַמַּחֲנֶה", "אלעסכר", "the camp,"),
        ("וְלֹא", "ולא", "that they not"),
        ("יְטַמְּאוּ", "ינגסו", "defile"),
        ("אֶת-מַחֲנֵיהֶם", "עסכרהם", "their camp,"),
        ("אֲשֶׁר", "אלד'י", "in which"),
        ("אֲנִי", "אנא", "I"),
        ("שֹׁכֵן", "סאכנה", "dwell"),
        ("בְּתוֹכָם", "פי מא בינהם", "among them."),
    ],
    4: [
        # וַיַּעֲשׂוּ-כֵן בְּנֵי יִשְׂרָאֵל וַיְשַׁלְּחוּ אוֹתָם אֶל-מִחוּץ לַמַּחֲנֶה כַּאֲשֶׁר דִּבֶּר יְהוָה אֶל-מֹשֶׁה כֵּן עָשׂוּ בְּנֵי יִשְׂרָאֵל
        # JA: פצנע כד'אך בני אסראיל. ונפוהם אלי' כ'ארג אלעסכר. כמא אמר אללה מוסי'. כד'אך צנעו בני אסראיל
        # EN: And the sons of Israel did so, and drove them out to the outside of the camp, as God had commanded Moses — so the sons of Israel did.
        ("וַיַּעֲשׂוּ-כֵן", "פצנע כד'אך", "And"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel did so,"),
        ("וַיְשַׁלְּחוּ אוֹתָם אֶל-מִחוּץ לַמַּחֲנֶה", "ונפוהם אלי' כ'ארג אלעסכר", "and drove them out to the outside of the camp,"),
        ("כַּאֲשֶׁר דִּבֶּר יְהוָה אֶל-מֹשֶׁה", "כמא אמר אללה מוסי'", "as God had commanded Moses —"),
        ("כֵּן עָשׂוּ בְּנֵי יִשְׂרָאֵל", "כד'אך צנעו בני אסראיל", "so the sons of Israel did."),
    ],
    5: [
        # וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה לֵּאמֹר", "מוסי' תכלימא", "directly."),
    ],
    6: [
        # דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל אִישׁ אוֹ-אִשָּׁה כִּי יַעֲשׂוּ מִכָּל-חַטֹּאת הָאָדָם לִמְעֹל מַעַל בַּיהוָה וְאָשְׁמָה הַנֶּפֶשׁ הַהִוא
        # JA: קל לבני אסראיל. אי רגל או אמראה. יצנע שייא מן כ'טאיא אלנאס. לינכת' נכת'א באללה. פאת'ם
        # EN: Say to the sons of Israel: any man or woman who does something from the sins common among people, so as to break faith with God — and has sinned,
        ("דַּבֵּר", "קל", "Say"),
        ("אֶל-בְּנֵי", "לבני", "to the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel:"),
        ("אִישׁ", "אי רגל", "any man"),
        ("אוֹ-אִשָּׁה", "או אמראה", "or woman"),
        ("כִּי יַעֲשׂוּ", "יצנע", "who does"),
        ("מִכָּל-חַטֹּאת", "שייא מן כ'טאיא", "something from the sins"),
        ("הָאָדָם", "אלנאס", "common among people,"),
        ("לִמְעֹל", "לינכת'", "so as to break faith"),
        ("מַעַל", "נכת'א", "with"),
        ("בַּיהוָה", "באללה", "God —"),
        ("וְאָשְׁמָה הַנֶּפֶשׁ הַהִוא", "פאת'ם", "and has sinned,"),
    ],
    7: [
        # וְהִתְוַדּוּ אֶת-חַטָּאתָם אֲשֶׁר עָשׂוּ וְהֵשִׁיב אֶת-אֲשָׁמוֹ בְּרֹאשׁוֹ וַחֲמִישִׁתוֹ יֹסֵף עָלָיו וְנָתַן לַאֲשֶׁר אָשַׁם לוֹ
        # JA: ת'ם יקר בכ'טייתה אלד'י צנעהא. פלירד אלצ'לאמה בראסהא. ויזיד עלי'הא כמסהא. וידפעהא אלי' מן צ'למה
        # EN: then he shall confess his wrongdoing which he committed; and he shall return the wrongful taking in full, and add a fifth part to it, and pay it to the one he wronged.
        ("וְהִתְוַדּוּ", "ת'ם יקר", "then he shall confess"),
        ("אֶת-חַטָּאתָם", "בכ'טייתה", "his wrongdoing"),
        ("אֲשֶׁר", "אלד'י", "which"),
        ("עָשׂוּ", "צנעהא", "he committed;"),
        ("וְהֵשִׁיב", "פלירד", "and he shall return"),
        ("אֶת-אֲשָׁמוֹ", "אלצ'לאמה", "the wrongful taking"),
        ("בְּרֹאשׁוֹ", "בראסהא", "in full,"),
        ("וַחֲמִישִׁתוֹ יֹסֵף עָלָיו", "ויזיד עלי'הא כמסהא", "and add a fifth part to it,"),
        ("וְנָתַן", "וידפעהא", "and pay it"),
        ("לַאֲשֶׁר", "אלי' מן", "to the one"),
        ("אָשַׁם", "צ'למה", "he wronged."),
    ],
    8: [
        # וְאִם-אֵין לָאִישׁ גֹּאֵל לְהָשִׁיב הָאָשָׁם אֵלָיו--הָאָשָׁם הַמּוּשָׁב לַיהוָה לַכֹּהֵן מִלְּבַד אֵיל הַכִּפֻּרִים אֲשֶׁר יְכַפֶּר-בּוֹ עָלָיו
        # JA: ואן לם יכון לאלמצ'לום ולי. לתרד אלצ'לאמה אלמרדודה ללה והי לאלאמאם. סוא כבש אלג'פראן. אלד'י יסתג'פר בה ענה
        # EN: And if the wronged one has no next of kin to whom the wrongful taking may be returned, then the wrongful taking that is returned shall be for God — it belongs to the imām — apart from the ram of atonement by which he seeks forgiveness on his behalf.
        ("וְאִם-אֵין", "ואן לם יכון", "And if"),
        ("לָאִישׁ", "לאלמצ'לום", "the wronged one has"),
        ("גֹּאֵל", "ולי", "no next of kin"),
        ("לְהָשִׁיב", "לתרד", "to whom the wrongful taking may be returned,"),
        ("הָאָשָׁם", "אלצ'לאמה", "then the wrongful taking"),
        ("הַמּוּשָׁב", "אלמרדודה", "that is returned"),
        ("לַיהוָה", "ללה", "shall be for God —"),
        ("לַכֹּהֵן", "והי לאלאמאם", "it belongs to the imām —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("אֵיל", "כבש", "the ram of"),
        ("הַכִּפֻּרִים", "אלג'פראן", "atonement"),
        ("אֲשֶׁר", "אלד'י", "by which"),
        ("יְכַפֶּר-בּוֹ", "יסתג'פר בה", "he seeks forgiveness"),
        ("עָלָיו", "ענה", "on his behalf."),
    ],
    9: [
        # וְכָל-תְּרוּמָה לְכָל-קָדְשֵׁי בְנֵי-יִשְׂרָאֵל אֲשֶׁר-יַקְרִיבוּ לַכֹּהֵן--לוֹ יִהְיֶה
        # JA: וכל רפיעה. מן גמיע אקדאס בני אסראיל פלאי אמאם דפעוהא כאנת לה
        # EN: And every contribution from all the sacred gifts of the sons of Israel — to whichever imām they hand it, it shall be his.
        ("וְכָל-תְּרוּמָה", "וכל רפיעה", "And every contribution"),
        ("לְכָל-קָדְשֵׁי", "מן גמיע אקדאס", "from all the sacred gifts of"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel —"),
        ("לַכֹּהֵן", "פלאי אמאם", "to whichever imām"),
        ("אֲשֶׁר-יַקְרִיבוּ", "דפעוהא", "they hand it,"),
        ("לוֹ יִהְיֶה", "כאנת לה", "it shall be his."),
    ],
    10: [
        # וְאִישׁ אֶת-קֳדָשָׁיו לוֹ יִהְיוּ אִישׁ אֲשֶׁר-יִתֵּן לַכֹּהֵן לוֹ יִהְיֶה
        # JA: וכל אמר יכון לה אמר אקדאסה. לאי אמאם דפעהא כאנת לה
        # EN: And every man who has disposition over his sacred things: to whichever imām he gives it, it shall be his.
        ("וְאִישׁ", "וכל אמר", "And every man"),
        (None, "יכון לה", "who has disposition over"),
        ("אֶת-קֳדָשָׁיו", "אמר אקדאסה", "his sacred things:"),
        ("לַכֹּהֵן", "לאי אמאם", "to whichever imām"),
        ("אֲשֶׁר-יִתֵּן", "דפעהא", "he gives it,"),
        ("לוֹ יִהְיֶה", "כאנת לה", "it shall be his."),
    ],
    11: [
        # וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה לֵּאמֹר", "מוסי' תכלימא", "directly."),
    ],
    12: [
        # דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם אִישׁ אִישׁ כִּי-תִשְׂטֶה אִשְׁתּוֹ וּמָעֲלָה בוֹ מָעַל
        # JA: מר בני אסראיל. וקל להם. אי רגל חאדת זוגתה. פכ'אנתה כ'יאנה
        # EN: Command the sons of Israel and say to them: any man whose wife has gone astray and betrayed him with a betrayal —
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("אִישׁ אִישׁ", "אי רגל", "any man"),
        ("כִּי-תִשְׂטֶה אִשְׁתּוֹ", "חאדת זוגתה", "whose wife has gone astray"),
        ("וּמָעֲלָה", "פכ'אנתה", "and betrayed him"),
        ("מָעַל", "כ'יאנה", "with a betrayal —"),
    ],
    13: [
        # וְשָׁכַב אִישׁ אֹתָהּ שִׁכְבַת-זֶרַע וְנֶעְלַם מֵעֵינֵי אִישָׁהּ וְנִסְתְּרָה וְהִיא נִטְמָאָה וְעֵד אֵין בָּהּ וְהִוא לֹא נִתְפָּשָׂה
        # JA: באן צ'אגעהא רגל מצאגעה' אנסאל. וג'בי ד'אלך ען זוגהא. ואנסתרת והי נגסה. ושאהד ליס עלי'הא. והי לם תקהר
        # EN: in that a man has lain with her in a lying of emission, and this has been hidden from her husband, and she has concealed herself while being impure, and there is no witness against her, and she was not forced —
        ("וְשָׁכַב", "באן צ'אגעהא", "in that a man has lain with her"),
        ("אִישׁ", "רגל", "in a lying of"),
        ("שִׁכְבַת-זֶרַע", "מצאגעה' אנסאל", "emission,"),
        ("וְנֶעְלַם", "וג'בי ד'אלך", "and this has been hidden"),
        ("מֵעֵינֵי אִישָׁהּ", "ען זוגהא", "from her husband,"),
        ("וְנִסְתְּרָה", "ואנסתרת", "and she has concealed herself"),
        ("וְהִיא", "והי", "while being"),
        ("נִטְמָאָה", "נגסה", "impure,"),
        ("וְעֵד אֵין בָּהּ", "ושאהד ליס עלי'הא", "and there is no witness against her,"),
        ("וְהִוא לֹא נִתְפָּשָׂה", "והי לם תקהר", "and she was not forced —"),
    ],
    14: [
        # וְעָבַר עָלָיו רוּחַ-קִנְאָה וְקִנֵּא אֶת-אִשְׁתּוֹ וְהִוא נִטְמָאָה אוֹ-עָבַר עָלָיו רוּחַ-קִנְאָה וְקִנֵּא אֶת-אִשְׁתּוֹ וְהִיא לֹא נִטְמָאָה
        # JA: וכ'טר בבאלה ראי ג'ירה. פג'אר עלי'הא והי נגסה. או ג'יר נגסה
        # EN: and a thought of jealousy has entered his mind, and he is jealous over her while she is impure, or while she is not impure —
        ("וְעָבַר עָלָיו", "וכ'טר בבאלה", "and a thought of jealousy has entered his mind,"),
        ("רוּחַ-קִנְאָה", "ראי ג'ירה", "and he is jealous"),
        ("וְקִנֵּא אֶת-אִשְׁתּוֹ", "פג'אר עלי'הא", "over her"),
        ("וְהִוא נִטְמָאָה", "והי נגסה", "while she is impure,"),
        ("אוֹ-עָבַר עָלָיו רוּחַ-קִנְאָה וְקִנֵּא אֶת-אִשְׁתּוֹ וְהִיא לֹא נִטְמָאָה", "או ג'יר נגסה", "or while she is not impure —"),
    ],
    15: [
        # וְהֵבִיא הָאִישׁ אֶת-אִשְׁתּוֹ אֶל-הַכֹּהֵן וְהֵבִיא אֶת-קָרְבָּנָהּ עָלֶיהָ עֲשִׂירִת הָאֵיפָה קֶמַח שְׂעֹרִים לֹא-יִצֹק עָלָיו שֶׁמֶן וְלֹא-יִתֵּן עָלָיו לְבֹנָה--כִּי-מִנְחַת קְנָאֹת הוּא מִנְחַת זִכָּרוֹן מַזְכֶּרֶת עָו‍ֹן
        # JA: פליאת ד'אלך אלרג'ל בזוגתה אלי' אלאמאם. ויאתי בקרבאנהא מעהא. עשר ויבה מן דקיק אלשעיר. לא יצב עליה דהנא. ולא יגעל עליה לבאנא. לאנה קרבאן אלג'ירה. קרבאן אלדכר יד'כר באלד'נוב
        # EN: then that man shall bring his wife to the imām, and shall bring her offering with her: a tenth of a waybah of barley flour; he shall not pour oil upon it, nor place frankincense upon it, for it is the offering of jealousy, the offering of remembrance, which calls sins to mind.
        ("וְהֵבִיא", "פליאת", "then that man shall bring"),
        ("הָאִישׁ", "ד'אלך אלרג'ל", "his wife"),
        ("אֶת-אִשְׁתּוֹ", "בזוגתה", "to the imām,"),
        ("אֶל-הַכֹּהֵן", "אלי' אלאמאם", "and shall bring her offering with her:"),
        ("וְהֵבִיא אֶת-קָרְבָּנָהּ", "ויאתי בקרבאנהא", "a tenth of"),
        ("עָלֶיהָ", "מעהא", "a waybah of"),
        ("עֲשִׂירִת", "עשר", "barley flour;"),
        ("הָאֵיפָה", "ויבה", "he shall not pour"),
        ("קֶמַח", "מן דקיק", "oil upon it,"),
        ("שְׂעֹרִים", "אלשעיר", "nor place frankincense upon it,"),
        ("לֹא-יִצֹק עָלָיו שֶׁמֶן", "לא יצב עליה דהנא", "for it is the offering of jealousy,"),
        ("וְלֹא-יִתֵּן עָלָיו לְבֹנָה", "ולא יגעל עליה לבאנא", "the offering of remembrance,"),
        ("כִּי-מִנְחַת קְנָאֹת הוּא מִנְחַת זִכָּרוֹן מַזְכֶּרֶת עָו‍ֹן", "לאנה קרבאן אלג'ירה. קרבאן אלדכר יד'כר באלד'נוב", "which calls sins to mind."),
    ],
    16: [
        # וְהִקְרִיב אֹתָהּ הַכֹּהֵן וְהֶעֱמִדָהּ לִפְנֵי יְהוָה
        # JA: ויקדמהא אלאמאם. ויוקפהא בין ידי אללה
        # EN: And the imām shall present her and station her before God.
        ("וְהִקְרִיב אֹתָהּ הַכֹּהֵן", "ויקדמהא אלאמאם", "And the imām shall present her"),
        ("וְהֶעֱמִדָהּ", "ויוקפהא", "and station her"),
        ("לִפְנֵי", "בין ידי", "before"),
        ("יְהוָה", "אללה", "God."),
    ],
    17: [
        # וְלָקַח הַכֹּהֵן מַיִם קְדֹשִׁים בִּכְלִי-חָרֶשׂ וּמִן-הֶעָפָר אֲשֶׁר יִהְיֶה בְּקַרְקַע הַמִּשְׁכָּן יִקַּח הַכֹּהֵן וְנָתַן אֶל-הַמָּיִם
        # JA: ויאכ'ד' אלאמאם. מן אלמא אלמקדס פי אניה' כ'זף. ומן אלתראב. אלד'י יכון פי ערצה' אלמסכן. יאכ'ד' אלאמאם וילקי פי אלמא
        # EN: And the imām shall take holy water in an earthen vessel, and from the dust that is on the floor of the tabernacle the imām shall take and cast into the water.
        ("וְלָקַח הַכֹּהֵן", "ויאכ'ד' אלאמאם", "And the imām shall take"),
        ("מַיִם קְדֹשִׁים", "מן אלמא אלמקדס", "holy water"),
        ("בִּכְלִי-חָרֶשׂ", "פי אניה' כ'זף", "in an earthen vessel,"),
        ("וּמִן-הֶעָפָר", "ומן אלתראב", "and from the dust"),
        ("אֲשֶׁר", "אלד'י", "that is on"),
        ("יִהְיֶה", "יכון", "the floor of"),
        ("בְּקַרְקַע", "פי ערצה'", "the tabernacle"),
        ("הַמִּשְׁכָּן", "אלמסכן", "the imām shall take"),
        ("יִקַּח הַכֹּהֵן", "יאכ'ד' אלאמאם", "and cast"),
        ("וְנָתַן אֶל-הַמָּיִם", "וילקי פי אלמא", "into the water."),
    ],
    18: [
        # וְהֶעֱמִיד הַכֹּהֵן אֶת-הָאִשָּׁה לִפְנֵי יְהוָה וּפָרַע אֶת-רֹאשׁ הָאִשָּׁה וְנָתַן עַל-כַּפֶּיהָ אֵת מִנְחַת הַזִּכָּרוֹן מִנְחַת קְנָאֹת הִוא וּבְיַד הַכֹּהֵן יִהְיוּ מֵי הַמָּרִים הַמְאָרְרִים
        # JA: ויוקפהא בין ידי אללה. ויכשף ראסהא. ויגעל עלי' ידהא. קרבאן אלד'כר קרבאן אלג'ירה. ולימסך פי ידה אלמא אלמר אללאען
        # EN: And he shall station her before God, and uncover her head, and place upon her hands the offering of remembrance — the offering of jealousy; and in his hand the imām shall hold the bitter, cursing water.
        ("וְהֶעֱמִיד הַכֹּהֵן אֶת-הָאִשָּׁה", "ויוקפהא", "And he shall station her"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God,"),
        ("וּפָרַע", "ויכשף", "and uncover"),
        ("אֶת-רֹאשׁ הָאִשָּׁה", "ראסהא", "her head,"),
        ("וְנָתַן", "ויגעל", "and place"),
        ("עַל-כַּפֶּיהָ", "עלי' ידהא", "upon her hands"),
        ("אֵת מִנְחַת הַזִּכָּרוֹן", "קרבאן אלד'כר", "the offering of remembrance —"),
        ("מִנְחַת קְנָאֹת הִוא", "קרבאן אלג'ירה", "the offering of jealousy;"),
        ("וּבְיַד הַכֹּהֵן יִהְיוּ", "ולימסך פי ידה", "and in his hand the imām shall hold"),
        ("מֵי הַמָּרִים", "אלמא אלמר", "the bitter,"),
        ("הַמְאָרְרִים", "אללאען", "cursing water."),
    ],
    19: [
        # וְהִשְׁבִּיעַ אֹתָהּ הַכֹּהֵן וְאָמַר אֶל-הָאִשָּׁה אִם-לֹא שָׁכַב אִישׁ אֹתָךְ וְאִם-לֹא שָׂטִית טֻמְאָה תַּחַת אִישֵׁךְ--הִנָּקִי מִמֵּי הַמָּרִים הַמְאָרְרִים הָאֵלֶּה
        # JA: ויחלפהא ויקול להא. אן כאן לם י'צ'אגעך רג'ל. ולם תחידי אלי' נגאסה ג'יר זוגך. פאברי מן הד'א אלמא אלמר אללאען
        # EN: And he shall adjure her and say to her: 'If no man has lain with you, and you have not gone astray into impurity other than with your husband — then be cleared of this bitter, cursing water.'
        ("וְהִשְׁבִּיעַ אֹתָהּ הַכֹּהֵן", "ויחלפהא", "And he shall adjure her"),
        ("וְאָמַר", "ויקול", "and say"),
        ("אֶל-הָאִשָּׁה", "להא", "to her:"),
        ("אִם-לֹא", "אן כאן לם", "'If no"),
        ("שָׁכַב", "י'צ'אגעך", "man has lain with you,"),
        ("אִישׁ", "רג'ל", "and"),
        ("וְאִם-לֹא", "ולם", "you have not"),
        ("שָׂטִית", "תחידי", "gone astray"),
        ("טֻמְאָה", "אלי' נגאסה", "into impurity"),
        ("תַּחַת אִישֵׁךְ", "ג'יר זוגך", "other than with your husband —"),
        ("הִנָּקִי", "פאברי", "then be cleared of"),
        ("מִמֵּי הַמָּרִים הַמְאָרְרִים הָאֵלֶּה", "מן הד'א אלמא אלמר אללאען", "this bitter, cursing water.'"),
    ],
    20: [
        # וְאַתְּ כִּי שָׂטִית תַּחַת אִישֵׁךְ--וְכִי נִטְמֵאת וַיִּתֵּן אִישׁ בָּךְ אֶת-שְׁכָבְתּוֹ מִבַּלְעֲדֵי אִישֵׁךְ
        # JA: ואן כנת חדת. אלי' ג'יר זוגך ותנגסת בה. וגעל ג'ירה מצ'אגעתה פיך
        # EN: But if you have gone astray to one other than your husband, and defiled yourself with him, and another has placed his lying with you —
        ("וְאַתְּ", "ואן כנת", "But if you have"),
        ("כִּי שָׂטִית", "חדת", "gone astray"),
        ("תַּחַת אִישֵׁךְ", "אלי' ג'יר זוגך", "to one other than your husband,"),
        ("וְכִי נִטְמֵאת", "ותנגסת", "and defiled yourself"),
        (None, "בה", "with him,"),
        ("וַיִּתֵּן", "וגעל", "and another has placed"),
        ("אִישׁ", "ג'ירה", "his lying"),
        ("אֶת-שְׁכָבְתּוֹ מִבַּלְעֲדֵי אִישֵׁךְ", "מצ'אגעתה פיך", "with you —"),
    ],
    21: [
        # וְהִשְׁבִּיעַ הַכֹּהֵן אֶת-הָאִשָּׁה בִּשְׁבֻעַת הָאָלָה וְאָמַר הַכֹּהֵן לָאִשָּׁה יִתֵּן יְהוָה אוֹתָךְ לְאָלָה וְלִשְׁבֻעָה בְּתוֹךְ עַמֵּךְ--בְּתֵת יְהוָה אֶת-יְרֵכֵךְ נֹפֶלֶת וְאֶת-בִּטְנֵךְ צָבָה
        # JA: ויחלפהא עלי' ד'אלך ימין אלחרג. ויקול אלאמאם להא. יגעלך אללה. מסבה וימינא פי מא בין קומך. במא יגעל אללה ורכך סאקטא. ובטנך וארמא
        # EN: the imām shall adjure her regarding this with a grievous oath, and the imām shall say to her: 'May God make you a curse and an oath among your people, by God's making your thigh fall and your belly swell.'
        ("וְהִשְׁבִּיעַ הַכֹּהֵן אֶת-הָאִשָּׁה", "ויחלפהא", "the imām shall adjure her"),
        ("בִּשְׁבֻעַת", "עלי' ד'אלך ימין", "regarding this with a"),
        ("הָאָלָה", "אלחרג", "grievous oath,"),
        ("וְאָמַר הַכֹּהֵן", "ויקול אלאמאם", "and the imām shall say"),
        ("לָאִשָּׁה", "להא", "to her:"),
        ("יִתֵּן", "יגעלך", "'May God make you"),
        ("יְהוָה", "אללה", "a curse"),
        ("אוֹתָךְ לְאָלָה", "מסבה", "and an oath"),
        ("וְלִשְׁבֻעָה", "וימינא", "among your people,"),
        ("בְּתוֹךְ עַמֵּךְ", "פי מא בין קומך", "by God's making"),
        ("בְּתֵת יְהוָה אֶת-יְרֵכֵךְ נֹפֶלֶת וְאֶת-בִּטְנֵךְ צָבָה", "במא יגעל אללה ורכך סאקטא. ובטנך וארמא", "your thigh fall and your belly swell.'"),
    ],
    22: [
        # וּבָאוּ הַמַּיִם הַמְאָרְרִים הָאֵלֶּה בְּמֵעַיִךְ לַצְבּוֹת בֶּטֶן וְלַנְפִּל יָרֵךְ וְאָמְרָה הָאִשָּׁה אָמֵן אָמֵן
        # JA: וד'אלך. אד'א צאר הד'א אלמא אללאען אלי' אמעאך. פירם אלבטן ויסקט אלורך. ותקול אלאמראה אמין אמין
        # EN: And this — when this cursing water enters your bowels, the belly shall swell and the thigh shall fall. And the woman shall say: Amen, amen.
        (None, "וד'אלך", "And this —"),
        ("וּבָאוּ", "אד'א צאר", "when this cursing water enters"),
        ("הַמַּיִם הַמְאָרְרִים הָאֵלֶּה", "הד'א אלמא אללאען", "your bowels,"),
        ("בְּמֵעַיִךְ", "אלי' אמעאך", "the belly"),
        ("לַצְבּוֹת בֶּטֶן", "פירם אלבטן", "shall swell"),
        ("וְלַנְפִּל יָרֵךְ", "ויסקט אלורך", "and the thigh shall fall."),
        ("וְאָמְרָה הָאִשָּׁה", "ותקול אלאמראה", "And the woman shall say:"),
        ("אָמֵן", "אמין", "Amen,"),
        ("אָמֵן", "אמין", "amen."),
    ],
    23: [
        # וְכָתַב אֶת-הָאָלֹת הָאֵלֶּה הַכֹּהֵן--בַּסֵּפֶר וּמָחָה אֶל-מֵי הַמָּרִים
        # JA: ויכתב אלאמאם. הד'ה אללענאת פי כתאב. וימחיה פי אלמא אלמר
        # EN: And the imām shall write these curses in a book, and dissolve it in the bitter water.
        ("וְכָתַב", "ויכתב", "And the imām shall write"),
        ("הַכֹּהֵן", "אלאמאם", "these curses"),
        ("אֶת-הָאָלֹת הָאֵלֶּה", "הד'ה אללענאת", "in a book,"),
        ("בַּסֵּפֶר", "פי כתאב", "and dissolve it"),
        ("וּמָחָה אֶל-מֵי הַמָּרִים", "וימחיה פי אלמא אלמר", "in the bitter water."),
    ],
    24: [
        # וְהִשְׁקָה אֶת-הָאִשָּׁה אֶת-מֵי הַמָּרִים הַמְאָרְרִים וּבָאוּ בָהּ הַמַּיִם הַמְאָרְרִים לְמָרִים
        # JA: ויסקיהא אלמא אלמר אללאען. ויסתחיל פיהא מרא
        # EN: And he shall give her to drink the bitter, cursing water, and it shall turn bitter within her.
        ("וְהִשְׁקָה אֶת-הָאִשָּׁה", "ויסקיהא", "And he shall give her to drink"),
        ("אֶת-מֵי הַמָּרִים", "אלמא אלמר", "the bitter,"),
        ("הַמְאָרְרִים", "אללאען", "cursing water,"),
        ("וּבָאוּ בָהּ הַמַּיִם הַמְאָרְרִים לְמָרִים", "ויסתחיל פיהא מרא", "and it shall turn bitter within her."),
    ],
    25: [
        # וְלָקַח הַכֹּהֵן מִיַּד הָאִשָּׁה אֵת מִנְחַת הַקְּנָאֹת וְהֵנִיף אֶת-הַמִּנְחָה לִפְנֵי יְהוָה וְהִקְרִיב אֹתָהּ אֶל-הַמִּזְבֵּחַ
        # JA: ויאכ'ד' אלאמאם מן ידהא. קרבאן אלג'ירה. ויחרכה בין ידי אללה. ויקדמה אלי' אלמד'בח
        # EN: And the imām shall take the offering of jealousy from her hands, and wave it before God, and bring it forward to the altar.
        ("וְלָקַח הַכֹּהֵן", "ויאכ'ד' אלאמאם", "And the imām shall take"),
        ("מִיַּד הָאִשָּׁה", "מן ידהא", "from her hands"),
        ("אֵת מִנְחַת הַקְּנָאֹת", "קרבאן אלג'ירה", "the offering of jealousy"),
        ("וְהֵנִיף אֶת-הַמִּנְחָה", "ויחרכה", "and wave it"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God,"),
        ("וְהִקְרִיב אֹתָהּ", "ויקדמה", "and bring it forward"),
        ("אֶל-הַמִּזְבֵּחַ", "אלי' אלמד'בח", "to the altar."),
    ],
    26: [
        # וְקָמַץ הַכֹּהֵן מִן-הַמִּנְחָה אֶת-אַזְכָּרָתָהּ וְהִקְטִיר הַמִּזְבֵּחָה וְאַחַר יַשְׁקֶה אֶת-הָאִשָּׁה אֶת-הַמָּיִם
        # JA: ויקבץ' מנהא אלאמאם פיחהא. ויקתרה עלי' אלמד'בח. ובעד ד'אלך יסקיהא אלמא
        # EN: And the imām shall take from it his handful as its memorial portion, and burn it upon the altar; and after that he shall give her the water to drink.
        ("וְקָמַץ הַכֹּהֵן מִן-הַמִּנְחָה", "ויקבץ' מנהא אלאמאם", "And the imām shall take from it"),
        ("אֶת-אַזְכָּרָתָהּ", "פיחהא", "his handful as its memorial portion,"),
        ("וְהִקְטִיר", "ויקתרה", "and burn it"),
        ("הַמִּזְבֵּחָה", "עלי' אלמד'בח", "upon the altar;"),
        ("וְאַחַר", "ובעד ד'אלך", "and after that"),
        ("יַשְׁקֶה אֶת-הָאִשָּׁה אֶת-הַמָּיִם", "יסקיהא אלמא", "he shall give her the water to drink."),
    ],
    27: [
        # וְהִשְׁקָהּ אֶת-הַמַּיִם וְהָיְתָה אִם-נִטְמְאָה וַתִּמְעֹל מַעַל בְּאִישָׁהּ--וּבָאוּ בָהּ הַמַּיִם הַמְאָרְרִים לְמָרִים וְצָבְתָה בִטְנָהּ וְנָפְלָה יְרֵכָהּ וְהָיְתָה הָאִשָּׁה לְאָלָה בְּקֶרֶב עַמָּהּ
        # JA: פאד'י סקאהא אלמא. פאן כאנת קד תנגסת וכ'אנת זוגהא כ'יאנה. אסתחל פיהא מרא. פירם בטנהא. ויסקט ורכהא. וצארת מסבה פי מא בין קומהא
        # EN: And when he has given her the water to drink — if she had defiled herself and betrayed her husband with a betrayal, then bitterness shall take effect within her: her belly shall swell and her thigh shall fall, and she shall become a curse among her people.
        ("וְהִשְׁקָהּ אֶת-הַמַּיִם", "פאד'י סקאהא אלמא", "And when he has given her the water to drink —"),
        ("וְהָיְתָה", "פאן כאנת", "if she had"),
        ("אִם-נִטְמְאָה", "קד תנגסת", "defiled herself"),
        ("וַתִּמְעֹל", "וכ'אנת", "and betrayed"),
        ("מַעַל", "זוגהא", "her husband"),
        ("בְּאִישָׁהּ", "כ'יאנה", "with a betrayal,"),
        ("וּבָאוּ בָהּ הַמַּיִם הַמְאָרְרִים לְמָרִים", "אסתחל פיהא מרא", "then bitterness shall take effect within her:"),
        ("וְצָבְתָה", "פירם", "her belly shall swell"),
        ("בִטְנָהּ", "בטנהא", "and her thigh shall fall,"),
        ("וְנָפְלָה יְרֵכָהּ", "ויסקט ורכהא", "and she shall become"),
        ("וְהָיְתָה הָאִשָּׁה לְאָלָה", "וצארת מסבה", "a curse"),
        ("בְּקֶרֶב עַמָּהּ", "פי מא בין קומהא", "among her people."),
    ],
    28: [
        # וְאִם-לֹא נִטְמְאָה הָאִשָּׁה וּטְהֹרָה הִוא--וְנִקְּתָה וְנִזְרְעָה זָרַע
        # JA: ואן כאנת לם תנתגס. בל הי טאהרה. פברית וחמלת חמלא
        # EN: But if she had not defiled herself, but is pure, then she shall be cleared, and shall conceive a child.
        ("וְאִם-לֹא נִטְמְאָה", "ואן כאנת לם תנתגס", "But if she had not defiled herself,"),
        ("הָאִשָּׁה", "בל הי", "but is"),
        ("וּטְהֹרָה הִוא", "טאהרה", "pure,"),
        ("וְנִקְּתָה", "פברית", "then she shall be cleared,"),
        ("וְנִזְרְעָה", "וחמלת", "and shall conceive"),
        ("זָרַע", "חמלא", "a child."),
    ],
    29: [
        # זֹאת תּוֹרַת הַקְּנָאֹת אֲשֶׁר תִּשְׂטֶה אִשָּׁה תַּחַת אִישָׁהּ וְנִטְמָאָה
        # JA: הד'ה שריעה' אלג'ירה. פי אן תחיד אמראה. ען זוגהא פתנתגס
        # EN: This is the law of jealousy — when a woman goes astray from her husband and defiles herself.
        ("זֹאת", "הד'ה", "This is"),
        ("תּוֹרַת", "שריעה'", "the law of"),
        ("הַקְּנָאֹת", "אלג'ירה", "jealousy —"),
        ("אֲשֶׁר תִּשְׂטֶה", "פי אן תחיד", "when a woman goes astray"),
        ("אִשָּׁה", "אמראה", "from her husband"),
        ("תַּחַת אִישָׁהּ וְנִטְמָאָה", "ען זוגהא פתנתגס", "and defiles herself."),
    ],
    30: [
        # אוֹ אִישׁ אֲשֶׁר תַּעֲבֹר עָלָיו רוּחַ קִנְאָה--וְקִנֵּא אֶת-אִשְׁתּוֹ וְהֶעֱמִיד אֶת-הָאִשָּׁה לִפְנֵי יְהוָה וְעָשָׂה לָהּ הַכֹּהֵן אֵת כָּל-הַתּוֹרָה הַזֹּאת
        # JA: או רג'ל יכ'טר בבאלה. ראי ג'ירה פיג'אר עלי' זוגתה. פליוקפהא בין ידי אללה. ויצנע בהא אלאמאם. גמיע מא פי הד'א אלשריעה
        # EN: Or a man in whose mind a thought of jealousy arises and he is jealous over his wife — he shall station her before God, and the imām shall do to her all that is in this law.
        ("אוֹ", "או", "Or"),
        ("אִישׁ", "רג'ל", "a man"),
        ("אֲשֶׁר תַּעֲבֹר עָלָיו", "יכ'טר בבאלה", "in whose mind"),
        ("רוּחַ קִנְאָה", "ראי ג'ירה", "a thought of jealousy arises"),
        ("וְקִנֵּא", "פיג'אר עלי'", "and he is jealous over"),
        ("אֶת-אִשְׁתּוֹ", "זוגתה", "his wife —"),
        ("וְהֶעֱמִיד אֶת-הָאִשָּׁה", "פליוקפהא", "he shall station her"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God,"),
        ("וְעָשָׂה לָהּ", "ויצנע בהא", "and the imām shall do to her"),
        ("הַכֹּהֵן", "אלאמאם", "all that is in"),
        ("אֵת כָּל-הַתּוֹרָה הַזֹּאת", "גמיע מא פי הד'א אלשריעה", "this law."),
    ],
    31: [
        # וְנִקָּה הָאִישׁ מֵעָו‍ֹן וְהָאִשָּׁה הַהִוא תִּשָּׂא אֶת-עֲו‍ֹנָהּ
        # JA: חתי יברו אלרגל מן אלוזר. ותלך אלאמראה תחמל וזרהא
        # EN: So that the man may be cleared of guilt, and that woman shall bear her guilt.
        ("וְנִקָּה", "חתי יברו", "So that"),
        ("הָאִישׁ", "אלרגל", "the man may be cleared"),
        ("מֵעָו‍ֹן", "מן אלוזר", "of guilt,"),
        ("וְהָאִשָּׁה הַהִוא", "ותלך אלאמראה", "and that woman"),
        ("תִּשָּׂא", "תחמל", "shall bear"),
        ("אֶת-עֲו‍ֹנָהּ", "וזרהא", "her guilt."),
    ],
}

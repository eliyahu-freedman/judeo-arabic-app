"""Hand-authored word-level alignment triples for Bamidbar chapter 15."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: תם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "תם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to"),
        ("אֶל-מֹשֶׁה", "מוסי'", "Moses directly."),
        ("לֵּאמֹר", "תכלימא", ""),
    ],
    2: [
        # HE: דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם כִּי תָבֹאוּ אֶל-אֶרֶץ מוֹשְׁבֹתֵיכֶם אֲשֶׁר אֲנִי נֹתֵן לָכֶם
        # JA: מר בני אסראיל. וקל להם. אד'א דכ'לתם אלי' בלד סכנאכם. אלד'י אנא מעטיכם
        # EN: Command the sons of Israel, and say to them: When you enter the land of your dwelling, which I am giving you,
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel,"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("כִּי תָבֹאוּ", "אד'א דכ'לתם", "When you enter"),
        ("אֶל-אֶרֶץ", "אלי' בלד", "the land of"),
        ("מוֹשְׁבֹתֵיכֶם", "סכנאכם", "your dwelling,"),
        ("אֲשֶׁר", "אלד'י", "which"),
        ("אֲנִי נֹתֵן", "אנא מעטיכם", "I am giving you,"),
    ],
    3: [
        # HE: וַעֲשִׂיתֶם אִשֶּׁה לַיהוָה עֹלָה אוֹ-זֶבַח לְפַלֵּא-נֶדֶר אוֹ בִנְדָבָה אוֹ בְּמֹעֲדֵיכֶם--לַעֲשׂוֹת רֵיחַ נִיחֹחַ לַיהוָה מִן-הַבָּקָר אוֹ מִן-הַצֹּאן
        # JA: פקרבתם קרבאנא ללה צעידה או ד'בחא. תסויג' נד'רא או תברעא. או פי אעיאדכם. וארדתם אן יכון מקבולא מרצ'ייא ללה. מן אלבקר או מן אלג'נם
        # EN: and you offer an offering to God — a burnt offering or a sacrifice, to fulfill a vow or as a freewill gift, or at your festivals — and you intend it to be accepted and pleasing to God, from the cattle or from the flock,
        ("וַעֲשִׂיתֶם", "פקרבתם", "and you offer"),
        ("אִשֶּׁה", "קרבאנא", "an offering"),
        ("לַיהוָה", "ללה", "to God —"),
        ("עֹלָה", "צעידה", "a burnt offering"),
        ("אוֹ-זֶבַח", "או ד'בחא", "or a sacrifice,"),
        ("לְפַלֵּא-נֶדֶר", "תסויג' נד'רא", "to fulfill a vow"),
        ("אוֹ בִנְדָבָה", "או תברעא", "or as a freewill gift,"),
        ("אוֹ בְּמֹעֲדֵיכֶם", "או פי אעיאדכם", "or at your festivals —"),
        ("לַעֲשׂוֹת רֵיחַ נִיחֹחַ", "וארדתם אן יכון מקבולא מרצ'ייא", "and you intend it to be accepted and pleasing"),
        ("לַיהוָה", "ללה", "to God,"),
        ("מִן-הַבָּקָר", "מן אלבקר", "from the cattle"),
        ("אוֹ מִן-הַצֹּאן", "או מן אלג'נם", "or from the flock,"),
    ],
    4: [
        # HE: וְהִקְרִיב הַמַּקְרִיב קָרְבָּנוֹ לַיהוָה--מִנְחָה סֹלֶת עִשָּׂרוֹן בָּלוּל בִּרְבִעִית הַהִין שָׁמֶן
        # JA: פיקרב צאחב ד'אלך אלקרבאן ללה. מעה מן אלבר עשרא סמדא. מלתות ברבע קסט דהן
        # EN: then the one who brings that offering shall bring with it, from grain, a tenth of fine flour mixed with a quarter of a qist of oil;
        ("וְהִקְרִיב הַמַּקְרִיב", "פיקרב צאחב", "then the one who brings"),
        ("קָרְבָּנוֹ", "ד'אלך אלקרבאן", "that offering"),
        ("לַיהוָה", "ללה", "shall bring with it,"),
        ("מִנְחָה", "מעה מן אלבר", "from grain,"),
        ("סֹלֶת עִשָּׂרוֹן", "עשרא סמדא", "a tenth of fine flour"),
        ("בָּלוּל", "מלתות", "mixed"),
        ("בִּרְבִעִית הַהִין", "ברבע קסט", "with a quarter of a qist of"),
        ("שָׁמֶן", "דהן", "oil;"),
    ],
    5: [
        # HE: וְיַיִן לַנֶּסֶךְ רְבִיעִית הַהִין תַּעֲשֶׂה עַל-הָעֹלָה אוֹ לַזָּבַח--לַכֶּבֶשׂ הָאֶחָד
        # JA: וכ'מר לאלמזאג רבע קסט. תצנעה מע אלצעידה או מע אלד'בח. לאלחמל אלואחד
        # EN: and wine for the libation — a quarter of a qist — you shall make it with the burnt offering or with the sacrifice, for the one lamb.
        ("וְיַיִן", "וכ'מר", "and wine"),
        ("לַנֶּסֶךְ", "לאלמזאג", "for the libation —"),
        ("רְבִיעִית הַהִין", "רבע קסט", "a quarter of a qist —"),
        ("תַּעֲשֶׂה", "תצנעה", "you shall make it"),
        ("עַל-הָעֹלָה", "מע אלצעידה", "with the burnt offering"),
        ("אוֹ לַזָּבַח", "או מע אלד'בח", "or with the sacrifice,"),
        ("לַכֶּבֶשׂ", "לאלחמל", "for the one"),
        ("הָאֶחָד", "אלואחד", "lamb."),
    ],
    6: [
        # HE: אוֹ לָאַיִל תַּעֲשֶׂה מִנְחָה סֹלֶת שְׁנֵי עֶשְׂרֹנִים בְּלוּלָה בַשֶּׁמֶן שְׁלִשִׁית הַהִין
        # JA: ולאלכבש תקרב מן אלבר עשרין סמד. מלתות בת'לת' קסט דהן
        # EN: And for the ram you shall bring, from grain, two tenths of fine flour mixed with a third of a qist of oil;
        ("אוֹ לָאַיִל", "ולאלכבש", "And for the ram"),
        ("תַּעֲשֶׂה", "תקרב", "you shall bring,"),
        ("מִנְחָה", "מן אלבר", "from grain,"),
        ("סֹלֶת שְׁנֵי עֶשְׂרֹנִים", "עשרין סמד", "two tenths of fine flour"),
        ("בְּלוּלָה", "מלתות", "mixed"),
        ("בַשֶּׁמֶן שְׁלִשִׁית הַהִין", "בת'לת' קסט דהן", "with a third of a qist of oil;"),
    ],
    7: [
        # HE: וְיַיִן לַנֶּסֶךְ שְׁלִשִׁית הַהִין--תַּקְרִיב רֵיחַ-נִיחֹחַ לַיהוָה
        # JA: וכ'מר לאלמזאג ת'לת' קסט. תקרבה מרצ'י מקבול ללה
        # EN: and wine for the libation — a third of a qist — you shall offer it, accepted and pleasing to God.
        ("וְיַיִן", "וכ'מר", "and wine"),
        ("לַנֶּסֶךְ", "לאלמזאג", "for the libation —"),
        ("שְׁלִשִׁית הַהִין", "ת'לת' קסט", "a third of a qist —"),
        ("תַּקְרִיב", "תקרבה", "you shall offer it,"),
        ("רֵיחַ-נִיחֹחַ", "מרצ'י", "accepted"),
        ("לַיהוָה", "מקבול ללה", "and pleasing to God."),
    ],
    8: [
        # HE: וְכִי-תַעֲשֶׂה בֶן-בָּקָר עֹלָה אוֹ-זָבַח לְפַלֵּא-נֶדֶר אוֹ-שְׁלָמִים לַיהוָה
        # JA: ואד'א צנעת מן אלבקר צעידה או ד'בחא. תסויג נד'רא או סלאמה ללה
        # EN: And when you make from the cattle a burnt offering or a sacrifice, to fulfill a vow or as a peace-offering to God,
        ("וְכִי-תַעֲשֶׂה", "ואד'א צנעת", "And when you make"),
        ("בֶן-בָּקָר", "מן אלבקר", "from the cattle"),
        ("עֹלָה", "צעידה", "a burnt offering"),
        ("אוֹ-זָבַח", "או ד'בחא", "or a sacrifice,"),
        ("לְפַלֵּא-נֶדֶר", "תסויג נד'רא", "to fulfill a vow"),
        ("אוֹ-שְׁלָמִים", "או סלאמה", "or as a peace-offering"),
        ("לַיהוָה", "ללה", "to God,"),
    ],
    9: [
        # HE: וְהִקְרִיב עַל-בֶּן-הַבָּקָר מִנְחָה סֹלֶת שְׁלֹשָׁה עֶשְׂרֹנִים בָּלוּל בַּשֶּׁמֶן חֲצִי הַהִין
        # JA: פיקרב מעה מן אלבר. ת'לאת'ה' עשור סמד. מלתות בנצף קסט דהן
        # EN: then he shall bring with it, from grain, three tenths of fine flour mixed with half a qist of oil;
        ("וְהִקְרִיב", "פיקרב", "then he shall bring"),
        ("עַל-בֶּן-הַבָּקָר", "מעה", "with it,"),
        ("מִנְחָה", "מן אלבר", "from grain,"),
        ("סֹלֶת שְׁלֹשָׁה עֶשְׂרֹנִים", "ת'לאת'ה' עשור סמד", "three tenths of fine flour"),
        ("בָּלוּל", "מלתות", "mixed"),
        ("בַּשֶּׁמֶן חֲצִי הַהִין", "בנצף קסט דהן", "with half a qist of oil;"),
    ],
    10: [
        # HE: וְיַיִן תַּקְרִיב לַנֶּסֶךְ חֲצִי הַהִין--אִשֵּׁה רֵיחַ-נִיחֹחַ לַיהוָה
        # JA: וכ'מר קרבה לאלמזאג נצף קסט. מקבול מרצ'י ללה
        # EN: and wine — offer it for the libation — half a qist, accepted and pleasing to God.
        ("וְיַיִן", "וכ'מר", "and wine —"),
        ("תַּקְרִיב", "קרבה", "offer it"),
        ("לַנֶּסֶךְ", "לאלמזאג", "for the libation —"),
        ("חֲצִי הַהִין", "נצף קסט", "half a qist,"),
        ("אִשֵּׁה רֵיחַ-נִיחֹחַ", "מקבול", "accepted"),
        ("לַיהוָה", "מרצ'י ללה", "and pleasing to God."),
    ],
    11: [
        # HE: כָּכָה יֵעָשֶׂה לַשּׁוֹר הָאֶחָד אוֹ לָאַיִל הָאֶחָד אוֹ-לַשֶּׂה בַכְּבָשִׂים אוֹ בָעִזִּים
        # JA: כד'אך יצנע. מע כל רת'. ומע כל כבש. ומע כל ראס מן אלצ'אן או מן אלמאעז
        # EN: So shall it be done with every ox, and with every ram, and with every head from the sheep or from the goats.
        ("כָּכָה יֵעָשֶׂה", "כד'אך יצנע", "So shall it be done"),
        ("לַשּׁוֹר הָאֶחָד", "מע כל רת'", "with every ox,"),
        ("אוֹ לָאַיִל הָאֶחָד", "ומע כל כבש", "and with every ram,"),
        ("אוֹ-לַשֶּׂה בַכְּבָשִׂים", "ומע כל ראס", "and with every head"),
        ("אוֹ בָעִזִּים", "מן אלצ'אן או מן אלמאעז", "from the sheep or from the goats."),
    ],
    12: [
        # HE: כַּמִּסְפָּר אֲשֶׁר תַּעֲשׂוּ--כָּכָה תַּעֲשׂוּ לָאֶחָד כְּמִסְפָּרָם
        # JA: בחסב אחצא מא תקרבון מנהא. כד'אך תצנעו מע כל ואחד מן אלמחציין
        # EN: According to the count of what you offer of them, so shall you do with each one of those counted.
        ("כַּמִּסְפָּר", "בחסב אחצא", "According to the count of"),
        ("אֲשֶׁר תַּעֲשׂוּ", "מא תקרבון מנהא", "what you offer of them,"),
        ("כָּכָה תַּעֲשׂוּ", "כד'אך תצנעו", "so shall you do"),
        ("לָאֶחָד", "מע כל ואחד", "with each one of"),
        ("כְּמִסְפָּרָם", "מן אלמחציין", "those counted."),
    ],
    13: [
        # HE: כָּל-הָאֶזְרָח יַעֲשֶׂה-כָּכָה אֶת-אֵלֶּה לְהַקְרִיב אִשֵּׁה רֵיחַ-נִיחֹחַ לַיהוָה
        # JA: כד'א יצנע כל צריח. אד'א קרב קרבאנא מקבולא מרצ'ייא ללה
        # EN: So shall every native-born do, when he brings an offering accepted and pleasing to God.
        ("כָּל-הָאֶזְרָח", "כל צריח", "every native-born do,"),
        ("יַעֲשֶׂה-כָּכָה", "כד'א יצנע", "So shall"),
        ("לְהַקְרִיב", "אד'א קרב", "when he brings"),
        ("אִשֵּׁה", "קרבאנא", "an offering"),
        ("רֵיחַ-נִיחֹחַ", "מקבולא", "accepted"),
        ("לַיהוָה", "מרצ'ייא ללה", "and pleasing to God."),
    ],
    14: [
        # HE: וְכִי-יָגוּר אִתְּכֶם גֵּר אוֹ אֲשֶׁר-בְּתוֹכְכֶם לְדֹרֹתֵיכֶם וְעָשָׂה אִשֵּׁה רֵיחַ-נִיחֹחַ לַיהוָה--כַּאֲשֶׁר תַּעֲשׂוּ כֵּן יַעֲשֶׂה
        # JA: ואי דכ'יל דכ'ל מעכם. או סכן פי מא בינכם עלי' מר אגיאלכם. פעמל קרבאנא. ואראד אן יכון מקבול מרצ'י ללה. פכמא תצנעון כדאך יצנע
        # EN: And any sojourner who has come among you, or who has dwelt in your midst throughout the passing of your generations, and has made an offering and intended it to be accepted and pleasing to God — just as you do, so shall he do.
        ("וְכִי-יָגוּר", "ואי דכ'יל דכ'ל", "And any sojourner who has come"),
        ("אִתְּכֶם גֵּר", "מעכם", "among you,"),
        ("אוֹ אֲשֶׁר-בְּתוֹכְכֶם", "או סכן פי מא בינכם", "or who has dwelt in your midst"),
        ("לְדֹרֹתֵיכֶם", "עלי' מר אגיאלכם", "throughout the passing of your generations,"),
        ("וְעָשָׂה אִשֵּׁה", "פעמל קרבאנא", "and has made an offering"),
        ("רֵיחַ-נִיחֹחַ", "ואראד אן יכון מקבול מרצ'י", "and intended it to be accepted and pleasing"),
        ("לַיהוָה", "ללה", "to God —"),
        ("כַּאֲשֶׁר תַּעֲשׂוּ", "פכמא תצנעון", "just as you do,"),
        ("כֵּן יַעֲשֶׂה", "כדאך יצנע", "so shall he do."),
    ],
    15: [
        # HE: הַקָּהָל חֻקָּה אַחַת לָכֶם וְלַגֵּר הַגָּר חֻקַּת עוֹלָם לְדֹרֹתֵיכֶם כָּכֶם כַּגֵּר יִהְיֶה לִפְנֵי יְהוָה
        # JA: יא אייה' אלגוק רסם ואחד. לכם ולאלג'ריב אלדכ'יל. רסם אלדהר עלי' מר אגיאלכם. כמא אן אלג'ריב מת'לכם בין ידי אללה
        # EN: O assembly! One ordinance for you and for the stranger who has come in — an eternal ordinance throughout the passing of your generations, for the stranger is as you are before God.
        ("הַקָּהָל", "יא אייה' אלגוק", "O assembly!"),
        ("חֻקָּה אַחַת", "רסם ואחד", "One ordinance"),
        ("לָכֶם", "לכם", "for you"),
        ("וְלַגֵּר הַגָּר", "ולאלג'ריב אלדכ'יל", "and for the stranger who has come in —"),
        ("חֻקַּת עוֹלָם", "רסם אלדהר", "an eternal ordinance"),
        ("לְדֹרֹתֵיכֶם", "עלי' מר אגיאלכם", "throughout the passing of your generations,"),
        ("כָּכֶם כַּגֵּר", "כמא אן אלג'ריב מת'לכם", "for the stranger is as you are"),
        ("יִהְיֶה לִפְנֵי יְהוָה", "בין ידי אללה", "before God."),
    ],
    16: [
        # HE: תּוֹרָה אַחַת וּמִשְׁפָּט אֶחָד יִהְיֶה לָכֶם וְלַגֵּר הַגָּר אִתְּכֶם
        # JA: כד'אך שריעה ואחדה. וחכם ואחד יכון לכם. ולאלג'ריב אלדכ'יל פי מא בינכם
        # EN: So likewise: one law and one ruling shall be for you and for the stranger who has come in among you.
        ("תּוֹרָה", "כד'אך שריעה", "So likewise: one law"),
        ("אַחַת", "ואחדה", ""),
        ("וּמִשְׁפָּט אֶחָד", "וחכם ואחד", "and one ruling"),
        ("יִהְיֶה לָכֶם", "יכון לכם", "shall be for you"),
        ("וְלַגֵּר הַגָּר", "ולאלג'ריב אלדכ'יל", "and for the stranger who has come in"),
        ("אִתְּכֶם", "פי מא בינכם", "among you."),
    ],
    17: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to"),
        ("אֶל-מֹשֶׁה", "מוסי'", "Moses directly."),
        ("לֵּאמֹר", "תכלימא", ""),
    ],
    18: [
        # HE: דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם בְּבֹאֲכֶם אֶל-הָאָרֶץ אֲשֶׁר אֲנִי מֵבִיא אֶתְכֶם שָׁמָּה
        # JA: מר בני אסראיל. וקל להם. אד'א דכ'לתם אלי' אלבלד. אלד'י אנא מדכ'לכם אלי' ת'ם
        # EN: Command the sons of Israel, and say to them: When you enter the land to which I am bringing you there,
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel,"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("בְּבֹאֲכֶם", "אד'א דכ'לתם", "When you enter"),
        ("אֶל-הָאָרֶץ", "אלי' אלבלד", "the land"),
        ("אֲשֶׁר", "אלד'י", "to which"),
        ("אֲנִי מֵבִיא", "אנא מדכ'לכם", "I am bringing you"),
        ("אֶתְכֶם שָׁמָּה", "אלי' ת'ם", "there,"),
    ],
    19: [
        # HE: וְהָיָה בַּאֲכָלְכֶם מִלֶּחֶם הָאָרֶץ--תָּרִימוּ תְרוּמָה לַיהוָה
        # JA: פמתא מא אכלתם מן טעאם אלבלד. פארפעו רפיעה ללה
        # EN: then whenever you eat of the food of the land, raise up a heave-offering to God.
        ("וְהָיָה", "פמתא מא", "then whenever"),
        ("בַּאֲכָלְכֶם", "אכלתם", "you eat"),
        ("מִלֶּחֶם", "מן טעאם", "of the food of"),
        ("הָאָרֶץ", "אלבלד", "the land,"),
        ("תָּרִימוּ", "פארפעו", "raise up"),
        ("תְרוּמָה", "רפיעה", "a heave-offering"),
        ("לַיהוָה", "ללה", "to God."),
    ],
    20: [
        # HE: רֵאשִׁית עֲרִסֹתֵכֶם--חַלָּה תָּרִימוּ תְרוּמָה כִּתְרוּמַת גֹּרֶן כֵּן תָּרִימוּ אֹתָהּ
        # JA: אוול עגינכם. גרדקה תרפעוהא רפיעה. כרפיעה' אלבד'אר. כד'אך תרפעונהא
        # EN: The first of your dough — a loaf-cake you shall raise up as a heave-offering, like the heave-offering of the threshing-floor; so shall you raise it up.
        ("רֵאשִׁית", "אוול", "The first of"),
        ("עֲרִסֹתֵכֶם", "עגינכם", "your dough —"),
        ("חַלָּה", "גרדקה", "a loaf-cake"),
        ("תָּרִימוּ", "תרפעוהא", "you shall raise up"),
        ("תְרוּמָה", "רפיעה", "as a heave-offering,"),
        ("כִּתְרוּמַת", "כרפיעה'", "like the heave-offering of"),
        ("גֹּרֶן", "אלבד'אר", "the threshing-floor;"),
        ("כֵּן תָּרִימוּ אֹתָהּ", "כד'אך תרפעונהא", "so shall you raise it up."),
    ],
    21: [
        # HE: מֵרֵאשִׁית עֲרִסֹתֵיכֶם תִּתְּנוּ לַיהוָה תְּרוּמָה--לְדֹרֹתֵיכֶם
        # JA: וכד'אלך אוול עגינכם. תגעלו ללה רפיעה. עלי' מר אגיאלכם
        # EN: And likewise, the first of your dough you shall make for God a heave-offering, throughout the passing of your generations.
        ("מֵרֵאשִׁית", "וכד'אלך אוול", "And likewise, the first of"),
        ("עֲרִסֹתֵיכֶם", "עגינכם", "your dough"),
        ("תִּתְּנוּ", "תגעלו", "you shall make"),
        ("לַיהוָה", "ללה", "for God"),
        ("תְּרוּמָה", "רפיעה", "a heave-offering,"),
        ("לְדֹרֹתֵיכֶם", "עלי' מר אגיאלכם", "throughout the passing of your generations."),
    ],
    22: [
        # HE: וְכִי תִשְׁגּוּ--וְלֹא תַעֲשׂוּ אֵת כָּל-הַמִּצְו‍ֹת הָאֵלֶּה אֲשֶׁר-דִּבֶּר יְהוָה אֶל-מֹשֶׁה
        # JA: ואד'י סהיתם. ולם תעמלו גמיע הד'ה אלוצאיא. אלד'י אמר אללה בהא מוסי'
        # EN: And if you have erred, and have not carried out all these commandments which God commanded Moses —
        ("וְכִי תִשְׁגּוּ", "ואד'י סהיתם", "And if you have erred,"),
        ("וְלֹא תַעֲשׂוּ", "ולם תעמלו", "and have not carried out"),
        ("אֵת כָּל-הַמִּצְו‍ֹת", "גמיע הד'ה אלוצאיא", "all these commandments"),
        ("אֲשֶׁר-דִּבֶּר", "אלד'י אמר", "which God commanded"),
        ("יְהוָה", "אללה", ""),
        ("אֶל-מֹשֶׁה", "בהא מוסי'", "Moses —"),
    ],
    23: [
        # HE: אֵת כָּל-אֲשֶׁר צִוָּה יְהוָה אֲלֵיכֶם בְּיַד-מֹשֶׁה מִן-הַיּוֹם אֲשֶׁר צִוָּה יְהוָה וָהָלְאָה--לְדֹרֹתֵיכֶם
        # JA: מת'ל גמיע מא אמרכם אללה בה עלי' יד מוסי'. מן יום אבתדא באלאמר. והלם עלי' מר אגיאלכם
        # EN: like all that God commanded you by the hand of Moses, from the day He began the command, and onward throughout the passing of your generations —
        ("אֵת כָּל-אֲשֶׁר", "מת'ל גמיע מא", "like all that"),
        ("צִוָּה יְהוָה", "אמרכם אללה", "God commanded you"),
        ("אֲלֵיכֶם בְּיַד-מֹשֶׁה", "בה עלי' יד מוסי'", "by the hand of Moses,"),
        ("מִן-הַיּוֹם", "מן יום", "from the day"),
        ("אֲשֶׁר צִוָּה יְהוָה", "אבתדא באלאמר", "He began the command,"),
        ("וָהָלְאָה", "והלם", "and onward"),
        ("לְדֹרֹתֵיכֶם", "עלי' מר אגיאלכם", "throughout the passing of your generations —"),
    ],
    24: [
        # HE: וְהָיָה אִם מֵעֵינֵי הָעֵדָה נֶעֶשְׂתָה לִשְׁגָגָה וְעָשׂוּ כָל-הָעֵדָה פַּר בֶּן-בָּקָר אֶחָד לְעֹלָה לְרֵיחַ נִיחֹחַ לַיהוָה וּמִנְחָתוֹ וְנִסְכּוֹ כַּמִּשְׁפָּט וּשְׂעִיר-עִזִּים אֶחָד לְחַטָּת
        # JA: פאן כאן אלסהו ען עיון אלגמאעה. פליצנעו רת'א מן אלבקר. צעידה מקבולא מרצ'ייא ללה. ומעה בר ומזאג כמא יגב. ועתוד מן אלמאעז לאלד'כוה
        # EN: then if the error was away from the eyes of the assembly, they shall make a bull from the cattle — a burnt offering, accepted and pleasing to God — and with it grain and libation as required, and a he-goat from the goats for the purification-offering.
        ("וְהָיָה אִם", "פאן כאן", "then if"),
        ("מֵעֵינֵי הָעֵדָה", "אלסהו ען עיון אלגמאעה", "the error was away from the eyes of the assembly,"),
        ("וְעָשׂוּ כָל-הָעֵדָה", "פליצנעו", "they shall make"),
        ("פַּר בֶּן-בָּקָר", "רת'א מן אלבקר", "a bull from the cattle —"),
        ("לְעֹלָה", "צעידה", "a burnt offering,"),
        ("לְרֵיחַ נִיחֹחַ", "מקבולא מרצ'ייא", "accepted and pleasing"),
        ("לַיהוָה", "ללה", "to God —"),
        ("וּמִנְחָתוֹ", "ומעה בר", "and with it grain"),
        ("וְנִסְכּוֹ", "ומזאג", "and libation"),
        ("כַּמִּשְׁפָּט", "כמא יגב", "as required,"),
        ("וּשְׂעִיר-עִזִּים", "ועתוד מן אלמאעז", "and a he-goat from the goats"),
        ("לְחַטָּת", "לאלד'כוה", "for the purification-offering."),
    ],
    25: [
        # HE: וְכִפֶּר הַכֹּהֵן עַל-כָּל-עֲדַת בְּנֵי יִשְׂרָאֵל--וְנִסְלַח לָהֶם כִּי-שְׁגָגָה הִוא--וְהֵם הֵבִיאוּ אֶת-קָרְבָּנָם אִשֶּׁה לַיהוָה וְחַטָּאתָם לִפְנֵי יְהוָה עַל-שִׁגְגָתָם
        # JA: ויסתג'פר להם. אד' ד'אלך סהו. והם פאתו בצעידתהם קרבאנא ללה. וד'כותהם עלי' סהותהם
        # EN: And he shall seek forgiveness for them, since that was an error, and they have brought their burnt offering as an offering to God, and their purification-offering for their lapse.
        ("וְכִפֶּר הַכֹּהֵן", "ויסתג'פר", "And he shall seek forgiveness"),
        ("עַל-כָּל-עֲדַת בְּנֵי יִשְׂרָאֵל", "להם", "for them,"),
        ("כִּי-שְׁגָגָה הִוא", "אד' ד'אלך סהו", "since that was an error,"),
        ("וְהֵם הֵבִיאוּ", "והם פאתו", "and they have brought"),
        ("אֶת-קָרְבָּנָם אִשֶּׁה", "בצעידתהם קרבאנא", "their burnt offering as an offering"),
        ("לַיהוָה", "ללה", "to God,"),
        ("וְחַטָּאתָם", "וד'כותהם", "and their purification-offering"),
        ("עַל-שִׁגְגָתָם", "עלי' סהותהם", "for their lapse."),
    ],
    26: [
        # HE: וְנִסְלַח לְכָל-עֲדַת בְּנֵי יִשְׂרָאֵל וְלַגֵּר הַגָּר בְּתוֹכָם כִּי לְכָל-הָעָם בִּשְׁגָגָה
        # JA: פיג'פר לגמאעה' בני אסראיל. ולאלג'ריב אלדכ'יל פי מא בינהם. אד' גמיע אלקום עלי' סהו
        # EN: And it shall be forgiven to the assembly of the sons of Israel and to the stranger who has come in among them, since all the people acted in error.
        ("וְנִסְלַח", "פיג'פר", "And it shall be forgiven"),
        ("לְכָל-עֲדַת", "לגמאעה'", "to the assembly of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("וְלַגֵּר הַגָּר", "ולאלג'ריב אלדכ'יל", "and to the stranger who has come in"),
        ("בְּתוֹכָם", "פי מא בינהם", "among them,"),
        ("כִּי לְכָל-הָעָם", "אד' גמיע אלקום", "since all the people"),
        ("בִּשְׁגָגָה", "עלי' סהו", "acted in error."),
    ],
    27: [
        # HE: וְאִם-נֶפֶשׁ אַחַת תֶּחֱטָא בִשְׁגָגָה--וְהִקְרִיבָה עֵז בַּת-שְׁנָתָהּ לְחַטָּאת
        # JA: ואן אכ'טא אנסאן ואחד כד'אלך סהוא. פליקרב שאה אבנה' סנתהא לאלד'כוה
        # EN: And if a single person errs likewise, in error, he shall offer a ewe-lamb in its first year for the purification-offering.
        ("וְאִם-נֶפֶשׁ אַחַת", "ואן אכ'טא אנסאן ואחד", "And if a single person errs"),
        ("תֶּחֱטָא בִשְׁגָגָה", "כד'אלך סהוא", "likewise, in error,"),
        ("וְהִקְרִיבָה", "פליקרב", "he shall offer"),
        ("עֵז", "שאה", "a ewe-lamb"),
        ("בַּת-שְׁנָתָהּ", "אבנה' סנתהא", "in its first year"),
        ("לְחַטָּאת", "לאלד'כוה", "for the purification-offering."),
    ],
    28: [
        # HE: וְכִפֶּר הַכֹּהֵן עַל-הַנֶּפֶשׁ הַשֹּׁגֶגֶת בְּחֶטְאָה בִשְׁגָגָה--לִפְנֵי יְהוָה לְכַפֵּר עָלָיו וְנִסְלַח לוֹ
        # JA: פיסתג'פר אלאמאם. ען ד'אלך אלאנסאן אלסאהי. עלי' מא אכ'טא סהוא בין ידי אללה. ויג'פר לה ויצפח ענה
        # EN: And the imām shall seek forgiveness on behalf of that erring person, for what he erred in error before God; and it shall be forgiven him and pardoned from him.
        ("וְכִפֶּר הַכֹּהֵן", "פיסתג'פר אלאמאם", "And the imām shall seek forgiveness"),
        ("עַל-הַנֶּפֶשׁ הַשֹּׁגֶגֶת", "ען ד'אלך אלאנסאן אלסאהי", "on behalf of that erring person,"),
        ("בְּחֶטְאָה בִשְׁגָגָה", "עלי' מא אכ'טא סהוא", "for what he erred in error"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God;"),
        ("לְכַפֵּר עָלָיו", "ויג'פר לה", "and it shall be forgiven him"),
        ("וְנִסְלַח לוֹ", "ויצפח ענה", "and pardoned from him."),
    ],
    29: [
        # HE: הָאֶזְרָח בִּבְנֵי יִשְׂרָאֵל וְלַגֵּר הַגָּר בְּתוֹכָם--תּוֹרָה אַחַת יִהְיֶה לָכֶם לָעֹשֶׂה בִּשְׁגָגָה
        # JA: אלצריח מן בני אסראיל. ואלג'ריב אלדכ'יל פי מא בינהם. שריעה ואחדה תכון לכם. למן יכ'טי סהוא
        # EN: For the native-born among the sons of Israel, and the stranger who has come in among them — one law shall be for you, for whoever errs in error.
        ("הָאֶזְרָח", "אלצריח", "For the native-born"),
        ("בִּבְנֵי יִשְׂרָאֵל", "מן בני אסראיל", "among the sons of Israel,"),
        ("וְלַגֵּר הַגָּר", "ואלג'ריב אלדכ'יל", "and the stranger who has come in"),
        ("בְּתוֹכָם", "פי מא בינהם", "among them —"),
        ("תּוֹרָה אַחַת", "שריעה ואחדה", "one law"),
        ("יִהְיֶה לָכֶם", "תכון לכם", "shall be for you,"),
        ("לָעֹשֶׂה בִּשְׁגָגָה", "למן יכ'טי סהוא", "for whoever errs in error."),
    ],
    30: [
        # HE: וְהַנֶּפֶשׁ אֲשֶׁר-תַּעֲשֶׂה בְּיָד רָמָה מִן-הָאֶזְרָח וּמִן-הַגֵּר--אֶת-יְהוָה הוּא מְגַדֵּף וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא מִקֶּרֶב עַמָּהּ
        # JA: ואי אנסאן צנע ד'אלך ביד רפיעה. מן אלצריח ואלדכ'יל. פהו קאד'ף רבה. ינקטע ד'אלך אלאנסאן מן בין קומה
        # EN: But any person who does that with a high hand, whether native-born or sojourner — he is a blasphemer against his Lord; that person shall be cut off from among his people.
        ("וְהַנֶּפֶשׁ", "ואי אנסאן", "But any person"),
        ("אֲשֶׁר-תַּעֲשֶׂה", "צנע ד'אלך", "who does that"),
        ("בְּיָד רָמָה", "ביד רפיעה", "with a high hand,"),
        ("מִן-הָאֶזְרָח", "מן אלצריח", "whether native-born"),
        ("וּמִן-הַגֵּר", "ואלדכ'יל", "or sojourner —"),
        ("אֶת-יְהוָה הוּא מְגַדֵּף", "פהו קאד'ף רבה", "he is a blasphemer against his Lord;"),
        ("וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא", "ינקטע ד'אלך אלאנסאן", "that person shall be cut off"),
        ("מִקֶּרֶב עַמָּהּ", "מן בין קומה", "from among his people."),
    ],
    31: [
        # HE: כִּי דְבַר-יְהוָה בָּזָה וְאֶת-מִצְוָתוֹ הֵפַר הִכָּרֵת תִּכָּרֵת הַנֶּפֶשׁ הַהִוא עֲו‍ֹנָה בָהּ
        # JA: למא אזרא בכלאם אללה. ופסך' עהדה. פינקטע ד'אלך אלאנסאן אנקטאעא. ווזרה עליה
        # EN: Because he has despised the word of God and broken His covenant — that person shall surely be cut off; his iniquity is upon him.
        ("כִּי", "למא", "Because"),
        ("דְבַר-יְהוָה בָּזָה", "אזרא בכלאם אללה", "he has despised the word of God"),
        ("וְאֶת-מִצְוָתוֹ הֵפַר", "ופסך' עהדה", "and broken His covenant —"),
        ("הִכָּרֵת תִּכָּרֵת הַנֶּפֶשׁ הַהִוא", "פינקטע ד'אלך אלאנסאן אנקטאעא", "that person shall surely be cut off;"),
        ("עֲו‍ֹנָה בָהּ", "ווזרה עליה", "his iniquity is upon him."),
    ],
    32: [
        # HE: וַיִּהְיוּ בְנֵי-יִשְׂרָאֵל בַּמִּדְבָּר וַיִּמְצְאוּ אִישׁ מְקֹשֵׁשׁ עֵצִים--בְּיוֹם הַשַּׁבָּת
        # JA: ולמא אקאם בני אסראיל פי אלבר. פוגדו רגלא. יחתטב חטבא פי יום אלסבת
        # EN: And when the sons of Israel were dwelling in the wilderness, they found a man gathering wood for himself on the Sabbath day.
        ("וַיִּהְיוּ", "ולמא אקאם", "And when"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("בַּמִּדְבָּר", "פי אלבר", "were dwelling in the wilderness,"),
        ("וַיִּמְצְאוּ", "פוגדו", "they found"),
        ("אִישׁ", "רגלא", "a man"),
        ("מְקֹשֵׁשׁ עֵצִים", "יחתטב חטבא", "gathering wood for himself"),
        ("בְּיוֹם הַשַּׁבָּת", "פי יום אלסבת", "on the Sabbath day."),
    ],
    33: [
        # HE: וַיַּקְרִיבוּ אֹתוֹ הַמֹּצְאִים אֹתוֹ מְקֹשֵׁשׁ עֵצִים--אֶל-מֹשֶׁה וְאֶל-אַהֲרֹן וְאֶל כָּל-הָעֵדָה
        # JA: פקדמוה אלד'י וגדוה יחתטב חטבא. אלי' מוסי' והרון. וסאיר אלגמאעה
        # EN: And those who found him gathering wood brought him to Moses and Aaron, and the rest of the assembly.
        ("וַיַּקְרִיבוּ אֹתוֹ", "פקדמוה", "And those who found him gathering wood brought him"),
        ("הַמֹּצְאִים אֹתוֹ", "אלד'י וגדוה", ""),
        ("מְקֹשֵׁשׁ עֵצִים", "יחתטב חטבא", ""),
        ("אֶל-מֹשֶׁה", "אלי' מוסי'", "to Moses"),
        ("וְאֶל-אַהֲרֹן", "והרון", "and Aaron,"),
        ("וְאֶל כָּל-הָעֵדָה", "וסאיר אלגמאעה", "and the rest of the assembly."),
    ],
    34: [
        # HE: וַיַּנִּיחוּ אֹתוֹ בַּמִּשְׁמָר כִּי לֹא פֹרַשׁ מַה-יֵּעָשֶׂה לוֹ
        # JA: ווצ'עוה פי אלחבס. לאנה לם יפסר להם מא יצנע בה
        # EN: And they placed him in custody, because it had not been made clear to them what should be done with him.
        ("וַיַּנִּיחוּ אֹתוֹ", "ווצ'עוה", "And they placed him"),
        ("בַּמִּשְׁמָר", "פי אלחבס", "in custody,"),
        ("כִּי לֹא פֹרַשׁ", "לאנה לם יפסר להם", "because it had not been made clear to them"),
        ("מַה-יֵּעָשֶׂה", "מא יצנע", "what should be done"),
        ("לוֹ", "בה", "with him."),
    ],
    35: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה מוֹת יוּמַת הָאִישׁ רָגוֹם אֹתוֹ בָאֲבָנִים כָּל-הָעֵדָה מִחוּץ לַמַּחֲנֶה
        # JA: פקאל אללה למוסי. יקתל אלרגל קתלא. וד'אלך אן ירגמוה באלחגארה גמיע אלגמאעה. כ'ארג אלעסכר
        # EN: And God said to Moses: The man shall surely be put to death — and that by the whole assembly stoning him with stones, outside the camp.
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי", "to Moses:"),
        ("מוֹת יוּמַת", "יקתל", "The man shall surely be put to death —"),
        ("הָאִישׁ", "אלרגל קתלא", ""),
        ("רָגוֹם אֹתוֹ", "וד'אלך אן ירגמוה", "and that by"),
        ("בָאֲבָנִים", "באלחגארה", "stoning him with stones,"),
        ("כָּל-הָעֵדָה", "גמיע אלגמאעה", "the whole assembly"),
        ("מִחוּץ לַמַּחֲנֶה", "כ'ארג אלעסכר", "outside the camp."),
    ],
    36: [
        # HE: וַיֹּצִיאוּ אֹתוֹ כָּל-הָעֵדָה אֶל-מִחוּץ לַמַּחֲנֶה וַיִּרְגְּמוּ אֹתוֹ בָּאֲבָנִים וַיָּמֹת כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה
        # JA: פאכ'רגוה כ'ארג אלעסכר. ורגמוה באלחגארה חתי' מאת. כמא אמר אללה מוסי'
        # EN: And they brought him out outside the camp, and stoned him with stones until he died — as God had commanded Moses.
        ("וַיֹּצִיאוּ אֹתוֹ כָּל-הָעֵדָה", "פאכ'רגוה", "And they brought him out"),
        ("אֶל-מִחוּץ לַמַּחֲנֶה", "כ'ארג אלעסכר", "outside the camp,"),
        ("וַיִּרְגְּמוּ אֹתוֹ", "ורגמוה", "and stoned him"),
        ("בָּאֲבָנִים", "באלחגארה", "with stones"),
        ("וַיָּמֹת", "חתי' מאת", "until he died —"),
        ("כַּאֲשֶׁר", "כמא", "as"),
        ("צִוָּה יְהוָה", "אמר אללה", "God had commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses."),
    ],
    37: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: פקאל אללה למוסי' קאילא
        # EN: And God said to Moses, saying:
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses,"),
        ("לֵּאמֹר", "קאילא", "saying:"),
    ],
    38: [
        # HE: דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם וְעָשׂוּ לָהֶם צִיצִת עַל-כַּנְפֵי בִגְדֵיהֶם לְדֹרֹתָם וְנָתְנוּ עַל-צִיצִת הַכָּנָף פְּתִיל תְּכֵלֶת
        # JA: מר בני אסראיל וקל להם. אן יצנעו להם ד'ואבה. עלי' אכנאף אזארהם עלי' מר אגיאלהם. ויגעלון עלי' דואבה' אלכנף סלך אסמאנגון
        # EN: Command the sons of Israel and say to them that they shall make for themselves a fringe upon the edges of their outer garments, throughout the passing of their generations; and they shall place upon the fringe of the edge a thread of blue-violet wool.
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel"),
        ("וְאָמַרְתָּ אֲלֵהֶם", "וקל להם", "and say to them"),
        ("וְעָשׂוּ לָהֶם", "אן יצנעו להם", "that they shall make for themselves"),
        ("צִיצִת", "ד'ואבה", "a fringe"),
        ("עַל-כַּנְפֵי בִגְדֵיהֶם", "עלי' אכנאף אזארהם", "upon the edges of their outer garments,"),
        ("לְדֹרֹתָם", "עלי' מר אגיאלהם", "throughout the passing of their generations;"),
        ("וְנָתְנוּ", "ויגעלון", "and they shall place"),
        ("עַל-צִיצִת הַכָּנָף", "עלי' דואבה' אלכנף", "upon the fringe of the edge"),
        ("פְּתִיל תְּכֵלֶת", "סלך אסמאנגון", "a thread of blue-violet wool."),
    ],
    39: [
        # HE: וְהָיָה לָכֶם לְצִיצִת וּרְאִיתֶם אֹתוֹ וּזְכַרְתֶּם אֶת-כָּל-מִצְו‍ֹת יְהוָה וַעֲשִׂיתֶם אֹתָם וְלֹא-תָתוּרוּ אַחֲרֵי לְבַבְכֶם וְאַחֲרֵי עֵינֵיכֶם אֲשֶׁר-אַתֶּם זֹנִים אַחֲרֵיהֶם
        # JA: פתכון תלך לכם ד'ואבה צ'אהרה. תרוהא פתד'כרו. גמיע וצאיא אללה ותעמלוהא. ולא תרומו אתבאע קלובכם ועיונכם. אלד'י אנתם טאג'יון וראהם
        # EN: And that shall be for you a visible fringe — you shall see it and remember all the commandments of God and do them; and you shall not seek to follow your hearts and your eyes, after which you go astray.
        ("וְהָיָה לָכֶם לְצִיצִת", "פתכון תלך לכם ד'ואבה", "And that shall be for you a visible fringe —"),
        ("וּרְאִיתֶם אֹתוֹ", "צ'אהרה. תרוהא", "you shall see it"),
        ("וּזְכַרְתֶּם", "פתד'כרו", "and remember"),
        ("אֶת-כָּל-מִצְו‍ֹת", "גמיע וצאיא", "all the commandments of"),
        ("יְהוָה", "אללה", "God"),
        ("וַעֲשִׂיתֶם אֹתָם", "ותעמלוהא", "and do them;"),
        ("וְלֹא-תָתוּרוּ", "ולא תרומו", "and you shall not seek to follow"),
        ("אַחֲרֵי לְבַבְכֶם", "אתבאע קלובכם", "your hearts"),
        ("וְאַחֲרֵי עֵינֵיכֶם", "ועיונכם", "and your eyes,"),
        ("אֲשֶׁר-אַתֶּם זֹנִים אַחֲרֵיהֶם", "אלד'י אנתם טאג'יון וראהם", "after which you go astray."),
    ],
    40: [
        # HE: לְמַעַן תִּזְכְּרוּ וַעֲשִׂיתֶם אֶת-כָּל-מִצְו‍ֹתָי וִהְיִיתֶם קְדֹשִׁים לֵאלֹהֵיכֶם
        # JA: לכי תד'כרו ד'אלך דאימא. ותעמלו גמיע וצאיאי. פתכונו מקדסין לרבכם
        # EN: So that you may remember that always, and do all My commandments — and you shall be consecrated to your Lord.
        ("לְמַעַן", "לכי", "So that"),
        ("תִּזְכְּרוּ", "תד'כרו", "you may remember"),
        (None, "ד'אלך", "that"),
        (None, "דאימא", "always,"),
        ("וַעֲשִׂיתֶם", "ותעמלו", "and do"),
        ("אֶת-כָּל-מִצְו‍ֹתָי", "גמיע וצאיאי", "all My commandments —"),
        ("וִהְיִיתֶם קְדֹשִׁים", "פתכונו מקדסין", "and you shall be consecrated"),
        ("לֵאלֹהֵיכֶם", "לרבכם", "to your Lord."),
    ],
    41: [
        # HE: אֲנִי יְהוָה אֱלֹהֵיכֶם אֲשֶׁר הוֹצֵאתִי אֶתְכֶם מֵאֶרֶץ מִצְרַיִם לִהְיוֹת לָכֶם לֵאלֹהִים אֲנִי יְהוָה אֱלֹהֵיכֶם
        # JA: אנא אללה רבכם. אלד'י אכ'רגתכם מן בלד מצר. לאכון לכם אלאהא. אנא אללה רבכם דאים אלבקא
        # EN: I am God your Lord, who brought you out from the land of Egypt, to be your God. I am God your Lord, everlasting in existence.
        ("אֲנִי", "אנא", "I am"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֵיכֶם", "רבכם", "your Lord,"),
        ("אֲשֶׁר הוֹצֵאתִי", "אלד'י אכ'רגתכם", "who brought you out"),
        ("מֵאֶרֶץ מִצְרַיִם", "מן בלד מצר", "from the land of Egypt,"),
        ("לִהְיוֹת לָכֶם לֵאלֹהִים", "לאכון לכם אלאהא", "to be your God."),
        ("אֲנִי יְהוָה", "אנא אללה", "I am God"),
        ("אֱלֹהֵיכֶם", "רבכם", "your Lord,"),
        (None, "דאים אלבקא", "everlasting in existence."),
    ],
}

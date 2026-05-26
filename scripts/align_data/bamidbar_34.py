"""Hand-authored word-level alignment triples for Bamidbar chapter 34."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses in speech.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "spoke"),
        ("יְהוָה", "אללה", "God"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "in speech."),
    ],
    2: [
        # HE: צַו אֶת-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם כִּי-אַתֶּם בָּאִים אֶל-הָאָרֶץ כְּנָעַן זֹאת הָאָרֶץ אֲשֶׁר תִּפֹּל לָכֶם בְּנַחֲלָה אֶרֶץ כְּנַעַן לִגְבֻלֹתֶיהָ
        # JA: מר בני אסראיל וקל להם. אנכם דאכ'לין אלי' בלד כנעאן. פהד'ה חדוד אלבלד. אלד'י יחצל לכם נחלה
        # EN: Command the sons of Israel and say to them: You are entering the land of Canaan — and these are the borders of the land that shall come to you as an inheritance.
        ("צַו", "מר", "Command"),
        ("אֶת-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("כִּי-אַתֶּם", "אנכם", "You are"),
        ("בָּאִים", "דאכ'לין", "entering"),
        ("אֶל-הָאָרֶץ", "אלי' בלד", "the land of"),
        ("כְּנָעַן", "כנעאן", "Canaan —"),
        ("זֹאת הָאָרֶץ", "פהד'ה חדוד אלבלד", "and these are the borders of the land"),
        ("אֲשֶׁר תִּפֹּל לָכֶם", "אלד'י יחצל לכם", "that shall come to you"),
        ("בְּנַחֲלָה", "נחלה", "as an inheritance."),
    ],
    3: [
        # HE: וְהָיָה לָכֶם פְּאַת-נֶגֶב מִמִּדְבַּר-צִן עַל-יְדֵי אֱדוֹם וְהָיָה לָכֶם גְּבוּל נֶגֶב מִקְצֵה יָם-הַמֶּלַח קֵדְמָה
        # JA: פיבתדי לכם אלחד אלגנובי. מן ברייה' צין אלי' גאנב אדום. פיכון מן טרף אלבחירה אלמייתה שרקייא
        # EN: And the southern border shall begin for you from the wilderness of Zin, which is beside Edom; and the southern border shall be from the end of the Dead Sea on the east.
        ("וְהָיָה לָכֶם", "פיבתדי לכם", "And the southern border shall begin for you"),
        ("פְּאַת-נֶגֶב", "אלחד אלגנובי", "from the wilderness of Zin,"),
        ("מִמִּדְבַּר-צִן", "מן ברייה' צין", "which is"),
        ("עַל-יְדֵי אֱדוֹם", "אלי' גאנב אדום", "beside Edom;"),
        ("גְּבוּל נֶגֶב", "פיכון", "and the southern border shall be"),
        ("מִקְצֵה", "מן טרף", "from the end of"),
        ("יָם-הַמֶּלַח", "אלבחירה אלמייתה", "the Dead Sea"),
        ("קֵדְמָה", "שרקייא", "on the east."),
    ],
    4: [
        # HE: וְנָסַב לָכֶם הַגְּבוּל מִנֶּגֶב לְמַעֲלֵה עַקְרַבִּים וְעָבַר צִנָה והיה (וְהָיוּ) תּוֹצְאֹתָיו מִנֶּגֶב לְקָדֵשׁ בַּרְנֵעַ וְיָצָא חֲצַר-אַדָּר וְעָבַר עַצְמֹנָה
        # JA: ת'ם יסתדיר לכם מן אלגנוב. אלי' עקבה' עקרבים ויעבר אלי' צין. ויכון כ'רוגה אלי' גאנב רקים ברנע. ויכ'רג אלי' רפח ויעבר אלי' מנאזל
        # EN: Then the border shall turn for you from the south of the ascent of Akrabbim, and shall continue to Zin; and its exit shall be to the south of Kadesh-Barnea (Raqim); and it shall go out to Rafah, and continue to Azmon.
        (None, "ת'ם", "Then"),
        ("וְנָסַב לָכֶם", "יסתדיר לכם", "the border shall turn for you"),
        ("הַגְּבוּל מִנֶּגֶב", "מן אלגנוב", "from the south of"),
        ("לְמַעֲלֵה עַקְרַבִּים", "אלי' עקבה' עקרבים", "the ascent of Akrabbim,"),
        ("וְעָבַר צִנָה", "ויעבר אלי' צין", "and shall continue to Zin;"),
        ("תּוֹצְאֹתָיו מִנֶּגֶב", "ויכון כ'רוגה אלי' גאנב", "and its exit shall be to the south of"),
        ("לְקָדֵשׁ בַּרְנֵעַ", "רקים ברנע", "Kadesh-Barnea (Raqim);"),
        ("וְיָצָא חֲצַר-אַדָּר", "ויכ'רג אלי' רפח", "and it shall go out to Rafah,"),
        ("וְעָבַר עַצְמֹנָה", "ויעבר אלי' מנאזל", "and continue to Azmon."),
    ],
    5: [
        # HE: וְנָסַב הַגְּבוּל מֵעַצְמוֹן נַחְלָה מִצְרָיִם וְהָיוּ תוֹצְאֹתָיו הַיָּמָּה
        # JA: ויסתדיר מן מנאזל אלי' ואד אלעריש. ויכון כ'רוגה אלי' אלבחר
        # EN: And it shall turn from Azmon to the Wadi of al-Arish; and its exit shall be to the sea.
        ("וְנָסַב הַגְּבוּל", "ויסתדיר", "And it shall turn"),
        ("מֵעַצְמוֹן", "מן מנאזל", "from Azmon"),
        ("נַחְלָה מִצְרָיִם", "אלי' ואד אלעריש", "to the Wadi of al-Arish;"),
        ("וְהָיוּ תוֹצְאֹתָיו", "ויכון כ'רוגה", "and its exit shall be"),
        ("הַיָּמָּה", "אלי' אלבחר", "to the sea."),
    ],
    6: [
        # HE: וּגְבוּל יָם וְהָיָה לָכֶם הַיָּם הַגָּדוֹל וּגְבוּל זֶה-יִהְיֶה לָכֶם גְּבוּל יָם
        # JA: ואלחד אלג'רבי. יכון לכם אלבחר אלכביר ותכ'מה
        # EN: And the western border — the Great Sea and its boundary shall be for you.
        ("וּגְבוּל יָם", "ואלחד אלג'רבי", "And the western border —"),
        ("וְהָיָה לָכֶם", "יכון לכם", "shall be for you."),
        ("הַיָּם הַגָּדוֹל", "אלבחר אלכביר", "the Great Sea"),
        ("וּגְבוּל", "ותכ'מה", "and its boundary"),
    ],
    7: [
        # HE: וְזֶה-יִהְיֶה לָכֶם גְּבוּל צָפוֹן מִן-הַיָּם הַגָּדֹל תְּתָאוּ לָכֶם הֹר הָהָר
        # JA: והד'א יכון לכם אלחד אלשמאלי'. מן אלבחר אלכביר. תחדו לכם אלי' גבל הור
        # EN: And this shall be the northern border for you: from the Great Sea you shall mark out your border to Mount Hor.
        ("וְזֶה-יִהְיֶה", "והד'א יכון", "And this shall be"),
        ("לָכֶם", "לכם", "for you:"),
        ("גְּבוּל צָפוֹן", "אלחד אלשמאלי'", "the northern border"),
        ("מִן-הַיָּם", "מן אלבחר", "from the Great Sea"),
        ("הַגָּדֹל", "אלכביר", "you shall mark out"),
        ("תְּתָאוּ לָכֶם", "תחדו לכם", "your border"),
        ("הֹר הָהָר", "אלי' גבל הור", "to Mount Hor."),
    ],
    8: [
        # HE: מֵהֹר הָהָר תְּתָאוּ לְבֹא חֲמָת וְהָיוּ תּוֹצְאֹת הַגְּבֻל צְדָדָה
        # JA: ומנה אלי' חמאה. ויכון כ'רוגה אלי' צדד
        # EN: From it to Hamath; and its exit shall be to Zedad.
        ("מֵהֹר הָהָר", "ומנה", "From it"),
        ("תְּתָאוּ לְבֹא חֲמָת", "אלי' חמאה", "to Hamath;"),
        ("וְהָיוּ תּוֹצְאֹת", "ויכון כ'רוגה", "and its exit shall be"),
        ("הַגְּבֻל צְדָדָה", "אלי' צדד", "to Zedad."),
    ],
    9: [
        # HE: וְיָצָא הַגְּבֻל זִפְרֹנָה וְהָיוּ תוֹצְאֹתָיו חֲצַר עֵינָן זֶה-יִהְיֶה לָכֶם גְּבוּל צָפוֹן
        # JA: ויכ'רג אלי' זפרון. וינתהי אלי' חצר עינן. הד'א יכון לכם אלחד אלשמאלי'
        # EN: And it shall go out to Ziphron, and end at Hazar-Enan. This shall be the northern border for you.
        ("וְיָצָא הַגְּבֻל", "ויכ'רג", "And it shall go out"),
        ("זִפְרֹנָה", "אלי' זפרון", "to Ziphron,"),
        ("וְהָיוּ תוֹצְאֹתָיו", "וינתהי", "and end"),
        ("חֲצַר עֵינָן", "אלי' חצר עינן", "at Hazar-Enan."),
        ("זֶה-יִהְיֶה", "הד'א יכון", "This shall be"),
        ("לָכֶם", "לכם", "for you."),
        ("גְּבוּל צָפוֹן", "אלחד אלשמאלי'", "the northern border"),
    ],
    10: [
        # HE: וְהִתְאַוִּיתֶם לָכֶם לִגְבוּל קֵדְמָה מֵחֲצַר עֵינָן שְׁפָמָה
        # JA: וחדו לכם אלחד אלשרקי. מן חצר עינן אלי' פאמיה
        # EN: And you shall mark out the eastern border for yourselves, from Hazar-Enan to Shepham.
        ("וְהִתְאַוִּיתֶם", "וחדו", "And you shall mark out"),
        ("לָכֶם", "לכם", "for yourselves,"),
        ("לִגְבוּל קֵדְמָה", "אלחד אלשרקי", "the eastern border"),
        ("מֵחֲצַר עֵינָן", "מן חצר עינן", "from Hazar-Enan"),
        ("שְׁפָמָה", "אלי' פאמיה", "to Shepham."),
    ],
    11: [
        # HE: וְיָרַד הַגְּבֻל מִשְּׁפָם הָרִבְלָה מִקֶּדֶם לָעָיִן וְיָרַד הַגְּבֻל וּמָחָה עַל-כֶּתֶף יָם-כִּנֶּרֶת קֵדְמָה
        # JA: וינחדר מן פאמיה. אלי' דפני מן שרקי אלעין. פינחדר ויצ'רב. אלי' גאנב בחר גניסר שרקייא
        # EN: And the border shall descend from Shepham to Daphneh, east of the spring; then it shall descend and extend to the eastern shore of the Sea of Gennesaret.
        ("וְיָרַד הַגְּבֻל", "וינחדר", "And the border shall descend"),
        ("מִשְּׁפָם", "מן פאמיה", "from Shepham"),
        ("הָרִבְלָה", "אלי' דפני", "to Daphneh,"),
        ("מִקֶּדֶם לָעָיִן", "מן שרקי אלעין", "east of the spring;"),
        (None, "פינחדר", "then it shall descend"),
        ("וּמָחָה", "ויצ'רב", "and extend"),
        ("עַל-כֶּתֶף יָם-כִּנֶּרֶת", "אלי' גאנב בחר גניסר", "to the eastern shore of"),
        ("קֵדְמָה", "שרקייא", "the Sea of Gennesaret."),
    ],
    12: [
        # HE: וְיָרַד הַגְּבוּל הַיַּרְדֵּנָה וְהָיוּ תוֹצְאֹתָיו יָם הַמֶּלַח זֹאת תִּהְיֶה לָכֶם הָאָרֶץ לִגְבֻלֹתֶיהָ סָבִיב
        # JA: וינזל אלארדן. ויכון כ'רוגה אלבחירה אלמייתה. הד'א תכון לכם חדוד אלבלד מסתדירא
        # EN: And the border shall go down along the Jordan, and its exit shall be at the Dead Sea. This shall be your boundary of the land all around.
        ("וְיָרַד הַגְּבוּל", "וינזל", "And the border shall go down"),
        ("הַיַּרְדֵּנָה", "אלארדן", "along the Jordan,"),
        ("וְהָיוּ תוֹצְאֹתָיו", "ויכון כ'רוגה", "and its exit shall be"),
        ("יָם הַמֶּלַח", "אלבחירה אלמייתה", "at the Dead Sea."),
        ("זֹאת תִּהְיֶה", "הד'א תכון", "This shall be"),
        ("לָכֶם", "לכם", "your boundary"),
        ("הָאָרֶץ לִגְבֻלֹתֶיהָ", "חדוד אלבלד", "of the land"),
        ("סָבִיב", "מסתדירא", "all around."),
    ],
    13: [
        # HE: וַיְצַו מֹשֶׁה אֶת-בְּנֵי יִשְׂרָאֵל לֵאמֹר זֹאת הָאָרֶץ אֲשֶׁר תִּתְנַחֲלוּ אֹתָהּ בְּגוֹרָל אֲשֶׁר צִוָּה יְהוָה לָתֵת לְתִשְׁעַת הַמַּטּוֹת וַחֲצִי הַמַּטֶּה
        # JA: פאמר מוסי' בני אסראיל. ען קול אללה וקאל. הד'א אלבלד אלמחדוד תוזעונה באסהם . כמא אמר אללה. אן יעטא לתסעה' אסבאט ונצף
        # EN: And Moses commanded the sons of Israel, on the word of God, and said: This is the bounded land which you shall apportion by lots, as God commanded — that it be given to nine tribes and a half.
        ("וַיְצַו", "פאמר", "And Moses commanded"),
        ("מֹשֶׁה", "מוסי'", "the sons of Israel,"),
        ("אֶת-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "on the word of"),
        ("לֵאמֹר", "ען קול אללה וקאל", "God, and said:"),
        ("זֹאת הָאָרֶץ", "הד'א אלבלד אלמחדוד", "This is the bounded land"),
        ("אֲשֶׁר תִּתְנַחֲלוּ אֹתָהּ", "תוזעונה", "which you shall apportion"),
        ("בְּגוֹרָל", "באסהם", "by lots,"),
        ("אֲשֶׁר צִוָּה יְהוָה", "כמא אמר אללה", "as God commanded —"),
        ("לָתֵת", "אן יעטא", "that it be given"),
        ("לְתִשְׁעַת הַמַּטּוֹת", "לתסעה' אסבאט", "to nine tribes"),
        ("וַחֲצִי הַמַּטֶּה", "ונצף", "and a half."),
    ],
    14: [
        # HE: כִּי לָקְחוּ מַטֵּה בְנֵי הָראוּבֵנִי לְבֵית אֲבֹתָם וּמַטֵּה בְנֵי-הַגָּדִי לְבֵית אֲבֹתָם וַחֲצִי מַטֵּה מְנַשֶּׁה לָקְחוּ נַחֲלָתָם
        # JA: אד' קד אכ'ד' סבט ראובן. וסבט גד ונצף סבט מנשה. נחלתהם לביות אבאיהם
        # EN: For the tribe of Reuben, and the tribe of Gad, and the half-tribe of Manasseh have already taken their inheritance, according to their ancestral houses.
        ("כִּי", "אד' קד", "For"),
        ("לָקְחוּ", "אכ'ד'", "have already taken"),
        ("מַטֵּה בְנֵי הָראוּבֵנִי", "סבט ראובן", "the tribe of Reuben,"),
        ("וּמַטֵּה בְנֵי-הַגָּדִי", "וסבט גד", "and the tribe of Gad,"),
        ("וַחֲצִי מַטֵּה מְנַשֶּׁה", "ונצף סבט מנשה", "and the half-tribe of Manasseh"),
        ("נַחֲלָתָם", "נחלתהם", "their inheritance,"),
        ("לְבֵית אֲבֹתָם", "לביות אבאיהם", "according to their ancestral houses."),
    ],
    15: [
        # HE: שְׁנֵי הַמַּטּוֹת וַחֲצִי הַמַּטֶּה לָקְחוּ נַחֲלָתָם מֵעֵבֶר לְיַרְדֵּן יְרֵחוֹ--קֵדְמָה מִזְרָחָה
        # JA: הד'אן אלסבטאן ואלנצף. אכ'דו נחלתהם. מן עבר ארדן יריחא אלשרקי
        # EN: These two tribes and the half took their inheritance from across the Jordan of Jericho on the east.
        ("שְׁנֵי הַמַּטּוֹת", "הד'אן אלסבטאן", "These two tribes"),
        ("וַחֲצִי הַמַּטֶּה", "ואלנצף", "and the half"),
        ("לָקְחוּ", "אכ'דו", "took"),
        ("נַחֲלָתָם", "נחלתהם", "their inheritance"),
        ("מֵעֵבֶר", "מן עבר", "from across"),
        ("לְיַרְדֵּן יְרֵחוֹ", "ארדן יריחא", "the Jordan of Jericho"),
        ("קֵדְמָה מִזְרָחָה", "אלשרקי", "on the east."),
    ],
    16: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses in speech.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "spoke"),
        ("יְהוָה", "אללה", "God"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "in speech."),
    ],
    17: [
        # HE: אֵלֶּה שְׁמוֹת הָאֲנָשִׁים אֲשֶׁר-יִנְחֲלוּ לָכֶם אֶת-הָאָרֶץ אֶלְעָזָר הַכֹּהֵן וִיהוֹשֻׁעַ בִּן-נוּן
        # JA: הד'א אסמא אלרגאל. אלד'י יקסמו לכם אלבלד. אלעזר אלאמאם. ויהושע אבן נון
        # EN: These are the names of the men who shall apportion the land for you: Eleazar the imām, and Joshua son of Nun.
        ("אֵלֶּה", "הד'א", "These are"),
        ("שְׁמוֹת", "אסמא", "the names of"),
        ("הָאֲנָשִׁים", "אלרגאל", "the men"),
        ("אֲשֶׁר-יִנְחֲלוּ", "אלד'י יקסמו", "who shall apportion"),
        ("לָכֶם", "לכם", "for you:"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land"),
        ("אֶלְעָזָר", "אלעזר", "Eleazar"),
        ("הַכֹּהֵן", "אלאמאם", "the imām,"),
        ("וִיהוֹשֻׁעַ", "ויהושע", "and Joshua"),
        ("בִּן-נוּן", "אבן נון", "son of Nun."),
    ],
    18: [
        # HE: וְנָשִׂיא אֶחָד נָשִׂיא אֶחָד מִמַּטֶּה--תִּקְחוּ לִנְחֹל אֶת-הָאָרֶץ
        # JA: ושריף מן כל סבט. כ'ד'וה ליקסם אלבלד
        # EN: And one noble from each tribe — take him to apportion the land.
        ("וְנָשִׂיא אֶחָד", "ושריף", "And one noble"),
        ("מִמַּטֶּה", "מן כל סבט", "from each tribe —"),
        ("תִּקְחוּ", "כ'ד'וה", "take him"),
        ("לִנְחֹל", "ליקסם", "to apportion"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land."),
    ],
    19: [
        # HE: וְאֵלֶּה שְׁמוֹת הָאֲנָשִׁים לְמַטֵּה יְהוּדָה כָּלֵב בֶּן-יְפֻנֶּה
        # JA: והד'א אסמאיהם. מן סבט יהודה. כלב אבן יפנה
        # EN: And these are their names: from the tribe of Judah, Caleb son of Jephunneh.
        ("וְאֵלֶּה", "והד'א", "And these are"),
        ("שְׁמוֹת הָאֲנָשִׁים", "אסמאיהם", "their names:"),
        ("לְמַטֵּה", "מן סבט", "from the tribe of"),
        ("יְהוּדָה", "יהודה", "Judah,"),
        ("כָּלֵב", "כלב", "Caleb"),
        ("בֶּן-יְפֻנֶּה", "אבן יפנה", "son of Jephunneh."),
    ],
    20: [
        # HE: וּלְמַטֵּה בְּנֵי שִׁמְעוֹן שְׁמוּאֵל בֶּן-עַמִּיהוּד
        # JA: ומן סבט שמעון. שמואל אבן עמיהוד
        # EN: And from the tribe of Simeon, Samuel son of Ammihud.
        ("וּלְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("בְּנֵי שִׁמְעוֹן", "שמעון", "Simeon,"),
        ("שְׁמוּאֵל", "שמואל", "Samuel"),
        ("בֶּן-עַמִּיהוּד", "אבן עמיהוד", "son of Ammihud."),
    ],
    21: [
        # HE: לְמַטֵּה בִנְיָמִן אֱלִידָד בֶּן-כִּסְלוֹן
        # JA: ומן סבט בנימין. אלי'דד אבן כסלון
        # EN: And from the tribe of Benjamin, Elidad son of Kislon.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("בִנְיָמִן", "בנימין", "Benjamin,"),
        ("אֱלִידָד", "אלי'דד", "Elidad"),
        ("בֶּן-כִּסְלוֹן", "אבן כסלון", "son of Kislon."),
    ],
    22: [
        # HE: וּלְמַטֵּה בְנֵי-דָן נָשִׂיא--בֻּקִּי בֶּן-יָגְלִי
        # JA: ומן סבט דן שריפא. בקי אבן יגלי
        # EN: And from the tribe of Dan, a noble: Bukki son of Jogli.
        ("וּלְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("בְנֵי-דָן", "דן", "Dan,"),
        ("נָשִׂיא", "שריפא", "a noble:"),
        ("בֻּקִּי", "בקי", "Bukki"),
        ("בֶּן-יָגְלִי", "אבן יגלי", "son of Jogli."),
    ],
    23: [
        # HE: לִבְנֵי יוֹסֵף לְמַטֵּה בְנֵי-מְנַשֶּׁה נָשִׂיא--חַנִּיאֵל בֶּן-אֵפֹד
        # JA: לבני יוסף מן סבט בני מנשה שריף. חניאל אבן אפוד
        # EN: For the sons of Joseph, from the tribe of the sons of Manasseh, a noble: Hanniel son of Ephod.
        ("לִבְנֵי יוֹסֵף", "לבני יוסף", "For the sons of Joseph,"),
        ("לְמַטֵּה", "מן סבט", "from the tribe of"),
        ("בְנֵי-מְנַשֶּׁה", "בני מנשה", "the sons of Manasseh,"),
        ("נָשִׂיא", "שריף", "a noble:"),
        ("חַנִּיאֵל", "חניאל", "Hanniel"),
        ("בֶּן-אֵפֹד", "אבן אפוד", "son of Ephod."),
    ],
    24: [
        # HE: וּלְמַטֵּה בְנֵי-אֶפְרַיִם נָשִׂיא--קְמוּאֵל בֶּן-שִׁפְטָן
        # JA: ומן סבט בני אפרים שריף. קמואל אבן שפטן
        # EN: And from the tribe of the sons of Ephraim, a noble: Kemuel son of Shiphtan.
        ("וּלְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("בְנֵי-אֶפְרַיִם", "בני אפרים", "the sons of Ephraim,"),
        ("נָשִׂיא", "שריף", "a noble:"),
        ("קְמוּאֵל", "קמואל", "Kemuel"),
        ("בֶּן-שִׁפְטָן", "אבן שפטן", "son of Shiphtan."),
    ],
    25: [
        # HE: וּלְמַטֵּה בְנֵי-זְבוּלֻן נָשִׂיא--אֱלִיצָפָן בֶּן-פַּרְנָךְ
        # JA: ולסבט זבולון שריפא. אליצפן אבן פרנך
        # EN: And for the tribe of Zebulun, a noble: Elizaphan son of Parnach.
        ("וּלְמַטֵּה", "ולסבט", "And for the tribe of"),
        ("בְנֵי-זְבוּלֻן", "זבולון", "Zebulun,"),
        ("נָשִׂיא", "שריפא", "a noble:"),
        ("אֱלִיצָפָן", "אליצפן", "Elizaphan"),
        ("בֶּן-פַּרְנָךְ", "אבן פרנך", "son of Parnach."),
    ],
    26: [
        # HE: וּלְמַטֵּה בְנֵי-יִשָּׂשכָר נָשִׂיא--פַּלְטִיאֵל בֶּן-עַזָּן
        # JA: ומן סבט יששכר שריפא פלטיאל אבן עזן
        # EN: And from the tribe of Issachar, a noble: Paltiel son of Azzan.
        ("וּלְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("בְנֵי-יִשָּׂשכָר", "יששכר", "Issachar,"),
        ("נָשִׂיא", "שריפא", "a noble:"),
        ("פַּלְטִיאֵל", "פלטיאל", "Paltiel"),
        ("בֶּן-עַזָּן", "אבן עזן", "son of Azzan."),
    ],
    27: [
        # HE: וּלְמַטֵּה בְנֵי-אָשֵׁר נָשִׂיא--אֲחִיהוּד בֶּן-שְׁלֹמִי
        # JA: ומן סבט אשר שריפא. אחיהוד אבן שלומי
        # EN: And from the tribe of Asher, a noble: Ahihud son of Shelomi.
        ("וּלְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("בְנֵי-אָשֵׁר", "אשר", "Asher,"),
        ("נָשִׂיא", "שריפא", "a noble:"),
        ("אֲחִיהוּד", "אחיהוד", "Ahihud"),
        ("בֶּן-שְׁלֹמִי", "אבן שלומי", "son of Shelomi."),
    ],
    28: [
        # HE: וּלְמַטֵּה בְנֵי-נַפְתָּלִי נָשִׂיא--פְּדַהְאֵל בֶּן-עַמִּיהוּד
        # JA: ומן סבט נפתלי שריפא. פדהאל אבן עמיהוד
        # EN: And from the tribe of Naphtali, a noble: Pedahel son of Ammihud.
        ("וּלְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("בְנֵי-נַפְתָּלִי", "נפתלי", "Naphtali,"),
        ("נָשִׂיא", "שריפא", "a noble:"),
        ("פְּדַהְאֵל", "פדהאל", "Pedahel"),
        ("בֶּן-עַמִּיהוּד", "אבן עמיהוד", "son of Ammihud."),
    ],
    29: [
        # HE: אֵלֶּה אֲשֶׁר צִוָּה יְהוָה לְנַחֵל אֶת-בְּנֵי-יִשְׂרָאֵל בְּאֶרֶץ כְּנָעַן
        # JA: הולאי. אלד'י אמר אללה. אן יקסמו לבני אסראיל בלד כנעאן
        # EN: These are those who entered — whom God commanded to apportion the land of Canaan for the sons of Israel.
        ("אֵלֶּה", "הולאי", "These are those who entered —"),
        ("אֲשֶׁר צִוָּה", "אלד'י אמר", "whom God commanded"),
        ("יְהוָה", "אללה", "to apportion"),
        ("לְנַחֵל", "אן יקסמו", "the land of"),
        ("אֶת-בְּנֵי-יִשְׂרָאֵל", "לבני אסראיל", "for the sons of Israel."),
        ("בְּאֶרֶץ כְּנָעַן", "בלד כנעאן", "Canaan"),
    ],
}

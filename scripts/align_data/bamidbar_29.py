"""Hand-authored word-level alignment triples for Bamidbar chapter 29."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וּבַחֹדֶשׁ הַשְּׁבִיעִי בְּאֶחָד לַחֹדֶשׁ מִקְרָא-קֹדֶשׁ יִהְיֶה לָכֶם--כָּל-מְלֶאכֶת עֲבֹדָה לֹא תַעֲשׂוּ יוֹם תְּרוּעָה יִהְיֶה לָכֶם
        # JA: ופי אליום אלאוול מן אלשהר אלסאבע. אסם מקדס יכון לכם. כל צנעה' מכסב לא תעמלו. ויום גלבה יכון לכם
        # EN: And on the first day of the seventh month, a holy name shall be for you — no craft of gain shall you perform; and it shall be for you a day of clamor.
        ("וּבַחֹדֶשׁ", "ופי", "And on the first day of"),
        ("הַשְּׁבִיעִי", "אליום אלאוול", "the seventh month,"),
        ("בְּאֶחָד לַחֹדֶשׁ", "מן אלשהר אלסאבע", "a holy name"),
        ("מִקְרָא-קֹדֶשׁ", "אסם מקדס", "shall be for you —"),
        ("יִהְיֶה לָכֶם", "יכון לכם", "no craft of gain"),
        ("כָּל-מְלֶאכֶת עֲבֹדָה", "כל צנעה' מכסב", "shall you perform;"),
        ("לֹא תַעֲשׂוּ", "לא תעמלו", "and it shall be for you"),
        ("יוֹם תְּרוּעָה", "ויום גלבה", "a day of clamor."),
    ],
    2: [
        # HE: וַעֲשִׂיתֶם עֹלָה לְרֵיחַ נִיחֹחַ לַיהוָה--פַּר בֶּן-בָּקָר אֶחָד אַיִל אֶחָד כְּבָשִׂים בְּנֵי-שָׁנָה שִׁבְעָה תְּמִימִם
        # JA: וקרבו צעידה. מקבולה מרצ'ייה ללה . רת'א ואחדא וכבשא. וסבעה' חמלאן בני סנה צחאחא
        # EN: And offer up an elevation-offering, an acceptable and pleasing offering to God: one bull from the herd, and one ram, and seven yearling lambs — sound ones.
        ("וַעֲשִׂיתֶם", "וקרבו", "And offer up"),
        ("עֹלָה", "צעידה", "an elevation-offering,"),
        ("לְרֵיחַ נִיחֹחַ", "מקבולה מרצ'ייה", "an acceptable and pleasing offering"),
        ("לַיהוָה", "ללה", "to God:"),
        ("פַּר בֶּן-בָּקָר אֶחָד", "רת'א ואחדא", "one bull from the herd,"),
        ("אַיִל אֶחָד", "וכבשא", "and one ram,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה שִׁבְעָה", "וסבעה' חמלאן בני סנה", "and seven yearling lambs —"),
        ("תְּמִימִם", "צחאחא", "sound ones."),
    ],
    3: [
        # HE: וּמִנְחָתָם--סֹלֶת בְּלוּלָה בַשָּׁמֶן שְׁלֹשָׁה עֶשְׂרֹנִים לַפָּר שְׁנֵי עֶשְׂרֹנִים לָאָיִל
        # JA: ומעהם מן אלבר. סמד מלתות בדהן. ת'לאת'ה' עשור לאלרת'. ועשרין לאלכבש
        # EN: And with them, from the grain: fine flour mixed with oil — three tenths for the bull, and two tenths for the ram.
        ("וּמִנְחָתָם", "ומעהם", "And with them,"),
        ("סֹלֶת", "מן אלבר", "from the grain:"),
        ("בְּלוּלָה", "סמד מלתות", "fine flour mixed"),
        ("בַשָּׁמֶן", "בדהן", "with oil —"),
        ("שְׁלֹשָׁה עֶשְׂרֹנִים", "ת'לאת'ה' עשור", "three tenths"),
        ("לַפָּר", "לאלרת'", "for the bull,"),
        ("שְׁנֵי עֶשְׂרֹנִים", "ועשרין", "and two tenths"),
        ("לָאָיִל", "לאלכבש", "for the ram."),
    ],
    4: [
        # HE: וְעִשָּׂרוֹן אֶחָד לַכֶּבֶשׂ הָאֶחָד לְשִׁבְעַת הַכְּבָשִׂים
        # JA: ועשר לכל חמל מן אלסבעה
        # EN: And one tenth for each lamb of the seven.
        ("וְעִשָּׂרוֹן אֶחָד", "ועשר", "And one tenth"),
        ("לַכֶּבֶשׂ הָאֶחָד", "לכל חמל", "for each lamb"),
        ("לְשִׁבְעַת הַכְּבָשִׂים", "מן אלסבעה", "of the seven."),
    ],
    5: [
        # HE: וּשְׂעִיר-עִזִּים אֶחָד חַטָּאת לְכַפֵּר עֲלֵיכֶם
        # JA: ועתוד מן אלמאעז לאלד'כוה. ליסתג'פר ענכם
        # EN: And a he-goat from the goats for the purification-offering, to seek forgiveness on your behalf.
        ("וּשְׂעִיר-עִזִּים אֶחָד", "ועתוד מן אלמאעז", "And a he-goat from the goats"),
        ("חַטָּאת", "לאלד'כוה", "for the purification-offering,"),
        ("לְכַפֵּר", "ליסתג'פר", "to seek forgiveness"),
        ("עֲלֵיכֶם", "ענכם", "on your behalf."),
    ],
    6: [
        # HE: מִלְּבַד עֹלַת הַחֹדֶשׁ וּמִנְחָתָהּ וְעֹלַת הַתָּמִיד וּמִנְחָתָהּ וְנִסְכֵּיהֶם כְּמִשְׁפָּטָם לְרֵיחַ נִיחֹחַ אִשֶּׁה לַיהוָה
        # JA: מא כ'לא קרבאן אלשהר וברה. וקרבאן אלדאים וברה. ומזאגהם כאלסביל. מקבול מרצ'י קרבאן ללה
        # EN: This is apart from the offering of the month and its grain, and the perpetual offering and its grain, and their libation as is customary — an acceptable and pleasing offering to God.
        ("מִלְּבַד", "מא כ'לא", "This is apart from"),
        ("עֹלַת הַחֹדֶשׁ", "קרבאן אלשהר", "the offering of the month"),
        ("וּמִנְחָתָהּ", "וברה", "and its grain,"),
        ("וְעֹלַת הַתָּמִיד", "וקרבאן אלדאים", "and the perpetual offering"),
        (None, "וברה", "and its grain,"),
        ("וְנִסְכֵּיהֶם", "ומזאגהם", "and their libation"),
        ("כְּמִשְׁפָּטָם", "כאלסביל", "as is customary —"),
        ("לְרֵיחַ נִיחֹחַ", "מקבול מרצ'י", "an acceptable and pleasing offering"),
        ("לַיהוָה", "ללה", "to God."),
    ],
    7: [
        # HE: וּבֶעָשׂוֹר לַחֹדֶשׁ הַשְּׁבִיעִי הַזֶּה מִקְרָא-קֹדֶשׁ יִהְיֶה לָכֶם וְעִנִּיתֶם אֶת-נַפְשֹׁתֵיכֶם כָּל-מְלָאכָה לֹא תַעֲשׂוּ
        # JA: ופי אלעאשר מנה. אסם מקדס יכון לכם. ואגיעו אנפסכם. וכל עמל לא תעמלו
        # EN: And on the tenth of this seventh month, a holy name shall be for you; and make your souls hunger; and no labor shall you perform.
        ("וּבֶעָשׂוֹר", "ופי אלעאשר", "And on the tenth"),
        ("לַחֹדֶשׁ הַשְּׁבִיעִי הַזֶּה", "מנה", "of this seventh month,"),
        ("מִקְרָא-קֹדֶשׁ", "אסם מקדס", "a holy name"),
        ("יִהְיֶה לָכֶם", "יכון לכם", "shall be for you;"),
        ("וְעִנִּיתֶם", "ואגיעו", "and make"),
        ("אֶת-נַפְשֹׁתֵיכֶם", "אנפסכם", "your souls hunger;"),
        ("כָּל-מְלָאכָה", "וכל עמל", "and no labor"),
        ("לֹא תַעֲשׂוּ", "לא תעמלו", "shall you perform."),
    ],
    8: [
        # HE: וְהִקְרַבְתֶּם עֹלָה לַיהוָה רֵיחַ נִיחֹחַ פַּר בֶּן-בָּקָר אֶחָד אַיִל אֶחָד כְּבָשִׂים בְּנֵי-שָׁנָה שִׁבְעָה תְּמִימִם יִהְיוּ לָכֶם
        # JA: וקרבו צעידה ללה מקבול מרצ'י. רת'א ואחדא וכבשא. וסבעה חמלאן בני סנה. צחאחא תכון לכם
        # EN: And offer up an elevation-offering to God, acceptable and pleasing: one bull from the herd, and one ram, and seven yearling lambs — sound ones shall they be for you.
        ("וְהִקְרַבְתֶּם", "וקרבו", "And offer up"),
        ("עֹלָה", "צעידה", "an elevation-offering"),
        ("לַיהוָה", "ללה", "to God,"),
        ("רֵיחַ נִיחֹחַ", "מקבול מרצ'י", "acceptable and pleasing:"),
        ("פַּר בֶּן-בָּקָר אֶחָד", "רת'א ואחדא", "one bull from the herd,"),
        ("אַיִל אֶחָד", "וכבשא", "and one ram,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה שִׁבְעָה", "וסבעה חמלאן בני סנה", "and seven yearling lambs —"),
        ("תְּמִימִם יִהְיוּ לָכֶם", "צחאחא תכון לכם", "sound ones shall they be for you."),
    ],
    9: [
        # HE: וּמִנְחָתָם--סֹלֶת בְּלוּלָה בַשָּׁמֶן שְׁלֹשָׁה עֶשְׂרֹנִים לַפָּר שְׁנֵי עֶשְׂרֹנִים לָאַיִל הָאֶחָד
        # JA: ומעהם מן אלבר. סמד מלתות בדהן. ת'לאת'ה' עשור לאלרת'. ועשרין לאלכבש
        # EN: And with them, from the grain: fine flour mixed with oil — three tenths for the bull, and two tenths for the ram.
        ("וּמִנְחָתָם", "ומעהם", "And with them,"),
        ("סֹלֶת", "מן אלבר", "from the grain:"),
        ("בְּלוּלָה", "סמד מלתות", "fine flour mixed"),
        ("בַשָּׁמֶן", "בדהן", "with oil —"),
        ("שְׁלֹשָׁה עֶשְׂרֹנִים", "ת'לאת'ה' עשור", "three tenths"),
        ("לַפָּר", "לאלרת'", "for the bull,"),
        ("שְׁנֵי עֶשְׂרֹנִים", "ועשרין", "and two tenths"),
        ("לָאַיִל הָאֶחָד", "לאלכבש", "for the ram."),
    ],
    10: [
        # HE: עִשָּׂרוֹן עִשָּׂרוֹן לַכֶּבֶשׂ הָאֶחָד--לְשִׁבְעַת הַכְּבָשִׂים
        # JA: ועשר לכל חמל מן אלסבעה
        # EN: And one tenth for each lamb of the seven.
        ("עִשָּׂרוֹן עִשָּׂרוֹן", "ועשר", "And one tenth"),
        ("לַכֶּבֶשׂ הָאֶחָד", "לכל חמל", "for each lamb"),
        ("לְשִׁבְעַת הַכְּבָשִׂים", "מן אלסבעה", "of the seven."),
    ],
    11: [
        # HE: שְׂעִיר-עִזִּים אֶחָד חַטָּאת מִלְּבַד חַטַּאת הַכִּפֻּרִים וְעֹלַת הַתָּמִיד וּמִנְחָתָהּ וְנִסְכֵּיהֶם
        # JA: ועתוד מן אלמאעז לאלד'כוה. מא כ'לא דכוה' אלג'פראן וקרבאן אלדאים. וברהא ומזאגהא
        # EN: And a he-goat from the goats for the purification-offering — apart from the purification-offering of atonement, and the perpetual offering and its grain, and its libation.
        ("שְׂעִיר-עִזִּים אֶחָד", "ועתוד מן אלמאעז", "And a he-goat from the goats"),
        ("חַטָּאת", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "מא כ'לא", "apart from"),
        ("חַטַּאת הַכִּפֻּרִים", "דכוה' אלג'פראן", "the purification-offering of atonement,"),
        ("וְעֹלַת הַתָּמִיד", "וקרבאן אלדאים", "and the perpetual offering"),
        ("וּמִנְחָתָהּ", "וברהא", "and its grain,"),
        ("וְנִסְכֵּיהֶם", "ומזאגהא", "and its libation."),
    ],
    12: [
        # HE: וּבַחֲמִשָּׁה עָשָׂר יוֹם לַחֹדֶשׁ הַשְּׁבִיעִי מִקְרָא-קֹדֶשׁ יִהְיֶה לָכֶם--כָּל-מְלֶאכֶת עֲבֹדָה לֹא תַעֲשׂוּ וְחַגֹּתֶם חַג לַיהוָה שִׁבְעַת יָמִים
        # JA: ופי אליום אלכ'אמס עשר מן אלשהר אלסאבע. אסם מקדס יכון לכם. כל צנעה' מכסב לא תעמלו. וחגו חג ללה סבעה' אייאם
        # EN: And on the fifteenth day of the seventh month, a holy name shall be for you — no craft of gain shall you perform; and celebrate a festival to God for seven days.
        ("וּבַחֲמִשָּׁה עָשָׂר יוֹם", "ופי אליום אלכ'אמס עשר", "And on the fifteenth day"),
        ("לַחֹדֶשׁ הַשְּׁבִיעִי", "מן אלשהר אלסאבע", "of the seventh month,"),
        ("מִקְרָא-קֹדֶשׁ", "אסם מקדס", "a holy name"),
        ("יִהְיֶה לָכֶם", "יכון לכם", "shall be for you —"),
        ("כָּל-מְלֶאכֶת עֲבֹדָה", "כל צנעה' מכסב", "no craft of gain"),
        ("לֹא תַעֲשׂוּ", "לא תעמלו", "shall you perform;"),
        ("וְחַגֹּתֶם", "וחגו", "and celebrate"),
        ("חַג", "חג", "a festival"),
        ("לַיהוָה", "ללה", "to God"),
        ("שִׁבְעַת יָמִים", "סבעה' אייאם", "for seven days."),
    ],
    13: [
        # HE: וְהִקְרַבְתֶּם עֹלָה אִשֵּׁה רֵיחַ נִיחֹחַ לַיהוָה--פָּרִים בְּנֵי-בָקָר שְׁלֹשָׁה עָשָׂר אֵילִם שְׁנָיִם כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר תְּמִימִם יִהְיוּ
        # JA: וקרבו צעידה. קרבאנא מקבולא מרצ'יא ללה . ת'לאת'ה' עשר רת' מן אלבקר וכבשין. וארבעה' עשר חמל. בני סנה צחאחא
        # EN: And offer up an elevation-offering, an acceptable and pleasing offering to God: thirteen bulls from the herd, and two rams, and fourteen yearling lambs — sound ones.
        ("וְהִקְרַבְתֶּם", "וקרבו", "And offer up"),
        ("עֹלָה", "צעידה", "an elevation-offering,"),
        ("אִשֵּׁה רֵיחַ נִיחֹחַ", "קרבאנא מקבולא מרצ'יא", "an acceptable and pleasing offering"),
        ("לַיהוָה", "ללה", "to God:"),
        ("פָּרִים בְּנֵי-בָקָר שְׁלֹשָׁה עָשָׂר", "ת'לאת'ה' עשר רת' מן אלבקר", "thirteen bulls from the herd,"),
        ("אֵילִם שְׁנָיִם", "וכבשין", "and two rams,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר", "וארבעה' עשר חמל", "and fourteen yearling lambs —"),
        ("תְּמִימִם יִהְיוּ", "בני סנה צחאחא", "sound ones."),
    ],
    14: [
        # HE: וּמִנְחָתָם--סֹלֶת בְּלוּלָה בַשָּׁמֶן שְׁלֹשָׁה עֶשְׂרֹנִים לַפָּר הָאֶחָד לִשְׁלֹשָׁה עָשָׂר פָּרִים שְׁנֵי עֶשְׂרֹנִים לָאַיִל הָאֶחָד לִשְׁנֵי הָאֵילִם
        # JA: ומעהם מן אלבר. סמד מלתות בדהן. ת'לאת'ה' עשור. לכל רת' מן אלת'לאת'ה' עשר. ועשרין לכל כבש מן אלכבשין
        # EN: And with them, from the grain: fine flour mixed with oil — three tenths for each bull of the thirteen, and two tenths for each ram of the two rams.
        ("וּמִנְחָתָם", "ומעהם", "And with them,"),
        ("סֹלֶת", "מן אלבר", "from the grain:"),
        ("בְּלוּלָה", "סמד מלתות", "fine flour mixed"),
        ("בַשָּׁמֶן", "בדהן", "with oil —"),
        ("שְׁלֹשָׁה עֶשְׂרֹנִים", "ת'לאת'ה' עשור", "three tenths"),
        ("לַפָּר הָאֶחָד לִשְׁלֹשָׁה עָשָׂר פָּרִים", "לכל רת' מן אלת'לאת'ה' עשר", "for each bull of the thirteen,"),
        ("שְׁנֵי עֶשְׂרֹנִים", "ועשרין", "and two tenths"),
        ("לָאַיִל הָאֶחָד לִשְׁנֵי הָאֵילִם", "לכל כבש מן אלכבשין", "for each ram of the two rams."),
    ],
    15: [
        # HE: וְעִשָּׂרוֹן עִשָּׂרוֹן לַכֶּבֶשׂ הָאֶחָד--לְאַרְבָּעָה עָשָׂר כְּבָשִׂים
        # JA: ועשר לכל חמל מן אלארבעה' עשר
        # EN: And one tenth for each lamb of the fourteen.
        ("וְעִשָּׂרוֹן עִשָּׂרוֹן", "ועשר", "And one tenth"),
        ("לַכֶּבֶשׂ הָאֶחָד", "לכל חמל", "for each lamb"),
        ("לְאַרְבָּעָה עָשָׂר כְּבָשִׂים", "מן אלארבעה' עשר", "of the fourteen."),
    ],
    16: [
        # HE: וּשְׂעִיר-עִזִּים אֶחָד חַטָּאת מִלְּבַד עֹלַת הַתָּמִיד מִנְחָתָהּ וְנִסְכָּהּ
        # JA: ועתוד מן אלמאעז לאלד'כוה. סוא קרבאן אלדאים. וברה ומזאגה
        # EN: And a he-goat from the goats for the purification-offering — apart from the perpetual offering, its grain and its libation.
        ("וּשְׂעִיר-עִזִּים אֶחָד", "ועתוד מן אלמאעז", "And a he-goat from the goats"),
        ("חַטָּאת", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the perpetual offering,"),
        ("מִנְחָתָהּ", "וברה", "its grain"),
        ("וְנִסְכָּהּ", "ומזאגה", "and its libation."),
    ],
    17: [
        # HE: וּבַיּוֹם הַשֵּׁנִי פָּרִים בְּנֵי-בָקָר שְׁנֵים עָשָׂר--אֵילִם שְׁנָיִם כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר תְּמִימִם
        # JA: ופי אליום אלת'אני. את'ני עשר רת' מן אלבקר וכבשין. וארבעה' עשר חמל. בני סנה צחאחא
        # EN: And on the second day: twelve bulls from the herd, and two rams, and fourteen yearling lambs — sound ones.
        ("וּבַיּוֹם", "ופי אליום", "And on the"),
        ("הַשֵּׁנִי", "אלת'אני", "second day:"),
        ("פָּרִים בְּנֵי-בָקָר שְׁנֵים עָשָׂר", "את'ני עשר רת' מן אלבקר", "twelve bulls from the herd,"),
        ("אֵילִם שְׁנָיִם", "וכבשין", "and two rams,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר", "וארבעה' עשר חמל", "and fourteen yearling lambs —"),
        ("תְּמִימִם", "בני סנה צחאחא", "sound ones."),
    ],
    18: [
        # HE: וּמִנְחָתָם וְנִסְכֵּיהֶם לַפָּרִים לָאֵילִם וְלַכְּבָשִׂים בְּמִסְפָּרָם--כַּמִּשְׁפָּט
        # JA: וברהם ומזאגהם. לאלרת'ות' ואלכבאש ואלחמלאן. באחצאיהם עלי' אלסביל
        # EN: And their grain and their libation — for the bulls, and the rams, and the lambs — in their enumerated amounts, as is customary.
        ("וּמִנְחָתָם", "וברהם", "And their grain"),
        ("וְנִסְכֵּיהֶם", "ומזאגהם", "and their libation —"),
        ("לַפָּרִים", "לאלרת'ות'", "for the bulls,"),
        ("לָאֵילִם", "ואלכבאש", "and the rams,"),
        ("וְלַכְּבָשִׂים", "ואלחמלאן", "and the lambs —"),
        ("בְּמִסְפָּרָם", "באחצאיהם", "in their enumerated amounts,"),
        ("כַּמִּשְׁפָּט", "עלי' אלסביל", "as is customary."),
    ],
    19: [
        # HE: וּשְׂעִיר-עִזִּים אֶחָד חַטָּאת מִלְּבַד עֹלַת הַתָּמִיד וּמִנְחָתָהּ וְנִסְכֵּיהֶם
        # JA: ועתוד מן אלמאעז לאלד'כוה. סוא קרבאן אלדאים. וברהם ומזאגהם
        # EN: And a he-goat from the goats for the purification-offering — apart from the perpetual offering and its grain, and its libation.
        ("וּשְׂעִיר-עִזִּים אֶחָד", "ועתוד מן אלמאעז", "And a he-goat from the goats"),
        ("חַטָּאת", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the perpetual offering"),
        ("וּמִנְחָתָהּ", "וברהם", "and its grain,"),
        ("וְנִסְכֵּיהֶם", "ומזאגהם", "and its libation."),
    ],
    20: [
        # HE: וּבַיּוֹם הַשְּׁלִישִׁי פָּרִים עַשְׁתֵּי-עָשָׂר אֵילִם שְׁנָיִם כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר תְּמִימִם
        # JA: ופי אליום אלת'לאת' אחדי' עשר רת' וכבשין. וארבעה' עשר חמל. בני סנה צחאחא
        # EN: And on the third day: eleven bulls from the herd, and two rams, and fourteen yearling lambs — sound ones.
        ("וּבַיּוֹם", "ופי אליום", "And on the"),
        ("הַשְּׁלִישִׁי", "אלת'לאת'", "third day:"),
        ("פָּרִים עַשְׁתֵּי-עָשָׂר", "אחדי' עשר רת'", "eleven bulls from the herd,"),
        ("אֵילִם שְׁנָיִם", "וכבשין", "and two rams,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר", "וארבעה' עשר חמל", "and fourteen yearling lambs —"),
        ("תְּמִימִם", "בני סנה צחאחא", "sound ones."),
    ],
    21: [
        # HE: וּמִנְחָתָם וְנִסְכֵּיהֶם לַפָּרִים לָאֵילִם וְלַכְּבָשִׂים בְּמִסְפָּרָם--כַּמִּשְׁפָּט
        # JA: וברהם ומזאגהם. לאלרת'ות' ואלכבאש ואלחמלאן. באחצאיהם עלי' אלסביל
        # EN: And their grain and their libation — for the bulls, and the rams, and the lambs — in their enumerated amounts, as is customary.
        ("וּמִנְחָתָם", "וברהם", "And their grain"),
        ("וְנִסְכֵּיהֶם", "ומזאגהם", "and their libation —"),
        ("לַפָּרִים", "לאלרת'ות'", "for the bulls,"),
        ("לָאֵילִם", "ואלכבאש", "and the rams,"),
        ("וְלַכְּבָשִׂים", "ואלחמלאן", "and the lambs —"),
        ("בְּמִסְפָּרָם", "באחצאיהם", "in their enumerated amounts,"),
        ("כַּמִּשְׁפָּט", "עלי' אלסביל", "as is customary."),
    ],
    22: [
        # HE: וּשְׂעִיר חַטָּאת אֶחָד מִלְּבַד עֹלַת הַתָּמִיד וּמִנְחָתָהּ וְנִסְכָּהּ
        # JA: ועתוד לאלד'כוה. סוא קרבאן אלדאים. וברה ומזאגה
        # EN: And a he-goat for the purification-offering — apart from the perpetual offering, its grain and its libation.
        ("וּשְׂעִיר", "ועתוד", "And a he-goat"),
        ("חַטָּאת אֶחָד", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the perpetual offering,"),
        ("וּמִנְחָתָהּ", "וברה", "its grain"),
        ("וְנִסְכָּהּ", "ומזאגה", "and its libation."),
    ],
    23: [
        # HE: וּבַיּוֹם הָרְבִיעִי פָּרִים עֲשָׂרָה אֵילִם שְׁנָיִם כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר תְּמִימִם
        # JA: ופי אליום אלראבע. עשרה רתות וכבשין. וארבעה' עשר חמל. בני סנה צחאחא
        # EN: And on the fourth day: ten bulls from the herd, and two rams, and fourteen yearling lambs — sound ones.
        ("וּבַיּוֹם", "ופי אליום", "And on the"),
        ("הָרְבִיעִי", "אלראבע", "fourth day:"),
        ("פָּרִים עֲשָׂרָה", "עשרה רתות", "ten bulls from the herd,"),
        ("אֵילִם שְׁנָיִם", "וכבשין", "and two rams,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר", "וארבעה' עשר חמל", "and fourteen yearling lambs —"),
        ("תְּמִימִם", "בני סנה צחאחא", "sound ones."),
    ],
    24: [
        # HE: מִנְחָתָם וְנִסְכֵּיהֶם לַפָּרִים לָאֵילִם וְלַכְּבָשִׂים בְּמִסְפָּרָם--כַּמִּשְׁפָּט
        # JA: וברהם ומזאגהם. לאלרת'ות' ואלכבאש ואלחמלאן. באחצאיהם עלי' אלסביל
        # EN: And their grain and their libation — for the bulls, and the rams, and the lambs — in their enumerated amounts, as is customary.
        ("מִנְחָתָם", "וברהם", "And their grain"),
        ("וְנִסְכֵּיהֶם", "ומזאגהם", "and their libation —"),
        ("לַפָּרִים", "לאלרת'ות'", "for the bulls,"),
        ("לָאֵילִם", "ואלכבאש", "and the rams,"),
        ("וְלַכְּבָשִׂים", "ואלחמלאן", "and the lambs —"),
        ("בְּמִסְפָּרָם", "באחצאיהם", "in their enumerated amounts,"),
        ("כַּמִּשְׁפָּט", "עלי' אלסביל", "as is customary."),
    ],
    25: [
        # HE: וּשְׂעִיר-עִזִּים אֶחָד חַטָּאת מִלְּבַד עֹלַת הַתָּמִיד מִנְחָתָהּ וְנִסְכָּהּ
        # JA: ועתוד מן אלמאעז לאלד'כוה. סוא קרבאן אלדאים. וברה ומזאגה
        # EN: And a he-goat from the goats for the purification-offering — apart from the perpetual offering, its grain and its libation.
        ("וּשְׂעִיר-עִזִּים אֶחָד", "ועתוד מן אלמאעז", "And a he-goat from the goats"),
        ("חַטָּאת", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the perpetual offering,"),
        ("מִנְחָתָהּ", "וברה", "its grain"),
        ("וְנִסְכָּהּ", "ומזאגה", "and its libation."),
    ],
    26: [
        # HE: וּבַיּוֹם הַחֲמִישִׁי פָּרִים תִּשְׁעָה אֵילִם שְׁנָיִם כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר תְּמִימִם
        # JA: ופי אליום אלכ'אמס. תסעה רתות' וכבשין. וארבעה' עשר חמל. בני סנה צחאחא
        # EN: And on the fifth day: nine bulls from the herd, and two rams, and fourteen yearling lambs — sound ones.
        ("וּבַיּוֹם", "ופי אליום", "And on the"),
        ("הַחֲמִישִׁי", "אלכ'אמס", "fifth day:"),
        ("פָּרִים תִּשְׁעָה", "תסעה רתות'", "nine bulls from the herd,"),
        ("אֵילִם שְׁנָיִם", "וכבשין", "and two rams,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר", "וארבעה' עשר חמל", "and fourteen yearling lambs —"),
        ("תְּמִימִם", "בני סנה צחאחא", "sound ones."),
    ],
    27: [
        # HE: וּמִנְחָתָם וְנִסְכֵּיהֶם לַפָּרִים לָאֵילִם וְלַכְּבָשִׂים בְּמִסְפָּרָם--כַּמִּשְׁפָּט
        # JA: וברהם ומזאגהם. לאלרת'ות' ואלכבאש ואלחמלאן. באחצאיהם עלי' אלסביל
        # EN: And their grain and their libation — for the bulls, and the rams, and the lambs — in their enumerated amounts, as is customary.
        ("וּמִנְחָתָם", "וברהם", "And their grain"),
        ("וְנִסְכֵּיהֶם", "ומזאגהם", "and their libation —"),
        ("לַפָּרִים", "לאלרת'ות'", "for the bulls,"),
        ("לָאֵילִם", "ואלכבאש", "and the rams,"),
        ("וְלַכְּבָשִׂים", "ואלחמלאן", "and the lambs —"),
        ("בְּמִסְפָּרָם", "באחצאיהם", "in their enumerated amounts,"),
        ("כַּמִּשְׁפָּט", "עלי' אלסביל", "as is customary."),
    ],
    28: [
        # HE: וּשְׂעִיר חַטָּאת אֶחָד מִלְּבַד עֹלַת הַתָּמִיד וּמִנְחָתָהּ וְנִסְכָּהּ
        # JA: ועתוד לאלד'כוה. סוא קרבאן אלדאים. וברה ומזאגה
        # EN: And a he-goat for the purification-offering — apart from the perpetual offering, its grain and its libation.
        ("וּשְׂעִיר", "ועתוד", "And a he-goat"),
        ("חַטָּאת אֶחָד", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the perpetual offering,"),
        ("וּמִנְחָתָהּ", "וברה", "its grain"),
        ("וְנִסְכָּהּ", "ומזאגה", "and its libation."),
    ],
    29: [
        # HE: וּבַיּוֹם הַשִּׁשִּׁי פָּרִים שְׁמֹנָה אֵילִם שְׁנָיִם כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר תְּמִימִם
        # JA: ופי אליום אלסאדס. ת'מאניה רתות' וכבשין. וארבעה' עשר חמל בני סנה צחאחא
        # EN: And on the sixth day: eight bulls from the herd, and two rams, and fourteen yearling lambs — sound ones.
        ("וּבַיּוֹם", "ופי אליום", "And on the"),
        ("הַשִּׁשִּׁי", "אלסאדס", "sixth day:"),
        ("פָּרִים שְׁמֹנָה", "ת'מאניה רתות'", "eight bulls from the herd,"),
        ("אֵילִם שְׁנָיִם", "וכבשין", "and two rams,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר", "וארבעה' עשר חמל", "and fourteen yearling lambs —"),
        ("תְּמִימִם", "בני סנה צחאחא", "sound ones."),
    ],
    30: [
        # HE: וּמִנְחָתָם וְנִסְכֵּיהֶם לַפָּרִים לָאֵילִם וְלַכְּבָשִׂים בְּמִסְפָּרָם--כַּמִּשְׁפָּט
        # JA: וברהם ומזאגהם. לאלרת'ות' ואלכבאש ולאלחמלאן. באחצאיהם עלי' אלסביל
        # EN: And their grain and their libation — for the bulls, and the rams, and the lambs — in their enumerated amounts, as is customary.
        ("וּמִנְחָתָם", "וברהם", "And their grain"),
        ("וְנִסְכֵּיהֶם", "ומזאגהם", "and their libation —"),
        ("לַפָּרִים", "לאלרת'ות'", "for the bulls,"),
        ("לָאֵילִם", "ואלכבאש", "and the rams,"),
        ("וְלַכְּבָשִׂים", "ולאלחמלאן", "and the lambs —"),
        ("בְּמִסְפָּרָם", "באחצאיהם", "in their enumerated amounts,"),
        ("כַּמִּשְׁפָּט", "עלי' אלסביל", "as is customary."),
    ],
    31: [
        # HE: וּשְׂעִיר חַטָּאת אֶחָד מִלְּבַד עֹלַת הַתָּמִיד מִנְחָתָהּ וּנְסָכֶיהָ
        # JA: ועתוד לאלד'כוה סוא קרבאן אלדאים וברהא ומזאגהא
        # EN: And a he-goat for the purification-offering — apart from the perpetual offering and its grain, and its libation.
        ("וּשְׂעִיר", "ועתוד", "And a he-goat"),
        ("חַטָּאת אֶחָד", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the perpetual offering"),
        ("מִנְחָתָהּ", "וברהא", "and its grain,"),
        ("וּנְסָכֶיהָ", "ומזאגהא", "and its libation."),
    ],
    32: [
        # HE: וּבַיּוֹם הַשְּׁבִיעִי פָּרִים שִׁבְעָה אֵילִם שְׁנָיִם כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר תְּמִימִם
        # JA: ופי אליום אלסאבע סבעה רתות' וכבשין. וארבעה' עשר חמל. בני סנה צחאחא
        # EN: And on the seventh day: seven bulls from the herd, and two rams, and fourteen yearling lambs — sound ones.
        ("וּבַיּוֹם", "ופי אליום", "And on the"),
        ("הַשְּׁבִיעִי", "אלסאבע", "seventh day:"),
        ("פָּרִים שִׁבְעָה", "סבעה רתות'", "seven bulls from the herd,"),
        ("אֵילִם שְׁנָיִם", "וכבשין", "and two rams,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה אַרְבָּעָה עָשָׂר", "וארבעה' עשר חמל", "and fourteen yearling lambs —"),
        ("תְּמִימִם", "בני סנה צחאחא", "sound ones."),
    ],
    33: [
        # HE: וּמִנְחָתָם וְנִסְכֵּהֶם לַפָּרִים לָאֵילִם וְלַכְּבָשִׂים בְּמִסְפָּרָם--כְּמִשְׁפָּטָם
        # JA: וברהם ומזאגהם. לאלרת'ות' ואלכבאש ואלחמלאן. באחצאיהם עלי' אלסביל
        # EN: And their grain and their libation — for the bulls, and the rams, and the lambs — in their enumerated amounts, as is customary.
        ("וּמִנְחָתָם", "וברהם", "And their grain"),
        ("וְנִסְכֵּהֶם", "ומזאגהם", "and their libation —"),
        ("לַפָּרִים", "לאלרת'ות'", "for the bulls,"),
        ("לָאֵילִם", "ואלכבאש", "and the rams,"),
        ("וְלַכְּבָשִׂים", "ואלחמלאן", "and the lambs —"),
        ("בְּמִסְפָּרָם", "באחצאיהם", "in their enumerated amounts,"),
        ("כְּמִשְׁפָּטָם", "עלי' אלסביל", "as is customary."),
    ],
    34: [
        # HE: וּשְׂעִיר חַטָּאת אֶחָד מִלְּבַד עֹלַת הַתָּמִיד מִנְחָתָהּ וְנִסְכָּהּ
        # JA: ועתוד לאלד'כוה. סוא קרבאן אלדאים. וברה ומזאגה
        # EN: And a he-goat for the purification-offering — apart from the perpetual offering, its grain and its libation.
        ("וּשְׂעִיר", "ועתוד", "And a he-goat"),
        ("חַטָּאת אֶחָד", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the perpetual offering,"),
        ("מִנְחָתָהּ", "וברה", "its grain"),
        ("וְנִסְכָּהּ", "ומזאגה", "and its libation."),
    ],
    35: [
        # HE: בַּיּוֹם הַשְּׁמִינִי--עֲצֶרֶת תִּהְיֶה לָכֶם כָּל-מְלֶאכֶת עֲבֹדָה לֹא תַעֲשׂוּ
        # JA: ופי אליום אלת'אמן. מכת' פי אלקדס יכון לכם. כל צנעה' מכסב לא תעמלו
        # EN: And on the eighth day, a sojourn in the sacred precinct shall be for you — no craft of gain shall you perform.
        ("בַּיּוֹם", "ופי אליום", "And on the"),
        ("הַשְּׁמִינִי", "אלת'אמן", "eighth day,"),
        ("עֲצֶרֶת", "מכת' פי אלקדס", "a sojourn in the sacred precinct"),
        ("תִּהְיֶה לָכֶם", "יכון לכם", "shall be for you —"),
        ("כָּל-מְלֶאכֶת עֲבֹדָה", "כל צנעה' מכסב", "no craft of gain"),
        ("לֹא תַעֲשׂוּ", "לא תעמלו", "shall you perform."),
    ],
    36: [
        # HE: וְהִקְרַבְתֶּם עֹלָה אִשֵּׁה רֵיחַ נִיחֹחַ לַיהוָה--פַּר אֶחָד אַיִל אֶחָד כְּבָשִׂים בְּנֵי-שָׁנָה שִׁבְעָה תְּמִימִם
        # JA: וקרבו צעידה. קרבאנא מקבולא מרצ'ייא ללה . רת'א ואחדא וכבשא. וסבעה חמלאן. בני סנה צחאחא
        # EN: And offer up an elevation-offering, an acceptable and pleasing offering to God: one bull, and one ram, and seven yearling lambs — sound ones.
        ("וְהִקְרַבְתֶּם", "וקרבו", "And offer up"),
        ("עֹלָה", "צעידה", "an elevation-offering,"),
        ("אִשֵּׁה רֵיחַ נִיחֹחַ", "קרבאנא מקבולא מרצ'ייא", "an acceptable and pleasing offering"),
        ("לַיהוָה", "ללה", "to God:"),
        ("פַּר אֶחָד", "רת'א ואחדא", "one bull,"),
        ("אַיִל אֶחָד", "וכבשא", "and one ram,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה שִׁבְעָה", "וסבעה חמלאן", "and seven yearling lambs —"),
        ("תְּמִימִם", "בני סנה צחאחא", "sound ones."),
    ],
    37: [
        # HE: מִנְחָתָם וְנִסְכֵּיהֶם לַפָּר לָאַיִל וְלַכְּבָשִׂים בְּמִסְפָּרָם--כַּמִּשְׁפָּט
        # JA: וברהא ומזאגהא. לאלרת' ואלכבש ואלחמלאן. באחצאיהם עלי' אלסביל
        # EN: And their grain and their libation — for the bull, and the ram, and the lambs — in their enumerated amounts, as is customary.
        ("מִנְחָתָם", "וברהא", "And their grain"),
        ("וְנִסְכֵּיהֶם", "ומזאגהא", "and their libation —"),
        ("לַפָּר", "לאלרת'", "for the bull,"),
        ("לָאַיִל", "ואלכבש", "and the ram,"),
        ("וְלַכְּבָשִׂים", "ואלחמלאן", "and the lambs —"),
        ("בְּמִסְפָּרָם", "באחצאיהם", "in their enumerated amounts,"),
        ("כַּמִּשְׁפָּט", "עלי' אלסביל", "as is customary."),
    ],
    38: [
        # HE: וּשְׂעִיר חַטָּאת אֶחָד מִלְּבַד עֹלַת הַתָּמִיד וּמִנְחָתָהּ וְנִסְכָּהּ
        # JA: ועתוד לאלד'כוה. סוא קרבאן אלדאים. וברה ומזאגה
        # EN: And a he-goat for the purification-offering — apart from the perpetual offering, its grain and its libation.
        ("וּשְׂעִיר", "ועתוד", "And a he-goat"),
        ("חַטָּאת אֶחָד", "לאלד'כוה", "for the purification-offering —"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the perpetual offering,"),
        ("וּמִנְחָתָהּ", "וברה", "its grain"),
        ("וְנִסְכָּהּ", "ומזאגה", "and its libation."),
    ],
    39: [
        # HE: אֵלֶּה תַּעֲשׂוּ לַיהוָה בְּמוֹעֲדֵיכֶם--לְבַד מִנִּדְרֵיכֶם וְנִדְבֹתֵיכֶם לְעֹלֹתֵיכֶם וּלְמִנְחֹתֵיכֶם וּלְנִסְכֵּיכֶם וּלְשַׁלְמֵיכֶם
        # JA: הד'א מא תקרבו ללה פי אעיאדכם. מא כ'לא נד'ורכם ותברעכם. מן צואעד והדאיא. ומזאג וד'בח סלאמה
        # EN: This is what you shall offer to God at your festivals — apart from your vows and your freewill-offerings, from elevation-offerings and gifts, and libation and the slaughter of well-being.
        ("אֵלֶּה", "הד'א", "This is"),
        ("תַּעֲשׂוּ", "מא תקרבו", "what you shall offer"),
        ("לַיהוָה", "ללה", "to God"),
        ("בְּמוֹעֲדֵיכֶם", "פי אעיאדכם", "at your festivals —"),
        ("לְבַד", "מא כ'לא", "apart from"),
        ("מִנִּדְרֵיכֶם", "נד'ורכם", "your vows"),
        ("וְנִדְבֹתֵיכֶם", "ותברעכם", "and your freewill-offerings,"),
        ("לְעֹלֹתֵיכֶם", "מן צואעד", "from elevation-offerings"),
        ("וּלְמִנְחֹתֵיכֶם", "והדאיא", "and gifts,"),
        ("וּלְנִסְכֵּיכֶם", "ומזאג", "and libation"),
        ("וּלְשַׁלְמֵיכֶם", "וד'בח סלאמה", "and the slaughter of well-being."),
    ],
}

"""Hand-authored word-level alignment triples for Bamidbar chapter 28."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר יְהוָה", "כלם אללה", "God spoke"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "directly."),
    ],
    2: [
        # HE: צַו אֶת-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם אֶת-קָרְבָּנִי לַחְמִי לְאִשַּׁי רֵיחַ נִיחֹחִי תִּשְׁמְרוּ לְהַקְרִיב לִי בְּמוֹעֲדוֹ
        # JA: מר בני אסראיל. וקל להם. קרבאני דאימי מרצ'יי מקבולי. אחפצוה. אן תקרבוה לי פי וקתה
        # EN: Command the sons of Israel, and say to them: My offering — continual, pleasing, accepted — take care to bring it to Me in its appointed time.
        ("צַו", "מר", "Command"),
        ("אֶת-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel,"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("אֶת-קָרְבָּנִי", "קרבאני", "My offering —"),
        ("לַחְמִי", "דאימי", "continual,"),
        ("לְאִשַּׁי", "מרצ'יי", "pleasing,"),
        ("רֵיחַ נִיחֹחִי", "מקבולי", "accepted —"),
        ("תִּשְׁמְרוּ", "אחפצוה", "take care"),
        ("לְהַקְרִיב לִי", "אן תקרבוה לי", "to bring it to Me"),
        ("בְּמוֹעֲדוֹ", "פי וקתה", "in its appointed time."),
    ],
    3: [
        # HE: וְאָמַרְתָּ לָהֶם--זֶה הָאִשֶּׁה אֲשֶׁר תַּקְרִיבוּ לַיהוָה כְּבָשִׂים בְּנֵי-שָׁנָה תְמִימִם שְׁנַיִם לַיּוֹם עֹלָה תָמִיד
        # JA: וביין להם. אן אלמרצ'י. אלד'י תקרבונה ללה . חמלין אבני סנה צחאחא. פי כל יום צעידה דאימא
        # EN: And make clear to them that the pleasing offering which you bring to God is two yearling male lambs without blemish — each day an offering, continually.
        ("וְאָמַרְתָּ", "וביין", "And make clear"),
        ("לָהֶם", "להם", "to them"),
        ("הָאִשֶּׁה", "אן אלמרצ'י", "that the pleasing offering"),
        ("אֲשֶׁר תַּקְרִיבוּ", "אלד'י תקרבונה", "which you bring"),
        ("לַיהוָה", "ללה", "to God"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה", "חמלין אבני סנה", "is two yearling male lambs"),
        ("תְמִימִם", "צחאחא", "without blemish —"),
        ("שְׁנַיִם לַיּוֹם", "פי כל יום", "each day"),
        ("עֹלָה", "צעידה", "an offering,"),
        ("תָמִיד", "דאימא", "continually."),
    ],
    4: [
        # HE: אֶת-הַכֶּבֶשׂ אֶחָד תַּעֲשֶׂה בַבֹּקֶר וְאֵת הַכֶּבֶשׂ הַשֵּׁנִי תַּעֲשֶׂה בֵּין הָעַרְבָּיִם
        # JA: אחדהמא באלג'דאה. ואלאכ'ר בין אלג'רובין
        # EN: One of them in the morning, and the other between the two settings.
        ("אֶת-הַכֶּבֶשׂ אֶחָד", "אחדהמא", "One of them"),
        ("בַבֹּקֶר", "באלג'דאה", "in the morning,"),
        ("וְאֵת הַכֶּבֶשׂ הַשֵּׁנִי", "ואלאכ'ר", "and the other"),
        ("בֵּין הָעַרְבָּיִם", "בין אלג'רובין", "between the two settings."),
    ],
    5: [
        # HE: וַעֲשִׂירִית הָאֵיפָה סֹלֶת לְמִנְחָה בְּלוּלָה בְּשֶׁמֶן כָּתִית רְבִיעִת הַהִין
        # JA: ועשר ויבה. סמד מן אלבר. מלתות. ברבע קסט מן דהן מטחון
        # EN: And a tenth of a waybah of fine wheat flour, mixed, with a quarter of a qist of pressed oil.
        ("וַעֲשִׂירִית", "ועשר", "And a tenth of"),
        ("הָאֵיפָה", "ויבה", "a waybah"),
        ("סֹלֶת", "סמד מן אלבר", "of fine wheat flour,"),
        ("בְּלוּלָה", "מלתות", "mixed,"),
        ("רְבִיעִת", "ברבע קסט", "with a quarter of a qist"),
        ("בְּשֶׁמֶן", "מן דהן", "of"),
        ("כָּתִית", "מטחון", "pressed oil."),
    ],
    6: [
        # HE: עֹלַת תָּמִיד--הָעֲשֻׂיָה בְּהַר סִינַי לְרֵיחַ נִיחֹחַ אִשֶּׁה לַיהוָה
        # JA: צעידה דאימא. כמא צנעת פי ברייה' סיני. מקבולה מרצ'ייה ללה
        # EN: A continual offering, as was done in the wilderness of Sinai — accepted and pleasing to God.
        ("עֹלַת תָּמִיד", "צעידה דאימא", "A continual offering,"),
        ("הָעֲשֻׂיָה", "כמא צנעת", "as was done"),
        ("בְּהַר סִינַי", "פי ברייה' סיני", "in the wilderness of Sinai —"),
        ("לְרֵיחַ נִיחֹחַ", "מקבולה", "accepted"),
        ("אִשֶּׁה", "מרצ'ייה", "and pleasing"),
        ("לַיהוָה", "ללה", "to God."),
    ],
    7: [
        # HE: וְנִסְכּוֹ רְבִיעִת הַהִין לַכֶּבֶשׂ הָאֶחָד בַּקֹּדֶשׁ הַסֵּךְ נֶסֶךְ שֵׁכָר--לַיהוָה
        # JA: ומעה מן אלמזאג. רבע קסט לכל חמל. ירש פי אלקדס רשא. מן עתיקה ללה
        # EN: And with it, from the mixed drink, a quarter of a qist for each lamb — to be poured in the sanctuary, a pouring from its aged kind, to God.
        ("וְנִסְכּוֹ", "ומעה", "And with it,"),
        ("רְבִיעִת הַהִין", "מן אלמזאג", "from the mixed drink,"),
        ("לַכֶּבֶשׂ הָאֶחָד", "רבע קסט לכל חמל", "a quarter of a qist for each lamb —"),
        ("בַּקֹּדֶשׁ", "ירש פי אלקדס", "to be poured in the sanctuary,"),
        ("הַסֵּךְ נֶסֶךְ", "רשא", "a pouring"),
        ("שֵׁכָר", "מן עתיקה", "from its aged kind,"),
        ("לַיהוָה", "ללה", "to God."),
    ],
    8: [
        # HE: וְאֵת הַכֶּבֶשׂ הַשֵּׁנִי תַּעֲשֶׂה בֵּין הָעַרְבָּיִם כְּמִנְחַת הַבֹּקֶר וּכְנִסְכּוֹ תַּעֲשֶׂה אִשֵּׁה רֵיחַ נִיחֹחַ לַיהוָה
        # JA: ואד'א צנעת אלחמל אלת'אני בין אלג'רובין. פכהדייה' אלג'דאה ומזאגהא איצ'א אצנעה. קרבאנא מקבולא מרצ'ייא ללה
        # EN: And when you make the second lamb between the two settings, make it like the gift of the morning and its mixed drink as well — an offering accepted and pleasing to God.
        ("וְאֵת הַכֶּבֶשׂ הַשֵּׁנִי", "ואד'א צנעת אלחמל אלת'אני", "And when you make the second lamb"),
        ("בֵּין הָעַרְבָּיִם", "בין אלג'רובין", "between the two settings,"),
        ("כְּמִנְחַת הַבֹּקֶר", "פכהדייה' אלג'דאה", "make it like the gift of the morning"),
        ("וּכְנִסְכּוֹ", "ומזאגהא", "and its mixed drink"),
        ("תַּעֲשֶׂה", "איצ'א אצנעה", "as well —"),
        ("אִשֵּׁה", "קרבאנא", "an offering"),
        ("רֵיחַ נִיחֹחַ", "מקבולא", "accepted"),
        ("לַיהוָה", "מרצ'ייא ללה", "and pleasing to God."),
    ],
    9: [
        # HE: וּבְיוֹם הַשַּׁבָּת--שְׁנֵי-כְבָשִׂים בְּנֵי-שָׁנָה תְּמִימִם וּשְׁנֵי עֶשְׂרֹנִים סֹלֶת מִנְחָה בְּלוּלָה בַשֶּׁמֶן--וְנִסְכּוֹ
        # JA: ופי יום אלסבת. חמלין אבני סנה צחאצא. ומעהמא מן אלבר עשרין. סמד מלתות בדהן ומזאגהם
        # EN: And on the Sabbath day: two yearling male lambs without blemish, and with them two tenths of fine wheat flour mixed with oil, and their mixed drink.
        ("וּבְיוֹם", "ופי יום", "And on the"),
        ("הַשַּׁבָּת", "אלסבת", "Sabbath day:"),
        ("שְׁנֵי-כְבָשִׂים בְּנֵי-שָׁנָה", "חמלין אבני סנה", "two yearling male lambs"),
        ("תְּמִימִם", "צחאצא", "without blemish,"),
        ("וּשְׁנֵי עֶשְׂרֹנִים", "ומעהמא מן אלבר עשרין", "and with them two tenths"),
        ("סֹלֶת מִנְחָה", "סמד", "of fine wheat flour"),
        ("בְּלוּלָה", "מלתות", "mixed"),
        ("בַשֶּׁמֶן", "בדהן", "with oil,"),
        ("וְנִסְכּוֹ", "ומזאגהם", "and their mixed drink."),
    ],
    10: [
        # HE: עֹלַת שַׁבַּת בְּשַׁבַּתּוֹ עַל-עֹלַת הַתָּמִיד וְנִסְכָּהּ
        # JA: ד'אלך קרבאן סבת בסבת. מע אלקרבאן אלדאים ומזאגה
        # EN: That is the offering of Sabbath by Sabbath, together with the continual offering and its mixed drink.
        ("עֹלַת שַׁבַּת", "ד'אלך קרבאן סבת", "That is the offering of Sabbath"),
        ("בְּשַׁבַּתּוֹ", "בסבת", "by Sabbath,"),
        ("עַל-עֹלַת הַתָּמִיד", "מע אלקרבאן אלדאים", "together with the continual offering"),
        ("וְנִסְכָּהּ", "ומזאגה", "and its mixed drink."),
    ],
    11: [
        # HE: וּבְרָאשֵׁי חָדְשֵׁיכֶם--תַּקְרִיבוּ עֹלָה לַיהוָה פָּרִים בְּנֵי-בָקָר שְׁנַיִם וְאַיִל אֶחָד כְּבָשִׂים בְּנֵי-שָׁנָה שִׁבְעָה תְּמִימִם
        # JA: ופי רוס שהורכם. קרבו קרבאן צעידה ללה . רת'ין מן אלבקר וכבשא. וסבעה' חמלאן בני סנה צחאחא
        # EN: And at the heads of your months, bring an offering — a burnt-offering to God: two bulls from the cattle, and a ram, and seven yearling lambs without blemish.
        ("וּבְרָאשֵׁי", "ופי רוס", "And at the heads of"),
        ("חָדְשֵׁיכֶם", "שהורכם", "your months,"),
        ("תַּקְרִיבוּ", "קרבו קרבאן", "bring an offering —"),
        ("עֹלָה", "צעידה", "a burnt-offering"),
        ("לַיהוָה", "ללה", "to God:"),
        ("פָּרִים בְּנֵי-בָקָר", "רת'ין מן אלבקר", "two bulls from the cattle,"),
        ("וְאַיִל אֶחָד", "וכבשא", "and a ram,"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה", "וסבעה' חמלאן בני סנה", "and seven yearling lambs"),
        ("שִׁבְעָה תְּמִימִם", "צחאחא", "without blemish."),
    ],
    12: [
        # HE: וּשְׁלֹשָׁה עֶשְׂרֹנִים סֹלֶת מִנְחָה בְּלוּלָה בַשֶּׁמֶן לַפָּר הָאֶחָד וּשְׁנֵי עֶשְׂרֹנִים סֹלֶת מִנְחָה בְּלוּלָה בַשֶּׁמֶן לָאַיִל הָאֶחָד
        # JA: ות'לאת'ה' עשור מן אלבר. סמד מלתות בדהן לכל רת'. ועשרין לאלכבש
        # EN: And three tenths of fine wheat flour mixed with oil for each bull, and two tenths for the ram.
        ("וּשְׁלֹשָׁה עֶשְׂרֹנִים", "ות'לאת'ה' עשור", "And three tenths"),
        ("סֹלֶת מִנְחָה", "מן אלבר. סמד", "of fine wheat flour"),
        ("בְּלוּלָה", "מלתות", "mixed"),
        ("בַשֶּׁמֶן", "בדהן", "with oil"),
        ("לַפָּר הָאֶחָד", "לכל רת'", "for each bull,"),
        ("וּשְׁנֵי עֶשְׂרֹנִים", "ועשרין", "and two tenths"),
        ("לָאַיִל הָאֶחָד", "לאלכבש", "for the ram."),
    ],
    13: [
        # HE: וְעִשָּׂרֹן עִשָּׂרוֹן סֹלֶת מִנְחָה בְּלוּלָה בַשֶּׁמֶן לַכֶּבֶשׂ הָאֶחָד עֹלָה רֵיחַ נִיחֹחַ אִשֶּׁה לַיהוָה
        # JA: ועשר לכל חמל כד'אך. אלצעידה אלמקבולה אלמרצ'ייה ללה
        # EN: And a tenth of fine flour mixed with oil for each lamb likewise — an offering accepted and pleasing to God.
        ("וְעִשָּׂרֹן עִשָּׂרוֹן", "ועשר", "And a tenth"),
        ("לַכֶּבֶשׂ הָאֶחָד", "לכל חמל", "for each lamb"),
        (None, "כד'אך", "likewise —"),
        ("עֹלָה", "אלצעידה", "an offering"),
        ("רֵיחַ נִיחֹחַ", "אלמקבולה", "accepted"),
        ("אִשֶּׁה", "אלמרצ'ייה", "and pleasing"),
        ("לַיהוָה", "ללה", "to God."),
    ],
    14: [
        # HE: וְנִסְכֵּיהֶם חֲצִי הַהִין יִהְיֶה לַפָּר וּשְׁלִישִׁת הַהִין לָאַיִל וּרְבִיעִת הַהִין לַכֶּבֶשׂ--יָיִן זֹאת עֹלַת חֹדֶשׁ בְּחָדְשׁוֹ לְחָדְשֵׁי הַשָּׁנָה
        # JA: ומזאגהם. יכון נצף קסט לכל ת'ור. ות'לת' קסט לאלכבש. ורבע קסט. לאלחמל מן אלשראב. הד'א קרבאן שהר בשהר. לשהור אלסנה
        # EN: And their mixed drink shall be: half a qist for each bull, and a third of a qist for the ram, and a quarter of a qist for the lamb — from the drink. This is the offering of month by month, for the months of the year.
        ("וְנִסְכֵּיהֶם", "ומזאגהם", "And their mixed drink"),
        ("חֲצִי הַהִין", "יכון נצף קסט", "shall be: half a qist"),
        ("לַפָּר", "לכל ת'ור", "for each bull,"),
        ("וּשְׁלִישִׁת הַהִין", "ות'לת' קסט", "and a third of a qist"),
        ("לָאַיִל", "לאלכבש", "for the ram,"),
        ("וּרְבִיעִת הַהִין", "ורבע קסט", "and a quarter of a qist"),
        ("לַכֶּבֶשׂ", "לאלחמל", "for the lamb —"),
        ("יָיִן", "מן אלשראב", "from the drink."),
        ("זֹאת עֹלַת חֹדֶשׁ", "הד'א קרבאן שהר", "This is the offering of month"),
        ("בְּחָדְשׁוֹ", "בשהר", "by month,"),
        ("לְחָדְשֵׁי הַשָּׁנָה", "לשהור אלסנה", "for the months of the year."),
    ],
    15: [
        # HE: וּשְׂעִיר עִזִּים אֶחָד לְחַטָּאת לַיהוָה עַל-עֹלַת הַתָּמִיד יֵעָשֶׂה וְנִסְכּוֹ
        # JA: ועתוד מן אלמאעז ד'כוה ללה . מע קרבאן אלדאים. יקרב ד'אלך ומזאגה
        # EN: And a male goat-kid as a purification-offering to God — together with the continual offering, that shall be brought, with its mixed drink.
        ("וּשְׂעִיר עִזִּים אֶחָד", "ועתוד מן אלמאעז", "And a male goat-kid"),
        ("לְחַטָּאת", "ד'כוה", "as a purification-offering"),
        ("לַיהוָה", "ללה", "to God —"),
        ("עַל-עֹלַת הַתָּמִיד", "מע קרבאן אלדאים", "together with the continual offering,"),
        ("יֵעָשֶׂה", "יקרב ד'אלך", "that shall be brought,"),
        ("וְנִסְכּוֹ", "ומזאגה", "with its mixed drink."),
    ],
    16: [
        # HE: וּבַחֹדֶשׁ הָרִאשׁוֹן בְּאַרְבָּעָה עָשָׂר יוֹם--לַחֹדֶשׁ פֶּסַח לַיהוָה
        # JA: ופי אלשהר אלאוול. פי אליום אלראבע עשר מנה. פסחא ללה
        # EN: And in the first month, on the fourteenth day of it — a Passover to God.
        ("וּבַחֹדֶשׁ", "ופי אלשהר", "And in the"),
        ("הָרִאשׁוֹן", "אלאוול", "first month,"),
        ("בְּאַרְבָּעָה עָשָׂר", "פי אליום אלראבע עשר", "on the fourteenth day"),
        ("יוֹם--לַחֹדֶשׁ", "מנה", "of it —"),
        ("פֶּסַח", "פסחא", "a Passover"),
        ("לַיהוָה", "ללה", "to God."),
    ],
    17: [
        # HE: וּבַחֲמִשָּׁה עָשָׂר יוֹם לַחֹדֶשׁ הַזֶּה חָג שִׁבְעַת יָמִים מַצּוֹת יֵאָכֵל
        # JA: ופי אליום אלכ'אמס עשר מנה חג. סבעה' אייאם יוכל פטירא
        # EN: And on the fifteenth day of it, a pilgrimage-festival: seven days shall unleavened bread be eaten.
        ("וּבַחֲמִשָּׁה עָשָׂר", "ופי אליום אלכ'אמס עשר", "And on the fifteenth day"),
        ("יוֹם לַחֹדֶשׁ הַזֶּה", "מנה", "of it,"),
        ("חָג", "חג", "a pilgrimage-festival:"),
        ("שִׁבְעַת יָמִים", "סבעה' אייאם", "seven days"),
        ("מַצּוֹת", "יוכל פטירא", "shall unleavened bread be eaten."),
    ],
    18: [
        # HE: בַּיּוֹם הָרִאשׁוֹן מִקְרָא-קֹדֶשׁ כָּל-מְלֶאכֶת עֲבֹדָה לֹא תַעֲשׂוּ
        # JA: פי אליום אלאוול מנהא אסם מקדס. כל צנעה' מכסב לא תעמלו
        # EN: On the first day of it — a consecrated name; no work for gain shall you do.
        ("בַּיּוֹם", "פי אליום", "On the"),
        ("הָרִאשׁוֹן", "אלאוול", "first day"),
        ("מִקְרָא-קֹדֶשׁ", "מנהא אסם מקדס", "of it — a consecrated name;"),
        ("כָּל-מְלֶאכֶת עֲבֹדָה", "כל צנעה' מכסב", "no work for gain"),
        ("לֹא תַעֲשׂוּ", "לא תעמלו", "shall you do."),
    ],
    19: [
        # HE: וְהִקְרַבְתֶּם אִשֶּׁה עֹלָה לַיהוָה פָּרִים בְּנֵי-בָקָר שְׁנַיִם וְאַיִל אֶחָד וְשִׁבְעָה כְבָשִׂים בְּנֵי שָׁנָה תְּמִימִם יִהְיוּ לָכֶם
        # JA: וקרבו קרבאנא צעידה ללה . רת'ין מן אלבקר וכבשא. וסבעה חמלאן בני סנה. צחאחא יכונאן לכם
        # EN: And bring an offering — a burnt-offering to God: two bulls from the cattle, and a ram, and seven yearling lambs; they shall be without blemish for you.
        ("וְהִקְרַבְתֶּם", "וקרבו קרבאנא", "And bring an offering —"),
        ("אִשֶּׁה עֹלָה", "צעידה", "a burnt-offering"),
        ("לַיהוָה", "ללה", "to God:"),
        ("פָּרִים בְּנֵי-בָקָר שְׁנַיִם", "רת'ין מן אלבקר", "two bulls from the cattle,"),
        ("וְאַיִל אֶחָד", "וכבשא", "and a ram,"),
        ("וְשִׁבְעָה כְבָשִׂים", "וסבעה חמלאן", "and seven yearling lambs;"),
        ("בְּנֵי שָׁנָה", "בני סנה", "they shall be"),
        ("תְּמִימִם יִהְיוּ לָכֶם", "צחאחא יכונאן לכם", "without blemish for you."),
    ],
    20: [
        # HE: וּמִנְחָתָם--סֹלֶת בְּלוּלָה בַשָּׁמֶן שְׁלֹשָׁה עֶשְׂרֹנִים לַפָּר וּשְׁנֵי עֶשְׂרֹנִים לָאַיִל--תַּעֲשׂוּ
        # JA: ומעהם מן אלבר. סמד מלתות בדהן. ת'לאת'ה' עשור לכל רת' ועשרין לאלכבש
        # EN: And with them from the grain: fine flour mixed with oil — three tenths for each bull, and two tenths for the ram.
        ("וּמִנְחָתָם", "ומעהם", "And with them"),
        ("סֹלֶת", "מן אלבר. סמד", "from the grain: fine flour"),
        ("בְּלוּלָה", "מלתות", "mixed"),
        ("בַשָּׁמֶן", "בדהן", "with oil —"),
        ("שְׁלֹשָׁה עֶשְׂרֹנִים", "ת'לאת'ה' עשור", "three tenths"),
        ("לַפָּר", "לכל רת'", "for each bull,"),
        ("וּשְׁנֵי עֶשְׂרֹנִים", "ועשרין", "and two tenths"),
        ("לָאַיִל", "לאלכבש", "for the ram."),
    ],
    21: [
        # HE: עִשָּׂרוֹן עִשָּׂרוֹן תַּעֲשֶׂה לַכֶּבֶשׂ הָאֶחָד--לְשִׁבְעַת הַכְּבָשִׂים
        # JA: ועשר לכל חמל מן אלסבעה
        # EN: And a tenth for each lamb from the seven.
        ("עִשָּׂרוֹן עִשָּׂרוֹן", "ועשר", "And a tenth"),
        ("לַכֶּבֶשׂ הָאֶחָד", "לכל חמל", "for each lamb"),
        ("לְשִׁבְעַת הַכְּבָשִׂים", "מן אלסבעה", "from the seven."),
    ],
    22: [
        # HE: וּשְׂעִיר חַטָּאת אֶחָד לְכַפֵּר עֲלֵיכֶם
        # JA: ועתוד לאלד'כוה. ליסתג'פר ענכם
        # EN: And a male goat-kid for the purification-offering, to seek forgiveness for you.
        ("וּשְׂעִיר חַטָּאת אֶחָד", "ועתוד", "And a male goat-kid"),
        ("לְכַפֵּר", "לאלד'כוה", "for the purification-offering,"),
        (None, "ליסתג'פר", "to seek forgiveness"),
        ("עֲלֵיכֶם", "ענכם", "for you."),
    ],
    23: [
        # HE: מִלְּבַד עֹלַת הַבֹּקֶר אֲשֶׁר לְעֹלַת הַתָּמִיד--תַּעֲשׂוּ אֶת-אֵלֶּה
        # JA: מא כ'לא קרבאן אלג'דאה. וקרבאן אלדאים אלת'אני. תקרבו הד'ה
        # EN: Apart from the morning offering and the second continual offering — these you shall bring.
        ("מִלְּבַד", "מא כ'לא", "Apart from"),
        ("עֹלַת הַבֹּקֶר", "קרבאן אלג'דאה", "the morning offering"),
        ("אֲשֶׁר לְעֹלַת הַתָּמִיד", "וקרבאן אלדאים אלת'אני", "and the second continual offering —"),
        ("תַּעֲשׂוּ אֶת-אֵלֶּה", "תקרבו הד'ה", "these you shall bring."),
    ],
    24: [
        # HE: כָּאֵלֶּה תַּעֲשׂוּ לַיּוֹם שִׁבְעַת יָמִים--לֶחֶם אִשֵּׁה רֵיחַ-נִיחֹחַ לַיהוָה עַל-עוֹלַת הַתָּמִיד יֵעָשֶׂה וְנִסְכּוֹ
        # JA: ומת'להא קרבו פי כל יום מן אלסבעה אלאייאם. קרבאנא מקבולא מרצ'ייא ללה . מע אלקרבאן אלדאים. יקרב ד'אלך ומזאגה
        # EN: And the like of it bring on each day of the seven days — an offering accepted and pleasing to God; together with the continual offering, that shall be brought, with its mixed drink.
        ("כָּאֵלֶּה תַּעֲשׂוּ", "ומת'להא קרבו", "And the like of it bring"),
        ("לַיּוֹם", "פי כל יום", "on each day"),
        ("שִׁבְעַת יָמִים", "מן אלסבעה אלאייאם", "of the seven days —"),
        ("לֶחֶם אִשֵּׁה", "קרבאנא", "an offering"),
        ("רֵיחַ-נִיחֹחַ", "מקבולא", "accepted"),
        ("לַיהוָה", "מרצ'ייא ללה", "and pleasing to God;"),
        ("עַל-עוֹלַת הַתָּמִיד", "מע אלקרבאן אלדאים", "together with the continual offering,"),
        ("יֵעָשֶׂה", "יקרב ד'אלך", "that shall be brought,"),
        ("וְנִסְכּוֹ", "ומזאגה", "with its mixed drink."),
    ],
    25: [
        # HE: וּבַיּוֹם הַשְּׁבִיעִי--מִקְרָא-קֹדֶשׁ יִהְיֶה לָכֶם כָּל-מְלֶאכֶת עֲבֹדָה לֹא תַעֲשׂוּ
        # JA: ופי אליום אלסאבע. אסם מקדס יכון לכם. כל צנעה' מכסב לא תעמלו
        # EN: And on the seventh day — a consecrated name shall be for you; no work for gain shall you do.
        ("וּבַיּוֹם", "ופי אליום", "And on the"),
        ("הַשְּׁבִיעִי", "אלסאבע", "seventh day —"),
        ("מִקְרָא-קֹדֶשׁ", "אסם מקדס", "a consecrated name"),
        ("יִהְיֶה לָכֶם", "יכון לכם", "shall be for you;"),
        ("כָּל-מְלֶאכֶת עֲבֹדָה", "כל צנעה' מכסב", "no work for gain"),
        ("לֹא תַעֲשׂוּ", "לא תעמלו", "shall you do."),
    ],
    26: [
        # HE: וּבְיוֹם הַבִּכּוּרִים בְּהַקְרִיבְכֶם מִנְחָה חֲדָשָׁה לַיהוָה--בְּשָׁבֻעֹתֵיכֶם מִקְרָא-קֹדֶשׁ יִהְיֶה לָכֶם כָּל-מְלֶאכֶת עֲבֹדָה לֹא תַעֲשׂוּ
        # JA: ופי יום אלבכור. פי תקריבכם. ברא גדידא ללה . בעד אסאביעכם אסם מקדס יכון לכם. כל צנעה' מכסב לא תעמלו
        # EN: And on the day of first-fruits, when you bring a new grain-offering to God — after your weeks — a consecrated name shall be for you; no work for gain shall you do.
        ("וּבְיוֹם הַבִּכּוּרִים", "ופי יום אלבכור", "And on the day of first-fruits,"),
        ("בְּהַקְרִיבְכֶם", "פי תקריבכם", "when you bring"),
        ("מִנְחָה חֲדָשָׁה", "ברא גדידא", "a new grain-offering"),
        ("לַיהוָה", "ללה", "to God —"),
        ("בְּשָׁבֻעֹתֵיכֶם", "בעד אסאביעכם", "after your weeks —"),
        ("מִקְרָא-קֹדֶשׁ", "אסם מקדס", "a consecrated name"),
        ("יִהְיֶה לָכֶם", "יכון לכם", "shall be for you;"),
        ("כָּל-מְלֶאכֶת עֲבֹדָה", "כל צנעה' מכסב", "no work for gain"),
        ("לֹא תַעֲשׂוּ", "לא תעמלו", "shall you do."),
    ],
    27: [
        # HE: וְהִקְרַבְתֶּם עוֹלָה לְרֵיחַ נִיחֹחַ לַיהוָה--פָּרִים בְּנֵי-בָקָר שְׁנַיִם אַיִל אֶחָד שִׁבְעָה כְבָשִׂים בְּנֵי שָׁנָה
        # JA: וקרבו צעידה. מקבולה מרצ'ייה ללה. ר'תין מן אלבקר וכבשא. וסבעה' חמלאן בני סנה
        # EN: And bring a burnt-offering, accepted and pleasing to God: two bulls from the cattle, and a ram, and seven yearling lambs.
        ("וְהִקְרַבְתֶּם", "וקרבו", "And bring"),
        ("עוֹלָה", "צעידה", "a burnt-offering,"),
        ("לְרֵיחַ נִיחֹחַ", "מקבולה", "accepted"),
        ("לַיהוָה", "מרצ'ייה ללה", "and pleasing to God:"),
        ("פָּרִים בְּנֵי-בָקָר שְׁנַיִם", "ר'תין מן אלבקר", "two bulls from the cattle,"),
        ("אַיִל אֶחָד", "וכבשא", "and a ram,"),
        ("שִׁבְעָה כְבָשִׂים בְּנֵי שָׁנָה", "וסבעה' חמלאן בני סנה", "and seven yearling lambs."),
    ],
    28: [
        # HE: וּמִנְחָתָם--סֹלֶת בְּלוּלָה בַשָּׁמֶן שְׁלֹשָׁה עֶשְׂרֹנִים לַפָּר הָאֶחָד שְׁנֵי עֶשְׂרֹנִים לָאַיִל הָאֶחָד
        # JA: ומעהם מן אלבר. סמד מלתות בדהן. ת'לאת'ה' עשור לכל רת'. ועשרין לאלכבש
        # EN: And with them from the grain: fine flour mixed with oil — three tenths for each bull, and two tenths for the ram.
        ("וּמִנְחָתָם", "ומעהם", "And with them"),
        ("סֹלֶת", "מן אלבר. סמד", "from the grain: fine flour"),
        ("בְּלוּלָה", "מלתות", "mixed"),
        ("בַשָּׁמֶן", "בדהן", "with oil —"),
        ("שְׁלֹשָׁה עֶשְׂרֹנִים", "ת'לאת'ה' עשור", "three tenths"),
        ("לַפָּר הָאֶחָד", "לכל רת'", "for each bull,"),
        ("שְׁנֵי עֶשְׂרֹנִים", "ועשרין", "and two tenths"),
        ("לָאַיִל הָאֶחָד", "לאלכבש", "for the ram."),
    ],
    29: [
        # HE: עִשָּׂרוֹן עִשָּׂרוֹן לַכֶּבֶשׂ הָאֶחָד--לְשִׁבְעַת הַכְּבָשִׂים
        # JA: ועשר לכל חמל מן אלסבעה
        # EN: And a tenth for each lamb from the seven.
        ("עִשָּׂרוֹן עִשָּׂרוֹן", "ועשר", "And a tenth"),
        ("לַכֶּבֶשׂ הָאֶחָד", "לכל חמל", "for each lamb"),
        ("לְשִׁבְעַת הַכְּבָשִׂים", "מן אלסבעה", "from the seven."),
    ],
    30: [
        # HE: שְׂעִיר עִזִּים אֶחָד לְכַפֵּר עֲלֵיכֶם
        # JA: ועתוד מן אלמאעז. ליסתג'פר ענכם
        # EN: And a male goat-kid from the goats, to seek forgiveness for you.
        ("שְׂעִיר עִזִּים אֶחָד", "ועתוד מן אלמאעז", "And a male goat-kid from the goats,"),
        (None, "ליסתג'פר", "to seek forgiveness"),
        ("לְכַפֵּר עֲלֵיכֶם", "ענכם", "for you."),
    ],
    31: [
        # HE: מִלְּבַד עֹלַת הַתָּמִיד וּמִנְחָתוֹ--תַּעֲשׂוּ תְּמִימִם יִהְיוּ-לָכֶם וְנִסְכֵּיהֶם
        # JA: מא כ'לא קרבאן אלדאים. וברה תקרבו ד'אלך. וצחאחא תכון לכם ומזאגהא
        # EN: Apart from the continual offering and its grain — these you shall bring; without blemish shall they be for you, and their mixed drink.
        ("מִלְּבַד", "מא כ'לא", "Apart from"),
        ("עֹלַת הַתָּמִיד", "קרבאן אלדאים", "the continual offering"),
        ("וּמִנְחָתוֹ", "וברה", "and its grain —"),
        ("תַּעֲשׂוּ", "תקרבו ד'אלך", "these you shall bring;"),
        ("תְּמִימִם יִהְיוּ-לָכֶם", "וצחאחא תכון לכם", "without blemish shall they be for you,"),
        ("וְנִסְכֵּיהֶם", "ומזאגהא", "and their mixed drink."),
    ],
}

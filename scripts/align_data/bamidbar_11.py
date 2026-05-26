"""Hand-authored word-level alignment triples for Bamidbar chapter 11."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    2: [
        # HE: וַיִּצְעַק הָעָם אֶל-מֹשֶׁה וַיִּתְפַּלֵּל מֹשֶׁה אֶל-יְהוָה וַתִּשְׁקַע הָאֵשׁ
        # JA: פצרך' אלקום אלי' מוסי'. פדעא רבה. פג'ארת אלנאר
        # EN: And the people cried out to Moses; and he prayed to his Lord, and the fire died down.
        ("וַיִּצְעַק הָעָם", "פצרך' אלקום", "And the people cried out"),
        ("אֶל-מֹשֶׁה", "אלי' מוסי'", "to Moses;"),
        ("וַיִּתְפַּלֵּל מֹשֶׁה", "פדעא", "and he prayed"),
        ("אֶל-יְהוָה", "רבה", "to his Lord,"),
        ("וַתִּשְׁקַע הָאֵשׁ", "פג'ארת אלנאר", "and the fire died down."),
    ],
    3: [
        # HE: וַיִּקְרָא שֵׁם-הַמָּקוֹם הַהוּא תַּבְעֵרָה כִּי-בָעֲרָה בָם אֵשׁ יְהוָה
        # JA: פסמא ד'אלך אלמוצ'ע אלמשתעלה. למא אשתעלת פיהם נאר אללה
        # EN: And he called that place 'the Blazing,' because the fire of God had blazed among them.
        ("וַיִּקְרָא", "פסמא", "And he called"),
        ("שֵׁם-הַמָּקוֹם הַהוּא", "ד'אלך אלמוצ'ע", "that place"),
        ("תַּבְעֵרָה", "אלמשתעלה", "'the Blazing,'"),
        ("כִּי-בָעֲרָה", "למא אשתעלת", "because"),
        ("אֵשׁ יְהוָה", "נאר אללה", "the fire of God"),
        ("בָם", "פיהם", "had blazed among them."),
    ],
    4: [
        # HE: וְהָאסַפְסֻף אֲשֶׁר בְּקִרְבּוֹ הִתְאַוּוּ תַּאֲוָה וַיָּשֻׁבוּ וַיִּבְכּוּ גַּם בְּנֵי יִשְׂרָאֵל וַיֹּאמְרוּ מִי יַאֲכִלֵנוּ בָּשָׂר
        # JA: ואללפיף אלד'ין פי מא בינהם. תשהו שהוה. פרגע איצ'א בני אסראיל מעהם. פבכו וקאלו. מן יטעמנא לחמא
        # EN: And the mixed multitude who were among them craved a craving; and the sons of Israel also turned back with them, and they wept and said: 'Who shall feed us meat?'
        ("וְהָאסַפְסֻף", "ואללפיף", "And the mixed multitude"),
        ("אֲשֶׁר בְּקִרְבּוֹ", "אלד'ין פי מא בינהם", "who were among them"),
        ("הִתְאַוּוּ", "תשהו", "craved"),
        ("תַּאֲוָה", "שהוה", "a craving;"),
        ("וַיָּשֻׁבוּ", "פרגע", "and the sons of Israel"),
        (None, "איצ'א", "also"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "turned back"),
        (None, "מעהם", "with them,"),
        ("וַיִּבְכּוּ", "פבכו", "and they wept"),
        ("וַיֹּאמְרוּ", "וקאלו", "and said:"),
        ("מִי יַאֲכִלֵנוּ", "מן יטעמנא", "'Who shall feed us"),
        ("בָּשָׂר", "לחמא", "meat?'"),
    ],
    5: [
        # HE: זָכַרְנוּ אֶת-הַדָּגָה אֲשֶׁר-נֹאכַל בְּמִצְרַיִם חִנָּם אֵת הַקִּשֻּׁאִים וְאֵת הָאֲבַטִּחִים וְאֶת-הֶחָצִיר וְאֶת-הַבְּצָלִים וְאֶת-הַשּׁוּמִים
        # JA: פד'כרנא אלסמך. אלד'י כנא נאכלה במצר מגאנא. אלקת'א ואלבטיך'. ואלכראת' ואלבצל ואלתום
        # EN: We remember the fish which we used to eat in Egypt for nothing — the cucumbers and the melons, and the leeks and the onions and the garlic.
        ("זָכַרְנוּ", "פד'כרנא", "We remember"),
        ("אֶת-הַדָּגָה", "אלסמך", "the fish"),
        ("אֲשֶׁר-נֹאכַל", "אלד'י כנא נאכלה", "which we used to eat"),
        ("בְּמִצְרַיִם", "במצר", "in Egypt"),
        ("חִנָּם", "מגאנא", "for nothing —"),
        ("אֵת הַקִּשֻּׁאִים", "אלקת'א", "the cucumbers"),
        ("וְאֵת הָאֲבַטִּחִים", "ואלבטיך'", "and the melons,"),
        ("וְאֶת-הֶחָצִיר", "ואלכראת'", "and the leeks"),
        ("וְאֶת-הַבְּצָלִים", "ואלבצל", "and the onions"),
        ("וְאֶת-הַשּׁוּמִים", "ואלתום", "and the garlic."),
    ],
    6: [
        # HE: וְעַתָּה נַפְשֵׁנוּ יְבֵשָׁה אֵין כֹּל--בִּלְתִּי אֶל-הַמָּן עֵינֵינוּ
        # JA: ואלאן. פנפוסנא יאבסה ממא ליס שי. ואנמא עיוננא אלי' אלמן ממדודה
        # EN: And now our souls are dried up, as though there were nothing at all — for our eyes are stretched only toward the manna.
        ("וְעַתָּה", "ואלאן", "And now"),
        ("נַפְשֵׁנוּ", "פנפוסנא", "our souls are"),
        ("יְבֵשָׁה", "יאבסה", "dried up,"),
        ("אֵין כֹּל", "ממא ליס שי", "as though there were nothing at all —"),
        (None, "ואנמא", "for our eyes"),
        ("עֵינֵינוּ", "עיוננא", "are stretched"),
        ("בִּלְתִּי אֶל-הַמָּן", "אלי' אלמן ממדודה", "only toward the manna."),
    ],
    7: [
        # HE: וְהַמָּן כִּזְרַע-גַּד הוּא וְעֵינוֹ כְּעֵין הַבְּדֹלַח
        # JA: וכאן אלמן כבזר אלכבזרה. ולונה כלון אללולו
        # EN: And the manna was like the seed of coriander, and its color was like the color of pearls.
        ("וְהַמָּן", "וכאן אלמן", "And the manna was"),
        ("כִּזְרַע-גַּד", "כבזר אלכבזרה", "like the seed of coriander,"),
        ("וְעֵינוֹ", "ולונה", "and its color was"),
        (None, "כלון", "like the color of"),
        ("הַבְּדֹלַח", "אללולו", "pearls."),
    ],
    8: [
        # HE: שָׁטוּ הָעָם וְלָקְטוּ וְטָחֲנוּ בָרֵחַיִם אוֹ דָכוּ בַּמְּדֹכָה וּבִשְּׁלוּ בַּפָּרוּר וְעָשׂוּ אֹתוֹ עֻגוֹת וְהָיָה טַעְמוֹ כְּטַעַם לְשַׁד הַשָּׁמֶן
        # JA: יטוף אלקום פילקטונה ויטחנון מנה פי אלרחא. או ידקון באלמדק. ויטבכון מנה פי אלבראם. ויצנעון מנה מלילא. ויכון טעמה כחלאוה בדסם
        # EN: The people would go about and gather it, and grind it in the millstone or pound it in the mortar, and cook it in the pots, and make of it a roasted cake; and its taste was like the sweetness of something rich with fat.
        ("שָׁטוּ הָעָם", "יטוף אלקום", "The people would go about"),
        ("וְלָקְטוּ", "פילקטונה", "and gather it,"),
        ("וְטָחֲנוּ בָרֵחַיִם", "ויטחנון מנה פי אלרחא", "and grind it in the millstone"),
        ("אוֹ דָכוּ בַּמְּדֹכָה", "או ידקון באלמדק", "or pound it in the mortar,"),
        ("וּבִשְּׁלוּ בַּפָּרוּר", "ויטבכון מנה פי אלבראם", "and cook it in the pots,"),
        ("וְעָשׂוּ אֹתוֹ עֻגוֹת", "ויצנעון מנה מלילא", "and make of it a roasted cake;"),
        ("וְהָיָה", "ויכון", "and its taste was"),
        ("טַעְמוֹ", "טעמה", "like the sweetness of"),
        ("כְּטַעַם לְשַׁד הַשָּׁמֶן", "כחלאוה בדסם", "something rich with fat."),
    ],
    9: [
        # HE: וּבְרֶדֶת הַטַּל עַל-הַמַּחֲנֶה לָיְלָה יֵרֵד הַמָּן עָלָיו
        # JA: וענד נזול אלטל. עלי' אלעסכר לילא. ינזל אלמן עליה
        # EN: And when the dew descended upon the camp at night, the manna would descend upon it.
        ("וּבְרֶדֶת הַטַּל", "וענד נזול אלטל", "And when the dew descended"),
        ("עַל-הַמַּחֲנֶה", "עלי' אלעסכר", "upon the camp"),
        ("לָיְלָה", "לילא", "at night,"),
        ("יֵרֵד הַמָּן", "ינזל אלמן", "the manna would descend"),
        ("עָלָיו", "עליה", "upon it."),
    ],
    10: [
        # HE: וַיִּשְׁמַע מֹשֶׁה אֶת-הָעָם בֹּכֶה לְמִשְׁפְּחֹתָיו--אִישׁ לְפֶתַח אָהֳלוֹ וַיִּחַר-אַף יְהוָה מְאֹד וּבְעֵינֵי מֹשֶׁה רָע
        # JA: פלמא סמע מוסי' אלקום. יבכון לעשאירהם. כל אמר עלי' באב כ'באיה. פאשתד ג'צב אללה גדא. וסא ד'אלך ענד מוסי'
        # EN: And when Moses heard the people weeping for their clans — every man at the door of his tent — God's anger was greatly intensified, and it was grievous in the sight of Moses.
        ("וַיִּשְׁמַע מֹשֶׁה", "פלמא סמע מוסי'", "And when Moses heard"),
        ("אֶת-הָעָם", "אלקום", "the people"),
        ("בֹּכֶה", "יבכון", "weeping"),
        ("לְמִשְׁפְּחֹתָיו", "לעשאירהם", "for their clans —"),
        ("אִישׁ", "כל אמר", "every man"),
        ("לְפֶתַח אָהֳלוֹ", "עלי' באב כ'באיה", "at the door of his tent —"),
        ("וַיִּחַר-אַף יְהוָה", "פאשתד ג'צב אללה", "God's anger was greatly"),
        ("מְאֹד", "גדא", "intensified,"),
        ("וּבְעֵינֵי מֹשֶׁה רָע", "וסא ד'אלך ענד מוסי'", "and it was grievous in the sight of Moses."),
    ],
    11: [
        # HE: וַיֹּאמֶר מֹשֶׁה אֶל-יְהוָה לָמָה הֲרֵעֹתָ לְעַבְדֶּךָ וְלָמָּה לֹא-מָצָתִי חֵן בְּעֵינֶיךָ לָשׂוּם אֶת-מַשָּׂא כָּל-הָעָם הַזֶּה--עָלָי
        # JA: פקאל מוסי' ללה. לם אבלית עבדך. ולם לם אגד חצ'אא ענדך. אד' ציירת. גמיע כלפה' הולאי אלקום עליי
        # EN: And Moses said to God: 'Why have You brought trial upon Your servant, and why have I not found favor before You, since You have placed the whole burden of the management of these people upon me?'
        ("וַיֹּאמֶר מֹשֶׁה", "פקאל מוסי'", "And Moses said"),
        ("אֶל-יְהוָה", "ללה", "to God:"),
        ("לָמָה הֲרֵעֹתָ", "לם אבלית", "'Why have You brought trial"),
        ("לְעַבְדֶּךָ", "עבדך", "upon Your servant,"),
        ("וְלָמָּה לֹא-מָצָתִי חֵן", "ולם לם אגד חצ'אא", "and why have I not found favor"),
        ("בְּעֵינֶיךָ", "ענדך", "before You,"),
        ("לָשׂוּם", "אד' ציירת", "since You have placed"),
        ("אֶת-מַשָּׂא כָּל-הָעָם הַזֶּה", "גמיע כלפה' הולאי אלקום", "the whole burden of the management of these people"),
        ("עָלָי", "עליי", "upon me?'"),
    ],
    12: [
        # HE: הֶאָנֹכִי הָרִיתִי אֵת כָּל-הָעָם הַזֶּה--אִם-אָנֹכִי יְלִדְתִּיהוּ כִּי-תֹאמַר אֵלַי שָׂאֵהוּ בְחֵיקֶךָ כַּאֲשֶׁר יִשָּׂא הָאֹמֵן אֶת-הַיֹּנֵק עַל הָאֲדָמָה אֲשֶׁר נִשְׁבַּעְתָּ לַאֲבֹתָיו
        # JA: הל אנא חמלתהם. אם ולדתהם. אד' קלת לי סוסהם. כאנך תחמלהם פי חגרך. כמא יחמל אלחאצ'ן אלרצ'יע. אלי' אלבלד. אלד'י קסמת לאבאיהם
        # EN: 'Did I conceive them, or did I beget them, that You said to me: Tend them — as though You would carry them in Your lap, as a nurse carries an infant — to the land which You allotted to their fathers?'
        ("הֶאָנֹכִי הָרִיתִי", "הל אנא חמלתהם", "'Did I conceive them,"),
        ("אִם-אָנֹכִי יְלִדְתִּיהוּ", "אם ולדתהם", "or did I beget them,"),
        ("כִּי-תֹאמַר אֵלַי", "אד' קלת לי", "that You said to me:"),
        ("שָׂאֵהוּ", "סוסהם", "Tend them —"),
        ("בְחֵיקֶךָ", "כאנך תחמלהם פי חגרך", "as though You would carry them in Your lap,"),
        ("כַּאֲשֶׁר יִשָּׂא הָאֹמֵן", "כמא יחמל אלחאצ'ן", "as a nurse carries"),
        ("אֶת-הַיֹּנֵק", "אלרצ'יע", "an infant —"),
        ("עַל הָאֲדָמָה", "אלי' אלבלד", "to the land"),
        ("אֲשֶׁר נִשְׁבַּעְתָּ", "אלד'י קסמת", "which You allotted"),
        ("לַאֲבֹתָיו", "לאבאיהם", "to their fathers?'"),
    ],
    13: [
        # HE: מֵאַיִן לִי בָּשָׂר לָתֵת לְכָל-הָעָם הַזֶּה כִּי-יִבְכּוּ עָלַי לֵאמֹר תְּנָה-לָּנוּ בָשָׂר וְנֹאכֵלָה
        # JA: מן אין לי לחם. אעטי גמיעהם. אד' יבכון עליי ויקולון. אעטנא לחמא נאכלה
        # EN: 'From where do I have meat to give to all of them, when they weep over me and say: Give us meat that we may eat?'
        ("מֵאַיִן", "מן אין", "'From where"),
        ("לִי בָּשָׂר", "לי לחם", "do I have meat"),
        ("לָתֵת", "אעטי", "to give"),
        ("לְכָל-הָעָם הַזֶּה", "גמיעהם", "to all of them,"),
        ("כִּי-יִבְכּוּ", "אד' יבכון", "when they weep"),
        ("עָלַי", "עליי", "over me"),
        ("לֵאמֹר", "ויקולון", "and say:"),
        ("תְּנָה-לָּנוּ", "אעטנא", "Give us"),
        ("בָשָׂר", "לחמא", "meat"),
        ("וְנֹאכֵלָה", "נאכלה", "that we may eat?'"),
    ],
    14: [
        # HE: לֹא-אוּכַל אָנֹכִי לְבַדִּי לָשֵׂאת אֶת-כָּל-הָעָם הַזֶּה כִּי כָבֵד מִמֶּנִּי
        # JA: לא אטיק אנא ואחדי אן אסוסהם. בל הו ת'קיל עליי
        # EN: 'I alone cannot manage them; it is too heavy for me.'
        ("לֹא-אוּכַל", "לא אטיק", "'I alone cannot"),
        ("אָנֹכִי לְבַדִּי", "אנא ואחדי", "manage them;"),
        ("לָשֵׂאת אֶת-כָּל-הָעָם הַזֶּה", "אן אסוסהם", "it is"),
        (None, "בל", "too"),
        ("כִּי כָבֵד", "הו ת'קיל", "heavy"),
        ("מִמֶּנִּי", "עליי", "for me.'"),
    ],
    15: [
        # HE: וְאִם-כָּכָה אַתְּ-עֹשֶׂה לִּי הָרְגֵנִי נָא הָרֹג--אִם-מָצָאתִי חֵן בְּעֵינֶיךָ וְאַל-אֶרְאֶה בְּרָעָתִי
        # JA: ואן כנת אלזמתניה עקובה. פאגעלהא אמאתתי. אן וגדת חצ'אא ענדך. ולא ארא בלייתי
        # EN: 'And if You have bound me to it as a punishment, then let that punishment be my death — if I have found favor before You — that I may not see my affliction.'
        ("וְאִם-כָּכָה אַתְּ-עֹשֶׂה לִּי", "ואן כנת אלזמתניה", "'And if You have bound me to it"),
        ("הָרְגֵנִי נָא הָרֹג", "עקובה", "as a punishment,"),
        (None, "פאגעלהא", "then let that punishment be"),
        (None, "אמאתתי", "my death —"),
        ("אִם-מָצָאתִי חֵן", "אן וגדת חצ'אא", "if I have found favor"),
        ("בְּעֵינֶיךָ", "ענדך", "before You —"),
        ("וְאַל-אֶרְאֶה בְּרָעָתִי", "ולא ארא בלייתי", "that I may not see my affliction.'"),
    ],
    16: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה אֶסְפָה-לִּי שִׁבְעִים אִישׁ מִזִּקְנֵי יִשְׂרָאֵל אֲשֶׁר יָדַעְתָּ כִּי-הֵם זִקְנֵי הָעָם וְשֹׁטְרָיו וְלָקַחְתָּ אֹתָם אֶל-אֹהֶל מוֹעֵד וְהִתְיַצְּבוּ שָׁם עִמָּךְ
        # JA: פקאל אללה למוסי'. אגמע לי סבעין רגלא מן שיוך' בני אסראיל. אלד'ין תעלם אנהם שיוכ'הם וערפאהם. וכ'דהם אלי' כ'בא אלמחצ'ר. ויקפון ת'ם מעך
        # EN: And God said to Moses: 'Gather for me seventy men from the elders of the sons of Israel — those whom you know to be their elders and their overseers — and take them to the tent of the assembly, and let them stand there with you.'
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses:"),
        ("אֶסְפָה-לִּי", "אגמע לי", "'Gather for me"),
        ("שִׁבְעִים אִישׁ", "סבעין רגלא", "seventy men"),
        ("מִזִּקְנֵי יִשְׂרָאֵל", "מן שיוך' בני אסראיל", "from the elders of the sons of Israel —"),
        ("אֲשֶׁר יָדַעְתָּ", "אלד'ין תעלם", "those whom you know"),
        ("כִּי-הֵם זִקְנֵי הָעָם", "אנהם שיוכ'הם", "to be their elders"),
        ("וְשֹׁטְרָיו", "וערפאהם", "and their overseers —"),
        ("וְלָקַחְתָּ אֹתָם", "וכ'דהם", "and take them"),
        ("אֶל-אֹהֶל מוֹעֵד", "אלי' כ'בא אלמחצ'ר", "to the tent of the assembly,"),
        ("וְהִתְיַצְּבוּ", "ויקפון", "and let them stand"),
        ("שָׁם עִמָּךְ", "ת'ם מעך", "there with you.'"),
    ],
    17: [
        # HE: וְיָרַדְתִּי וְדִבַּרְתִּי עִמְּךָ שָׁם וְאָצַלְתִּי מִן-הָרוּחַ אֲשֶׁר עָלֶיךָ וְשַׂמְתִּי עֲלֵיהֶם וְנָשְׂאוּ אִתְּךָ בְּמַשָּׂא הָעָם וְלֹא-תִשָּׂא אַתָּה לְבַדֶּךָ
        # JA: חתי אתגלא ואכ'אטבך הנאך. ואפידהם מן אלנור אלד'י עלי' וגהך ואגעלה עליהם. פי'עאונונך פי סיאסה' אלקום. ולא תסוסהם אנת וחדך
        # EN: 'Until I appear and speak with you there, and I shall impart to them of the light which is upon your face and set it upon them; so they shall assist you in the governance of the people, and you shall not govern them alone.'
        ("וְיָרַדְתִּי", "חתי אתגלא", "'Until I appear"),
        ("וְדִבַּרְתִּי עִמְּךָ שָׁם", "ואכ'אטבך הנאך", "and speak with you there,"),
        ("וְאָצַלְתִּי", "ואפידהם", "and I shall impart to them"),
        ("מִן-הָרוּחַ", "מן אלנור", "of the light"),
        ("אֲשֶׁר עָלֶיךָ", "אלד'י עלי' וגהך", "which is upon your face"),
        ("וְשַׂמְתִּי עֲלֵיהֶם", "ואגעלה עליהם", "and set it upon them;"),
        ("וְנָשְׂאוּ אִתְּךָ", "פי'עאונונך", "so they shall assist you"),
        ("בְּמַשָּׂא הָעָם", "פי סיאסה' אלקום", "in the governance of the people,"),
        ("וְלֹא-תִשָּׂא אַתָּה לְבַדֶּךָ", "ולא תסוסהם אנת וחדך", "and you shall not govern them alone.'"),
    ],
    18: [
        # HE: וְאֶל-הָעָם תֹּאמַר הִתְקַדְּשׁוּ לְמָחָר וַאֲכַלְתֶּם בָּשָׂר--כִּי בְּכִיתֶם בְּאָזְנֵי יְהוָה לֵאמֹר מִי יַאֲכִלֵנוּ בָּשָׂר כִּי-טוֹב לָנוּ בְּמִצְרָיִם וְנָתַן יְהוָה לָכֶם בָּשָׂר וַאֲכַלְתֶּם
        # JA: וקל לאלקום. אסתעדו אלי' ג'ד חתא תאכלון לחמא. לאגל מא בכיתם בין ידי אללה וקלתם. מן יטעמנא לחמא. וכאן אלאצלח לנא במצר. פיעטיכם אללה. לחמא תאכלונה
        # EN: 'And say to the people: Prepare yourselves until tomorrow, that you may eat meat — because you have wept before God and said: Who shall feed us meat? For it was better for us in Egypt. So God shall give you meat that you shall eat.'
        ("וְאֶל-הָעָם תֹּאמַר", "וקל לאלקום", "'And say to the people:"),
        ("הִתְקַדְּשׁוּ", "אסתעדו", "Prepare yourselves"),
        ("לְמָחָר", "אלי' ג'ד", "until tomorrow,"),
        ("וַאֲכַלְתֶּם בָּשָׂר", "חתא תאכלון לחמא", "that you may eat meat —"),
        ("כִּי בְּכִיתֶם", "לאגל מא בכיתם", "because you have wept"),
        ("בְּאָזְנֵי יְהוָה", "בין ידי אללה", "before God"),
        ("לֵאמֹר", "וקלתם", "and said:"),
        ("מִי יַאֲכִלֵנוּ בָּשָׂר", "מן יטעמנא לחמא", "Who shall feed us meat?"),
        ("כִּי-טוֹב לָנוּ בְּמִצְרָיִם", "וכאן אלאצלח לנא במצר", "For it was better for us in Egypt."),
        ("וְנָתַן יְהוָה לָכֶם", "פיעטיכם אללה", "So God shall give you"),
        ("בָּשָׂר וַאֲכַלְתֶּם", "לחמא תאכלונה", "meat that you shall eat.'"),
    ],
    19: [
        # HE: לֹא יוֹם אֶחָד תֹּאכְלוּן וְלֹא יוֹמָיִם וְלֹא חֲמִשָּׁה יָמִים וְלֹא עֲשָׂרָה יָמִים וְלֹא עֶשְׂרִים יוֹם
        # JA: לא יום ואחד. תאכלונה ולא יומין. ולא כ'מסה ולא עשרה. ולא עשרין
        # EN: 'Not one day shall you eat it, and not two days, and not five, and not ten, and not twenty —'
        ("לֹא יוֹם אֶחָד", "לא יום ואחד", "'Not one day"),
        ("תֹּאכְלוּן", "תאכלונה", "shall you eat it,"),
        ("וְלֹא יוֹמָיִם", "ולא יומין", "and not two days,"),
        ("וְלֹא חֲמִשָּׁה יָמִים", "ולא כ'מסה", "and not five,"),
        ("וְלֹא עֲשָׂרָה יָמִים", "ולא עשרה", "and not ten,"),
        ("וְלֹא עֶשְׂרִים יוֹם", "ולא עשרין", "and not twenty —'"),
    ],
    20: [
        # HE: עַד חֹדֶשׁ יָמִים עַד אֲשֶׁר-יֵצֵא מֵאַפְּכֶם וְהָיָה לָכֶם לְזָרָא יַעַן כִּי-מְאַסְתֶּם אֶת-יְהוָה אֲשֶׁר בְּקִרְבְּכֶם וַתִּבְכּוּ לְפָנָיו לֵאמֹר לָמָּה זֶּה יָצָאנוּ מִמִּצְרָיִם
        # JA: אלא אלי' אייאם שהר. אלי' אן יכ'רג מן אנאפכם מת'לא. ויציר לכם הזאלא. לאגל מא זהדתם. פי נור אללה אלד'י פי מא בינכם. ובכיתם בין ידיה וקלתם. לם כ'רגנא מן מצר
        # EN: 'but for the days of a month, until it comes out of your nostrils as a byword, and becomes a disgrace to you — because you have shown contempt for the light of God which is among you, and you wept before Him and said: Why did we ever leave Egypt?'
        ("עַד חֹדֶשׁ יָמִים", "אלא אלי' אייאם שהר", "'but for the days of a month,"),
        ("עַד אֲשֶׁר-יֵצֵא", "אלי' אן יכ'רג", "until it comes out"),
        ("מֵאַפְּכֶם", "מן אנאפכם", "of your nostrils"),
        (None, "מת'לא", "as a byword,"),
        ("וְהָיָה לָכֶם לְזָרָא", "ויציר לכם הזאלא", "and becomes a disgrace to you —"),
        ("יַעַן כִּי-מְאַסְתֶּם", "לאגל מא זהדתם", "because you have shown contempt"),
        ("אֶת-יְהוָה", "פי נור אללה", "for the light of God"),
        ("אֲשֶׁר בְּקִרְבְּכֶם", "אלד'י פי מא בינכם", "which is among you,"),
        ("וַתִּבְכּוּ לְפָנָיו", "ובכיתם בין ידיה", "and you wept before Him"),
        ("לֵאמֹר", "וקלתם", "and said:"),
        ("לָמָּה זֶּה יָצָאנוּ מִמִּצְרָיִם", "לם כ'רגנא מן מצר", "Why did we ever leave Egypt?'"),
    ],
    21: [
        # HE: וַיֹּאמֶר מֹשֶׁה שֵׁשׁ-מֵאוֹת אֶלֶף רַגְלִי הָעָם אֲשֶׁר אָנֹכִי בְּקִרְבּוֹ וְאַתָּה אָמַרְתָּ בָּשָׂר אֶתֵּן לָהֶם וְאָכְלוּ חֹדֶשׁ יָמִים
        # JA: קאל מוסי'. סת מאיה' אלף רגל ראגל. אלקום אלד'י אנא פי מא בינהם. ואנת קלת. אעטיהם לחמא. יאכלונה שהרא
        # EN: Moses said: 'Six hundred thousand men on foot are the people among whom I am — and You said: I shall give them meat that they shall eat for a month!'
        ("וַיֹּאמֶר מֹשֶׁה", "קאל מוסי'", "Moses said:"),
        ("שֵׁשׁ-מֵאוֹת אֶלֶף", "סת מאיה' אלף", "'Six hundred thousand"),
        ("רַגְלִי", "רגל ראגל", "men on foot"),
        ("הָעָם", "אלקום", "are the people"),
        ("אֲשֶׁר אָנֹכִי בְּקִרְבּוֹ", "אלד'י אנא פי מא בינהם", "among whom I am —"),
        ("וְאַתָּה אָמַרְתָּ", "ואנת קלת", "and You said:"),
        ("בָּשָׂר אֶתֵּן לָהֶם", "אעטיהם לחמא", "I shall give them meat"),
        ("וְאָכְלוּ חֹדֶשׁ יָמִים", "יאכלונה שהרא", "that they shall eat for a month!'"),
    ],
    22: [
        # HE: הֲצֹאן וּבָקָר יִשָּׁחֵט לָהֶם וּמָצָא לָהֶם אִם אֶת-כָּל-דְּגֵי הַיָּם יֵאָסֵף לָהֶם וּמָצָא לָהֶם
        # JA: פמן אענאתהם. אג'נם ובקר תד'בח להם פתכפיהם. או גמיע סמך אלבחר. יחאש להם פיקנעהם
        # EN: 'Then for their relief — shall flocks and herds be slaughtered for them so as to suffice them? Or shall all the fish of the sea be netted for them so as to satisfy them?'
        (None, "פמן אענאתהם", "'Then for their relief —"),
        ("הֲצֹאן", "אג'נם", "shall flocks"),
        ("וּבָקָר", "ובקר", "and herds"),
        ("יִשָּׁחֵט לָהֶם", "תד'בח להם", "be slaughtered for them"),
        ("וּמָצָא לָהֶם", "פתכפיהם", "so as to suffice them?"),
        ("אִם אֶת-כָּל-דְּגֵי הַיָּם", "או גמיע סמך אלבחר", "Or shall all the fish of the sea"),
        ("יֵאָסֵף לָהֶם", "יחאש להם", "be netted for them"),
        (None, "פיקנעהם", "so as to satisfy them?'"),
    ],
    23: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה הֲיַד יְהוָה תִּקְצָר עַתָּה תִרְאֶה הֲיִקְרְךָ דְבָרִי אִם-לֹא
        # JA: פקאל אללה למוסי'. הל קדרה' אללה תקצר. אלאן תנצ'ר. איואפיכם כלאמי אם לא
        # EN: And God said to Moses: 'Is the power of God too short? Now you shall see whether My word comes to you or not.'
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses:"),
        ("הֲיַד יְהוָה תִּקְצָר", "הל קדרה' אללה תקצר", "'Is the power of God too short?"),
        ("עַתָּה תִרְאֶה", "אלאן תנצ'ר", "Now you shall see"),
        ("הֲיִקְרְךָ דְבָרִי", "איואפיכם כלאמי", "whether My word comes to you"),
        ("אִם-לֹא", "אם לא", "or not.'"),
    ],
    24: [
        # HE: וַיֵּצֵא מֹשֶׁה--וַיְדַבֵּר אֶל-הָעָם אֵת דִּבְרֵי יְהוָה וַיֶּאֱסֹף שִׁבְעִים אִישׁ מִזִּקְנֵי הָעָם וַיַּעֲמֵד אֹתָם סְבִיבֹת הָאֹהֶל
        # JA: פכ'רג מוסי'. ואכ'בר אלקום בכלאם אללה. וגמע. סבעין רגלא מן שיוכ'הם. ואוקפהם חואלי אלכ'בא
        # EN: And Moses went out and informed the people of the word of God; and he gathered seventy men from their elders, and stationed them around the tent.
        ("וַיֵּצֵא מֹשֶׁה", "פכ'רג מוסי'", "And Moses went out"),
        ("וַיְדַבֵּר אֶל-הָעָם", "ואכ'בר אלקום", "and informed the people"),
        ("אֵת דִּבְרֵי יְהוָה", "בכלאם אללה", "of the word of God;"),
        ("וַיֶּאֱסֹף", "וגמע", "and he gathered"),
        ("שִׁבְעִים אִישׁ", "סבעין רגלא", "seventy men"),
        ("מִזִּקְנֵי הָעָם", "מן שיוכ'הם", "from their elders,"),
        ("וַיַּעֲמֵד אֹתָם", "ואוקפהם", "and stationed them"),
        ("סְבִיבֹת הָאֹהֶל", "חואלי אלכ'בא", "around the tent."),
    ],
    25: [
        # HE: וַיֵּרֶד יְהוָה בֶּעָנָן וַיְדַבֵּר אֵלָיו וַיָּאצֶל מִן-הָרוּחַ אֲשֶׁר עָלָיו וַיִּתֵּן עַל-שִׁבְעִים אִישׁ הַזְּקֵנִים וַיְהִי כְּנוֹחַ עֲלֵיהֶם הָרוּחַ וַיִּתְנַבְּאוּ וְלֹא יָסָפוּ
        # JA: פתגלא אללה פי אלג'מאם וכ'אטבה. ואפאד. מן אלנור אלד'י עליה. וכסא אלסבעין אלרגל אלשיוך'. פלמא אסתקר עליהם ד'אלך אלנור. תנבו ולם יחתאגו אלי' עודה
        # EN: And God appeared in the cloud and spoke with him; and He imparted of the light which was upon him, and covered the seventy elder men with it; and when that light settled upon them, they prophesied — and they had no need to return to it.
        ("וַיֵּרֶד יְהוָה", "פתגלא אללה", "And God appeared"),
        ("בֶּעָנָן", "פי אלג'מאם", "in the cloud"),
        ("וַיְדַבֵּר אֵלָיו", "וכ'אטבה", "and spoke with him;"),
        ("וַיָּאצֶל", "ואפאד", "and He imparted"),
        ("מִן-הָרוּחַ אֲשֶׁר עָלָיו", "מן אלנור אלד'י עליה", "of the light which was upon him,"),
        ("וַיִּתֵּן עַל-שִׁבְעִים אִישׁ הַזְּקֵנִים", "וכסא אלסבעין אלרגל אלשיוך'", "and covered the seventy elder men with it;"),
        ("וַיְהִי כְּנוֹחַ עֲלֵיהֶם הָרוּחַ", "פלמא אסתקר עליהם ד'אלך אלנור", "and when that light settled upon them,"),
        ("וַיִּתְנַבְּאוּ", "תנבו", "they prophesied —"),
        ("וְלֹא יָסָפוּ", "ולם יחתאגו אלי' עודה", "and they had no need to return to it."),
    ],
    26: [
        # HE: וַיִּשָּׁאֲרוּ שְׁנֵי-אֲנָשִׁים בַּמַּחֲנֶה שֵׁם הָאֶחָד אֶלְדָּד וְשֵׁם הַשֵּׁנִי מֵידָד וַתָּנַח עֲלֵהֶם הָרוּחַ וְהֵמָּה בַּכְּתֻבִים וְלֹא יָצְאוּ הָאֹהֱלָה וַיִּתְנַבְּאוּ בַּמַּחֲנֶה
        # JA: ובקי רגלאן פי אלעסכר. אסם אחדהמא אלדד. ואלת'אני מידד ואסתקרת עליהם אלנבווה. והמא מן אלמכתובין. ולם יכ'רגו אלי' אלכ'בא. בל תנבו פי אלעסכר
        # EN: And two men remained in the camp — the name of one of them was Eldad, and the second Medad — and the prophecy settled upon them; and they were among those who were registered, but they had not gone out to the tent; rather, they prophesied in the camp.
        ("וַיִּשָּׁאֲרוּ שְׁנֵי-אֲנָשִׁים", "ובקי רגלאן", "And two men remained"),
        ("בַּמַּחֲנֶה", "פי אלעסכר", "in the camp —"),
        ("שֵׁם הָאֶחָד אֶלְדָּד", "אסם אחדהמא אלדד", "the name of one of them was Eldad,"),
        ("וְשֵׁם הַשֵּׁנִי מֵידָד", "ואלת'אני מידד", "and the second Medad —"),
        ("וַתָּנַח עֲלֵהֶם הָרוּחַ", "ואסתקרת עליהם אלנבווה", "and the prophecy settled upon them;"),
        ("וְהֵמָּה בַּכְּתֻבִים", "והמא מן אלמכתובין", "and they were among those who were registered,"),
        ("וְלֹא יָצְאוּ הָאֹהֱלָה", "ולם יכ'רגו אלי' אלכ'בא", "but they had not gone out to the tent;"),
        ("וַיִּתְנַבְּאוּ בַּמַּחֲנֶה", "בל תנבו פי אלעסכר", "rather, they prophesied in the camp."),
    ],
    27: [
        # HE: וַיָּרָץ הַנַּעַר וַיַּגֵּד לְמֹשֶׁה וַיֹּאמַר אֶלְדָּד וּמֵידָד מִתְנַבְּאִים בַּמַּחֲנֶה
        # JA: פחאצ'ר אלג'לאם. ואכ'בר מוסי' וקאל. אלדד ומידד. מתנביין פי אלעסכר
        # EN: And the youth came hurrying and informed Moses, and said: 'Eldad and Medad are prophesying in the camp.'
        ("וַיָּרָץ הַנַּעַר", "פחאצ'ר אלג'לאם", "And the youth came hurrying"),
        ("וַיַּגֵּד לְמֹשֶׁה", "ואכ'בר מוסי'", "and informed Moses,"),
        ("וַיֹּאמַר", "וקאל", "and said:"),
        ("אֶלְדָּד וּמֵידָד", "אלדד ומידד", "'Eldad and Medad"),
        ("מִתְנַבְּאִים", "מתנביין", "are prophesying"),
        ("בַּמַּחֲנֶה", "פי אלעסכר", "in the camp.'"),
    ],
    28: [
        # HE: וַיַּעַן יְהוֹשֻׁעַ בִּן-נוּן מְשָׁרֵת מֹשֶׁה מִבְּחֻרָיו--וַיֹּאמַר אֲדֹנִי מֹשֶׁה כְּלָאֵם
        # JA: פאגאבה יהושע אבן נון. כ'אדם מוסי'. מן תלאמידה וקאל. יא סיידי יא מוסי' אחבסהמא
        # EN: And Joshua son of Nun, Moses' attendant, one of his disciples, answered and said: 'My lord, O Moses — restrain them!'
        ("וַיַּעַן יְהוֹשֻׁעַ בִּן-נוּן", "פאגאבה יהושע אבן נון", "And Joshua son of Nun,"),
        ("מְשָׁרֵת מֹשֶׁה", "כ'אדם מוסי'", "Moses' attendant,"),
        ("מִבְּחֻרָיו", "מן תלאמידה", "one of his disciples,"),
        ("וַיֹּאמַר", "וקאל", "answered and said:"),
        (None, "יא סיידי יא מוסי'", "'My lord, O Moses —"),
        ("כְּלָאֵם", "אחבסהמא", "restrain them!'"),
    ],
    29: [
        # HE: וַיֹּאמֶר לוֹ מֹשֶׁה הַמְקַנֵּא אַתָּה לִי וּמִי יִתֵּן כָּל-עַם יְהוָה נְבִיאִים--כִּי-יִתֵּן יְהוָה אֶת-רוּחוֹ עֲלֵיהֶם
        # JA: קאל לה מוסי'. הל תג'אר לי. לית צאר גמיע אמה' אללה אנביא. באן יגעל מן נורה ונבוותה עליהם
        # EN: And Moses said to him: 'Are you jealous on my behalf? Would that all the nation of God might become prophets — that He might set of His light and His prophecy upon them!'
        ("וַיֹּאמֶר לוֹ מֹשֶׁה", "קאל לה מוסי'", "And Moses said to him:"),
        ("הַמְקַנֵּא אַתָּה לִי", "הל תג'אר לי", "'Are you jealous on my behalf?"),
        (None, "לית", "Would that"),
        ("וּמִי יִתֵּן כָּל-עַם יְהוָה", "צאר גמיע אמה' אללה", "all the nation of God"),
        ("נְבִיאִים", "אנביא", "might become prophets —"),
        ("כִּי-יִתֵּן יְהוָה אֶת-רוּחוֹ", "באן יגעל מן נורה ונבוותה", "that He might set of His light and His prophecy"),
        ("עֲלֵיהֶם", "עליהם", "upon them!'"),
    ],
    30: [
        # HE: וַיֵּאָסֵף מֹשֶׁה אֶל-הַמַּחֲנֶה--הוּא וְזִקְנֵי יִשְׂרָאֵל
        # JA: פלמא אנצ'ם מוסי' אלי' אלעסכר. הו ושיוך בני אסראיל
        # EN: And when Moses rejoined the camp — he and the elders of the sons of Israel —
        ("וַיֵּאָסֵף מֹשֶׁה", "פלמא אנצ'ם מוסי'", "And when Moses rejoined"),
        ("אֶל-הַמַּחֲנֶה", "אלי' אלעסכר", "the camp —"),
        (None, "הו", "he"),
        ("וְזִקְנֵי יִשְׂרָאֵל", "ושיוך בני אסראיל", "and the elders of the sons of Israel —"),
    ],
    31: [
        # HE: וְרוּחַ נָסַע מֵאֵת יְהוָה וַיָּגָז שַׂלְוִים מִן-הַיָּם וַיִּטֹּשׁ עַל-הַמַּחֲנֶה כְּדֶרֶךְ יוֹם כֹּה וּכְדֶרֶךְ יוֹם כֹּה סְבִיבוֹת הַמַּחֲנֶה--וּכְאַמָּתַיִם עַל-פְּנֵי הָאָרֶץ
        # JA: והבת ריח מן ענד אללה. וקטעת סלוי מן אלבחר. ואלקתה עלי' אלעסכר שביה כמסיר יום ימנה ויסרה חואלי אלעסכר. וארתפאעה מן אלארץ' ד'ראעין
        # EN: a wind blew from God, and it drove quail in from the sea and cast them upon the camp, like a day's journey to the right and to the left around the camp; and their height from the ground was two cubits.
        ("וְרוּחַ נָסַע", "והבת ריח", "a wind blew"),
        ("מֵאֵת יְהוָה", "מן ענד אללה", "from God,"),
        ("וַיָּגָז שַׂלְוִים", "וקטעת סלוי", "and it drove quail in"),
        ("מִן-הַיָּם", "מן אלבחר", "from the sea"),
        ("וַיִּטֹּשׁ עַל-הַמַּחֲנֶה", "ואלקתה עלי' אלעסכר", "and cast them upon the camp,"),
        ("כְּדֶרֶךְ יוֹם כֹּה", "שביה כמסיר יום", "like a day's journey"),
        ("וּכְדֶרֶךְ יוֹם כֹּה", "ימנה ויסרה", "to the right and to the left"),
        ("סְבִיבוֹת הַמַּחֲנֶה", "חואלי אלעסכר", "around the camp;"),
        ("וּכְאַמָּתַיִם עַל-פְּנֵי הָאָרֶץ", "וארתפאעה מן אלארץ' ד'ראעין", "and their height from the ground was two cubits."),
    ],
    32: [
        # HE: וַיָּקָם הָעָם כָּל-הַיּוֹם הַהוּא וְכָל-הַלַּיְלָה וְכֹל יוֹם הַמָּחֳרָת וַיַּאַסְפוּ אֶת-הַשְּׂלָו--הַמַּמְעִיט אָסַף עֲשָׂרָה חֳמָרִים וַיִּשְׁטְחוּ לָהֶם שָׁטוֹחַ סְבִיבוֹת הַמַּחֲנֶה
        # JA: פקאם אלקום. באקי יומהם ולילתהם. וטול נהאר ג'דהם פגמעו אלסלוי. אקלהם. גמע עשרה אנאביר. פסטחוה להם סטוחא. חואלי אלעסכר
        # EN: And the people rose — the remainder of their day and their night and the length of the next day — and gathered the quail; the least among them gathered ten heaps; and they spread them out as layers around the camp.
        ("וַיָּקָם הָעָם", "פקאם אלקום", "And the people rose —"),
        ("כָּל-הַיּוֹם הַהוּא וְכָל-הַלַּיְלָה", "באקי יומהם ולילתהם", "the remainder of their day and their night"),
        ("וְכֹל יוֹם הַמָּחֳרָת", "וטול נהאר ג'דהם", "and the length of the next day —"),
        ("וַיַּאַסְפוּ אֶת-הַשְּׂלָו", "פגמעו אלסלוי", "and gathered the quail;"),
        ("הַמַּמְעִיט", "אקלהם", "the least among them"),
        ("אָסַף עֲשָׂרָה חֳמָרִים", "גמע עשרה אנאביר", "gathered ten heaps;"),
        ("וַיִּשְׁטְחוּ לָהֶם שָׁטוֹחַ", "פסטחוה להם סטוחא", "and they spread them out as layers"),
        ("סְבִיבוֹת הַמַּחֲנֶה", "חואלי אלעסכר", "around the camp."),
    ],
    33: [
        # HE: הַבָּשָׂר עוֹדֶנּוּ בֵּין שִׁנֵּיהֶם--טֶרֶם יִכָּרֵת וְאַף יְהוָה חָרָה בָעָם וַיַּךְ יְהוָה בָּעָם מַכָּה רַבָּה מְאֹד
        # JA: ואלחם בעד בין אסנאנהם. קבל אן ימצ'ג'וה. אד' אשתד ג'צ'ב אללה עליהם. פצ'רבהם צ'רבה ]עט'ימה] ]עט'ימה] עצ'ימה גדא
        # EN: While the meat was still between their teeth, before they had chewed it, God's anger grew fierce against them, and He struck them with a very great blow.
        ("הַבָּשָׂר עוֹדֶנּוּ", "ואלחם בעד", "While the meat was still"),
        ("בֵּין שִׁנֵּיהֶם", "בין אסנאנהם", "between their teeth,"),
        ("טֶרֶם יִכָּרֵת", "קבל אן ימצ'ג'וה", "before they had chewed it,"),
        ("וְאַף יְהוָה חָרָה בָעָם", "אד' אשתד ג'צ'ב אללה עליהם", "God's anger grew fierce against them,"),
        ("וַיַּךְ יְהוָה בָּעָם", "פצ'רבהם", "and He struck them"),
        ("מַכָּה רַבָּה מְאֹד", "צ'רבה ]עט'ימה] ]עט'ימה] עצ'ימה גדא", "with a very great blow."),
    ],
    34: [
        # HE: וַיִּקְרָא אֶת-שֵׁם-הַמָּקוֹם הַהוּא קִבְרוֹת הַתַּאֲוָה כִּי-שָׁם קָבְרוּ אֶת-הָעָם הַמִּתְאַוִּים
        # JA: וסמא ד'אלך אלמוצ'ע קבור אלשהוה. לאנהם דפנו הנאך. אלקום אלמתשהיין
        # EN: And he called that place 'the Graves of Craving,' because there they buried the people who had craved.
        ("וַיִּקְרָא אֶת-שֵׁם-הַמָּקוֹם הַהוּא", "וסמא ד'אלך אלמוצ'ע", "And he called that place"),
        ("קִבְרוֹת הַתַּאֲוָה", "קבור אלשהוה", "'the Graves of Craving,'"),
        ("כִּי-שָׁם קָבְרוּ", "לאנהם דפנו הנאך", "because there they buried"),
        ("אֶת-הָעָם", "אלקום", "the people"),
        ("הַמִּתְאַוִּים", "אלמתשהיין", "who had craved."),
    ],
    35: [
        # HE: מִקִּבְרוֹת הַתַּאֲוָה נָסְעוּ הָעָם חֲצֵרוֹת וַיִּהְיוּ בַּחֲצֵרוֹת
        # JA: ורחלו מנה אלי' חצרות. פלמא אקאמו בהא
        # EN: And they journeyed from there to Hazeroth; and when they settled there.
        ("מִקִּבְרוֹת הַתַּאֲוָה", "ורחלו מנה", "And they journeyed from there"),
        ("נָסְעוּ הָעָם חֲצֵרוֹת", "אלי' חצרות", "to Hazeroth;"),
        ("וַיִּהְיוּ בַּחֲצֵרוֹת", "פלמא אקאמו בהא", "and when they settled there."),
    ],
}

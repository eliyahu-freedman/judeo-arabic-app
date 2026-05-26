"""Hand-authored word-level alignment triples for Bamidbar chapter 21."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיִּשְׁמַע הַכְּנַעֲנִי מֶלֶךְ-עֲרָד יֹשֵׁב הַנֶּגֶב כִּי בָּא יִשְׂרָאֵל דֶּרֶךְ הָאֲתָרִים וַיִּלָּחֶם בְּיִשְׂרָאֵל וַיִּשְׁבְּ מִמֶּנּוּ שֶׁבִי
        # JA: ת'ם סמע אלכנאעני מלך ערד אלמקים פי אלדארום. באן בני אסראיל קד גאו. טריק אלאתרים. פחארבהם. וסבא מנהם סביא
        # EN: Then the Canaanite, king of Arad, dwelling in the south, heard that the sons of Israel had come by the way of the Atharim; and he fought against them, and took some of them captive.
        (None, "ת'ם", "Then"),
        ("וַיִּשְׁמַע", "סמע", "heard"),
        ("הַכְּנַעֲנִי", "אלכנאעני", "the Canaanite,"),
        ("מֶלֶךְ-עֲרָד", "מלך ערד", "king of Arad,"),
        ("יֹשֵׁב", "אלמקים", "dwelling"),
        ("הַנֶּגֶב", "פי אלדארום", "in the south,"),
        ("כִּי בָּא", "באן", "that"),
        ("יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        (None, "קד גאו", "had come"),
        ("דֶּרֶךְ", "טריק", "by the way of"),
        ("הָאֲתָרִים", "אלאתרים", "the Atharim;"),
        ("וַיִּלָּחֶם בְּיִשְׂרָאֵל", "פחארבהם", "and he fought against them,"),
        ("וַיִּשְׁבְּ מִמֶּנּוּ", "וסבא מנהם", "and took some of them"),
        ("שֶׁבִי", "סביא", "captive."),
    ],
    2: [
        # HE: וַיִּדַּר יִשְׂרָאֵל נֶדֶר לַיהוָה וַיֹּאמַר אִם-נָתֹן תִּתֵּן אֶת-הָעָם הַזֶּה בְּיָדִי--וְהַחֲרַמְתִּי אֶת-עָרֵיהֶם
        # JA: פנד'ר אל אסראיל נד'רא. ללה קאילין. אן אסלמת הולאי אלקום פי ידי. געלת קראהם צואפי
        # EN: And the house of Israel vowed a vow to God, saying: 'If You deliver this people into my hand, I shall make their towns devoted property.'
        ("וַיִּדַּר", "פנד'ר", "And the house of Israel vowed"),
        ("יִשְׂרָאֵל", "אל אסראיל", "a vow"),
        ("נֶדֶר", "נד'רא", "to God,"),
        ("לַיהוָה", "ללה", "saying:"),
        ("וַיֹּאמַר", "קאילין", "'If"),
        ("אִם-נָתֹן תִּתֵּן", "אן אסלמת", "You deliver"),
        ("אֶת-הָעָם הַזֶּה", "הולאי אלקום", "this people"),
        ("בְּיָדִי", "פי ידי", "into my hand,"),
        ("וְהַחֲרַמְתִּי", "געלת", "I shall make"),
        ("אֶת-עָרֵיהֶם", "קראהם צואפי", "their towns devoted property.'"),
    ],
    3: [
        # HE: וַיִּשְׁמַע יְהוָה בְּקוֹל יִשְׂרָאֵל וַיִּתֵּן אֶת-הַכְּנַעֲנִי וַיַּחֲרֵם אֶתְהֶם וְאֶת-עָרֵיהֶם וַיִּקְרָא שֵׁם-הַמָּקוֹם חָרְמָה
        # JA: פסמע אללה דעא אל אסראיל. ואסלם פי אידיהם. אלכנאעני. פגעלוה וקראה צואפי. וסמא ד'אלך אלמוצ'ע חרמה
        # EN: And God heard the prayer of the house of Israel, and delivered the Canaanite into their hands; and they made him and his towns devoted property, and they named that place Hormah.
        ("וַיִּשְׁמַע", "פסמע", "And God heard"),
        ("יְהוָה", "אללה", "the prayer of"),
        ("בְּקוֹל יִשְׂרָאֵל", "דעא אל אסראיל", "the house of Israel,"),
        ("וַיִּתֵּן", "ואסלם", "and delivered"),
        ("אֶת-הַכְּנַעֲנִי", "פי אידיהם. אלכנאעני", "the Canaanite into their hands;"),
        ("וַיַּחֲרֵם אֶתְהֶם", "פגעלוה", "and they made him"),
        ("וְאֶת-עָרֵיהֶם", "וקראה צואפי", "and his towns devoted property,"),
        ("וַיִּקְרָא", "וסמא", "and they named"),
        ("שֵׁם-הַמָּקוֹם", "ד'אלך אלמוצ'ע", "that place"),
        ("חָרְמָה", "חרמה", "Hormah."),
    ],
    4: [
        # HE: וַיִּסְעוּ מֵהֹר הָהָר דֶּרֶךְ יַם-סוּף לִסְבֹב אֶת-אֶרֶץ אֱדוֹם וַתִּקְצַר נֶפֶשׁ-הָעָם בַּדָּרֶךְ
        # JA: ת'ם רחלו מן גבל הור טריק בחר אלקלזם. ליסתדירו בלד אדום. פצ'גרת נפוס אלקום פי אלטריק
        # EN: Then they journeyed from Mount Hor by the way of the Sea of Qulzum (Red Sea), to go around the land of Edom; and the souls of the people grew weary on the way.
        (None, "ת'ם", "Then"),
        ("וַיִּסְעוּ", "רחלו", "they journeyed"),
        ("מֵהֹר הָהָר", "מן גבל הור", "from Mount Hor"),
        ("דֶּרֶךְ יַם-סוּף", "טריק בחר אלקלזם", "by the way of the Sea of Qulzum (Red Sea),"),
        ("לִסְבֹב", "ליסתדירו", "to go around"),
        ("אֶת-אֶרֶץ", "בלד", "the land of"),
        ("אֱדוֹם", "אדום", "Edom;"),
        ("וַתִּקְצַר נֶפֶשׁ-הָעָם", "פצ'גרת נפוס אלקום", "and the souls of the people grew weary"),
        ("בַּדָּרֶךְ", "פי אלטריק", "on the way."),
    ],
    5: [
        # HE: וַיְדַבֵּר הָעָם בֵּאלֹהִים וּבְמֹשֶׁה לָמָה הֶעֱלִיתֻנוּ מִמִּצְרַיִם לָמוּת בַּמִּדְבָּר כִּי אֵין לֶחֶם וְאֵין מַיִם וְנַפְשֵׁנוּ קָצָה בַּלֶּחֶם הַקְּלֹקֵל
        # JA: פתכלמו פי אללה ופי מוסי'. וקאלו לם אצעדתמונא מן מצר. לנמות פי אלבר. ממא ליס כ'בז ולא מא. וקד צ'גרת נפוסנא. מן אלטעאם אלכ'פיף
        # EN: And they spoke against God and against Moses, saying: 'Why did you bring us up from Egypt to die in the wilderness, where there is no bread and no water? And our souls are weary of this light food.'
        ("וַיְדַבֵּר", "פתכלמו", "And they spoke"),
        ("בֵּאלֹהִים", "פי אללה", "against God"),
        ("וּבְמֹשֶׁה", "ופי מוסי'", "and against Moses,"),
        ("לָמָה הֶעֱלִיתֻנוּ", "וקאלו לם אצעדתמונא", "saying: 'Why did you bring us up"),
        ("מִמִּצְרַיִם", "מן מצר", "from Egypt"),
        ("לָמוּת", "לנמות", "to die"),
        ("בַּמִּדְבָּר", "פי אלבר", "in the wilderness,"),
        ("כִּי אֵין לֶחֶם", "ממא ליס כ'בז", "where there is no bread"),
        ("וְאֵין מַיִם", "ולא מא", "and no water?"),
        ("וְנַפְשֵׁנוּ קָצָה", "וקד צ'גרת נפוסנא", "And our souls are weary of"),
        ("בַּלֶּחֶם הַקְּלֹקֵל", "מן אלטעאם אלכ'פיף", "this light food.'"),
    ],
    6: [
        # HE: וַיְשַׁלַּח יְהוָה בָּעָם אֵת הַנְּחָשִׁים הַשְּׂרָפִים וַיְנַשְּׁכוּ אֶת-הָעָם וַיָּמָת עַם-רָב מִיִּשְׂרָאֵל
        # JA: פבעת' אללה פי אלקום. חיאת מחרקה. לסעתהם פמאת מנהם כת'ירין
        # EN: And God sent among the people burning serpents; they bit them, and many of them died.
        ("וַיְשַׁלַּח", "פבעת'", "And God sent"),
        ("יְהוָה", "אללה", "among"),
        ("בָּעָם", "פי אלקום", "the people"),
        ("הַנְּחָשִׁים הַשְּׂרָפִים", "חיאת מחרקה", "burning serpents;"),
        ("וַיְנַשְּׁכוּ אֶת-הָעָם", "לסעתהם", "they bit them,"),
        ("וַיָּמָת עַם-רָב מִיִּשְׂרָאֵל", "פמאת מנהם כת'ירין", "and many of them died."),
    ],
    7: [
        # HE: וַיָּבֹא הָעָם אֶל-מֹשֶׁה וַיֹּאמְרוּ חָטָאנוּ כִּי-דִבַּרְנוּ בַיהוָה וָבָךְ--הִתְפַּלֵּל אֶל-יְהוָה וְיָסֵר מֵעָלֵינוּ אֶת-הַנָּחָשׁ וַיִּתְפַּלֵּל מֹשֶׁה בְּעַד הָעָם
        # JA: פגאו אלי' מוסי' וקאלו קד אכ'טאנא. אד' תכלמנא פי אללה ופיך. אדע אלי' אללה. אן יזיל ענא אלחיאת. פדעא להם מוסי'
        # EN: And they came to Moses and said: 'We have erred, since we spoke against God and against you. Pray to God that He remove the serpents from us.' And Moses prayed for them.
        ("וַיָּבֹא הָעָם", "פגאו", "And they came"),
        ("אֶל-מֹשֶׁה", "אלי' מוסי'", "to Moses"),
        ("וַיֹּאמְרוּ", "וקאלו", "and said:"),
        ("חָטָאנוּ", "קד אכ'טאנא", "'We have erred,"),
        ("כִּי-דִבַּרְנוּ", "אד' תכלמנא", "since we spoke"),
        ("בַיהוָה", "פי אללה", "against God"),
        ("וָבָךְ", "ופיך", "and against you."),
        ("הִתְפַּלֵּל", "אדע", "Pray"),
        ("אֶל-יְהוָה", "אלי' אללה", "to God"),
        ("וְיָסֵר מֵעָלֵינוּ אֶת-הַנָּחָשׁ", "אן יזיל ענא אלחיאת", "that He remove the serpents from us.'"),
        ("וַיִּתְפַּלֵּל מֹשֶׁה", "פדעא להם מוסי'", "And Moses prayed for them."),
    ],
    8: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה עֲשֵׂה לְךָ שָׂרָף וְשִׂים אֹתוֹ עַל-נֵס וְהָיָה כָּל-הַנָּשׁוּךְ וְרָאָה אֹתוֹ וָחָי
        # JA: פקאל אללה לה. אצנע לך מחרקא. וארפעה עלי' עלם. פכל מלסוע. ילתפת אלי'ה תאיבא פיבקא
        # EN: And God said to him: 'Make yourself a burning image, and raise it upon a standard; then every one who has been bitten, if he turns toward it in repentance, shall survive.'
        ("וַיֹּאמֶר", "פקאל", "And God said"),
        ("יְהוָה", "אללה", "to him:"),
        ("אֶל-מֹשֶׁה", "לה", "'Make yourself"),
        ("עֲשֵׂה לְךָ", "אצנע לך", "a burning image,"),
        ("שָׂרָף", "מחרקא", "and raise it"),
        ("וְשִׂים אֹתוֹ", "וארפעה", "upon"),
        ("עַל-נֵס", "עלי' עלם", "a standard;"),
        (None, "פכל", "then every one"),
        ("כָּל-הַנָּשׁוּךְ", "מלסוע", "who has been bitten,"),
        ("וְרָאָה אֹתוֹ", "ילתפת אלי'ה תאיבא", "if he turns toward it in repentance,"),
        ("וָחָי", "פיבקא", "shall survive.'"),
    ],
    9: [
        # HE: וַיַּעַשׂ מֹשֶׁה נְחַשׁ נְחֹשֶׁת וַיְשִׂמֵהוּ עַל-הַנֵּס וְהָיָה אִם-נָשַׁךְ הַנָּחָשׁ אֶת-אִישׁ--וְהִבִּיט אֶל-נְחַשׁ הַנְּחֹשֶׁת וָחָי
        # JA: פצנע מוסי' ת'עבאנא מן נחאס. ורפעה עלי' עלם. פכאן אלי' אנסאן לד'גה ת'עבאנא. אלתפת אלי'ה תאיבא בקא חייא
        # EN: And Moses made a serpent of bronze, and raised it upon a standard; and it was that any person who had been bitten by a serpent — if he turned toward it in repentance, he remained alive.
        ("וַיַּעַשׂ מֹשֶׁה", "פצנע מוסי'", "And Moses made"),
        ("נְחַשׁ", "ת'עבאנא", "a serpent"),
        ("נְחֹשֶׁת", "מן נחאס", "of bronze,"),
        ("וַיְשִׂמֵהוּ", "ורפעה", "and raised it"),
        ("עַל-הַנֵּס", "עלי' עלם", "upon a standard;"),
        ("וְהָיָה", "פכאן", "and it was that"),
        ("אִם-נָשַׁךְ הַנָּחָשׁ אֶת-אִישׁ", "אלי' אנסאן לד'גה ת'עבאנא", "any person who had been bitten by a serpent —"),
        ("וְהִבִּיט", "אלתפת אלי'ה תאיבא", "if he turned toward it in repentance,"),
        ("וָחָי", "בקא חייא", "he remained alive."),
    ],
    10: [
        # HE: וַיִּסְעוּ בְּנֵי יִשְׂרָאֵל וַיַּחֲנוּ בְּאֹבֹת
        # JA: פרחלו בני אסראיל. ונזלו פי אובות
        # EN: And the sons of Israel journeyed, and encamped at Oboth.
        ("וַיִּסְעוּ", "פרחלו", "And"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel journeyed,"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּאֹבֹת", "פי אובות", "at Oboth."),
    ],
    11: [
        # HE: וַיִּסְעוּ מֵאֹבֹת וַיַּחֲנוּ בְּעִיֵּי הָעֲבָרִים בַּמִּדְבָּר אֲשֶׁר עַל-פְּנֵי מוֹאָב מִמִּזְרַח הַשָּׁמֶשׁ
        # JA: ורחלו מן אובות. ונזלו פי בלאקע אלמגאזאת. פי אלברייה אלתי עלי'ה גהה' מואב. מן מטלע אלשמס
        # EN: And they journeyed from Oboth, and encamped in the open wastes of the crossings, in the wilderness that faces the direction of Moab, from the rising of the sun.
        ("וַיִּסְעוּ", "ורחלו", "And they journeyed"),
        ("מֵאֹבֹת", "מן אובות", "from Oboth,"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּעִיֵּי הָעֲבָרִים", "פי בלאקע אלמגאזאת", "in the open wastes of the crossings,"),
        ("בַּמִּדְבָּר", "פי אלברייה", "in the wilderness"),
        ("אֲשֶׁר עַל-פְּנֵי", "אלתי עלי'ה", "that faces"),
        ("מוֹאָב", "גהה' מואב", "the direction of Moab,"),
        ("מִמִּזְרַח הַשָּׁמֶשׁ", "מן מטלע אלשמס", "from the rising of the sun."),
    ],
    12: [
        # HE: מִשָּׁם נָסָעוּ וַיַּחֲנוּ בְּנַחַל זָרֶד
        # JA: ורחלו מן ת'ם. ונזלו פי ואד זרד
        # EN: And they journeyed from there, and encamped in the valley of Zared.
        ("מִשָּׁם", "ורחלו מן ת'ם", "And they journeyed from there,"),
        ("נָסָעוּ", "ונזלו", "and encamped"),
        ("וַיַּחֲנוּ", "פי ואד", "in the valley of"),
        ("בְּנַחַל זָרֶד", "זרד", "Zared."),
    ],
    13: [
        # HE: מִשָּׁם נָסָעוּ וַיַּחֲנוּ מֵעֵבֶר אַרְנוֹן אֲשֶׁר בַּמִּדְבָּר הַיֹּצֵא מִגְּבֻל הָאֱמֹרִי כִּי אַרְנוֹן גְּבוּל מוֹאָב בֵּין מוֹאָב וּבֵין הָאֱמֹרִי
        # JA: ורחלו מן ת'ם. ונזלו. פי גאנב ארנון אלד'י פי אלברייה. אלכ'ארג ען תכ'ם אלאמוריין. לאן ארנון פי תח'ם מואב בין מואב ובין אלאמורי
        # EN: And they journeyed from there, and encamped on the side of the Arnon which is in the wilderness, that goes out beyond the border of the Amorites; for the Arnon is on the border of Moab, between Moab and the Amorite.
        ("מִשָּׁם נָסָעוּ", "ורחלו מן ת'ם", "And they journeyed from there,"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("מֵעֵבֶר", "פי גאנב", "on the side of"),
        ("אַרְנוֹן", "ארנון", "the Arnon"),
        ("אֲשֶׁר בַּמִּדְבָּר", "אלד'י פי אלברייה", "which is in the wilderness,"),
        ("הַיֹּצֵא", "אלכ'ארג", "that goes out"),
        ("מִגְּבֻל הָאֱמֹרִי", "ען תכ'ם אלאמוריין", "beyond the border of the Amorites;"),
        ("כִּי", "לאן", "for"),
        ("אַרְנוֹן גְּבוּל מוֹאָב", "ארנון פי תח'ם מואב", "the Arnon is on the border of Moab,"),
        ("בֵּין מוֹאָב", "בין מואב", "between Moab"),
        ("וּבֵין הָאֱמֹרִי", "ובין אלאמורי", "and the Amorite."),
    ],
    14: [
        # HE: עַל-כֵּן יֵאָמַר בְּסֵפֶר מִלְחֲמֹת יְהוָה אֶת-וָהֵב בְּסוּפָה וְאֶת-הַנְּחָלִים אַרְנוֹן
        # JA: לדא'לך יקאל. פי כתאב פתוח אללה. מן אלדראדר אלקלזם. ומן אלאודיה פארנון
        # EN: Therefore it is said in the Book of the Conquests of God: 'From the whirlpools of Qulzum, and from the valleys — even Arnon;
        ("עַל-כֵּן", "לדא'לך", "Therefore"),
        ("יֵאָמַר", "יקאל", "it is said"),
        ("בְּסֵפֶר", "פי כתאב", "in the Book of"),
        ("מִלְחֲמֹת יְהוָה", "פתוח אללה", "the Conquests of God:"),
        ("אֶת-וָהֵב בְּסוּפָה", "מן אלדראדר אלקלזם", "'From the whirlpools of Qulzum,"),
        ("וְאֶת-הַנְּחָלִים", "ומן אלאודיה", "and from the valleys —"),
        ("אַרְנוֹן", "פארנון", "even Arnon;"),
    ],
    15: [
        # HE: וְאֶשֶׁד הַנְּחָלִים אֲשֶׁר נָטָה לְשֶׁבֶת עָר וְנִשְׁעַן לִגְבוּל מוֹאָב
        # JA: ומצב אלאודיה. אלד'י מאילה אלי' עמארה' ער. ומסנדה אלי' ת'כם מואב
        # EN: and the outflow of the valleys, which inclines toward the inhabited place of Ar, and leans upon the border of Moab.'
        ("וְאֶשֶׁד", "ומצב", "and the outflow of"),
        ("הַנְּחָלִים", "אלאודיה", "the valleys,"),
        ("אֲשֶׁר נָטָה", "אלד'י מאילה", "which inclines"),
        ("לְשֶׁבֶת עָר", "אלי' עמארה' ער", "toward the inhabited place of Ar,"),
        ("וְנִשְׁעַן", "ומסנדה", "and leans"),
        ("לִגְבוּל מוֹאָב", "אלי' ת'כם מואב", "upon the border of Moab.'"),
    ],
    16: [
        # HE: וּמִשָּׁם בְּאֵרָה הִוא הַבְּאֵר אֲשֶׁר אָמַר יְהוָה לְמֹשֶׁה אֱסֹף אֶת-הָעָם וְאֶתְּנָה לָהֶם מָיִם
        # JA: ורחלו מן ת'ם אלי' אלביר. אלת'י קאל אללה למוסי' ענהא. אגמע אלקום. חתי' אעטיהם מאא
        # EN: And they journeyed from there to the well, of which God had said to Moses: 'Gather the people, that I may give them water.'
        ("וּמִשָּׁם", "ורחלו מן ת'ם", "And they journeyed from there"),
        ("בְּאֵרָה", "אלי' אלביר", "to the well,"),
        ("הִוא הַבְּאֵר אֲשֶׁר אָמַר", "אלת'י קאל", "of which"),
        ("יְהוָה", "אללה", "God had said"),
        ("לְמֹשֶׁה", "למוסי' ענהא", "to Moses:"),
        ("אֱסֹף", "אגמע", "'Gather"),
        ("אֶת-הָעָם", "אלקום", "the people,"),
        ("וְאֶתְּנָה לָהֶם", "חתי' אעטיהם", "that I may give them"),
        ("מָיִם", "מאא", "water.'"),
    ],
    17: [
        # HE: אָז יָשִׁיר יִשְׂרָאֵל אֶת-הַשִּׁירָה הַזֹּאת עֲלִי בְאֵר עֱנוּ-לָהּ
        # JA: חיניד' אנשא אל אסראיל. הד'א אלאנשא וקאלו. אצעדי יא ביר תגאובו להא
        # EN: Then the house of Israel sang this song, and said: 'Rise up, O well!' — and they respond to it.
        ("אָז", "חיניד'", "Then"),
        ("יָשִׁיר יִשְׂרָאֵל", "אנשא אל אסראיל", "the house of Israel sang"),
        ("אֶת-הַשִּׁירָה הַזֹּאת", "הד'א אלאנשא", "this song,"),
        ("עֲלִי בְאֵר", "וקאלו. אצעדי יא ביר", "and said: 'Rise up, O well!'"),
        ("עֱנוּ-לָהּ", "תגאובו להא", "— and they respond to it."),
    ],
    18: [
        # HE: בְּאֵר חֲפָרוּהָ שָׂרִים כָּרוּהָ נְדִיבֵי הָעָם בִּמְחֹקֵק בְּמִשְׁעֲנֹתָם וּמִמִּדְבָּר מַתָּנָה
        # JA: ביר חפרוא אלרויסא. וכראהא נבל אלקום. רסמוהא בוכאיאתהם. ת'ם רחלו מן תלך אלברייה אלי' ד'את אלעטא
        # EN: 'A well which the chiefs dug, which the nobles of the people hollowed out, marked with their staffs.' Then they journeyed from that wilderness to the place of bestowal.
        ("בְּאֵר", "ביר", "'A well"),
        ("חֲפָרוּהָ", "חפרוא", "which the chiefs"),
        ("שָׂרִים", "אלרויסא", "dug,"),
        ("כָּרוּהָ", "וכראהא", "which the nobles of"),
        ("נְדִיבֵי הָעָם", "נבל אלקום", "the people hollowed out,"),
        ("בִּמְחֹקֵק בְּמִשְׁעֲנֹתָם", "רסמוהא בוכאיאתהם", "marked with their staffs.'"),
        (None, "ת'ם", "Then"),
        ("וּמִמִּדְבָּר", "רחלו מן תלך אלברייה", "they journeyed from that wilderness"),
        ("מַתָּנָה", "אלי' ד'את אלעטא", "to the place of bestowal."),
    ],
    19: [
        # HE: וּמִמַּתָּנָה נַחֲלִיאֵל וּמִנַּחֲלִיאֵל בָּמוֹת
        # JA: ומן ד'את אלעטא אלי' אלואד אלאלי. ומן ד'אלך אלואד אלי' ד'את אלכנאיס
        # EN: And from the place of bestowal to the central valley; and from that valley to the place of the assemblies.
        ("וּמִמַּתָּנָה", "ומן ד'את אלעטא", "And from the place of bestowal"),
        ("נַחֲלִיאֵל", "אלי' אלואד אלאלי", "to the central valley;"),
        ("וּמִנַּחֲלִיאֵל", "ומן ד'אלך אלואד", "and from that valley"),
        ("בָּמוֹת", "אלי' ד'את אלכנאיס", "to the place of the assemblies."),
    ],
    20: [
        # HE: וּמִבָּמוֹת הַגַּיְא אֲשֶׁר בִּשְׂדֵה מוֹאָב--רֹאשׁ הַפִּסְגָּה וְנִשְׁקָפָה עַל-פְּנֵי הַיְשִׁימֹן
        # JA: ומן ת'ם. אלי' אלואד אלד'י פי בלד מואב. ענד ראס אלקלעה. אלמטלעה עלא וגה אלסמאוא
        # EN: And from there to the valley that is in the land of Moab, by the summit of the fortress that overlooks the face of the open waste.
        ("וּמִבָּמוֹת", "ומן ת'ם", "And from there"),
        ("הַגַּיְא", "אלי' אלואד", "to the valley"),
        ("אֲשֶׁר בִּשְׂדֵה", "אלד'י פי בלד", "that is in the land of"),
        ("מוֹאָב", "מואב", "Moab,"),
        ("רֹאשׁ הַפִּסְגָּה", "ענד ראס אלקלעה", "by the summit of the fortress"),
        ("וְנִשְׁקָפָה", "אלמטלעה", "that overlooks"),
        ("עַל-פְּנֵי הַיְשִׁימֹן", "עלא וגה אלסמאוא", "the face of the open waste."),
    ],
    21: [
        # HE: וַיִּשְׁלַח יִשְׂרָאֵל מַלְאָכִים אֶל-סִיחֹן מֶלֶךְ-הָאֱמֹרִי לֵאמֹר
        # JA: ת'ם בעת' אל אסראיל ברסל. אלי' סיחון מלך אלאמוריין קאילא
        # EN: Then the house of Israel sent messengers to Sihon king of the Amorites, saying:
        (None, "ת'ם", "Then"),
        ("וַיִּשְׁלַח", "בעת'", "the house of Israel sent"),
        ("יִשְׂרָאֵל", "אל אסראיל", "messengers"),
        ("מַלְאָכִים", "ברסל", "to Sihon"),
        ("אֶל-סִיחֹן", "אלי' סיחון", "king of"),
        ("מֶלֶךְ-הָאֱמֹרִי", "מלך אלאמוריין", "the Amorites,"),
        ("לֵאמֹר", "קאילא", "saying:"),
    ],
    22: [
        # HE: אֶעְבְּרָה בְאַרְצֶךָ לֹא נִטֶּה בְּשָׂדֶה וּבְכֶרֶם--לֹא נִשְׁתֶּה מֵי בְאֵר בְּדֶרֶךְ הַמֶּלֶךְ נֵלֵךְ עַד אֲשֶׁר-נַעֲבֹר גְּבֻלֶךָ
        # JA: אריד אן אגוז פי בלדך. וליסנא נמיל אלי' צ'יעה ולא כרם. ולא נשרב מא צהריג. בל פי אלטריק אלגאדה נסיר. אלי' אן נגוז תכ'מך
        # EN: 'I wish to pass through your land; and we shall not turn aside to any farm or vineyard, nor shall we drink water from a cistern — but we shall travel by the broad road, until we pass through your border.'
        ("אֶעְבְּרָה", "אריד אן אגוז", "'I wish to pass"),
        ("בְאַרְצֶךָ", "פי בלדך", "through your land;"),
        ("לֹא נִטֶּה", "וליסנא נמיל", "and we shall not turn aside"),
        ("בְּשָׂדֶה", "אלי' צ'יעה", "to any farm"),
        ("וּבְכֶרֶם", "ולא כרם", "or vineyard,"),
        ("לֹא נִשְׁתֶּה", "ולא נשרב", "nor shall we drink"),
        ("מֵי בְאֵר", "מא צהריג", "water from a cistern —"),
        ("בְּדֶרֶךְ הַמֶּלֶךְ", "בל פי אלטריק אלגאדה", "but we shall travel by the broad road,"),
        ("נֵלֵךְ עַד אֲשֶׁר-נַעֲבֹר", "אלי' אן נגוז", "until we pass through"),
        ("גְּבֻלֶךָ", "תכ'מך", "your border.'"),
    ],
    23: [
        # HE: וְלֹא-נָתַן סִיחֹן אֶת-יִשְׂרָאֵל עֲבֹר בִּגְבֻלוֹ וַיֶּאֱסֹף סִיחֹן אֶת-כָּל-עַמּוֹ וַיֵּצֵא לִקְרַאת יִשְׂרָאֵל הַמִּדְבָּרָה וַיָּבֹא יָהְצָה וַיִּלָּחֶם בְּיִשְׂרָאֵל
        # JA: ולם ידע סיחון בני אסראיל אן יגוזו פי תכ'מה. פגמע גמיע קומה. וכ'רג תלקאהם אלי' אלברייה. חתא ואפא יהץ. פחארבהם
        # EN: But Sihon would not allow the sons of Israel to pass through his border; and he gathered all his people, and went out to meet them into the wilderness, until he reached Jahaz; and he fought against them.
        ("וְלֹא-נָתַן", "ולם ידע", "But Sihon would not allow"),
        ("סִיחֹן", "סיחון", "the sons of Israel"),
        ("אֶת-יִשְׂרָאֵל עֲבֹר", "בני אסראיל אן יגוזו", "to pass through"),
        ("בִּגְבֻלוֹ", "פי תכ'מה", "his border;"),
        ("וַיֶּאֱסֹף סִיחֹן", "פגמע", "and he gathered"),
        ("אֶת-כָּל-עַמּוֹ", "גמיע קומה", "all his people,"),
        ("וַיֵּצֵא", "וכ'רג", "and went out"),
        ("לִקְרַאת יִשְׂרָאֵל", "תלקאהם", "to meet them"),
        ("הַמִּדְבָּרָה", "אלי' אלברייה", "into the wilderness,"),
        ("וַיָּבֹא יָהְצָה", "חתא ואפא יהץ", "until he reached Jahaz;"),
        ("וַיִּלָּחֶם בְּיִשְׂרָאֵל", "פחארבהם", "and he fought against them."),
    ],
    24: [
        # HE: וַיַּכֵּהוּ יִשְׂרָאֵל לְפִי-חָרֶב וַיִּירַשׁ אֶת-אַרְצוֹ מֵאַרְנֹן עַד-יַבֹּק עַד-בְּנֵי עַמּוֹן--כִּי עַז גְּבוּל בְּנֵי עַמּוֹן
        # JA: פקתלוה בחד אלסיף. וחאזו בלדה מן ארנון. אלי' יבוק אלי' בני עמון. אד' כאן תכ'מהם שדידא עלי'ה
        # EN: And they slew him with the edge of the sword, and took possession of his land from Arnon to Jabbok, as far as the sons of Ammon — for the border of the sons of Ammon was strong and high.
        ("וַיַּכֵּהוּ יִשְׂרָאֵל", "פקתלוה", "And they slew him"),
        ("לְפִי-חָרֶב", "בחד אלסיף", "with the edge of the sword,"),
        ("וַיִּירַשׁ", "וחאזו", "and took possession of"),
        ("אֶת-אַרְצוֹ", "בלדה", "his land"),
        ("מֵאַרְנֹן", "מן ארנון", "from Arnon"),
        ("עַד-יַבֹּק", "אלי' יבוק", "to Jabbok,"),
        ("עַד-בְּנֵי עַמּוֹן", "אלי' בני עמון", "as far as the sons of Ammon —"),
        ("כִּי", "אד' כאן", "for"),
        ("עַז גְּבוּל בְּנֵי עַמּוֹן", "תכ'מהם שדידא עלי'ה", "the border of the sons of Ammon was strong and high."),
    ],
    25: [
        # HE: וַיִּקַּח יִשְׂרָאֵל אֵת כָּל-הֶעָרִים הָאֵלֶּה וַיֵּשֶׁב יִשְׂרָאֵל בְּכָל-עָרֵי הָאֱמֹרִי בְּחֶשְׁבּוֹן וּבְכָל-בְּנֹתֶיהָ
        # JA: פאכ'דו גמיע הד'ה אלקרא. וסכנו פי גמיע קרא אלאמוריין. פי חשבון ורסאתיקהא
        # EN: And they took all these towns, and settled in all the towns of the Amorites — in Heshbon and its surrounding districts.
        ("וַיִּקַּח יִשְׂרָאֵל", "פאכ'דו", "And they took"),
        ("אֵת כָּל-הֶעָרִים הָאֵלֶּה", "גמיע הד'ה אלקרא", "all these towns,"),
        ("וַיֵּשֶׁב יִשְׂרָאֵל", "וסכנו", "and settled"),
        ("בְּכָל-עָרֵי", "פי גמיע קרא", "in all the towns of"),
        ("הָאֱמֹרִי", "אלאמוריין", "the Amorites —"),
        ("בְּחֶשְׁבּוֹן", "פי חשבון", "in Heshbon"),
        ("וּבְכָל-בְּנֹתֶיהָ", "ורסאתיקהא", "and its surrounding districts."),
    ],
    26: [
        # HE: כִּי חֶשְׁבּוֹן--עִיר סִיחֹן מֶלֶךְ הָאֱמֹרִי הִוא וְהוּא נִלְחַם בְּמֶלֶךְ מוֹאָב הָרִאשׁוֹן וַיִּקַּח אֶת-כָּל-אַרְצוֹ מִיָּדוֹ עַד-אַרְנֹן
        # JA: וד'אלך אן חשבון. הי מנבר סיחון מלך אלאמוריין. והו כאן קד חארב מלך מואב אלאוול. פ'אכ'ד' גמיע בלדה. מן ידה אלי' ארנון
        # EN: For Heshbon is the seat of Sihon king of the Amorites; and he had fought against the former king of Moab, and taken all his land from his hand as far as Arnon.
        ("כִּי", "וד'אלך אן", "For"),
        ("חֶשְׁבּוֹן", "חשבון", "Heshbon"),
        ("עִיר סִיחֹן", "הי מנבר סיחון", "is the seat of Sihon"),
        ("מֶלֶךְ הָאֱמֹרִי", "מלך אלאמוריין", "king of the Amorites;"),
        ("וְהוּא נִלְחַם", "והו כאן קד חארב", "and he had fought against"),
        ("בְּמֶלֶךְ מוֹאָב הָרִאשׁוֹן", "מלך מואב אלאוול", "the former king of Moab,"),
        ("וַיִּקַּח", "פ'אכ'ד'", "and taken"),
        ("אֶת-כָּל-אַרְצוֹ", "גמיע בלדה", "all his land"),
        ("מִיָּדוֹ", "מן ידה", "from his hand"),
        ("עַד-אַרְנֹן", "אלי' ארנון", "as far as Arnon."),
    ],
    27: [
        # HE: עַל-כֵּן יֹאמְרוּ הַמֹּשְׁלִים בֹּאוּ חֶשְׁבּוֹן תִּבָּנֶה וְתִכּוֹנֵן עִיר סִיחוֹן
        # JA: ולד'אלך יקולון אלממת'לין אדכלו אלי' חשבון חתי' תבנא ותהייא קריה' סיחון
        # EN: Therefore those who speak in parables say: 'Enter Heshbon, that the town of Sihon may be built and established.'
        ("עַל-כֵּן", "ולד'אלך", "Therefore"),
        ("יֹאמְרוּ הַמֹּשְׁלִים", "יקולון אלממת'לין", "those who speak in parables say:"),
        ("בֹּאוּ", "אדכלו", "'Enter"),
        ("חֶשְׁבּוֹן", "אלי' חשבון", "Heshbon,"),
        ("תִּבָּנֶה", "חתי' תבנא", "that the town of Sihon may be built"),
        ("וְתִכּוֹנֵן עִיר סִיחוֹן", "ותהייא קריה' סיחון", "and established.'"),
    ],
    28: [
        # HE: כִּי-אֵשׁ יָצְאָה מֵחֶשְׁבּוֹן לֶהָבָה מִקִּרְיַת סִיחֹן אָכְלָה עָר מוֹאָב בַּעֲלֵי בָּמוֹת אַרְנֹן
        # JA: לאן נארא כ'רגת מן חשבון. ולהיב מן קריה' סיחון. פאכלת ער מואב. ואצחאב ביאע ארנון
        # EN: 'For a fire went out from Heshbon, and a flame from the town of Sihon; it consumed Ar of Moab, and the lords of the marketplaces of Arnon.'
        ("כִּי-אֵשׁ", "לאן נארא", "'For a fire"),
        ("יָצְאָה", "כ'רגת", "went out"),
        ("מֵחֶשְׁבּוֹן", "מן חשבון", "from Heshbon,"),
        ("לֶהָבָה", "ולהיב", "and a flame"),
        ("מִקִּרְיַת סִיחֹן", "מן קריה' סיחון", "from the town of Sihon;"),
        ("אָכְלָה", "פאכלת", "it consumed"),
        ("עָר מוֹאָב", "ער מואב", "Ar of Moab,"),
        ("בַּעֲלֵי בָּמוֹת אַרְנֹן", "ואצחאב ביאע ארנון", "and the lords of the marketplaces of Arnon.'"),
    ],
    29: [
        # HE: אוֹי-לְךָ מוֹאָב אָבַדְתָּ עַם-כְּמוֹשׁ נָתַן בָּנָיו פְּלֵיטִם וּבְנֹתָיו בַּשְּׁבִית לְמֶלֶךְ אֱמֹרִי סִיחוֹן
        # JA: פוילך יא מואב. כיף בדת יא עבדת כמוש. לקד געל בניה אסארא ובנאתה סביא. למלך אלאמורי סיחון
        # EN: 'Woe to you, O Moab! How you are undone, O worshippers of Chemosh! He has made his sons captives and his daughters taken prisoner — to the Amorite king Sihon.'
        ("אוֹי-לְךָ", "פוילך", "'Woe to you,"),
        ("מוֹאָב", "יא מואב", "O Moab!"),
        ("אָבַדְתָּ", "כיף בדת", "How you are undone,"),
        ("עַם-כְּמוֹשׁ", "יא עבדת כמוש", "O worshippers of Chemosh!"),
        ("נָתַן", "לקד געל", "He has made"),
        ("בָּנָיו פְּלֵיטִם", "בניה אסארא", "his sons captives"),
        ("וּבְנֹתָיו בַּשְּׁבִית", "ובנאתה סביא", "and his daughters taken prisoner —"),
        ("לְמֶלֶךְ אֱמֹרִי", "למלך אלאמורי", "to the Amorite king"),
        ("סִיחוֹן", "סיחון", "Sihon.'"),
    ],
    30: [
        # HE: וַנִּירָם אָבַד חֶשְׁבּוֹן עַד-דִּיבֹן וַנַּשִּׁים עַד-נֹפַח אֲשֶׁר עַד-מֵידְבָא
        # JA: וזאל סימאהם מן חשבון אלי' דיבון. ותוחש אלי' נופח. אלד'י ענד מידבא
        # EN: And their mark has departed from Heshbon as far as Dibon, and desolation has spread to Nophah, which is near Medeba.
        ("וַנִּירָם", "וזאל סימאהם", "And their mark has departed"),
        ("אָבַד חֶשְׁבּוֹן", "מן חשבון", "from Heshbon"),
        ("עַד-דִּיבֹן", "אלי' דיבון", "as far as Dibon,"),
        ("וַנַּשִּׁים", "ותוחש", "and desolation has spread"),
        ("עַד-נֹפַח", "אלי' נופח", "to Nophah,"),
        ("אֲשֶׁר עַד-מֵידְבָא", "אלד'י ענד מידבא", "which is near Medeba."),
    ],
    31: [
        # HE: וַיֵּשֶׁב יִשְׂרָאֵל בְּאֶרֶץ הָאֱמֹרִי
        # JA: ולמא אקאם אל אסראיל. פי בלד אלאמוריין
        # EN: And when the house of Israel settled in the land of the Amorites,
        ("וַיֵּשֶׁב", "ולמא אקאם", "And when the house of Israel settled"),
        ("יִשְׂרָאֵל", "אל אסראיל", "in"),
        ("בְּאֶרֶץ", "פי בלד", "the land of"),
        ("הָאֱמֹרִי", "אלאמוריין", "the Amorites,"),
    ],
    32: [
        # HE: וַיִּשְׁלַח מֹשֶׁה לְרַגֵּל אֶת-יַעְזֵר וַיִּלְכְּדוּ בְּנֹתֶיהָ ויירש (וַיּוֹרֶשׁ) אֶת-הָאֱמֹרִי אֲשֶׁר-שָׁם
        # JA: פבעת' מוסי' בקום ירומון יעזר. פפתחו רסאתיקהא. וקרצ'ו אלאמורי אלד'י פיהא
        # EN: Moses sent people to reconnoiter Jazer; and they captured its surrounding districts, and drove out the Amorites who were in them.
        ("וַיִּשְׁלַח מֹשֶׁה", "פבעת' מוסי'", "Moses sent"),
        ("לְרַגֵּל", "בקום ירומון", "people to reconnoiter"),
        ("אֶת-יַעְזֵר", "יעזר", "Jazer;"),
        ("וַיִּלְכְּדוּ", "פפתחו", "and they captured"),
        ("בְּנֹתֶיהָ", "רסאתיקהא", "its surrounding districts,"),
        ("ויירש (וַיּוֹרֶשׁ) אֶת-הָאֱמֹרִי", "וקרצ'ו אלאמורי", "and drove out the Amorites"),
        ("אֲשֶׁר-שָׁם", "אלד'י פיהא", "who were in them."),
    ],
    33: [
        # HE: וַיִּפְנוּ וַיַּעֲלוּ דֶּרֶךְ הַבָּשָׁן וַיֵּצֵא עוֹג מֶלֶךְ-הַבָּשָׁן לִקְרָאתָם הוּא וְכָל-עַמּוֹ לַמִּלְחָמָה--אֶדְרֶעִי
        # JA: ת'ם ולו וצעדו. טריק אלבת'נייה. פכ'רג עוג מלך אלבת'נייה תלקאהם הו וגמיע קומה. לאלחרב אלי' אד'ראעאת
        # EN: Then they turned and went up by the way of the Bashan; and Og king of the Bashan came out to meet them — he and all his people — to battle, at Edrei.
        (None, "ת'ם", "Then"),
        ("וַיִּפְנוּ", "ולו", "they turned"),
        ("וַיַּעֲלוּ", "וצעדו", "and went up"),
        ("דֶּרֶךְ הַבָּשָׁן", "טריק אלבת'נייה", "by the way of the Bashan;"),
        ("וַיֵּצֵא עוֹג", "פכ'רג עוג", "and Og"),
        ("מֶלֶךְ-הַבָּשָׁן", "מלך אלבת'נייה", "king of the Bashan"),
        ("לִקְרָאתָם", "תלקאהם", "came out to meet them —"),
        ("הוּא וְכָל-עַמּוֹ", "הו וגמיע קומה", "he and all his people —"),
        ("לַמִּלְחָמָה", "לאלחרב", "to battle,"),
        ("אֶדְרֶעִי", "אלי' אד'ראעאת", "at Edrei."),
    ],
    34: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה אַל-תִּירָא אֹתוֹ--כִּי בְיָדְךָ נָתַתִּי אֹתוֹ וְאֶת-כָּל-עַמּוֹ וְאֶת-אַרְצוֹ וְעָשִׂיתָ לּוֹ--כַּאֲשֶׁר עָשִׂיתָ לְסִיחֹן מֶלֶךְ הָאֱמֹרִי אֲשֶׁר יוֹשֵׁב בְּחֶשְׁבּוֹן
        # JA: פקאל אללה למוסי' לא תכ'אפה. פאני מסלמה פי ידך. וגמיע קומה ובלדה. פאצנע בה. כמא צנעת. בסיחון מלך אלאמוריין. אלמקים פי חשבון
        # EN: And God said to Moses: 'Do not fear him, for I am delivering him into your hand — and all his people and his land. Do to him as you did to Sihon king of the Amorites who dwelt in Heshbon.'
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses:"),
        ("אַל-תִּירָא אֹתוֹ", "לא תכ'אפה", "'Do not fear him,"),
        ("כִּי בְיָדְךָ נָתַתִּי אֹתוֹ", "פאני מסלמה פי ידך", "for I am delivering him into your hand —"),
        ("וְאֶת-כָּל-עַמּוֹ", "וגמיע קומה", "and all his people"),
        ("וְאֶת-אַרְצוֹ", "ובלדה", "and his land."),
        ("וְעָשִׂיתָ לּוֹ", "פאצנע בה", "Do to him"),
        ("כַּאֲשֶׁר עָשִׂיתָ", "כמא צנעת", "as you did"),
        ("לְסִיחֹן", "בסיחון", "to Sihon"),
        ("מֶלֶךְ הָאֱמֹרִי", "מלך אלאמוריין", "king of the Amorites"),
        ("אֲשֶׁר יוֹשֵׁב בְּחֶשְׁבּוֹן", "אלמקים פי חשבון", "who dwelt in Heshbon.'"),
    ],
    35: [
        # HE: וַיַּכּוּ אֹתוֹ וְאֶת-בָּנָיו וְאֶת-כָּל-עַמּוֹ עַד-בִּלְתִּי הִשְׁאִיר-לוֹ שָׂרִיד וַיִּירְשׁוּ אֶת-אַרְצוֹ
        # JA: פקתלוה ובניה וגמיע קומה. חתי' לם יבק לה שרידא. וחאזו בלדה
        # EN: And they slew him and his sons and all his people, until not a survivor remained to him; and they took possession of his land.
        ("וַיַּכּוּ אֹתוֹ", "פקתלוה", "And they slew him"),
        ("וְאֶת-בָּנָיו", "ובניה", "and his sons"),
        ("וְאֶת-כָּל-עַמּוֹ", "וגמיע קומה", "and all his people,"),
        ("עַד-בִּלְתִּי הִשְׁאִיר-לוֹ", "חתי' לם יבק לה", "until not a survivor remained"),
        ("שָׂרִיד", "שרידא", "to him;"),
        ("וַיִּירְשׁוּ", "וחאזו", "and they took possession of"),
        ("אֶת-אַרְצוֹ", "בלדה", "his land."),
    ],
}

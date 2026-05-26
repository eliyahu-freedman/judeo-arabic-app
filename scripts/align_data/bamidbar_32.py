"""Hand-authored word-level alignment triples for Bamidbar chapter 32."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וּמִקְנֶה רַב הָיָה לִבְנֵי רְאוּבֵן וְלִבְנֵי-גָד--עָצוּם מְאֹד וַיִּרְאוּ אֶת-אֶרֶץ יַעְזֵר וְאֶת-אֶרֶץ גִּלְעָד וְהִנֵּה הַמָּקוֹם מְקוֹם מִקְנֶה
        # JA: ומאשיה כת'ירה. כאנת לבני ראובן. ולבני גד עצ'ימה גדא. פראו. בלד יעזר ובלד גרש. ואד'א בה מוצ'ע מאשיה
        # EN: And livestock, numerous, belonged to the sons of Reuben and to the sons of Gad — very great. And they saw the land of Jazer and the land of Gilead, and behold, it was a place for livestock.
        ("וּמִקְנֶה", "ומאשיה", "And livestock,"),
        ("רַב", "כת'ירה", "numerous,"),
        ("הָיָה", "כאנת", "belonged"),
        ("לִבְנֵי רְאוּבֵן", "לבני ראובן", "to the sons of Reuben"),
        ("וְלִבְנֵי-גָד", "ולבני גד", "and to the sons of Gad —"),
        ("עָצוּם מְאֹד", "עצ'ימה גדא", "very great."),
        ("וַיִּרְאוּ", "פראו", "And they saw"),
        ("אֶת-אֶרֶץ יַעְזֵר", "בלד יעזר", "the land of Jazer"),
        ("וְאֶת-אֶרֶץ גִּלְעָד", "ובלד גרש", "and the land of Gilead,"),
        ("וְהִנֵּה", "ואד'א בה", "and behold,"),
        ("הַמָּקוֹם מְקוֹם מִקְנֶה", "מוצ'ע מאשיה", "it was a place for livestock."),
    ],
    2: [
        # HE: וַיָּבֹאוּ בְנֵי-גָד וּבְנֵי רְאוּבֵן וַיֹּאמְרוּ אֶל-מֹשֶׁה וְאֶל-אֶלְעָזָר הַכֹּהֵן וְאֶל-נְשִׂיאֵי הָעֵדָה לֵאמֹר
        # JA: פגאו בני גד ובני ראובן. וקאלו למוסי' ואלעזר אלאמאם. ואשראף אלגמאעה קאילין
        # EN: And the sons of Gad and the sons of Reuben came, and said to Moses and Eleazar the imām and to the nobles of the congregation, saying:
        ("וַיָּבֹאוּ", "פגאו", "And the sons of Gad and the sons of Reuben came,"),
        ("בְנֵי-גָד", "בני גד", "and said"),
        ("וּבְנֵי רְאוּבֵן", "ובני ראובן", "to Moses"),
        ("וַיֹּאמְרוּ", "וקאלו", "and Eleazar"),
        ("אֶל-מֹשֶׁה", "למוסי'", "the imām"),
        ("וְאֶל-אֶלְעָזָר הַכֹּהֵן", "ואלעזר אלאמאם", "and to the nobles of"),
        ("וְאֶל-נְשִׂיאֵי הָעֵדָה", "ואשראף אלגמאעה", "the congregation,"),
        ("לֵאמֹר", "קאילין", "saying:"),
    ],
    3: [
        # HE: עֲטָרוֹת וְדִיבֹן וְיַעְזֵר וְנִמְרָה וְחֶשְׁבּוֹן וְאֶלְעָלֵה וּשְׂבָם וּנְבוֹ וּבְעֹן
        # JA: אן עטרות ודיבון ויעזב ונמרה. וחשבון ואלעלה. וסבם ונבו ובעון
        # EN: that Ataroth, and Dibon, and Jazer, and Nimrah, and Heshbon, and Elaleh, and Sibam, and Nebo, and Beon —
        (None, "אן", "that"),
        ("עֲטָרוֹת", "עטרות", "Ataroth,"),
        ("וְדִיבֹן", "ודיבון", "and Dibon,"),
        ("וְיַעְזֵר", "ויעזב", "and Jazer,"),
        ("וְנִמְרָה", "ונמרה", "and Nimrah,"),
        ("וְחֶשְׁבּוֹן", "וחשבון", "and Heshbon,"),
        ("וְאֶלְעָלֵה", "ואלעלה", "and Elaleh,"),
        ("וּשְׂבָם", "וסבם", "and Sibam,"),
        ("וּנְבוֹ", "ונבו", "and Nebo,"),
        ("וּבְעֹן", "ובעון", "and Beon —"),
    ],
    4: [
        # HE: הָאָרֶץ אֲשֶׁר הִכָּה יְהוָה לִפְנֵי עֲדַת יִשְׂרָאֵל--אֶרֶץ מִקְנֶה הִוא וְלַעֲבָדֶיךָ מִקְנֶה
        # JA: אלבלד. אלד'י פתחה אללה בין ידי גמאעה' בני אסראיל. הו בלד יצלח לאלמאשיה. ולעבידך מואשי
        # EN: the land which God opened before the congregation of the sons of Israel — it is a land suited for livestock, and your servants have livestock.
        ("הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר הִכָּה", "אלד'י פתחה", "which God opened"),
        ("יְהוָה", "אללה", "before"),
        ("לִפְנֵי עֲדַת", "בין ידי גמאעה'", "the congregation of"),
        ("יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel —"),
        ("הִוא", "הו", "it is"),
        ("אֶרֶץ מִקְנֶה", "בלד יצלח לאלמאשיה", "a land suited for livestock,"),
        ("וְלַעֲבָדֶיךָ מִקְנֶה", "ולעבידך מואשי", "and your servants have livestock."),
    ],
    5: [
        # HE: וַיֹּאמְרוּ אִם-מָצָאנוּ חֵן בְּעֵינֶיךָ--יֻתַּן אֶת-הָאָרֶץ הַזֹּאת לַעֲבָדֶיךָ לַאֲחֻזָּה אַל-תַּעֲבִרֵנוּ אֶת-הַיַּרְדֵּן
        # JA: פקאלו. אן וגדנא חצ'אא ענדך. ידפע אלינא הד'א אלבלד נחלה. לא תגיזנא אלארדן
        # EN: And they said: if we have found favor with you, let this land be given over to us as an inheritance; do not bring us across the Jordan.
        ("וַיֹּאמְרוּ", "פקאלו", "And they said:"),
        ("אִם-מָצָאנוּ", "אן וגדנא", "if we have found"),
        ("חֵן בְּעֵינֶיךָ", "חצ'אא ענדך", "favor with you,"),
        ("יֻתַּן", "ידפע אלינא", "let this land be given over"),
        ("אֶת-הָאָרֶץ הַזֹּאת", "הד'א אלבלד", "to us"),
        ("לַעֲבָדֶיךָ לַאֲחֻזָּה", "נחלה", "as an inheritance;"),
        ("אַל-תַּעֲבִרֵנוּ", "לא תגיזנא", "do not bring us across"),
        ("אֶת-הַיַּרְדֵּן", "אלארדן", "the Jordan."),
    ],
    6: [
        # HE: וַיֹּאמֶר מֹשֶׁה לִבְנֵי-גָד וְלִבְנֵי רְאוּבֵן הַאַחֵיכֶם יָבֹאוּ לַמִּלְחָמָה וְאַתֶּם תֵּשְׁבוּ פֹה
        # JA: פקאל להם מוסי'. הל אכ'ותכם ימצ'ון אלי' אלחרב. ואנתם תגלסון ההנא
        # EN: And Moses said to them: shall your brothers go forth to war while you sit here?
        ("וַיֹּאמֶר", "פקאל", "And Moses said"),
        ("מֹשֶׁה", "מוסי'", "to them:"),
        (None, "להם", "shall"),
        ("הַאַחֵיכֶם", "הל אכ'ותכם", "your brothers"),
        ("יָבֹאוּ", "ימצ'ון", "go forth"),
        ("לַמִּלְחָמָה", "אלי' אלחרב", "to war"),
        ("וְאַתֶּם", "ואנתם", "while you"),
        ("תֵּשְׁבוּ פֹה", "תגלסון ההנא", "sit here?"),
    ],
    7: [
        # HE: וְלָמָּה תנואון (תְנִיאוּן) אֶת-לֵב בְּנֵי יִשְׂרָאֵל--מֵעֲבֹר אֶל-הָאָרֶץ אֲשֶׁר-נָתַן לָהֶם יְהוָה
        # JA: ולם תגבנון קלוב בני אסראיל. מן אלמציר אלי' אלבלד. אלד'י אעטאהם אללה
        # EN: And why do you make the hearts of the sons of Israel faint from journeying to the land which God has given them?
        ("וְלָמָּה", "ולם", "And why do you make"),
        ("תנואון", "תגבנון", "the hearts of"),
        ("אֶת-לֵב", "קלוב", "the sons of Israel faint"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "from journeying"),
        ("מֵעֲבֹר", "מן אלמציר", "to the land"),
        ("אֶל-הָאָרֶץ", "אלי' אלבלד", "which God has given"),
        ("אֲשֶׁר-נָתַן לָהֶם יְהוָה", "אלד'י אעטאהם אללה", "them?"),
    ],
    8: [
        # HE: כֹּה עָשׂוּ אֲבֹתֵיכֶם בְּשָׁלְחִי אֹתָם מִקָּדֵשׁ בַּרְנֵעַ לִרְאוֹת אֶת-הָאָרֶץ
        # JA: כד'א צנעו אבאיכם. חין בעת'ת בהם. מן רקים ברנע לירומו אלבלד
        # EN: Thus did your fathers, when I sent them from Kadesh-barnea to scout out the land.
        ("כֹּה", "כד'א", "Thus"),
        ("עָשׂוּ", "צנעו", "did"),
        ("אֲבֹתֵיכֶם", "אבאיכם", "your fathers,"),
        ("בְּשָׁלְחִי", "חין בעת'ת", "when I sent"),
        ("אֹתָם", "בהם", "them"),
        ("מִקָּדֵשׁ בַּרְנֵעַ", "מן רקים ברנע", "from Kadesh-barnea"),
        ("לִרְאוֹת אֶת-הָאָרֶץ", "לירומו אלבלד", "to scout out the land."),
    ],
    9: [
        # HE: וַיַּעֲלוּ עַד-נַחַל אֶשְׁכּוֹל וַיִּרְאוּ אֶת-הָאָרֶץ וַיָּנִיאוּ אֶת-לֵב בְּנֵי יִשְׂרָאֵל--לְבִלְתִּי-בֹא אֶל-הָאָרֶץ אֲשֶׁר-נָתַן לָהֶם יְהוָה
        # JA: פבלג'ו אלי' ואד אלענקוד. וראוה. וגבנו קלוב בני אסראיל. מן אן ידכ'לו אלבלד. אלד'י אעטאהם אללה
        # EN: They reached the Valley of the Cluster and saw the land, and they made the hearts of the sons of Israel faint, so that they would not enter the land which God had given them.
        ("וַיַּעֲלוּ", "פבלג'ו", "They reached"),
        ("עַד-נַחַל אֶשְׁכּוֹל", "אלי' ואד אלענקוד", "the Valley of the Cluster"),
        ("וַיִּרְאוּ אֶת-הָאָרֶץ", "וראוה", "and saw the land,"),
        ("וַיָּנִיאוּ", "וגבנו", "and they made the hearts of"),
        ("אֶת-לֵב בְּנֵי יִשְׂרָאֵל", "קלוב בני אסראיל", "the sons of Israel faint,"),
        ("לְבִלְתִּי-בֹא", "מן אן ידכ'לו", "so that they would not enter"),
        ("אֶל-הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר-נָתַן לָהֶם יְהוָה", "אלד'י אעטאהם אללה", "which God had given them."),
    ],
    10: [
        # HE: וַיִּחַר-אַף יְהוָה בַּיּוֹם הַהוּא וַיִּשָּׁבַע לֵאמֹר
        # JA: פאשתד ג'צ'ב אללה פי ד'אלך אלוקת. ואקסם קאילא
        # EN: And God's wrath intensified at that time, and He swore, saying:
        ("וַיִּחַר-אַף יְהוָה", "פאשתד ג'צ'ב אללה", "And God's wrath intensified"),
        ("בַּיּוֹם הַהוּא", "פי ד'אלך אלוקת", "at that time,"),
        ("וַיִּשָּׁבַע", "ואקסם", "and He swore,"),
        ("לֵאמֹר", "קאילא", "saying:"),
    ],
    11: [
        # HE: אִם-יִרְאוּ הָאֲנָשִׁים הָעֹלִים מִמִּצְרַיִם מִבֶּן עֶשְׂרִים שָׁנָה וָמַעְלָה אֵת הָאֲדָמָה אֲשֶׁר נִשְׁבַּעְתִּי לְאַבְרָהָם לְיִצְחָק וּלְיַעֲקֹב כִּי לֹא-מִלְאוּ אַחֲרָי
        # JA: אן ראו אלרגאל אלד'י צעדו מן מצר. מן ן' עשרין סנה פצאעדא. אלבלד אלד'י אקסמת. לאברהים ויצחק ויעקוב. אד' לם יתבעו טאעתי
        # EN: 'The men who came up from Egypt, from twenty years old and upward, shall not see the land which I swore to Abraham and Isaac and Jacob, since they did not follow My obedience.
        ("אִם-יִרְאוּ", "אן ראו", "'The men"),
        ("הָאֲנָשִׁים", "אלרגאל", "who came up"),
        ("הָעֹלִים", "אלד'י צעדו", "from Egypt,"),
        ("מִמִּצְרַיִם", "מן מצר", "from twenty years old"),
        ("מִבֶּן עֶשְׂרִים שָׁנָה", "מן ן' עשרין סנה", "and upward, shall not see"),
        ("וָמַעְלָה", "פצאעדא", "the land"),
        ("אֵת הָאֲדָמָה", "אלבלד", "which I swore"),
        ("אֲשֶׁר נִשְׁבַּעְתִּי", "אלד'י אקסמת", "to Abraham"),
        ("לְאַבְרָהָם", "לאברהים", "and Isaac"),
        ("לְיִצְחָק", "ויצחק", "and Jacob —"),
        ("וּלְיַעֲקֹב", "ויעקוב", "since they did not follow"),
        ("כִּי לֹא-מִלְאוּ אַחֲרָי", "אד' לם יתבעו טאעתי", "My obedience."),
    ],
    12: [
        # HE: בִּלְתִּי כָּלֵב בֶּן-יְפֻנֶּה הַקְּנִזִּי וִיהוֹשֻׁעַ בִּן-נוּן כִּי מִלְאוּ אַחֲרֵי יְהוָה
        # JA: אלא כלב אבן יפנה אלקנזי. ויהושע אבן נון. פאנהמא אתבעא טאעה' אללה
        # EN: Except Caleb son of Jephunneh the Kenizzite and Joshua son of Nun, for they followed the obedience of God.'
        ("בִּלְתִּי", "אלא", "Except"),
        ("כָּלֵב", "כלב", "Caleb"),
        ("בֶּן-יְפֻנֶּה", "אבן יפנה", "son of Jephunneh"),
        ("הַקְּנִזִּי", "אלקנזי", "the Kenizzite"),
        ("וִיהוֹשֻׁעַ", "ויהושע", "and Joshua"),
        ("בִּן-נוּן", "אבן נון", "son of Nun,"),
        ("כִּי מִלְאוּ", "פאנהמא אתבעא", "for they followed"),
        ("אַחֲרֵי יְהוָה", "טאעה' אללה", "the obedience of God.'"),
    ],
    13: [
        # HE: וַיִּחַר-אַף יְהוָה בְּיִשְׂרָאֵל וַיְנִעֵם בַּמִּדְבָּר אַרְבָּעִים שָׁנָה--עַד-תֹּם כָּל-הַדּוֹר הָעֹשֶׂה הָרַע בְּעֵינֵי יְהוָה
        # JA: פלמא אשתד ג'צ'ב אללה עליהם. תווההם פי אלברייה ארבעין סנה. אלי' אן פני גמיע אלגיל. אלד'י פעל אלשר בין ידי אללה
        # EN: And when God's wrath intensified against them, He led them astray in the wilderness forty years, until the whole generation that had done evil before God had perished.
        ("וַיִּחַר-אַף יְהוָה", "פלמא אשתד ג'צ'ב אללה", "And when God's wrath intensified"),
        ("בְּיִשְׂרָאֵל", "עליהם", "against them,"),
        ("וַיְנִעֵם", "תווההם", "He led them astray"),
        ("בַּמִּדְבָּר", "פי אלברייה", "in the wilderness"),
        ("אַרְבָּעִים שָׁנָה", "ארבעין סנה", "forty years,"),
        ("עַד-תֹּם כָּל-הַדּוֹר", "אלי' אן פני גמיע אלגיל", "until the whole generation"),
        ("הָעֹשֶׂה הָרַע", "אלד'י פעל אלשר", "that had done evil"),
        ("בְּעֵינֵי יְהוָה", "בין ידי אללה", "before God had perished."),
    ],
    14: [
        # HE: וְהִנֵּה קַמְתֶּם תַּחַת אֲבֹתֵיכֶם--תַּרְבּוּת אֲנָשִׁים חַטָּאִים לִסְפּוֹת עוֹד עַל חֲרוֹן אַף-יְהוָה--אֶל-יִשְׂרָאֵל
        # JA: והד'אכם קד קמתם פי מכאן אבאיכם. עלי' תעלים אלנאס אלכ'אטיין. לתזידו איצ'א פי שדה' ג'צ'ב אללה עלי' אל אסראיל
        # EN: And behold, you have risen in the place of your fathers — in the teachings of sinful people — to add yet more to the intensity of God's wrath against the house of Israel.
        ("וְהִנֵּה", "והד'אכם", "And behold,"),
        ("קַמְתֶּם", "קד קמתם", "you have risen"),
        ("תַּחַת אֲבֹתֵיכֶם", "פי מכאן אבאיכם", "in the place of your fathers —"),
        ("תַּרְבּוּת אֲנָשִׁים", "עלי' תעלים אלנאס", "in the teachings of"),
        ("חַטָּאִים", "אלכ'אטיין", "sinful people —"),
        ("לִסְפּוֹת עוֹד", "לתזידו איצ'א", "to add yet more"),
        ("עַל חֲרוֹן", "פי שדה'", "to the intensity of"),
        ("אַף-יְהוָה", "ג'צ'ב אללה", "God's wrath"),
        ("אֶל-יִשְׂרָאֵל", "עלי' אל אסראיל", "against the house of Israel."),
    ],
    15: [
        # HE: כִּי תְשׁוּבֻן מֵאַחֲרָיו וְיָסַף עוֹד לְהַנִּיחוֹ בַּמִּדְבָּר וְשִׁחַתֶּם לְכָל-הָעָם הַזֶּה
        # JA: לאנכם אן רגעתם ען טאעתה. זאד פי תרכהם פי אלברייה. פתהלכון הולאי אלקום אד'א אמסכו ענכם
        # EN: For if you turn back from His obedience, He will increase His leaving them in the wilderness, and you will bring destruction upon these people if they hold to your view.
        ("כִּי", "לאנכם", "For"),
        ("תְשׁוּבֻן", "אן רגעתם", "if you turn back"),
        ("מֵאַחֲרָיו", "ען טאעתה", "from His obedience,"),
        ("וְיָסַף עוֹד", "זאד", "He will increase"),
        ("לְהַנִּיחוֹ", "פי תרכהם", "His leaving them"),
        ("בַּמִּדְבָּר", "פי אלברייה", "in the wilderness,"),
        ("וְשִׁחַתֶּם", "פתהלכון", "and you will bring destruction upon"),
        ("לְכָל-הָעָם הַזֶּה", "הולאי אלקום", "these people"),
        (None, "אד'א אמסכו ענכם", "if they hold to your view."),
    ],
    16: [
        # HE: וַיִּגְּשׁוּ אֵלָיו וַיֹּאמְרוּ גִּדְרֹת צֹאן נִבְנֶה לְמִקְנֵנוּ פֹּה וְעָרִים לְטַפֵּנוּ
        # JA: פתקדמו אליה וקאלו. אנא נבני חצ'אירא למואשינא ההנא. וקרא לאטפלנא
        # EN: Then they came forward to him and said: we will build enclosures for our livestock here, and towns for our children.
        ("וַיִּגְּשׁוּ", "פתקדמו", "Then they came forward"),
        ("אֵלָיו", "אליה", "to him"),
        ("וַיֹּאמְרוּ", "וקאלו", "and said:"),
        (None, "אנא", "we will build"),
        ("גִּדְרֹת צֹאן", "נבני חצ'אירא", "enclosures for"),
        ("לְמִקְנֵנוּ", "למואשינא", "our livestock"),
        ("פֹּה", "ההנא", "here,"),
        ("וְעָרִים", "וקרא", "and towns"),
        ("לְטַפֵּנוּ", "לאטפלנא", "for our children."),
    ],
    17: [
        # HE: וַאֲנַחְנוּ נֵחָלֵץ חֻשִׁים לִפְנֵי בְּנֵי יִשְׂרָאֵל עַד אֲשֶׁר אִם-הֲבִיאֹנֻם אֶל-מְקוֹמָם וְיָשַׁב טַפֵּנוּ בְּעָרֵי הַמִּבְצָר מִפְּנֵי יֹשְׁבֵי הָאָרֶץ
        # JA: ונחן נתגרד מסרעין. בין ידי בני אסראיל. אלי' אן נוצלהם אלי' מכאנהם. פיקים אטפאלנא פי קרא חצינה. מן קבל אהל אלבלד
        # EN: And we shall arm ourselves swiftly before the sons of Israel, until we bring them to their place; and our children shall dwell in fortified towns, on account of the inhabitants of the land.
        ("וַאֲנַחְנוּ", "ונחן", "And we"),
        ("נֵחָלֵץ", "נתגרד", "shall arm ourselves"),
        ("חֻשִׁים", "מסרעין", "swiftly"),
        ("לִפְנֵי בְּנֵי יִשְׂרָאֵל", "בין ידי בני אסראיל", "before the sons of Israel,"),
        ("עַד אֲשֶׁר אִם-הֲבִיאֹנֻם", "אלי' אן נוצלהם", "until we bring them"),
        ("אֶל-מְקוֹמָם", "אלי' מכאנהם", "to their place;"),
        ("וְיָשַׁב", "פיקים", "and our children shall dwell"),
        ("טַפֵּנוּ", "אטפאלנא", "in fortified towns,"),
        ("בְּעָרֵי הַמִּבְצָר", "פי קרא חצינה", "on account of"),
        ("מִפְּנֵי יֹשְׁבֵי הָאָרֶץ", "מן קבל אהל אלבלד", "the inhabitants of the land."),
    ],
    18: [
        # HE: לֹא נָשׁוּב אֶל-בָּתֵּינוּ--עַד הִתְנַחֵל בְּנֵי יִשְׂרָאֵל אִישׁ נַחֲלָתוֹ
        # JA: לא נרגע אלי' ביותנא. אלי' אן יחוז כל סבט מן בני אסראיל נחלתה
        # EN: We shall not return to our homes until every tribe of the sons of Israel has obtained its inheritance.
        ("לֹא נָשׁוּב", "לא נרגע", "We shall not return"),
        ("אֶל-בָּתֵּינוּ", "אלי' ביותנא", "to our homes"),
        ("עַד הִתְנַחֵל", "אלי' אן יחוז", "until every tribe of"),
        ("אִישׁ", "כל סבט", "the sons of Israel"),
        ("בְּנֵי יִשְׂרָאֵל", "מן בני אסראיל", "has obtained"),
        ("נַחֲלָתוֹ", "נחלתה", "its inheritance."),
    ],
    19: [
        # HE: כִּי לֹא נִנְחַל אִתָּם מֵעֵבֶר לַיַּרְדֵּן וָהָלְאָה כִּי בָאָה נַחֲלָתֵנוּ אֵלֵינוּ מֵעֵבֶר הַיַּרְדֵּן מִזְרָחָה
        # JA: לאנא לא נחוז מעהם. מן עבר אלארדן אלי' הנאך. אד' קד קבצ'נא נחלתנא. מן עבר אלארדן שרקייא
        # EN: For we shall not inherit with them from across the Jordan onward, since we have already received our inheritance from the eastern side of the Jordan.
        ("כִּי", "לאנא", "For"),
        ("לֹא נִנְחַל", "לא נחוז", "we shall not inherit"),
        ("אִתָּם", "מעהם", "with them"),
        ("מֵעֵבֶר לַיַּרְדֵּן", "מן עבר אלארדן", "from across the Jordan"),
        ("וָהָלְאָה", "אלי' הנאך", "onward,"),
        ("כִּי בָאָה", "אד' קד קבצ'נא", "since we have already received"),
        ("נַחֲלָתֵנוּ אֵלֵינוּ", "נחלתנא", "our inheritance"),
        ("מֵעֵבֶר הַיַּרְדֵּן מִזְרָחָה", "מן עבר אלארדן שרקייא", "from the eastern side of the Jordan."),
    ],
    20: [
        # HE: וַיֹּאמֶר אֲלֵיהֶם מֹשֶׁה אִם-תַּעֲשׂוּן אֶת-הַדָּבָר הַזֶּה אִם-תֵּחָלְצוּ לִפְנֵי יְהוָה לַמִּלְחָמָה
        # JA: פקאל להם מוסי'. אן צנעתם הד'א אלאמר. ותגרדתם בין ידי אליה לאלגיש
        # EN: And Moses said to them: if you do this thing, and arm yourselves before God for the host,
        ("וַיֹּאמֶר", "פקאל", "And Moses said"),
        ("אֲלֵיהֶם", "להם", "to them:"),
        ("מֹשֶׁה", "מוסי'", "if you do"),
        ("אִם-תַּעֲשׂוּן", "אן צנעתם", "this thing,"),
        ("אֶת-הַדָּבָר הַזֶּה", "הד'א אלאמר", "and arm yourselves"),
        ("אִם-תֵּחָלְצוּ", "ותגרדתם", "before God"),
        ("לִפְנֵי יְהוָה לַמִּלְחָמָה", "בין ידי אליה לאלגיש", "for the host,"),
    ],
    21: [
        # HE: וְעָבַר לָכֶם כָּל-חָלוּץ אֶת-הַיַּרְדֵּן לִפְנֵי יְהוָה עַד הוֹרִישׁוֹ אֶת-אֹיְבָיו מִפָּנָיו
        # JA: ועבר לכם כל מגרד מנכם. אלארדן בין ידיה. אלי' אן יקרץ' אעדאיה מן בין ידיה
        # EN: and every armed man among you crosses the Jordan before Him, until He cuts off His enemies from before Him —
        ("וְעָבַר לָכֶם", "ועבר לכם", "and every armed man among you"),
        ("כָּל-חָלוּץ", "כל מגרד מנכם", "crosses"),
        ("אֶת-הַיַּרְדֵּן", "אלארדן", "the Jordan"),
        ("לִפְנֵי יְהוָה", "בין ידיה", "before Him,"),
        ("עַד הוֹרִישׁוֹ", "אלי' אן יקרץ'", "until He cuts off"),
        ("אֶת-אֹיְבָיו", "אעדאיה", "His enemies"),
        ("מִפָּנָיו", "מן בין ידיה", "from before Him —"),
    ],
    22: [
        # HE: וְנִכְבְּשָׁה הָאָרֶץ לִפְנֵי יְהוָה וְאַחַר תָּשֻׁבוּ--וִהְיִיתֶם נְקִיִּם מֵיְהוָה וּמִיִּשְׂרָאֵל וְהָיְתָה הָאָרֶץ הַזֹּאת לָכֶם לַאֲחֻזָּה--לִפְנֵי יְהוָה
        # JA: ואד'א פתח אלבלד. בין ידיה פבעד ד'אלך תרגעון. פתכונון אבריא. ענד אללה וענד אל אסראיל. ויכון הד'א אלבלד לכם. חוזא בין ידיה
        # EN: and when the land is opened before Him, after that you shall return, and you shall be acquitted before God and before the house of Israel, and this land shall be yours as a possession before Him —
        ("וְנִכְבְּשָׁה הָאָרֶץ", "ואד'א פתח אלבלד", "and when the land is opened"),
        ("לִפְנֵי יְהוָה", "בין ידיה", "before Him,"),
        ("וְאַחַר", "פבעד ד'אלך", "after that"),
        ("תָּשֻׁבוּ", "תרגעון", "you shall return,"),
        ("וִהְיִיתֶם נְקִיִּם", "פתכונון אבריא", "and you shall be acquitted"),
        ("מֵיְהוָה", "ענד אללה", "before God"),
        ("וּמִיִּשְׂרָאֵל", "וענד אל אסראיל", "and before the house of Israel,"),
        ("וְהָיְתָה הָאָרֶץ הַזֹּאת", "ויכון הד'א אלבלד", "and this land shall be"),
        ("לָכֶם", "לכם", "yours"),
        ("לַאֲחֻזָּה", "חוזא", "as a possession"),
        ("לִפְנֵי יְהוָה", "בין ידיה", "before Him —"),
    ],
    23: [
        # HE: וְאִם-לֹא תַעֲשׂוּן כֵּן הִנֵּה חֲטָאתֶם לַיהוָה וּדְעוּ חַטַּאתְכֶם אֲשֶׁר תִּמְצָא אֶתְכֶם
        # JA: ואן לם תצנעון כד'אך. פקד אכ'טאתם ללה. ואעתרפו בכ'טאיאכם אד'א נאלתכם עקובתה
        # EN: but if you do not do thus, you have sinned against God; and acknowledge your sins when His punishment reaches you.
        ("וְאִם-לֹא", "ואן לם", "but if you do not"),
        ("תַעֲשׂוּן כֵּן", "תצנעון כד'אך", "do thus,"),
        ("הִנֵּה חֲטָאתֶם", "פקד אכ'טאתם", "you have sinned"),
        ("לַיהוָה", "ללה", "against God;"),
        ("וּדְעוּ", "ואעתרפו", "and acknowledge"),
        ("חַטַּאתְכֶם", "בכ'טאיאכם", "your sins"),
        ("אֲשֶׁר תִּמְצָא אֶתְכֶם", "אד'א נאלתכם עקובתה", "when His punishment reaches you."),
    ],
    24: [
        # HE: בְּנוּ-לָכֶם עָרִים לְטַפְּכֶם וּגְדֵרֹת לְצֹנַאֲכֶם וְהַיֹּצֵא מִפִּיכֶם תַּעֲשׂוּ
        # JA: אבנו לכם קרא לאטפאלכם. וחצ'אירא לג'נמכם. ומא כ'רג מן פמכם אצנעוה
        # EN: Build yourselves towns for your children, and enclosures for your flocks, and what has gone out of your mouth — carry it out.
        ("בְּנוּ-לָכֶם", "אבנו לכם", "Build yourselves"),
        ("עָרִים", "קרא", "towns"),
        ("לְטַפְּכֶם", "לאטפאלכם", "for your children,"),
        ("וּגְדֵרֹת", "וחצ'אירא", "and enclosures"),
        ("לְצֹנַאֲכֶם", "לג'נמכם", "for your flocks,"),
        ("וְהַיֹּצֵא", "ומא כ'רג", "and what has gone out"),
        ("מִפִּיכֶם", "מן פמכם", "of your mouth —"),
        ("תַּעֲשׂוּ", "אצנעוה", "carry it out."),
    ],
    25: [
        # HE: וַיֹּאמֶר בְּנֵי-גָד וּבְנֵי רְאוּבֵן אֶל-מֹשֶׁה לֵאמֹר עֲבָדֶיךָ יַעֲשׂוּ כַּאֲשֶׁר אֲדֹנִי מְצַוֶּה
        # JA: קאלו לה. עבידך יצנעון. כמא יאמרהם סיידנא
        # EN: They said to him: your servants shall do as our lord commands them.
        ("וַיֹּאמֶר", "קאלו", "They said"),
        ("אֶל-מֹשֶׁה", "לה", "to him:"),
        ("עֲבָדֶיךָ", "עבידך", "your servants"),
        ("יַעֲשׂוּ", "יצנעון", "shall do"),
        ("כַּאֲשֶׁר", "כמא", "as"),
        ("אֲדֹנִי", "סיידנא", "our lord"),
        ("מְצַוֶּה", "יאמרהם", "commands them."),
    ],
    26: [
        # HE: טַפֵּנוּ נָשֵׁינוּ מִקְנֵנוּ וְכָל-בְּהֶמְתֵּנוּ--יִהְיוּ-שָׁם בְּעָרֵי הַגִּלְעָד
        # JA: אטפאלנא ונסאנא. מואשינא וסאיר בהאימנא. יקימון פי בלד גרש
        # EN: Our children and our women, our livestock and the rest of our beasts, shall dwell in the land of Gilead.
        ("טַפֵּנוּ", "אטפאלנא", "Our children"),
        ("נָשֵׁינוּ", "ונסאנא", "and our women,"),
        ("מִקְנֵנוּ", "מואשינא", "our livestock"),
        ("וְכָל-בְּהֶמְתֵּנוּ", "וסאיר בהאימנא", "and the rest of our beasts,"),
        ("יִהְיוּ-שָׁם", "יקימון", "shall dwell"),
        ("בְּעָרֵי הַגִּלְעָד", "פי בלד גרש", "in the land of Gilead."),
    ],
    27: [
        # HE: וַעֲבָדֶיךָ יַעַבְרוּ כָּל-חֲלוּץ צָבָא לִפְנֵי יְהוָה--לַמִּלְחָמָה כַּאֲשֶׁר אֲדֹנִי דֹּבֵר
        # JA: ועבידך יעברון. כל מגרד מנהם ללגיש. בין ידי אללה לאלחרב. כמא קאל סיידנא
        # EN: And your servants shall cross over, every armed man among them for the host, before God, for the war — as our lord has said.
        ("וַעֲבָדֶיךָ", "ועבידך", "And your servants"),
        ("יַעַבְרוּ", "יעברון", "shall cross over,"),
        ("כָּל-חֲלוּץ", "כל מגרד מנהם", "every armed man among them"),
        ("צָבָא", "ללגיש", "for the host,"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God,"),
        ("לַמִּלְחָמָה", "לאלחרב", "for the war —"),
        ("כַּאֲשֶׁר אֲדֹנִי דֹּבֵר", "כמא קאל סיידנא", "as our lord has said."),
    ],
    28: [
        # HE: וַיְצַו לָהֶם מֹשֶׁה אֵת אֶלְעָזָר הַכֹּהֵן וְאֵת יְהוֹשֻׁעַ בִּן-נוּן וְאֶת-רָאשֵׁי אֲבוֹת הַמַּטּוֹת לִבְנֵי יִשְׂרָאֵל
        # JA: פאמר להם מוסי'. אלעזר אלאמאם ויהושע אבן נון. ורויסא אבא אסבאט בני אסראיל
        # EN: And Moses gave instructions concerning them to Eleazar the imām and Joshua son of Nun, and to the heads of the fathers of the tribes of the sons of Israel.
        ("וַיְצַו", "פאמר", "And Moses gave instructions"),
        ("מֹשֶׁה", "מוסי'", "concerning them"),
        (None, "להם", "to"),
        ("אֵת אֶלְעָזָר הַכֹּהֵן", "אלעזר אלאמאם", "Eleazar the imām"),
        ("וְאֵת יְהוֹשֻׁעַ", "ויהושע", "and Joshua"),
        ("בִּן-נוּן", "אבן נון", "son of Nun,"),
        ("וְאֶת-רָאשֵׁי אֲבוֹת הַמַּטּוֹת", "ורויסא אבא אסבאט", "and to the heads of the fathers of the tribes of"),
        ("לִבְנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel."),
    ],
    29: [
        # HE: וַיֹּאמֶר מֹשֶׁה אֲלֵהֶם אִם-יַעַבְרוּ בְנֵי-גָד וּבְנֵי-רְאוּבֵן אִתְּכֶם אֶת-הַיַּרְדֵּן כָּל-חָלוּץ לַמִּלְחָמָה לִפְנֵי יְהוָה וְנִכְבְּשָׁה הָאָרֶץ לִפְנֵיכֶם--וּנְתַתֶּם לָהֶם אֶת-אֶרֶץ הַגִּלְעָד לַאֲחֻזָּה
        # JA: פקאל אן עברו מעכם אלארדן. כל רגל מגרד לאלחרב בין ידי אללה. חתי יפתח אלבלד בין אידיכם. פאעטוהם בלד גרש חוזא
        # EN: And he said: if every armed man among them crosses the Jordan with you for war before God, until the land is opened before you, then give them the land of Gilead as a possession.
        ("וַיֹּאמֶר מֹשֶׁה אֲלֵהֶם", "פקאל", "And he said:"),
        ("אִם-יַעַבְרוּ", "אן עברו", "if every armed man"),
        ("כָּל-חָלוּץ", "כל רגל מגרד", "among them crosses"),
        ("אִתְּכֶם אֶת-הַיַּרְדֵּן", "מעכם אלארדן", "the Jordan with you"),
        ("לַמִּלְחָמָה", "לאלחרב", "for war"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God,"),
        ("וְנִכְבְּשָׁה הָאָרֶץ", "חתי יפתח אלבלד", "until the land is opened"),
        ("לִפְנֵיכֶם", "בין אידיכם", "before you,"),
        ("וּנְתַתֶּם לָהֶם", "פאעטוהם", "then give them"),
        ("אֶת-אֶרֶץ הַגִּלְעָד", "בלד גרש", "the land of Gilead"),
        ("לַאֲחֻזָּה", "חוזא", "as a possession."),
    ],
    30: [
        # HE: וְאִם-לֹא יַעַבְרוּ חֲלוּצִים אִתְּכֶם--וְנֹאחֲזוּ בְתֹכְכֶם בְּאֶרֶץ כְּנָעַן
        # JA: ואן לם יעברון מגרדין מעכם. פליחוזו פי מא בינכם פי בלד כנעאן
        # EN: But if they do not cross over armed with you, then let them receive a holding among you in the land of Canaan.
        ("וְאִם-לֹא", "ואן לם", "But if they do not"),
        ("יַעַבְרוּ חֲלוּצִים", "יעברון מגרדין", "cross over armed"),
        ("אִתְּכֶם", "מעכם", "with you,"),
        ("וְנֹאחֲזוּ", "פליחוזו", "then let them receive a holding"),
        ("בְתֹכְכֶם", "פי מא בינכם", "among you"),
        ("בְּאֶרֶץ כְּנָעַן", "פי בלד כנעאן", "in the land of Canaan."),
    ],
    31: [
        # HE: וַיַּעֲנוּ בְנֵי-גָד וּבְנֵי רְאוּבֵן לֵאמֹר אֵת אֲשֶׁר דִּבֶּר יְהוָה אֶל-עֲבָדֶיךָ כֵּן נַעֲשֶׂה
        # JA: פאגאבוה וקאלו לה. גמיע מא אמר אללה בה עבידך אנא צאנעין
        # EN: And they answered him and said to him: all that God has commanded — your servants — we shall carry out.
        ("וַיַּעֲנוּ", "פאגאבוה", "And they answered him"),
        ("בְנֵי-גָד וּבְנֵי רְאוּבֵן", "וקאלו", "and said"),
        ("לֵאמֹר", "לה", "to him:"),
        ("אֵת אֲשֶׁר דִּבֶּר יְהוָה", "גמיע מא אמר אללה", "all that God has commanded —"),
        ("אֶל-עֲבָדֶיךָ", "בה עבידך", "your servants —"),
        ("כֵּן נַעֲשֶׂה", "אנא צאנעין", "we shall carry out."),
    ],
    32: [
        # HE: נַחְנוּ נַעֲבֹר חֲלוּצִים לִפְנֵי יְהוָה אֶרֶץ כְּנָעַן וְאִתָּנוּ אֲחֻזַּת נַחֲלָתֵנוּ מֵעֵבֶר לַיַּרְדֵּן
        # JA: נחן נעבר מגרדין. בין ידי אללה אלי' בלד כנעאן. חתי יחצל לנא חוז נחלתנא. מן עבר אלארדן
        # EN: We shall cross over armed before God to the land of Canaan, so that the possession of our inheritance on the eastern side of the Jordan may be secured to us.
        ("נַחְנוּ", "נחן", "We shall cross over"),
        ("נַעֲבֹר", "נעבר", "armed"),
        ("חֲלוּצִים", "מגרדין", "before God"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "to the land of Canaan,"),
        ("אֶרֶץ כְּנָעַן", "אלי' בלד כנעאן", "so that the possession"),
        ("וְאִתָּנוּ אֲחֻזַּת נַחֲלָתֵנוּ", "חתי יחצל לנא חוז נחלתנא", "of our inheritance"),
        ("מֵעֵבֶר לַיַּרְדֵּן", "מן עבר אלארדן", "may be secured to us."),
    ],
    33: [
        # HE: וַיִּתֵּן לָהֶם מֹשֶׁה לִבְנֵי-גָד וְלִבְנֵי רְאוּבֵן וְלַחֲצִי שֵׁבֶט מְנַשֶּׁה בֶן-יוֹסֵף אֶת-מַמְלֶכֶת סִיחֹן מֶלֶךְ הָאֱמֹרִי וְאֶת-מַמְלֶכֶת עוֹג מֶלֶךְ הַבָּשָׁן הָאָרֶץ לְעָרֶיהָ בִּגְבֻלֹת--עָרֵי הָאָרֶץ סָבִיב
        # JA: פאעטא מוסי' בני גד ובני ראובן. ונצף סבט מנשה אבן יוסף בלד ממלכה' סיחון מלך אלאמוריין. ובלד ממלכה' עוג מלך אלבת'נייה. כל ארץ' מע קראהא. אלד'י עלי' תכ'מהא מסתדירא
        # EN: So Moses gave to the sons of Gad and to the sons of Reuben and to the half-tribe of Manasseh son of Joseph the land of the kingdom of Sihon king of the Amorites and the land of the kingdom of Og king of Bashan — the whole land with its towns, which are within its borders all around.
        ("וַיִּתֵּן", "פאעטא", "So Moses gave"),
        ("מֹשֶׁה", "מוסי'", "to the sons of Gad"),
        ("לִבְנֵי-גָד", "בני גד", "and to the sons of Reuben"),
        ("וְלִבְנֵי רְאוּבֵן", "ובני ראובן", "and to the half-tribe of"),
        ("וְלַחֲצִי שֵׁבֶט מְנַשֶּׁה", "ונצף סבט מנשה", "Manasseh son of Joseph"),
        ("בֶן-יוֹסֵף", "אבן יוסף", "the land of the kingdom of"),
        ("אֶת-מַמְלֶכֶת סִיחֹן", "בלד ממלכה' סיחון", "Sihon king of the Amorites"),
        ("מֶלֶךְ הָאֱמֹרִי", "מלך אלאמוריין", "and the land of the kingdom of"),
        ("וְאֶת-מַמְלֶכֶת עוֹג", "ובלד ממלכה' עוג", "Og king of Bashan —"),
        ("מֶלֶךְ הַבָּשָׁן", "מלך אלבת'נייה", "the whole land"),
        ("הָאָרֶץ לְעָרֶיהָ", "כל ארץ' מע קראהא", "with its towns,"),
        ("בִּגְבֻלֹת--עָרֵי הָאָרֶץ סָבִיב", "אלד'י עלי' תכ'מהא מסתדירא", "which are within its borders all around."),
    ],
    34: [
        # HE: וַיִּבְנוּ בְנֵי-גָד אֶת-דִּיבֹן וְאֶת-עֲטָרֹת וְאֵת עֲרֹעֵר
        # JA: פבנו בני גד. דיבון ועטרות וערוער
        # EN: And the sons of Gad built Dibon, and Ataroth, and Aroer,
        ("וַיִּבְנוּ בְנֵי-גָד", "פבנו בני גד", "And the sons of Gad built"),
        ("אֶת-דִּיבֹן", "דיבון", "Dibon,"),
        ("וְאֶת-עֲטָרֹת", "ועטרות", "and Ataroth,"),
        ("וְאֵת עֲרֹעֵר", "וערוער", "and Aroer,"),
    ],
    35: [
        # HE: וְאֶת-עַטְרֹת שׁוֹפָן וְאֶת-יַעְזֵר וְיָגְבְּהָה
        # JA: ועטרות שופן ויעזר ויגהה
        # EN: and Atroth-shophan, and Jazer, and Jogbehah,
        ("וְאֶת-עַטְרֹת שׁוֹפָן", "ועטרות שופן", "and Atroth-shophan,"),
        ("וְאֶת-יַעְזֵר", "ויעזר", "and Jazer,"),
        ("וְיָגְבְּהָה", "ויגהה", "and Jogbehah,"),
    ],
    36: [
        # HE: וְאֶת-בֵּית נִמְרָה וְאֶת-בֵּית הָרָן עָרֵי מִבְצָר וְגִדְרֹת צֹאן
        # JA: ובית נמרה ובית הרן. קרא חצינה וחצ'איר ג'נם
        # EN: and Beth-nimrah and Beth-haran — fortified towns, and enclosures for flocks.
        ("וְאֶת-בֵּית נִמְרָה", "ובית נמרה", "and Beth-nimrah"),
        ("וְאֶת-בֵּית הָרָן", "ובית הרן", "and Beth-haran —"),
        ("עָרֵי מִבְצָר", "קרא חצינה", "fortified towns,"),
        ("וְגִדְרֹת צֹאן", "וחצ'איר ג'נם", "and enclosures for flocks."),
    ],
    37: [
        # HE: וּבְנֵי רְאוּבֵן בָּנוּ אֶת-חֶשְׁבּוֹן וְאֶת-אֶלְעָלֵא וְאֵת קִרְיָתָיִם
        # JA: ובנו בני ראובן. חשבון ואלעלא וקריתים
        # EN: And the sons of Reuben built Heshbon, and Elaleh, and Kiriathaim,
        ("וּבְנֵי רְאוּבֵן", "ובנו בני ראובן", "And the sons of Reuben built"),
        ("אֶת-חֶשְׁבּוֹן", "חשבון", "Heshbon,"),
        ("וְאֶת-אֶלְעָלֵא", "ואלעלא", "and Elaleh,"),
        ("וְאֵת קִרְיָתָיִם", "וקריתים", "and Kiriathaim,"),
    ],
    38: [
        # HE: וְאֶת-נְבוֹ וְאֶת-בַּעַל מְעוֹן מוּסַבֹּת שֵׁם--וְאֶת-שִׂבְמָה וַיִּקְרְאוּ בְשֵׁמֹת אֶת-שְׁמוֹת הֶעָרִים אֲשֶׁר בָּנוּ
        # JA: ונבו ובעל מעון. מנקולה אסמאיהן וסבמה. וד'אלך אנהם סמו אלקרא אלתי בנוהא כמא שאו
        # EN: and Nebo, and Baal-meon — their names being transferred — and Sibmah; for they gave names to the towns which they built as they saw fit.
        ("וְאֶת-נְבוֹ", "ונבו", "and Nebo,"),
        ("וְאֶת-בַּעַל מְעוֹן", "ובעל מעון", "and Baal-meon —"),
        ("מוּסַבֹּת שֵׁם", "מנקולה אסמאיהן", "their names being transferred —"),
        ("וְאֶת-שִׂבְמָה", "וסבמה", "and Sibmah;"),
        ("וַיִּקְרְאוּ", "וד'אלך אנהם סמו", "for they gave names"),
        ("בְשֵׁמֹת אֶת-שְׁמוֹת הֶעָרִים", "אלקרא אלתי בנוהא", "to the towns which they built"),
        ("אֲשֶׁר בָּנוּ", "כמא שאו", "as they saw fit."),
    ],
    39: [
        # HE: וַיֵּלְכוּ בְּנֵי מָכִיר בֶּן-מְנַשֶּׁה גִּלְעָדָה--וַיִּלְכְּדֻהָ וַיּוֹרֶשׁ אֶת-הָאֱמֹרִי אֲשֶׁר-בָּהּ
        # JA: ת'ם מצ'ו בני מכיר אבן מנשה אלי' גרש פפתחוהא. וקרצ'ו אלאמורי אלד'י פיהא
        # EN: Then the sons of Machir son of Manasseh went to Gilead and took it, and drove out the Amorite who was in it.
        (None, "ת'ם", "Then"),
        ("וַיֵּלְכוּ", "מצ'ו", "went"),
        ("בְּנֵי מָכִיר", "בני מכיר", "the sons of Machir"),
        ("בֶּן-מְנַשֶּׁה", "אבן מנשה", "son of Manasseh"),
        ("גִּלְעָדָה", "אלי' גרש", "to Gilead"),
        ("וַיִּלְכְּדֻהָ", "פפתחוהא", "and took it,"),
        ("וַיּוֹרֶשׁ", "וקרצ'ו", "and drove out"),
        ("אֶת-הָאֱמֹרִי", "אלאמורי", "the Amorite"),
        ("אֲשֶׁר-בָּהּ", "אלד'י פיהא", "who was in it."),
    ],
    40: [
        # HE: וַיִּתֵּן מֹשֶׁה אֶת-הַגִּלְעָד לְמָכִיר בֶּן-מְנַשֶּׁה וַיֵּשֶׁב בָּהּ
        # JA: פדפע מוסי' גרש. לאל מכיר אבן מנשה. פאקאמו פיהא
        # EN: And Moses gave Gilead to Machir son of Manasseh, and they settled in it.
        ("וַיִּתֵּן", "פדפע", "And Moses gave"),
        ("מֹשֶׁה", "מוסי'", "Gilead"),
        ("אֶת-הַגִּלְעָד", "גרש", "to Machir"),
        ("לְמָכִיר", "לאל מכיר", "son of Manasseh,"),
        ("בֶּן-מְנַשֶּׁה", "אבן מנשה", "and they settled"),
        ("וַיֵּשֶׁב בָּהּ", "פאקאמו פיהא", "in it."),
    ],
    41: [
        # HE: וְיָאִיר בֶּן-מְנַשֶּׁה הָלַךְ וַיִּלְכֹּד אֶת-חַוֹּתֵיהֶם וַיִּקְרָא אֶתְהֶן חַוֹּת יָאִיר
        # JA: פמצ'א יאיר אבן מנשה. ופתח סואדהן. וסמאהא סואד יאיר
        # EN: And Jair son of Manasseh went and captured their villages, and called them the Villages of Jair.
        ("וְיָאִיר", "פמצ'א יאיר", "And Jair"),
        ("בֶּן-מְנַשֶּׁה", "אבן מנשה", "son of Manasseh went"),
        ("הָלַךְ וַיִּלְכֹּד", "ופתח", "and captured"),
        ("אֶת-חַוֹּתֵיהֶם", "סואדהן", "their villages,"),
        ("וַיִּקְרָא אֶתְהֶן", "וסמאהא", "and called them"),
        ("חַוֹּת יָאִיר", "סואד יאיר", "the Villages of Jair."),
    ],
    42: [
        # HE: וְנֹבַח הָלַךְ וַיִּלְכֹּד אֶת-קְנָת וְאֶת-בְּנֹתֶיהָ וַיִּקְרָא לָה נֹבַח בִּשְׁמוֹ
        # JA: ומצ'א נבח. פפתח קנת ורסאתיקהא. וסמאהא נבח עלי' אסמה
        # EN: And Nobah went and captured Kenath and its districts, and called it Nobah after his own name.
        ("וְנֹבַח", "ומצ'א נבח", "And Nobah went"),
        ("הָלַךְ וַיִּלְכֹּד", "פפתח", "and captured"),
        ("אֶת-קְנָת", "קנת", "Kenath"),
        ("וְאֶת-בְּנֹתֶיהָ", "ורסאתיקהא", "and its districts,"),
        ("וַיִּקְרָא לָה", "וסמאהא", "and called it"),
        ("נֹבַח", "נבח", "Nobah"),
        ("בִּשְׁמוֹ", "עלי' אסמה", "after his own name."),
    ],
}

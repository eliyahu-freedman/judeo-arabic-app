"""Hand-authored alignment triples for Vayikra chapter 1.

Word-level: each JA (Saadia) word is its own group, mapped to the Hebrew word
it renders and its English counterpart. The runtime resolver matches each side
independently (lib/alignment.ts), so words link correctly even across word-order
crossings — verb-subject inversions, English-fronted negations, and Hebrew
construct reorderings. Words Saadia adds with no Hebrew source (glosses,
expansions) carry he=None and link JA↔English only.
"""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    # JA: "כ'אטב בני אסראיל וקל להם. אי אנסאן קרב מנכם קרבאנא ללה. מן אלבהאים. פמן אלבקר ואלג'נם תקרבונה"
    # HE: "דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם אָדָם כִּי-יַקְרִיב מִכֶּם קָרְבָּן לַיהוָה--מִן-הַבְּהֵמָה מִן-הַבָּקָר וּמִן-הַצֹּאן תַּקְרִיבוּ אֶת-קָרְבַּנְכֶם"
    # EN: "Address the sons of Israel and say to them: any person among you who brings an offering to God — from the beasts, from the cattle and the flock shall you bring it."
    2: [
        ("דַּבֵּר", "כ'אטב", "Address"),
        ("אֶל-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them"),
        ("אָדָם", "אי אנסאן", "any person"),
        ("כִּי-יַקְרִיב", "קרב", "who brings"),
        ("מִכֶּם", "מנכם", "among you"),
        ("קָרְבָּן", "קרבאנא", "an offering"),
        ("לַיהוָה", "ללה", "to God"),
        ("מִן-הַבְּהֵמָה", "מן אלבהאים", "from the beasts"),
        ("מִן-הַבָּקָר", "פמן אלבקר", "from the cattle"),
        ("וּמִן-הַצֹּאן", "ואלג'נם", "and the flock"),
        ("תַּקְרִיבוּ אֶת-קָרְבַּנְכֶם", "תקרבונה", "shall you bring it"),
    ],
    # JA: "אן כאן קרבאנה צעידה מן אלבקר. פד'כר צחיח יקרבה. פליקדמה אלי' באב כ'בא אלמחצ'ר. עלי' מא ירתצ'א ענה בין ידי אללה"
    # HE: "אִם-עֹלָה קָרְבָּנוֹ מִן-הַבָּקָר זָכָר תָּמִים יַקְרִיבֶנּוּ אֶל-פֶּתַח אֹהֶל מוֹעֵד יַקְרִיב אֹתוֹ לִרְצֹנוֹ לִפְנֵי יְהוָה"
    # EN: "If his offering is an ascent-offering from the cattle, a sound male shall he bring it; he shall present it at the entrance of the tent of the assembly, according to what shall be acceptable of him before God."
    3: [
        ("אִם-עֹלָה", "אן כאן", "If"),
        ("קָרְבָּנוֹ", "קרבאנה", "his offering"),
        (None, "צעידה", "an ascent-offering"),
        ("מִן-הַבָּקָר", "מן אלבקר", "from the cattle"),
        ("זָכָר תָּמִים", "פד'כר צחיח", "a sound male"),
        ("יַקְרִיבֶנּוּ", "יקרבה", "shall he bring it"),
        ("אֶל-פֶּתַח", "פליקדמה אלי' באב", "he shall present it at the entrance of"),
        ("אֹהֶל", "כ'בא", "the tent of"),
        ("מוֹעֵד", "אלמחצ'ר", "the assembly"),
        ("לִרְצֹנוֹ", "עלי' מא ירתצ'א ענה", "according to what shall be acceptable of him"),
        ("לִפְנֵי", "בין ידי", "before"),
        ("יְהוָה", "אללה", "God"),
    ],
    # JA: "ויסנד ידה עלי' ראסה. וירצ'א ענה ויג'פר לה"
    # HE: "וְסָמַךְ יָדוֹ עַל רֹאשׁ הָעֹלָה וְנִרְצָה לוֹ לְכַפֵּר עָלָיו"
    # EN: "And he shall lean his hand upon its head, and it shall be accepted of him and forgiven him."
    4: [
        ("וְסָמַךְ", "ויסנד", "And he shall lean"),
        ("יָדוֹ", "ידה", "his hand"),
        ("עַל", "עלי'", "upon"),
        ("רֹאשׁ", "ראסה", "its head"),
        ("וְנִרְצָה לוֹ", "וירצ'א ענה", "and it shall be accepted of him"),
        ("לְכַפֵּר", "ויג'פר", "and forgiven"),
        ("עָלָיו", "לה", "him"),
    ],
    # JA: "ויד'בח אלרת' בין ידי אללה. ויקרב בני הרון אלאיימה אלדם. וירשוה עלי' אלמד'בח מסתדירא. אלד'י ענד באב כ'בא אלמחצ'ר"
    # HE: "וְשָׁחַט אֶת-בֶּן הַבָּקָר לִפְנֵי יְהוָה וְהִקְרִיבוּ בְּנֵי אַהֲרֹן הַכֹּהֲנִים אֶת-הַדָּם וְזָרְקוּ אֶת-הַדָּם עַל-הַמִּזְבֵּחַ סָבִיב אֲשֶׁר-פֶּתַח אֹהֶל מוֹעֵד"
    # EN: "And he shall slaughter the bullock before God; and the sons of Aaron, the priests, shall bring the blood near, and shall sprinkle it upon the altar all around, which is at the entrance of the tent of the assembly."
    5: [
        ("וְשָׁחַט", "ויד'בח", "And he shall slaughter"),
        ("אֶת-בֶּן הַבָּקָר", "אלרת'", "the bullock"),
        ("לִפְנֵי", "בין ידי", "before"),
        ("יְהוָה", "אללה", "God"),
        ("וְהִקְרִיבוּ", "ויקרב", "shall bring"),
        ("בְּנֵי", "בני", "the sons of"),
        ("אַהֲרֹן", "הרון", "Aaron"),
        ("הַכֹּהֲנִים", "אלאיימה", "the priests"),
        ("אֶת-הַדָּם", "אלדם", "the blood near"),
        ("וְזָרְקוּ", "וירשוה", "and shall sprinkle it"),
        ("עַל-הַמִּזְבֵּחַ", "עלי' אלמד'בח", "upon the altar"),
        ("סָבִיב", "מסתדירא", "all around"),
        ("אֲשֶׁר-פֶּתַח", "אלד'י ענד באב", "which is at the entrance of"),
        ("אֹהֶל", "כ'בא", "the tent of"),
        ("מוֹעֵד", "אלמחצ'ר", "the assembly"),
    ],
    # JA: "ויסלך' אלצעידה ויעצ'יהא אעצ'אא"
    # HE: "וְהִפְשִׁיט אֶת-הָעֹלָה וְנִתַּח אֹתָהּ לִנְתָחֶיהָ"
    # EN: "And he shall flay the ascent-offering and divide it into its limbs."
    6: [
        ("וְהִפְשִׁיט", "ויסלך'", "And he shall flay"),
        ("אֶת-הָעֹלָה", "אלצעידה", "the ascent-offering"),
        ("וְנִתַּח", "ויעצ'יהא", "and divide it"),
        ("לִנְתָחֶיהָ", "אעצ'אא", "into its limbs"),
    ],
    # JA: "וישעלון בני הרון אלאמאם. נארא עלי' אלמד'בח. וינצ'דון עליהא חטבא"
    # HE: "וְנָתְנוּ בְּנֵי אַהֲרֹן הַכֹּהֵן אֵשׁ--עַל-הַמִּזְבֵּחַ וְעָרְכוּ עֵצִים עַל-הָאֵשׁ"
    # EN: "And the sons of Aaron, the priest, shall kindle fire upon the altar, and shall arrange wood upon it."
    7: [
        ("וְנָתְנוּ", "וישעלון", "shall kindle"),
        ("בְּנֵי", "בני", "the sons of"),
        ("אַהֲרֹן", "הרון", "Aaron"),
        ("הַכֹּהֵן", "אלאמאם", "the priest"),
        ("אֵשׁ", "נארא", "fire"),
        ("עַל-הַמִּזְבֵּחַ", "עלי' אלמד'בח", "upon the altar"),
        ("וְעָרְכוּ", "וינצ'דון", "and shall arrange"),
        ("עֵצִים", "חטבא", "wood"),
        ("עַל-הָאֵשׁ", "עליהא", "upon it"),
    ],
    # JA: "וינצ'ד בני הרון אלאיימה. אלאעצ'א ואלראס ואלקצבה. עלי' אלחטב אלד'י עלי' אלנאר. אלד'י עלי' אלמד'בח"
    # HE: "וְעָרְכוּ בְּנֵי אַהֲרֹן הַכֹּהֲנִים אֵת הַנְּתָחִים אֶת-הָרֹאשׁ וְאֶת-הַפָּדֶר--עַל-הָעֵצִים אֲשֶׁר עַל-הָאֵשׁ אֲשֶׁר עַל-הַמִּזְבֵּחַ"
    # EN: "And the sons of Aaron, the priests, shall arrange the limbs, and the head, and the spinal column, upon the wood that is upon the fire, which is upon the altar."
    8: [
        ("וְעָרְכוּ", "וינצ'ד", "shall arrange"),
        ("בְּנֵי", "בני", "the sons of"),
        ("אַהֲרֹן", "הרון", "Aaron"),
        ("הַכֹּהֲנִים", "אלאיימה", "the priests"),
        ("אֵת הַנְּתָחִים", "אלאעצ'א", "the limbs"),
        ("אֶת-הָרֹאשׁ", "ואלראס", "and the head"),
        ("וְאֶת-הַפָּדֶר", "ואלקצבה", "and the spinal column"),
        ("עַל-הָעֵצִים", "עלי' אלחטב", "upon the wood"),
        ("אֲשֶׁר עַל-הָאֵשׁ", "אלד'י עלי' אלנאר", "that is upon the fire"),
        ("אֲשֶׁר עַל-הַמִּזְבֵּחַ", "אלד'י עלי' אלמד'בח", "which is upon the altar"),
    ],
    # JA: "וגופה ואכארעה יג'סלהא באלמא. ויקתר אלאמאם אלכל עלי' אלמד'בח. צעידה קרבאן מקבול מרצ'י ללה"
    # HE: "וְקִרְבּוֹ וּכְרָעָיו יִרְחַץ בַּמָּיִם וְהִקְטִיר הַכֹּהֵן אֶת-הַכֹּל הַמִּזְבֵּחָה עֹלָה אִשֵּׁה רֵיחַ-נִיחוֹחַ לַיהוָה"
    # EN: "Its innards and its legs shall he wash with water; and the priest shall burn the whole upon the altar — an ascent-offering, an acceptable and pleasing offering to God."
    9: [
        ("וְקִרְבּוֹ", "וגופה", "Its innards"),
        ("וּכְרָעָיו", "ואכארעה", "and its legs"),
        ("יִרְחַץ", "יג'סלהא", "shall he wash"),
        ("בַּמָּיִם", "באלמא", "with water"),
        ("הַכֹּהֵן", "אלאמאם", "and the priest"),
        ("וְהִקְטִיר", "ויקתר", "shall burn"),
        ("אֶת-הַכֹּל", "אלכל", "the whole"),
        ("הַמִּזְבֵּחָה", "עלי' אלמד'בח", "upon the altar"),
        ("עֹלָה", "צעידה", "an ascent-offering"),
        ("אִשֵּׁה רֵיחַ-נִיחוֹחַ", "קרבאן מקבול", "an acceptable"),
        ("לַיהוָה", "מרצ'י ללה", "and pleasing offering to God"),
    ],
    # JA: "ואן כאן קרבאנה מן אלג'נם. פמן אלצ'אן או מן אלמאעז צעידה פליקרבה ד'כרא צחיחא"
    # HE: "וְאִם-מִן-הַצֹּאן קָרְבָּנוֹ מִן-הַכְּשָׂבִים אוֹ מִן-הָעִזִּים לְעֹלָה--זָכָר תָּמִים יַקְרִיבֶנּוּ"
    # EN: "And if his offering is from the flock — from the sheep or from the goats — an ascent-offering, he shall bring it as a sound male."
    10: [
        ("וְאִם-מִן-הַצֹּאן", "ואן כאן קרבאנה מן אלג'נם", "And if his offering is from the flock"),
        ("מִן-הַכְּשָׂבִים", "פמן אלצ'אן", "from the sheep"),
        ("אוֹ", "או", "or"),
        ("מִן-הָעִזִּים", "מן אלמאעז", "from the goats"),
        ("לְעֹלָה", "צעידה", "an ascent-offering"),
        ("זָכָר", "פליקרבה ד'כרא", "he shall bring it as a"),
        ("תָּמִים יַקְרִיבֶנּוּ", "צחיחא", "sound male"),
    ],
    # JA: "ויד'בחה עלי' גאנב אלמד'בח. שמאלייא בין ידי אללה. וירש בני הרון אלאיימה דמה. עלי' אלמד'בח מסתדירא"
    # HE: "וְשָׁחַט אֹתוֹ עַל יֶרֶךְ הַמִּזְבֵּחַ צָפֹנָה--לִפְנֵי יְהוָה וְזָרְקוּ בְּנֵי אַהֲרֹן הַכֹּהֲנִים אֶת-דָּמוֹ עַל-הַמִּזְבֵּחַ--סָבִיב"
    # EN: "And he shall slaughter it on the side of the altar, northward, before God; and the sons of Aaron, the priests, shall sprinkle its blood upon the altar all around."
    11: [
        ("וְשָׁחַט", "ויד'בחה", "And he shall slaughter it"),
        ("עַל יֶרֶךְ הַמִּזְבֵּחַ", "עלי' גאנב אלמד'בח", "on the side of the altar"),
        ("צָפֹנָה", "שמאלייא", "northward"),
        ("לִפְנֵי", "בין ידי", "before"),
        ("יְהוָה", "אללה", "God"),
        ("וְזָרְקוּ", "וירש", "shall sprinkle"),
        ("בְּנֵי", "בני", "the sons of"),
        ("אַהֲרֹן", "הרון", "Aaron"),
        ("הַכֹּהֲנִים", "אלאיימה", "the priests"),
        ("אֶת-דָּמוֹ", "דמה", "its blood"),
        ("עַל-הַמִּזְבֵּחַ", "עלי' אלמד'בח", "upon the altar"),
        ("סָבִיב", "מסתדירא", "all around"),
    ],
    # JA: "ויעצ'יה אעצ'אא. וראסה וקצבתה. וינצ'דהא אלאמאם. עלי' אלחטב אלד'י עלי' אלנאר. אלד'י עלי' אלמד'בח"
    # HE: "וְנִתַּח אֹתוֹ לִנְתָחָיו וְאֶת-רֹאשׁוֹ וְאֶת-פִּדְרוֹ וְעָרַךְ הַכֹּהֵן אֹתָם עַל-הָעֵצִים אֲשֶׁר עַל-הָאֵשׁ אֲשֶׁר עַל-הַמִּזְבֵּחַ"
    # EN: "And he shall divide it into its limbs, and its head and its spinal column; and the priest shall arrange them upon the wood that is upon the fire, which is upon the altar."
    12: [
        ("וְנִתַּח", "ויעצ'יה", "And he shall divide it"),
        ("לִנְתָחָיו", "אעצ'אא", "into its limbs"),
        ("וְאֶת-רֹאשׁוֹ", "וראסה", "and its head"),
        ("וְאֶת-פִּדְרוֹ", "וקצבתה", "and its spinal column"),
        ("הַכֹּהֵן", "אלאמאם", "and the priest"),
        ("וְעָרַךְ", "וינצ'דהא", "shall arrange them"),
        ("עַל-הָעֵצִים", "עלי' אלחטב", "upon the wood"),
        ("אֲשֶׁר עַל-הָאֵשׁ", "אלד'י עלי' אלנאר", "that is upon the fire"),
        ("אֲשֶׁר עַל-הַמִּזְבֵּחַ", "אלד'י עלי' אלמד'בח", "which is upon the altar"),
    ],
    # JA: "ואלגוף ואלאכארע יג'סלהא באלמא. ויקדם אלאמאם אלכל ויקתרה עלי' אלמד'בח. הו צעידה. קרבאן מקבול מרצ'י ללה"
    # HE: "וְהַקֶּרֶב וְהַכְּרָעַיִם יִרְחַץ בַּמָּיִם וְהִקְרִיב הַכֹּהֵן אֶת-הַכֹּל וְהִקְטִיר הַמִּזְבֵּחָה--עֹלָה הוּא אִשֵּׁה רֵיחַ נִיחֹחַ לַיהוָה"
    # EN: "And the innards and the legs shall he wash with water; and the priest shall present the whole and burn it upon the altar — it is an ascent-offering, an acceptable and pleasing offering to God."
    13: [
        ("וְהַקֶּרֶב", "ואלגוף", "And the innards"),
        ("וְהַכְּרָעַיִם", "ואלאכארע", "and the legs"),
        ("יִרְחַץ", "יג'סלהא", "shall he wash"),
        ("בַּמָּיִם", "באלמא", "with water"),
        ("הַכֹּהֵן", "אלאמאם", "and the priest"),
        ("וְהִקְרִיב", "ויקדם", "shall present"),
        ("אֶת-הַכֹּל", "אלכל", "the whole"),
        ("וְהִקְטִיר", "ויקתרה", "and burn it"),
        ("הַמִּזְבֵּחָה", "עלי' אלמד'בח", "upon the altar"),
        ("עֹלָה הוּא", "הו צעידה", "it is an ascent-offering"),
        ("אִשֵּׁה רֵיחַ נִיחֹחַ", "קרבאן מקבול", "an acceptable"),
        ("לַיהוָה", "מרצ'י ללה", "and pleasing offering to God"),
    ],
    # JA: "ואן כאן קרבאנה מן אלטאיר צעידה ללה. פליקרבה מן אלשפאנין. או מן פראך' אלחמאם"
    # HE: "וְאִם מִן-הָעוֹף עֹלָה קָרְבָּנוֹ לַיהוָה וְהִקְרִיב מִן-הַתֹּרִים אוֹ מִן-בְּנֵי הַיּוֹנָה--אֶת-קָרְבָּנוֹ"
    # EN: "And if his offering to God is an ascent-offering from birds, he shall bring it from the turtledoves or from the young of the pigeons."
    14: [
        ("וְאִם", "ואן כאן", "And if"),
        ("קָרְבָּנוֹ", "קרבאנה", "his offering"),
        ("מִן-הָעוֹף", "מן אלטאיר", "from birds"),
        ("עֹלָה", "צעידה", "an ascent-offering"),
        ("לַיהוָה", "ללה", "to God"),
        ("וְהִקְרִיב", "פליקרבה", "he shall bring it"),
        ("מִן-הַתֹּרִים", "מן אלשפאנין", "from the turtledoves"),
        ("אוֹ", "או", "or"),
        ("מִן-בְּנֵי הַיּוֹנָה", "מן פראך' אלחמאם", "from the young of the pigeons"),
    ],
    # JA: "ויקדמה אלאמאם אלי' אלמד'בח. ויפצל ראסה. ת'ם יקתרה עלי' אלמד'בח. וימצ'י דמה. עלי' חאיט אלמד'בח"
    # HE: "וְהִקְרִיבוֹ הַכֹּהֵן אֶל-הַמִּזְבֵּחַ וּמָלַק אֶת-רֹאשׁוֹ וְהִקְטִיר הַמִּזְבֵּחָה וְנִמְצָה דָמוֹ עַל קִיר הַמִּזְבֵּחַ"
    # EN: "And the priest shall present it to the altar, and shall separate its head; then he shall burn it upon the altar, and its blood shall drain upon the wall of the altar."
    15: [
        ("הַכֹּהֵן", "אלאמאם", "And the priest"),
        ("וְהִקְרִיבוֹ", "ויקדמה", "shall present it"),
        ("אֶל-הַמִּזְבֵּחַ", "אלי' אלמד'בח", "to the altar"),
        ("וּמָלַק", "ויפצל", "and shall separate"),
        ("אֶת-רֹאשׁוֹ", "ראסה", "its head"),
        (None, "ת'ם", "then"),
        ("וְהִקְטִיר", "יקתרה", "he shall burn it"),
        ("הַמִּזְבֵּחָה", "עלי' אלמד'בח", "upon the altar"),
        ("דָמוֹ", "דמה", "and its blood"),
        ("וְנִמְצָה", "וימצ'י", "shall drain"),
        ("עַל קִיר הַמִּזְבֵּחַ", "עלי' חאיט אלמד'בח", "upon the wall of the altar"),
    ],
    # JA: "וינזע חוצלתה מע קאנצתה. ויטרחהא לזק אלמד'בח שרקייא. פי מוצ'ע מטרח אלרמאד"
    # HE: "וְהֵסִיר אֶת-מֻרְאָתוֹ בְּנֹצָתָהּ וְהִשְׁלִיךְ אֹתָהּ אֵצֶל הַמִּזְבֵּחַ קֵדְמָה--אֶל-מְקוֹם הַדָּשֶׁן"
    # EN: "And he shall remove its crop along with its gizzard, and shall throw them beside the altar on the east side, at the place where the ash is cast."
    16: [
        ("וְהֵסִיר", "וינזע", "And he shall remove"),
        ("אֶת-מֻרְאָתוֹ", "חוצלתה", "its crop"),
        ("בְּנֹצָתָהּ", "מע קאנצתה", "along with its gizzard"),
        ("וְהִשְׁלִיךְ", "ויטרחהא", "and shall throw them"),
        ("אֵצֶל הַמִּזְבֵּחַ", "לזק אלמד'בח", "beside the altar"),
        ("קֵדְמָה", "שרקייא", "on the east side"),
        ("אֶל-מְקוֹם הַדָּשֶׁן", "פי מוצ'ע מטרח אלרמאד", "at the place where the ash is cast"),
    ],
    # JA: "ויפצלה מן אגנחתה ולא יפרזה. ת'ם יקתרה אלאמאם עלי' אלמד'בח. עלי' אלחטב אלד'י עלי' אלנאר צעידה. קרבאן מקבול מרצ'י ללה"
    # HE: "וְשִׁסַּע אֹתוֹ בִכְנָפָיו לֹא יַבְדִּיל וְהִקְטִיר אֹתוֹ הַכֹּהֵן הַמִּזְבֵּחָה עַל-הָעֵצִים אֲשֶׁר עַל-הָאֵשׁ עֹלָה הוּא אִשֵּׁה רֵיחַ נִיחֹחַ--לַיהוָה"
    # EN: "And he shall split it open by its wings without severing it completely; then the priest shall burn it upon the altar, upon the wood that is upon the fire — an ascent-offering, an acceptable and pleasing offering to God."
    17: [
        ("וְשִׁסַּע", "ויפצלה", "And he shall split it open"),
        ("בִכְנָפָיו", "מן אגנחתה", "by its wings"),
        ("לֹא יַבְדִּיל", "ולא יפרזה", "without severing it completely"),
        (None, "ת'ם", "then"),
        ("וְהִקְטִיר", "יקתרה", "shall burn it"),
        ("הַכֹּהֵן", "אלאמאם", "the priest"),
        ("הַמִּזְבֵּחָה", "עלי' אלמד'בח", "upon the altar"),
        ("עַל-הָעֵצִים", "עלי' אלחטב", "upon the wood"),
        ("אֲשֶׁר עַל-הָאֵשׁ", "אלד'י עלי' אלנאר", "that is upon the fire"),
        ("עֹלָה", "צעידה", "an ascent-offering"),
        ("אִשֵּׁה רֵיחַ נִיחֹחַ", "קרבאן מקבול", "an acceptable"),
        ("לַיהוָה", "מרצ'י ללה", "and pleasing offering to God"),
    ],
}

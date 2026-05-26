"""Hand-authored word-level alignment triples for Bamidbar chapter 13."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: תם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "תם", "Then"),
        ("וַיְדַבֵּר", "כלם", "spoke"),
        ("יְהוָה", "אללה", "God"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "directly."),
    ],
    2: [
        # HE: שְׁלַח-לְךָ אֲנָשִׁים וְיָתֻרוּ אֶת-אֶרֶץ כְּנַעַן אֲשֶׁר-אֲנִי נֹתֵן לִבְנֵי יִשְׂרָאֵל אִישׁ אֶחָד אִישׁ אֶחָד לְמַטֵּה אֲבֹתָיו תִּשְׁלָחוּ--כֹּל נָשִׂיא בָהֶם
        # JA: אבעת' ברגאל. ירומון בלד כנעאן. אלד'י אנא מעטיה לבני אסראיל. רגל ואחד מן סבט אבאיה תבעת' בה. כל שריף מנהם
        # EN: Send forth men to scout the land of Canaan, which I am giving to the sons of Israel — one man from the tribe of their fathers you shall send with him, every noble among them.
        ("שְׁלַח-לְךָ", "אבעת'", "Send forth"),
        ("אֲנָשִׁים", "ברגאל", "men"),
        ("וְיָתֻרוּ", "ירומון", "to scout"),
        ("אֶת-אֶרֶץ", "בלד", "the land of"),
        ("כְּנַעַן", "כנעאן", "Canaan,"),
        ("אֲשֶׁר-אֲנִי", "אלד'י אנא", "which I"),
        ("נֹתֵן", "מעטיה", "am giving"),
        ("לִבְנֵי", "לבני", "to the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel —"),
        ("אִישׁ אֶחָד", "רגל ואחד", "one man"),
        ("לְמַטֵּה", "מן סבט", "from the tribe of"),
        ("אֲבֹתָיו", "אבאיה", "their fathers"),
        ("תִּשְׁלָחוּ", "תבעת' בה", "you shall send with him,"),
        ("כֹּל נָשִׂיא", "כל שריף", "every noble"),
        ("בָהֶם", "מנהם", "among them."),
    ],
    3: [
        # HE: וַיִּשְׁלַח אֹתָם מֹשֶׁה מִמִּדְבַּר פָּארָן עַל-פִּי יְהוָה כֻּלָּם אֲנָשִׁים רָאשֵׁי בְנֵי-יִשְׂרָאֵל הֵמָּה
        # JA: פבעת' בהם מוסי'. מן ברייה' פארן עלי' קול אללה. כלהם רגאל. ריסא בני אסראיל
        # EN: And Moses sent them forth from the wilderness of Paran, at the word of God; all of them men, heads of the sons of Israel.
        ("וַיִּשְׁלַח אֹתָם מֹשֶׁה", "פבעת' בהם מוסי'", "And Moses sent them forth"),
        ("מִמִּדְבַּר", "מן ברייה'", "from the wilderness of"),
        ("פָּארָן", "פארן", "Paran,"),
        ("עַל-פִּי", "עלי' קול", "at the word of"),
        ("יְהוָה", "אללה", "God;"),
        ("כֻּלָּם", "כלהם", "all of them"),
        ("אֲנָשִׁים", "רגאל", "men,"),
        ("רָאשֵׁי", "ריסא", "heads of"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel."),
    ],
    4: [
        # HE: וְאֵלֶּה שְׁמוֹתָם לְמַטֵּה רְאוּבֵן שַׁמּוּעַ בֶּן-זַכּוּר
        # JA: והד'ה אסמאיהם. מן סבט ראובן. שמוע אבן זכור
        # EN: And these are their names: from the tribe of Reuben — Shammua son of Zaccur.
        ("וְאֵלֶּה", "והד'ה", "And these are"),
        ("שְׁמוֹתָם", "אסמאיהם", "their names:"),
        ("לְמַטֵּה", "מן סבט", "from the tribe of"),
        ("רְאוּבֵן", "ראובן", "Reuben —"),
        ("שַׁמּוּעַ", "שמוע", "Shammua"),
        ("בֶּן-זַכּוּר", "אבן זכור", "son of Zaccur."),
    ],
    5: [
        # HE: לְמַטֵּה שִׁמְעוֹן שָׁפָט בֶּן-חוֹרִי
        # JA: ומן סבט שמעון. שפט אבן חורי
        # EN: And from the tribe of Simeon — Shaphat son of Hori.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("שִׁמְעוֹן", "שמעון", "Simeon —"),
        ("שָׁפָט", "שפט", "Shaphat"),
        ("בֶּן-חוֹרִי", "אבן חורי", "son of Hori."),
    ],
    6: [
        # HE: לְמַטֵּה יְהוּדָה כָּלֵב בֶּן-יְפֻנֶּה
        # JA: ומן סבט יהודה. כלב אבן יפונה
        # EN: And from the tribe of Judah — Caleb son of Jephunneh.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("יְהוּדָה", "יהודה", "Judah —"),
        ("כָּלֵב", "כלב", "Caleb"),
        ("בֶּן-יְפֻנֶּה", "אבן יפונה", "son of Jephunneh."),
    ],
    7: [
        # HE: לְמַטֵּה יִשָּׂשכָר יִגְאָל בֶּן-יוֹסֵף
        # JA: ומן סבט יששכר. יגאל אבן יוסף
        # EN: And from the tribe of Issachar — Igal son of Joseph.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("יִשָּׂשכָר", "יששכר", "Issachar —"),
        ("יִגְאָל", "יגאל", "Igal"),
        ("בֶּן-יוֹסֵף", "אבן יוסף", "son of Joseph."),
    ],
    8: [
        # HE: לְמַטֵּה אֶפְרָיִם הוֹשֵׁעַ בִּן-נוּן
        # JA: ומן סבט אפרים. הושע אבן נון
        # EN: And from the tribe of Ephraim — Hoshea son of Nun.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("אֶפְרָיִם", "אפרים", "Ephraim —"),
        ("הוֹשֵׁעַ", "הושע", "Hoshea"),
        ("בִּן-נוּן", "אבן נון", "son of Nun."),
    ],
    9: [
        # HE: לְמַטֵּה בִנְיָמִן פַּלְטִי בֶּן-רָפוּא
        # JA: ומן סבט בנימין. פלטי אבן רפוא
        # EN: And from the tribe of Benjamin — Palti son of Raphu.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("בִנְיָמִן", "בנימין", "Benjamin —"),
        ("פַּלְטִי", "פלטי", "Palti"),
        ("בֶּן-רָפוּא", "אבן רפוא", "son of Raphu."),
    ],
    10: [
        # HE: לְמַטֵּה זְבוּלֻן גַּדִּיאֵל בֶּן-סוֹדִי
        # JA: ומן סבט זבולון. גדיאל אבן סודי
        # EN: And from the tribe of Zebulun — Gaddiel son of Sodi.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("זְבוּלֻן", "זבולון", "Zebulun —"),
        ("גַּדִּיאֵל", "גדיאל", "Gaddiel"),
        ("בֶּן-סוֹדִי", "אבן סודי", "son of Sodi."),
    ],
    11: [
        # HE: לְמַטֵּה יוֹסֵף לְמַטֵּה מְנַשֶּׁה--גַּדִּי בֶּן-סוּסִי
        # JA: ומן סבט יוסף אלד'י הו סבט מנשה. גדי אבן סוסי
        # EN: And from the tribe of Joseph — which is the tribe of Manasseh — Gaddi son of Susi.
        ("לְמַטֵּה יוֹסֵף", "ומן סבט יוסף", "And from the tribe of Joseph —"),
        ("לְמַטֵּה מְנַשֶּׁה", "אלד'י הו סבט מנשה", "which is the tribe of Manasseh —"),
        ("גַּדִּי", "גדי", "Gaddi"),
        ("בֶּן-סוּסִי", "אבן סוסי", "son of Susi."),
    ],
    12: [
        # HE: לְמַטֵּה דָן עַמִּיאֵל בֶּן-גְּמַלִּי
        # JA: ומן סבט דן. עמיאל אבן גמלי
        # EN: And from the tribe of Dan — Ammiel son of Gemalli.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("דָן", "דן", "Dan —"),
        ("עַמִּיאֵל", "עמיאל", "Ammiel"),
        ("בֶּן-גְּמַלִּי", "אבן גמלי", "son of Gemalli."),
    ],
    13: [
        # HE: לְמַטֵּה אָשֵׁר סְתוּר בֶּן-מִיכָאֵל
        # JA: ומן סבט אשר. סתור אבן מיכאל
        # EN: And from the tribe of Asher — Sethur son of Michael.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("אָשֵׁר", "אשר", "Asher —"),
        ("סְתוּר", "סתור", "Sethur"),
        ("בֶּן-מִיכָאֵל", "אבן מיכאל", "son of Michael."),
    ],
    14: [
        # HE: לְמַטֵּה נַפְתָּלִי נַחְבִּי בֶּן-וָפְסִי
        # JA: ומן סבט נפתלי. נחבי אבן ופסי
        # EN: And from the tribe of Naphtali — Nahbi son of Vophsi.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("נַפְתָּלִי", "נפתלי", "Naphtali —"),
        ("נַחְבִּי", "נחבי", "Nahbi"),
        ("בֶּן-וָפְסִי", "אבן ופסי", "son of Vophsi."),
    ],
    15: [
        # HE: לְמַטֵּה גָד גְּאוּאֵל בֶּן-מָכִי
        # JA: ומן סבט גד. גאואל אבן מכי
        # EN: And from the tribe of Gad — Geuel son of Machi.
        ("לְמַטֵּה", "ומן סבט", "And from the tribe of"),
        ("גָד", "גד", "Gad —"),
        ("גְּאוּאֵל", "גאואל", "Geuel"),
        ("בֶּן-מָכִי", "אבן מכי", "son of Machi."),
    ],
    16: [
        # HE: אֵלֶּה שְׁמוֹת הָאֲנָשִׁים אֲשֶׁר-שָׁלַח מֹשֶׁה לָתוּר אֶת-הָאָרֶץ וַיִּקְרָא מֹשֶׁה לְהוֹשֵׁעַ בִּן-נוּן יְהוֹשֻׁעַ
        # JA: והד'א אסמא אלרגאל. אלד'י בעת' בהם מוסי' לירומו אלבלד. וסמא מוסי'. הושע אבן נון יהושע
        # EN: These are the names of the men whom Moses sent forth to scout the land. And Moses called Hoshea son of Nun — Joshua.
        ("אֵלֶּה", "והד'א", "These are"),
        ("שְׁמוֹת", "אסמא", "the names of"),
        ("הָאֲנָשִׁים", "אלרגאל", "the men"),
        ("אֲשֶׁר-שָׁלַח מֹשֶׁה", "אלד'י בעת' בהם מוסי'", "whom Moses sent forth"),
        ("לָתוּר", "לירומו", "to scout"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land."),
        ("וַיִּקְרָא מֹשֶׁה", "וסמא מוסי'", "And Moses called"),
        ("לְהוֹשֵׁעַ", "הושע", "Hoshea"),
        ("בִּן-נוּן", "אבן נון", "son of Nun —"),
        ("יְהוֹשֻׁעַ", "יהושע", "Joshua."),
    ],
    17: [
        # HE: וַיִּשְׁלַח אֹתָם מֹשֶׁה לָתוּר אֶת-אֶרֶץ כְּנָעַן וַיֹּאמֶר אֲלֵהֶם עֲלוּ זֶה בַּנֶּגֶב וַעֲלִיתֶם אֶת-הָהָר
        # JA: פבעת' בהם לירומו בלד כנעאן. וקאל להם. אצעדו אוולא אלי' אלדארום. תם אצעדו אלי' אלגבל
        # EN: And he sent them forth to scout the land of Canaan, and said to them: 'Go up first to the south, then go up to the mountain.'
        ("וַיִּשְׁלַח אֹתָם", "פבעת' בהם", "And he sent them forth"),
        ("לָתוּר", "לירומו", "to scout"),
        ("אֶת-אֶרֶץ", "בלד", "the land of"),
        ("כְּנָעַן", "כנעאן", "Canaan,"),
        ("וַיֹּאמֶר", "וקאל", "and said"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("עֲלוּ", "אצעדו", "'Go up"),
        ("זֶה בַּנֶּגֶב", "אוולא אלי' אלדארום", "first to the south,"),
        (None, "תם", "then"),
        ("וַעֲלִיתֶם", "אצעדו", "go up"),
        ("אֶת-הָהָר", "אלי' אלגבל", "to the mountain.'"),
    ],
    18: [
        # HE: וּרְאִיתֶם אֶת-הָאָרֶץ מַה-הִוא וְאֶת-הָעָם הַיֹּשֵׁב עָלֶיהָ--הֶחָזָק הוּא הֲרָפֶה הַמְעַט הוּא אִם-רָב
        # JA: ואנצ'רו אלבלד מא הי. ואלקום אלמקימין פיה. אהו שדיד אם מסתרכ'י. אקליל הו אם כת'יר
        # EN: 'And observe the land — what it is, and the people who dwell in it — whether it is strong or slack, whether it is few or many.'
        ("וּרְאִיתֶם", "ואנצ'רו", "'And observe"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land —"),
        ("מַה-הִוא", "מא הי", "what it is,"),
        ("וְאֶת-הָעָם", "ואלקום", "and the people"),
        ("הַיֹּשֵׁב", "אלמקימין", "who dwell"),
        ("עָלֶיהָ", "פיה", "in it —"),
        ("הֶחָזָק הוּא", "אהו שדיד", "whether it is strong"),
        ("הֲרָפֶה", "אם מסתרכ'י", "or slack,"),
        ("הַמְעַט הוּא", "אקליל הו", "whether it is few"),
        ("אִם-רָב", "אם כת'יר", "or many.'"),
    ],
    19: [
        # HE: וּמָה הָאָרֶץ אֲשֶׁר-הוּא יֹשֵׁב בָּהּ--הֲטוֹבָה הִוא אִם-רָעָה וּמָה הֶעָרִים אֲשֶׁר-הוּא יוֹשֵׁב בָּהֵנָּה--הַבְּמַחֲנִים אִם בְּמִבְצָרִים
        # JA: ומא אלארץ'. אלד'י הו סאכנהא. אגיידה הי אם רדייה. ומא אלקרא. אלד'י הו סאכנהא. אפי ארבאץ' או פי חצון
        # EN: 'And what is the land in which it dwells — whether it is good or poor; and what are the towns in which it dwells — whether they are in open encampments or in fortresses.'
        ("וּמָה הָאָרֶץ", "ומא אלארץ'", "'And what is the land"),
        ("אֲשֶׁר-הוּא יֹשֵׁב בָּהּ", "אלד'י הו סאכנהא", "in which it dwells —"),
        ("הֲטוֹבָה הִוא", "אגיידה הי", "whether it is good"),
        ("אִם-רָעָה", "אם רדייה", "or poor;"),
        ("וּמָה הֶעָרִים", "ומא אלקרא", "and what are the towns"),
        ("אֲשֶׁר-הוּא יוֹשֵׁב בָּהֵנָּה", "אלד'י הו סאכנהא", "in which it dwells —"),
        ("הַבְּמַחֲנִים", "אפי ארבאץ'", "whether they are in open encampments"),
        ("אִם בְּמִבְצָרִים", "או פי חצון", "or in fortresses.'"),
    ],
    20: [
        # HE: וּמָה הָאָרֶץ הַשְּׁמֵנָה הִוא אִם-רָזָה הֲיֵשׁ-בָּהּ עֵץ אִם-אַיִן וְהִתְחַזַּקְתֶּם וּלְקַחְתֶּם מִפְּרִי הָאָרֶץ וְהַיָּמִים--יְמֵי בִּכּוּרֵי עֲנָבִים
        # JA: ומא הייה' אלארץ' . אהי סמינה אם הזלא. והל פיהא שגר מג'רוס אם לא. ותשדדו. וכ'דו מן ת'מרהא. והד'א אלפצל. אייאם בכור אלענב
        # EN: 'And what is the land — whether it is fat or lean, and whether there are planted trees in it or not. And be courageous, and take of its fruit.' And behold, this season was the days of the first-ripening of the grapes.
        ("וּמָה הָאָרֶץ", "ומא הייה' אלארץ'", "'And what is the land —"),
        ("הַשְּׁמֵנָה הִוא", "אהי סמינה", "whether it is fat"),
        ("אִם-רָזָה", "אם הזלא", "or lean,"),
        ("הֲיֵשׁ-בָּהּ", "והל פיהא", "and whether there are"),
        ("עֵץ", "שגר מג'רוס", "planted trees"),
        ("אִם-אַיִן", "אם לא", "in it or not."),
        ("וְהִתְחַזַּקְתֶּם", "ותשדדו", "And be courageous,"),
        ("וּלְקַחְתֶּם", "וכ'דו", "and take"),
        ("מִפְּרִי הָאָרֶץ", "מן ת'מרהא", "of its fruit.'"),
        (None, "והד'א", "And behold,"),
        ("וְהַיָּמִים", "אלפצל", "this season was"),
        ("יְמֵי בִּכּוּרֵי", "אייאם בכור", "the days of the first-ripening of"),
        ("עֲנָבִים", "אלענב", "the grapes."),
    ],
    21: [
        # HE: וַיַּעֲלוּ וַיָּתֻרוּ אֶת-הָאָרֶץ מִמִּדְבַּר-צִן עַד-רְחֹב לְבֹא חֲמָת
        # JA: פצעדו וראמו אלבלד. מן ברייה' צין אלי' רחוב אלי' חמאה
        # EN: And they went up and scouted the land, from the wilderness of Zin to Rehob, toward Hamath.
        ("וַיַּעֲלוּ", "פצעדו", "And they went up"),
        ("וַיָּתֻרוּ", "וראמו", "and scouted"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land,"),
        ("מִמִּדְבַּר-צִן", "מן ברייה' צין", "from the wilderness of Zin"),
        ("עַד-רְחֹב", "אלי' רחוב", "to Rehob,"),
        ("לְבֹא חֲמָת", "אלי' חמאה", "toward Hamath."),
    ],
    22: [
        # HE: וַיַּעֲלוּ בַנֶּגֶב וַיָּבֹא עַד-חֶבְרוֹן וְשָׁם אֲחִימַן שֵׁשַׁי וְתַלְמַי יְלִידֵי הָעֲנָק וְחֶבְרוֹן שֶׁבַע שָׁנִים נִבְנְתָה לִפְנֵי צֹעַן מִצְרָיִם
        # JA: פצעדו אוולי' אלי' אלדארום וגאו אלי' חברא. ות'ם אחימן ששי ותלמי. בני אלגבאברה. וכאנת חברא קד בנית קבל צאן מנבר מצר בסבע סנין
        # EN: And they went up first to the south, and came to Hebron; and there were Ahiman, Sheshai, and Talmai — the children of the giants. And Hebron had already been built before Zoan, the seat of Egypt, by seven years.
        ("וַיַּעֲלוּ", "פצעדו", "And they went up"),
        ("בַנֶּגֶב", "אוולי' אלי' אלדארום", "first to the south,"),
        ("וַיָּבֹא", "וגאו", "and came"),
        ("עַד-חֶבְרוֹן", "אלי' חברא", "to Hebron;"),
        (None, "ות'ם", "and there were"),
        ("אֲחִימַן", "אחימן", "Ahiman,"),
        ("שֵׁשַׁי", "ששי", "Sheshai,"),
        ("וְתַלְמַי", "ותלמי", "and Talmai —"),
        ("יְלִידֵי הָעֲנָק", "בני אלגבאברה", "the children of the giants."),
        ("וְחֶבְרוֹן", "וכאנת חברא", "And Hebron"),
        (None, "קד", "had already been"),
        ("נִבְנְתָה", "בנית", "built"),
        ("לִפְנֵי", "קבל", "before"),
        ("צֹעַן", "צאן", "Zoan,"),
        ("מִצְרָיִם", "מנבר מצר", "the seat of Egypt,"),
        ("שֶׁבַע שָׁנִים", "בסבע סנין", "by seven years."),
    ],
    23: [
        # HE: וַיָּבֹאוּ עַד-נַחַל אֶשְׁכֹּל וַיִּכְרְתוּ מִשָּׁם זְמוֹרָה וְאֶשְׁכּוֹל עֲנָבִים אֶחָד וַיִּשָּׂאֻהוּ בַמּוֹט בִּשְׁנָיִם וּמִן-הָרִמֹּנִים וּמִן-הַתְּאֵנִים
        # JA: וגאו אלי' ואד אלענקוד. פקטעו מן ת'ם חבלה וענקוד ענב ואחד. וחמלוה פי אלדהק פי מא בין את'נין. ומן אלרמאן ומן אלתין
        # EN: And they came to the Valley of the Cluster, and cut from there a branch and one cluster of grapes, and carried it on a pole between two; and also some of the pomegranates and of the figs.
        ("וַיָּבֹאוּ", "וגאו", "And they came"),
        ("עַד-נַחַל", "אלי' ואד", "to the Valley of"),
        ("אֶשְׁכֹּל", "אלענקוד", "the Cluster,"),
        ("וַיִּכְרְתוּ", "פקטעו", "and cut"),
        ("מִשָּׁם", "מן ת'ם", "from there"),
        ("זְמוֹרָה", "חבלה", "a branch"),
        ("וְאֶשְׁכּוֹל עֲנָבִים אֶחָד", "וענקוד ענב ואחד", "and one cluster of grapes,"),
        ("וַיִּשָּׂאֻהוּ", "וחמלוה", "and carried it"),
        ("בַמּוֹט", "פי אלדהק", "on a pole"),
        ("בִּשְׁנָיִם", "פי מא בין את'נין", "between two;"),
        ("וּמִן-הָרִמֹּנִים", "ומן אלרמאן", "and also some of the pomegranates"),
        ("וּמִן-הַתְּאֵנִים", "ומן אלתין", "and of the figs."),
    ],
    24: [
        # HE: לַמָּקוֹם הַהוּא קָרָא נַחַל אֶשְׁכּוֹל עַל אֹדוֹת הָאֶשְׁכּוֹל אֲשֶׁר-כָּרְתוּ מִשָּׁם בְּנֵי יִשְׂרָאֵל
        # JA: פלד'אלך סמי אלמוצ'ע ואד אלענקוד. בסבב אלענקוד. אלד'י קטעו מנה בני אסראיל
        # EN: Therefore that place was named the Valley of the Cluster, on account of the cluster which the sons of Israel cut from there.
        ("לַמָּקוֹם הַהוּא", "פלד'אלך", "Therefore"),
        ("קָרָא", "סמי", "that place was named"),
        ("נַחַל אֶשְׁכּוֹל", "אלמוצ'ע ואד אלענקוד", "the Valley of the Cluster,"),
        ("עַל אֹדוֹת", "בסבב", "on account of"),
        ("הָאֶשְׁכּוֹל", "אלענקוד", "the cluster"),
        ("אֲשֶׁר-כָּרְתוּ", "אלד'י קטעו מנה", "which the sons of Israel cut"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "from there."),
    ],
    25: [
        # HE: וַיָּשֻׁבוּ מִתּוּר הָאָרֶץ מִקֵּץ אַרְבָּעִים יוֹם
        # JA: פרגעו מן ריאם אלבלד. בעד ארבעין יומא
        # EN: And they returned from scouting the land, after forty days.
        ("וַיָּשֻׁבוּ", "פרגעו", "And they returned"),
        ("מִתּוּר", "מן ריאם", "from scouting"),
        ("הָאָרֶץ", "אלבלד", "the land,"),
        ("מִקֵּץ", "בעד", "after"),
        ("אַרְבָּעִים יוֹם", "ארבעין יומא", "forty days."),
    ],
    26: [
        # HE: וַיֵּלְכוּ וַיָּבֹאוּ אֶל-מֹשֶׁה וְאֶל-אַהֲרֹן וְאֶל-כָּל-עֲדַת בְּנֵי-יִשְׂרָאֵל אֶל-מִדְבַּר פָּארָן--קָדֵשָׁה וַיָּשִׁיבוּ אֹתָם דָּבָר וְאֶת-כָּל-הָעֵדָה וַיַּרְאוּם אֶת-פְּרִי הָאָרֶץ
        # JA: פסארו חתא גאו אלי' מוסי' והרון. וסאיר גמאעה' בני אסראיל. אלי' ברייה' פארן אלי' רקים. פאגאבוהם באלכ'בר וסאיר אלגמאעה. ואורוהם ת'מר אלארץ'
        # EN: And they journeyed until they came to Moses and Aaron, and the rest of the congregation of the sons of Israel, to the wilderness of Paran, to Kadesh; and they answered them with the report — them and the rest of the congregation — and showed them the fruit of the land.
        ("וַיֵּלְכוּ", "פסארו", "And they journeyed"),
        ("וַיָּבֹאוּ", "חתא גאו", "until they came"),
        ("אֶל-מֹשֶׁה", "אלי' מוסי'", "to Moses"),
        ("וְאֶל-אַהֲרֹן", "והרון", "and Aaron,"),
        ("וְאֶל-כָּל-עֲדַת", "וסאיר גמאעה'", "and the rest of the congregation of"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("אֶל-מִדְבַּר פָּארָן", "אלי' ברייה' פארן", "to the wilderness of Paran,"),
        ("קָדֵשָׁה", "אלי' רקים", "to Kadesh;"),
        ("וַיָּשִׁיבוּ אֹתָם", "פאגאבוהם", "and they answered them"),
        ("דָּבָר", "באלכ'בר", "with the report —"),
        (None, "וסאיר אלגמאעה", "them and the rest of the congregation —"),
        ("וַיַּרְאוּם", "ואורוהם", "and showed them"),
        ("אֶת-פְּרִי הָאָרֶץ", "ת'מר אלארץ'", "the fruit of the land."),
    ],
    27: [
        # HE: וַיְסַפְּרוּ-לוֹ וַיֹּאמְרוּ בָּאנוּ אֶל-הָאָרֶץ אֲשֶׁר שְׁלַחְתָּנוּ וְגַם זָבַת חָלָב וּדְבַשׁ הִוא--וְזֶה-פִּרְיָהּ
        # JA: פקצו עליה וקאלו. צרנא אלי' אלבלד אלד'י בעת'ת בנא. וחקא אנה יפיץ' אללבן ואלעסל. והד'א ת'מרה
        # EN: And they recounted to him, and said: 'We went to the land to which you sent us, and indeed it flows with milk and honey — and here is its fruit.'
        ("וַיְסַפְּרוּ-לוֹ", "פקצו עליה", "And they recounted to him,"),
        ("וַיֹּאמְרוּ", "וקאלו", "and said:"),
        ("בָּאנוּ", "צרנא", "'We went"),
        ("אֶל-הָאָרֶץ", "אלי' אלבלד", "to the land"),
        ("אֲשֶׁר שְׁלַחְתָּנוּ", "אלד'י בעת'ת בנא", "to which you sent us,"),
        ("וְגַם", "וחקא", "and indeed"),
        ("זָבַת חָלָב", "אנה יפיץ' אללבן", "it flows with milk"),
        ("וּדְבַשׁ", "ואלעסל", "and honey —"),
        ("וְזֶה-פִּרְיָהּ", "והד'א ת'מרה", "and here is its fruit.'"),
    ],
    28: [
        # HE: אֶפֶס כִּי-עַז הָעָם הַיֹּשֵׁב בָּאָרֶץ וְהֶעָרִים בְּצֻרוֹת גְּדֹלֹת מְאֹד וְגַם-יְלִדֵי הָעֲנָק רָאִינוּ שָׁם
        # JA: כלא אן אלקום אלמקימין פיה עזיזין. ואלקרא. חצינה עצימה גדא. ואיצ'א אולאד אלגבאברה ראינאהם תם
        # EN: 'However, the people who dwell in it are mighty, and the towns are very greatly fortified; and moreover, the children of the giants — we saw them there.'
        ("אֶפֶס כִּי-עַז", "כלא אן אלקום אלמקימין פיה עזיזין", "'However, the people who dwell in it are mighty,"),
        ("וְהֶעָרִים", "ואלקרא", "and the towns"),
        ("בְּצֻרוֹת גְּדֹלֹת מְאֹד", "חצינה עצימה גדא", "are very greatly fortified;"),
        ("וְגַם-יְלִדֵי הָעֲנָק", "ואיצ'א אולאד אלגבאברה", "and moreover, the children of the giants —"),
        ("רָאִינוּ", "ראינאהם", "we saw them"),
        ("שָׁם", "תם", "there.'"),
    ],
    29: [
        # HE: עֲמָלֵק יוֹשֵׁב בְּאֶרֶץ הַנֶּגֶב וְהַחִתִּי וְהַיְבוּסִי וְהָאֱמֹרִי יוֹשֵׁב בָּהָר וְהַכְּנַעֲנִי יוֹשֵׁב עַל-הַיָּם וְעַל יַד הַיַּרְדֵּן
        # JA: אלעמאלקה מקימין פי בלד אלדארום. ואלחתיין. ואליבוסיין ואלאמוריין מקימין פי אלגבל. ואלכנאעניין מקימין עלי' אלבחר. ועלי שאט אלארדון
        # EN: 'The Amalekites dwell in the land of the south; and the Hittites and the Jebusites and the Amorites dwell in the mountain; and the Canaanites dwell by the sea and along the bank of the Jordan.'
        ("עֲמָלֵק", "אלעמאלקה", "'The Amalekites"),
        ("יוֹשֵׁב", "מקימין", "dwell"),
        ("בְּאֶרֶץ הַנֶּגֶב", "פי בלד אלדארום", "in the land of the south;"),
        ("וְהַחִתִּי", "ואלחתיין", "and the Hittites"),
        ("וְהַיְבוּסִי", "ואליבוסיין", "and the Jebusites"),
        ("וְהָאֱמֹרִי", "ואלאמוריין", "and the Amorites"),
        ("יוֹשֵׁב בָּהָר", "מקימין פי אלגבל", "dwell in the mountain;"),
        ("וְהַכְּנַעֲנִי", "ואלכנאעניין", "and the Canaanites"),
        ("יוֹשֵׁב עַל-הַיָּם", "מקימין עלי' אלבחר", "dwell by the sea"),
        ("וְעַל יַד הַיַּרְדֵּן", "ועלי שאט אלארדון", "and along the bank of the Jordan.'"),
    ],
    30: [
        # HE: וַיַּהַס כָּלֵב אֶת-הָעָם אֶל-מֹשֶׁה וַיֹּאמֶר עָלֹה נַעֲלֶה וְיָרַשְׁנוּ אֹתָהּ--כִּי-יָכוֹל נוּכַל לָהּ
        # JA: פאסכת כלב אלקום אלי' קול מוסי'. וקאל. בל נצעד צעודא ונחוזה. פאנא נטיקהם
        # EN: And Caleb silenced the people toward what Moses had said, and said: 'Nay, we shall go up and seize it — for we are able to overcome them!'
        ("וַיַּהַס", "פאסכת", "And Caleb"),
        ("כָּלֵב", "כלב", "silenced"),
        ("אֶת-הָעָם", "אלקום", "the people"),
        ("אֶל-מֹשֶׁה", "אלי' קול מוסי'", "toward what Moses had said,"),
        ("וַיֹּאמֶר", "וקאל", "and said:"),
        (None, "בל", "'Nay,"),
        ("עָלֹה נַעֲלֶה", "נצעד צעודא", "we shall go up"),
        ("וְיָרַשְׁנוּ אֹתָהּ", "ונחוזה", "and seize it —"),
        ("כִּי-יָכוֹל נוּכַל לָהּ", "פאנא נטיקהם", "for we are able to overcome them!'"),
    ],
    31: [
        # HE: וְהָאֲנָשִׁים אֲשֶׁר-עָלוּ עִמּוֹ אָמְרוּ לֹא נוּכַל לַעֲלוֹת אֶל-הָעָם כִּי-חָזָק הוּא מִמֶּנּוּ
        # JA: ואלקום אלד'ין מצ'ו מעה קאלו. לא נטיק אן נצעד אלי' אלקום. לאנהם אשד מנא
        # EN: But the men who had gone with him said: 'We are not able to go up to the people, for they are stronger than us.'
        ("וְהָאֲנָשִׁים", "ואלקום", "But the men"),
        ("אֲשֶׁר-עָלוּ", "אלד'ין מצ'ו", "who had gone"),
        ("עִמּוֹ", "מעה", "with him"),
        ("אָמְרוּ", "קאלו", "said:"),
        ("לֹא נוּכַל", "לא נטיק", "'We are not able"),
        ("לַעֲלוֹת", "אן נצעד", "to go up"),
        ("אֶל-הָעָם", "אלי' אלקום", "to the people,"),
        ("כִּי-חָזָק הוּא", "לאנהם אשד", "for they are stronger"),
        ("מִמֶּנּוּ", "מנא", "than us.'"),
    ],
    32: [
        # HE: וַיֹּצִיאוּ דִּבַּת הָאָרֶץ אֲשֶׁר תָּרוּ אֹתָהּ אֶל-בְּנֵי יִשְׂרָאֵל לֵאמֹר הָאָרֶץ אֲשֶׁר עָבַרְנוּ בָהּ לָתוּר אֹתָהּ אֶרֶץ אֹכֶלֶת יוֹשְׁבֶיהָ הִוא וְכָל-הָעָם אֲשֶׁר-רָאִינוּ בְתוֹכָהּ אַנְשֵׁי מִדּוֹת
        # JA: ואכ'רגו שנאעה רדייה. עלי' אלבלד אלד'י ראמוה. לבני אסראיל וקאלו. אלבלד אלד'י מררנא פיה לנרומה. הו בלד יהלך אהלה. וגמיע אלקום. אלד'י ראינאהם פיה ד'וי מסאחה
        # EN: And they spread an evil slander against the land which they had scouted, to the sons of Israel, saying: 'The land through which we passed to scout it is a land that destroys its inhabitants; and all the people whom we saw in it are of great stature.'
        ("וַיֹּצִיאוּ", "ואכ'רגו", "And they spread"),
        ("דִּבַּת הָאָרֶץ", "שנאעה רדייה", "an evil slander"),
        ("אֲשֶׁר תָּרוּ אֹתָהּ", "עלי' אלבלד אלד'י ראמוה", "against the land which they had scouted,"),
        ("אֶל-בְּנֵי יִשְׂרָאֵל", "לבני אסראיל", "to the sons of Israel,"),
        ("לֵאמֹר", "וקאלו", "saying:"),
        ("הָאָרֶץ", "אלבלד", "'The land"),
        ("אֲשֶׁר עָבַרְנוּ בָהּ", "אלד'י מררנא פיה", "through which we passed"),
        ("לָתוּר אֹתָהּ", "לנרומה", "to scout it"),
        ("אֶרֶץ אֹכֶלֶת יוֹשְׁבֶיהָ", "הו בלד יהלך אהלה", "is a land that destroys its inhabitants;"),
        ("וְכָל-הָעָם", "וגמיע אלקום", "and all the people"),
        ("אֲשֶׁר-רָאִינוּ בְתוֹכָהּ", "אלד'י ראינאהם פיה", "whom we saw in it"),
        ("אַנְשֵׁי מִדּוֹת", "ד'וי מסאחה", "are of great stature.'"),
    ],
    33: [
        # HE: וְשָׁם רָאִינוּ אֶת-הַנְּפִילִים בְּנֵי עֲנָק--מִן-הַנְּפִלִים וַנְּהִי בְעֵינֵינוּ כַּחֲגָבִים וְכֵן הָיִינוּ בְּעֵינֵיהֶם
        # JA: וראינא ת'ם אלעלוג. בני אלגבאברה מן עלוגהם. וצרנא פי עיוננא כאלגראד. וכד'אך כנא פי עיונהם
        # EN: 'And we saw there the brutes — children of the giants from among their brutes — and we were in our own eyes as locusts; and so were we in their eyes.'
        ("וְשָׁם רָאִינוּ", "וראינא ת'ם", "'And we saw there"),
        ("אֶת-הַנְּפִילִים", "אלעלוג", "the brutes —"),
        ("בְּנֵי עֲנָק", "בני אלגבאברה", "children of the giants"),
        ("מִן-הַנְּפִלִים", "מן עלוגהם", "from among their brutes —"),
        ("וַנְּהִי", "וצרנא", "and we were"),
        ("בְעֵינֵינוּ", "פי עיוננא", "in our own eyes"),
        ("כַּחֲגָבִים", "כאלגראד", "as locusts;"),
        ("וְכֵן", "וכד'אך", "and so"),
        ("הָיִינוּ", "כנא", "were we"),
        ("בְּעֵינֵיהֶם", "פי עיונהם", "in their eyes.'"),
    ],
}

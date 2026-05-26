"""Hand-authored word-level alignment triples for Bamidbar chapter 9."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה בְמִדְבַּר-סִינַי בַּשָּׁנָה הַשֵּׁנִית לְצֵאתָם מֵאֶרֶץ מִצְרַיִם בַּחֹדֶשׁ הָרִאשׁוֹן--לֵאמֹר
        # JA: וקבל ד'אלך כלם אללה מוסי' פי ברייה' סיני. פי אלסנה אלתאניה. לכ'רוגהם מן בלד מצר. פי אלשהר אלאוול קאילא
        # EN: And before that, God spoke to Moses in the wilderness of Sinai, in the second year of their departure from the land of Egypt, in the first month, saying:
        (None, "וקבל ד'אלך", "And before that,"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי'", "in the wilderness of"),
        ("בְמִדְבַּר-סִינַי", "פי ברייה' סיני", "Sinai,"),
        ("בַּשָּׁנָה הַשֵּׁנִית", "פי אלסנה אלתאניה", "in the second year"),
        ("לְצֵאתָם", "לכ'רוגהם", "of their departure"),
        ("מֵאֶרֶץ מִצְרַיִם", "מן בלד מצר", "from the land of Egypt,"),
        ("בַּחֹדֶשׁ הָרִאשׁוֹן", "פי אלשהר אלאוול", "in the first month,"),
        ("לֵאמֹר", "קאילא", "saying:"),
    ],
    2: [
        # HE: וְיַעֲשׂוּ בְנֵי-יִשְׂרָאֵל אֶת-הַפָּסַח בְּמוֹעֲדוֹ
        # JA: ויצנעו בני אסראיל. אלפסח פי וקתה
        # EN: "Let the sons of Israel perform the Passover at its appointed time."
        ("וְיַעֲשׂוּ", "ויצנעו", "perform"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("אֶת-הַפָּסַח", "אלפסח", "the Passover"),
        ("בְּמוֹעֲדוֹ", "פי וקתה", "at its appointed time."),
    ],
    3: [
        # HE: בְּאַרְבָּעָה עָשָׂר-יוֹם בַּחֹדֶשׁ הַזֶּה בֵּין הָעַרְבַּיִם תַּעֲשׂוּ אֹתוֹ--בְּמֹעֲדוֹ כְּכָל-חֻקֹּתָיו וּכְכָל-מִשְׁפָּטָיו תַּעֲשׂוּ אֹתוֹ
        # JA: פי אליום אלראבע עשר. מן הד'א אלשהר. בין אלג'רובין. תצנעוה פי וקתה. כגמיע רסומה ואחכאמה תצנעוה
        # EN: "On the fourteenth day of this month, between the two sunsets, you shall perform it at its appointed time; according to all its statutes and ordinances you shall perform it."
        ("בְּאַרְבָּעָה עָשָׂר-יוֹם", "פי אליום אלראבע עשר", "On the fourteenth day"),
        ("בַּחֹדֶשׁ הַזֶּה", "מן הד'א אלשהר", "of this month,"),
        ("בֵּין הָעַרְבַּיִם", "בין אלג'רובין", "between the two sunsets,"),
        ("תַּעֲשׂוּ אֹתוֹ", "תצנעוה", "you shall perform it"),
        ("בְּמֹעֲדוֹ", "פי וקתה", "at its appointed time;"),
        ("כְּכָל-חֻקֹּתָיו", "כגמיע רסומה", "according to all its statutes"),
        ("וּכְכָל-מִשְׁפָּטָיו", "ואחכאמה", "and ordinances"),
        (None, "תצנעוה", "you shall perform it."),
    ],
    4: [
        # HE: וַיְדַבֵּר מֹשֶׁה אֶל-בְּנֵי יִשְׂרָאֵל לַעֲשֹׂת הַפָּסַח
        # JA: פכלם מוסי' בני אסראיל פי עמל אלפסח
        # EN: And Moses spoke to the sons of Israel concerning the performance of the Passover.
        ("וַיְדַבֵּר", "פכלם", "And Moses spoke"),
        ("מֹשֶׁה", "מוסי'", "to the sons of"),
        ("אֶל-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "Israel"),
        ("לַעֲשֹׂת", "פי עמל", "concerning the performance of"),
        ("הַפָּסַח", "אלפסח", "the Passover."),
    ],
    5: [
        # HE: וַיַּעֲשׂוּ אֶת-הַפֶּסַח בָּרִאשׁוֹן בְּאַרְבָּעָה עָשָׂר יוֹם לַחֹדֶשׁ בֵּין הָעַרְבַּיִם--בְּמִדְבַּר סִינָי כְּכֹל אֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה--כֵּן עָשׂוּ בְּנֵי יִשְׂרָאֵל
        # JA: פעמלוה פי אלשהר אלאוול. פי אליום אלראבע עשר מנה. בין אלג'רובין פי ברייה' סיני. כגמיע מא אמר אללה מוסי'. כד'אך צנעו בני אסראיל
        # EN: And they performed it in the first month, on the fourteenth day of it, between the two sunsets, in the wilderness of Sinai — according to all that God had commanded Moses; so did the sons of Israel.
        ("וַיַּעֲשׂוּ אֶת-הַפֶּסַח", "פעמלוה", "And they performed it"),
        ("בָּרִאשׁוֹן", "פי אלשהר אלאוול", "in the first month,"),
        ("בְּאַרְבָּעָה עָשָׂר יוֹם לַחֹדֶשׁ", "פי אליום אלראבע עשר מנה", "on the fourteenth day of it,"),
        ("בֵּין הָעַרְבַּיִם", "בין אלג'רובין", "between the two sunsets,"),
        ("בְּמִדְבַּר סִינָי", "פי ברייה' סיני", "in the wilderness of Sinai —"),
        ("כְּכֹל אֲשֶׁר צִוָּה יְהוָה", "כגמיע מא אמר אללה", "according to all that God had commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses;"),
        ("כֵּן עָשׂוּ", "כד'אך צנעו", "so did"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel."),
    ],
    6: [
        # HE: וַיְהִי אֲנָשִׁים אֲשֶׁר הָיוּ טְמֵאִים לְנֶפֶשׁ אָדָם וְלֹא-יָכְלוּ לַעֲשֹׂת-הַפֶּסַח בַּיּוֹם הַהוּא וַיִּקְרְבוּ לִפְנֵי מֹשֶׁה וְלִפְנֵי אַהֲרֹן--בַּיּוֹם הַהוּא
        # JA: פכאן פיהם אנאס. תנגסו במיית מן אלנאס. פלם יגוז להם אן יעמלו אלפסח פי ד'אלך אליום. פתקדמו פיה. בין ידי מוסי' והרון
        # EN: And there were among them people who had become impure from a dead person, and it was not permitted for them to perform the Passover on that day; so they came forward regarding it, before Moses and Aaron.
        ("וַיְהִי", "פכאן", "And there were"),
        ("אֲנָשִׁים", "פיהם אנאס", "among them people"),
        ("אֲשֶׁר הָיוּ טְמֵאִים", "תנגסו", "who had become impure"),
        ("לְנֶפֶשׁ אָדָם", "במיית מן אלנאס", "from a dead person,"),
        ("וְלֹא-יָכְלוּ", "פלם יגוז להם", "and it was not permitted for them"),
        ("לַעֲשֹׂת-הַפֶּסַח", "אן יעמלו אלפסח", "to perform the Passover"),
        ("בַּיּוֹם הַהוּא", "פי ד'אלך אליום", "on that day;"),
        ("וַיִּקְרְבוּ", "פתקדמו פיה", "so they came forward regarding it,"),
        ("לִפְנֵי מֹשֶׁה", "בין ידי מוסי'", "before Moses"),
        ("וְלִפְנֵי אַהֲרֹן", "והרון", "and Aaron."),
    ],
    7: [
        # HE: וַיֹּאמְרוּ הָאֲנָשִׁים הָהֵמָּה אֵלָיו אֲנַחְנוּ טְמֵאִים לְנֶפֶשׁ אָדָם לָמָּה נִגָּרַע לְבִלְתִּי הַקְרִיב אֶת-קָרְבַּן יְהוָה בְּמֹעֲדוֹ בְּתוֹךְ בְּנֵי יִשְׂרָאֵל
        # JA: וקאלו. נחן אנגאס מן מיית מן אלנאס. פלם נמנע. מן אן נקרב מת'ל קרבאן אללה פי וקתה. פי מא בין בני אסראיל
        # EN: And they said: "We are impure from a dead person — why then should we be prevented from bringing the offering of God at its appointed time, among the sons of Israel?"
        ("וַיֹּאמְרוּ", "וקאלו", "And they said:"),
        ("אֲנַחְנוּ טְמֵאִים", "נחן אנגאס", "We are impure"),
        ("לְנֶפֶשׁ אָדָם", "מן מיית מן אלנאס", "from a dead person —"),
        ("לָמָּה נִגָּרַע", "פלם נמנע", "why then should we be prevented"),
        ("לְבִלְתִּי הַקְרִיב", "מן אן נקרב", "from bringing"),
        ("אֶת-קָרְבַּן יְהוָה", "מת'ל קרבאן אללה", "the offering of God"),
        ("בְּמֹעֲדוֹ", "פי וקתה", "at its appointed time,"),
        ("בְּתוֹךְ בְּנֵי יִשְׂרָאֵל", "פי מא בין בני אסראיל", "among the sons of Israel?"),
    ],
    8: [
        # HE: וַיֹּאמֶר אֲלֵהֶם מֹשֶׁה עִמְדוּ וְאֶשְׁמְעָה מַה-יְצַוֶּה יְהוָה לָכֶם
        # JA: פקאל להם מוסי'. קפו חתא אסמע. מא יאמר אללה פיכם
        # EN: And Moses said to them: "Wait, until I hear what God will command concerning you."
        ("וַיֹּאמֶר", "פקאל", "And Moses said"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("מֹשֶׁה", "מוסי'", "Wait,"),
        ("עִמְדוּ", "קפו", "until"),
        ("וְאֶשְׁמְעָה", "חתא אסמע", "I hear"),
        ("מַה-יְצַוֶּה יְהוָה", "מא יאמר אללה", "what God will command"),
        ("לָכֶם", "פיכם", "concerning you."),
    ],
    9: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "spoke"),
        ("יְהוָה", "אללה", "God"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "directly."),
    ],
    10: [
        # HE: דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל לֵאמֹר אִישׁ אִישׁ כִּי-יִהְיֶה-טָמֵא לָנֶפֶשׁ אוֹ בְדֶרֶךְ רְחֹקָה לָכֶם אוֹ לְדֹרֹתֵיכֶם וְעָשָׂה פֶסַח לַיהוָה
        # JA: מר בני אסראיל קאילא. אי אנסאן כאן נגס מן מיית. או פי ספר מנכם. או מן אגיאלכם. פיצנע פסחא ללה
        # EN: "Command the sons of Israel, saying: Any person who has been impure from a dead person, or is on a journey from among you, or from your generations — let him perform a Passover for God.
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("לֵאמֹר", "קאילא", "saying:"),
        ("אִישׁ אִישׁ", "אי אנסאן", "Any person"),
        ("כִּי-יִהְיֶה-טָמֵא לָנֶפֶשׁ", "כאן נגס מן מיית", "who has been impure from a dead person,"),
        ("אוֹ בְדֶרֶךְ רְחֹקָה", "או פי ספר מנכם", "or is on a journey from among you,"),
        ("אוֹ לְדֹרֹתֵיכֶם", "או מן אגיאלכם", "or from your generations —"),
        ("וְעָשָׂה פֶסַח", "פיצנע פסחא", "let him perform a Passover"),
        ("לַיהוָה", "ללה", "for God."),
    ],
    11: [
        # HE: בַּחֹדֶשׁ הַשֵּׁנִי בְּאַרְבָּעָה עָשָׂר יוֹם בֵּין הָעַרְבַּיִם--יַעֲשׂוּ אֹתוֹ עַל-מַצּוֹת וּמְרֹרִים יֹאכְלֻהוּ
        # JA: פי אלשהר אלת'אני. פי אליום אלראבע עשר מנה. בין אלג'רובין אצנעוה פי וקתה. מע פטיר ומראר יאכלונה
        # EN: In the second month, on the fourteenth day of it, between the two sunsets, perform it at its appointed time; with unleavened bread and bitter herbs they shall eat it.
        ("בַּחֹדֶשׁ הַשֵּׁנִי", "פי אלשהר אלת'אני", "In the second month,"),
        ("בְּאַרְבָּעָה עָשָׂר יוֹם", "פי אליום אלראבע עשר מנה", "on the fourteenth day of it,"),
        ("בֵּין הָעַרְבַּיִם", "בין אלג'רובין", "between the two sunsets,"),
        ("יַעֲשׂוּ אֹתוֹ", "אצנעוה", "perform it"),
        ("עַל-מַצּוֹת", "פי וקתה. מע פטיר", "at its appointed time; with unleavened bread"),
        ("וּמְרֹרִים", "ומראר", "and bitter herbs"),
        ("יֹאכְלֻהוּ", "יאכלונה", "they shall eat it."),
    ],
    12: [
        # HE: לֹא-יַשְׁאִירוּ מִמֶּנּוּ עַד-בֹּקֶר וְעֶצֶם לֹא יִשְׁבְּרוּ-בוֹ כְּכָל-חֻקַּת הַפֶּסַח יַעֲשׂוּ אֹתוֹ
        # JA: לא יבקו מנה אלי' אלג'דאה. ולא יכסרו מנה עצ'מא. וכסאיר רסום אלפסח יצנעוה
        # EN: They shall leave none of it until the morning, nor shall they break a bone of it; and according to the rest of the statutes of the Passover they shall perform it.
        ("לֹא-יַשְׁאִירוּ", "לא יבקו", "They shall leave none of it"),
        ("מִמֶּנּוּ עַד-בֹּקֶר", "מנה אלי' אלג'דאה", "until the morning,"),
        ("וְעֶצֶם לֹא יִשְׁבְּרוּ-בוֹ", "ולא יכסרו מנה עצ'מא", "nor shall they break a bone of it;"),
        ("כְּכָל-חֻקַּת הַפֶּסַח", "וכסאיר רסום אלפסח", "and according to the rest of the statutes of the Passover"),
        ("יַעֲשׂוּ אֹתוֹ", "יצנעוה", "they shall perform it."),
    ],
    13: [
        # HE: וְהָאִישׁ אֲשֶׁר-הוּא טָהוֹר וּבְדֶרֶךְ לֹא-הָיָה וְחָדַל לַעֲשׂוֹת הַפָּסַח--וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא מֵעַמֶּיהָ כִּי קָרְבַּן יְהוָה לֹא הִקְרִיב בְּמֹעֲדוֹ--חֶטְאוֹ יִשָּׂא הָאִישׁ הַהוּא
        # JA: ואי רגל כאן טאהר ולם יכון פי ספר. ואמתנע אן יעמל אלפסח. פינקטע ד'אלך אלאנסאן מן בין קומה. אד' לם יקרב קרבאן אללה פי וקתה. פקד חמל ד'אלך אלרגל וזרה
        # EN: But any man who is pure and was not on a journey, and refrained from performing the Passover — that person shall be cut off from among his people, since he did not bring the offering of God at its appointed time; that man has borne his guilt.
        ("וְהָאִישׁ", "ואי רגל", "But any man"),
        ("אֲשֶׁר-הוּא טָהוֹר", "כאן טאהר", "who is pure"),
        ("וּבְדֶרֶךְ לֹא-הָיָה", "ולם יכון פי ספר", "and was not on a journey,"),
        ("וְחָדַל לַעֲשׂוֹת הַפֶּסַח", "ואמתנע אן יעמל אלפסח", "and refrained from performing the Passover —"),
        ("וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא", "פינקטע ד'אלך אלאנסאן", "that person shall be cut off"),
        ("מֵעַמֶּיהָ", "מן בין קומה", "from among his people,"),
        ("כִּי קָרְבַּן יְהוָה לֹא הִקְרִיב", "אד' לם יקרב קרבאן אללה", "since he did not bring the offering of God"),
        ("בְּמֹעֲדוֹ", "פי וקתה", "at its appointed time;"),
        ("חֶטְאוֹ יִשָּׂא", "פקד חמל ד'אלך אלרגל וזרה", "that man has borne his guilt."),
    ],
    14: [
        # HE: וְכִי-יָגוּר אִתְּכֶם גֵּר וְעָשָׂה פֶסַח לַיהוָה--כְּחֻקַּת הַפֶּסַח וּכְמִשְׁפָּטוֹ כֵּן יַעֲשֶׂה חֻקָּה אַחַת יִהְיֶה לָכֶם וְלַגֵּר וּלְאֶזְרַח הָאָרֶץ
        # JA: ואן דכ'ל פיכם דכ'יל. פליצנע פסחא ללה. כרסם אלפסח וחכמה כד'אך יצנע. אד' שריעה ואחדה תכון לכם. לאלדכ'יל וצריח אלאמה
        # EN: And if a stranger enters among you, let him perform a Passover for God; according to the statute of the Passover and its ordinance, so shall he perform it — for one law shall there be for you, for the stranger and for the native-born of the nation."
        ("וְכִי-יָגוּר אִתְּכֶם גֵּר", "ואן דכ'ל פיכם דכ'יל", "And if a stranger enters among you,"),
        ("וְעָשָׂה פֶסַח", "פליצנע פסחא", "let him perform a Passover"),
        ("לַיהוָה", "ללה", "for God;"),
        ("כְּחֻקַּת הַפֶּסַח", "כרסם אלפסח", "according to the statute of the Passover"),
        ("וּכְמִשְׁפָּטוֹ", "וחכמה", "and its ordinance,"),
        ("כֵּן יַעֲשֶׂה", "כד'אך יצנע", "so shall he perform it —"),
        ("חֻקָּה אַחַת יִהְיֶה לָכֶם", "אד' שריעה ואחדה תכון לכם", "for one law shall there be for you,"),
        ("וְלַגֵּר", "לאלדכ'יל", "for the stranger"),
        ("וּלְאֶזְרַח הָאָרֶץ", "וצריח אלאמה", "and for the native-born of the nation."),
    ],
    15: [
        # HE: וּבְיוֹם הָקִים אֶת-הַמִּשְׁכָּן כִּסָּה הֶעָנָן אֶת-הַמִּשְׁכָּן לְאֹהֶל הָעֵדֻת וּבָעֶרֶב יִהְיֶה עַל-הַמִּשְׁכָּן כְּמַרְאֵה-אֵשׁ--עַד-בֹּקֶר
        # JA: ומן יום נצב אלמסכן גטאה אלג'מאם עלי' כ'בא אלשהאדה. ובאלליל יכון עליה. כרויא נאר אלי' אלג'דאה
        # EN: And on the day of the erection of the tabernacle, the cloud covered it — over the tent of testimony; and at night it would be upon it, like the appearance of fire until the morning.
        ("וּבְיוֹם הָקִים", "ומן יום נצב", "And on the day of the erection of"),
        ("אֶת-הַמִּשְׁכָּן", "אלמסכן", "the tabernacle,"),
        ("כִּסָּה הֶעָנָן", "גטאה אלג'מאם", "the cloud covered it —"),
        ("לְאֹהֶל הָעֵדֻת", "עלי' כ'בא אלשהאדה", "over the tent of testimony;"),
        ("וּבָעֶרֶב", "ובאלליל", "and at night"),
        ("יִהְיֶה עַל-הַמִּשְׁכָּן", "יכון עליה", "it would be upon it,"),
        ("כְּמַרְאֵה-אֵשׁ", "כרויא נאר", "like the appearance of fire"),
        ("עַד-בֹּקֶר", "אלי' אלג'דאה", "until the morning."),
    ],
    16: [
        # HE: כֵּן יִהְיֶה תָמִיד הֶעָנָן יְכַסֶּנּוּ וּמַרְאֵה-אֵשׁ לָיְלָה
        # JA: כד'אך יכון דאימא. אלג'מאם יג'טיה נהארא. ורויא אלנאר לילא
        # EN: So it would be continually: the cloud covering it by day, and the appearance of fire by night.
        (None, "כד'אך", "So"),
        ("כֵּן יִהְיֶה", "יכון", "it would be"),
        ("תָמִיד", "דאימא", "continually:"),
        ("הֶעָנָן יְכַסֶּנּוּ", "אלג'מאם יג'טיה", "the cloud covering it"),
        (None, "נהארא", "by day,"),
        ("וּמַרְאֵה-אֵשׁ", "ורויא אלנאר", "and the appearance of fire"),
        ("לָיְלָה", "לילא", "by night."),
    ],
    17: [
        # HE: וּלְפִי הֵעָלוֹת הֶעָנָן מֵעַל הָאֹהֶל--וְאַחֲרֵי כֵן יִסְעוּ בְּנֵי יִשְׂרָאֵל וּבִמְקוֹם אֲשֶׁר יִשְׁכָּן-שָׁם הֶעָנָן--שָׁם יַחֲנוּ בְּנֵי יִשְׂרָאֵל
        # JA: ועלי' קדר ארתפאע אלג'מאם ען אלכ'בא. פבעד ד'אלך ירחלון בני אסראיל. ופי מוצ'ע יסכן פיה אלג'מאם. ת'ם ינזלון בני אסראיל
        # EN: And according to the lifting of the cloud from upon the tent, after that the sons of Israel would set out; and in the place where the cloud would settle, there the sons of Israel would encamp.
        ("וּלְפִי הֵעָלוֹת הֶעָנָן", "ועלי' קדר ארתפאע אלג'מאם", "And according to the lifting of the cloud"),
        ("מֵעַל הָאֹהֶל", "ען אלכ'בא", "from upon the tent,"),
        ("וְאַחֲרֵי כֵן", "פבעד ד'אלך", "after that"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("יִסְעוּ", "ירחלון", "would set out;"),
        ("וּבִמְקוֹם אֲשֶׁר יִשְׁכָּן-שָׁם הֶעָנָן", "ופי מוצ'ע יסכן פיה אלג'מאם", "and in the place where the cloud would settle,"),
        ("שָׁם יַחֲנוּ", "ת'ם", "there"),
        ("בְּנֵי יִשְׂרָאֵל", "ינזלון בני אסראיל", "the sons of Israel would encamp."),
    ],
    18: [
        # HE: עַל-פִּי יְהוָה יִסְעוּ בְּנֵי יִשְׂרָאֵל וְעַל-פִּי יְהוָה יַחֲנוּ כָּל-יְמֵי אֲשֶׁר יִשְׁכֹּן הֶעָנָן עַל-הַמִּשְׁכָּן--יַחֲנוּ
        # JA: עלי' קול אללה. ירחל בני אסראיל. ועלי' קולה ינזלון. פהם טול מדה' מא יסכן אלג'מאם. עלי' אלמסכן מקימין
        # EN: At the word of God the sons of Israel would set out, and at His word they would encamp; all the duration of the time that the cloud dwelt upon the tabernacle, they remained encamped.
        ("עַל-פִּי יְהוָה", "עלי' קול אללה", "At the word of God"),
        ("יִסְעוּ", "ירחל", "would set out,"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("וְעַל-פִּי יְהוָה", "ועלי' קולה", "and at His word"),
        ("יַחֲנוּ", "ינזלון", "they would encamp;"),
        ("כָּל-יְמֵי", "פהם טול מדה'", "all the duration of the time"),
        ("אֲשֶׁר יִשְׁכֹּן הֶעָנָן", "מא יסכן אלג'מאם", "that the cloud dwelt"),
        ("עַל-הַמִּשְׁכָּן", "עלי' אלמסכן", "upon the tabernacle,"),
        (None, "מקימין", "they remained encamped."),
    ],
    19: [
        # HE: וּבְהַאֲרִיךְ הֶעָנָן עַל-הַמִּשְׁכָּן יָמִים רַבִּים--וְשָׁמְרוּ בְנֵי-יִשְׂרָאֵל אֶת-מִשְׁמֶרֶת יְהוָה וְלֹא יִסָּעוּ
        # JA: ואן טאל אלג'מאם. אייאמא כת'ירה עלי' אלמסכן. פיחפץ' בני אסראיל. חפץ' אללה ולא ירחלון
        # EN: And if the cloud lingered many days upon the tabernacle, the sons of Israel would observe the charge of God and not set out.
        ("וּבְהַאֲרִיךְ הֶעָנָן", "ואן טאל אלג'מאם", "And if the cloud lingered"),
        ("יָמִים רַבִּים", "אייאמא כת'ירה", "many days"),
        ("עַל-הַמִּשְׁכָּן", "עלי' אלמסכן", "upon the tabernacle,"),
        ("וְשָׁמְרוּ", "פיחפץ'", "would observe"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("אֶת-מִשְׁמֶרֶת יְהוָה", "חפץ' אללה", "the charge of God"),
        ("וְלֹא יִסָּעוּ", "ולא ירחלון", "and not set out."),
    ],
    20: [
        # HE: וְיֵשׁ אֲשֶׁר יִהְיֶה הֶעָנָן יָמִים מִסְפָּר--עַל-הַמִּשְׁכָּן עַל-פִּי יְהוָה יַחֲנוּ וְעַל-פִּי יְהוָה יִסָּעוּ
        # JA: ורבמא כאן אלג'מאם אייאמא מחצאה עלי' אלמסכן. פהם עלי' קול אללה ינזלו ועלי' קולה ירחלון
        # EN: And sometimes the cloud was upon the tabernacle for a number of countable days; they would encamp at the word of God, and at His word they would set out.
        ("וְיֵשׁ אֲשֶׁר יִהְיֶה הֶעָנָן", "ורבמא כאן אלג'מאם", "And sometimes the cloud was"),
        ("עַל-הַמִּשְׁכָּן", "עלי' אלמסכן", "upon the tabernacle"),
        ("יָמִים מִסְפָּר", "אייאמא מחצאה", "for a number of countable days;"),
        ("עַל-פִּי יְהוָה יַחֲנוּ", "פהם עלי' קול אללה ינזלו", "they would encamp at the word of God,"),
        ("וְעַל-פִּי יְהוָה יִסָּעוּ", "ועלי' קולה ירחלון", "and at His word they would set out."),
    ],
    21: [
        # HE: וְיֵשׁ אֲשֶׁר-יִהְיֶה הֶעָנָן מֵעֶרֶב עַד-בֹּקֶר וְנַעֲלָה הֶעָנָן בַּבֹּקֶר וְנָסָעוּ אוֹ יוֹמָם וָלַיְלָה וְנַעֲלָה הֶעָנָן וְנָסָעוּ
        # JA: ורבמא כאן אלג'מאם מן אלמסא אלי' אלצבאח. ת'ם ירתפע באלג'דאה וירחלון. או נהארא ולילא. ת'ם ירתפע וירחלון
        # EN: And sometimes the cloud was from evening until morning; then it would lift at daybreak and they would set out. Or a day and a night — then it would lift and they would set out.
        ("וְיֵשׁ אֲשֶׁר-יִהְיֶה הֶעָנָן", "ורבמא כאן אלג'מאם", "And sometimes the cloud was"),
        ("מֵעֶרֶב", "מן אלמסא", "from evening"),
        ("עַד-בֹּקֶר", "אלי' אלצבאח", "until morning;"),
        (None, "ת'ם", "then"),
        ("וְנַעֲלָה הֶעָנָן", "ירתפע", "it would lift"),
        ("בַּבֹּקֶר", "באלג'דאה", "at daybreak"),
        ("וְנָסָעוּ", "וירחלון", "and they would set out."),
        ("אוֹ יוֹמָם", "או נהארא", "Or a day"),
        ("וָלַיְלָה", "ולילא", "and a night —"),
        (None, "ת'ם", "then"),
        (None, "ירתפע", "it would lift"),
        (None, "וירחלון", "and they would set out."),
    ],
    22: [
        # HE: אוֹ-יֹמַיִם אוֹ-חֹדֶשׁ אוֹ-יָמִים בְּהַאֲרִיךְ הֶעָנָן עַל-הַמִּשְׁכָּן לִשְׁכֹּן עָלָיו יַחֲנוּ בְנֵי-יִשְׂרָאֵל וְלֹא יִסָּעוּ וּבְהֵעָלֹתוֹ יִסָּעוּ
        # JA: או יומין או שהרא או חולא. אד'א טאלת מדה' אלג'מאם עלי' אלמסכן ליסכן עליה. בני אסראיל מקימין ג'יר ראחלין. ופי ארתפאעה ירחלון
        # EN: Or two days, or a month, or a full year: whenever the duration of the cloud upon the tabernacle was prolonged, to dwell upon it — the sons of Israel remained encamped and did not set out; and at its lifting they would set out.
        ("אוֹ-יֹמַיִם", "או יומין", "Or two days,"),
        ("אוֹ-חֹדֶשׁ", "או שהרא", "or a month,"),
        ("אוֹ-יָמִים", "או חולא", "or a full year:"),
        ("בְּהַאֲרִיךְ הֶעָנָן עַל-הַמִּשְׁכָּן", "אד'א טאלת מדה' אלג'מאם עלי' אלמסכן", "whenever the duration of the cloud upon the tabernacle was prolonged,"),
        ("לִשְׁכֹּן עָלָיו", "ליסכן עליה", "to dwell upon it —"),
        ("יַחֲנוּ בְנֵי-יִשְׂרָאֵל", "בני אסראיל מקימין", "the sons of Israel remained encamped"),
        ("וְלֹא יִסָּעוּ", "ג'יר ראחלין", "and did not set out;"),
        ("וּבְהֵעָלֹתוֹ יִסָּעוּ", "ופי ארתפאעה ירחלון", "and at its lifting they would set out."),
    ],
    23: [
        # HE: עַל-פִּי יְהוָה יַחֲנוּ וְעַל-פִּי יְהוָה יִסָּעוּ אֶת-מִשְׁמֶרֶת יְהוָה שָׁמָרוּ עַל-פִּי יְהוָה בְּיַד-מֹשֶׁה
        # JA: כד'אך עלי' קול אללה ינזלון. ועלי קולה ירחלון. ויחפצון מא אסתחפצ'הם. מן קולה ביד מוסי'
        # EN: So at the word of God they would encamp, and at His word they would set out; and they kept what He had entrusted to them to keep, of His word, by the hand of Moses.
        (None, "כד'אך", "So"),
        ("עַל-פִּי יְהוָה יַחֲנוּ", "עלי' קול אללה ינזלון", "at the word of God they would encamp,"),
        ("וְעַל-פִּי יְהוָה יִסָּעוּ", "ועלי קולה ירחלון", "and at His word they would set out;"),
        ("אֶת-מִשְׁמֶרֶת יְהוָה שָׁמָרוּ", "ויחפצון מא אסתחפצ'הם", "and they kept what He had entrusted to them to keep,"),
        ("עַל-פִּי יְהוָה", "מן קולה", "of His word,"),
        ("בְּיַד-מֹשֶׁה", "ביד מוסי'", "by the hand of Moses."),
    ],
}

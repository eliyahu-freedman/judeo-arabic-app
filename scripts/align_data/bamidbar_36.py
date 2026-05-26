"""Hand-authored word-level alignment triples for Bamidbar chapter 36."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיִּקְרְבוּ רָאשֵׁי הָאָבוֹת לְמִשְׁפַּחַת בְּנֵי-גִלְעָד בֶּן-מָכִיר בֶּן-מְנַשֶּׁה--מִמִּשְׁפְּחֹת בְּנֵי יוֹסֵף וַיְדַבְּרוּ לִפְנֵי מֹשֶׁה וְלִפְנֵי הַנְּשִׂאִים--רָאשֵׁי אָבוֹת לִבְנֵי יִשְׂרָאֵל
        # JA: ת'ם תקדם. רויסא אבא עשירה' בני גלעד אבן מכיר אבן מנשה. מן עשאיר בני יוסף. וקאלו בין ידי מוסי' ואלאשראף. רויסא אבא בני אסראיל
        # EN: Then the heads of the fathers of the clan of the sons of Gilead son of Makir son of Manasseh, from the clans of the sons of Joseph, came forward and spoke before Moses and the nobles — the heads of the fathers of the sons of Israel.
        (None, "ת'ם", "Then"),
        ("וַיִּקְרְבוּ", "תקדם", "came forward"),
        ("רָאשֵׁי הָאָבוֹת", "רויסא אבא", "the heads of the fathers of"),
        ("לְמִשְׁפַּחַת", "עשירה'", "the clan of"),
        ("בְּנֵי-גִלְעָד", "בני גלעד", "the sons of Gilead"),
        ("בֶּן-מָכִיר", "אבן מכיר", "son of Makir"),
        ("בֶּן-מְנַשֶּׁה", "אבן מנשה", "son of Manasseh,"),
        ("מִמִּשְׁפְּחֹת", "מן עשאיר", "from the clans of"),
        ("בְּנֵי יוֹסֵף", "בני יוסף", "the sons of Joseph,"),
        ("וַיְדַבְּרוּ", "וקאלו", "and spoke"),
        ("לִפְנֵי מֹשֶׁה", "בין ידי מוסי'", "before Moses"),
        ("וְלִפְנֵי הַנְּשִׂאִים", "ואלאשראף", "and the nobles —"),
        ("רָאשֵׁי אָבוֹת", "רויסא אבא", "the heads of the fathers of"),
        ("לִבְנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel."),
    ],
    2: [
        # HE: וַיֹּאמְרוּ אֶת-אֲדֹנִי צִוָּה יְהוָה לָתֵת אֶת-הָאָרֶץ בְּנַחֲלָה בְּגוֹרָל לִבְנֵי יִשְׂרָאֵל וַאדֹנִי צֻוָּה בַיהוָה לָתֵת אֶת-נַחֲלַת צְלָפְחָד אָחִינוּ לִבְנֹתָיו
        # JA: ננוקאלו . אן אללה אמר סיידנא. באן יעטא אלבלד נחלה. באסהם לבני אסראיל. ואמרה איצ'א. באן ידפע נחלה' צלפחד אכ'ינא אלי' בנאתה
        # EN: And they said: 'God commanded our lord to give the land as an inheritance by equal portions to the sons of Israel; and He also commanded him to transfer the inheritance of Zelophehad our brother to his daughters.
        ("וַיֹּאמְרוּ", "ננוקאלו", "And they said:"),
        ("אֶת-אֲדֹנִי", "סיידנא", "our lord"),
        ("צִוָּה יְהוָה", "אן אללה אמר", "'God commanded"),
        ("לָתֵת", "באן יעטא", "to give"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land"),
        ("בְּנַחֲלָה", "נחלה", "as an inheritance"),
        ("בְּגוֹרָל", "באסהם", "by equal portions"),
        ("לִבְנֵי יִשְׂרָאֵל", "לבני אסראיל", "to the sons of Israel;"),
        ("וַאדֹנִי צֻוָּה", "ואמרה איצ'א", "and He also commanded him"),
        ("לָתֵת אֶת-נַחֲלַת", "באן ידפע נחלה'", "to transfer the inheritance of"),
        ("צְלָפְחָד", "צלפחד", "Zelophehad"),
        ("אָחִינוּ", "אכ'ינא", "our brother"),
        ("לִבְנֹתָיו", "אלי' בנאתה", "to his daughters."),
    ],
    3: [
        # HE: וְהָיוּ לְאֶחָד מִבְּנֵי שִׁבְטֵי בְנֵי-יִשְׂרָאֵל לְנָשִׁים וְנִגְרְעָה נַחֲלָתָן מִנַּחֲלַת אֲבֹתֵינוּ וְנוֹסַף עַל נַחֲלַת הַמַּטֶּה אֲשֶׁר תִּהְיֶינָה לָהֶם וּמִגֹּרַל נַחֲלָתֵנוּ יִגָּרֵעַ
        # JA: פנכ'אף אן יצרן נסאא. לואחד מן אסבאט בני אסראיל. פתנקץ חצתהן מן נחלה' אבאינא. ותזאד עלי' חצה' אלסבט. אלד'י יתזווגן מנה. ויכון סהם נחלתנא מנקוצא
        # EN: And we fear that they may become wives of one from the other tribes of the sons of Israel, so that their portion will be diminished from the inheritance of our fathers, and will be added to the portion of the tribe into which they marry — and the allotted share of our inheritance shall be reduced.
        (None, "פנכ'אף", "And we fear"),
        ("וְהָיוּ", "אן יצרן נסאא", "that they may become wives"),
        ("לְאֶחָד", "לואחד", "of one"),
        ("מִבְּנֵי שִׁבְטֵי", "מן אסבאט", "from the other tribes of"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("וְנִגְרְעָה נַחֲלָתָן", "פתנקץ חצתהן", "so that their portion will be diminished"),
        ("מִנַּחֲלַת אֲבֹתֵינוּ", "מן נחלה' אבאינא", "from the inheritance of our fathers,"),
        ("וְנוֹסַף", "ותזאד", "and will be added"),
        ("עַל נַחֲלַת הַמַּטֶּה", "עלי' חצה' אלסבט", "to the portion of the tribe"),
        ("אֲשֶׁר תִּהְיֶינָה לָהֶם", "אלד'י יתזווגן מנה", "into which they marry —"),
        ("וּמִגֹּרַל נַחֲלָתֵנוּ יִגָּרֵעַ", "ויכון סהם נחלתנא מנקוצא", "and the allotted share of our inheritance shall be reduced."),
    ],
    4: [
        # HE: וְאִם-יִהְיֶה הַיֹּבֵל לִבְנֵי יִשְׂרָאֵל וְנוֹסְפָה נַחֲלָתָן עַל נַחֲלַת הַמַּטֶּה אֲשֶׁר תִּהְיֶינָה לָהֶם וּמִנַּחֲלַת מַטֵּה אֲבֹתֵינוּ יִגָּרַע נַחֲלָתָן
        # JA: ולו חתי יואפי סנה' אלאטלאק לבני אסראיל. לבקית חצתהן מזאדה. עלי' חצה' אלסבט. אלד'י יתזווגן מנה. ונאקצה מן חצתנא
        # EN: And even when the year of release comes for the sons of Israel, their portion will remain added to the portion of the tribe into which they marry, and diminished from our portion.'
        (None, "ולו", "And even when"),
        ("וְאִם-יִהְיֶה הַיֹּבֵל", "חתי יואפי סנה' אלאטלאק", "the year of release comes"),
        ("לִבְנֵי יִשְׂרָאֵל", "לבני אסראיל", "for the sons of Israel,"),
        ("וְנוֹסְפָה נַחֲלָתָן", "לבקית חצתהן מזאדה", "their portion will remain added"),
        ("עַל נַחֲלַת הַמַּטֶּה", "עלי' חצה' אלסבט", "to the portion of the tribe"),
        ("אֲשֶׁר תִּהְיֶינָה לָהֶם", "אלד'י יתזווגן מנה", "into which they marry,"),
        ("וּמִנַּחֲלַת מַטֵּה אֲבֹתֵינוּ יִגָּרַע נַחֲלָתָן", "ונאקצה מן חצתנא", "and diminished from our portion.'"),
    ],
    5: [
        # HE: וַיְצַו מֹשֶׁה אֶת-בְּנֵי יִשְׂרָאֵל עַל-פִּי יְהוָה לֵאמֹר כֵּן מַטֵּה בְנֵי-יוֹסֵף דֹּבְרִים
        # JA: פאמר מוסי' בני אסראיל. ען קול אללה קאילא. נעמא קאל סבט ולד יוסף
        # EN: And Moses gave an order to the sons of Israel, according to the word of God, saying: 'The tribe of the sons of Joseph speaks rightly.
        ("וַיְצַו מֹשֶׁה", "פאמר מוסי'", "And Moses gave an order"),
        ("אֶת-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "to the sons of Israel,"),
        ("עַל-פִּי יְהוָה", "ען קול אללה", "according to the word of God,"),
        ("לֵאמֹר", "קאילא", "saying:"),
        ("כֵּן", "נעמא", "'The tribe of"),
        ("מַטֵּה בְנֵי-יוֹסֵף דֹּבְרִים", "קאל סבט ולד יוסף", "the sons of Joseph speaks rightly."),
    ],
    6: [
        # HE: זֶה הַדָּבָר אֲשֶׁר-צִוָּה יְהוָה לִבְנוֹת צְלָפְחָד לֵאמֹר לַטּוֹב בְּעֵינֵיהֶם תִּהְיֶינָה לְנָשִׁים אַךְ לְמִשְׁפַּחַת מַטֵּה אֲבִיהֶם--תִּהְיֶינָה לְנָשִׁים
        # JA: הד'א אלאמר אלד'י אמר אללה. פי חכם בנאת צלפחד. אן יתזווגן למן חסן ענדהן. לכן יכון מן עשירה' סבט אביהן
        # EN: This is the matter which God has commanded concerning the case of the daughters of Zelophehad: let them marry whomever seems good to them, but they shall be from the clan of the tribe of their father.
        ("זֶה הַדָּבָר", "הד'א אלאמר", "This is the matter"),
        ("אֲשֶׁר-צִוָּה יְהוָה", "אלד'י אמר אללה", "which God has commanded"),
        ("לִבְנוֹת צְלָפְחָד", "פי חכם בנאת צלפחד", "concerning the case of the daughters of Zelophehad:"),
        ("לַטּוֹב בְּעֵינֵיהֶם", "אן יתזווגן למן חסן ענדהן", "let them marry whomever seems good to them,"),
        ("אַךְ", "לכן", "but"),
        ("לְמִשְׁפַּחַת", "יכון מן עשירה'", "they shall be from the clan of"),
        ("מַטֵּה אֲבִיהֶם", "סבט אביהן", "the tribe of their father."),
    ],
    7: [
        # HE: וְלֹא-תִסֹּב נַחֲלָה לִבְנֵי יִשְׂרָאֵל מִמַּטֶּה אֶל-מַטֶּה כִּי אִישׁ בְּנַחֲלַת מַטֵּה אֲבֹתָיו יִדְבְּקוּ בְּנֵי יִשְׂרָאֵל
        # JA: חתי' לא תדור הד'ה אלנחלה לבני אסראיל. מן סבט אלי' סבט . אלא ילזם כל סבט מנהם נחלה אבאיה
        # EN: So that this inheritance shall not pass among the sons of Israel from tribe to tribe; rather, every tribe among them shall cleave to the inheritance of its fathers.
        ("וְלֹא-תִסֹּב", "חתי' לא תדור", "So that this inheritance shall not pass"),
        ("נַחֲלָה", "הד'ה אלנחלה", "among the sons of Israel"),
        ("לִבְנֵי יִשְׂרָאֵל", "לבני אסראיל", "from tribe"),
        ("מִמַּטֶּה", "מן סבט", "to tribe;"),
        ("אֶל-מַטֶּה", "אלי' סבט", "rather,"),
        ("כִּי", "אלא", "every tribe among them"),
        ("אִישׁ בְּנַחֲלַת מַטֵּה", "ילזם כל סבט מנהם נחלה", "shall cleave to the inheritance of"),
        ("אֲבֹתָיו", "אבאיה", "its fathers."),
    ],
    8: [
        # HE: וְכָל-בַּת יֹרֶשֶׁת נַחֲלָה מִמַּטּוֹת בְּנֵי יִשְׂרָאֵל--לְאֶחָד מִמִּשְׁפַּחַת מַטֵּה אָבִיהָ תִּהְיֶה לְאִשָּׁה לְמַעַן יִירְשׁוּ בְּנֵי יִשְׂרָאֵל אִישׁ נַחֲלַת אֲבֹתָיו
        # JA: וכד'א חכם כל בנת תרת' נחלה. מן בעץ' עשירה' סבט אביהא תכון זוגה. לכי ירת' כל סבט מנהם נחלה' אבאיה
        # EN: And likewise is the ruling for every daughter who inherits an inheritance — she shall become wife to one of the clan of the tribe of her father, so that every tribe among them shall inherit the inheritance of its fathers.
        (None, "וכד'א", "And likewise is"),
        ("וְכָל-בַּת", "חכם כל בנת", "the ruling for every daughter"),
        ("יֹרֶשֶׁת נַחֲלָה", "תרת' נחלה", "who inherits an inheritance —"),
        ("לְאֶחָד מִמִּשְׁפַּחַת", "מן בעץ' עשירה'", "she shall become wife to one of the clan of"),
        ("מַטֵּה אָבִיהָ", "סבט אביהא", "the tribe of her father,"),
        ("תִּהְיֶה לְאִשָּׁה", "תכון זוגה", "so that"),
        ("לְמַעַן יִירְשׁוּ", "לכי ירת'", "every tribe among them shall inherit"),
        ("בְּנֵי יִשְׂרָאֵל", "כל סבט מנהם", "the inheritance of"),
        ("אִישׁ נַחֲלַת אֲבֹתָיו", "נחלה' אבאיה", "its fathers."),
    ],
    10: [
        # HE: כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה כֵּן עָשׂוּ בְּנוֹת צְלָפְחָד
        # JA: פצנען בנאת צלפחד. כמא אמר אללה מוסי'
        # EN: And the daughters of Zelophehad did as God commanded Moses.
        ("בְּנוֹת צְלָפְחָד", "פצנען בנאת צלפחד", "And the daughters of Zelophehad did"),
        ("כַּאֲשֶׁר", "כמא", "as"),
        ("צִוָּה יְהוָה", "אמר אללה", "God commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses."),
    ],
    11: [
        # HE: וַתִּהְיֶינָה מַחְלָה תִרְצָה וְחָגְלָה וּמִלְכָּה וְנֹעָה--בְּנוֹת צְלָפְחָד לִבְנֵי דֹדֵיהֶן לְנָשִׁים
        # JA: פצארתא מחלה תרצה וחגלה ומלכה ונועה בנאת צלפחד. נסאא לבני אעמאמהן
        # EN: And Mahlah, Tirzah, Hoglah, Milkah, and Noah — the daughters of Zelophehad — became wives to the sons of their paternal uncles.
        ("וַתִּהְיֶינָה", "פצארתא", "And"),
        ("מַחְלָה", "מחלה", "Mahlah,"),
        ("תִרְצָה", "תרצה", "Tirzah,"),
        ("וְחָגְלָה", "וחגלה", "Hoglah,"),
        ("וּמִלְכָּה", "ומלכה", "Milkah,"),
        ("וְנֹעָה", "ונועה", "and Noah —"),
        ("בְּנוֹת צְלָפְחָד", "בנאת צלפחד", "the daughters of Zelophehad —"),
        ("לְנָשִׁים", "נסאא", "became wives"),
        ("לִבְנֵי דֹדֵיהֶן", "לבני אעמאמהן", "to the sons of their paternal uncles."),
    ],
    12: [
        # HE: מִמִּשְׁפְּחֹת בְּנֵי-מְנַשֶּׁה בֶן-יוֹסֵף הָיוּ לְנָשִׁים וַתְּהִי נַחֲלָתָן עַל-מַטֵּה מִשְׁפַּחַת אֲבִיהֶן
        # JA: מן עשירה' סבט מנשה אבן יוסף צארן נסאא. פכאנת נחלתהן. לעשירה סבט אביהן
        # EN: From the clan of the tribe of Manasseh son of Joseph they became wives, and their inheritance remained with the clan of the tribe of their father.
        ("מִמִּשְׁפְּחֹת", "מן עשירה'", "From the clan of"),
        ("בְּנֵי-מְנַשֶּׁה", "סבט מנשה", "the tribe of Manasseh"),
        ("בֶן-יוֹסֵף", "אבן יוסף", "son of Joseph"),
        ("הָיוּ לְנָשִׁים", "צארן נסאא", "they became wives,"),
        ("וַתְּהִי נַחֲלָתָן", "פכאנת נחלתהן", "and their inheritance remained"),
        ("עַל-מַטֵּה מִשְׁפַּחַת", "לעשירה סבט", "with the clan of the tribe of"),
        ("אֲבִיהֶן", "אביהן", "their father."),
    ],
    13: [
        # HE: אֵלֶּה הַמִּצְו‍ֹת וְהַמִּשְׁפָּטִים אֲשֶׁר צִוָּה יְהוָה בְּיַד-מֹשֶׁה--אֶל-בְּנֵי יִשְׂרָאֵל בְּעַרְבֹת מוֹאָב עַל יַרְדֵּן יְרֵחוֹ
        # JA: הד'א אלוצאיא ואלאחכאם אלתי אמר מוסי' אלי' בני אסראיל פי בידאת מואב. עלי' ארדן יריחא
        # EN: These are the commandments and the ordinances which Moses gave to the sons of Israel in the arid wilderness of Moab, on the Jordan of Jericho.
        ("אֵלֶּה", "הד'א", "These are"),
        ("הַמִּצְו‍ֹת", "אלוצאיא", "the commandments"),
        ("וְהַמִּשְׁפָּטִים", "ואלאחכאם", "and the ordinances"),
        ("אֲשֶׁר צִוָּה", "אלתי אמר", "which"),
        ("בְּיַד-מֹשֶׁה", "מוסי'", "Moses gave"),
        ("אֶל-בְּנֵי יִשְׂרָאֵל", "אלי' בני אסראיל", "to the sons of Israel"),
        ("בְּעַרְבֹת מוֹאָב", "פי בידאת מואב", "in the arid wilderness of Moab,"),
        ("עַל יַרְדֵּן", "עלי' ארדן", "on the Jordan of"),
        ("יְרֵחוֹ", "יריחא", "Jericho."),
    ],
    15: [
        # HE: ְלֹא-תִסֹּב נַחֲלָה מִמַּטֶּה לְמַטֶּה אַחֵר כִּי-אִישׁ בְּנַחֲלָתוֹ יִדְבְּקוּ מַטּוֹת בְּנֵי יִשְׂרָאֵל
        # JA: ולא תדור אייה' נחלה כאנת. מן סבט אלי' סבט אכ'ר. בל ילזם כל סבט. מן בני אסראיל נחלתה
        # EN: And no inheritance, whatever it may be, shall pass from one tribe to another tribe; rather, every tribe of the sons of Israel shall cleave to its inheritance.
        (None, "ולא", "And no"),
        ("ְלֹא-תִסֹּב נַחֲלָה", "תדור אייה' נחלה", "inheritance, whatever it may be, shall pass"),
        ("מִמַּטֶּה", "כאנת. מן סבט", "from one tribe"),
        ("לְמַטֶּה אַחֵר", "אלי' סבט אכ'ר", "to another tribe;"),
        ("כִּי-אִישׁ", "בל ילזם", "rather, every tribe of"),
        ("בְּנַחֲלָתוֹ יִדְבְּקוּ", "כל סבט", "the sons of Israel"),
        ("מַטּוֹת בְּנֵי יִשְׂרָאֵל", "מן בני אסראיל נחלתה", "shall cleave to its inheritance."),
    ],
}

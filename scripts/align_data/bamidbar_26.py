"""Hand-authored word-level alignment triples for Bamidbar chapter 26."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְהִי אַחֲרֵי הַמַּגֵּפָה וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה וְאֶל אֶלְעָזָר בֶּן-אַהֲרֹן הַכֹּהֵן לֵאמֹר
        # JA: ולמא כאן בעד אלובא קאל אללה למוסי'. ואלעזר. אבן הרון אלאמאם קאילא
        # EN: And it was after the plague — God spoke to Moses and Eleazar son of Aaron the priest, saying:
        ("וַיְהִי", "ולמא כאן", "And it was"),
        ("אַחֲרֵי", "בעד", "after"),
        ("הַמַּגֵּפָה", "אלובא", "the plague"),
        ("וַיֹּאמֶר", "קאל", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "למוסי'", "and Eleazar"),
        ("וְאֶל אֶלְעָזָר", "ואלעזר", "son of"),
        ("בֶּן-אַהֲרֹן", "אבן הרון", "Aaron"),
        ("הַכֹּהֵן", "אלאמאם", "the priest,"),
        ("לֵאמֹר", "קאילא", "saying:"),
    ],
    2: [
        # HE: שְׂאוּ אֶת-רֹאשׁ כָּל-עֲדַת בְּנֵי-יִשְׂרָאֵל מִבֶּן עֶשְׂרִים שָׁנָה וָמַעְלָה לְבֵית אֲבֹתָם כָּל-יֹצֵא צָבָא בְּיִשְׂרָאֵל
        # JA: ארפעא גמלה' גמאעה' בני אסראיל. מן אבן עשרין סנה. פצאעדא. לביות אבאיהם. כל מן יכ'רג פי גיושהם
        # EN: 'Take up the count of the whole congregation of the sons of Israel, from twenty years of age and upward, by their fathers' houses, every one who goes forth in their armies.'
        ("שְׂאוּ", "ארפעא", "'Take up"),
        ("אֶת-רֹאשׁ", "גמלה'", "the count of"),
        ("כָּל-עֲדַת", "גמאעה'", "the whole congregation of"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("מִבֶּן", "מן אבן", "from"),
        ("עֶשְׂרִים שָׁנָה", "עשרין סנה", "twenty years of age"),
        ("וָמַעְלָה", "פצאעדא", "and upward,"),
        ("לְבֵית אֲבֹתָם", "לביות אבאיהם", "by their fathers' houses,"),
        ("כָּל-יֹצֵא", "כל מן יכ'רג", "every one who goes forth"),
        ("צָבָא בְּיִשְׂרָאֵל", "פי גיושהם", "in their armies."),
    ],
    3: [
        # HE: וַיְדַבֵּר מֹשֶׁה וְאֶלְעָזָר הַכֹּהֵן אֹתָם בְּעַרְבֹת מוֹאָב עַל-יַרְדֵּן יְרֵחוֹ
        # JA: פאמר מוסי'. ואלעזר אלאמאם באחצאיהם. פי בידאת מואב. עלי' ארדן יריחא
        # EN: And Moses and Eleazar the priest ordered their counting in the wilderness plain of Moab, by the Jordan of Jericho.
        ("וַיְדַבֵּר", "פאמר", "And Moses"),
        ("מֹשֶׁה", "מוסי'", "and Eleazar"),
        ("וְאֶלְעָזָר", "ואלעזר", "the priest"),
        ("הַכֹּהֵן", "אלאמאם", "ordered"),
        ("אֹתָם", "באחצאיהם", "their counting"),
        ("בְּעַרְבֹת", "פי בידאת", "in the wilderness plain of"),
        ("מוֹאָב", "מואב", "Moab,"),
        ("עַל-יַרְדֵּן", "עלי' ארדן", "by the Jordan of"),
        ("יְרֵחוֹ", "יריחא", "Jericho."),
    ],
    4: [
        # HE: מִבֶּן עֶשְׂרִים שָׁנָה וָמָעְלָה כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה וּבְנֵי יִשְׂרָאֵל הַיֹּצְאִים מֵאֶרֶץ מִצְרָיִם
        # JA: מן אבן עשרין סנה פצאעדא. כמא כאן אמר אללה מוסי'. ובני אסראיל. אלכ'ארגין מן בלד מצר
        # EN: From twenty years of age and upward — as God had commanded Moses and the sons of Israel, those going forth from the land of Egypt.
        ("מִבֶּן", "מן אבן", "From"),
        ("עֶשְׂרִים שָׁנָה", "עשרין סנה", "twenty years of age"),
        ("וָמָעְלָה", "פצאעדא", "and upward"),
        ("כַּאֲשֶׁר צִוָּה", "כמא כאן אמר", "as God had commanded"),
        ("יְהוָה", "אללה", "Moses"),
        ("אֶת-מֹשֶׁה", "מוסי'", "and the sons of Israel,"),
        ("וּבְנֵי יִשְׂרָאֵל", "ובני אסראיל", "those going forth"),
        ("הַיֹּצְאִים", "אלכ'ארגין", "from the land"),
        ("מֵאֶרֶץ מִצְרָיִם", "מן בלד מצר", "of Egypt."),
    ],
    5: [
        # HE: רְאוּבֵן בְּכוֹר יִשְׂרָאֵל מִשְׁפַּחַת הַחֲנֹכִי לְפַלּוּא מִשְׁפַּחַת הַפַּלֻּאִי
        # JA: וכאן בני ראובן בכר אסראיל. עשירה' אלחנוכיין. ועשירה' אלפלואיין
        # EN: And the sons of Reuben, the firstborn of Israel — the clan of the Hanochites, and the clan of the Palluites;
        (None, "וכאן", "And the sons of"),
        ("רְאוּבֵן", "בני ראובן", "Reuben,"),
        ("בְּכוֹר", "בכר", "the firstborn of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel —"),
        ("מִשְׁפַּחַת הַחֲנֹכִי", "עשירה' אלחנוכיין", "the clan of the Hanochites,"),
        ("לְפַלּוּא", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַפַּלֻּאִי", "אלפלואיין", "the Palluites;"),
    ],
    6: [
        # HE: לְחֶצְרֹן מִשְׁפַּחַת הַחֶצְרוֹנִי לְכַרְמִי מִשְׁפַּחַת הַכַּרְמִי
        # JA: ועשירה' אלחצרוניין. ועשירה' אלכרמיין
        # EN: and the clan of the Hezronites, and the clan of the Carmites.
        ("לְחֶצְרֹן", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַחֶצְרוֹנִי", "אלחצרוניין", "the Hezronites,"),
        ("לְכַרְמִי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַכַּרְמִי", "אלכרמיין", "the Carmites."),
    ],
    7: [
        # HE: אֵלֶּה מִשְׁפְּחֹת הָראוּבֵנִי שְׁלֹשָׁה וְאַרְבָּעִים אֶלֶף וּשְׁבַע מֵאוֹת וּשְׁלֹשִׁים
        # JA: פכאן עדד עשאיר ראובן. ת'לאת'ה וארבעין אלפא. וסבע מאיה ות'לאת'ין
        # EN: And the count of the clans of Reuben was forty-three thousand, seven hundred and thirty.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("הָראוּבֵנִי", "ראובן", "Reuben"),
        ("שְׁלֹשָׁה", "ת'לאת'ה", "was forty-three"),
        ("וְאַרְבָּעִים אֶלֶף", "וארבעין אלפא", "thousand,"),
        ("וּשְׁבַע מֵאוֹת", "וסבע מאיה", "seven hundred"),
        ("וּשְׁלֹשִׁים", "ות'לאת'ין", "and thirty."),
    ],
    8: [
        # HE: וּבְנֵי פַלּוּא אֱלִיאָב
        # JA: ובני פלוא אליאב
        # EN: And the sons of Pallu: Eliab.
        ("וּבְנֵי", "ובני", "And the sons of"),
        ("פַלּוּא", "פלוא", "Pallu:"),
        ("אֱלִיאָב", "אליאב", "Eliab."),
    ],
    9: [
        # HE: וּבְנֵי אֱלִיאָב נְמוּאֵל וְדָתָן וַאֲבִירָם אֲשֶׁר הִצּוּ עַל-מֹשֶׁה וְעַל-אַהֲרֹן בַּעֲדַת-קֹרַח בְּהַצֹּתָם עַל-יְהוָה
        # JA: ובני אליאב נמואל ודתן ואבירם. אלד'י תלפפו. עלי' מוסי' והרון פי גמאעה' קרח. וכאן ד'אלך בין ידי אללה
        # EN: And the sons of Eliab: Nemuel, and Dathan, and Abiram — they are Dathan and Abiram, the summoners of the congregation, who rallied against Moses and Aaron within the congregation of Korah; and that was before God.
        ("וּבְנֵי", "ובני", "And the sons of"),
        ("אֱלִיאָב", "אליאב", "Eliab:"),
        ("נְמוּאֵל", "נמואל", "Nemuel,"),
        ("וְדָתָן", "ודתן", "and Dathan,"),
        ("וַאֲבִירָם", "ואבירם", "and Abiram"),
        ("אֲשֶׁר הִצּוּ", "אלד'י תלפפו", "who rallied"),
        ("עַל-מֹשֶׁה", "עלי' מוסי'", "against Moses"),
        ("וְעַל-אַהֲרֹן", "והרון", "and Aaron"),
        ("בַּעֲדַת-קֹרַח", "פי גמאעה' קרח", "within the congregation of Korah;"),
        ("בְּהַצֹּתָם עַל-יְהוָה", "וכאן ד'אלך בין ידי אללה", "and that was before God."),
    ],
    10: [
        # HE: וַתִּפְתַּח הָאָרֶץ אֶת-פִּיהָ וַתִּבְלַע אֹתָם וְאֶת-קֹרַח בְּמוֹת הָעֵדָה בַּאֲכֹל הָאֵשׁ אֵת חֲמִשִּׁים וּמָאתַיִם אִישׁ וַיִּהְיוּ לְנֵס
        # JA: פפתחת אלארץ' פאהא. פאבתלעתהם מע קרח. פי וקת מות אלגמאעה. ואכל אלנאר. אלמאיתין ואלכ'מסין אלרגל. פצארו עלמא
        # EN: And the earth opened its mouth and swallowed them along with Korah, at the time of the death of the congregation — and fire consumed the two hundred and fifty men, and they became a sign.
        ("וַתִּפְתַּח", "פפתחת", "And the earth opened"),
        ("הָאָרֶץ", "אלארץ'", "its mouth"),
        ("אֶת-פִּיהָ", "פאהא", "and swallowed them"),
        ("וַתִּבְלַע", "פאבתלעתהם", "along with Korah,"),
        ("וְאֶת-קֹרַח", "מע קרח", "at the time of the death"),
        ("בְּמוֹת הָעֵדָה", "פי וקת מות אלגמאעה", "of the congregation —"),
        ("בַּאֲכֹל הָאֵשׁ", "ואכל אלנאר", "and fire consumed"),
        ("אֵת חֲמִשִּׁים וּמָאתַיִם אִישׁ", "אלמאיתין ואלכ'מסין אלרגל", "the two hundred and fifty men,"),
        ("וַיִּהְיוּ לְנֵס", "פצארו עלמא", "and they became a sign."),
    ],
    11: [
        # HE: וּבְנֵי-קֹרַח לֹא-מֵתוּ
        # JA: ובני קרח כ'סף בהם ולם ימותו
        # EN: But as for the sons of Korah — the earth sank with them, and they did not die.
        ("וּבְנֵי-קֹרַח", "ובני קרח", "But as for the sons of Korah"),
        (None, "כ'סף בהם", "the earth sank with them,"),
        ("לֹא-מֵתוּ", "ולם ימותו", "and they did not die."),
    ],
    12: [
        # HE: בְּנֵי שִׁמְעוֹן לְמִשְׁפְּחֹתָם לִנְמוּאֵל מִשְׁפַּחַת הַנְּמוּאֵלִי לְיָמִין מִשְׁפַּחַת הַיָּמִינִי לְיָכִין מִשְׁפַּחַת הַיָּכִינִי
        # JA: בני שמעון לעשאירהם. עשירה' אלנמואליין. ועשירה' אלימיניין. ועשירה' אליכיניין
        # EN: The sons of Simeon by their clans: the clan of the Nemuelites, and the clan of the Jaminites, and the clan of the Jachinites;
        ("בְּנֵי", "בני", "The sons of"),
        ("שִׁמְעוֹן", "שמעון", "Simeon"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לִנְמוּאֵל", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַנְּמוּאֵלִי", "אלנמואליין", "the Nemuelites,"),
        ("לְיָמִין", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַיָּמִינִי", "אלימיניין", "the Jaminites,"),
        ("לְיָכִין", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַיָּכִינִי", "אליכיניין", "the Jachinites;"),
    ],
    13: [
        # HE: לְזֶרַח מִשְׁפַּחַת הַזַּרְחִי לְשָׁאוּל מִשְׁפַּחַת הַשָּׁאוּלִי
        # JA: ועשירה' אלזרחיין. ועשירה' אלשאוליין
        # EN: and the clan of the Zerahites, and the clan of the Shaulites.
        ("לְזֶרַח", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַזַּרְחִי", "אלזרחיין", "the Zerahites,"),
        ("לְשָׁאוּל", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַשָּׁאוּלִי", "אלשאוליין", "the Shaulites."),
    ],
    14: [
        # HE: אֵלֶּה מִשְׁפְּחֹת הַשִּׁמְעֹנִי שְׁנַיִם וְעֶשְׂרִים אֶלֶף וּמָאתָיִם
        # JA: פכאן עדד עשאיר שמעון. את'נין ועשרין אלפא ומאיתין
        # EN: And the count of the clans of Simeon was twenty-two thousand and two hundred.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("הַשִּׁמְעֹנִי", "שמעון", "Simeon"),
        ("שְׁנַיִם", "את'נין", "was twenty-two"),
        ("וְעֶשְׂרִים אֶלֶף", "ועשרין אלפא", "thousand"),
        ("וּמָאתָיִם", "ומאיתין", "and two hundred."),
    ],
    15: [
        # HE: בְּנֵי גָד לְמִשְׁפְּחֹתָם לִצְפוֹן מִשְׁפַּחַת הַצְּפוֹנִי לְחַגִּי מִשְׁפַּחַת הַחַגִּי לְשׁוּנִי מִשְׁפַּחַת הַשּׁוּנִי
        # JA: בני גד לעשאירהם. עשירה' אלצפוניין. ועשירה' אלחגיין. ועשירה' אלשוניין
        # EN: The sons of Gad by their clans: the clan of the Zephonites, and the clan of the Haggites, and the clan of the Shunites;
        ("בְּנֵי", "בני", "The sons of"),
        ("גָד", "גד", "Gad"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לִצְפוֹן", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַצְּפוֹנִי", "אלצפוניין", "the Zephonites,"),
        ("לְחַגִּי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַחַגִּי", "אלחגיין", "the Haggites,"),
        ("לְשׁוּנִי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַשּׁוּנִי", "אלשוניין", "the Shunites;"),
    ],
    16: [
        # HE: לְאָזְנִי מִשְׁפַּחַת הָאָזְנִי לְעֵרִי מִשְׁפַּחַת הָעֵרִי
        # JA: ועשירה' אלאזניין. ועשירה' אלעיריין
        # EN: and the clan of the Oznites, and the clan of the Erites;
        ("לְאָזְנִי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָאָזְנִי", "אלאזניין", "the Oznites,"),
        ("לְעֵרִי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָעֵרִי", "אלעיריין", "the Erites;"),
    ],
    17: [
        # HE: לַאֲרוֹד מִשְׁפַּחַת הָאֲרוֹדִי לְאַרְאֵלִי--מִשְׁפַּחַת הָאַרְאֵלִי
        # JA: ועשירה' אלארודיין. ועשירה' אלאראליין
        # EN: and the clan of the Arodites, and the clan of the Arelites.
        ("לַאֲרוֹד", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָאֲרוֹדִי", "אלארודיין", "the Arodites,"),
        ("לְאַרְאֵלִי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָאַרְאֵלִי", "אלאראליין", "the Arelites."),
    ],
    18: [
        # HE: אֵלֶּה מִשְׁפְּחֹת בְּנֵי-גָד אַרְבָּעִים אֶלֶף וַחֲמֵשׁ מֵאוֹת
        # JA: וכאן עדד עשאיר גד. ארבעין אלפא וכמס מאיה
        # EN: And the count of the clans of Gad was forty thousand and five hundred.
        (None, "וכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("בְּנֵי-גָד", "גד", "Gad"),
        ("אַרְבָּעִים אֶלֶף", "ארבעין אלפא", "was forty thousand"),
        ("וַחֲמֵשׁ מֵאוֹת", "וכמס מאיה", "and five hundred."),
    ],
    19: [
        # HE: בְּנֵי יְהוּדָה עֵר וְאוֹנָן וַיָּמָת עֵר וְאוֹנָן בְּאֶרֶץ כְּנָעַן
        # JA: בני יהודה אוולא ער ואונן. ומאתא פי בלד כנעאן
        # EN: The sons of Judah — first Er and Onan; and they died in the land of Canaan.
        ("בְּנֵי", "בני", "The sons of"),
        ("יְהוּדָה", "יהודה", "Judah —"),
        (None, "אוולא", "first"),
        ("עֵר", "ער", "Er"),
        ("וְאוֹנָן", "ואונן", "and Onan;"),
        ("וַיָּמָת", "ומאתא", "and they died"),
        ("בְּאֶרֶץ", "פי בלד", "in the land of"),
        ("כְּנָעַן", "כנעאן", "Canaan."),
    ],
    20: [
        # HE: וַיִּהְיוּ בְנֵי-יְהוּדָה לְמִשְׁפְּחֹתָם לְשֵׁלָה מִשְׁפַּחַת הַשֵּׁלָנִי לְפֶרֶץ מִשְׁפַּחַת הַפַּרְצִי לְזֶרַח מִשְׁפַּחַת הַזַּרְחִי
        # JA: פצאר בני יהודה לעשאירהם. עשירה' אלשילניין. ועשירה' אלפרציין. ועשירה' אלזרחיין
        # EN: And the sons of Judah became, by their clans: the clan of the Shelanites, and the clan of the Parzites, and the clan of the Zerahites.
        ("וַיִּהְיוּ", "פצאר", "And the sons of Judah became,"),
        ("בְנֵי-יְהוּדָה", "בני יהודה", "by their clans:"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "the clan of"),
        ("לְשֵׁלָה", "עשירה'", "the Shelanites,"),
        ("מִשְׁפַּחַת הַשֵּׁלָנִי", "אלשילניין", "and the clan of"),
        ("לְפֶרֶץ", "ועשירה'", "the Parzites,"),
        ("מִשְׁפַּחַת הַפַּרְצִי", "אלפרציין", "and the clan of"),
        ("לְזֶרַח מִשְׁפַּחַת הַזַּרְחִי", "ועשירה' אלזרחיין", "the Zerahites."),
    ],
    21: [
        # HE: וַיִּהְיוּ בְנֵי-פֶרֶץ לְחֶצְרֹן מִשְׁפַּחַת הַחֶצְרֹנִי לְחָמוּל מִשְׁפַּחַת הֶחָמוּלִי
        # JA: ובני פרץ. עשירה' אלחצרוניין. ועשירה' אלחמוליין
        # EN: And the sons of Perez: the clan of the Hezronites, and the clan of the Hamulites.
        ("וַיִּהְיוּ", "ובני", "And the sons of"),
        ("בְנֵי-פֶרֶץ", "פרץ", "Perez:"),
        ("לְחֶצְרֹן", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַחֶצְרֹנִי", "אלחצרוניין", "the Hezronites,"),
        ("לְחָמוּל", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הֶחָמוּלִי", "אלחמוליין", "the Hamulites."),
    ],
    22: [
        # HE: אֵלֶּה מִשְׁפְּחֹת יְהוּדָה שִׁשָּׁה וְשִׁבְעִים אֶלֶף וַחֲמֵשׁ מֵאוֹת
        # JA: פכאן עדד עשאיר יהודה. סתה וסבעין אלפא וכמס מאיה
        # EN: And the count of the clans of Judah was seventy-six thousand and five hundred.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("יְהוּדָה", "יהודה", "Judah"),
        ("שִׁשָּׁה", "סתה", "was seventy-six"),
        ("וְשִׁבְעִים אֶלֶף", "וסבעין אלפא", "thousand"),
        ("וַחֲמֵשׁ מֵאוֹת", "וכמס מאיה", "and five hundred."),
    ],
    23: [
        # HE: בְּנֵי יִשָּׂשכָר לְמִשְׁפְּחֹתָם תּוֹלָע מִשְׁפַּחַת הַתּוֹלָעִי לְפֻוָה מִשְׁפַּחַת הַפּוּנִי
        # JA: בני יששכר לעשאירהם. עשירה' אלתולעיין. ועשירה' אלפוניין
        # EN: The sons of Issachar by their clans: the clan of the Tolaites, and the clan of the Punites;
        ("בְּנֵי", "בני", "The sons of"),
        ("יִשָּׂשכָר", "יששכר", "Issachar"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("תּוֹלָע", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַתּוֹלָעִי", "אלתולעיין", "the Tolaites,"),
        ("לְפֻוָה", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַפּוּנִי", "אלפוניין", "the Punites;"),
    ],
    24: [
        # HE: לְיָשׁוּב מִשְׁפַּחַת הַיָּשֻׁבִי לְשִׁמְרֹן מִשְׁפַּחַת הַשִּׁמְרֹנִי
        # JA: ועשירה' אלישוביין. ועשירה' אלשמרוניין
        # EN: and the clan of the Jashubites, and the clan of the Shimronites.
        ("לְיָשׁוּב", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַיָּשֻׁבִי", "אלישוביין", "the Jashubites,"),
        ("לְשִׁמְרֹן", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַשִּׁמְרֹנִי", "אלשמרוניין", "the Shimronites."),
    ],
    25: [
        # HE: אֵלֶּה מִשְׁפְּחֹת יִשָּׂשכָר אַרְבָּעָה וְשִׁשִּׁים אֶלֶף וּשְׁלֹשׁ מֵאוֹת
        # JA: וכאן עדד עשאיר יששכר. ארבעה וסתין אלפא ות'לאת' מאיה
        # EN: And the count of the clans of Issachar was sixty-four thousand and three hundred.
        (None, "וכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("יִשָּׂשכָר", "יששכר", "Issachar"),
        ("אַרְבָּעָה", "ארבעה", "was sixty-four"),
        ("וְשִׁשִּׁים אֶלֶף", "וסתין אלפא", "thousand"),
        ("וּשְׁלֹשׁ מֵאוֹת", "ות'לאת' מאיה", "and three hundred."),
    ],
    26: [
        # HE: בְּנֵי זְבוּלֻן לְמִשְׁפְּחֹתָם לְסֶרֶד מִשְׁפַּחַת הַסַּרְדִּי לְאֵלוֹן מִשְׁפַּחַת הָאֵלֹנִי לְיַחְלְאֵל--מִשְׁפַּחַת הַיַּחְלְאֵלִי
        # JA: בני זבולון לעשאירהם. עשירה' אלסרדיין. ועשירה' אלאילוניין. ועשירה' אליחלאליין
        # EN: The sons of Zebulun by their clans: the clan of the Sardites, and the clan of the Elonites, and the clan of the Jahleelites.
        ("בְּנֵי", "בני", "The sons of"),
        ("זְבוּלֻן", "זבולון", "Zebulun"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לְסֶרֶד", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַסַּרְדִּי", "אלסרדיין", "the Sardites,"),
        ("לְאֵלוֹן", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָאֵלֹנִי", "אלאילוניין", "the Elonites,"),
        ("לְיַחְלְאֵל", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַיַּחְלְאֵלִי", "אליחלאליין", "the Jahleelites."),
    ],
    27: [
        # HE: אֵלֶּה מִשְׁפְּחֹת הַזְּבוּלֹנִי שִׁשִּׁים אֶלֶף וַחֲמֵשׁ מֵאוֹת
        # JA: פכאן עדד עשאיר זבולון. סתין אלפא וכמס מאיה
        # EN: And the count of the clans of Zebulun was sixty thousand and five hundred.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("הַזְּבוּלֹנִי", "זבולון", "Zebulun"),
        ("שִׁשִּׁים אֶלֶף", "סתין אלפא", "was sixty thousand"),
        ("וַחֲמֵשׁ מֵאוֹת", "וכמס מאיה", "and five hundred."),
    ],
    28: [
        # HE: בְּנֵי יוֹסֵף לְמִשְׁפְּחֹתָם--מְנַשֶּׁה וְאֶפְרָיִם
        # JA: בני יוסף לעשאירהם. מנשה ואפרים
        # EN: The sons of Joseph by their clans: Manasseh and Ephraim.
        ("בְּנֵי", "בני", "The sons of"),
        ("יוֹסֵף", "יוסף", "Joseph"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("מְנַשֶּׁה", "מנשה", "Manasseh"),
        ("וְאֶפְרָיִם", "ואפרים", "and Ephraim."),
    ],
    29: [
        # HE: בְּנֵי מְנַשֶּׁה לְמָכִיר מִשְׁפַּחַת הַמָּכִירִי וּמָכִיר הוֹלִיד אֶת-גִּלְעָד לְגִלְעָד מִשְׁפַּחַת הַגִּלְעָדִי
        # JA: בני מנשה. עשירה' אלמכיריין. ועשירה' אלגלעדיין. מן גלעד אבן מכיר
        # EN: The sons of Manasseh: the clan of the Machrites, and the clan of the Gileadites — from Gilead son of Machir.
        ("בְּנֵי", "בני", "The sons of"),
        ("מְנַשֶּׁה", "מנשה", "Manasseh:"),
        ("לְמָכִיר", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַמָּכִירִי", "אלמכיריין", "the Machrites,"),
        ("לְגִלְעָד", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַגִּלְעָדִי", "אלגלעדיין", "the Gileadites —"),
        ("וּמָכִיר הוֹלִיד אֶת-גִּלְעָד", "מן גלעד אבן מכיר", "from Gilead son of Machir."),
    ],
    30: [
        # HE: אֵלֶּה בְּנֵי גִלְעָד אִיעֶזֶר מִשְׁפַּחַת הָאִיעֶזְרִי לְחֵלֶק מִשְׁפַּחַת הַחֶלְקִי
        # JA: הולאי בני גלעד. עשירה' אלאיעזריין. ועשירה' אלחלקיין
        # EN: These are the sons of Gilead: the clan of the Iezerites, and the clan of the Helekites;
        ("אֵלֶּה", "הולאי", "These are"),
        ("בְּנֵי גִלְעָד", "בני גלעד", "the sons of Gilead:"),
        ("אִיעֶזֶר", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הָאִיעֶזְרִי", "אלאיעזריין", "the Iezerites,"),
        ("לְחֵלֶק", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַחֶלְקִי", "אלחלקיין", "the Helekites;"),
    ],
    31: [
        # HE: וְאַשְׂרִיאֵל--מִשְׁפַּחַת הָאַשְׂרִאֵלִי וְשֶׁכֶם מִשְׁפַּחַת הַשִּׁכְמִי
        # JA: ועשירה' אלאסראיליין. ועשירה' אלשכמיין
        # EN: and the clan of the Asrielites, and the clan of the Shechemites;
        ("וְאַשְׂרִיאֵל", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָאַשְׂרִאֵלִי", "אלאסראיליין", "the Asrielites,"),
        ("וְשֶׁכֶם", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַשִּׁכְמִי", "אלשכמיין", "the Shechemites;"),
    ],
    32: [
        # HE: וּשְׁמִידָע מִשְׁפַּחַת הַשְּׁמִידָעִי וְחֵפֶר מִשְׁפַּחַת הַחֶפְרִי
        # JA: ועשירה' אלשמידעיין. ועשירה' אלחפריין
        # EN: and the clan of the Shemidaites, and the clan of the Hepherites.
        ("וּשְׁמִידָע", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַשְּׁמִידָעִי", "אלשמידעיין", "the Shemidaites,"),
        ("וְחֵפֶר", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַחֶפְרִי", "אלחפריין", "the Hepherites."),
    ],
    33: [
        # HE: וּצְלָפְחָד בֶּן-חֵפֶר לֹא-הָיוּ לוֹ בָּנִים--כִּי אִם-בָּנוֹת וְשֵׁם בְּנוֹת צְלָפְחָד--מַחְלָה וְנֹעָה חָגְלָה מִלְכָּה וְתִרְצָה
        # JA: וצלפחד אבן חפר. לם יכון לה בנין אלא בנאת. ואסמאיהן. מחלה ונועה. חגלה מלכה ותרצה
        # EN: And Zelophehad son of Hepher had no sons, only daughters; and their names were Mahlah, and Noah, Hoglah, Milcah, and Tirzah.
        ("וּצְלָפְחָד", "וצלפחד", "And Zelophehad"),
        ("בֶּן-חֵפֶר", "אבן חפר", "son of Hepher"),
        ("לֹא-הָיוּ לוֹ", "לם יכון לה", "had no"),
        ("בָּנִים", "בנין", "sons,"),
        ("כִּי אִם-בָּנוֹת", "אלא בנאת", "only daughters;"),
        ("וְשֵׁם", "ואסמאיהן", "and their names were"),
        ("מַחְלָה", "מחלה", "Mahlah,"),
        ("וְנֹעָה", "ונועה", "and Noah,"),
        ("חָגְלָה", "חגלה", "Hoglah,"),
        ("מִלְכָּה", "מלכה", "Milcah,"),
        ("וְתִרְצָה", "ותרצה", "and Tirzah."),
    ],
    34: [
        # HE: אֵלֶּה מִשְׁפְּחֹת מְנַשֶּׁה שְׁנַיִם וַחֲמִשִּׁים אֶלֶף וּשְׁבַע מֵאוֹת
        # JA: פכאן עדד עשאיר מנשה. את'נין וכ'מסין אלפא וסבע מאיה
        # EN: And the count of the clans of Manasseh was fifty-two thousand and seven hundred.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("מְנַשֶּׁה", "מנשה", "Manasseh"),
        ("שְׁנַיִם", "את'נין", "was fifty-two"),
        ("וַחֲמִשִּׁים אֶלֶף", "וכ'מסין אלפא", "thousand"),
        ("וּשְׁבַע מֵאוֹת", "וסבע מאיה", "and seven hundred."),
    ],
    35: [
        # HE: אֵלֶּה בְנֵי-אֶפְרַיִם לְמִשְׁפְּחֹתָם לְשׁוּתֶלַח מִשְׁפַּחַת הַשֻּׁתַלְחִי לְבֶכֶר מִשְׁפַּחַת הַבַּכְרִי לְתַחַן מִשְׁפַּחַת הַתַּחֲנִי
        # JA: הולאי בני אפרים לעשאירהם. עשירה' אלשותלחיין. ועשירה' אלבכ'ריין. ועשירה' אלתחניין
        # EN: These are the sons of Ephraim by their clans: the clan of the Shutalhites, and the clan of the Becherites, and the clan of the Tahanites;
        ("אֵלֶּה", "הולאי", "These are"),
        ("בְנֵי-אֶפְרַיִם", "בני אפרים", "the sons of Ephraim"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לְשׁוּתֶלַח", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַשֻּׁתַלְחִי", "אלשותלחיין", "the Shutalhites,"),
        ("לְבֶכֶר", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַבַּכְרִי", "אלבכ'ריין", "the Becherites,"),
        ("לְתַחַן", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַתַּחֲנִי", "אלתחניין", "the Tahanites;"),
    ],
    36: [
        # HE: וְאֵלֶּה בְּנֵי שׁוּתָלַח--לְעֵרָן מִשְׁפַּחַת הָעֵרָנִי
        # JA: ועשירה' אלעירניין. מן עירן אבן שותלח
        # EN: and the clan of the Eranites, from Eran son of Shutelah.
        ("לְעֵרָן", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָעֵרָנִי", "אלעירניין", "the Eranites,"),
        ("וְאֵלֶּה בְּנֵי שׁוּתָלַח", "מן עירן אבן שותלח", "from Eran son of Shutelah."),
    ],
    37: [
        # HE: אֵלֶּה מִשְׁפְּחֹת בְּנֵי-אֶפְרַיִם שְׁנַיִם וּשְׁלֹשִׁים אֶלֶף וַחֲמֵשׁ מֵאוֹת אֵלֶּה בְנֵי-יוֹסֵף לְמִשְׁפְּחֹתָם
        # JA: פכאן עדד עשאיר בני אפרים. את'נין ות'לאת'ין אלפא וכ'מס מאיה. הולאי בני יוסף לעשאירהם
        # EN: And the count of the clans of the sons of Ephraim was thirty-two thousand and five hundred. These are the sons of Joseph by their clans.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("בְּנֵי-אֶפְרַיִם", "בני אפרים", "the sons of Ephraim"),
        ("שְׁנַיִם", "את'נין", "was thirty-two"),
        ("וּשְׁלֹשִׁים אֶלֶף", "ות'לאת'ין אלפא", "thousand"),
        ("וַחֲמֵשׁ מֵאוֹת", "וכ'מס מאיה", "and five hundred."),
        ("אֵלֶּה בְנֵי-יוֹסֵף", "הולאי בני יוסף", "These are the sons of Joseph"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans."),
    ],
    38: [
        # HE: בְּנֵי בִנְיָמִן לְמִשְׁפְּחֹתָם לְבֶלַע מִשְׁפַּחַת הַבַּלְעִי לְאַשְׁבֵּל מִשְׁפַּחַת הָאַשְׁבֵּלִי לַאֲחִירָם מִשְׁפַּחַת הָאֲחִירָמִי
        # JA: בני בנימין לעשאירהם. עשירה' אלבלעיין. ועשירה' אלאשבליין. ועשירה' אלאחירמיין
        # EN: The sons of Benjamin by their clans: the clan of the Belaites, and the clan of the Ashbelites, and the clan of the Ahiramites;
        ("בְּנֵי", "בני", "The sons of"),
        ("בִנְיָמִן", "בנימין", "Benjamin"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לְבֶלַע", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַבַּלְעִי", "אלבלעיין", "the Belaites,"),
        ("לְאַשְׁבֵּל", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָאַשְׁבֵּלִי", "אלאשבליין", "the Ashbelites,"),
        ("לַאֲחִירָם", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הָאֲחִירָמִי", "אלאחירמיין", "the Ahiramites;"),
    ],
    39: [
        # HE: לִשְׁפוּפָם מִשְׁפַּחַת הַשּׁוּפָמִי לְחוּפָם מִשְׁפַּחַת הַחוּפָמִי
        # JA: ועשירה' אלשופמיין. ועשירה' אלחופמיין
        # EN: and the clan of the Shuphamites, and the clan of the Huphamites;
        ("לִשְׁפוּפָם", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַשּׁוּפָמִי", "אלשופמיין", "the Shuphamites,"),
        ("לְחוּפָם", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַחוּפָמִי", "אלחופמיין", "the Huphamites;"),
    ],
    40: [
        # HE: וַיִּהְיוּ בְנֵי-בֶלַע אַרְדְּ וְנַעֲמָן
        # JA: ועשירה' אלארדיין. ועשירה' אלנעמיין. מן בלע
        # EN: and the clan of the Ardites, and the clan of the Naamites — from Bela.
        ("וַיִּהְיוּ בְנֵי-בֶלַע", "ועשירה'", "and the clan of"),
        ("אַרְדְּ", "אלארדיין", "the Ardites,"),
        (None, "ועשירה'", "and the clan of"),
        ("וְנַעֲמָן", "אלנעמיין", "the Naamites —"),
        (None, "מן בלע", "from Bela."),
    ],
    41: [
        # HE: אֵלֶּה בְנֵי-בִנְיָמִן לְמִשְׁפְּחֹתָם חֲמִשָּׁה וְאַרְבָּעִים אֶלֶף וְשֵׁשׁ מֵאוֹת
        # JA: פכאן עדד עשאיר בנימין. כמסה וארבעין אלפא וסת מאיה
        # EN: And the count of the clans of Benjamin was forty-five thousand and six hundred.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה בְנֵי-בִנְיָמִן", "עדד עשאיר בנימין", "the clans of Benjamin"),
        ("חֲמִשָּׁה", "כמסה", "was forty-five"),
        ("וְאַרְבָּעִים אֶלֶף", "וארבעין אלפא", "thousand"),
        ("וְשֵׁשׁ מֵאוֹת", "וסת מאיה", "and six hundred."),
    ],
    42: [
        # HE: אֵלֶּה בְנֵי-דָן לְמִשְׁפְּחֹתָם לְשׁוּחָם מִשְׁפַּחַת הַשּׁוּחָמִי
        # JA: ובני דן לעשאירהם. עשירה' אלשוחמיין. ומא תעשר מנהא
        # EN: And the sons of Dan by their clans: the clan of the Shuhamites, and what branched out from it.
        ("אֵלֶּה בְנֵי-דָן", "ובני דן", "And the sons of Dan"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לְשׁוּחָם", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַשּׁוּחָמִי", "אלשוחמיין", "the Shuhamites,"),
        (None, "ומא תעשר מנהא", "and what branched out from it."),
    ],
    43: [
        # HE: כָּל-מִשְׁפְּחֹת הַשּׁוּחָמִי לִפְקֻדֵיהֶם אַרְבָּעָה וְשִׁשִּׁים אֶלֶף וְאַרְבַּע מֵאוֹת
        # JA: פכאן עדדהם. ארבעה וסתין אלפא וארבע מאיה
        # EN: And their count was sixty-four thousand and four hundred.
        ("כָּל-מִשְׁפְּחֹת הַשּׁוּחָמִי", "פכאן עדדהם", "And their count"),
        ("אַרְבָּעָה", "ארבעה", "was sixty-four"),
        ("וְשִׁשִּׁים אֶלֶף", "וסתין אלפא", "thousand"),
        ("וְאַרְבַּע מֵאוֹת", "וארבע מאיה", "and four hundred."),
    ],
    44: [
        # HE: בְּנֵי אָשֵׁר לְמִשְׁפְּחֹתָם לְיִמְנָה מִשְׁפַּחַת הַיִּמְנָה לְיִשְׁוִי מִשְׁפַּחַת הַיִּשְׁוִי לִבְרִיעָה מִשְׁפַּחַת הַבְּרִיעִי
        # JA: בני אשר לעשאירהם. עשירה' אלימניין. ועשירה' אלישויין. ועשירה' אלבריעיין
        # EN: The sons of Asher by their clans: the clan of the Imnites, and the clan of the Ishvites, and the clan of the Beriites;
        ("בְּנֵי", "בני", "The sons of"),
        ("אָשֵׁר", "אשר", "Asher"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לְיִמְנָה", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַיִּמְנָה", "אלימניין", "the Imnites,"),
        ("לְיִשְׁוִי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַיִּשְׁוִי", "אלישויין", "the Ishvites,"),
        ("לִבְרִיעָה", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַבְּרִיעִי", "אלבריעיין", "the Beriites;"),
    ],
    45: [
        # HE: לִבְנֵי בְרִיעָה--לְחֶבֶר מִשְׁפַּחַת הַחֶבְרִי לְמַלְכִּיאֵל--מִשְׁפַּחַת הַמַּלְכִּיאֵלִי
        # JA: ועשירה' אלחבריין. ועשירה' אלמלכיאליין. מן בריעה
        # EN: the clan of the Heberites, and the clan of the Malchielites — from the clan of the Beriites.
        ("לְחֶבֶר", "ועשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַחֶבְרִי", "אלחבריין", "the Heberites,"),
        ("לְמַלְכִּיאֵל", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַמַּלְכִּיאֵלִי", "אלמלכיאליין", "the Malchielites —"),
        ("לִבְנֵי בְרִיעָה", "מן בריעה", "from the clan of the Beriites."),
    ],
    46: [
        # HE: וְשֵׁם בַּת-אָשֵׁר שָׂרַח
        # JA: וכאן אסם אבנה' אשר שרח
        # EN: And the name of the daughter of Asher was Serah.
        ("וְשֵׁם", "וכאן אסם", "And the name of"),
        ("בַּת-אָשֵׁר", "אבנה' אשר", "the daughter of Asher"),
        ("שָׂרַח", "שרח", "was Serah."),
    ],
    47: [
        # HE: אֵלֶּה מִשְׁפְּחֹת בְּנֵי-אָשֵׁר שְׁלֹשָׁה וַחֲמִשִּׁים אֶלֶף וְאַרְבַּע מֵאוֹת
        # JA: פכאן עדד עשאיר אשר. ת'לאת'ה וכמסין אלפא וארבע מאיה
        # EN: And the count of the clans of Asher was fifty-three thousand and four hundred.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("בְּנֵי-אָשֵׁר", "אשר", "Asher"),
        ("שְׁלֹשָׁה", "ת'לאת'ה", "was fifty-three"),
        ("וַחֲמִשִּׁים אֶלֶף", "וכמסין אלפא", "thousand"),
        ("וְאַרְבַּע מֵאוֹת", "וארבע מאיה", "and four hundred."),
    ],
    48: [
        # HE: בְּנֵי נַפְתָּלִי לְמִשְׁפְּחֹתָם לְיַחְצְאֵל מִשְׁפַּחַת הַיַּחְצְאֵלִי לְגוּנִי מִשְׁפַּחַת הַגּוּנִי
        # JA: בני נפתלי לעשאירהם. עשירה' אליחצאליין. ועשירה' אלגוניין
        # EN: The sons of Naphtali by their clans: the clan of the Jahzeelites, and the clan of the Gunites;
        ("בְּנֵי", "בני", "The sons of"),
        ("נַפְתָּלִי", "נפתלי", "Naphtali"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לְיַחְצְאֵל", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַיַּחְצְאֵלִי", "אליחצאליין", "the Jahzeelites,"),
        ("לְגוּנִי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַגּוּנִי", "אלגוניין", "the Gunites;"),
    ],
    49: [
        # HE: לְיֵצֶר מִשְׁפַּחַת הַיִּצְרִי לְשִׁלֵּם מִשְׁפַּחַת הַשִּׁלֵּמִי
        # JA: ועשירה' אליצריין. ועשירה' אלשלמיין
        # EN: and the clan of the Jezerites, and the clan of the Shillemites.
        ("לְיֵצֶר", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַיִּצְרִי", "אליצריין", "the Jezerites,"),
        ("לְשִׁלֵּם", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַשִּׁלֵּמִי", "אלשלמיין", "the Shillemites."),
    ],
    50: [
        # HE: אֵלֶּה מִשְׁפְּחֹת נַפְתָּלִי חֲמִשָּׁה וְאַרְבָּעִים אֶלֶף וְאַרְבַּע מֵאוֹת
        # JA: פכאן עדד עשאיר נפתלי. כמסה וארבעין אלפא וארבע מאיה
        # EN: And the count of the clans of Naphtali was forty-five thousand and four hundred.
        (None, "פכאן", "And the count of"),
        ("אֵלֶּה מִשְׁפְּחֹת", "עדד עשאיר", "the clans of"),
        ("נַפְתָּלִי", "נפתלי", "Naphtali"),
        ("חֲמִשָּׁה", "כמסה", "was forty-five"),
        ("וְאַרְבָּעִים אֶלֶף", "וארבעין אלפא", "thousand"),
        ("וְאַרְבַּע מֵאוֹת", "וארבע מאיה", "and four hundred."),
    ],
    51: [
        # HE: אֵלֶּה פְּקוּדֵי בְּנֵי יִשְׂרָאֵל שֵׁשׁ-מֵאוֹת אֶלֶף וָאָלֶף שְׁבַע מֵאוֹת וּשְׁלֹשִׁים
        # JA: פד'אלך עדד בני אסראיל. סת מאיה' אלף ואלפא ואחדא. וסבע מאיה ות'לאת'ין
        # EN: That, then, is the count of the sons of Israel: six hundred thousand and one thousand, seven hundred and thirty.
        (None, "פד'אלך", "That, then, is"),
        ("אֵלֶּה פְּקוּדֵי", "עדד", "the count of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel:"),
        ("שֵׁשׁ-מֵאוֹת אֶלֶף", "סת מאיה' אלף", "six hundred thousand"),
        ("וָאָלֶף", "ואלפא ואחדא", "and one thousand,"),
        ("שְׁבַע מֵאוֹת", "וסבע מאיה", "seven hundred"),
        ("וּשְׁלֹשִׁים", "ות'לאת'ין", "and thirty."),
    ],
    52: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses, addressing him.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to"),
        ("אֶל-מֹשֶׁה", "מוסי'", "Moses,"),
        ("לֵּאמֹר", "תכלימא", "addressing him."),
    ],
    53: [
        # HE: לָאֵלֶּה תֵּחָלֵק הָאָרֶץ בְּנַחֲלָה בְּמִסְפַּר שֵׁמוֹת
        # JA: ולהולאי יגב אן יקסם אלבלד נחלה. באחצא אסמאיהם
        # EN: 'To these it is required that the land be apportioned as an inheritance, by the count of their names.
        ("לָאֵלֶּה", "ולהולאי", "'To these"),
        (None, "יגב אן", "it is required that"),
        ("תֵּחָלֵק", "יקסם", "the land be apportioned"),
        ("הָאָרֶץ", "אלבלד", "as an inheritance,"),
        ("בְּנַחֲלָה", "נחלה", "by the count"),
        ("בְּמִסְפַּר שֵׁמוֹת", "באחצא אסמאיהם", "of their names"),
    ],
    54: [
        # HE: לָרַב תַּרְבֶּה נַחֲלָתוֹ וְלַמְעַט תַּמְעִיט נַחֲלָתוֹ אִישׁ לְפִי פְקֻדָיו יֻתַּן נַחֲלָתוֹ
        # JA: פלאלכתיר תכת'ר נחלתה. ולאלקליל תקללהא. כל סבט עלי' קדר עדדה. יעטא נחלתה
        # EN: To the numerous you shall enlarge his inheritance, and to the few you shall diminish his inheritance — each tribe according to the measure of its number shall its inheritance be given.
        ("לָרַב", "פלאלכתיר", "To the numerous"),
        ("תַּרְבֶּה", "תכת'ר", "you shall enlarge"),
        ("נַחֲלָתוֹ", "נחלתה", "his inheritance,"),
        ("וְלַמְעַט", "ולאלקליל", "and to the few"),
        ("תַּמְעִיט", "תקללהא", "you shall diminish his inheritance —"),
        ("אִישׁ", "כל סבט", "each tribe"),
        ("לְפִי פְקֻדָיו", "עלי' קדר עדדה", "according to the measure of its number"),
        ("יֻתַּן נַחֲלָתוֹ", "יעטא נחלתה", "shall its inheritance be given."),
    ],
    55: [
        # HE: אַךְ-בְּגוֹרָל יֵחָלֵק אֶת-הָאָרֶץ לִשְׁמוֹת מַטּוֹת-אֲבֹתָם יִנְחָלוּ
        # JA: לכן באסהם יקסם אלבלד. באסמא אסבאט אבאיהם
        # EN: But by lots shall the land be apportioned, by the names of the tribes of their fathers.
        ("אַךְ", "לכן", "But"),
        ("בְּגוֹרָל", "באסהם", "by lots"),
        ("יֵחָלֵק", "יקסם", "shall the land be apportioned,"),
        ("אֶת-הָאָרֶץ", "אלבלד", "by the names of"),
        ("לִשְׁמוֹת", "באסמא", "the tribes of"),
        ("מַטּוֹת-אֲבֹתָם", "אסבאט אבאיהם", "their fathers."),
    ],
    56: [
        # HE: עַל-פִּי הַגּוֹרָל תֵּחָלֵק נַחֲלָתוֹ בֵּין רַב לִמְעָט
        # JA: ועלי קדר אלסהם. תקסם נחלתהם. בין כת'יר. וקליל
        # EN: According to the measure of the lots shall their inheritance be apportioned, between the numerous and the few.'
        ("עַל-פִּי", "ועלי קדר", "According to the measure of"),
        ("הַגּוֹרָל", "אלסהם", "the lots"),
        ("תֵּחָלֵק", "תקסם", "shall their inheritance be apportioned,"),
        ("נַחֲלָתוֹ", "נחלתהם", "between the numerous"),
        ("בֵּין רַב לִמְעָט", "בין כת'יר. וקליל", "and the few.'"),
    ],
    57: [
        # HE: וְאֵלֶּה פְקוּדֵי הַלֵּוִי לְמִשְׁפְּחֹתָם לְגֵרְשׁוֹן מִשְׁפַּחַת הַגֵּרְשֻׁנִּי לִקְהָת מִשְׁפַּחַת הַקְּהָתִי לִמְרָרִי מִשְׁפַּחַת הַמְּרָרִי
        # JA: והד'ה אעדאד לוי לעשאירהם. עשירה' אלגרשוניין. ועשירה' אלקהתיין. ועשירה' אלמרריין
        # EN: And these are the counts of Levi by their clans: the clan of the Gershonites, and the clan of the Kohathites, and the clan of the Merarites.
        ("וְאֵלֶּה", "והד'ה", "And these are"),
        ("פְקוּדֵי הַלֵּוִי", "אעדאד לוי", "the counts of Levi"),
        ("לְמִשְׁפְּחֹתָם", "לעשאירהם", "by their clans:"),
        ("לְגֵרְשׁוֹן", "עשירה'", "the clan of"),
        ("מִשְׁפַּחַת הַגֵּרְשֻׁנִּי", "אלגרשוניין", "the Gershonites,"),
        ("לִקְהָת", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַקְּהָתִי", "אלקהתיין", "the Kohathites,"),
        ("לִמְרָרִי", "ועשירה'", "and the clan of"),
        ("מִשְׁפַּחַת הַמְּרָרִי", "אלמרריין", "the Merarites."),
    ],
    58: [
        # HE: אֵלֶּה מִשְׁפְּחֹת לֵוִי מִשְׁפַּחַת הַלִּבְנִי מִשְׁפַּחַת הַחֶבְרֹנִי מִשְׁפַּחַת הַמַּחְלִי מִשְׁפַּחַת הַמּוּשִׁי מִשְׁפַּחַת הַקָּרְחִי וּקְהָת הוֹלִד אֶת-עַמְרָם
        # JA: וסאיר עשאירהם. עשירה' אללבניין. ועשירה' אלחברוניין ועשירה' אלמחליין ועשירה' אלמושיין. ועשירה' אלקרחיין. ואולד קהת עמרם
        # EN: And the rest of their clans: the clan of the Libnites, and the clan of the Hebronites, and the clan of the Mahlites, and the clan of the Mushites, and the clan of the Korahites — and Kohath begot Amram.
        ("אֵלֶּה מִשְׁפְּחֹת לֵוִי", "וסאיר עשאירהם", "And the rest of their clans:"),
        ("מִשְׁפַּחַת הַלִּבְנִי", "עשירה' אללבניין", "the clan of the Libnites,"),
        ("מִשְׁפַּחַת הַחֶבְרֹנִי", "ועשירה' אלחברוניין", "and the clan of the Hebronites,"),
        ("מִשְׁפַּחַת הַמַּחְלִי", "ועשירה' אלמחליין", "and the clan of the Mahlites,"),
        ("מִשְׁפַּחַת הַמּוּשִׁי", "ועשירה' אלמושיין", "and the clan of the Mushites,"),
        ("מִשְׁפַּחַת הַקָּרְחִי", "ועשירה' אלקרחיין", "and the clan of the Korahites —"),
        ("וּקְהָת", "ואולד קהת", "and Kohath begot"),
        ("הוֹלִד אֶת-עַמְרָם", "עמרם", "Amram."),
    ],
    59: [
        # HE: וְשֵׁם אֵשֶׁת עַמְרָם יוֹכֶבֶד בַּת-לֵוִי אֲשֶׁר יָלְדָה אֹתָהּ לְלֵוִי בְּמִצְרָיִם וַתֵּלֶד לְעַמְרָם אֶת-אַהֲרֹן וְאֶת-מֹשֶׁה וְאֵת מִרְיָם אֲחֹתָם
        # JA: וכאן אסם זוגה' עמרם. יוכבד אבנה' לוי. אלד'י ולדת ללוי במצר. פולדת לעמרם. הרון ומוסי. ומרים אכ'תהם
        # EN: And the name of the wife of Amram was Jochebed, daughter of Levi, who was born to Levi in Egypt; and she bore to Amram: Aaron and Moses, and Miriam their sister.
        ("וְשֵׁם", "וכאן אסם", "And the name of"),
        ("אֵשֶׁת עַמְרָם", "זוגה' עמרם", "the wife of Amram"),
        ("יוֹכֶבֶד", "יוכבד", "was Jochebed,"),
        ("בַּת-לֵוִי", "אבנה' לוי", "daughter of Levi,"),
        ("אֲשֶׁר יָלְדָה", "אלד'י ולדת", "who was born"),
        ("לְלֵוִי", "ללוי", "to Levi"),
        ("בְּמִצְרָיִם", "במצר", "in Egypt;"),
        ("וַתֵּלֶד", "פולדת", "and she bore"),
        ("לְעַמְרָם", "לעמרם", "to Amram:"),
        ("אֶת-אַהֲרֹן", "הרון", "Aaron"),
        ("וְאֶת-מֹשֶׁה", "ומוסי", "and Moses,"),
        ("וְאֵת מִרְיָם", "ומרים", "and Miriam"),
        ("אֲחֹתָם", "אכ'תהם", "their sister."),
    ],
    60: [
        # HE: וַיִּוָּלֵד לְאַהֲרֹן אֶת-נָדָב וְאֶת-אֲבִיהוּא אֶת-אֶלְעָזָר וְאֶת-אִיתָמָר
        # JA: פולד להרון. נדב ואביהוא. אלעזר ואיתמר
        # EN: And there were born to Aaron: Nadab and Abihu, Eleazar and Ithamar.
        ("וַיִּוָּלֵד", "פולד", "And there were born"),
        ("לְאַהֲרֹן", "להרון", "to Aaron:"),
        ("אֶת-נָדָב", "נדב", "Nadab"),
        ("וְאֶת-אֲבִיהוּא", "ואביהוא", "and Abihu,"),
        ("אֶת-אֶלְעָזָר", "אלעזר", "Eleazar"),
        ("וְאֶת-אִיתָמָר", "ואיתמר", "and Ithamar."),
    ],
    61: [
        # HE: וַיָּמָת נָדָב וַאֲבִיהוּא בְּהַקְרִיבָם אֵשׁ-זָרָה לִפְנֵי יְהוָה
        # JA: פמאת נדב ואביהוא. חין קרבא נארא ג'ריבא בין ידי אללה
        # EN: And Nadab and Abihu died when the two of them offered strange fire before God.
        ("וַיָּמָת", "פמאת", "And Nadab"),
        ("נָדָב", "נדב", "and Abihu died"),
        ("וַאֲבִיהוּא", "ואביהוא", "when the two"),
        ("בְּהַקְרִיבָם", "חין קרבא", "of them offered"),
        ("אֵשׁ-זָרָה", "נארא ג'ריבא", "strange fire"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God."),
    ],
    62: [
        # HE: וַיִּהְיוּ פְקֻדֵיהֶם שְׁלֹשָׁה וְעֶשְׂרִים אֶלֶף כָּל-זָכָר מִבֶּן-חֹדֶשׁ וָמָעְלָה כִּי לֹא הָתְפָּקְדוּ בְּתוֹךְ בְּנֵי יִשְׂרָאֵל כִּי לֹא-נִתַּן לָהֶם נַחֲלָה בְּתוֹךְ בְּנֵי יִשְׂרָאֵל
        # JA: פכאן עדדהם. ת'לאת'ה ועשרין אלפא. כל ד'כר מן אבן שהר פצאעדא. אד' לם יעדו. פי גמלה' בני אסראיל. אד' לם יעטו נחלה פי וסטהם
        # EN: And their count was twenty-three thousand — every male from a month of age and upward; since they were not counted among the total of the sons of Israel, since no inheritance was given to them in their midst.
        ("וַיִּהְיוּ פְקֻדֵיהֶם", "פכאן עדדהם", "And their count"),
        ("שְׁלֹשָׁה", "ת'לאת'ה", "was twenty-three"),
        ("וְעֶשְׂרִים אֶלֶף", "ועשרין אלפא", "thousand —"),
        ("כָּל-זָכָר", "כל ד'כר", "every male"),
        ("מִבֶּן-חֹדֶשׁ", "מן אבן שהר", "from a month of age"),
        ("וָמָעְלָה", "פצאעדא", "and upward;"),
        ("כִּי לֹא הָתְפָּקְדוּ", "אד' לם יעדו", "since they were not counted"),
        ("בְּתוֹךְ בְּנֵי יִשְׂרָאֵל", "פי גמלה' בני אסראיל", "among the total of the sons of Israel,"),
        ("כִּי לֹא-נִתַּן לָהֶם נַחֲלָה", "אד' לם יעטו נחלה", "since no inheritance was given to them"),
        ("בְּתוֹךְ בְּנֵי יִשְׂרָאֵל", "פי וסטהם", "in their midst."),
    ],
    63: [
        # HE: אֵלֶּה פְּקוּדֵי מֹשֶׁה וְאֶלְעָזָר הַכֹּהֵן אֲשֶׁר פָּקְדוּ אֶת-בְּנֵי יִשְׂרָאֵל בְּעַרְבֹת מוֹאָב עַל יַרְדֵּן יְרֵחוֹ
        # JA: הולאי מעדודי מוסי'. ואלעזר אלאמאם. אלד'י עדא בני אסראיל. פי בידאת מואב. עלי' ארדן יריחא
        # EN: These are the counts of Moses and Eleazar the priest, who counted the sons of Israel in the wilderness plain of Moab, by the Jordan of Jericho.
        ("אֵלֶּה", "הולאי", "These are"),
        ("פְּקוּדֵי מֹשֶׁה", "מעדודי מוסי'", "the counts of Moses"),
        ("וְאֶלְעָזָר", "ואלעזר", "and Eleazar"),
        ("הַכֹּהֵן", "אלאמאם", "the priest,"),
        ("אֲשֶׁר פָּקְדוּ", "אלד'י עדא", "who counted"),
        ("אֶת-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("בְּעַרְבֹת", "פי בידאת", "in the wilderness plain of"),
        ("מוֹאָב", "מואב", "Moab,"),
        ("עַל יַרְדֵּן", "עלי' ארדן", "by the Jordan of"),
        ("יְרֵחוֹ", "יריחא", "Jericho."),
    ],
    64: [
        # HE: וּבְאֵלֶּה לֹא-הָיָה אִישׁ מִפְּקוּדֵי מֹשֶׁה וְאַהֲרֹן הַכֹּהֵן אֲשֶׁר פָּקְדוּ אֶת-בְּנֵי יִשְׂרָאֵל בְּמִדְבַּר סִינָי
        # JA: ופי הולאי לם יכון רגל. מן מעדודי מוסי'. והרון אלאמאם. אלד'י עדא בני אסראיל פי ברייה' סיני
        # EN: And among these there was not a man from among those counted by Moses and Aaron the priest, who had counted the sons of Israel in the wilderness of Sinai —
        ("וּבְאֵלֶּה", "ופי הולאי", "And among these"),
        ("לֹא-הָיָה אִישׁ", "לם יכון רגל", "there was not a man"),
        ("מִפְּקוּדֵי מֹשֶׁה", "מן מעדודי מוסי'", "from among those counted by Moses"),
        ("וְאַהֲרֹן", "והרון", "and Aaron"),
        ("הַכֹּהֵן", "אלאמאם", "the priest,"),
        ("אֲשֶׁר פָּקְדוּ", "אלד'י עדא", "who had counted"),
        ("אֶת-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("בְּמִדְבַּר סִינָי", "פי ברייה' סיני", "in the wilderness of Sinai —"),
    ],
    65: [
        # HE: כִּי-אָמַר יְהוָה לָהֶם מוֹת יָמֻתוּ בַּמִּדְבָּר וְלֹא-נוֹתַר מֵהֶם אִישׁ כִּי אִם-כָּלֵב בֶּן-יְפֻנֶּה וִיהוֹשֻׁעַ בִּן-נוּן
        # JA: לאן אללה חכם עליהם. אן יתמאותון פי אלברייה. ולם יבק מנהם רגל. אלא כלב אבן יפנה. ויהושע אבן נון
        # EN: for God had decreed upon them that they should die one by one in the wilderness; and not a man remained of them, save Caleb son of Jephunneh, and Joshua son of Nun.
        ("כִּי-אָמַר", "לאן", "for"),
        ("יְהוָה", "אללה", "God"),
        ("לָהֶם", "חכם עליהם", "had decreed upon them"),
        ("מוֹת יָמֻתוּ", "אן יתמאותון", "that they should die one by one"),
        ("בַּמִּדְבָּר", "פי אלברייה", "in the wilderness;"),
        ("וְלֹא-נוֹתַר", "ולם יבק", "and not a man remained"),
        ("מֵהֶם אִישׁ", "מנהם רגל", "of them,"),
        ("כִּי אִם-כָּלֵב", "אלא כלב", "save Caleb"),
        ("בֶּן-יְפֻנֶּה", "אבן יפנה", "son of Jephunneh,"),
        ("וִיהוֹשֻׁעַ", "ויהושע", "and Joshua"),
        ("בִּן-נוּן", "אבן נון", "son of Nun."),
    ],
}

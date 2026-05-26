"""Hand-authored word-level alignment triples for Bamidbar chapter 17."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי' תכלימא", "directly."),
    ],
    2: [
        # HE: אֱמֹר אֶל-אֶלְעָזָר בֶּן-אַהֲרֹן הַכֹּהֵן וְיָרֵם אֶת-הַמַּחְתֹּת מִבֵּין הַשְּׂרֵפָה וְאֶת-הָאֵשׁ זְרֵה-הָלְאָה כִּי קָדֵשׁוּ
        # JA: מר אלעזר אבן הרון אלאמאם. באן ירפע אלמגאמר מן בין אלמחרקין. ויד'רי אלנאר הנאך. לאנהא קד תקדסת
        # EN: Command Eleazar son of Aaron the priest, that he lift the fire-pans from among the burned ones, and scatter the fire there — for they have become consecrated.
        ("אֱמֹר", "מר", "Command"),
        ("אֶל-אֶלְעָזָר", "אלעזר", "Eleazar"),
        ("בֶּן-אַהֲרֹן", "אבן הרון", "son of Aaron"),
        ("הַכֹּהֵן", "אלאמאם", "the priest,"),
        ("וְיָרֵם", "באן ירפע", "that he lift"),
        ("אֶת-הַמַּחְתֹּת", "אלמגאמר", "the fire-pans"),
        ("מִבֵּין הַשְּׂרֵפָה", "מן בין אלמחרקין", "from among the burned ones,"),
        ("וְאֶת-הָאֵשׁ", "ויד'רי אלנאר", "and scatter the fire"),
        ("זְרֵה-הָלְאָה", "הנאך", "there —"),
        ("כִּי קָדֵשׁוּ", "לאנהא קד תקדסת", "for they have become consecrated."),
    ],
    3: [
        # HE: אֵת מַחְתּוֹת הַחַטָּאִים הָאֵלֶּה בְּנַפְשֹׁתָם וְעָשׂוּ אֹתָם רִקֻּעֵי פַחִים צִפּוּי לַמִּזְבֵּחַ--כִּי-הִקְרִיבֻם לִפְנֵי-יְהוָה וַיִּקְדָּשׁוּ וְיִהְיוּ לְאוֹת לִבְנֵי יִשְׂרָאֵל
        # JA: אמא מגאמר הולאי אלמכ'טיין עלי' נפוסהם. פיצנעוהא צפאיחא רקאק ג'שאא לאלמד'בח. פאנהא למא קדמוהא בין ידי אללה קד תקדסת. ותציר עלאמה לבני אסראיל
        # EN: As for the fire-pans of these men who sinned against their own souls, let them be made into thin beaten plates, a covering for the altar — for since they presented them before God they have become consecrated, and they shall be a sign for the sons of Israel.
        ("אֵת מַחְתּוֹת", "אמא מגאמר", "As for the fire-pans of"),
        ("הַחַטָּאִים הָאֵלֶּה", "הולאי אלמכ'טיין", "these men who sinned"),
        ("בְּנַפְשֹׁתָם", "עלי' נפוסהם", "against their own souls,"),
        ("וְעָשׂוּ אֹתָם", "פיצנעוהא", "let them be made into"),
        ("רִקֻּעֵי פַחִים", "צפאיחא רקאק", "thin beaten plates,"),
        ("צִפּוּי לַמִּזְבֵּחַ", "ג'שאא לאלמד'בח", "a covering for the altar —"),
        ("כִּי-הִקְרִיבֻם", "פאנהא למא קדמוהא", "for since they presented them"),
        ("לִפְנֵי-יְהוָה", "בין ידי אללה", "before God"),
        ("וַיִּקְדָּשׁוּ", "קד תקדסת", "they have become consecrated,"),
        ("וְיִהְיוּ לְאוֹת", "ותציר עלאמה", "and they shall be a sign"),
        ("לִבְנֵי יִשְׂרָאֵל", "לבני אסראיל", "for the sons of Israel."),
    ],
    4: [
        # HE: וַיִּקַּח אֶלְעָזָר הַכֹּהֵן אֵת מַחְתּוֹת הַנְּחֹשֶׁת אֲשֶׁר הִקְרִיבוּ הַשְּׂרֻפִים וַיְרַקְּעוּם צִפּוּי לַמִּזְבֵּחַ
        # JA: פאכ'ד' אלעזר אלאמאם. מגאמר אלנחאס. אלד'י קדמוהא אלמחרקין. פארקוהא צפאיחא לאלמד'בח
        # EN: And Eleazar the priest took the copper fire-pans which the burned ones had presented, and they beat them into plates for the altar —
        ("וַיִּקַּח אֶלְעָזָר", "פאכ'ד' אלעזר", "And Eleazar"),
        ("הַכֹּהֵן", "אלאמאם", "the priest took"),
        ("אֵת מַחְתּוֹת הַנְּחֹשֶׁת", "מגאמר אלנחאס", "the copper fire-pans"),
        ("אֲשֶׁר הִקְרִיבוּ הַשְּׂרֻפִים", "אלד'י קדמוהא אלמחרקין", "which the burned ones had presented,"),
        ("וַיְרַקְּעוּם", "פארקוהא", "and they beat them into"),
        ("צִפּוּי לַמִּזְבֵּחַ", "צפאיחא לאלמד'בח", "plates for the altar —"),
    ],
    5: [
        # HE: זִכָּרוֹן לִבְנֵי יִשְׂרָאֵל לְמַעַן אֲשֶׁר לֹא-יִקְרַב אִישׁ זָר אֲשֶׁר לֹא מִזֶּרַע אַהֲרֹן הוּא לְהַקְטִיר קְטֹרֶת לִפְנֵי יְהוָה וְלֹא-יִהְיֶה כְקֹרַח וְכַעֲדָתוֹ כַּאֲשֶׁר דִּבֶּר יְהוָה בְּיַד-מֹשֶׁה לוֹ
        # JA: ד'כרא לבני אסראיל. לכי לא יתקדם רגל אגנבי. מן ליס הו מן נסל הרון. ליבכ'ר בכ'ורא בין ידי אללה. ולא יכון כקרח וכגמועה. כמא נזל אללה. עלי' יד מוסי פיה
        # EN: a memorial for the sons of Israel, so that no outsider who is not of the lineage of Aaron shall draw near to burn incense before God, and that none be like Korah and his assembly — as God laid down by the hand of Moses concerning him.
        ("זִכָּרוֹן", "ד'כרא", "a memorial"),
        ("לִבְנֵי יִשְׂרָאֵל", "לבני אסראיל", "for the sons of Israel,"),
        ("לְמַעַן אֲשֶׁר לֹא-יִקְרַב", "לכי לא יתקדם", "so that no"),
        ("אִישׁ זָר", "רגל אגנבי", "outsider"),
        ("אֲשֶׁר לֹא מִזֶּרַע אַהֲרֹן", "מן ליס הו מן נסל הרון", "who is not of the lineage of Aaron"),
        ("לְהַקְטִיר קְטֹרֶת", "ליבכ'ר בכ'ורא", "shall draw near to burn incense"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God,"),
        ("וְלֹא-יִהְיֶה כְקֹרַח", "ולא יכון כקרח", "and that none be like Korah"),
        ("וְכַעֲדָתוֹ", "וכגמועה", "and his assembly —"),
        ("כַּאֲשֶׁר דִּבֶּר יְהוָה", "כמא נזל אללה", "as God laid down"),
        ("בְּיַד-מֹשֶׁה", "עלי' יד מוסי", "by the hand of Moses"),
        ("לוֹ", "פיה", "concerning him."),
    ],
    6: [
        # HE: וַיִּלֹּנוּ כָּל-עֲדַת בְּנֵי-יִשְׂרָאֵל מִמָּחֳרָת עַל-מֹשֶׁה וְעַל-אַהֲרֹן לֵאמֹר אַתֶּם הֲמִתֶּם אֶת-עַם יְהוָה
        # JA: פתד'מר. גמאעה' בני אסראיל מן ג'ד. עלי' מוסי' והרון קאילין. אנתמא קתלתמא מן אמה' אללה
        # EN: And the whole congregation of the sons of Israel complained on the next day against Moses and Aaron, saying: 'You two have killed from the nation of God.'
        ("וַיִּלֹּנוּ", "פתד'מר", "And"),
        ("כָּל-עֲדַת", "גמאעה'", "the whole congregation of"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("מִמָּחֳרָת", "מן ג'ד", "complained on the next day"),
        ("עַל-מֹשֶׁה", "עלי' מוסי'", "against Moses"),
        ("וְעַל-אַהֲרֹן", "והרון", "and Aaron,"),
        ("לֵאמֹר", "קאילין", "saying:"),
        ("אַתֶּם הֲמִתֶּם", "אנתמא קתלתמא", "'You two have killed"),
        ("אֶת-עַם יְהוָה", "מן אמה' אללה", "from the nation of God.'"),
    ],
    7: [
        # HE: וַיְהִי בְּהִקָּהֵל הָעֵדָה עַל-מֹשֶׁה וְעַל-אַהֲרֹן וַיִּפְנוּ אֶל-אֹהֶל מוֹעֵד וְהִנֵּה כִסָּהוּ הֶעָנָן וַיֵּרָא כְּבוֹד יְהוָה
        # JA: פלמא תגווקו עליהמא אלתפתו אלי' כ'בא אלמחצ'ר. פאד'א בנור אללה. צהר פי אלג'מאם
        # EN: And when they had gathered against the two of them, they turned toward the tent of the assembly — and behold, the light of God appeared in the cloud.
        ("וַיְהִי בְּהִקָּהֵל הָעֵדָה", "פלמא תגווקו", "And when they had gathered"),
        ("עַל-מֹשֶׁה וְעַל-אַהֲרֹן", "עליהמא", "against the two of them,"),
        ("וַיִּפְנוּ", "אלתפתו", "they turned"),
        ("אֶל-אֹהֶל מוֹעֵד", "אלי' כ'בא אלמחצ'ר", "toward the tent of the assembly —"),
        ("וְהִנֵּה", "פאד'א", "and behold,"),
        ("כְּבוֹד יְהוָה", "בנור אללה", "the light of God"),
        ("וַיֵּרָא", "צהר", "appeared"),
        ("כִסָּהוּ הֶעָנָן", "פי אלג'מאם", "in the cloud."),
    ],
    8: [
        # HE: וַיָּבֹא מֹשֶׁה וְאַהֲרֹן אֶל-פְּנֵי אֹהֶל מוֹעֵד
        # JA: פתקדם מוסי' והרון. בין ידי כ'בא אלמחצ'ר
        # EN: And Moses and Aaron came forward before the tent of the assembly.
        ("וַיָּבֹא", "פתקדם", "And"),
        ("מֹשֶׁה", "מוסי'", "Moses"),
        ("וְאַהֲרֹן", "והרון", "and Aaron"),
        ("אֶל-פְּנֵי", "בין ידי", "came forward before"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly."),
    ],
    9: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה. מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי' תכלימא", "directly."),
    ],
    10: [
        # HE: הֵרֹמּוּ מִתּוֹךְ הָעֵדָה הַזֹּאת וַאֲכַלֶּה אֹתָם כְּרָגַע וַיִּפְּלוּ עַל-פְּנֵיהֶם
        # JA: אן ארתפעתם מן בין הד'א אלגמאעה. אפניתהם כטרפה. פוקעא עלי' וגוההמא
        # EN: 'If you remove yourselves from among this congregation, I shall destroy them in the twinkling of an eye.' And the two of them fell upon their faces.
        ("הֵרֹמּוּ", "אן ארתפעתם", "'If you remove yourselves"),
        ("מִתּוֹךְ", "מן בין", "from among"),
        ("הָעֵדָה הַזֹּאת", "הד'א אלגמאעה", "this congregation,"),
        ("וַאֲכַלֶּה אֹתָם", "אפניתהם", "I shall destroy them"),
        ("כְּרָגַע", "כטרפה", "in the twinkling of an eye.'"),
        ("וַיִּפְּלוּ עַל-פְּנֵיהֶם", "פוקעא עלי' וגוההמא", "And the two of them fell upon their faces."),
    ],
    11: [
        # HE: וַיֹּאמֶר מֹשֶׁה אֶל-אַהֲרֹן קַח אֶת-הַמַּחְתָּה וְתֶן-עָלֶיהָ אֵשׁ מֵעַל הַמִּזְבֵּחַ וְשִׂים קְטֹרֶת וְהוֹלֵךְ מְהֵרָה אֶל-הָעֵדָה וְכַפֵּר עֲלֵיהֶם כִּי-יָצָא הַקֶּצֶף מִלִּפְנֵי יְהוָה הֵחֵל הַנָּגֶף
        # JA: פקאל מוסי' להרון. כ'ד' אלמגמרה. ואגעל עליהא נארא. מן פוק אלמד'בח ואלקי בכורא. ואד'הב בה מסרעא. אלי' אלגמאעה ואסתג'פר ענהם. פאן אלסכ'ט. קד כ'רג מן בין ידי אללה. וקד בדא בהם אלצדאם
        # EN: And Moses said to Aaron: 'Take the fire-pan, and place upon it fire from the altar, and cast incense upon it, and go with it quickly to the congregation, and seek forgiveness for them — for the wrath has gone forth from before God, and the plague has already begun among them.'
        ("וַיֹּאמֶר מֹשֶׁה", "פקאל מוסי'", "And Moses said"),
        ("אֶל-אַהֲרֹן", "להרון", "to Aaron:"),
        ("קַח אֶת-הַמַּחְתָּה", "כ'ד' אלמגמרה", "'Take the fire-pan,"),
        ("וְתֶן-עָלֶיהָ אֵשׁ", "ואגעל עליהא נארא", "and place upon it fire"),
        ("מֵעַל הַמִּזְבֵּחַ", "מן פוק אלמד'בח", "from the altar,"),
        ("וְשִׂים קְטֹרֶת", "ואלקי בכורא", "and cast incense upon it,"),
        ("וְהוֹלֵךְ מְהֵרָה", "ואד'הב בה מסרעא", "and go with it quickly"),
        ("אֶל-הָעֵדָה", "אלי' אלגמאעה", "to the congregation,"),
        ("וְכַפֵּר עֲלֵיהֶם", "ואסתג'פר ענהם", "and seek forgiveness for them —"),
        ("כִּי-יָצָא הַקֶּצֶף", "פאן אלסכ'ט", "for the wrath"),
        ("מִלִּפְנֵי יְהוָה", "קד כ'רג מן בין ידי אללה", "has gone forth from before God,"),
        ("הֵחֵל הַנָּגֶף", "וקד בדא בהם אלצדאם", "and the plague has already begun among them.'"),
    ],
    12: [
        # HE: וַיִּקַּח אַהֲרֹן כַּאֲשֶׁר דִּבֶּר מֹשֶׁה וַיָּרָץ אֶל-תּוֹךְ הַקָּהָל וְהִנֵּה הֵחֵל הַנֶּגֶף בָּעָם וַיִּתֵּן אֶת-הַקְּטֹרֶת וַיְכַפֵּר עַל-הָעָם
        # JA: פאכ'ד' ד'אלך הרון. כמא קאל מוסי. וחאצ'ר אלי' וסט אלגוק. פאד'א באלובא קד אבתדא בהם. פבכ'ר אלבכור. ואסתג'פר ענהם
        # EN: And Aaron took it, just as Moses had said, and he came to the midst of the assembly — and behold, the pestilence had already begun among them; and he burned the incense, and sought forgiveness for them.
        ("וַיִּקַּח אַהֲרֹן", "פאכ'ד' ד'אלך הרון", "And Aaron took it,"),
        ("כַּאֲשֶׁר דִּבֶּר מֹשֶׁה", "כמא קאל מוסי", "just as Moses had said,"),
        ("וַיָּרָץ", "וחאצ'ר", "and he came"),
        ("אֶל-תּוֹךְ הַקָּהָל", "אלי' וסט אלגוק", "to the midst of the assembly —"),
        ("וְהִנֵּה הֵחֵל הַנֶּגֶף בָּעָם", "פאד'א באלובא קד אבתדא בהם", "and behold, the pestilence had already begun among them;"),
        ("וַיִּתֵּן אֶת-הַקְּטֹרֶת", "פבכ'ר אלבכור", "and he burned the incense,"),
        ("וַיְכַפֵּר עַל-הָעָם", "ואסתג'פר ענהם", "and sought forgiveness for them."),
    ],
    13: [
        # HE: וַיַּעֲמֹד בֵּין-הַמֵּתִים וּבֵין הַחַיִּים וַתֵּעָצַר הַמַּגֵּפָה
        # JA: פוקף בין אלמותא ואלאחיא. ואנחבס אלובא
        # EN: And he stood between the dead and the living, and the pestilence was held back.
        ("וַיַּעֲמֹד", "פוקף", "And he stood"),
        ("בֵּין-הַמֵּתִים", "בין אלמותא", "between the dead"),
        ("וּבֵין הַחַיִּים", "ואלאחיא", "and the living,"),
        ("וַתֵּעָצַר הַמַּגֵּפָה", "ואנחבס אלובא", "and the pestilence was held back."),
    ],
    14: [
        # HE: וַיִּהְיוּ הַמֵּתִים בַּמַּגֵּפָה אַרְבָּעָה עָשָׂר אֶלֶף וּשְׁבַע מֵאוֹת--מִלְּבַד הַמֵּתִים עַל-דְּבַר-קֹרַח
        # JA: פכאן עדד מן מאת בד'אלך אלובא. ארבעה' עשר אלף וסבע מאיה. סוא מן מאת בסבב קרח
        # EN: And the number of those who died in that pestilence was fourteen thousand and seven hundred — besides those who died on account of Korah.
        ("וַיִּהְיוּ הַמֵּתִים", "פכאן עדד מן מאת", "And the number of those who died"),
        ("בַּמַּגֵּפָה", "בד'אלך אלובא", "in that pestilence"),
        ("אַרְבָּעָה עָשָׂר אֶלֶף", "ארבעה' עשר אלף", "was fourteen thousand"),
        ("וּשְׁבַע מֵאוֹת", "וסבע מאיה", "and seven hundred —"),
        ("מִלְּבַד הַמֵּתִים", "סוא מן מאת", "besides those who died"),
        ("עַל-דְּבַר-קֹרַח", "בסבב קרח", "on account of Korah."),
    ],
    15: [
        # HE: וַיָּשָׁב אַהֲרֹן אֶל-מֹשֶׁה אֶל-פֶּתַח אֹהֶל מוֹעֵד וְהַמַּגֵּפָה נֶעֱצָרָה
        # JA: פרגע הרון אלי' מוסי. אלי' באב כ'בא אלמחצ'ר. וקד אנחבס אלובא
        # EN: Then Aaron returned to Moses, to the entrance of the tent of the assembly, and the pestilence had been held back.
        ("וַיָּשָׁב", "פרגע", "Then"),
        ("אַהֲרֹן", "הרון", "Aaron returned"),
        ("אֶל-מֹשֶׁה", "אלי' מוסי", "to Moses,"),
        ("אֶל-פֶּתַח", "אלי' באב", "to the entrance of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly,"),
        ("וְהַמַּגֵּפָה נֶעֱצָרָה", "וקד אנחבס אלובא", "and the pestilence had been held back."),
    ],
    16: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי' תכלימא", "directly."),
    ],
    17: [
        # HE: דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְקַח מֵאִתָּם מַטֶּה מַטֶּה לְבֵית אָב מֵאֵת כָּל-נְשִׂיאֵהֶם לְבֵית אֲבֹתָם--שְׁנֵים עָשָׂר מַטּוֹת אִישׁ אֶת-שְׁמוֹ תִּכְתֹּב עַל-מַטֵּהוּ
        # JA: מר בני אסראיל. וכ'ד' מנהם. עצא עצא לכל בית אב. מן אשראפהם לביות אבאיהם. את'ני עשר עצא. ואכתב אסם כל רגל עלי' עצאה
        # EN: 'Command the sons of Israel, and take from them a staff, one staff for each father's house, from their nobles, for the houses of their fathers — twelve staves; and write the name of each man upon his staff.
        ("דַּבֵּר", "מר", "'Command"),
        ("אֶל-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("וְקַח", "וכ'ד'", "and take"),
        ("מֵאִתָּם", "מנהם", "from them"),
        ("מַטֶּה מַטֶּה", "עצא עצא", "a staff, one staff"),
        ("לְבֵית אָב", "לכל בית אב", "for each father's house,"),
        ("מֵאֵת כָּל-נְשִׂיאֵהֶם", "מן אשראפהם", "from their nobles,"),
        ("לְבֵית אֲבֹתָם", "לביות אבאיהם", "for the houses of their fathers —"),
        ("שְׁנֵים עָשָׂר מַטּוֹת", "את'ני עשר עצא", "twelve staves;"),
        ("אִישׁ אֶת-שְׁמוֹ תִּכְתֹּב", "ואכתב אסם כל רגל", "and write the name of each man"),
        ("עַל-מַטֵּהוּ", "עלי' עצאה", "upon his staff."),
    ],
    18: [
        # HE: וְאֵת שֵׁם אַהֲרֹן תִּכְתֹּב עַל-מַטֵּה לֵוִי כִּי מַטֶּה אֶחָד לְרֹאשׁ בֵּית אֲבוֹתָם
        # JA: ואסם הרון. אכתב עלי' עצא לוי. אנך אנמא תאכ'ד' עצא ואחד. לגמלה' ביות אבאיהם
        # EN: And Aaron's name — write it upon the staff of Levi; for you are to take but one staff for the whole body of the houses of their fathers.'
        ("וְאֵת שֵׁם אַהֲרֹן", "ואסם הרון", "And Aaron's name —"),
        ("תִּכְתֹּב", "אכתב", "write it"),
        ("עַל-מַטֵּה לֵוִי", "עלי' עצא לוי", "upon the staff of Levi;"),
        ("כִּי", "אנך", "for"),
        ("מַטֶּה אֶחָד", "אנמא תאכ'ד' עצא ואחד", "you are to take but one staff"),
        ("לְרֹאשׁ בֵּית אֲבוֹתָם", "לגמלה' ביות אבאיהם", "for the whole body of the houses of their fathers.'"),
    ],
    19: [
        # HE: וְהִנַּחְתָּם בְּאֹהֶל מוֹעֵד--לִפְנֵי הָעֵדוּת אֲשֶׁר אִוָּעֵד לָכֶם שָׁמָּה
        # JA: וצ'עהא פי כ'בא אלמחצ'ר. בין ידי אלשהאדה. אלד'י אחצ'רך הנאך
        # EN: 'And place them in the tent of the assembly, before the testimony, where I shall meet you there.'
        ("וְהִנַּחְתָּם", "וצ'עהא", "'And place them"),
        ("בְּאֹהֶל מוֹעֵד", "פי כ'בא אלמחצ'ר", "in the tent of the assembly,"),
        ("לִפְנֵי הָעֵדוּת", "בין ידי אלשהאדה", "before the testimony,"),
        ("אֲשֶׁר אִוָּעֵד לָכֶם", "אלד'י אחצ'רך", "where I shall meet you"),
        ("שָׁמָּה", "הנאך", "there.'"),
    ],
    20: [
        # HE: וְהָיָה הָאִישׁ אֲשֶׁר אֶבְחַר-בּוֹ--מַטֵּהוּ יִפְרָח וַהֲשִׁכֹּתִי מֵעָלַי אֶת-תְּלֻנּוֹת בְּנֵי יִשְׂרָאֵל אֲשֶׁר הֵם מַלִּינִם עֲלֵיכֶם
        # JA: פאלרג'ל אלד'י אכ'תארה תפרע עצאה. חתא אהדי עני. תדמר בני אסראיל. אלד'י הם מתד'מרין עליכם
        # EN: 'And the man whom I shall choose — his staff shall put forth branches, so that I may quiet away from Me the complaining of the sons of Israel, which they are complaining against you.'
        ("וְהָיָה הָאִישׁ", "פאלרג'ל", "'And the man"),
        ("אֲשֶׁר אֶבְחַר-בּוֹ", "אלד'י אכ'תארה", "whom I shall choose —"),
        ("מַטֵּהוּ יִפְרָח", "תפרע עצאה", "his staff shall put forth branches,"),
        ("וַהֲשִׁכֹּתִי מֵעָלַי", "חתא אהדי עני", "so that I may quiet away from Me"),
        ("אֶת-תְּלֻנּוֹת", "תדמר", "the complaining of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("אֲשֶׁר הֵם מַלִּינִם", "אלד'י הם מתד'מרין", "which they are complaining"),
        ("עֲלֵיכֶם", "עליכם", "against you.'"),
    ],
    21: [
        # HE: וַיְדַבֵּר מֹשֶׁה אֶל-בְּנֵי יִשְׂרָאֵל וַיִּתְּנוּ אֵלָיו כָּל-נְשִׂיאֵיהֶם מַטֶּה לְנָשִׂיא אֶחָד מַטֶּה לְנָשִׂיא אֶחָד לְבֵית אֲבֹתָם--שְׁנֵים עָשָׂר מַטּוֹת וּמַטֵּה אַהֲרֹן בְּתוֹךְ מַטּוֹתָם
        # JA: פכלם מוסי' בדאלך בני אסראיל. פדפע אליה כל אשראפהם. עצא מן כל שריף לביות אבאיהם. את'ני עשר עצא. ועצא הרון פי מא בין עציהם
        # EN: And Moses spoke this to the sons of Israel, and all their nobles gave to him a staff, one staff for each noble, for the houses of their fathers — twelve staves; and Aaron's staff was among their staves.
        ("וַיְדַבֵּר מֹשֶׁה", "פכלם מוסי'", "And Moses spoke"),
        (None, "בדאלך", "this"),
        ("אֶל-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "to the sons of Israel,"),
        ("וַיִּתְּנוּ אֵלָיו כָּל-נְשִׂיאֵיהֶם", "פדפע אליה כל אשראפהם", "and all their nobles gave to him"),
        ("מַטֶּה לְנָשִׂיא אֶחָד", "עצא מן כל שריף", "a staff, one staff for each noble,"),
        ("לְבֵית אֲבֹתָם", "לביות אבאיהם", "for the houses of their fathers —"),
        ("שְׁנֵים עָשָׂר מַטּוֹת", "את'ני עשר עצא", "twelve staves;"),
        ("וּמַטֵּה אַהֲרֹן", "ועצא הרון", "and Aaron's staff"),
        ("בְּתוֹךְ מַטּוֹתָם", "פי מא בין עציהם", "was among their staves."),
    ],
    22: [
        # HE: וַיַּנַּח מֹשֶׁה אֶת-הַמַּטֹּת לִפְנֵי יְהוָה בְּאֹהֶל הָעֵדֻת
        # JA: פוצ'עהא מוסי' בין ידי אללה. פי כ'בא אלשהאדה
        # EN: And Moses placed them before God, in the tent of the testimony.
        ("וַיַּנַּח מֹשֶׁה", "פוצ'עהא מוסי'", "And Moses placed them"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God,"),
        ("בְּאֹהֶל הָעֵדֻת", "פי כ'בא אלשהאדה", "in the tent of the testimony."),
    ],
    23: [
        # HE: וַיְהִי מִמָּחֳרָת וַיָּבֹא מֹשֶׁה אֶל-אֹהֶל הָעֵדוּת וְהִנֵּה פָּרַח מַטֵּה-אַהֲרֹן לְבֵית לֵוִי וַיֹּצֵא פֶרַח וַיָּצֵץ צִיץ וַיִּגְמֹל שְׁקֵדִים
        # JA: ולמא כאן מן ג'ד. דכ'ל מוסי אלי' כ'בא אלשהאדה. פאד'א קד פרעת עצא הרון אלתי הי לבית לוי. פאכ'רגת פרועא ונוורת נוארא. ועקדת לוזא
        # EN: And when the next day came, Moses entered the tent of the testimony — and behold, the staff of Aaron, which was for the house of Levi, had put forth branches: it had brought out branches, and had burst into blossom, and had formed almonds.
        ("וַיְהִי מִמָּחֳרָת", "ולמא כאן מן ג'ד", "And when the next day came,"),
        ("וַיָּבֹא מֹשֶׁה", "דכ'ל מוסי", "Moses entered"),
        ("אֶל-אֹהֶל הָעֵדוּת", "אלי' כ'בא אלשהאדה", "the tent of the testimony —"),
        ("וְהִנֵּה פָּרַח מַטֵּה-אַהֲרֹן", "פאד'א קד פרעת עצא הרון", "and behold, the staff of Aaron"),
        ("לְבֵית לֵוִי", "אלתי הי לבית לוי", "which was for the house of Levi, had put forth branches:"),
        ("וַיֹּצֵא פֶרַח", "פאכ'רגת פרועא", "it had brought out branches,"),
        ("וַיָּצֵץ צִיץ", "ונוורת נוארא", "and had burst into blossom,"),
        ("וַיִּגְמֹל שְׁקֵדִים", "ועקדת לוזא", "and had formed almonds."),
    ],
    24: [
        # HE: וַיֹּצֵא מֹשֶׁה אֶת-כָּל-הַמַּטֹּת מִלִּפְנֵי יְהוָה אֶל-כָּל-בְּנֵי יִשְׂרָאֵל וַיִּרְאוּ וַיִּקְחוּ אִישׁ מַטֵּהוּ
        # JA: פאכ'רג מוסי. גמיע אלעצי מן בין ידי אללה. אלי' גמיע בני אסראיל. פנצ'ר כל ואחד אלי' עצאה פאכ'ד'הא
        # EN: And Moses brought out all the staves from before God to all the sons of Israel, and each one looked at his own staff and took it.
        ("וַיֹּצֵא מֹשֶׁה", "פאכ'רג מוסי", "And Moses brought out"),
        ("אֶת-כָּל-הַמַּטֹּת", "גמיע אלעצי", "all the staves"),
        ("מִלִּפְנֵי יְהוָה", "מן בין ידי אללה", "from before God"),
        ("אֶל-כָּל-בְּנֵי יִשְׂרָאֵל", "אלי' גמיע בני אסראיל", "to all the sons of Israel,"),
        ("וַיִּרְאוּ", "פנצ'ר כל ואחד", "and each one looked"),
        ("וַיִּקְחוּ אִישׁ מַטֵּהוּ", "אלי' עצאה פאכ'ד'הא", "at his own staff and took it."),
    ],
    25: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה הָשֵׁב אֶת-מַטֵּה אַהֲרֹן לִפְנֵי הָעֵדוּת לְמִשְׁמֶרֶת לְאוֹת לִבְנֵי-מֶרִי וּתְכַל תְּלוּנֹּתָם מֵעָלַי וְלֹא יָמֻתוּ
        # JA: ת'ם קאל אללה למוסי'. רד עצא הרון בין ידי אלשהאדה. תכון חפץ' עלאמה לד'וי אלכ'לף פיפנא תד'מרהם עליי ולא יהלכון
        # EN: Then God said to Moses: 'Return Aaron's staff before the testimony, to be kept as a sign for those who are rebellious, that their complaining against Me may be brought to an end, and they shall not perish.'
        (None, "ת'ם", "Then"),
        ("וַיֹּאמֶר יְהוָה", "קאל אללה", "God said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses:"),
        ("הָשֵׁב אֶת-מַטֵּה אַהֲרֹן", "רד עצא הרון", "'Return Aaron's staff"),
        ("לִפְנֵי הָעֵדוּת", "בין ידי אלשהאדה", "before the testimony,"),
        ("לְמִשְׁמֶרֶת", "תכון חפץ'", "to be kept"),
        ("לְאוֹת", "עלאמה", "as a sign"),
        ("לִבְנֵי-מֶרִי", "לד'וי אלכ'לף", "for those who are rebellious,"),
        ("וּתְכַל תְּלוּנֹּתָם מֵעָלַי", "פיפנא תד'מרהם עליי", "that their complaining against Me may be brought to an end,"),
        ("וְלֹא יָמֻתוּ", "ולא יהלכון", "and they shall not perish.'"),
    ],
    26: [
        # HE: וַיַּעַשׂ מֹשֶׁה כַּאֲשֶׁר צִוָּה יְהוָה אֹתוֹ כֵּן עָשָׂה
        # JA: פצנע מוסי'. כמא אמרה אללה מן ד'אלך
        # EN: And Moses did as God had commanded him in this.
        ("וַיַּעַשׂ מֹשֶׁה", "פצנע מוסי'", "And Moses did"),
        ("כַּאֲשֶׁר צִוָּה יְהוָה", "כמא אמרה אללה", "as God had commanded him"),
        ("אֹתוֹ כֵּן עָשָׂה", "מן ד'אלך", "in this."),
    ],
    27: [
        # HE: וַיֹּאמְרוּ בְּנֵי יִשְׂרָאֵל אֶל-מֹשֶׁה לֵאמֹר הֵן גָּוַעְנוּ אָבַדְנוּ כֻּלָּנוּ אָבָדְנוּ
        # JA: ת'ם קאל בני אסראיל למוסי'. הוד'א קד תופא מנא ובאד מנא. פכלנא האלכין
        # EN: Then the sons of Israel said to Moses: 'Behold, some of us have died and some of us have perished — so we are all doomed.'
        (None, "ת'ם", "Then"),
        ("וַיֹּאמְרוּ בְּנֵי יִשְׂרָאֵל", "קאל בני אסראיל", "the sons of Israel said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses:"),
        ("הֵן גָּוַעְנוּ", "הוד'א קד תופא מנא", "'Behold, some of us have died"),
        ("אָבַדְנוּ", "ובאד מנא", "and some of us have perished —"),
        ("כֻּלָּנוּ אָבָדְנוּ", "פכלנא האלכין", "so we are all doomed.'"),
    ],
    28: [
        # HE: כֹּל הַקָּרֵב הַקָּרֵב אֶל-מִשְׁכַּן יְהוָה יָמוּת הַאִם תַּמְנוּ לִגְו‍ֹעַ
        # JA: ואד'א כאן כל מתקדם. אלי' מסכן אללה יהלך. פהוד'א נחן פאנון מתופון
        # EN: And if every one who draws near to the dwelling of God is destroyed, then behold — we are perishing, we are dying.'
        ("כֹּל הַקָּרֵב הַקָּרֵב", "ואד'א כאן כל מתקדם", "And if every one who draws near"),
        ("אֶל-מִשְׁכַּן יְהוָה", "אלי' מסכן אללה", "to the dwelling of God"),
        ("יָמוּת", "יהלך", "is destroyed,"),
        ("הַאִם תַּמְנוּ", "פהוד'א נחן", "then behold — we"),
        ("לִגְו‍ֹעַ", "פאנון מתופון", "are perishing, we are dying.'"),
    ],
}

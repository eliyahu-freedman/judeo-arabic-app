"""Hand-authored word-level alignment triples for Bamidbar chapter 18."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-אַהֲרֹן אַתָּה וּבָנֶיךָ וּבֵית-אָבִיךָ אִתָּךְ תִּשְׂאוּ אֶת-עֲו‍ֹן הַמִּקְדָּשׁ וְאַתָּה וּבָנֶיךָ אִתָּךְ תִּשְׂאוּ אֶת-עֲו‍ֹן כְּהֻנַּתְכֶם
        # JA: פקאל אללה להרון. אנת ובניך ובית אביך מעך. תחמלון וזר אלקדס. ואנת. ובניך מעך תחמלון וזר אמאמתכם
        # EN: And God said to Aaron: 'You and your sons and your father's house with you shall bear the burden of the sanctuary; and you and your sons with you shall bear the burden of your priesthood.
        (None, "פקאל", "And"),
        ("וַיֹּאמֶר יְהוָה", "אללה", "God said"),
        ("אֶל-אַהֲרֹן", "להרון", "to Aaron:"),
        ("אַתָּה", "אנת", "'You"),
        ("וּבָנֶיךָ", "ובניך", "and your sons"),
        ("וּבֵית-אָבִיךָ", "ובית אביך", "and your father's house"),
        ("אִתָּךְ", "מעך", "with you"),
        ("תִּשְׂאוּ", "תחמלון", "shall bear"),
        ("אֶת-עֲו‍ֹן", "וזר", "the burden of"),
        ("הַמִּקְדָּשׁ", "אלקדס", "the sanctuary;"),
        ("וְאַתָּה", "ואנת", "and you"),
        ("וּבָנֶיךָ", "ובניך", "and your sons"),
        ("אִתָּךְ", "מעך", "with you"),
        ("תִּשְׂאוּ", "תחמלון", "shall bear"),
        ("אֶת-עֲו‍ֹן", "וזר", "the burden of"),
        ("כְּהֻנַּתְכֶם", "אמאמתכם", "your priesthood."),
    ],
    2: [
        # HE: וְגַם אֶת-אַחֶיךָ מַטֵּה לֵוִי שֵׁבֶט אָבִיךָ הַקְרֵב אִתָּךְ וְיִלָּווּ עָלֶיךָ וִישָׁרְתוּךָ וְאַתָּה וּבָנֶיךָ אִתָּךְ לִפְנֵי אֹהֶל הָעֵדֻת
        # JA: ואיצ'א אכ'ותך בני לוי. סבט אביך קדמהם אליך. וינצ'אפון אליך ויכ'דמונך. ואנת ובניך מעך. פקט. בין ידי כ'בא אלשהאדה
        # EN: And likewise your brothers, the sons of Levi — the tribe of your father — bring them forward to you, that they may be joined to you and serve you; while you and your sons with you alone shall be before the tent of the testimony.
        ("וְגַם", "ואיצ'א", "And likewise"),
        ("אֶת-אַחֶיךָ", "אכ'ותך", "your brothers,"),
        ("מַטֵּה לֵוִי", "בני לוי", "the sons of Levi —"),
        ("שֵׁבֶט אָבִיךָ", "סבט אביך", "the tribe of your father —"),
        ("הַקְרֵב", "קדמהם", "bring them forward"),
        ("אִתָּךְ", "אליך", "to you,"),
        ("וְיִלָּווּ עָלֶיךָ", "וינצ'אפון אליך", "that they may be joined to you"),
        ("וִישָׁרְתוּךָ", "ויכ'דמונך", "and serve you;"),
        ("וְאַתָּה", "ואנת", "while you"),
        ("וּבָנֶיךָ", "ובניך", "and your sons"),
        ("אִתָּךְ", "מעך", "with you"),
        (None, "פקט", "alone"),
        ("לִפְנֵי", "בין ידי", "shall be before"),
        ("אֹהֶל הָעֵדֻת", "כ'בא אלשהאדה", "the tent of the testimony."),
    ],
    3: [
        # HE: וְשָׁמְרוּ מִשְׁמַרְתְּךָ וּמִשְׁמֶרֶת כָּל-הָאֹהֶל אַךְ אֶל-כְּלֵי הַקֹּדֶשׁ וְאֶל-הַמִּזְבֵּחַ לֹא יִקְרָבוּ וְלֹא-יָמֻתוּ גַם-הֵם גַּם-אַתֶּם
        # JA: ויחפצון מחפצך. וחפץ' גמיע אלכ'בא. מא כ'לא אניה' אלקדס ואלמד'בח לא יתקדמו. ללא יהלכון אנתם והם אגמעין
        # EN: And they shall keep your charge and the charge of the whole tent — except that they shall not approach the vessels of the sanctuary and the altar, lest both you and they perish together.
        ("וְשָׁמְרוּ", "ויחפצון", "And they shall keep"),
        ("מִשְׁמַרְתְּךָ", "מחפצך", "your charge"),
        ("וּמִשְׁמֶרֶת", "וחפץ'", "and the charge of"),
        ("כָּל-הָאֹהֶל", "גמיע אלכ'בא", "the whole tent —"),
        (None, "מא כ'לא", "except that"),
        ("אֶל-כְּלֵי הַקֹּדֶשׁ", "אניה' אלקדס", "the vessels of the sanctuary"),
        ("וְאֶל-הַמִּזְבֵּחַ", "ואלמד'בח", "and the altar"),
        ("לֹא יִקְרָבוּ", "לא יתקדמו", "they shall not approach"),
        ("וְלֹא-יָמֻתוּ", "ללא יהלכון", "lest both you and they"),
        ("גַם-הֵם גַּם-אַתֶּם", "אנתם והם אגמעין", "perish together."),
    ],
    4: [
        # HE: וְנִלְווּ עָלֶיךָ--וְשָׁמְרוּ אֶת-מִשְׁמֶרֶת אֹהֶל מוֹעֵד לְכֹל עֲבֹדַת הָאֹהֶל וְזָר לֹא-יִקְרַב אֲלֵיכֶם
        # JA: ואלמנצ'אפין אליך. יחפצון חפץ' כ'בא אלמחצ'ר וכ'דמתה. ואגנבי לא יתקדם אליכם
        # EN: And those joined to you shall keep the charge of the tent of assembly and all its service; but an outsider shall not approach you.
        ("וְנִלְווּ עָלֶיךָ", "ואלמנצ'אפין אליך", "And those joined to you"),
        ("וְשָׁמְרוּ", "יחפצון", "shall keep"),
        ("אֶת-מִשְׁמֶרֶת", "חפץ'", "the charge of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of assembly"),
        ("לְכֹל עֲבֹדַת הָאֹהֶל", "וכ'דמתה", "and all its service;"),
        ("וְזָר", "ואגנבי", "but an outsider"),
        ("לֹא-יִקְרַב", "לא יתקדם", "shall not approach"),
        ("אֲלֵיכֶם", "אליכם", "you."),
    ],
    5: [
        # HE: וּשְׁמַרְתֶּם אֵת מִשְׁמֶרֶת הַקֹּדֶשׁ וְאֵת מִשְׁמֶרֶת הַמִּזְבֵּחַ וְלֹא-יִהְיֶה עוֹד קֶצֶף עַל-בְּנֵי יִשְׂרָאֵל
        # JA: ותחפצ'ו חפץ' אלקד'ס וחפץ' אלמד'בח. ולא יכון זיאדה' סכ'ט. עלי' בני אסראיל
        # EN: And you shall keep the charge of the sanctuary and the charge of the altar, so that there be no further outburst of wrath upon the sons of Israel.
        ("וּשְׁמַרְתֶּם", "ותחפצ'ו", "And you shall keep"),
        ("מִשְׁמֶרֶת הַקֹּדֶשׁ", "חפץ' אלקד'ס", "the charge of the sanctuary"),
        ("וְאֵת מִשְׁמֶרֶת", "וחפץ'", "and the charge of"),
        ("הַמִּזְבֵּחַ", "אלמד'בח", "the altar,"),
        ("וְלֹא-יִהְיֶה", "ולא יכון", "so that there be"),
        ("עוֹד", "זיאדה'", "no further"),
        ("קֶצֶף", "סכ'ט", "outburst of wrath"),
        ("עַל-בְּנֵי", "עלי' בני", "upon the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel."),
    ],
    6: [
        # HE: וַאֲנִי הִנֵּה לָקַחְתִּי אֶת-אֲחֵיכֶם הַלְוִיִּם מִתּוֹךְ בְּנֵי יִשְׂרָאֵל--לָכֶם מַתָּנָה נְתֻנִים לַיהוָה לַעֲבֹד אֶת-עֲבֹדַת אֹהֶל מוֹעֵד
        # JA: פאני קד אכ'ד'ת אכ'ותכם אלליואניין. מן בין בני אסראיל. וגעלתהם הבה לכם ללה. ליכ'דמו כ'דמה' כ'בא אלמחצ'ר
        # EN: For I have taken your brothers, the Levites, from among the sons of Israel — I have made them a gift to you, dedicated to God, to serve the service of the tent of assembly.
        (None, "פאני", "For I"),
        ("וַאֲנִי הִנֵּה לָקַחְתִּי", "קד אכ'ד'ת", "have taken"),
        ("אֶת-אֲחֵיכֶם", "אכ'ותכם", "your brothers,"),
        ("הַלְוִיִּם", "אלליואניין", "the Levites,"),
        ("מִתּוֹךְ", "מן בין", "from among"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel —"),
        ("לָכֶם", "וגעלתהם הבה לכם", "I have made them a gift to you,"),
        ("מַתָּנָה נְתֻנִים לַיהוָה", "ללה", "dedicated to God,"),
        ("לַעֲבֹד", "ליכ'דמו", "to serve"),
        ("אֶת-עֲבֹדַת", "כ'דמה'", "the service of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of assembly."),
    ],
    7: [
        # HE: וְאַתָּה וּבָנֶיךָ אִתְּךָ תִּשְׁמְרוּ אֶת-כְּהֻנַּתְכֶם לְכָל-דְּבַר הַמִּזְבֵּחַ וּלְמִבֵּית לַפָּרֹכֶת--וַעֲבַדְתֶּם עֲבֹדַת מַתָּנָה אֶתֵּן אֶת-כְּהֻנַּתְכֶם וְהַזָּר הַקָּרֵב יוּמָת
        # JA: ואנת ובניך מעך. תחפצון אמאמתכם. לגמיע אמור אלמד'בח. ודאכ'ל אלסגף ותכ'דמונה. פקד געלת כ'דמתכם כ'דמה מוהובה. ואי אגנבי תקדם אליהא פליקתל
        # EN: And you and your sons with you shall keep your priesthood for all matters of the altar and what is within the veil, and you shall serve them; for I have made your service a gifted service — and any outsider who approaches it shall be put to death.'
        ("וְאַתָּה", "ואנת", "And you"),
        ("וּבָנֶיךָ", "ובניך", "and your sons"),
        ("אִתְּךָ", "מעך", "with you"),
        ("תִּשְׁמְרוּ", "תחפצון", "shall keep"),
        ("אֶת-כְּהֻנַּתְכֶם", "אמאמתכם", "your priesthood"),
        ("לְכָל-דְּבַר הַמִּזְבֵּחַ", "לגמיע אמור אלמד'בח", "for all matters of the altar"),
        ("וּלְמִבֵּית לַפָּרֹכֶת", "ודאכ'ל אלסגף", "and what is within the veil,"),
        ("וַעֲבַדְתֶּם", "ותכ'דמונה", "and you shall serve them;"),
        ("עֲבֹדַת מַתָּנָה", "פקד געלת כ'דמתכם כ'דמה מוהובה", "for I have made your service a gifted service —"),
        ("וְהַזָּר", "ואי אגנבי", "and any outsider"),
        ("הַקָּרֵב", "תקדם אליהא", "who approaches it"),
        ("יוּמָת", "פליקתל", "shall be put to death.'"),
    ],
    8: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-אַהֲרֹן וַאֲנִי הִנֵּה נָתַתִּי לְךָ אֶת-מִשְׁמֶרֶת תְּרוּמֹתָי לְכָל-קָדְשֵׁי בְנֵי-יִשְׂרָאֵל לְךָ נְתַתִּים לְמָשְׁחָה וּלְבָנֶיךָ--לְחָק-עוֹלָם
        # JA: ת'ם כלם אללה הרון. וקאל. אני קד אעטיתך חפץ' רפאיעי. מן גמיע אקדאס בני אסראיל. אעטיתהא לך מסחא. ולבניך רסם אלדהר
        # EN: Then God spoke to Aaron, and said: 'I have indeed given you the charge of My raised-offerings, from all the holy things of the sons of Israel; I have given them to you as an anointing, and to your sons as a perpetual ordinance.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר יְהוָה", "כלם אללה", "God spoke"),
        ("אֶל-אַהֲרֹן", "הרון", "to Aaron,"),
        (None, "וקאל", "and said:"),
        ("וַאֲנִי הִנֵּה נָתַתִּי", "אני קד אעטיתך", "'I have indeed given you"),
        ("אֶת-מִשְׁמֶרֶת", "חפץ'", "the charge of"),
        ("תְּרוּמֹתָי", "רפאיעי", "My raised-offerings,"),
        ("לְכָל-קָדְשֵׁי", "מן גמיע אקדאס", "from all the holy things of"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel;"),
        ("לְךָ נְתַתִּים", "אעטיתהא לך", "I have given them to you"),
        ("לְמָשְׁחָה", "מסחא", "as an anointing,"),
        ("וּלְבָנֶיךָ", "ולבניך", "and to your sons"),
        ("לְחָק-עוֹלָם", "רסם אלדהר", "as a perpetual ordinance."),
    ],
    9: [
        # HE: זֶה-יִהְיֶה לְךָ מִקֹּדֶשׁ הַקֳּדָשִׁים מִן-הָאֵשׁ כָּל-קָרְבָּנָם לְכָל-מִנְחָתָם וּלְכָל-חַטָּאתָם וּלְכָל-אֲשָׁמָם אֲשֶׁר יָשִׁיבוּ לִי--קֹדֶשׁ קָדָשִׁים לְךָ הוּא וּלְבָנֶיךָ
        # JA: הד'א יכון לך. מן כ'ואץ אלאקדאס מן בעד אלמחרק. מן גמיע קראבינהם וברהם ודכותהם. וקרבאן אלאת'ם אלד'י יאתוני בה. פהו מן כ'ואץ אלאקדאס. לך ולבניך
        # EN: This shall be yours from the choicest of the holy things, after the burning: from all their offerings and their grain-offerings and their purification-offerings, and the guilt-offering which they bring to Me — it is from the choicest of the holy things, for you and for your sons.
        ("זֶה-יִהְיֶה לְךָ", "הד'א יכון לך", "This shall be yours"),
        ("מִקֹּדֶשׁ הַקֳּדָשִׁים", "מן כ'ואץ אלאקדאס", "from the choicest of the holy things,"),
        ("מִן-הָאֵשׁ", "מן בעד אלמחרק", "after the burning:"),
        ("כָּל-קָרְבָּנָם", "מן גמיע קראבינהם", "from all their offerings"),
        ("לְכָל-מִנְחָתָם", "וברהם", "and their grain-offerings"),
        ("וּלְכָל-חַטָּאתָם", "ודכותהם", "and their purification-offerings,"),
        ("וּלְכָל-אֲשָׁמָם", "וקרבאן אלאת'ם", "and the guilt-offering"),
        ("אֲשֶׁר יָשִׁיבוּ לִי", "אלד'י יאתוני בה", "which they bring to Me —"),
        ("קֹדֶשׁ קָדָשִׁים", "פהו מן כ'ואץ אלאקדאס", "it is from the choicest of the holy things,"),
        ("לְךָ הוּא", "לך", "for you"),
        ("וּלְבָנֶיךָ", "ולבניך", "and for your sons."),
    ],
    10: [
        # HE: בְּקֹדֶשׁ הַקֳּדָשִׁים תֹּאכְלֶנּוּ כָּל-זָכָר יֹאכַל אֹתוֹ קֹדֶשׁ יִהְיֶה-לָּךְ
        # JA: ובכ'אץ אלט'הר תאכלה. כל ד'כר יאכל מנה. כד'אך יכון לך קדסא
        # EN: You shall eat it in the choicest of purity: every male shall eat of it; thus shall it be holy to you.
        ("בְּקֹדֶשׁ הַקֳּדָשִׁים", "ובכ'אץ אלט'הר", "You shall eat it in the choicest of purity:"),
        ("תֹּאכְלֶנּוּ", "תאכלה", "every"),
        ("כָּל-זָכָר", "כל ד'כר", "male"),
        ("יֹאכַל אֹתוֹ", "יאכל מנה", "shall eat of it;"),
        (None, "כד'אך", "thus"),
        ("קֹדֶשׁ יִהְיֶה-לָּךְ", "יכון לך קדסא", "shall it be holy to you."),
    ],
    11: [
        # HE: וְזֶה-לְּךָ תְּרוּמַת מַתָּנָם לְכָל-תְּנוּפֹת בְּנֵי יִשְׂרָאֵל--לְךָ נְתַתִּים וּלְבָנֶיךָ וְלִבְנֹתֶיךָ אִתְּךָ לְחָק-עוֹלָם כָּל-טָהוֹר בְּבֵיתְךָ יֹאכַל אֹתוֹ
        # JA: והד'ה לך רפאיע עטאיאהם. מן גמיע מחרכאת בני אסראיל. לך אעטיתהא. ולבניך ולבנאתך. מעך רסם אלדהר. כל טאהר פי מנזלך יאכלהא
        # EN: And these are yours — the raised-offerings of their gifts, from all the wave-offerings of the sons of Israel; I have given them to you, and to your sons and to your daughters with you, as a perpetual ordinance: every one who is pure in your household may eat it.
        ("וְזֶה-לְּךָ", "והד'ה לך", "And these are yours —"),
        ("תְּרוּמַת מַתָּנָם", "רפאיע עטאיאהם", "the raised-offerings of their gifts,"),
        ("לְכָל-תְּנוּפֹת", "מן גמיע מחרכאת", "from all the wave-offerings of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel;"),
        ("לְךָ נְתַתִּים", "לך אעטיתהא", "I have given them to you,"),
        ("וּלְבָנֶיךָ", "ולבניך", "and to your sons"),
        ("וְלִבְנֹתֶיךָ", "ולבנאתך", "and to your daughters"),
        ("אִתְּךָ", "מעך", "with you,"),
        ("לְחָק-עוֹלָם", "רסם אלדהר", "as a perpetual ordinance:"),
        ("כָּל-טָהוֹר", "כל טאהר", "every one who is pure"),
        ("בְּבֵיתְךָ", "פי מנזלך", "in your household"),
        ("יֹאכַל אֹתוֹ", "יאכלהא", "may eat it."),
    ],
    12: [
        # HE: כֹּל חֵלֶב יִצְהָר וְכָל-חֵלֶב תִּירוֹשׁ וְדָגָן--רֵאשִׁיתָם אֲשֶׁר-יִתְּנוּ לַיהוָה לְךָ נְתַתִּים
        # JA: וגמיע אגוד אלדהן ואלעציר ואלבר. אואילהא. אלד'י יגעלונהא ללה קד געלתהא לך
        # EN: And all the choicest of the oil and of the juice and of the grain — their firstfruits which they set apart for God — I have given them to you.
        ("כֹּל חֵלֶב יִצְהָר", "וגמיע אגוד אלדהן", "And all the choicest of the oil"),
        ("וְכָל-חֵלֶב תִּירוֹשׁ", "ואלעציר", "and of the juice"),
        ("וְדָגָן", "ואלבר", "and of the grain —"),
        ("רֵאשִׁיתָם", "אואילהא", "their firstfruits"),
        ("אֲשֶׁר-יִתְּנוּ", "אלד'י יגעלונהא", "which they set apart"),
        ("לַיהוָה", "ללה", "for God —"),
        ("לְךָ נְתַתִּים", "קד געלתהא לך", "I have given them to you."),
    ],
    13: [
        # HE: בִּכּוּרֵי כָּל-אֲשֶׁר בְּאַרְצָם אֲשֶׁר-יָבִיאוּ לַיהוָה--לְךָ יִהְיֶה כָּל-טָהוֹר בְּבֵיתְךָ יֹאכְלֶנּוּ
        # JA: ובכור מא פי ריאצ'הם. אלד'י יאתון בה ללה יכון לך. וכל טאהר פי מנזלך יאכלה
        # EN: And the firstfruits of all that is in their gardens, which they bring to God, shall be yours; every one who is pure in your household may eat it.
        ("בִּכּוּרֵי", "ובכור", "And the firstfruits of"),
        ("כָּל-אֲשֶׁר בְּאַרְצָם", "מא פי ריאצ'הם", "all that is in their gardens,"),
        ("אֲשֶׁר-יָבִיאוּ", "אלד'י יאתון בה", "which they bring"),
        ("לַיהוָה", "ללה", "to God,"),
        ("לְךָ יִהְיֶה", "יכון לך", "shall be yours;"),
        ("כָּל-טָהוֹר", "וכל טאהר", "every one who is pure"),
        ("בְּבֵיתְךָ", "פי מנזלך", "in your household"),
        ("יֹאכְלֶנּוּ", "יאכלה", "may eat it."),
    ],
    14: [
        # HE: כָּל-חֵרֶם בְּיִשְׂרָאֵל לְךָ יִהְיֶה
        # JA: וכל צ'ואף פי אל אסראיל יכון לך
        # EN: And every devoted thing in the house of Israel shall be yours.
        (None, "וכל", "And every"),
        ("כָּל-חֵרֶם", "צ'ואף", "devoted thing"),
        ("בְּיִשְׂרָאֵל", "פי אל אסראיל", "in the house of Israel"),
        ("לְךָ יִהְיֶה", "יכון לך", "shall be yours."),
    ],
    15: [
        # HE: כָּל-פֶּטֶר רֶחֶם לְכָל-בָּשָׂר אֲשֶׁר-יַקְרִיבוּ לַיהוָה בָּאָדָם וּבַבְּהֵמָה--יִהְיֶה-לָּךְ אַךְ פָּדֹה תִפְדֶּה אֵת בְּכוֹר הָאָדָם וְאֵת בְּכוֹר-הַבְּהֵמָה הַטְּמֵאָה תִּפְדֶּה
        # JA: וכל אוול בטן. מן כל בשרי. אלד'י יקדמונה ללה. מן אנסאן ובהימה יכון לך. לכן יגב אן תפדי בכור אלנאס. ובכור אלבהימה אלנגסה
        # EN: Every firstborn of the womb, of all flesh, which they present to God — of human and of beast — shall be yours; yet you are required to redeem the firstborn of people, and the firstborn of unclean beasts you shall redeem.
        ("כָּל-פֶּטֶר רֶחֶם", "וכל אוול בטן", "Every firstborn of the womb,"),
        ("לְכָל-בָּשָׂר", "מן כל בשרי", "of all flesh,"),
        ("אֲשֶׁר-יַקְרִיבוּ", "אלד'י יקדמונה", "which they present"),
        ("לַיהוָה", "ללה", "to God —"),
        ("בָּאָדָם", "מן אנסאן", "of human"),
        ("וּבַבְּהֵמָה", "ובהימה", "and of beast —"),
        ("יִהְיֶה-לָּךְ", "יכון לך", "shall be yours;"),
        ("אַךְ פָּדֹה תִפְדֶּה", "לכן יגב אן תפדי", "yet you are required to redeem"),
        ("אֵת בְּכוֹר הָאָדָם", "בכור אלנאס", "the firstborn of people,"),
        ("וְאֵת בְּכוֹר-הַבְּהֵמָה", "ובכור אלבהימה", "and the firstborn of"),
        ("הַטְּמֵאָה תִּפְדֶּה", "אלנגסה", "unclean beasts you shall redeem."),
    ],
    16: [
        # HE: וּפְדוּיָו מִבֶּן-חֹדֶשׁ תִּפְדֶּה בְּעֶרְכְּךָ כֶּסֶף חֲמֵשֶׁת שְׁקָלִים בְּשֶׁקֶל הַקֹּדֶשׁ עֶשְׂרִים גֵּרָה הוּא
        # JA: ופדא אלנאס מן אבן שהר. בקימתה. כ'מסה מת'אקיל פצ'ה אלקדס. והו עשרין דאנק
        # EN: And the redemption of people shall be from one month of age, at its valuation: five shekels of silver of the sanctuary, which is twenty daniq.
        ("וּפְדוּיָו", "ופדא אלנאס", "And the redemption of people"),
        ("מִבֶּן-חֹדֶשׁ", "מן אבן שהר", "shall be from one month of age,"),
        ("תִּפְדֶּה בְּעֶרְכְּךָ", "בקימתה", "at its valuation:"),
        ("כֶּסֶף חֲמֵשֶׁת שְׁקָלִים", "כ'מסה מת'אקיל פצ'ה", "five shekels of silver"),
        ("בְּשֶׁקֶל הַקֹּדֶשׁ", "אלקדס", "of the sanctuary,"),
        ("עֶשְׂרִים גֵּרָה הוּא", "והו עשרין דאנק", "which is twenty daniq."),
    ],
    17: [
        # HE: אַךְ בְּכוֹר-שׁוֹר אוֹ-בְכוֹר כֶּשֶׂב אוֹ-בְכוֹר עֵז לֹא תִפְדֶּה--קֹדֶשׁ הֵם אֶת-דָּמָם תִּזְרֹק עַל-הַמִּזְבֵּחַ וְאֶת-חֶלְבָּם תַּקְטִיר--אִשֶּׁה לְרֵיחַ נִיחֹחַ לַיהוָה
        # JA: פאמא בכר אלבקר ואלצ'אן ואלמאעז. פלא תפדהא פאנהא מקדסה. רש דמהא עלי' אלמד'בח וקתר שחמהא. קרבאן מקבול מרצ'י ללה
        # EN: But the firstborn of oxen and of sheep and of goats you shall not redeem, for they are holy: sprinkle their blood upon the altar, and burn their fat — an accepted and pleasing offering to God.
        (None, "פאמא", "But"),
        ("אַךְ בְּכוֹר-שׁוֹר", "בכר אלבקר", "the firstborn of oxen"),
        ("אוֹ-בְכוֹר כֶּשֶׂב", "ואלצ'אן", "and of sheep"),
        ("אוֹ-בְכוֹר עֵז", "ואלמאעז", "and of goats"),
        ("לֹא תִפְדֶּה", "פלא תפדהא", "you shall not redeem,"),
        ("קֹדֶשׁ הֵם", "פאנהא מקדסה", "for they are holy:"),
        ("אֶת-דָּמָם תִּזְרֹק", "רש דמהא", "sprinkle their blood"),
        ("עַל-הַמִּזְבֵּחַ", "עלי' אלמד'בח", "upon the altar,"),
        ("וְאֶת-חֶלְבָּם תַּקְטִיר", "וקתר שחמהא", "and burn their fat —"),
        ("אִשֶּׁה לְרֵיחַ נִיחֹחַ", "קרבאן מקבול מרצ'י", "an accepted and pleasing offering"),
        ("לַיהוָה", "ללה", "to God."),
    ],
    18: [
        # HE: וּבְשָׂרָם יִהְיֶה-לָּךְ כַּחֲזֵה הַתְּנוּפָה וּכְשׁוֹק הַיָּמִין לְךָ יִהְיֶה
        # JA: ולחמהא יכון לך. כקץ אלתחריך. וכאלסאק אלימני יכון לך
        # EN: And their flesh shall be yours — as the breast of the wave-offering and as the right thigh, it shall be yours.
        ("וּבְשָׂרָם", "ולחמהא", "And their flesh"),
        ("יִהְיֶה-לָּךְ", "יכון לך", "shall be yours —"),
        ("כַּחֲזֵה", "כקץ", "as the breast of"),
        ("הַתְּנוּפָה", "אלתחריך", "the wave-offering"),
        ("וּכְשׁוֹק", "וכאלסאק", "and as the"),
        ("הַיָּמִין", "אלימני", "right thigh,"),
        ("לְךָ יִהְיֶה", "יכון לך", "it shall be yours."),
    ],
    19: [
        # HE: כֹּל תְּרוּמֹת הַקֳּדָשִׁים אֲשֶׁר יָרִימוּ בְנֵי-יִשְׂרָאֵל לַיהוָה--נָתַתִּי לְךָ וּלְבָנֶיךָ וְלִבְנֹתֶיךָ אִתְּךָ לְחָק-עוֹלָם בְּרִית מֶלַח עוֹלָם הִוא לִפְנֵי יְהוָה לְךָ וּלְזַרְעֲךָ אִתָּךְ
        # JA: וסאיר רפאיע אלאקדאס. אלתי ירפעוהא בני אסראיל ללה. געלתהא לך. ולבניך ולבנאתך. מעך רסם אלדהר. עהד ת'באת אלעאלם הו ללה. לך ולנסלך בעדך
        # EN: And the rest of the raised-offerings of the holy things which the sons of Israel give to God — I have given them to you, and to your sons and to your daughters with you, as a perpetual ordinance; it is a covenant of the world's enduring stability before God, for you and for your offspring after you.'
        ("כֹּל תְּרוּמֹת", "וסאיר רפאיע", "And the rest of the raised-offerings of"),
        ("הַקֳּדָשִׁים", "אלאקדאס", "the holy things"),
        ("אֲשֶׁר יָרִימוּ", "אלתי ירפעוהא", "which the sons of Israel"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "give"),
        ("לַיהוָה", "ללה", "to God —"),
        ("נָתַתִּי לְךָ", "געלתהא לך", "I have given them to you,"),
        ("וּלְבָנֶיךָ", "ולבניך", "and to your sons"),
        ("וְלִבְנֹתֶיךָ", "ולבנאתך", "and to your daughters"),
        ("אִתְּךָ", "מעך", "with you,"),
        ("לְחָק-עוֹלָם", "רסם אלדהר", "as a perpetual ordinance;"),
        ("בְּרִית מֶלַח עוֹלָם", "עהד ת'באת אלעאלם", "it is a covenant of the world's enduring stability"),
        ("הִוא לִפְנֵי יְהוָה", "הו ללה", "before God,"),
        ("לְךָ", "לך", "for you"),
        ("וּלְזַרְעֲךָ אִתָּךְ", "ולנסלך בעדך", "and for your offspring after you.'"),
    ],
    20: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-אַהֲרֹן בְּאַרְצָם לֹא תִנְחָל וְחֵלֶק לֹא-יִהְיֶה לְךָ בְּתוֹכָם אֲנִי חֶלְקְךָ וְנַחֲלָתְךָ בְּתוֹךְ בְּנֵי יִשְׂרָאֵל
        # JA: ת'ם קאל אללה לה. פי ריאצ'הם לא תנחל. ולא יכון לך נציב פי מא בינהם. פאני קד געלת קראביני קסמך ונחלתך. פי מא בין בני אסראיל
        # EN: Then God said to him: 'In their gardens you shall not inherit, nor shall you have a portion among them; for I have made My offerings your portion and your inheritance among the sons of Israel.'
        (None, "ת'ם", "Then"),
        ("וַיֹּאמֶר יְהוָה", "קאל אללה", "God said"),
        ("אֶל-אַהֲרֹן", "לה", "to him:"),
        ("בְּאַרְצָם", "פי ריאצ'הם", "'In their gardens"),
        ("לֹא תִנְחָל", "לא תנחל", "you shall not inherit,"),
        ("וְחֵלֶק לֹא-יִהְיֶה לְךָ", "ולא יכון לך נציב", "nor shall you have a portion"),
        ("בְּתוֹכָם", "פי מא בינהם", "among them;"),
        ("אֲנִי", "פאני", "for I"),
        ("חֶלְקְךָ", "קד געלת קראביני קסמך", "have made My offerings your portion"),
        ("וְנַחֲלָתְךָ", "ונחלתך", "and your inheritance"),
        ("בְּתוֹךְ בְּנֵי יִשְׂרָאֵל", "פי מא בין בני אסראיל", "among the sons of Israel.'"),
    ],
    21: [
        # HE: וְלִבְנֵי לֵוִי הִנֵּה נָתַתִּי כָּל-מַעֲשֵׂר בְּיִשְׂרָאֵל לְנַחֲלָה חֵלֶף עֲבֹדָתָם אֲשֶׁר-הֵם עֹבְדִים אֶת-עֲבֹדַת אֹהֶל מוֹעֵד
        # JA: ולבני לוי. קד געלת כל עשר מן אל אסראיל נחלה. בדל כ'דמתהם. אלד'י יכ'דמון כ'בא אלמחצ'ר
        # EN: And to the sons of Levi — I have given every tithe from the house of Israel as an inheritance, in exchange for their service which they serve at the tent of assembly.
        ("וְלִבְנֵי", "ולבני", "And to the sons of"),
        ("לֵוִי", "לוי", "Levi —"),
        ("הִנֵּה נָתַתִּי", "קד געלת", "I have given"),
        ("כָּל-מַעֲשֵׂר", "כל עשר", "every tithe"),
        ("בְּיִשְׂרָאֵל", "מן אל אסראיל", "from the house of Israel"),
        ("לְנַחֲלָה", "נחלה", "as an inheritance,"),
        ("חֵלֶף", "בדל", "in exchange for"),
        ("עֲבֹדָתָם", "כ'דמתהם", "their service"),
        ("אֲשֶׁר-הֵם עֹבְדִים", "אלד'י יכ'דמון", "which they serve"),
        ("אֶת-עֲבֹדַת אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "at the tent of assembly."),
    ],
    22: [
        # HE: וְלֹא-יִקְרְבוּ עוֹד בְּנֵי יִשְׂרָאֵל אֶל-אֹהֶל מוֹעֵד לָשֵׂאת חֵטְא לָמוּת
        # JA: ולא יתקדם בני אסראיל איצ'א אלי' כ'בא אלמחצ'ר. פיחמלון וזרא פיהלכון
        # EN: And the sons of Israel shall no longer approach the tent of assembly, lest they bear a burden and perish.
        ("וְלֹא-יִקְרְבוּ", "ולא יתקדם", "And the sons of Israel shall no longer"),
        ("עוֹד", "איצ'א", "approach"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the tent of"),
        ("אֶל-אֹהֶל מוֹעֵד", "אלי' כ'בא אלמחצ'ר", "assembly,"),
        ("לָשֵׂאת חֵטְא", "פיחמלון וזרא", "lest they bear a burden"),
        ("לָמוּת", "פיהלכון", "and perish."),
    ],
    23: [
        # HE: וְעָבַד הַלֵּוִי הוּא אֶת-עֲבֹדַת אֹהֶל מוֹעֵד וְהֵם יִשְׂאוּ עֲו‍ֹנָם חֻקַּת עוֹלָם לְדֹרֹתֵיכֶם וּבְתוֹךְ בְּנֵי יִשְׂרָאֵל לֹא יִנְחֲלוּ נַחֲלָה
        # JA: ויכ'דמון אלליואניין וחדהם כ'בא אלמחצ'ר. והם יחמלון וזרהם. רסם אלדהר עלא מר אגיאלכם. ופי מא בין בני אסראיל. לא ינחלו נחלה
        # EN: And the Levites alone shall serve the tent of assembly, and they shall bear their burden — a perpetual ordinance throughout your generations; and among the sons of Israel they shall not inherit an inheritance.
        ("וְעָבַד", "ויכ'דמון", "And the Levites alone shall"),
        ("הַלֵּוִי הוּא", "אלליואניין וחדהם", "serve"),
        ("אֶת-עֲבֹדַת אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of assembly,"),
        ("וְהֵם", "והם", "and they"),
        ("יִשְׂאוּ", "יחמלון", "shall bear"),
        ("עֲו‍ֹנָם", "וזרהם", "their burden —"),
        ("חֻקַּת עוֹלָם", "רסם אלדהר", "a perpetual ordinance"),
        ("לְדֹרֹתֵיכֶם", "עלא מר אגיאלכם", "throughout your generations;"),
        ("וּבְתוֹךְ", "ופי מא בין", "and among"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("לֹא יִנְחֲלוּ", "לא ינחלו", "they shall not inherit"),
        ("נַחֲלָה", "נחלה", "an inheritance."),
    ],
    24: [
        # HE: כִּי אֶת-מַעְשַׂר בְּנֵי-יִשְׂרָאֵל אֲשֶׁר יָרִימוּ לַיהוָה תְּרוּמָה נָתַתִּי לַלְוִיִּם לְנַחֲלָה עַל-כֵּן אָמַרְתִּי לָהֶם בְּתוֹךְ בְּנֵי יִשְׂרָאֵל לֹא יִנְחֲלוּ נַחֲלָה
        # JA: פאן עשור בני אסראיל. אלתי ירפעונהא ללה רפיעה. געלתהא לאלליואניין נחלה. פלד'אלך קלת להם. פי מא בין בני אסראיל. לא ינחלון נחלה
        # EN: For the tithes of the sons of Israel, which they raise up to God as a raised-offering, I have given to the Levites as an inheritance; therefore I have said to them: among the sons of Israel they shall not inherit an inheritance.'
        ("כִּי", "פאן", "For"),
        ("אֶת-מַעְשַׂר", "עשור", "the tithes of"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("אֲשֶׁר יָרִימוּ", "אלתי ירפעונהא", "which they raise up"),
        ("לַיהוָה", "ללה", "to God"),
        ("תְּרוּמָה", "רפיעה", "as a raised-offering,"),
        ("נָתַתִּי", "געלתהא", "I have given"),
        ("לַלְוִיִּם", "לאלליואניין", "to the Levites"),
        ("לְנַחֲלָה", "נחלה", "as an inheritance;"),
        ("עַל-כֵּן", "פלד'אלך", "therefore"),
        ("אָמַרְתִּי לָהֶם", "קלת להם", "I have said to them:"),
        ("בְּתוֹךְ בְּנֵי יִשְׂרָאֵל", "פי מא בין בני אסראיל", "among the sons of Israel"),
        ("לֹא יִנְחֲלוּ", "לא ינחלון", "they shall not inherit"),
        ("נַחֲלָה", "נחלה", "an inheritance.'"),
    ],
    25: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses, saying:
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to"),
        ("אֶל-מֹשֶׁה", "מוסי'", "Moses,"),
        ("לֵּאמֹר", "תכלימא", "saying:"),
    ],
    26: [
        # HE: וְאֶל-הַלְוִיִּם תְּדַבֵּר וְאָמַרְתָּ אֲלֵהֶם כִּי-תִקְחוּ מֵאֵת בְּנֵי-יִשְׂרָאֵל אֶת-הַמַּעֲשֵׂר אֲשֶׁר נָתַתִּי לָכֶם מֵאִתָּם בְּנַחֲלַתְכֶם--וַהֲרֵמֹתֶם מִמֶּנּוּ תְּרוּמַת יְהוָה מַעֲשֵׂר מִן-הַמַּעֲשֵׂר
        # JA: ומר אלליואניין וקל להם. אד'א אכ'דתם מן בני אסראיל אלעשר. אלד'י געלתה לכם מנהם בנחלתכם. פארפעו מנה רפיעה ללה. עשרא מן אלעשר
        # EN: 'Command the Levites and say to them: when you take from the sons of Israel the tithe which I have given you from them as your inheritance, then raise up from it a raised-offering for God — a tenth of the tenth.
        ("וְאֶל-הַלְוִיִּם תְּדַבֵּר", "ומר אלליואניין", "'Command the Levites"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("כִּי-תִקְחוּ", "אד'א אכ'דתם", "when you take"),
        ("מֵאֵת בְּנֵי-יִשְׂרָאֵל", "מן בני אסראיל", "from the sons of Israel"),
        ("אֶת-הַמַּעֲשֵׂר", "אלעשר", "the tithe"),
        ("אֲשֶׁר נָתַתִּי לָכֶם", "אלד'י געלתה לכם", "which I have given you"),
        ("מֵאִתָּם", "מנהם", "from them"),
        ("בְּנַחֲלַתְכֶם", "בנחלתכם", "as your inheritance,"),
        ("וַהֲרֵמֹתֶם מִמֶּנּוּ", "פארפעו מנה", "then raise up from it"),
        ("תְּרוּמַת יְהוָה", "רפיעה ללה", "a raised-offering for God —"),
        ("מַעֲשֵׂר מִן-הַמַּעֲשֵׂר", "עשרא מן אלעשר", "a tenth of the tenth."),
    ],
    27: [
        # HE: וְנֶחְשַׁב לָכֶם תְּרוּמַתְכֶם--כַּדָּגָן מִן-הַגֹּרֶן וְכַמְלֵאָה מִן-הַיָּקֶב
        # JA: וד'אלך אן תחסב לכם רפאיעכם. כאלבר לבני אסראיל מן אלבד'אר. וכאלסלאפה מן אלת'ג'אר
        # EN: And this shall be reckoned for you as your raised-offerings — like the grain of the sons of Israel from the threshing-seed, and like the first-pressing from the vats.
        ("וְנֶחְשַׁב", "וד'אלך אן תחסב", "And this shall be reckoned"),
        ("לָכֶם", "לכם", "for you"),
        ("תְּרוּמַתְכֶם", "רפאיעכם", "as your raised-offerings —"),
        ("כַּדָּגָן", "כאלבר", "like the grain"),
        (None, "לבני אסראיל", "of the sons of Israel"),
        ("מִן-הַגֹּרֶן", "מן אלבד'אר", "from the threshing-seed,"),
        ("וְכַמְלֵאָה", "וכאלסלאפה", "and like the first-pressing"),
        ("מִן-הַיָּקֶב", "מן אלת'ג'אר", "from the vats."),
    ],
    28: [
        # HE: כֵּן תָּרִימוּ גַם-אַתֶּם תְּרוּמַת יְהוָה מִכֹּל מַעְשְׂרֹתֵיכֶם אֲשֶׁר תִּקְחוּ מֵאֵת בְּנֵי יִשְׂרָאֵל וּנְתַתֶּם מִמֶּנּוּ אֶת-תְּרוּמַת יְהוָה לְאַהֲרֹן הַכֹּהֵן
        # JA: כד'אך תרפעו אנתם איצ'א רפיעה ללה. מן גמיע עשורכם. אלתי תאכ'ד'והא מן בני אסראיל. ואעטו ד'אלך להרון אלאמאם
        # EN: So shall you also raise up a raised-offering for God from all your tithes which you take from the sons of Israel, and give that to Aaron the imām.
        (None, "כד'אך", "So"),
        ("כֵּן תָּרִימוּ", "תרפעו", "shall you"),
        ("גַם-אַתֶּם", "אנתם איצ'א", "also raise up"),
        ("תְּרוּמַת יְהוָה", "רפיעה ללה", "a raised-offering for God"),
        ("מִכֹּל מַעְשְׂרֹתֵיכֶם", "מן גמיע עשורכם", "from all your tithes"),
        ("אֲשֶׁר תִּקְחוּ", "אלתי תאכ'ד'והא", "which you take"),
        ("מֵאֵת בְּנֵי יִשְׂרָאֵל", "מן בני אסראיל", "from the sons of Israel,"),
        ("וּנְתַתֶּם מִמֶּנּוּ", "ואעטו ד'אלך", "and give that"),
        ("אֶת-תְּרוּמַת יְהוָה לְאַהֲרֹן", "להרון", "to Aaron"),
        ("הַכֹּהֵן", "אלאמאם", "the imām."),
    ],
    29: [
        # HE: מִכֹּל מַתְּנֹתֵיכֶם תָּרִימוּ אֵת כָּל-תְּרוּמַת יְהוָה מִכָּל-חֶלְבּוֹ--אֶת-מִקְדְּשׁוֹ מִמֶּנּוּ
        # JA: וליכון מא תרפעונה. מן גמיע עטאיאכם ללה. אגודהא ואכ'צהא מנהא
        # EN: And let what you raise up from all your gifts for God be the choicest and most select of them.
        (None, "וליכון", "And let"),
        ("מִכֹּל מַתְּנֹתֵיכֶם תָּרִימוּ", "מא תרפעונה", "what you raise up"),
        ("אֵת כָּל-תְּרוּמַת יְהוָה", "מן גמיע עטאיאכם ללה", "from all your gifts for God"),
        ("מִכָּל-חֶלְבּוֹ", "אגודהא", "be the choicest"),
        ("אֶת-מִקְדְּשׁוֹ מִמֶּנּוּ", "ואכ'צהא מנהא", "and most select of them."),
    ],
    30: [
        # HE: וְאָמַרְתָּ אֲלֵהֶם בַּהֲרִימְכֶם אֶת-חֶלְבּוֹ מִמֶּנּוּ וְנֶחְשַׁב לַלְוִיִּם כִּתְבוּאַת גֹּרֶן וְכִתְבוּאַת יָקֶב
        # JA: וקל להם. אד'א רפעתם אגודה מנה. צאר אלבאקי לכם יא ליואניין. כג'לה' בני אסראיל מן אלבד'אר ואלת'ג'אר
        # EN: And say to them: when you have raised up the choicest of it, the remainder shall count as yours, O Levites, as the yield of the sons of Israel from threshing-seed and from the vats.
        ("וְאָמַרְתָּ", "וקל", "And say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("בַּהֲרִימְכֶם", "אד'א רפעתם", "when you have raised up"),
        ("אֶת-חֶלְבּוֹ", "אגודה", "the choicest of it,"),
        ("מִמֶּנּוּ", "מנה", "the remainder"),
        ("וְנֶחְשַׁב לַלְוִיִּם", "צאר אלבאקי לכם יא ליואניין", "shall count as yours, O Levites,"),
        ("כִּתְבוּאַת גֹּרֶן", "כג'לה' בני אסראיל מן אלבד'אר", "as the yield of the sons of Israel from threshing-seed"),
        ("וְכִתְבוּאַת יָקֶב", "ואלת'ג'אר", "and from the vats."),
    ],
    31: [
        # HE: וַאֲכַלְתֶּם אֹתוֹ בְּכָל-מָקוֹם אַתֶּם וּבֵיתְכֶם כִּי-שָׂכָר הוּא לָכֶם חֵלֶף עֲבֹדַתְכֶם בְּאֹהֶל מוֹעֵד
        # JA: וגאיז אן תאכלוה פי כל מוצ'ע. אנתם ואלכם. לאנה אגרתכם. בדל כ'דמתכם פי כ'בא אלמחצ'ר
        # EN: And it is permitted that you eat it in every place — you and your households — for it is your wages in exchange for your service in the tent of assembly.
        ("וַאֲכַלְתֶּם", "וגאיז אן תאכלוה", "And it is permitted that you eat it"),
        ("בְּכָל-מָקוֹם", "פי כל מוצ'ע", "in every place —"),
        ("אַתֶּם", "אנתם", "you"),
        ("וּבֵיתְכֶם", "ואלכם", "and your households —"),
        ("כִּי-שָׂכָר הוּא לָכֶם", "לאנה אגרתכם", "for it is your wages"),
        ("חֵלֶף", "בדל", "in exchange for"),
        ("עֲבֹדַתְכֶם", "כ'דמתכם", "your service"),
        ("בְּאֹהֶל מוֹעֵד", "פי כ'בא אלמחצ'ר", "in the tent of assembly."),
    ],
    32: [
        # HE: וְלֹא-תִשְׂאוּ עָלָיו חֵטְא בַּהֲרִימְכֶם אֶת-חֶלְבּוֹ מִמֶּנּוּ וְאֶת-קָדְשֵׁי בְנֵי-יִשְׂרָאֵל לֹא תְחַלְּלוּ וְלֹא תָמוּתוּ
        # JA: ולא תחמלון עליה וזרא. ענד רפעכם אגודה מנה. ואקדאס בני אסראיל. לא תבד'לוהא ולא תהלכון
        # EN: And you shall bear no burden on account of it when you raise up the choicest of it; and the holy things of the sons of Israel you shall not treat lightly, lest you perish.'
        ("וְלֹא-תִשְׂאוּ", "ולא תחמלון", "And you shall bear"),
        ("עָלָיו", "עליה", "no burden on account of it"),
        ("חֵטְא", "וזרא", "when"),
        ("בַּהֲרִימְכֶם", "ענד רפעכם", "you raise up"),
        ("אֶת-חֶלְבּוֹ", "אגודה", "the choicest of it;"),
        ("מִמֶּנּוּ", "מנה", "and"),
        ("וְאֶת-קָדְשֵׁי", "ואקדאס", "the holy things of"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("לֹא תְחַלְּלוּ", "לא תבד'לוהא", "you shall not treat lightly,"),
        ("וְלֹא תָמוּתוּ", "ולא תהלכון", "lest you perish.'"),
    ],
}

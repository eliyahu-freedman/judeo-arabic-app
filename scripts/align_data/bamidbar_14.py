"""Hand-authored word-level alignment triples for Bamidbar chapter 14."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַתִּשָּׂא כָּל-הָעֵדָה וַיִּתְּנוּ אֶת-קוֹלָם וַיִּבְכּוּ הָעָם בַּלַּיְלָה הַהוּא
        # JA: ת'ם רפעת אלגמאעה אצואתהם. ובכו פי תלך אלילה
        # EN: Then the assembly raised their voices, and they wept in that night.
        (None, "ת'ם", "Then"),
        ("וַתִּשָּׂא", "רפעת", "the assembly raised"),
        ("כָּל-הָעֵדָה", "אלגמאעה", "their voices,"),
        ("אֶת-קוֹלָם", "אצואתהם", "and they"),
        ("וַיִּבְכּוּ", "ובכו", "wept"),
        ("הָעָם", "פי תלך", "in that"),
        ("בַּלַּיְלָה הַהוּא", "אלילה", "night."),
    ],
    2: [
        # HE: וַיִּלֹּנוּ עַל-מֹשֶׁה וְעַל-אַהֲרֹן כֹּל בְּנֵי יִשְׂרָאֵל וַיֹּאמְרוּ אֲלֵהֶם כָּל-הָעֵדָה לוּ-מַתְנוּ בְּאֶרֶץ מִצְרַיִם אוֹ בַּמִּדְבָּר הַזֶּה לוּ-מָתְנוּ
        # JA: פתד'מרו. עלי'' מוסי' והרון. גמאעה' בני אסראיל. וקאלא להם. יא ליתנא מתנא פי בלד מצר. או יא ליתנא מתנא פי הד'א אלבר
        # EN: And the congregation of the sons of Israel grumbled against Moses and Aaron, and said to them: 'Would that we had died in the land of Egypt — or would that we had died in this wilderness!'
        ("וַיִּלֹּנוּ", "פתד'מרו", "And the congregation of the sons of Israel grumbled"),
        ("עַל-מֹשֶׁה", "עלי'' מוסי'", "against Moses"),
        ("וְעַל-אַהֲרֹן", "והרון", "and Aaron,"),
        ("כֹּל בְּנֵי יִשְׂרָאֵל", "גמאעה' בני אסראיל", "and said to them:"),
        ("וַיֹּאמְרוּ", "וקאלא", "'Would that we had died"),
        ("אֲלֵהֶם", "להם", "in the land of Egypt —"),
        ("לוּ-מַתְנוּ", "יא ליתנא מתנא", "or would that we had died"),
        ("בְּאֶרֶץ מִצְרַיִם", "פי בלד מצר", "in this wilderness!'"),
        ("אוֹ", "או", ""),
        ("בַּמִּדְבָּר הַזֶּה לוּ-מָתְנוּ", "יא ליתנא מתנא פי הד'א אלבר", ""),
    ],
    3: [
        # HE: וְלָמָה יְהוָה מֵבִיא אֹתָנוּ אֶל-הָאָרֶץ הַזֹּאת לִנְפֹּל בַּחֶרֶב--נָשֵׁינוּ וְטַפֵּנוּ יִהְיוּ לָבַז הֲלוֹא טוֹב לָנוּ שׁוּב מִצְרָיְמָה
        # JA: ולם ידכ'לנא אללה. תלך אלבלד פנקע באלסיף. פיציר נסאנא ואטפאלנא ג'נימה. אלא אן אלאצלח לנא אלרגוע אלי' מצר
        # EN: 'And why would God bring us into that land, that we should fall by the sword, so that our wives and our children become spoil? Is it not better for us to return to Egypt?'
        ("וְלָמָה", "ולם", "'And why"),
        ("יְהוָה מֵבִיא אֹתָנוּ", "ידכ'לנא אללה", "would God bring us"),
        ("אֶל-הָאָרֶץ הַזֹּאת", "תלך אלבלד", "into that land,"),
        ("לִנְפֹּל", "פנקע", "that we should fall"),
        ("בַּחֶרֶב", "באלסיף", "by the sword,"),
        ("נָשֵׁינוּ", "פיציר נסאנא", "so that our wives"),
        ("וְטַפֵּנוּ", "ואטפאלנא", "and our children"),
        ("יִהְיוּ לָבַז", "ג'נימה", "become spoil?"),
        ("הֲלוֹא", "אלא אן", "Is it not"),
        ("טוֹב לָנוּ", "אלאצלח לנא", "better for us"),
        ("שׁוּב מִצְרָיְמָה", "אלרגוע אלי' מצר", "to return to Egypt?'"),
    ],
    4: [
        # HE: וַיֹּאמְרוּ אִישׁ אֶל-אָחִיו נִתְּנָה רֹאשׁ וְנָשׁוּבָה מִצְרָיְמָה
        # JA: ת'ם קאל בעצ'הם לבעץ'. נולי ריסא ונרגע אלי' מצר
        # EN: Then some of them said to one another: 'Let us appoint a head, and return to Egypt.'
        (None, "ת'ם", "Then"),
        ("וַיֹּאמְרוּ", "קאל", "some of them said"),
        ("אִישׁ", "בעצ'הם", "to one another:"),
        ("אֶל-אָחִיו", "לבעץ'", "'Let us appoint a head,"),
        ("נִתְּנָה רֹאשׁ", "נולי ריסא", "and return"),
        ("וְנָשׁוּבָה", "ונרגע", "to Egypt.'"),
        ("מִצְרָיְמָה", "אלי' מצר", ""),
    ],
    5: [
        # HE: וַיִּפֹּל מֹשֶׁה וְאַהֲרֹן עַל-פְּנֵיהֶם לִפְנֵי כָּל-קְהַל עֲדַת בְּנֵי יִשְׂרָאֵל
        # JA: פוקע מוסי' והרון עלי' וגוההמא. בחצ'רה' גוק גמאעה' בני אסראיל
        # EN: And Moses and Aaron fell upon their faces before the assembly of the congregation of the sons of Israel.
        ("וַיִּפֹּל", "פוקע", "And Moses and Aaron fell"),
        ("מֹשֶׁה", "מוסי'", "upon their faces"),
        ("וְאַהֲרֹן", "והרון", "before"),
        ("עַל-פְּנֵיהֶם", "עלי' וגוההמא", "the assembly of"),
        ("לִפְנֵי", "בחצ'רה'", "the congregation of"),
        ("כָּל-קְהַל", "גוק", "the sons of Israel."),
        ("עֲדַת", "גמאעה'", ""),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", ""),
    ],
    6: [
        # HE: וִיהוֹשֻׁעַ בִּן-נוּן וְכָלֵב בֶּן-יְפֻנֶּה מִן-הַתָּרִים אֶת-הָאָרֶץ--קָרְעוּ בִּגְדֵיהֶם
        # JA: ויהושע אבן נון. וכלב אבן יפנה. מן ראימי אלבלד. כ'רקא ת'יאבהמא
        # EN: And Joshua son of Nun, and Caleb son of Jephunneh — among those who had scouted the land — tore their garments.
        ("וִיהוֹשֻׁעַ", "ויהושע", "And Joshua"),
        ("בִּן-נוּן", "אבן נון", "son of Nun,"),
        ("וְכָלֵב", "וכלב", "and Caleb"),
        ("בֶּן-יְפֻנֶּה", "אבן יפנה", "son of Jephunneh —"),
        ("מִן-הַתָּרִים", "מן ראימי", "among those who had scouted"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land —"),
        ("קָרְעוּ", "כ'רקא", "tore"),
        ("בִּגְדֵיהֶם", "ת'יאבהמא", "their garments."),
    ],
    7: [
        # HE: וַיֹּאמְרוּ אֶל-כָּל-עֲדַת בְּנֵי-יִשְׂרָאֵל לֵאמֹר הָאָרֶץ אֲשֶׁר עָבַרְנוּ בָהּ לָתוּר אֹתָהּ--טוֹבָה הָאָרֶץ מְאֹד מְאֹד
        # JA: פקאלא. לגמאעה' בני אסראיל קאילין. אלבלד. אלד'י מררנאה לנרומה. בלד גייד גדא גדא
        # EN: And they said to the congregation of the sons of Israel, saying: 'The land which we passed through to seek it out — it is a very, very good land.'
        ("וַיֹּאמְרוּ", "פקאלא", "And they said"),
        ("אֶל-כָּל-עֲדַת", "לגמאעה'", "to the congregation of"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("לֵאמֹר", "קאילין", "saying:"),
        ("הָאָרֶץ", "אלבלד", "'The land"),
        ("אֲשֶׁר עָבַרְנוּ בָהּ", "אלד'י מררנאה", "which we passed through"),
        ("לָתוּר אֹתָהּ", "לנרומה", "to seek it out —"),
        ("טוֹבָה הָאָרֶץ", "בלד גייד", "it is a very, very good land.'"),
        ("מְאֹד מְאֹד", "גדא גדא", ""),
    ],
    8: [
        # HE: אִם-חָפֵץ בָּנוּ יְהוָה--וְהֵבִיא אֹתָנוּ אֶל-הָאָרֶץ הַזֹּאת וּנְתָנָהּ לָנוּ אֶרֶץ אֲשֶׁר-הִוא זָבַת חָלָב וּדְבָשׁ
        # JA: אן כאן ללה מראד פינא. אדכ'לנאה ווהבה לנא. בלד יפיץ' אללבן ואלעסל
        # EN: 'If God has a will toward us, He will bring us into it and give it to us as a gift — a land flowing with milk and honey.'
        ("אִם-חָפֵץ", "אן כאן", "'If"),
        ("יְהוָה", "ללה", "God has"),
        ("בָּנוּ", "מראד פינא", "a will toward us,"),
        ("וְהֵבִיא אֹתָנוּ", "אדכ'לנאה", "He will bring us into it"),
        ("אֶל-הָאָרֶץ הַזֹּאת", "ווהבה", "and give it"),
        ("וּנְתָנָהּ לָנוּ", "לנא", "to us as a gift —"),
        ("אֶרֶץ", "בלד", "a land"),
        ("זָבַת חָלָב", "יפיץ' אללבן", "flowing with milk"),
        ("וּדְבָשׁ", "ואלעסל", "and honey.'"),
    ],
    9: [
        # HE: אַךְ בַּיהוָה אַל-תִּמְרֹדוּ וְאַתֶּם אַל-תִּירְאוּ אֶת-עַם הָאָרֶץ כִּי לַחְמֵנוּ הֵם סָר צִלָּם מֵעֲלֵיהֶם וַיהוָה אִתָּנוּ אַל-תִּירָאֻם
        # JA: אמא עלי' אללה פלא תתד'מרון. ולא תכ'אפון אהל אלבלד. לאנהם טעאמנא. וסיזול צ'להם ענהם. ואללה מענא לא תכ'אפוהם
        # EN: 'Only do not grumble against God, and do not fear the people of the land, for they are our food; their shadow has already departed from them. And God is with us — do not fear them.'
        ("אַךְ", "אמא", "'Only do not grumble against God,"),
        ("בַּיהוָה", "עלי' אללה", "and do not fear"),
        ("אַל-תִּמְרֹדוּ", "פלא תתד'מרון", "the people of the land,"),
        ("וְאַתֶּם אַל-תִּירְאוּ", "ולא תכ'אפון", "for they are our food;"),
        ("אֶת-עַם הָאָרֶץ", "אהל אלבלד", "their shadow has already departed"),
        ("כִּי לַחְמֵנוּ הֵם", "לאנהם טעאמנא", "from them."),
        ("סָר צִלָּם", "וסיזול צ'להם", "And God is with us —"),
        ("מֵעֲלֵיהֶם", "ענהם", "do not fear them.'"),
        ("וַיהוָה", "ואללה", ""),
        ("אִתָּנוּ", "מענא", ""),
        ("אַל-תִּירָאֻם", "לא תכ'אפוהם", ""),
    ],
    10: [
        # HE: וַיֹּאמְרוּ כָּל-הָעֵדָה לִרְגּוֹם אֹתָם בָּאֲבָנִים וּכְבוֹד יְהוָה נִרְאָה בְּאֹהֶל מוֹעֵד אֶל-כָּל-בְּנֵי יִשְׂרָאֵל
        # JA: פכאד גמיע אלשעב. אן ירגמוהמא באלחגארה. ת'ם צ'הר נור אללה. פי כ'בא אלמחצ'ר. לגמיע בני אסראיל
        # EN: Then nearly all the people were about to stone the two of them. Then the light of God appeared in the Tent of Meeting before all the sons of Israel.
        ("וַיֹּאמְרוּ", "פכאד", "Then nearly all the people"),
        ("כָּל-הָעֵדָה", "גמיע אלשעב", "were about to stone the two of them."),
        ("לִרְגּוֹם אֹתָם", "אן ירגמוהמא", "Then"),
        ("בָּאֲבָנִים", "באלחגארה", "the light of God appeared"),
        ("וּכְבוֹד יְהוָה", "ת'ם צ'הר נור אללה", "in the Tent of Meeting"),
        ("נִרְאָה בְּאֹהֶל מוֹעֵד", "פי כ'בא אלמחצ'ר", "before all the sons of Israel."),
        ("אֶל-כָּל-בְּנֵי יִשְׂרָאֵל", "לגמיע בני אסראיל", ""),
    ],
    11: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה עַד-אָנָה יְנַאֲצֻנִי הָעָם הַזֶּה וְעַד-אָנָה לֹא-יַאֲמִינוּ בִי בְּכֹל הָאֹתוֹת אֲשֶׁר עָשִׂיתִי בְּקִרְבּוֹ
        # JA: פקאל אללה למוסי. אלי' כם יעצוני הולאי אלקום. ואלי' כם לם יומנון בי. מע גמיע אלאיאת. אלתי צנעתהא פי מא בינהם
        # EN: And God said to Moses: 'How long shall these people defy Me, and how long will they not believe in Me, despite all the signs which I performed among them?'
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי", "to Moses:"),
        ("עַד-אָנָה", "אלי' כם", "'How long shall these people defy Me,"),
        ("יְנַאֲצֻנִי", "יעצוני", "and how long will they not believe in Me,"),
        ("הָעָם הַזֶּה", "הולאי אלקום", "despite all the signs"),
        ("וְעַד-אָנָה", "ואלי' כם", "which I performed among them?'"),
        ("לֹא-יַאֲמִינוּ בִי", "לם יומנון בי", ""),
        ("בְּכֹל הָאֹתוֹת", "מע גמיע אלאיאת", ""),
        ("אֲשֶׁר עָשִׂיתִי", "אלתי צנעתהא", ""),
        ("בְּקִרְבּוֹ", "פי מא בינהם", ""),
    ],
    12: [
        # HE: אַכֶּנּוּ בַדֶּבֶר וְאוֹרִשֶׁנּוּ וְאֶעֱשֶׂה אֹתְךָ לְגוֹי-גָּדוֹל וְעָצוּם מִמֶּנּוּ
        # JA: יסתחקון אן אצ'רבהם באלובא ואקרצ'הם. ואגעל מנך. אמה אכת'ר וא עצ'ם מנהם
        # EN: 'They deserve that I strike them with pestilence and wear them down, and make of you a nation more numerous and mightier than they.'
        ("אַכֶּנּוּ", "יסתחקון אן אצ'רבהם", "'They deserve that I strike them"),
        ("בַדֶּבֶר", "באלובא", "with pestilence"),
        ("וְאוֹרִשֶׁנּוּ", "ואקרצ'הם", "and wear them down,"),
        ("וְאֶעֱשֶׂה אֹתְךָ", "ואגעל מנך", "and make of you"),
        ("לְגוֹי-גָּדוֹל", "אמה אכת'ר", "a nation more numerous"),
        ("וְעָצוּם מִמֶּנּוּ", "וא עצ'ם מנהם", "and mightier than they.'"),
    ],
    13: [
        # HE: וַיֹּאמֶר מֹשֶׁה אֶל-יְהוָה וְשָׁמְעוּ מִצְרַיִם כִּי-הֶעֱלִיתָ בְכֹחֲךָ אֶת-הָעָם הַזֶּה מִקִּרְבּוֹ
        # JA: פקאל מוסי' ללה. ויסמעון אלמצריון. אלד'י אצעדת הולאי אלקום מן בינהם בקדרתך
        # EN: And Moses said to God: 'Yet the Egyptians will hear — You who brought these people up from among them by Your power —'
        ("וַיֹּאמֶר מֹשֶׁה", "פקאל מוסי'", "And Moses said"),
        ("אֶל-יְהוָה", "ללה", "to God:"),
        ("וְשָׁמְעוּ", "ויסמעון", "'Yet the Egyptians will hear —"),
        ("מִצְרַיִם", "אלמצריון", "You who brought these people up"),
        ("כִּי-הֶעֱלִיתָ", "אלד'י אצעדת", "from among them"),
        ("אֶת-הָעָם הַזֶּה", "הולאי אלקום", "by Your power —'"),
        ("מִקִּרְבּוֹ", "מן בינהם", ""),
        ("בְכֹחֲךָ", "בקדרתך", ""),
    ],
    14: [
        # HE: וְאָמְרוּ אֶל-יוֹשֵׁב הָאָרֶץ הַזֹּאת שָׁמְעוּ כִּי-אַתָּה יְהוָה בְּקֶרֶב הָעָם הַזֶּה אֲשֶׁר-עַיִן בְּעַיִן נִרְאָה אַתָּה יְהוָה וַעֲנָנְךָ עֹמֵד עֲלֵהֶם וּבְעַמֻּד עָנָן אַתָּה הֹלֵךְ לִפְנֵיהֶם יוֹמָם וּבְעַמּוּד אֵשׁ לָיְלָה
        # JA: פיקולון מע אהל הד'א אלבלד. אלד'י סמעו אנך אללה. נורך פי מא בין הולאי אלקום. עין בעין ירונה. וג'מאמך מקים עליהם. ובעמוד ג'מאם תסיר בין ידיהם נהארא. ובעמוד נאר לילא
        # EN: 'and they will tell, together with the inhabitants of this land who have heard that You are God: Your light is among these people, seen eye to eye; and Your clouds rest upon them; and in a pillar of cloud You go before them by day, and in a pillar of fire by night.'
        ("וְאָמְרוּ", "פיקולון", "'and they will tell,"),
        ("אֶל-יוֹשֵׁב הָאָרֶץ הַזֹּאת", "מע אהל הד'א אלבלד", "together with the inhabitants of this land"),
        ("שָׁמְעוּ", "אלד'י סמעו", "who have heard"),
        ("כִּי-אַתָּה יְהוָה", "אנך אללה", "that You are God:"),
        ("בְּקֶרֶב הָעָם הַזֶּה", "נורך פי מא בין הולאי אלקום", "Your light is among these people,"),
        ("אֲשֶׁר-עַיִן בְּעַיִן", "עין בעין", "seen eye to eye;"),
        ("נִרְאָה אַתָּה יְהוָה", "ירונה", "and Your clouds rest upon them;"),
        ("וַעֲנָנְךָ", "וג'מאמך", "and in a pillar of cloud"),
        ("עֹמֵד עֲלֵהֶם", "מקים עליהם", "You go before them"),
        ("וּבְעַמֻּד עָנָן", "ובעמוד ג'מאם", "by day,"),
        ("אַתָּה הֹלֵךְ לִפְנֵיהֶם", "תסיר בין ידיהם", "and in a pillar of fire by night.'"),
        ("יוֹמָם", "נהארא", ""),
        ("וּבְעַמּוּד אֵשׁ לָיְלָה", "ובעמוד נאר לילא", ""),
    ],
    15: [
        # HE: וְהֵמַתָּה אֶת-הָעָם הַזֶּה כְּאִישׁ אֶחָד וְאָמְרוּ הַגּוֹיִם אֲשֶׁר-שָׁמְעוּ אֶת-שִׁמְעֲךָ לֵאמֹר
        # JA: פאד'א קתלתהם אגמעין כרג'ל ואחד. קאל גמיע אלאמם. אלד'י סמעו אכ'ברך הד'ה קאילין
        # EN: 'And if You slay them all as one man, then all the nations who have heard these reports of You will say:'
        ("וְהֵמַתָּה", "פאד'א קתלתהם", "'And if You slay them"),
        ("אֶת-הָעָם הַזֶּה", "אגמעין", "all"),
        ("כְּאִישׁ אֶחָד", "כרג'ל ואחד", "as one man,"),
        ("וְאָמְרוּ", "קאל", "then all the nations"),
        ("הַגּוֹיִם", "גמיע אלאמם", "who have heard these reports of You"),
        ("אֲשֶׁר-שָׁמְעוּ", "אלד'י סמעו", "will say:'"),
        ("אֶת-שִׁמְעֲךָ", "אכ'ברך הד'ה", ""),
        ("לֵאמֹר", "קאילין", ""),
    ],
    16: [
        # HE: מִבִּלְתִּי יְכֹלֶת יְהוָה לְהָבִיא אֶת-הָעָם הַזֶּה אֶל-הָאָרֶץ אֲשֶׁר-נִשְׁבַּע לָהֶם וַיִּשְׁחָטֵם בַּמִּדְבָּר
        # JA: ממא לם יטיק אלרב. אן ידכ'ל הולאי אלקום. אלי' אלבלד אלד'י ועדהם בה. פקתלהם פי אלבר
        # EN: 'It was because the Lord was unable to bring these people into the land which He had promised them — so He slew them in the wilderness.'
        ("מִבִּלְתִּי יְכֹלֶת", "ממא לם יטיק", "'It was because the Lord was unable"),
        ("יְהוָה", "אלרב", "to bring"),
        ("לְהָבִיא", "אן ידכ'ל", "these people"),
        ("אֶת-הָעָם הַזֶּה", "הולאי אלקום", "into the land"),
        ("אֶל-הָאָרֶץ", "אלי' אלבלד", "which He had promised them —"),
        ("אֲשֶׁר-נִשְׁבַּע לָהֶם", "אלד'י ועדהם בה", "so He slew them"),
        ("וַיִּשְׁחָטֵם", "פקתלהם", "in the wilderness.'"),
        ("בַּמִּדְבָּר", "פי אלבר", ""),
    ],
    17: [
        # HE: וְעַתָּה יִגְדַּל-נָא כֹּחַ אֲדֹנָי כַּאֲשֶׁר דִּבַּרְתָּ לֵאמֹר
        # JA: ואלאן יתביין עצ'ם קדרתך יא רב. כמא קלת לי
        # EN: 'And now, let the greatness of Your power be made manifest, O Lord, as You spoke to me.'
        ("וְעַתָּה", "ואלאן", "'And now,"),
        ("יִגְדַּל-נָא", "יתביין", "let the greatness of Your power be made manifest,"),
        ("כֹּחַ אֲדֹנָי", "עצ'ם קדרתך", "O Lord,"),
        (None, "יא רב", "as You spoke to me.'"),
        ("כַּאֲשֶׁר דִּבַּרְתָּ", "כמא קלת", ""),
        ("לֵאמֹר", "לי", ""),
    ],
    18: [
        # HE: יְהוָה אֶרֶךְ אַפַּיִם וְרַב-חֶסֶד נֹשֵׂא עָו‍ֹן וָפָשַׁע וְנַקֵּה לֹא יְנַקֶּה--פֹּקֵד עֲו‍ֹן אָבוֹת עַל-בָּנִים עַל-שִׁלֵּשִׁים וְעַל-רִבֵּעִים
        # JA: אנך אללה. טויל אלמהל כת'יר אלפצ'ל. ג'אפר אלד'נב ואלגרם. ויברי ולא יברי. מטאלב בד'נוב אלאבא מע אלבנין. ואלת'ואלת' ואלרואבע
        # EN: 'That You are God — long in forbearance, abounding in grace, forgiving iniquity together with transgression — and acquits, yet does not wholly acquit — visiting the iniquities of the fathers upon the sons, and upon the third and upon the fourth generation.'
        ("יְהוָה", "אנך אללה", "'That You are God —"),
        ("אֶרֶךְ אַפַּיִם", "טויל אלמהל", "long in forbearance,"),
        ("וְרַב-חֶסֶד", "כת'יר אלפצ'ל", "abounding in grace,"),
        ("נֹשֵׂא עָו‍ֹן", "ג'אפר אלד'נב", "forgiving iniquity"),
        ("וָפָשַׁע", "ואלגרם", "together with transgression —"),
        ("וְנַקֵּה", "ויברי", "and acquits,"),
        ("לֹא יְנַקֶּה", "ולא יברי", "yet does not wholly acquit —"),
        ("פֹּקֵד עֲו‍ֹן אָבוֹת", "מטאלב בד'נוב אלאבא", "visiting the iniquities of the fathers"),
        ("עַל-בָּנִים", "מע אלבנין", "upon the sons,"),
        ("עַל-שִׁלֵּשִׁים", "ואלת'ואלת'", "and upon the third"),
        ("וְעַל-רִבֵּעִים", "ואלרואבע", "and upon the fourth generation.'"),
    ],
    19: [
        # HE: סְלַח-נָא לַעֲו‍ֹן הָעָם הַזֶּה--כְּגֹדֶל חַסְדֶּךָ וְכַאֲשֶׁר נָשָׂאתָה לָעָם הַזֶּה מִמִּצְרַיִם וְעַד-הֵנָּה
        # JA: אצפח ד'נב הולאי אלקום בכת'רה' פצ'לך. וכמא אחתמלת להם. מן מצר ואלי' אלאן
        # EN: 'Pardon the iniquity of these people according to the abundance of Your grace, and as You have borne with them from Egypt until now.'
        ("סְלַח-נָא", "אצפח", "'Pardon"),
        ("לַעֲו‍ֹן", "ד'נב", "the iniquity of"),
        ("הָעָם הַזֶּה", "הולאי אלקום", "these people"),
        ("כְּגֹדֶל חַסְדֶּךָ", "בכת'רה' פצ'לך", "according to the abundance of Your grace,"),
        ("וְכַאֲשֶׁר נָשָׂאתָה", "וכמא אחתמלת", "and as You have borne"),
        ("לָעָם הַזֶּה", "להם", "with them"),
        ("מִמִּצְרַיִם", "מן מצר", "from Egypt"),
        ("וְעַד-הֵנָּה", "ואלי' אלאן", "until now.'"),
    ],
    20: [
        # HE: וַיֹּאמֶר יְהוָה סָלַחְתִּי כִּדְבָרֶךָ
        # JA: קאל אללה. קד צפחת ענהם אלמעאגלה כמא קלת
        # EN: And God said: 'I have pardoned them from immediate punishment, as you have said.'
        ("וַיֹּאמֶר יְהוָה", "קאל אללה", "And God said:"),
        ("סָלַחְתִּי", "קד צפחת ענהם", "'I have pardoned them"),
        (None, "אלמעאגלה", "from immediate punishment,"),
        ("כִּדְבָרֶךָ", "כמא קלת", "as you have said.'"),
    ],
    21: [
        # HE: וְאוּלָם חַי-אָנִי וְיִמָּלֵא כְבוֹד-יְהוָה אֶת-כָּל-הָאָרֶץ
        # JA: ולכן ובקאי אלדאים ונורי אלד'י ימלא גמיע אלעאלם
        # EN: 'Yet — by My eternal existence, and by My light which fills all the world —'
        ("וְאוּלָם", "ולכן", "'Yet —"),
        ("חַי-אָנִי", "ובקאי אלדאים", "by My eternal existence,"),
        ("וְיִמָּלֵא", "ונורי", "and by My light"),
        ("כְבוֹד-יְהוָה", "אלד'י ימלא", "which fills"),
        ("אֶת-כָּל-הָאָרֶץ", "גמיע אלעאלם", "all the world —'"),
    ],
    22: [
        # HE: כִּי כָל-הָאֲנָשִׁים הָרֹאִים אֶת-כְּבֹדִי וְאֶת-אֹתֹתַי אֲשֶׁר-עָשִׂיתִי בְמִצְרַיִם וּבַמִּדְבָּר וַיְנַסּוּ אֹתִי זֶה עֶשֶׂר פְּעָמִים וְלֹא שָׁמְעוּ בְּקוֹלִי
        # JA: אן גמיע אלרגאל. אלד'י ראו כרמי ואיאתי. אלתי צנעתהא פי מצר ופי אלבר. ואמתחנוני הד'ה אלמרה אלעשארה. ולם יקבלו אמרי
        # EN: 'Surely all the men who saw My generosity and My signs which I performed in Egypt and in the wilderness, and who tested Me now this tenth time, and did not accept My command —'
        ("כִּי", "אן", "'Surely"),
        ("כָל-הָאֲנָשִׁים", "גמיע אלרגאל", "all the men"),
        ("הָרֹאִים אֶת-כְּבֹדִי", "אלד'י ראו כרמי", "who saw My generosity"),
        ("וְאֶת-אֹתֹתַי", "ואיאתי", "and My signs"),
        ("אֲשֶׁר-עָשִׂיתִי", "אלתי צנעתהא", "which I performed"),
        ("בְמִצְרַיִם", "פי מצר", "in Egypt"),
        ("וּבַמִּדְבָּר", "ופי אלבר", "and in the wilderness,"),
        ("וַיְנַסּוּ אֹתִי", "ואמתחנוני", "and who tested Me"),
        ("זֶה עֶשֶׂר פְּעָמִים", "הד'ה אלמרה אלעשארה", "now this tenth time,"),
        ("וְלֹא שָׁמְעוּ בְּקוֹלִי", "ולם יקבלו אמרי", "and did not accept My command —'"),
    ],
    23: [
        # HE: אִם-יִרְאוּ אֶת-הָאָרֶץ אֲשֶׁר נִשְׁבַּעְתִּי לַאֲבֹתָם וְכָל-מְנַאֲצַי לֹא יִרְאוּהָ
        # JA: אן ראו אלבלד. אלד'י אקסמת לאבאיהם. וכדאלך כל מן יעציני לא יראה
        # EN: 'they shall not see the land which I swore to their fathers; and likewise every one who defies Me shall not see it.'
        ("אִם-יִרְאוּ", "אן ראו", "'they shall not see"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר נִשְׁבַּעְתִּי", "אלד'י אקסמת", "which I swore"),
        ("לַאֲבֹתָם", "לאבאיהם", "to their fathers;"),
        (None, "וכדאלך", "and likewise"),
        ("וְכָל-מְנַאֲצַי", "כל מן יעציני", "every one who defies Me"),
        ("לֹא יִרְאוּהָ", "לא יראה", "shall not see it.'"),
    ],
    24: [
        # HE: וְעַבְדִּי כָלֵב עֵקֶב הָיְתָה רוּחַ אַחֶרֶת עִמּוֹ וַיְמַלֵּא אַחֲרָי--וַהֲבִיאֹתִיו אֶל-הָאָרֶץ אֲשֶׁר-בָּא שָׁמָּה וְזַרְעוֹ יוֹרִשֶׁנָּה
        # JA: ואמא עבדי כלב. פגזא מא כאן לה ראי אכ'ר. אתבע בה טאעתי. לאדכ'לה אלי' אלבלד אלד'י צאר אליה. ולנסלה יורתה
        # EN: 'But My servant Caleb — as recompense for his having held a different view, following obedience to Me thereby — him I will bring into the land which he reached, and for his offspring he shall pass it on as an inheritance.'
        ("וְעַבְדִּי", "ואמא עבדי", "'But My servant"),
        ("כָלֵב", "כלב", "Caleb —"),
        ("עֵקֶב", "פגזא", "as recompense"),
        ("הָיְתָה רוּחַ אַחֶרֶת עִמּוֹ", "מא כאן לה ראי אכ'ר", "for his having held a different view,"),
        ("וַיְמַלֵּא אַחֲרָי", "אתבע בה טאעתי", "following obedience to Me thereby —"),
        ("וַהֲבִיאֹתִיו", "לאדכ'לה", "him I will bring"),
        ("אֶל-הָאָרֶץ", "אלי' אלבלד", "into the land"),
        ("אֲשֶׁר-בָּא שָׁמָּה", "אלד'י צאר אליה", "which he reached,"),
        ("וְזַרְעוֹ", "ולנסלה", "and for his offspring"),
        ("יוֹרִשֶׁנָּה", "יורתה", "he shall pass it on as an inheritance.'"),
    ],
    25: [
        # HE: וְהָעֲמָלֵקִי וְהַכְּנַעֲנִי יוֹשֵׁב בָּעֵמֶק מָחָר פְּנוּ וּסְעוּ לָכֶם הַמִּדְבָּר--דֶּרֶךְ יַם-סוּף
        # JA: ואלאן פאלעמלאקיין ואלכנעאניין מקימין פי אלמרג. פולו מן ג'ד וארחלו. אלי' אלבר טריק בחר אלקלזם
        # EN: 'And now, the Amalekites and the Canaanites are dwelling in the valley. Turn back tomorrow and set out into the wilderness by the way of the Sea of Qulzum.'
        ("וְהָעֲמָלֵקִי", "ואלאן פאלעמלאקיין", "'And now, the Amalekites"),
        ("וְהַכְּנַעֲנִי", "ואלכנעאניין", "and the Canaanites"),
        ("יוֹשֵׁב בָּעֵמֶק", "מקימין פי אלמרג", "are dwelling in the valley."),
        ("מָחָר פְּנוּ", "פולו מן ג'ד", "Turn back tomorrow"),
        ("וּסְעוּ לָכֶם", "וארחלו", "and set out"),
        ("הַמִּדְבָּר", "אלי' אלבר", "into the wilderness"),
        ("דֶּרֶךְ יַם-סוּף", "טריק בחר אלקלזם", "by the way of the Sea of Qulzum.'"),
    ],
    26: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה וְאֶל-אַהֲרֹן לֵאמֹר
        # JA: ת'ם כלם אללה מוסי' והרון תכלימא
        # EN: Then God spoke to Moses and Aaron, saying:
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי'", "and Aaron,"),
        ("וְאֶל-אַהֲרֹן", "והרון", "saying:"),
        ("לֵאמֹר", "תכלימא", ""),
    ],
    27: [
        # HE: עַד-מָתַי לָעֵדָה הָרָעָה הַזֹּאת אֲשֶׁר הֵמָּה מַלִּינִים עָלָי אֶת-תְּלֻנּוֹת בְּנֵי יִשְׂרָאֵל אֲשֶׁר הֵמָּה מַלִּינִים עָלַי--שָׁמָעְתִּי
        # JA: אלי' כם אבקי הד'ה אלגמאעה אלרדייה. אלד'י ד'מרת אלאמה עליי. לקד סמעת תד'מר בני אסראיל. אלד'י תד'מרו עליי
        # EN: 'How long shall I leave this wicked congregation, which has incited the nation against Me? I have indeed heard the grumbling of the sons of Israel, who grumbled against Me.'
        ("עַד-מָתַי", "אלי' כם", "'How long"),
        (None, "אבקי", "shall I leave"),
        ("לָעֵדָה הָרָעָה הַזֹּאת", "הד'ה אלגמאעה אלרדייה", "this wicked congregation,"),
        ("אֲשֶׁר הֵמָּה מַלִּינִים עָלָי", "אלד'י ד'מרת אלאמה עליי", "which has incited the nation against Me?"),
        ("שָׁמָעְתִּי", "לקד סמעת", "I have indeed heard"),
        ("אֶת-תְּלֻנּוֹת", "תד'מר", "the grumbling of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("אֲשֶׁר הֵמָּה מַלִּינִים עָלַי", "אלד'י תד'מרו עליי", "who grumbled against Me.'"),
    ],
    28: [
        # HE: אֱמֹר אֲלֵהֶם חַי-אָנִי נְאֻם-יְהוָה אִם-לֹא כַּאֲשֶׁר דִּבַּרְתֶּם בְּאָזְנָי כֵּן אֶעֱשֶׂה לָכֶם
        # JA: אלא קל להם. ובקאי אלדאים יקול אללה. אן לם אצנע בכם. כמא קלתם בחצ'רתי
        # EN: 'Say to them: By My eternal existence — says God — if I do not deal with you as you have said in My presence!'
        ("אֱמֹר", "אלא קל", "'Say to them:"),
        ("אֲלֵהֶם", "להם", "By My eternal existence —"),
        ("חַי-אָנִי", "ובקאי אלדאים", "says God —"),
        ("נְאֻם-יְהוָה", "יקול אללה", "if I do not deal with you"),
        ("אִם-לֹא", "אן לם", "as you have said"),
        ("כַּאֲשֶׁר דִּבַּרְתֶּם", "אצנע בכם. כמא קלתם", "in My presence!'"),
        ("בְּאָזְנָי", "בחצ'רתי", ""),
    ],
    29: [
        # HE: בַּמִּדְבָּר הַזֶּה יִפְּלוּ פִגְרֵיכֶם וְכָל-פְּקֻדֵיכֶם לְכָל-מִסְפַּרְכֶם מִבֶּן עֶשְׂרִים שָׁנָה וָמָעְלָה אֲשֶׁר הֲלִינֹתֶם עָלָי
        # JA: ופי הד'א אלבר תקע אגסאדכם. מן כל מעדוד ומחצא מנכם. מן אבן עשרין סנה פצאעדא. כמא תד'מרתם עליי
        # EN: 'In this wilderness shall your bodies fall — from every one counted and numbered among you, from twenty years of age and upward — even as you grumbled against Me.'
        ("בַּמִּדְבָּר הַזֶּה", "ופי הד'א אלבר", "'In this wilderness shall your bodies fall —"),
        ("יִפְּלוּ", "תקע", "from every one counted"),
        ("פִגְרֵיכֶם", "אגסאדכם", "and numbered among you,"),
        ("וְכָל-פְּקֻדֵיכֶם", "מן כל מעדוד", "from twenty years of age"),
        ("לְכָל-מִסְפַּרְכֶם", "ומחצא מנכם", "and upward —"),
        ("מִבֶּן עֶשְׂרִים שָׁנָה", "מן אבן עשרין סנה", "even as you grumbled against Me.'"),
        ("וָמָעְלָה", "פצאעדא", ""),
        ("אֲשֶׁר הֲלִינֹתֶם עָלָי", "כמא תד'מרתם עליי", ""),
    ],
    30: [
        # HE: אִם-אַתֶּם תָּבֹאוּ אֶל-הָאָרֶץ אֲשֶׁר נָשָׂאתִי אֶת-יָדִי לְשַׁכֵּן אֶתְכֶם בָּהּ--כִּי אִם-כָּלֵב בֶּן-יְפֻנֶּה וִיהוֹשֻׁעַ בִּן-נוּן
        # JA: אן אנתם דכ'לתם אלבלד. אלד'י אקסמת באמרי. אן אסכנכם פיה. אלא כלב אבן יפנה. ויהושע אבן נון
        # EN: 'You shall not enter the land concerning which I swore by My word to settle you in it — except Caleb son of Jephunneh and Joshua son of Nun.'
        ("אִם-אַתֶּם תָּבֹאוּ", "אן אנתם דכ'לתם", "'You shall not enter"),
        ("אֶל-הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר נָשָׂאתִי", "אלד'י אקסמת", "concerning which I swore"),
        ("אֶת-יָדִי", "באמרי", "by My word"),
        ("לְשַׁכֵּן אֶתְכֶם בָּהּ", "אן אסכנכם פיה", "to settle you in it —"),
        ("כִּי אִם-כָּלֵב", "אלא כלב", "except Caleb"),
        ("בֶּן-יְפֻנֶּה", "אבן יפנה", "son of Jephunneh"),
        ("וִיהוֹשֻׁעַ", "ויהושע", "and Joshua"),
        ("בִּן-נוּן", "אבן נון", "son of Nun.'"),
    ],
    31: [
        # HE: וְטַפְּכֶם--אֲשֶׁר אֲמַרְתֶּם לָבַז יִהְיֶה וְהֵבֵיאתִי אֹתָם--וְיָדְעוּ אֶת-הָאָרֶץ אֲשֶׁר מְאַסְתֶּם בָּהּ
        # JA: ואטפאלכם. אלד'י קלתם אנהם יצירו ג'נימה. פאני אדכ'להם. חתא יערפון פצ'ילה' אלבלד. אלד'י זהדתם פיה
        # EN: 'And your children, whom you said would become spoil — them I will bring in, so that they may know the excellence of the land which you have despised.'
        ("וְטַפְּכֶם", "ואטפאלכם", "'And your children,"),
        ("אֲשֶׁר אֲמַרְתֶּם", "אלד'י קלתם", "whom you said"),
        ("לָבַז יִהְיֶה", "אנהם יצירו ג'נימה", "would become spoil —"),
        ("וְהֵבֵיאתִי אֹתָם", "פאני אדכ'להם", "them I will bring in,"),
        ("וְיָדְעוּ", "חתא יערפון", "so that they may know"),
        ("אֶת-הָאָרֶץ", "פצ'ילה' אלבלד", "the excellence of the land"),
        ("אֲשֶׁר מְאַסְתֶּם בָּהּ", "אלד'י זהדתם פיה", "which you have despised.'"),
    ],
    32: [
        # HE: וּפִגְרֵיכֶם אַתֶּם--יִפְּלוּ בַּמִּדְבָּר הַזֶּה
        # JA: אמא אגסאדכם אנתם. פתקע פי הד'א אלבר
        # EN: 'But your bodies — you yourselves — shall fall in this wilderness.'
        ("וּפִגְרֵיכֶם", "אמא אגסאדכם", "'But your bodies —"),
        ("אַתֶּם", "אנתם", "you yourselves —"),
        ("יִפְּלוּ", "פתקע", "shall fall"),
        ("בַּמִּדְבָּר הַזֶּה", "פי הד'א אלבר", "in this wilderness.'"),
    ],
    33: [
        # HE: וּבְנֵיכֶם יִהְיוּ רֹעִים בַּמִּדְבָּר אַרְבָּעִים שָׁנָה וְנָשְׂאוּ אֶת-זְנוּתֵיכֶם--עַד-תֹּם פִּגְרֵיכֶם בַּמִּדְבָּר
        # JA: ובניכם. יקימון תאיהין פי אלבר ארבעין סנה. ויחמלון טג'יאנכם. אלי'' פנא אגסאדכם פיה
        # EN: 'And your sons shall remain wandering in the wilderness forty years, and shall bear the burden of your rebellion — until the perishing of your bodies therein.'
        ("וּבְנֵיכֶם", "ובניכם", "'And your sons"),
        ("יִהְיוּ רֹעִים", "יקימון תאיהין", "shall remain wandering"),
        ("בַּמִּדְבָּר", "פי אלבר", "in the wilderness"),
        ("אַרְבָּעִים שָׁנָה", "ארבעין סנה", "forty years,"),
        ("וְנָשְׂאוּ", "ויחמלון", "and shall bear"),
        ("אֶת-זְנוּתֵיכֶם", "טג'יאנכם", "the burden of your rebellion —"),
        ("עַד-תֹּם", "אלי'' פנא", "until the perishing of"),
        ("פִּגְרֵיכֶם בַּמִּדְבָּר", "אגסאדכם פיה", "your bodies therein.'"),
    ],
    34: [
        # HE: בְּמִסְפַּר הַיָּמִים אֲשֶׁר-תַּרְתֶּם אֶת-הָאָרֶץ אַרְבָּעִים יוֹם--יוֹם לַשָּׁנָה יוֹם לַשָּׁנָה תִּשְׂאוּ אֶת-עֲו‍ֹנֹתֵיכֶם אַרְבָּעִים שָׁנָה וִידַעְתֶּם אֶת-תְּנוּאָתִי
        # JA: באחצא אלאייאם. אלד'י רמתם אלבלד פיהא ארבעין יומא. לכל יום סנה. תחמלון אוזארכם. אלי' תמאם ארבעין סנה. פתערפון מוצ'ע אענאתי
        # EN: 'By the count of the days in which you sought out the land — forty days, a year for each day — you shall bear your burdens for a full forty years, and you shall come to know the consequence of My displeasure.'
        ("בְּמִסְפַּר הַיָּמִים", "באחצא אלאייאם", "'By the count of the days"),
        ("אֲשֶׁר-תַּרְתֶּם", "אלד'י רמתם", "in which you sought out"),
        ("אֶת-הָאָרֶץ", "אלבלד פיהא", "the land —"),
        ("אַרְבָּעִים יוֹם", "ארבעין יומא", "forty days,"),
        ("יוֹם לַשָּׁנָה", "לכל יום סנה", "a year for each day —"),
        ("תִּשְׂאוּ אֶת-עֲו‍ֹנֹתֵיכֶם", "תחמלון אוזארכם", "you shall bear your burdens"),
        ("אַרְבָּעִים שָׁנָה", "אלי' תמאם ארבעין סנה", "for a full forty years,"),
        ("וִידַעְתֶּם", "פתערפון", "and you shall come to know"),
        ("אֶת-תְּנוּאָתִי", "מוצ'ע אענאתי", "the consequence of My displeasure.'"),
    ],
    35: [
        # HE: אֲנִי יְהוָה דִּבַּרְתִּי אִם-לֹא זֹאת אֶעֱשֶׂה לְכָל-הָעֵדָה הָרָעָה הַזֹּאת הַנּוֹעָדִים עָלָי בַּמִּדְבָּר הַזֶּה יִתַּמּוּ וְשָׁם יָמֻתוּ
        # JA: אנא אללה קלת ד'אלך ואצנעה. בגמיע הד'ה אלגמאעה אלרדייה. אלמגתמעה עליי. פי הד'א אלבר יפנון באלמות
        # EN: 'I, God, have spoken this and I will do it — against all this wicked congregation, gathered against Me: in this wilderness they shall perish by death.'
        ("אֲנִי יְהוָה", "אנא אללה", "'I, God,"),
        ("דִּבַּרְתִּי", "קלת ד'אלך", "have spoken this"),
        ("אִם-לֹא זֹאת אֶעֱשֶׂה", "ואצנעה", "and I will do it —"),
        ("לְכָל-הָעֵדָה הָרָעָה הַזֹּאת", "בגמיע הד'ה אלגמאעה אלרדייה", "against all this wicked congregation,"),
        ("הַנּוֹעָדִים עָלָי", "אלמגתמעה עליי", "gathered against Me:"),
        ("בַּמִּדְבָּר הַזֶּה", "פי הד'א אלבר", "in this wilderness"),
        ("יִתַּמּוּ", "יפנון", "they shall perish"),
        ("וְשָׁם יָמֻתוּ", "באלמות", "by death.'"),
    ],
    36: [
        # HE: וְהָאֲנָשִׁים אֲשֶׁר-שָׁלַח מֹשֶׁה לָתוּר אֶת-הָאָרֶץ וַיָּשֻׁבוּ וילונו (וַיַּלִּינוּ) עָלָיו אֶת-כָּל-הָעֵדָה לְהוֹצִיא דִבָּה עַל-הָאָרֶץ
        # JA: ואלרגאל אלד'י בעת' בהם מוסי' לירומו אלבלד. פרגעו וד'מרו עליה אלגמאעה. ואכ'רגו שנאעה עלי' אלבלד
        # EN: And the men whom Moses had sent to seek out the land — who returned and incited the congregation against him, and spread a reproach upon the land —
        ("וְהָאֲנָשִׁים", "ואלרגאל", "And the men"),
        ("אֲשֶׁר-שָׁלַח מֹשֶׁה", "אלד'י בעת' בהם מוסי'", "whom Moses had sent"),
        ("לָתוּר אֶת-הָאָרֶץ", "לירומו אלבלד", "to seek out the land —"),
        ("וַיָּשֻׁבוּ", "פרגעו", "who returned"),
        ("וילונו (וַיַּלִּינוּ) עָלָיו", "וד'מרו עליה", "and incited the congregation against him,"),
        ("אֶת-כָּל-הָעֵדָה", "אלגמאעה", "and spread a reproach"),
        ("לְהוֹצִיא דִבָּה", "ואכ'רגו שנאעה", "upon the land —"),
        ("עַל-הָאָרֶץ", "עלי' אלבלד", ""),
    ],
    37: [
        # HE: וַיָּמֻתוּ הָאֲנָשִׁים מוֹצִאֵי דִבַּת-הָאָרֶץ רָעָה--בַּמַּגֵּפָה לִפְנֵי יְהוָה
        # JA: פמאת אולאיך אלרגאל. באלצדאם בין ידי אללה
        # EN: those men died by a blow before God.
        ("וַיָּמֻתוּ", "פמאת", "those men died"),
        ("הָאֲנָשִׁים מוֹצִאֵי דִבַּת-הָאָרֶץ רָעָה", "אולאיך אלרגאל", "by a blow"),
        ("בַּמַּגֵּפָה", "באלצדאם", "before God."),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", ""),
    ],
    38: [
        # HE: וִיהוֹשֻׁעַ בִּן-נוּן וְכָלֵב בֶּן-יְפֻנֶּה חָיוּ מִן-הָאֲנָשִׁים הָהֵם הַהֹלְכִים לָתוּר אֶת-הָאָרֶץ
        # JA: ויהושע אבן נון. וכלב אבן יפונה. עאשו מן ג'מלה' אלרגאל. אלד'י מצ'ו לירומו אלבלד
        # EN: But Joshua son of Nun and Caleb son of Jephunneh lived, from among the men who had gone to seek out the land.
        ("וִיהוֹשֻׁעַ", "ויהושע", "But Joshua"),
        ("בִּן-נוּן", "אבן נון", "son of Nun"),
        ("וְכָלֵב", "וכלב", "and Caleb"),
        ("בֶּן-יְפֻנֶּה", "אבן יפונה", "son of Jephunneh"),
        ("חָיוּ", "עאשו", "lived,"),
        ("מִן-הָאֲנָשִׁים הָהֵם", "מן ג'מלה' אלרגאל", "from among the men"),
        ("הַהֹלְכִים לָתוּר", "אלד'י מצ'ו לירומו", "who had gone to seek out"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land."),
    ],
    39: [
        # HE: וַיְדַבֵּר מֹשֶׁה אֶת-הַדְּבָרִים הָאֵלֶּה אֶל-כָּל-בְּנֵי יִשְׂרָאֵל וַיִּתְאַבְּלוּ הָעָם מְאֹד
        # JA: ולמא כלם מוסי'' בהד'א אלכלאם. גמאעה' בני אסראיל. פחזן אלקום גדא
        # EN: And when Moses spoke these words to the congregation of the sons of Israel, the people grieved greatly.
        ("וַיְדַבֵּר", "ולמא כלם", "And when Moses spoke"),
        ("מֹשֶׁה", "מוסי''", "these words"),
        ("אֶת-הַדְּבָרִים הָאֵלֶּה", "בהד'א אלכלאם", "to the congregation of"),
        ("אֶל-כָּל-בְּנֵי יִשְׂרָאֵל", "גמאעה' בני אסראיל", "the sons of Israel,"),
        ("וַיִּתְאַבְּלוּ הָעָם", "פחזן אלקום", "the people grieved"),
        ("מְאֹד", "גדא", "greatly."),
    ],
    40: [
        # HE: וַיַּשְׁכִּמוּ בַבֹּקֶר וַיַּעֲלוּ אֶל-רֹאשׁ-הָהָר לֵאמֹר הִנֶּנּוּ וְעָלִינוּ אֶל-הַמָּקוֹם אֲשֶׁר-אָמַר יְהוָה--כִּי חָטָאנוּ
        # JA: ואדלגו באלג'דאה. וצעדו אלי' ראס אלגבל וקאלו. הא נחן צאעדין. אלי' אלמוצ'ע. אלד'י אמרנא אללה פקד אכ'טאנא
        # EN: And they rose early in the morning and went up to the top of the mountain, and said: 'Here we are, and we will go up to the place which God commanded us — for we have indeed sinned.'
        ("וַיַּשְׁכִּמוּ", "ואדלגו", "And they rose early"),
        ("בַבֹּקֶר", "באלג'דאה", "in the morning"),
        ("וַיַּעֲלוּ", "וצעדו", "and went up"),
        ("אֶל-רֹאשׁ-הָהָר", "אלי' ראס אלגבל", "to the top of the mountain,"),
        ("לֵאמֹר", "וקאלו", "and said:"),
        ("הִנֶּנּוּ", "הא נחן", "'Here we are,"),
        ("וְעָלִינוּ", "צאעדין", "and we will go up"),
        ("אֶל-הַמָּקוֹם", "אלי' אלמוצ'ע", "to the place"),
        ("אֲשֶׁר-אָמַר יְהוָה", "אלד'י אמרנא אללה", "which God commanded us —"),
        ("כִּי חָטָאנוּ", "פקד אכ'טאנא", "for we have indeed sinned.'"),
    ],
    41: [
        # HE: וַיֹּאמֶר מֹשֶׁה לָמָּה זֶּה אַתֶּם עֹבְרִים אֶת-פִּי יְהוָה וְהִוא לֹא תִצְלָח
        # JA: קאל להם מוסי'. יא קום לא תתגאוזו אמר אללה. פאנהא לא תנגח
        # EN: Moses said to them: 'O people, do not transgress the command of God — for it will not succeed.'
        ("וַיֹּאמֶר מֹשֶׁה", "קאל להם מוסי'", "Moses said to them:"),
        (None, "יא קום", "'O people,"),
        ("לָמָּה זֶּה אַתֶּם עֹבְרִים", "לא תתגאוזו", "do not transgress"),
        ("אֶת-פִּי יְהוָה", "אמר אללה", "the command of God —"),
        ("וְהִוא לֹא תִצְלָח", "פאנהא לא תנגח", "for it will not succeed.'"),
    ],
    42: [
        # HE: אַל-תַּעֲלוּ כִּי אֵין יְהוָה בְּקִרְבְּכֶם וְלֹא תִּנָּגְפוּ לִפְנֵי אֹיְבֵיכֶם
        # JA: לא תצעדו. אן נור אללה ליס הו מעכם. ולא תנצדמו. בין ידי אעדאיכם
        # EN: 'Do not go up — for the light of God is not with you — lest you be struck down before your enemies.'
        ("אַל-תַּעֲלוּ", "לא תצעדו", "'Do not go up —"),
        ("כִּי אֵין יְהוָה", "אן נור אללה", "for the light of God"),
        ("בְּקִרְבְּכֶם", "ליס הו מעכם", "is not with you —"),
        ("וְלֹא תִּנָּגְפוּ", "ולא תנצדמו", "lest you be struck down"),
        ("לִפְנֵי אֹיְבֵיכֶם", "בין ידי אעדאיכם", "before your enemies.'"),
    ],
    43: [
        # HE: כִּי הָעֲמָלֵקִי וְהַכְּנַעֲנִי שָׁם לִפְנֵיכֶם וּנְפַלְתֶּם בֶּחָרֶב כִּי-עַל-כֵּן שַׁבְתֶּם מֵאַחֲרֵי יְהוָה וְלֹא-יִהְיֶה יְהוָה עִמָּכֶם
        # JA: פאן אלעמאלקה ואלכנעאניין ת'ם בין אידיכם. פתקעון באלסיף. לאנכם רגעתם ען טאעה' אללה. פלא יכון אללה מעכם
        # EN: 'For the Amalekites and the Canaanites are there before you, and you will fall by the sword — because you have turned back from obedience to God, and God will not be with you.'
        ("כִּי הָעֲמָלֵקִי", "פאן אלעמאלקה", "'For the Amalekites"),
        ("וְהַכְּנַעֲנִי", "ואלכנעאניין", "and the Canaanites"),
        ("שָׁם לִפְנֵיכֶם", "ת'ם בין אידיכם", "are there before you,"),
        ("וּנְפַלְתֶּם", "פתקעון", "and you will fall"),
        ("בֶּחָרֶב", "באלסיף", "by the sword —"),
        ("כִּי-עַל-כֵּן שַׁבְתֶּם", "לאנכם רגעתם", "because you have turned back"),
        ("מֵאַחֲרֵי יְהוָה", "ען טאעה' אללה", "from obedience to God,"),
        ("וְלֹא-יִהְיֶה יְהוָה", "פלא יכון אללה", "and God will not be"),
        ("עִמָּכֶם", "מעכם", "with you.'"),
    ],
    44: [
        # HE: וַיַּעְפִּלוּ לַעֲלוֹת אֶל-רֹאשׁ הָהָר וַאֲרוֹן בְּרִית-יְהוָה וּמֹשֶׁה לֹא-מָשׁוּ מִקֶּרֶב הַמַּחֲנֶה
        # JA: פאעתדו. וצעדו אלי' ראס אלגבל. וצנדוק עהד אללה ומוסי. לם יזולא מן וסט אלעסכר
        # EN: Yet they acted presumptuously and went up to the top of the mountain; but the ark of the covenant of God and Moses did not stir from the midst of the camp.
        ("וַיַּעְפִּלוּ", "פאעתדו", "Yet they acted presumptuously"),
        ("לַעֲלוֹת", "וצעדו", "and went up"),
        ("אֶל-רֹאשׁ הָהָר", "אלי' ראס אלגבל", "to the top of the mountain;"),
        ("וַאֲרוֹן בְּרִית-יְהוָה", "וצנדוק עהד אללה", "but the ark of the covenant of God"),
        ("וּמֹשֶׁה", "ומוסי", "and Moses"),
        ("לֹא-מָשׁוּ", "לם יזולא", "did not stir"),
        ("מִקֶּרֶב הַמַּחֲנֶה", "מן וסט אלעסכר", "from the midst of the camp."),
    ],
    45: [
        # HE: וַיֵּרֶד הָעֲמָלֵקִי וְהַכְּנַעֲנִי הַיֹּשֵׁב בָּהָר הַהוּא וַיַּכּוּם וַיַּכְּתוּם עַד-הַחָרְמָה
        # JA: פנזל אלעמלאקיין ואלכנעאניין. אלמקימין פי ד'אלך אלגבל. פצ'רבוהם וחטמוהם אלי' חרמה
        # EN: And the Amalekites and the Canaanites who dwelt in that mountain came down, and struck them and shattered them as far as Hormah.
        ("וַיֵּרֶד הָעֲמָלֵקִי", "פנזל אלעמלאקיין", "And the Amalekites and the Canaanites"),
        ("וְהַכְּנַעֲנִי", "ואלכנעאניין", "who dwelt in that mountain came down,"),
        ("הַיֹּשֵׁב בָּהָר הַהוּא", "אלמקימין פי ד'אלך אלגבל", "and struck them"),
        ("וַיַּכּוּם", "פצ'רבוהם", "and shattered them"),
        ("וַיַּכְּתוּם", "וחטמוהם", "as far as Hormah."),
        ("עַד-הַחָרְמָה", "אלי' חרמה", ""),
    ],
}

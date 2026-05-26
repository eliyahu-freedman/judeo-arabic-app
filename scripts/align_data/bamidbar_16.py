"""Hand-authored word-level alignment triples for Bamidbar chapter 16."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיִּקַּח קֹרַח בֶּן-יִצְהָר בֶּן-קְהָת בֶּן-לֵוִי וְדָתָן וַאֲבִירָם בְּנֵי אֱלִיאָב וְאוֹן בֶּן-פֶּלֶת--בְּנֵי רְאוּבֵן
        # JA: פתקדם קרח. אבן יצהר אבן קהת אבן לוי. ודתן ואבירם. אבני אליאב. ואון אבן פלת מן בני ראובן
        # EN: And Korah — son of Izhar, son of Kohath, son of Levi — came forward; and Dathan and Abiram, sons of Eliab, and On son of Peleth, of the sons of Reuben.
        ("וַיִּקַּח", "פתקדם", "And"),
        ("קֹרַח", "קרח", "Korah —"),
        ("בֶּן-יִצְהָר", "אבן יצהר", "son of Izhar,"),
        ("בֶּן-קְהָת", "אבן קהת", "son of Kohath,"),
        ("בֶּן-לֵוִי", "אבן לוי", "son of Levi —"),
        (None, ".", "came forward;"),
        ("וְדָתָן", "ודתן", "and Dathan"),
        ("וַאֲבִירָם", "ואבירם", "and Abiram,"),
        ("בְּנֵי אֱלִיאָב", "אבני אליאב", "sons of Eliab,"),
        ("וְאוֹן", "ואון", "and On"),
        ("בֶּן-פֶּלֶת", "אבן פלת", "son of Peleth,"),
        ("בְּנֵי רְאוּבֵן", "מן בני ראובן", "of the sons of Reuben."),
    ],
    2: [
        # HE: וַיָּקֻמוּ לִפְנֵי מֹשֶׁה וַאֲנָשִׁים מִבְּנֵי-יִשְׂרָאֵל חֲמִשִּׁים וּמָאתָיִם נְשִׂיאֵי עֵדָה קְרִאֵי מוֹעֵד אַנְשֵׁי-שֵׁם
        # JA: פוקפו אמאם מוסי. ואנאס מן בני אסראיל מאיתין וכ'מסין. אשראף אלגמאעה. דעאת מחצ'ר ד'וי אסמא
        # EN: And they stood before Moses — and men of the sons of Israel, two hundred and fifty, nobles of the assembly, summoned to the council, men of known names.
        ("וַיָּקֻמוּ", "פוקפו", "And they stood"),
        ("לִפְנֵי מֹשֶׁה", "אמאם מוסי", "before Moses —"),
        ("וַאֲנָשִׁים", "ואנאס", "and men"),
        ("מִבְּנֵי-יִשְׂרָאֵל", "מן בני אסראיל", "of the sons of Israel,"),
        ("חֲמִשִּׁים וּמָאתָיִם", "מאיתין וכ'מסין", "two hundred and fifty,"),
        ("נְשִׂיאֵי עֵדָה", "אשראף אלגמאעה", "nobles of the assembly,"),
        ("קְרִאֵי מוֹעֵד", "דעאת מחצ'ר", "summoned to the council,"),
        ("אַנְשֵׁי-שֵׁם", "ד'וי אסמא", "men of known names."),
    ],
    3: [
        # HE: וַיִּקָּהֲלוּ עַל-מֹשֶׁה וְעַל-אַהֲרֹן וַיֹּאמְרוּ אֲלֵהֶם רַב-לָכֶם--כִּי כָל-הָעֵדָה כֻּלָּם קְדֹשִׁים וּבְתוֹכָם יְהוָה וּמַדּוּעַ תִּתְנַשְּׂאוּ עַל-קְהַל יְהוָה
        # JA: פתגווקו עלי' מוסי והרון. וקאלא להמא חסבכמא ריאסה. אד' אלגמאעה כלהם מקדסין. ופי מא בינהם נור אללה. ומא באלכמא תתשרפאן עלי' גוק אללה
        # EN: And they gathered in a troop against Moses and Aaron, and said to them: 'Enough of leadership for the two of you — for the whole assembly, every one of them, is holy, and the light of God is in their midst; so why do you exalt yourselves over the congregation of God?'
        ("וַיִּקָּהֲלוּ", "פתגווקו", "And they gathered in a troop"),
        ("עַל-מֹשֶׁה", "עלי' מוסי", "against Moses"),
        ("וְעַל-אַהֲרֹן", "והרון", "and Aaron,"),
        ("וַיֹּאמְרוּ", "וקאלא", "and said"),
        ("אֲלֵהֶם", "להמא", "to them:"),
        ("רַב-לָכֶם", "חסבכמא ריאסה", "'Enough of leadership for the two of you —"),
        ("כִּי כָל-הָעֵדָה", "אד' אלגמאעה", "for the whole assembly,"),
        ("כֻּלָּם", "כלהם", "every one of them,"),
        ("קְדֹשִׁים", "מקדסין", "is holy,"),
        ("וּבְתוֹכָם יְהוָה", "ופי מא בינהם נור אללה", "and the light of God is in their midst;"),
        ("וּמַדּוּעַ", "ומא באלכמא", "so why"),
        ("תִּתְנַשְּׂאוּ", "תתשרפאן", "do you exalt yourselves"),
        ("עַל-קְהַל יְהוָה", "עלי' גוק אללה", "over the congregation of God?'"),
    ],
    4: [
        # HE: וַיִּשְׁמַע מֹשֶׁה וַיִּפֹּל עַל-פָּנָיו
        # JA: פסמע ד'אלך מוסי'. ווקע עלי' וגהה ילתמס אלוחי
        # EN: And when Moses heard this, he fell upon his face, seeking revelation.
        ("וַיִּשְׁמַע", "פסמע", "And when"),
        (None, "ד'אלך", "Moses heard this,"),
        ("מֹשֶׁה", "מוסי'", "he fell"),
        ("וַיִּפֹּל", "ווקע", "upon"),
        ("עַל-פָּנָיו", "עלי' וגהה", "his face,"),
        (None, "ילתמס אלוחי", "seeking revelation."),
    ],
    5: [
        # HE: וַיְדַבֵּר אֶל-קֹרַח וְאֶל-כָּל-עֲדָתוֹ לֵאמֹר בֹּקֶר וְיֹדַע יְהוָה אֶת-אֲשֶׁר-לוֹ וְאֶת-הַקָּדוֹשׁ וְהִקְרִיב אֵלָיו וְאֵת אֲשֶׁר יִבְחַר-בּוֹ יַקְרִיב אֵלָיו
        # JA: וכלם קרח. וכל גמועה וקאל להם. ג'דא. יערף אללה אלד'י הו לה. ואלמקדס פיקרבה אליה. ומן יכ'תארה יקרבה אליה
        # EN: And he spoke to Korah and to all his gatherings, and said to them: 'Tomorrow — God shall make known the one who is His, and the holy one He shall bring near to Him; and whom He shall choose, He shall bring near to Him.'
        ("וַיְדַבֵּר", "וכלם", "And he spoke"),
        ("אֶל-קֹרַח", "קרח", "to Korah"),
        ("וְאֶל-כָּל-עֲדָתוֹ", "וכל גמועה", "and to all his gatherings,"),
        ("לֵאמֹר", "וקאל להם", "and said to them:"),
        ("בֹּקֶר", "ג'דא", "'Tomorrow —"),
        ("וְיֹדַע יְהוָה", "יערף אללה", "God shall make known"),
        ("אֶת-אֲשֶׁר-לוֹ", "אלד'י הו לה", "the one who is His,"),
        ("וְאֶת-הַקָּדוֹשׁ", "ואלמקדס", "and the holy one"),
        ("וְהִקְרִיב אֵלָיו", "פיקרבה אליה", "He shall bring near to Him;"),
        ("וְאֵת אֲשֶׁר יִבְחַר-בּוֹ", "ומן יכ'תארה", "and whom He shall choose,"),
        ("יַקְרִיב אֵלָיו", "יקרבה אליה", "He shall bring near to Him.'"),
    ],
    6: [
        # HE: זֹאת עֲשׂוּ קְחוּ-לָכֶם מַחְתּוֹת קֹרַח וְכָל-עֲדָתוֹ
        # JA: אצנעו כ'לה. כ'דו לכם מגאמרא. קרח וכל גמועה
        # EN: Do both these things: take for yourselves censers, O Korah and all his gatherings,
        ("זֹאת עֲשׂוּ", "אצנעו כ'לה", "Do both these things:"),
        ("קְחוּ-לָכֶם", "כ'דו לכם", "take for yourselves"),
        ("מַחְתּוֹת", "מגאמרא", "censers,"),
        ("קֹרַח", "קרח", "O Korah"),
        ("וְכָל-עֲדָתוֹ", "וכל גמועה", "and all his gatherings,"),
    ],
    7: [
        # HE: וּתְנוּ בָהֵן אֵשׁ וְשִׂימוּ עֲלֵיהֶן קְטֹרֶת לִפְנֵי יְהוָה מָחָר וְהָיָה הָאִישׁ אֲשֶׁר-יִבְחַר יְהוָה הוּא הַקָּדוֹשׁ רַב-לָכֶם בְּנֵי לֵוִי
        # JA: ואגעלו עליהא נארא. ואלקו עליהא בכורא. בין ידי אללה ג'דא. ואי רגל אכ'תארה אללה הו אלמקדס. חסבכם ד'אלך יא בני לוי
        # EN: and place fire upon them, and cast incense upon them, before God — tomorrow; and whichever man God shall choose, he is the holy one. Enough of this for you, O sons of Levi!'
        ("וּתְנוּ בָהֵן אֵשׁ", "ואגעלו עליהא נארא", "and place fire upon them,"),
        ("וְשִׂימוּ עֲלֵיהֶן קְטֹרֶת", "ואלקו עליהא בכורא", "and cast incense upon them,"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God —"),
        ("מָחָר", "ג'דא", "tomorrow;"),
        ("וְהָיָה הָאִישׁ", "ואי רגל", "and whichever man"),
        ("אֲשֶׁר-יִבְחַר יְהוָה", "אכ'תארה אללה", "God shall choose,"),
        ("הוּא הַקָּדוֹשׁ", "הו אלמקדס", "he is the holy one."),
        ("רַב-לָכֶם", "חסבכם ד'אלך", "Enough of this for you,"),
        ("בְּנֵי לֵוִי", "יא בני לוי", "O sons of Levi!'"),
    ],
    8: [
        # HE: וַיֹּאמֶר מֹשֶׁה אֶל-קֹרַח שִׁמְעוּ-נָא בְּנֵי לֵוִי
        # JA: וקאל מוסי' לקרח. אסמעו ד'אלך יא בני לוי
        # EN: And Moses said to Korah: 'Hear this, O sons of Levi.
        ("וַיֹּאמֶר", "וקאל", "And"),
        ("מֹשֶׁה", "מוסי'", "Moses said"),
        ("אֶל-קֹרַח", "לקרח", "to Korah:"),
        ("שִׁמְעוּ-נָא", "אסמעו ד'אלך", "'Hear this,"),
        ("בְּנֵי לֵוִי", "יא בני לוי", "O sons of Levi."),
    ],
    9: [
        # HE: הַמְעַט מִכֶּם כִּי-הִבְדִּיל אֱלֹהֵי יִשְׂרָאֵל אֶתְכֶם מֵעֲדַת יִשְׂרָאֵל לְהַקְרִיב אֶתְכֶם אֵלָיו--לַעֲבֹד אֶת-עֲבֹדַת מִשְׁכַּן יְהוָה וְלַעֲמֹד לִפְנֵי הָעֵדָה לְשָׁרְתָם
        # JA: אקליל ענדכם. אד' אפרזכם אללה אלאה אסראיל מן גמאעתהם. פקרבכם אליה לתכ'דמו מסכנה. ותקפו. בין ידי אלגמאעה תכ'דמונהם
        # EN: Is it too little for you that the God of Israel has separated you from their assembly, and brought you near to Him to serve His tabernacle, and to stand before the assembly to serve them?
        ("הַמְעַט", "אקליל", "Is it too little"),
        ("מִכֶּם", "ענדכם", "for you"),
        ("כִּי-הִבְדִּיל", "אד' אפרזכם", "that the God of Israel has separated you"),
        ("אֱלֹהֵי יִשְׂרָאֵל", "אללה אלאה אסראיל", "from"),
        ("מֵעֲדַת יִשְׂרָאֵל", "מן גמאעתהם", "their assembly,"),
        ("לְהַקְרִיב אֶתְכֶם אֵלָיו", "פקרבכם אליה", "and brought you near to Him"),
        ("לַעֲבֹד אֶת-עֲבֹדַת מִשְׁכַּן יְהוָה", "לתכ'דמו מסכנה", "to serve His tabernacle,"),
        ("וְלַעֲמֹד", "ותקפו", "and to stand"),
        ("לִפְנֵי הָעֵדָה", "בין ידי אלגמאעה", "before the assembly"),
        ("לְשָׁרְתָם", "תכ'דמונהם", "to serve them?"),
    ],
    10: [
        # HE: וַיַּקְרֵב אֹתְךָ וְאֶת-כָּל-אַחֶיךָ בְנֵי-לֵוִי אִתָּךְ וּבִקַּשְׁתֶּם גַּם-כְּהֻנָּה
        # JA: פכד'אך קרבך. וסאיר אכ'ותך בני לוי מעך. חתי' טלבתם אלאמאמה איצ'א
        # EN: And so He brought you near, and all your brothers the sons of Levi with you — and yet you have sought the office of imām as well?
        (None, "פכד'אך", "And so"),
        ("וַיַּקְרֵב", "קרבך", "He brought you near,"),
        ("וְאֶת-כָּל-אַחֶיךָ", "וסאיר אכ'ותך", "and all your brothers"),
        ("בְנֵי-לֵוִי", "בני לוי", "the sons of Levi"),
        ("אִתָּךְ", "מעך", "with you —"),
        ("וּבִקַּשְׁתֶּם", "חתי' טלבתם", "and yet you have sought"),
        ("גַּם-כְּהֻנָּה", "אלאמאמה איצ'א", "the office of imām as well?"),
    ],
    11: [
        # HE: לָכֵן אַתָּה וְכָל-עֲדָתְךָ--הַנֹּעָדִים עַל-יְהוָה וְאַהֲרֹן מַה-הוּא כִּי תלונו (תַלִּינוּ) עָלָיו
        # JA: לד'אלך. אנת וכל גמועך. אלמגתמעין עלי' אללה. והרון מן הו. אד' תתדמרון עליה
        # EN: Therefore — you and all your gatherings, who have assembled against God — and Aaron, what is he, that you bring your grievance against him?'
        ("לָכֵן", "לד'אלך", "Therefore —"),
        ("אַתָּה", "אנת", "you"),
        ("וְכָל-עֲדָתְךָ", "וכל גמועך", "and all your gatherings,"),
        ("הַנֹּעָדִים עַל-יְהוָה", "אלמגתמעין עלי' אללה", "who have assembled against God —"),
        ("וְאַהֲרֹן", "והרון", "and Aaron,"),
        ("מַה-הוּא", "מן הו", "what is he,"),
        ("כִּי תלונו (תַלִּינוּ)", "אד' תתדמרון", "that you bring your grievance"),
        ("עָלָיו", "עליה", "against him?'"),
    ],
    12: [
        # HE: וַיִּשְׁלַח מֹשֶׁה לִקְרֹא לְדָתָן וְלַאֲבִירָם בְּנֵי אֱלִיאָב וַיֹּאמְרוּ לֹא נַעֲלֶה
        # JA: ת'ם בעת' מוסי. לידעו בדתן ואבירם אבני אליאב. פקאלא לא נציר אליך
        # EN: Then Moses sent to summon Dathan and Abiram, sons of Eliab; and they said: 'We shall not come to you.
        (None, "ת'ם", "Then"),
        ("וַיִּשְׁלַח", "בעת'", "Moses sent"),
        ("מֹשֶׁה", "מוסי", "to summon"),
        ("לִקְרֹא לְדָתָן", "לידעו בדתן", "Dathan"),
        ("וְלַאֲבִירָם", "ואבירם", "and Abiram,"),
        ("בְּנֵי אֱלִיאָב", "אבני אליאב", "sons of Eliab;"),
        ("וַיֹּאמְרוּ", "פקאלא", "and they said:"),
        ("לֹא נַעֲלֶה", "לא נציר אליך", "'We shall not come to you."),
    ],
    13: [
        # HE: הַמְעַט כִּי הֶעֱלִיתָנוּ מֵאֶרֶץ זָבַת חָלָב וּדְבַשׁ לַהֲמִיתֵנוּ בַּמִּדְבָּר כִּי-תִשְׂתָּרֵר עָלֵינוּ גַּם-הִשְׂתָּרֵר
        # JA: אקליל. מא אצעדתנא מן בלד יפיץ' אללבן ואלעסל. לתקתלנא פי אלבר. חתי' תתרווס עלינא איצ'א תרווסא
        # EN: Is it too little — that you brought us up from a land flowing with milk and honey, to kill us in the wilderness — that you must lord it over us as well, lording it?
        ("הַמְעַט", "אקליל", "Is it too little —"),
        ("כִּי הֶעֱלִיתָנוּ", "מא אצעדתנא", "that you brought us up"),
        ("מֵאֶרֶץ", "מן בלד", "from a land"),
        ("זָבַת חָלָב", "יפיץ' אללבן", "flowing with milk"),
        ("וּדְבַשׁ", "ואלעסל", "and honey,"),
        ("לַהֲמִיתֵנוּ", "לתקתלנא", "to kill us"),
        ("בַּמִּדְבָּר", "פי אלבר", "in the wilderness —"),
        ("כִּי-תִשְׂתָּרֵר", "חתי' תתרווס", "that you must lord it over us"),
        ("עָלֵינוּ גַּם-הִשְׂתָּרֵר", "עלינא איצ'א תרווסא", "as well, lording it?"),
    ],
    14: [
        # HE: אַף לֹא אֶל-אֶרֶץ זָבַת חָלָב וּדְבַשׁ הֲבִיאֹתָנוּ וַתִּתֶּן-לָנוּ נַחֲלַת שָׂדֶה וָכָרֶם הַעֵינֵי הָאֲנָשִׁים הָהֵם תְּנַקֵּר--לֹא נַעֲלֶה
        # JA: ואיצ'א לם תדכ'לנא אלי' בלד יפיץ' אללבן ואלעסל. ולא אעטיתנא נחלה' צ'יעה או כרם. פלו תהדדת אולאיך אלקום. בקלע עיונהם לם נציר אליך
        # EN: And moreover, you have not brought us into a land flowing with milk and honey, nor given us an inheritance of estate or vineyard; even if you were to threaten those people with the gouging out of their eyes, we shall not come to you.'
        ("אַף", "ואיצ'א", "And moreover,"),
        ("לֹא אֶל-אֶרֶץ זָבַת חָלָב", "לם תדכ'לנא אלי' בלד יפיץ' אללבן", "you have not brought us into a land flowing with milk"),
        ("וּדְבַשׁ הֲבִיאֹתָנוּ", "ואלעסל", "and honey,"),
        ("וַתִּתֶּן-לָנוּ", "ולא אעטיתנא", "nor given us"),
        ("נַחֲלַת שָׂדֶה", "נחלה' צ'יעה", "an inheritance of estate"),
        ("וָכָרֶם", "או כרם", "or vineyard;"),
        ("הַעֵינֵי הָאֲנָשִׁים הָהֵם", "פלו תהדדת אולאיך אלקום", "even if you were to threaten those people"),
        ("תְּנַקֵּר", "בקלע עיונהם", "with the gouging out of their eyes,"),
        ("לֹא נַעֲלֶה", "לם נציר אליך", "we shall not come to you.'"),
    ],
    15: [
        # HE: וַיִּחַר לְמֹשֶׁה מְאֹד וַיֹּאמֶר אֶל-יְהוָה אַל-תֵּפֶן אֶל-מִנְחָתָם לֹא חֲמוֹר אֶחָד מֵהֶם נָשָׂאתִי וְלֹא הֲרֵעֹתִי אֶת-אַחַד מֵהֶם
        # JA: פאשתד עלי' מוסי ג'דא. פקאל. אללהם לא תקבל בכורהם. וד'ל בה עלי' אני לם אסכ'ר לאחדהם חמארא. פצ'לא עלי' אן אסי אלי' אחדהם
        # EN: And Moses was greatly angered, and said: 'O God, do not accept their incense — and let this testify that I have not pressed even one donkey of theirs into my service, much less that I have done wrong to any one of them.'
        ("וַיִּחַר לְמֹשֶׁה", "פאשתד עלי' מוסי", "And Moses was"),
        ("מְאֹד", "ג'דא", "greatly angered,"),
        ("וַיֹּאמֶר", "פקאל", "and said:"),
        ("אֶל-יְהוָה", "אללהם", "'O God,"),
        ("אַל-תֵּפֶן אֶל-מִנְחָתָם", "לא תקבל בכורהם", "do not accept their incense —"),
        (None, "וד'ל בה עלי'", "and let this testify"),
        ("לֹא חֲמוֹר אֶחָד", "אני לם אסכ'ר לאחדהם חמארא", "that I have not pressed even one donkey of theirs into my service,"),
        ("וְלֹא הֲרֵעֹתִי אֶת-אַחַד מֵהֶם", "פצ'לא עלי' אן אסי אלי' אחדהם", "much less that I have done wrong to any one of them.'"),
    ],
    16: [
        # HE: וַיֹּאמֶר מֹשֶׁה אֶל-קֹרַח אַתָּה וְכָל-עֲדָתְךָ הֱיוּ לִפְנֵי יְהוָה אַתָּה וָהֵם וְאַהֲרֹן מָחָר
        # JA: ת'ם קאל מוסי לקרח. אנת וכל גמועך. אחצ'רו בין ידי אללה. מע הרון ג'דא
        # EN: Then Moses said to Korah: 'You and all your gatherings — present yourselves before God, with Aaron, tomorrow.
        (None, "ת'ם", "Then"),
        ("וַיֹּאמֶר", "קאל", "Moses said"),
        ("מֹשֶׁה", "מוסי", "to Korah:"),
        ("אֶל-קֹרַח", "לקרח", "'You"),
        ("אַתָּה", "אנת", "and all your gatherings —"),
        ("וְכָל-עֲדָתְךָ", "וכל גמועך", "present yourselves"),
        ("הֱיוּ לִפְנֵי יְהוָה", "אחצ'רו בין ידי אללה", "before God,"),
        ("וְאַהֲרֹן", "מע הרון", "with Aaron,"),
        ("מָחָר", "ג'דא", "tomorrow."),
    ],
    17: [
        # HE: וּקְחוּ אִישׁ מַחְתָּתוֹ וּנְתַתֶּם עֲלֵיהֶם קְטֹרֶת וְהִקְרַבְתֶּם לִפְנֵי יְהוָה אִישׁ מַחְתָּתוֹ חֲמִשִּׁים וּמָאתַיִם מַחְתֹּת וְאַתָּה וְאַהֲרֹן אִישׁ מַחְתָּתוֹ
        # JA: וליאכ'ד' כל ואחד מגמרתה. ואלקו עליהא בכ'ורא. וקדמוהא בין ידי אללה. מאיתין וכ'מסין מגמרה. ואנת והרון כל ואחד מגמרתה
        # EN: And let each man take his censer, and cast incense upon it, and bring them before God — two hundred and fifty censers; and you and Aaron, each man his censer.'
        ("וּקְחוּ", "וליאכ'ד'", "And let"),
        ("אִישׁ מַחְתָּתוֹ", "כל ואחד מגמרתה", "each man take his censer,"),
        ("וּנְתַתֶּם עֲלֵיהֶם קְטֹרֶת", "ואלקו עליהא בכ'ורא", "and cast incense upon it,"),
        ("וְהִקְרַבְתֶּם", "וקדמוהא", "and bring them"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God —"),
        ("חֲמִשִּׁים וּמָאתַיִם מַחְתֹּת", "מאיתין וכ'מסין מגמרה", "two hundred and fifty censers;"),
        ("וְאַתָּה וְאַהֲרֹן", "ואנת והרון", "and you and Aaron,"),
        ("אִישׁ מַחְתָּתוֹ", "כל ואחד מגמרתה", "each man his censer.'"),
    ],
    18: [
        # HE: וַיִּקְחוּ אִישׁ מַחְתָּתוֹ וַיִּתְּנוּ עֲלֵיהֶם אֵשׁ וַיָּשִׂימוּ עֲלֵיהֶם קְטֹרֶת וַיַּעַמְדוּ פֶּתַח אֹהֶל מוֹעֵד--וּמֹשֶׁה וְאַהֲרֹן
        # JA: פאכ'ד' כל ואחד מגמרתה. וגעלו פיהא נארא. ואלקו עליהא בכורא. ווקפו. עלי' באב כ'בא אלמחצ'ר ומוסי' והרון
        # EN: And each man took his censer, and placed fire in it, and cast incense upon it; and they stood at the entrance of the tent of the assembly — and Moses and Aaron.
        ("וַיִּקְחוּ", "פאכ'ד'", "And each man took"),
        ("אִישׁ מַחְתָּתוֹ", "כל ואחד מגמרתה", "his censer,"),
        ("וַיִּתְּנוּ עֲלֵיהֶם אֵשׁ", "וגעלו פיהא נארא", "and placed fire in it,"),
        ("וַיָּשִׂימוּ עֲלֵיהֶם קְטֹרֶת", "ואלקו עליהא בכורא", "and cast incense upon it;"),
        ("וַיַּעַמְדוּ", "ווקפו", "and they stood"),
        ("פֶּתַח אֹהֶל מוֹעֵד", "עלי' באב כ'בא אלמחצ'ר", "at the entrance of the tent of the assembly —"),
        ("וּמֹשֶׁה וְאַהֲרֹן", "ומוסי' והרון", "and Moses and Aaron."),
    ],
    19: [
        # HE: וַיַּקְהֵל עֲלֵיהֶם קֹרַח אֶת-כָּל-הָעֵדָה אֶל-פֶּתַח אֹהֶל מוֹעֵד וַיֵּרָא כְבוֹד-יְהוָה אֶל-כָּל-הָעֵדָה
        # JA: פגווק עליהם קרח גמיע אלגמאעה. אלי' באב כ'בא אלמחצ'ר. פצ'הר נור אללה לגמיעהם
        # EN: And Korah gathered all the assembly against them, to the entrance of the tent of the assembly; and the light of God appeared to all of them.
        ("וַיַּקְהֵל עֲלֵיהֶם", "פגווק עליהם", "And Korah gathered"),
        ("קֹרַח", "קרח", "all the assembly"),
        ("אֶת-כָּל-הָעֵדָה", "גמיע אלגמאעה", "against them,"),
        ("אֶל-פֶּתַח", "אלי' באב", "to the entrance of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly;"),
        ("וַיֵּרָא", "פצ'הר", "and the light of God appeared"),
        ("כְבוֹד-יְהוָה", "נור אללה", "to all of them."),
        ("אֶל-כָּל-הָעֵדָה", "לגמיעהם", ""),
    ],
    20: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה וְאֶל-אַהֲרֹן לֵאמֹר
        # JA: ת'ם כלם אללה מוסי והרון תכלימא
        # EN: Then God spoke to Moses and Aaron in direct speech,
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי", "and Aaron"),
        ("וְאֶל-אַהֲרֹן", "והרון", "in direct speech,"),
        ("לֵאמֹר", "תכלימא", ""),
    ],
    21: [
        # HE: הִבָּדְלוּ מִתּוֹךְ הָעֵדָה הַזֹּאת וַאֲכַלֶּה אֹתָם כְּרָגַע
        # JA: אן אנפרזתם מן בין הד'ה אלגמאעה. אפניתהם כטרפה
        # EN: saying: 'If you separate yourselves from among this assembly, I shall destroy them in an instant.'
        ("הִבָּדְלוּ", "אן אנפרזתם", "saying: 'If you separate yourselves"),
        ("מִתּוֹךְ", "מן בין", "from among"),
        ("הָעֵדָה הַזֹּאת", "הד'ה אלגמאעה", "this assembly,"),
        ("וַאֲכַלֶּה אֹתָם", "אפניתהם", "I shall destroy them"),
        ("כְּרָגַע", "כטרפה", "in an instant.'"),
    ],
    22: [
        # HE: וַיִּפְּלוּ עַל-פְּנֵיהֶם וַיֹּאמְרוּ אֵל אֱלֹהֵי הָרוּחֹת לְכָל-בָּשָׂר הָאִישׁ אֶחָד יֶחֱטָא וְעַל כָּל-הָעֵדָה תִּקְצֹף
        # JA: פוקעא עלי' וגוההמא וקאלא. יא טאיק. יא אלאה ארואח כל בשרי. ארגל ואחד יכ'טי. ועלי סאיר אלגמאעה תסכ'ט
        # EN: And the two of them fell upon their faces and said: 'O Possessor of power and might! O God of the spirits of all living flesh! — shall one man err, and You be wrathful against the rest of the assembly?'
        ("וַיִּפְּלוּ", "פוקעא", "And the two of them fell"),
        ("עַל-פְּנֵיהֶם", "עלי' וגוההמא", "upon their faces"),
        ("וַיֹּאמְרוּ", "וקאלא", "and said:"),
        ("אֵל", "יא טאיק", "'O Possessor of power and might!"),
        ("אֱלֹהֵי הָרוּחֹת", "יא אלאה ארואח", "O God of the spirits of"),
        ("לְכָל-בָּשָׂר", "כל בשרי", "all living flesh! —"),
        ("הָאִישׁ אֶחָד", "ארגל ואחד", "shall one man"),
        ("יֶחֱטָא", "יכ'טי", "err,"),
        ("וְעַל כָּל-הָעֵדָה", "ועלי סאיר אלגמאעה", "and You be wrathful against the rest of the assembly?'"),
        ("תִּקְצֹף", "תסכ'ט", ""),
    ],
    23: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי תכלימא
        # EN: Then God spoke to Moses in direct speech,
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי", "in direct speech,"),
        ("לֵּאמֹר", "תכלימא", ""),
    ],
    24: [
        # HE: דַּבֵּר אֶל-הָעֵדָה לֵאמֹר הֵעָלוּ מִסָּבִיב לְמִשְׁכַּן-קֹרַח דָּתָן וַאֲבִירָם
        # JA: מר אלגמאעה וקל להם. ארתפעו. ען חואלי מסכן קרח דתן ואבירם
        # EN: saying: 'Command the assembly and say to them: Move away from around the dwelling of Korah, Dathan, and Abiram.'
        ("דַּבֵּר", "מר אלגמאעה", "saying: 'Command the assembly"),
        ("אֶל-הָעֵדָה", "וקל להם", "and say to them:"),
        ("הֵעָלוּ", "ארתפעו", "Move away"),
        ("מִסָּבִיב", "ען חואלי", "from around"),
        ("לְמִשְׁכַּן-קֹרַח", "מסכן קרח", "the dwelling of Korah,"),
        ("דָּתָן", "דתן", "Dathan,"),
        ("וַאֲבִירָם", "ואבירם", "and Abiram.'"),
    ],
    25: [
        # HE: וַיָּקָם מֹשֶׁה וַיֵּלֶךְ אֶל-דָּתָן וַאֲבִירָם וַיֵּלְכוּ אַחֲרָיו זִקְנֵי יִשְׂרָאֵל
        # JA: פקאם מוסי. ומצ'א אלי' דתן ואבירם. ומצו מעה שיוך' בני אסראיל
        # EN: And Moses arose and went to Dathan and Abiram; and the elders of the sons of Israel went with him.
        ("וַיָּקָם", "פקאם", "And Moses arose"),
        ("מֹשֶׁה", "מוסי", "and went"),
        ("וַיֵּלֶךְ", "ומצ'א", "to Dathan"),
        ("אֶל-דָּתָן", "אלי' דתן", "and Abiram;"),
        ("וַאֲבִירָם", "ואבירם", "and the elders"),
        ("וַיֵּלְכוּ", "ומצו", "went"),
        ("אַחֲרָיו", "מעה", "with him."),
        ("זִקְנֵי יִשְׂרָאֵל", "שיוך' בני אסראיל", "of the sons of Israel"),
    ],
    26: [
        # HE: וַיְדַבֵּר אֶל-הָעֵדָה לֵאמֹר סוּרוּ נָא מֵעַל אָהֳלֵי הָאֲנָשִׁים הָרְשָׁעִים הָאֵלֶּה וְאַל-תִּגְּעוּ בְּכָל-אֲשֶׁר לָהֶם פֶּן-תִּסָּפוּ בְּכָל-חַטֹּאתָם
        # JA: פכלם אלגמאעה וקאל להם. אעתזלו ען אכ'ביה' הולאי אלקום אלצ'אלמין. ולא תדנו בשי ממא הו להם. כלא תנסאפו בגמיע כ'טאיאהם
        # EN: And he spoke to the assembly and said to them: 'Withdraw from the tents of these wrongdoing people, and do not approach anything that belongs to them — lest you be swept away with all their sins.'
        ("וַיְדַבֵּר", "פכלם", "And he spoke"),
        ("אֶל-הָעֵדָה", "אלגמאעה", "to the assembly"),
        ("לֵאמֹר", "וקאל להם", "and said to them:"),
        ("סוּרוּ נָא", "אעתזלו", "'Withdraw"),
        ("מֵעַל אָהֳלֵי", "ען אכ'ביה'", "from the tents of"),
        ("הָאֲנָשִׁים הָרְשָׁעִים הָאֵלֶּה", "הולאי אלקום אלצ'אלמין", "these wrongdoing people,"),
        ("וְאַל-תִּגְּעוּ", "ולא תדנו", "and do not approach"),
        ("בְּכָל-אֲשֶׁר לָהֶם", "בשי ממא הו להם", "anything that belongs to them —"),
        ("פֶּן-תִּסָּפוּ", "כלא תנסאפו", "lest you be swept away"),
        ("בְּכָל-חַטֹּאתָם", "בגמיע כ'טאיאהם", "with all their sins.'"),
    ],
    27: [
        # HE: וַיֵּעָלוּ מֵעַל מִשְׁכַּן-קֹרַח דָּתָן וַאֲבִירָם--מִסָּבִיב וְדָתָן וַאֲבִירָם יָצְאוּ נִצָּבִים פֶּתַח אָהֳלֵיהֶם וּנְשֵׁיהֶם וּבְנֵיהֶם וְטַפָּם
        # JA: פארתעפו. ען חואלי מסכן קרח דתן ואבירם. והמא איצ'א כ'רגא. פאנתצבו עלא באב כ'באיהמא. ונסאהם ובניהם ואטפאלהם לירו מא יכון
        # EN: And they moved away from around the dwelling of Korah, Dathan, and Abiram; and the two of them also came out, and stood at the entrance of their tents — and their wives and their sons and their little ones — to see what would come to pass.
        ("וַיֵּעָלוּ", "פארתעפו", "And they moved away"),
        ("מֵעַל מִשְׁכַּן-קֹרַח", "ען חואלי מסכן קרח", "from around the dwelling of Korah,"),
        ("דָּתָן", "דתן", "Dathan,"),
        ("וַאֲבִירָם--מִסָּבִיב", "ואבירם", "and Abiram;"),
        ("וְדָתָן וַאֲבִירָם", "והמא איצ'א", "and the two of them also"),
        ("יָצְאוּ", "כ'רגא", "came out,"),
        ("נִצָּבִים", "פאנתצבו", "and stood"),
        ("פֶּתַח אָהֳלֵיהֶם", "עלא באב כ'באיהמא", "at the entrance of their tents —"),
        ("וּנְשֵׁיהֶם", "ונסאהם", "and their wives"),
        ("וּבְנֵיהֶם", "ובניהם", "and their sons"),
        ("וְטַפָּם", "ואטפאלהם", "and their little ones —"),
        (None, "לירו מא יכון", "to see what would come to pass."),
    ],
    28: [
        # HE: וַיֹּאמֶר מֹשֶׁה בְּזֹאת תֵּדְעוּן כִּי-יְהוָה שְׁלָחַנִי לַעֲשׂוֹת אֵת כָּל-הַמַּעֲשִׂים הָאֵלֶּה כִּי-לֹא מִלִּבִּי
        # JA: פקאל מוסי. בהד'ה אלכ'לה. תעלמון. אן אללה בעת' בי. לאעמל גמיע הד'ה אלאעמאל. ליס מן תלקא נפסי
        # EN: And Moses said: 'By this resolution you shall know that God has sent me to do all these deeds — not of my own accord.
        ("וַיֹּאמֶר", "פקאל", "And Moses said:"),
        ("מֹשֶׁה", "מוסי", "'By this resolution"),
        ("בְּזֹאת", "בהד'ה אלכ'לה", "you shall know"),
        ("תֵּדְעוּן", "תעלמון", "that God has sent me"),
        ("כִּי-יְהוָה שְׁלָחַנִי", "אן אללה בעת' בי", "to do"),
        ("לַעֲשׂוֹת", "לאעמל", "all these deeds —"),
        ("אֵת כָּל-הַמַּעֲשִׂים הָאֵלֶּה", "גמיע הד'ה אלאעמאל", "not"),
        ("כִּי-לֹא מִלִּבִּי", "ליס מן תלקא נפסי", "of my own accord."),
    ],
    29: [
        # HE: אִם-כְּמוֹת כָּל-הָאָדָם יְמֻתוּן אֵלֶּה וּפְקֻדַּת כָּל-הָאָדָם יִפָּקֵד עֲלֵיהֶם--לֹא יְהוָה שְׁלָחָנִי
        # JA: אן מאת הולאי אלקום כמות כל אלנאס. וטולבו כמטאלבתהם. פליס אללה בעת' בי
        # EN: If these people die as all people die, and are called to account as all people are called to account — then God has not sent me.
        ("אִם-כְּמוֹת", "אן מאת", "If these people die"),
        ("כָּל-הָאָדָם", "הולאי אלקום", "as all people die,"),
        ("יְמֻתוּן אֵלֶּה", "כמות כל אלנאס", "and are called to account"),
        ("וּפְקֻדַּת", "וטולבו", "as all people are called to account —"),
        ("כָּל-הָאָדָם יִפָּקֵד עֲלֵיהֶם", "כמטאלבתהם", "then God has not sent me."),
        ("לֹא יְהוָה שְׁלָחָנִי", "פליס אללה בעת' בי", ""),
    ],
    30: [
        # HE: וְאִם-בְּרִיאָה יִבְרָא יְהוָה וּפָצְתָה הָאֲדָמָה אֶת-פִּיהָ וּבָלְעָה אֹתָם וְאֶת-כָּל-אֲשֶׁר לָהֶם וְיָרְדוּ חַיִּים שְׁאֹלָה--וִידַעְתֶּם כִּי נִאֲצוּ הָאֲנָשִׁים הָאֵלֶּה אֶת-יְהוָה
        # JA: ואן כ'לק אללה כ'לקא. באן תפתח אלארץ' פאהא פתבתלעהם וגמיע מאלהם. וינזלו אחיא אלי' אלת'רא. עלמתם. אן הולאי אלקום קד עצו אללה
        # EN: But if God creates a creation — that the earth opens its mouth and swallows them and all that belongs to them, and they go down alive into the ground — then you shall know that these people have transgressed against God.'
        ("וְאִם-בְּרִיאָה", "ואן כ'לק", "But if God creates"),
        ("יִבְרָא יְהוָה", "אללה כ'לקא", "a creation —"),
        ("וּפָצְתָה הָאֲדָמָה", "באן תפתח אלארץ'", "that the earth opens"),
        ("אֶת-פִּיהָ", "פאהא", "its mouth"),
        ("וּבָלְעָה אֹתָם", "פתבתלעהם", "and swallows them"),
        ("וְאֶת-כָּל-אֲשֶׁר לָהֶם", "וגמיע מאלהם", "and all that belongs to them,"),
        ("וְיָרְדוּ", "וינזלו", "and they go down"),
        ("חַיִּים", "אחיא", "alive"),
        ("שְׁאֹלָה", "אלי' אלת'רא", "into the ground —"),
        ("וִידַעְתֶּם", "עלמתם", "then you shall know"),
        ("כִּי נִאֲצוּ", "אן הולאי אלקום קד עצו", "that these people have transgressed"),
        ("הָאֲנָשִׁים הָאֵלֶּה אֶת-יְהוָה", "אללה", "against God.'"),
    ],
    31: [
        # HE: וַיְהִי כְּכַלֹּתוֹ לְדַבֵּר אֵת כָּל-הַדְּבָרִים הָאֵלֶּה וַתִּבָּקַע הָאֲדָמָה אֲשֶׁר תַּחְתֵּיהֶם
        # JA: וכאן ענד פראג'ה. מן קול הד'א אלכלאם. אנשקת אלארץ' אלד'ין תחתהם
        # EN: And it came to pass, upon his finishing the saying of this speech, that the earth which was beneath them split open.
        ("וַיְהִי", "וכאן", "And it came to pass,"),
        ("כְּכַלֹּתוֹ", "ענד פראג'ה", "upon his finishing"),
        ("לְדַבֵּר", "מן קול", "the saying of"),
        ("אֵת כָּל-הַדְּבָרִים הָאֵלֶּה", "הד'א אלכלאם", "this speech,"),
        ("וַתִּבָּקַע", "אנשקת", "that the earth which was beneath them split open."),
        ("הָאֲדָמָה", "אלארץ'", ""),
        ("אֲשֶׁר תַּחְתֵּיהֶם", "אלד'ין תחתהם", ""),
    ],
    32: [
        # HE: וַתִּפְתַּח הָאָרֶץ אֶת-פִּיהָ וַתִּבְלַע אֹתָם וְאֶת-בָּתֵּיהֶם וְאֵת כָּל-הָאָדָם אֲשֶׁר לְקֹרַח וְאֵת כָּל-הָרְכוּשׁ
        # JA: פפתחת אלארץ' פאהא. פאבתלעתהם וביותהם. וכל אנסאן לקרח. וגמיע אלסרח
        # EN: And the earth opened its mouth and swallowed them and their houses, and every person belonging to Korah, and all the livestock.
        ("וַתִּפְתַּח", "פפתחת", "And the earth opened"),
        ("הָאָרֶץ", "אלארץ'", "its mouth"),
        ("אֶת-פִּיהָ", "פאהא", "and swallowed them"),
        ("וַתִּבְלַע אֹתָם", "פאבתלעתהם", "and their houses,"),
        ("וְאֶת-בָּתֵּיהֶם", "וביותהם", "and every person"),
        ("וְאֵת כָּל-הָאָדָם אֲשֶׁר לְקֹרַח", "וכל אנסאן לקרח", "belonging to Korah,"),
        ("וְאֵת כָּל-הָרְכוּשׁ", "וגמיע אלסרח", "and all the livestock."),
    ],
    33: [
        # HE: וַיֵּרְדוּ הֵם וְכָל-אֲשֶׁר לָהֶם חַיִּים--שְׁאֹלָה וַתְּכַס עֲלֵיהֶם הָאָרֶץ וַיֹּאבְדוּ מִתּוֹךְ הַקָּהָל
        # JA: פנזלו הם וגמיע מאלהם. אחיא אלי' אלת'רא. וג'טת עליהם אלארץ'. ובאדו מן בין אלגוק
        # EN: And they went down — they and all that was theirs — alive into the ground; and the earth closed over them, and they perished from among the congregation.
        ("וַיֵּרְדוּ", "פנזלו", "And they went down —"),
        ("הֵם", "הם", "they"),
        ("וְכָל-אֲשֶׁר לָהֶם", "וגמיע מאלהם", "and all that was theirs —"),
        ("חַיִּים", "אחיא", "alive"),
        ("שְׁאֹלָה", "אלי' אלת'רא", "into the ground;"),
        ("וַתְּכַס עֲלֵיהֶם", "וג'טת עליהם", "and the earth closed over them,"),
        ("הָאָרֶץ", "אלארץ'", "and they perished"),
        ("וַיֹּאבְדוּ", "ובאדו", "from among"),
        ("מִתּוֹךְ הַקָּהָל", "מן בין אלגוק", "the congregation."),
    ],
    34: [
        # HE: וְכָל-יִשְׂרָאֵל אֲשֶׁר סְבִיבֹתֵיהֶם--נָסוּ לְקֹלָם כִּי אָמְרוּ פֶּן-תִּבְלָעֵנוּ הָאָרֶץ
        # JA: וגמיע אל אסראיל. אלד'ין חואליהם הרבו מן שדה' אצואתהם. קאלו. כלא תבלענא אלארץ'
        # EN: And all the house of Israel who were around them fled at the sound of their voices, saying: 'Lest the earth swallow us too.'
        ("וְכָל-יִשְׂרָאֵל", "וגמיע אל אסראיל", "And all the house of Israel"),
        ("אֲשֶׁר סְבִיבֹתֵיהֶם", "אלד'ין חואליהם", "who were around them"),
        ("נָסוּ", "הרבו", "fled"),
        ("לְקֹלָם", "מן שדה' אצואתהם", "at the sound of their voices,"),
        ("כִּי אָמְרוּ", "קאלו", "saying:"),
        ("פֶּן-תִּבְלָעֵנוּ הָאָרֶץ", "כלא תבלענא אלארץ'", "'Lest the earth swallow us too.'"),
    ],
    35: [
        # HE: וְאֵשׁ יָצְאָה מֵאֵת יְהוָה וַתֹּאכַל אֵת הַחֲמִשִּׁים וּמָאתַיִם אִישׁ מַקְרִיבֵי הַקְּטֹרֶת
        # JA: ונאר כ'רגת מן ענד אללה. פאחרקת אלמאיתין ואלכ'מסין אלרגל. מקרבי אלבכור
        # EN: And a fire went out from God and burned the two hundred and fifty men, who had offered the incense.
        ("וְאֵשׁ", "ונאר", "And a fire"),
        ("יָצְאָה", "כ'רגת", "went out"),
        ("מֵאֵת יְהוָה", "מן ענד אללה", "from God"),
        ("וַתֹּאכַל", "פאחרקת", "and burned"),
        ("אֵת הַחֲמִשִּׁים וּמָאתַיִם", "אלמאיתין ואלכ'מסין", "the two hundred and fifty"),
        ("אִישׁ", "אלרגל", "men,"),
        ("מַקְרִיבֵי הַקְּטֹרֶת", "מקרבי אלבכור", "who had offered the incense."),
    ],
}

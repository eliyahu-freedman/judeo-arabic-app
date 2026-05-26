"""Hand-authored word-level alignment triples for Bamidbar chapter 35."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה בְּעַרְבֹת מוֹאָב עַל-יַרְדֵּן יְרֵחוֹ לֵאמֹר
        # JA: ת'ם כלם אללה מוסי' פי בידאת מואב. עלי' ארדן יריחא תכלימא
        # EN: Then God spoke to Moses in the wilderness of Moab, by the Jordan of Jericho directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to Moses"),
        ("אֶל-מֹשֶׁה", "מוסי'", "in the wilderness of"),
        ("בְּעַרְבֹת", "פי בידאת", "Moab,"),
        ("מוֹאָב", "מואב", "by the"),
        ("עַל-יַרְדֵּן", "עלי' ארדן", "Jordan of"),
        ("יְרֵחוֹ", "יריחא", "Jericho"),
        ("לֵאמֹר", "תכלימא", "directly."),
    ],
    2: [
        # HE: צַו אֶת-בְּנֵי יִשְׂרָאֵל וְנָתְנוּ לַלְוִיִּם מִנַּחֲלַת אֲחֻזָּתָם עָרִים לָשָׁבֶת וּמִגְרָשׁ לֶעָרִים סְבִיבֹתֵיהֶם תִּתְּנוּ לַלְוִיִּם
        # JA: מר בני אסראיל. באן יעטו אלליואניין. מן נחלת חוזהם קרא יסכנוהא. ואפניה להם חואלי'הא
        # EN: Command the sons of Israel that they give to the Levites, from the inheritance of their possession, towns to dwell in, and open spaces for them round about them.
        ("צַו", "מר", "Command"),
        ("אֶת-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel"),
        ("וְנָתְנוּ", "באן יעטו", "that they give"),
        ("לַלְוִיִּם", "אלליואניין", "to the Levites,"),
        ("מִנַּחֲלַת", "מן נחלת", "from the inheritance of"),
        ("אֲחֻזָּתָם", "חוזהם", "their possession,"),
        ("עָרִים", "קרא", "towns"),
        ("לָשָׁבֶת", "יסכנוהא", "to dwell in,"),
        ("וּמִגְרָשׁ", "ואפניה", "and open spaces"),
        ("סְבִיבֹתֵיהֶם", "חואלי'הא", "for them round about them."),
    ],
    3: [
        # HE: וְהָיוּ הֶעָרִים לָהֶם לָשָׁבֶת וּמִגְרְשֵׁיהֶם יִהְיוּ לִבְהֶמְתָּם וְלִרְכֻשָׁם וּלְכֹל חַיָּתָם
        # JA: ותכון אלקרא סכנא להם. ואפניתהא. לבהאימהם וסרחהם וסאיר חיואנהם
        # EN: And the towns shall be a dwelling for them, and their open spaces shall be for their beasts and their flocks and the rest of their animals.
        ("וְהָיוּ", "ותכון", "And the towns shall be"),
        ("הֶעָרִים", "אלקרא", "a dwelling"),
        ("לָשָׁבֶת", "סכנא", "for them,"),
        ("לָהֶם", "להם", "and their open spaces"),
        ("וּמִגְרְשֵׁיהֶם", "ואפניתהא", "shall be for their beasts"),
        ("לִבְהֶמְתָּם", "לבהאימהם", "and their flocks"),
        ("וְלִרְכֻשָׁם", "וסרחהם", "and the rest of"),
        ("וּלְכֹל חַיָּתָם", "וסאיר חיואנהם", "their animals."),
    ],
    4: [
        # HE: וּמִגְרְשֵׁי הֶעָרִים אֲשֶׁר תִּתְּנוּ לַלְוִיִּם מִקִּיר הָעִיר וָחוּצָה אֶלֶף אַמָּה סָבִיב
        # JA: ואפניה' אלקרא. אלתי תעטוהא לאליואניין. מן כ'ארג חאיט אלקריה. אלף ד'ראע מסתדירא
        # EN: And the open spaces of the towns which you give to the Levites shall extend from outside the wall of the town one thousand cubits all around.
        ("וּמִגְרְשֵׁי", "ואפניה'", "And the open spaces of"),
        ("הֶעָרִים", "אלקרא", "the towns"),
        ("אֲשֶׁר תִּתְּנוּ", "אלתי תעטוהא", "which you give"),
        ("לַלְוִיִּם", "לאליואניין", "to the Levites"),
        ("מִקִּיר", "מן כ'ארג חאיט", "from outside the wall of"),
        ("הָעִיר", "אלקריה", "the town"),
        ("אֶלֶף", "אלף", "one thousand"),
        ("אַמָּה", "ד'ראע", "cubits"),
        ("סָבִיב", "מסתדירא", "all around."),
    ],
    5: [
        # HE: וּמַדֹּתֶם מִחוּץ לָעִיר אֶת-פְּאַת-קֵדְמָה אַלְפַּיִם בָּאַמָּה וְאֶת-פְּאַת-נֶגֶב אַלְפַּיִם בָּאַמָּה וְאֶת-פְּאַת-יָם אַלְפַּיִם בָּאַמָּה וְאֵת פְּאַת צָפוֹן אַלְפַּיִם בָּאַמָּה--וְהָעִיר בַּתָּוֶךְ זֶה יִהְיֶה לָהֶם מִגְרְשֵׁי הֶעָרִים
        # JA: ת'ם אמסחו מן כ'ארג אלקריה. אלי' גהה' אלמשרק אלפין ד'ראע. ואלי' גהה' אלגנוב אלפין ד'ראע. ואלי' גהה' אלג'רב אלפין ד'ראע. ואלי' גהה' אלשמאל. אלפין ד'ראע ואלקריה פי וסטהא. פד'אלך יכון לכם. מקדאר אפניה' אלקרא
        # EN: Then measure from outside the town: toward the east two thousand cubits, and toward the south two thousand cubits, and toward the west two thousand cubits, and toward the north two thousand cubits — with the town in the midst of them. That shall be for you the measure of the open spaces of the towns.
        (None, "ת'ם", "Then"),
        ("וּמַדֹּתֶם", "אמסחו", "measure"),
        ("מִחוּץ לָעִיר", "מן כ'ארג אלקריה", "from outside the town:"),
        ("אֶת-פְּאַת-קֵדְמָה", "אלי' גהה' אלמשרק", "toward the east"),
        ("אַלְפַּיִם בָּאַמָּה", "אלפין ד'ראע", "two thousand cubits,"),
        ("וְאֶת-פְּאַת-נֶגֶב", "ואלי' גהה' אלגנוב", "and toward the south"),
        (None, "אלפין ד'ראע", "two thousand cubits,"),
        ("וְאֶת-פְּאַת-יָם", "ואלי' גהה' אלג'רב", "and toward the west"),
        (None, "אלפין ד'ראע", "two thousand cubits,"),
        ("וְאֵת פְּאַת צָפוֹן", "ואלי' גהה' אלשמאל", "and toward the north"),
        (None, "אלפין ד'ראע", "two thousand cubits —"),
        ("וְהָעִיר", "ואלקריה", "with the town"),
        ("בַּתָּוֶךְ", "פי וסטהא", "in the midst of them."),
        ("זֶה יִהְיֶה לָהֶם", "פד'אלך יכון לכם", "That shall be for you"),
        ("מִגְרְשֵׁי הֶעָרִים", "מקדאר אפניה' אלקרא", "the measure of the open spaces of the towns."),
    ],
    6: [
        # HE: וְאֵת הֶעָרִים אֲשֶׁר תִּתְּנוּ לַלְוִיִּם אֵת שֵׁשׁ-עָרֵי הַמִּקְלָט אֲשֶׁר תִּתְּנוּ לָנֻס שָׁמָּה הָרֹצֵחַ וַעֲלֵיהֶם תִּתְּנוּ אַרְבָּעִים וּשְׁתַּיִם עִיר
        # JA: ואלקרא אלד'י תעטוהא לאליואניין. מנהא סת קרא אלחמא. אלד'י תעזלוהא. ליהרב אלי'הא אלקאתל. ואצ'יפו אלי'הא. את'נין וארבעין קריה
        # EN: And the towns which you give to the Levites — among them shall be the six towns of refuge which you set apart, so that the killer may flee to them; and add to them forty-two towns.
        ("וְאֵת הֶעָרִים", "ואלקרא", "And the towns"),
        ("אֲשֶׁר תִּתְּנוּ", "אלד'י תעטוהא", "which you give"),
        ("לַלְוִיִּם", "לאליואניין", "to the Levites —"),
        ("אֵת שֵׁשׁ-עָרֵי", "מנהא סת קרא", "among them shall be the six towns of"),
        ("הַמִּקְלָט", "אלחמא", "refuge"),
        ("אֲשֶׁר תִּתְּנוּ", "אלד'י תעזלוהא", "which you set apart,"),
        ("לָנֻס", "ליהרב", "so that"),
        ("הָרֹצֵחַ", "אלקאתל", "the killer may flee to them;"),
        ("וַעֲלֵיהֶם תִּתְּנוּ", "ואצ'יפו אלי'הא", "and add to them"),
        ("אַרְבָּעִים וּשְׁתַּיִם", "את'נין וארבעין", "forty-two"),
        ("עִיר", "קריה", "towns."),
    ],
    7: [
        # HE: כָּל-הֶעָרִים אֲשֶׁר תִּתְּנוּ לַלְוִיִּם--אַרְבָּעִים וּשְׁמֹנֶה עִיר אֶתְהֶן וְאֶת-מִגְרְשֵׁיהֶן
        # JA: פתציר גמיע אלקרא. אלד'י תעטוהם. תמאניה וארבעין קריה ואפניתהא
        # EN: So all the towns which you give shall be forty-eight towns, with their open spaces.
        ("כָּל-הֶעָרִים", "פתציר גמיע אלקרא", "So all the towns"),
        ("אֲשֶׁר תִּתְּנוּ", "אלד'י תעטוהם", "which you give"),
        ("אַרְבָּעִים וּשְׁמֹנֶה", "תמאניה וארבעין", "shall be forty-eight"),
        ("עִיר", "קריה", "towns,"),
        ("וְאֶת-מִגְרְשֵׁיהֶן", "ואפניתהא", "with their open spaces."),
    ],
    8: [
        # HE: וְהֶעָרִים אֲשֶׁר תִּתְּנוּ מֵאֲחֻזַּת בְּנֵי-יִשְׂרָאֵל מֵאֵת הָרַב תַּרְבּוּ וּמֵאֵת הַמְעַט תַּמְעִיטוּ אִישׁ כְּפִי נַחֲלָתוֹ אֲשֶׁר יִנְחָלוּ יִתֵּן מֵעָרָיו לַלְוִיִּם
        # JA: ואלקרא. אלד'י תעטונהם מן חוז בני אסראיל. ממן אכ'ד' כת'ירא כת'רו. ומן מן אכ'ד' קלילא קללו. פליעט כל סבט עלי' קדר נחלתה
        # EN: And the towns which you give from the possession of the sons of Israel — from him who took much, give more; and from him who took little, give less; each tribe shall give according to the measure of its inheritance.
        ("וְהֶעָרִים", "ואלקרא", "And the towns"),
        ("אֲשֶׁר תִּתְּנוּ", "אלד'י תעטונהם", "which you give"),
        ("מֵאֲחֻזַּת", "מן חוז", "from the possession of"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel —"),
        ("מֵאֵת הָרַב", "ממן אכ'ד' כת'ירא", "from him who took much,"),
        ("תַּרְבּוּ", "כת'רו", "give more;"),
        ("וּמֵאֵת הַמְעַט", "ומן מן אכ'ד' קלילא", "and from him who took little,"),
        ("תַּמְעִיטוּ", "קללו", "give less;"),
        ("אִישׁ", "פליעט כל סבט", "each tribe shall give"),
        ("כְּפִי נַחֲלָתוֹ", "עלי' קדר נחלתה", "according to the measure of its inheritance."),
    ],
    9: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to"),
        ("אֶל-מֹשֶׁה", "מוסי'", "Moses"),
        ("לֵּאמֹר", "תכלימא", "directly."),
    ],
    10: [
        # HE: דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם כִּי אַתֶּם עֹבְרִים אֶת-הַיַּרְדֵּן אַרְצָה כְּנָעַן
        # JA: מר בני אסראיל. וקל להם. אד'א אנתם. גזתם אלארדן אלי' בלד כנעאן
        # EN: Command the sons of Israel, and say to them: When you have crossed the Jordan into the land of Canaan,
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel,"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("כִּי אַתֶּם", "אד'א אנתם", "When you"),
        ("עֹבְרִים", "גזתם", "have crossed"),
        ("אֶת-הַיַּרְדֵּן", "אלארדן", "the Jordan"),
        ("אַרְצָה כְּנָעַן", "אלי' בלד כנעאן", "into the land of Canaan,"),
    ],
    11: [
        # HE: וְהִקְרִיתֶם לָכֶם עָרִים עָרֵי מִקְלָט תִּהְיֶינָה לָכֶם וְנָס שָׁמָּה רֹצֵחַ מַכֵּה-נֶפֶשׁ בִּשְׁגָגָה
        # JA: פאסמו לכם קרא חמא. יהרב אלי'ה אי קאתל. קתל נפסא סהוא
        # EN: then designate for yourselves towns of refuge, so that any killer who has slain a person unintentionally may flee to them.
        ("וְהִקְרִיתֶם", "פאסמו", "then designate"),
        ("לָכֶם", "לכם", "for yourselves"),
        ("עָרִים", "קרא", "towns of"),
        ("עָרֵי מִקְלָט", "חמא", "refuge,"),
        ("וְנָס שָׁמָּה", "יהרב אלי'ה", "so that any killer"),
        ("רֹצֵחַ", "אי קאתל", "who has slain"),
        ("מַכֵּה-נֶפֶשׁ", "קתל נפסא", "a person unintentionally"),
        ("בִּשְׁגָגָה", "סהוא", "may flee to them."),
    ],
    12: [
        # HE: וְהָיוּ לָכֶם הֶעָרִים לְמִקְלָט מִגֹּאֵל וְלֹא יָמוּת הָרֹצֵחַ עַד-עָמְדוֹ לִפְנֵי הָעֵדָה לַמִּשְׁפָּט
        # JA: פתכון תלך אלקרא. תחמיה מן אלולי. ולא יקתל. חתי' יקף. בין ידי אלגמאעה פיחכמון עליה בד'אלך
        # EN: And those towns shall be a protection from the blood-avenger; and he shall not be killed until he has stood before the assembly, that they may judge him in this matter.
        ("וְהָיוּ", "פתכון", "And those towns shall be"),
        ("הֶעָרִים", "תלך אלקרא", "a protection"),
        ("לְמִקְלָט", "תחמיה", "from the blood-avenger;"),
        ("מִגֹּאֵל", "מן אלולי", "and he shall not be killed"),
        ("וְלֹא יָמוּת", "ולא יקתל", "until he has stood"),
        ("עַד-עָמְדוֹ", "חתי' יקף", "before the assembly,"),
        ("לִפְנֵי הָעֵדָה", "בין ידי אלגמאעה", "that they may judge"),
        ("לַמִּשְׁפָּט", "פיחכמון עליה בד'אלך", "him in this matter."),
    ],
    13: [
        # HE: וְהֶעָרִים אֲשֶׁר תִּתֵּנוּ--שֵׁשׁ-עָרֵי מִקְלָט תִּהְיֶינָה לָכֶם
        # JA: ואלקרא אלתי תעזלונהא. סת קרא חמא תכון לכם
        # EN: And the towns which you set apart — six towns of refuge shall they be for you.
        ("וְהֶעָרִים", "ואלקרא", "And the towns"),
        ("אֲשֶׁר תִּתֵּנוּ", "אלתי תעזלונהא", "which you set apart —"),
        ("שֵׁשׁ-עָרֵי", "סת קרא", "six towns of"),
        ("מִקְלָט", "חמא", "refuge"),
        ("תִּהְיֶינָה", "תכון", "shall they be"),
        ("לָכֶם", "לכם", "for you."),
    ],
    14: [
        # HE: אֵת שְׁלֹשׁ הֶעָרִים תִּתְּנוּ מֵעֵבֶר לַיַּרְדֵּן וְאֵת שְׁלֹשׁ הֶעָרִים תִּתְּנוּ בְּאֶרֶץ כְּנָעַן עָרֵי מִקְלָט תִּהְיֶינָה
        # JA: ת'לאת' מנהא פי עבר אלארדן. ות'לאת' מנהא פי בלד כנעאן. תכון קרא חמא
        # EN: Three of them shall be across the Jordan, and three of them shall be in the land of Canaan — they shall be towns of refuge.
        ("אֵת שְׁלֹשׁ", "ת'לאת' מנהא", "Three of them"),
        ("מֵעֵבֶר לַיַּרְדֵּן", "פי עבר אלארדן", "shall be across the Jordan,"),
        ("וְאֵת שְׁלֹשׁ", "ות'לאת' מנהא", "and three of them"),
        ("בְּאֶרֶץ כְּנָעַן", "פי בלד כנעאן", "shall be in the land of Canaan —"),
        ("עָרֵי מִקְלָט", "תכון קרא חמא", "they shall be towns of refuge."),
    ],
    15: [
        # HE: לִבְנֵי יִשְׂרָאֵל וְלַגֵּר וְלַתּוֹשָׁב בְּתוֹכָם תִּהְיֶינָה שֵׁשׁ-הֶעָרִים הָאֵלֶּה לְמִקְלָט--לָנוּס שָׁמָּה כָּל-מַכֵּה-נֶפֶשׁ בִּשְׁגָגָה
        # JA: לבני אסראיל. ולאלג'ריב אלדכ'יל פי מא בינהם. יהרב אלי'הא. כל מן קתל נפסא סהוא
        # EN: For the sons of Israel and for the stranger and for the guest who has entered among them — every one who has slain a person unintentionally may flee to them.
        ("לִבְנֵי", "לבני", "For the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel"),
        ("וְלַגֵּר", "ולאלג'ריב", "and for the stranger"),
        ("וְלַתּוֹשָׁב", "אלדכ'יל", "and for the guest"),
        ("בְּתוֹכָם", "פי מא בינהם", "who has entered among them —"),
        ("תִּהְיֶינָה שֵׁשׁ-הֶעָרִים", "יהרב אלי'הא", "every one who has slain"),
        ("כָּל-מַכֵּה-נֶפֶשׁ", "כל מן קתל נפסא", "a person unintentionally"),
        ("בִּשְׁגָגָה", "סהוא", "may flee to them."),
    ],
    16: [
        # HE: וְאִם-בִּכְלִי בַרְזֶל הִכָּהוּ וַיָּמֹת רֹצֵחַ הוּא מוֹת יוּמַת הָרֹצֵחַ
        # JA: ואמא אן כאן צ'רבה. באנא חדיד פקתלה פהו קאתל יסתחק אלקתל
        # EN: But if he struck him with an iron implement and killed him, he is a killer who deserves to be put to death.
        ("וְאִם", "ואמא אן כאן", "But if"),
        ("בִּכְלִי בַרְזֶל", "צ'רבה", "he struck him with an iron implement"),
        (None, "באנא חדיד", "and killed him,"),
        ("הִכָּהוּ וַיָּמֹת", "פקתלה", "he is a killer"),
        ("רֹצֵחַ הוּא", "פהו קאתל", "who deserves"),
        ("מוֹת יוּמַת הָרֹצֵחַ", "יסתחק אלקתל", "to be put to death."),
    ],
    17: [
        # HE: וְאִם בְּאֶבֶן יָד אֲשֶׁר-יָמוּת בָּהּ הִכָּהוּ וַיָּמֹת רֹצֵחַ הוּא מוֹת יוּמַת הָרֹצֵחַ
        # JA: או צ'רבה בחגר. מקבוץ' מקדאר מא ימות בהא פקתלה. פהו קאתל יסתחק אלקתל
        # EN: Or if he struck him with a stone held in the hand, of a size sufficient to cause death, and killed him, he is a killer who deserves to be put to death.
        ("וְאִם", "או", "Or if"),
        ("בְּאֶבֶן", "צ'רבה בחגר", "he struck him with a stone"),
        ("יָד", "מקבוץ'", "held in the hand,"),
        ("אֲשֶׁר-יָמוּת בָּהּ", "מקדאר מא ימות בהא", "of a size sufficient to cause death,"),
        ("הִכָּהוּ וַיָּמֹת", "פקתלה", "and killed him,"),
        ("רֹצֵחַ הוּא", "פהו קאתל", "he is a killer"),
        ("מוֹת יוּמַת הָרֹצֵחַ", "יסתחק אלקתל", "who deserves to be put to death."),
    ],
    18: [
        # HE: אוֹ בִּכְלִי עֵץ-יָד אֲשֶׁר-יָמוּת בּוֹ הִכָּהוּ וַיָּמֹת רֹצֵחַ הוּא מוֹת יוּמַת הָרֹצֵחַ
        # JA: או צ'רבה באנא כ'שב. מקבוץ' מקדאר מא ימות בה פקתלה פהו קאתל יסתחק אלקתל
        # EN: Or if he struck him with a wooden implement held in the hand, of a size sufficient to cause death, and killed him, he is a killer who deserves to be put to death.
        ("אוֹ", "או", "Or"),
        ("בִּכְלִי עֵץ-יָד", "צ'רבה באנא כ'שב", "if he struck him with a wooden implement"),
        ("אֲשֶׁר-יָמוּת בּוֹ", "מקבוץ' מקדאר מא ימות בה", "held in the hand, of a size sufficient to cause death,"),
        ("הִכָּהוּ וַיָּמֹת", "פקתלה", "and killed him,"),
        ("רֹצֵחַ הוּא", "פהו קאתל", "he is a killer"),
        ("מוֹת יוּמַת הָרֹצֵחַ", "יסתחק אלקתל", "who deserves to be put to death."),
    ],
    19: [
        # HE: גֹּאֵל הַדָּם הוּא יָמִית אֶת-הָרֹצֵחַ בְּפִגְעוֹ-בוֹ הוּא יְמִתֶנּוּ
        # JA: ולי אלדם הו יקתלה אד'א פאגאה בחק
        # EN: The blood-avenger — he shall put him to death when he encounters him, rightfully.
        ("גֹּאֵל", "ולי", "The blood-avenger —"),
        ("הַדָּם", "אלדם", "he shall"),
        ("הוּא יָמִית", "הו יקתלה", "put him to death"),
        ("בְּפִגְעוֹ-בוֹ", "אד'א פאגאה", "when he encounters him,"),
        ("הוּא יְמִתֶנּוּ", "בחק", "rightfully."),
    ],
    20: [
        # HE: וְאִם-בְּשִׂנְאָה יֶהְדֳּפֶנּוּ אוֹ-הִשְׁלִיךְ עָלָיו בִּצְדִיָּה וַיָּמֹת
        # JA: ואן דפעה בשנאה. או טרח עלי'ה שייא. בתעמד פקתלה
        # EN: And if he shoved him out of hatred, or hurled something at him deliberately, and killed him,
        ("וְאִם", "ואן", "And if"),
        ("בְּשִׂנְאָה", "בשנאה", "he shoved him out of hatred,"),
        ("יֶהְדֳּפֶנּוּ", "דפעה", "or"),
        ("אוֹ-הִשְׁלִיךְ", "או טרח עלי'ה", "hurled something"),
        ("עָלָיו", "שייא", "at him"),
        ("בִּצְדִיָּה", "בתעמד", "deliberately,"),
        ("וַיָּמֹת", "פקתלה", "and killed him,"),
    ],
    21: [
        # HE: אוֹ בְאֵיבָה הִכָּהוּ בְיָדוֹ וַיָּמֹת--מוֹת-יוּמַת הַמַּכֶּה רֹצֵחַ הוּא גֹּאֵל הַדָּם יָמִית אֶת-הָרֹצֵחַ--בְּפִגְעוֹ-בוֹ
        # JA: או צ'רבה בידה בעדאוה פקתלה. פליקתל אלצ'ארב קתלא לאנה קאתל. פולי אלדם יקתלה אד'א פאגאה בחק
        # EN: or struck him with his hand out of enmity and killed him — then the striker shall surely be put to death, for he is a killer; the blood-avenger shall put him to death when he encounters him, rightfully.
        ("אוֹ", "או", "or"),
        ("בְאֵיבָה", "צ'רבה בידה בעדאוה", "struck him with his hand out of enmity"),
        ("הִכָּהוּ", "פקתלה", "and killed him —"),
        ("מוֹת-יוּמַת הַמַּכֶּה", "פליקתל אלצ'ארב קתלא", "then the striker shall surely be put to death,"),
        ("רֹצֵחַ הוּא", "לאנה קאתל", "for he is a killer;"),
        ("גֹּאֵל הַדָּם", "פולי אלדם", "the blood-avenger"),
        ("יָמִית", "יקתלה", "shall put him to death"),
        ("בְּפִגְעוֹ-בוֹ", "אד'א פאגאה בחק", "when he encounters him, rightfully."),
    ],
    22: [
        # HE: וְאִם-בְּפֶתַע בְּלֹא-אֵיבָה הֲדָפוֹ אוֹ-הִשְׁלִיךְ עָלָיו כָּל-כְּלִי בְּלֹא צְדִיָּה
        # JA: ואן דפעה בג'תה בלא בג'צ'ה. או טרח עלי'ה. אייה' אניה בלא תעמד
        # EN: But if he pushed him suddenly without hatred, or threw any implement at him without intent,
        ("וְאִם", "ואן", "But if"),
        ("בְּפֶתַע", "דפעה בג'תה", "he pushed him suddenly"),
        ("בְּלֹא-אֵיבָה", "בלא בג'צ'ה", "without hatred,"),
        ("הֲדָפוֹ", "או", "or"),
        ("אוֹ-הִשְׁלִיךְ", "טרח עלי'ה", "threw any implement"),
        ("כָּל-כְּלִי", "אייה' אניה", "at him"),
        ("בְּלֹא צְדִיָּה", "בלא תעמד", "without intent,"),
    ],
    23: [
        # HE: אוֹ בְכָל-אֶבֶן אֲשֶׁר-יָמוּת בָּהּ בְּלֹא רְאוֹת וַיַּפֵּל עָלָיו וַיָּמֹת וְהוּא לֹא-אוֹיֵב לוֹ וְלֹא מְבַקֵּשׁ רָעָתוֹ
        # JA: או אוקע עלי'ה. אי חגר כאן בלא תעמד פמאת. והו פי ד'אלך ליס בעדו לה. ולא טאלב שרה
        # EN: or dropped upon him any stone — without intent — and he died, and he was not his enemy and was not seeking his harm,
        ("אוֹ", "או", "or"),
        ("בְכָל-אֶבֶן", "אוקע עלי'ה", "dropped upon him"),
        ("אֲשֶׁר-יָמוּת בָּהּ", "אי חגר כאן", "any stone —"),
        ("בְּלֹא רְאוֹת", "בלא תעמד", "without intent —"),
        ("וַיַּפֵּל עָלָיו", "פמאת", "and he died,"),
        ("וְהוּא", "והו פי ד'אלך", "and he was"),
        ("לֹא-אוֹיֵב לוֹ", "ליס בעדו לה", "not his enemy"),
        ("וְלֹא מְבַקֵּשׁ", "ולא טאלב", "and was not seeking"),
        ("רָעָתוֹ", "שרה", "his harm,"),
    ],
    24: [
        # HE: וְשָׁפְטוּ הָעֵדָה בֵּין הַמַּכֶּה וּבֵין גֹּאֵל הַדָּם--עַל הַמִּשְׁפָּטִים הָאֵלֶּה
        # JA: פלתחכם אלגמאעה. בין אלקאתל ובין אלולי. בהד'א אלאחכאם
        # EN: then the assembly shall judge between the killer and the blood-avenger, according to these ordinances.
        ("וְשָׁפְטוּ", "פלתחכם", "then the assembly shall judge"),
        ("הָעֵדָה", "אלגמאעה", "between the killer"),
        ("בֵּין הַמַּכֶּה", "בין אלקאתל", "and the blood-avenger,"),
        ("וּבֵין גֹּאֵל הַדָּם", "ובין אלולי", "according to"),
        ("עַל הַמִּשְׁפָּטִים", "בהד'א", "these"),
        ("הָאֵלֶּה", "אלאחכאם", "ordinances."),
    ],
    25: [
        # HE: וְהִצִּילוּ הָעֵדָה אֶת-הָרֹצֵחַ מִיַּד גֹּאֵל הַדָּם וְהֵשִׁיבוּ אֹתוֹ הָעֵדָה אֶל-עִיר מִקְלָטוֹ אֲשֶׁר-נָס שָׁמָּה וְיָשַׁב בָּהּ עַד-מוֹת הַכֹּהֵן הַגָּדֹל אֲשֶׁר-מָשַׁח אֹתוֹ בְּשֶׁמֶן הַקֹּדֶשׁ
        # JA: ותכ'לץ. אלגמאעה הד'א אלקאתל. מן יד אלולי. ותרדה אלי' קריה' חמאה אלתי הרב אלי'הא ויקים ת'ם. אלי' מות אלאמאם אלכביר. אלד'י מסח בדהן אלקדס
        # EN: And the assembly shall deliver this killer from the hand of the blood-avenger, and shall return him to the town of refuge to which he fled; and he shall remain there until the death of the great imām who was anointed with the oil of holiness.
        ("וְהִצִּילוּ", "ותכ'לץ", "And the assembly shall deliver"),
        ("הָעֵדָה", "אלגמאעה", "this killer"),
        ("אֶת-הָרֹצֵחַ", "הד'א אלקאתל", "from the hand of"),
        ("מִיַּד גֹּאֵל הַדָּם", "מן יד אלולי", "the blood-avenger,"),
        ("וְהֵשִׁיבוּ", "ותרדה", "and shall return him"),
        ("אֶל-עִיר מִקְלָטוֹ", "אלי' קריה' חמאה", "to the town of refuge"),
        ("אֲשֶׁר-נָס שָׁמָּה", "אלתי הרב אלי'הא", "to which he fled;"),
        ("וְיָשַׁב בָּהּ", "ויקים ת'ם", "and he shall remain there"),
        ("עַד-מוֹת", "אלי' מות", "until the death of"),
        ("הַכֹּהֵן הַגָּדֹל", "אלאמאם אלכביר", "the great imām"),
        ("אֲשֶׁר-מָשַׁח", "אלד'י מסח", "who was anointed"),
        ("בְּשֶׁמֶן הַקֹּדֶשׁ", "בדהן אלקדס", "with the oil of holiness."),
    ],
    26: [
        # HE: וְאִם-יָצֹא יֵצֵא הָרֹצֵחַ אֶת-גְּבוּל עִיר מִקְלָטוֹ אֲשֶׁר יָנוּס שָׁמָּה
        # JA: פאן הו כ'רג ען חד קריה חמאה. אלתי הרב אלי'הא
        # EN: But if he goes out beyond the boundary of the town of refuge to which he fled,
        ("וְאִם", "פאן הו", "But if he"),
        ("יָצֹא יֵצֵא", "כ'רג", "goes out"),
        ("אֶת-גְּבוּל", "ען חד", "beyond the boundary of"),
        ("עִיר מִקְלָטוֹ", "קריה חמאה", "the town of refuge"),
        ("אֲשֶׁר יָנוּס שָׁמָּה", "אלתי הרב אלי'הא", "to which he fled,"),
    ],
    27: [
        # HE: וּמָצָא אֹתוֹ גֹּאֵל הַדָּם מִחוּץ לִגְבוּל עִיר מִקְלָטוֹ וְרָצַח גֹּאֵל הַדָּם אֶת-הָרֹצֵחַ--אֵין לוֹ דָּם
        # JA: פוגדה אלולי. כ'ארג ען חד קריה' חמאה. פקתלה. פלא ת'יאר לה
        # EN: and the blood-avenger finds him outside the boundary of the town of refuge and kills him — there is no vengeance for him.
        ("וּמָצָא", "פוגדה", "and the blood-avenger finds him"),
        ("גֹּאֵל הַדָּם", "אלולי", "outside the boundary"),
        ("מִחוּץ לִגְבוּל", "כ'ארג ען חד", "of the town of refuge"),
        ("עִיר מִקְלָטוֹ", "קריה' חמאה", "and kills him —"),
        ("וְרָצַח גֹּאֵל הַדָּם", "פקתלה", "there is no"),
        ("אֵין לוֹ דָּם", "פלא ת'יאר לה", "vengeance for him."),
    ],
    28: [
        # HE: כִּי בְעִיר מִקְלָטוֹ יֵשֵׁב עַד-מוֹת הַכֹּהֵן הַגָּדֹל וְאַחֲרֵי מוֹת הַכֹּהֵן הַגָּדֹל--יָשׁוּב הָרֹצֵחַ אֶל-אֶרֶץ אֲחֻזָּתוֹ
        # JA: בל יגלס פי קריה' חמאה. אלי' מות אלאמאם אלכביר. ובעד מותה. ירגע אלי' ארץ' חוזה
        # EN: Rather, he must stay in the town of refuge until the death of the great imām; and after his death he may return to the land of his possession.
        ("כִּי", "בל", "Rather,"),
        ("בְעִיר מִקְלָטוֹ", "יגלס פי קריה' חמאה", "he must stay in the town of refuge"),
        ("יֵשֵׁב עַד-מוֹת", "אלי' מות", "until the death of"),
        ("הַכֹּהֵן הַגָּדֹל", "אלאמאם אלכביר", "the great imām;"),
        ("וְאַחֲרֵי מוֹת", "ובעד מותה", "and after his death"),
        ("הַכֹּהֵן הַגָּדֹל", "ירגע", "he may return"),
        ("יָשׁוּב הָרֹצֵחַ", "אלי' ארץ'", "to the land of"),
        ("אֶל-אֶרֶץ אֲחֻזָּתוֹ", "חוזה", "his possession."),
    ],
    29: [
        # HE: וְהָיוּ אֵלֶּה לָכֶם לְחֻקַּת מִשְׁפָּט לְדֹרֹתֵיכֶם בְּכֹל מוֹשְׁבֹתֵיכֶם
        # JA: פתכון הד'ה לכם חכם עלי' מר אגיאלכם פי גמיע מסאכנכם
        # EN: And these shall be ordinances for you throughout the passing of your generations, in all your dwellings.
        ("וְהָיוּ", "פתכון", "And these shall be"),
        ("אֵלֶּה", "הד'ה", "ordinances"),
        ("לָכֶם", "לכם", "for you"),
        ("לְחֻקַּת מִשְׁפָּט", "חכם", "throughout"),
        ("לְדֹרֹתֵיכֶם", "עלי' מר אגיאלכם", "the passing of your generations,"),
        ("בְּכֹל מוֹשְׁבֹתֵיכֶם", "פי גמיע מסאכנכם", "in all your dwellings."),
    ],
    30: [
        # HE: כָּל-מַכֵּה-נֶפֶשׁ--לְפִי עֵדִים יִרְצַח אֶת-הָרֹצֵחַ וְעֵד אֶחָד לֹא-יַעֲנֶה בְנֶפֶשׁ לָמוּת
        # JA: כל מן קתל נפסא עאמדא. פבקול שאהדין אקתלוה ואמא שאהד ואחד. פלא ישהד עלי'ה פיקתל
        # EN: Every one who has slain a person intentionally — by the word of two witnesses put him to death; but a single witness shall not testify against him so that he be put to death.
        ("כָּל-מַכֵּה-נֶפֶשׁ", "כל מן קתל נפסא", "Every one who has slain a person"),
        (None, "עאמדא", "intentionally —"),
        ("לְפִי עֵדִים", "פבקול שאהדין", "by the word of two witnesses"),
        ("יִרְצַח אֶת-הָרֹצֵחַ", "אקתלוה", "put him to death;"),
        ("וְעֵד אֶחָד", "ואמא שאהד ואחד", "but a single witness"),
        ("לֹא-יַעֲנֶה", "פלא ישהד עלי'ה", "shall not testify against him"),
        ("בְנֶפֶשׁ לָמוּת", "פיקתל", "so that he be put to death."),
    ],
    31: [
        # HE: וְלֹא-תִקְחוּ כֹפֶר לְנֶפֶשׁ רֹצֵחַ אֲשֶׁר-הוּא רָשָׁע לָמוּת כִּי-מוֹת יוּמָת
        # JA: ולא תאכדו דיה ען נפס קאתל. יגב עלי'ה אלקתל. אלא יקתל קתלא
        # EN: And you shall not accept blood-money as ransom for the life of a killer who is liable to be put to death — he shall surely be put to death.
        ("וְלֹא-תִקְחוּ", "ולא תאכדו", "And you shall not accept"),
        ("כֹפֶר", "דיה", "blood-money as ransom"),
        ("לְנֶפֶשׁ רֹצֵחַ", "ען נפס קאתל", "for the life of a killer"),
        ("אֲשֶׁר-הוּא רָשָׁע", "יגב עלי'ה", "who is liable"),
        ("לָמוּת", "אלקתל", "to be put to death —"),
        ("כִּי-מוֹת יוּמָת", "אלא יקתל קתלא", "he shall surely be put to death."),
    ],
    32: [
        # HE: וְלֹא-תִקְחוּ כֹפֶר לָנוּס אֶל-עִיר מִקְלָטוֹ לָשׁוּב לָשֶׁבֶת בָּאָרֶץ עַד-מוֹת הַכֹּהֵן
        # JA: ולא תאכדו מנה איצ'א דיה. לתהרבוה אלי' בעץ' קרא אלחמא. ליעוד ויסכן אלבלד. בעד מות אלאמאם
        # EN: Nor shall you accept from him blood-money to allow him to flee to one of the towns of refuge, so that he may return and dwell in the land after the death of the imām.
        ("וְלֹא-תִקְחוּ", "ולא תאכדו מנה", "Nor shall you accept from him"),
        ("כֹפֶר", "איצ'א דיה", "blood-money"),
        ("לָנוּס", "לתהרבוה", "to allow him to flee"),
        ("אֶל-עִיר מִקְלָטוֹ", "אלי' בעץ' קרא אלחמא", "to one of the towns of refuge,"),
        ("לָשׁוּב", "ליעוד", "so that he may return"),
        ("לָשֶׁבֶת", "ויסכן", "and dwell"),
        ("בָּאָרֶץ", "אלבלד", "in the land"),
        ("עַד-מוֹת הַכֹּהֵן", "בעד מות אלאמאם", "after the death of the imām."),
    ],
    33: [
        # HE: וְלֹא-תַחֲנִיפוּ אֶת-הָאָרֶץ אֲשֶׁר אַתֶּם בָּהּ כִּי הַדָּם הוּא יַחֲנִיף אֶת-הָאָרֶץ וְלָאָרֶץ לֹא-יְכֻפַּר לַדָּם אֲשֶׁר שֻׁפַּךְ-בָּהּ כִּי-אִם בְּדַם שֹׁפְכוֹ
        # JA: ולא תדנסו אלבלד. אלד'י אנתם פיה. לאן אלדם ידנסה ולא יג'פר לכם. ען אלדם אלד'י ספך פיה. אלא בדם סאפכה
        # EN: And you shall not defile the land in which you are; for blood defiles it, and atonement cannot be made for you concerning the blood that was shed in it, except by the blood of him who shed it.
        ("וְלֹא-תַחֲנִיפוּ", "ולא תדנסו", "And you shall not defile"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר אַתֶּם בָּהּ", "אלד'י אנתם פיה", "in which you are;"),
        ("כִּי", "לאן", "for"),
        ("הַדָּם", "אלדם", "blood"),
        ("הוּא יַחֲנִיף", "ידנסה", "defiles it,"),
        ("וְלָאָרֶץ לֹא-יְכֻפַּר", "ולא יג'פר לכם", "and atonement cannot be made for you"),
        ("לַדָּם", "ען אלדם", "concerning the blood"),
        ("אֲשֶׁר שֻׁפַּךְ-בָּהּ", "אלד'י ספך פיה", "that was shed in it,"),
        ("כִּי-אִם", "אלא", "except"),
        ("בְּדַם שֹׁפְכוֹ", "בדם סאפכה", "by the blood of him who shed it."),
    ],
    34: [
        # HE: וְלֹא תְטַמֵּא אֶת-הָאָרֶץ אֲשֶׁר אַתֶּם יֹשְׁבִים בָּהּ אֲשֶׁר אֲנִי שֹׁכֵן בְּתוֹכָהּ כִּי אֲנִי יְהוָה--שֹׁכֵן בְּתוֹךְ בְּנֵי יִשְׂרָאֵל
        # JA: ולא תנגסו אלבלד. אלד'י אנתם מקימין פיה. אלד'י נורי סאכן פיה. פאני אללה. נורי סאכן. פי מא בין בני אסראיל
        # EN: And you shall not make impure the land in which you are dwelling, in which My light dwells — for I am God, My light dwelling in the midst of the sons of Israel.
        ("וְלֹא תְטַמֵּא", "ולא תנגסו", "And you shall not make impure"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר אַתֶּם יֹשְׁבִים בָּהּ", "אלד'י אנתם מקימין פיה", "in which you are dwelling,"),
        ("אֲשֶׁר אֲנִי שֹׁכֵן", "אלד'י נורי סאכן פיה", "in which My light dwells —"),
        ("כִּי אֲנִי", "פאני", "for I am"),
        ("יְהוָה", "אללה", "God,"),
        ("שֹׁכֵן", "נורי סאכן", "My light dwelling"),
        ("בְּתוֹךְ בְּנֵי יִשְׂרָאֵל", "פי מא בין בני אסראיל", "in the midst of the sons of Israel."),
    ],
}

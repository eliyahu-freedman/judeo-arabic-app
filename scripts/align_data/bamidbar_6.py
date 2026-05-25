"""Hand-authored word-level alignment triples for Bamidbar chapter 6."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses, a speaking.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "spoke"),
        ("יְהוָה", "אללה", "God"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses,"),
        ("לֵּאמֹר", "תכלימא", "a speaking."),
    ],
    2: [
        # HE: דַּבֵּר אֶל-בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם אִישׁ אוֹ-אִשָּׁה כִּי יַפְלִא לִנְדֹּר נֶדֶר נָזִיר--לְהַזִּיר לַיהוָה
        # JA: מר בני אסראיל. וקל להם. אי רגל או אמראה. סווג' נד'רא נסך. ליתנסך לרבה
        # EN: Command the sons of Israel, and say to them: Any man or woman who has deemed a vow of devotion lawful, to practice devotion to his Lord —
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel,"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֲלֵהֶם", "להם", "to them:"),
        ("אִישׁ", "אי רגל", "Any man"),
        ("אוֹ-אִשָּׁה", "או אמראה", "or woman"),
        ("כִּי יַפְלִא", "סווג'", "who has deemed"),
        ("לִנְדֹּר", "נד'רא", "a vow"),
        ("נֶדֶר נָזִיר", "נסך", "of devotion lawful,"),
        ("לְהַזִּיר", "ליתנסך", "to practice devotion"),
        ("לַיהוָה", "לרבה", "to his Lord —"),
    ],
    3: [
        # HE: מִיַּיִן וְשֵׁכָר יַזִּיר חֹמֶץ יַיִן וְחֹמֶץ שֵׁכָר לֹא יִשְׁתֶּה וְכָל-מִשְׁרַת עֲנָבִים לֹא יִשְׁתֶּה וַעֲנָבִים לַחִים וִיבֵשִׁים לֹא יֹאכֵל
        # JA: פמן אלכ'מר ואלמסכר מנה יתנסך. חתא כ'ל כ'מר. וכ'ל מ'סכר לא ישרב. וכל נקיע אלענב לא ישרב. וענבא רטבא ויאבסא לא יאכל
        # EN: from wine and from what is intoxicating he shall practice devotion, such that even vinegar of wine and vinegar of an intoxicating drink he shall not drink; and every infusion of grapes he shall not drink; and grapes, fresh or dried, he shall not eat.
        ("מִיַּיִן", "פמן אלכ'מר", "from wine"),
        ("וְשֵׁכָר", "ואלמסכר", "and from what is intoxicating"),
        ("יַזִּיר", "מנה יתנסך", "he shall practice devotion,"),
        ("חֹמֶץ יַיִן", "חתא כ'ל כ'מר", "such that even vinegar of wine"),
        ("וְחֹמֶץ שֵׁכָר", "וכ'ל מ'סכר", "and vinegar of an intoxicating drink"),
        ("לֹא יִשְׁתֶּה", "לא ישרב", "he shall not drink;"),
        ("וְכָל-מִשְׁרַת", "וכל נקיע", "and every infusion of"),
        ("עֲנָבִים", "אלענב", "grapes"),
        (None, "לא ישרב", "he shall not drink;"),
        ("וַעֲנָבִים", "וענבא", "and grapes,"),
        ("לַחִים", "רטבא", "fresh"),
        ("וִיבֵשִׁים", "ויאבסא", "or dried,"),
        ("לֹא יֹאכֵל", "לא יאכל", "he shall not eat."),
    ],
    4: [
        # HE: כֹּל יְמֵי נִזְרוֹ מִכֹּל אֲשֶׁר יֵעָשֶׂה מִגֶּפֶן הַיַּיִן מֵחַרְצַנִּים וְעַד-זָג--לֹא יֹאכֵל
        # JA: טול אייאם נסכה. מן כל מא יעמל מן גפן אלכ'מר. מן אלפרצן אלי' אלזג לא יאכל
        # EN: All the days of his devotion, from everything made from the vine of wine — from the seeds to the skin surrounding it — he shall not eat.
        ("כֹּל", "טול", "All"),
        ("יְמֵי", "אייאם", "the days of"),
        ("נִזְרוֹ", "נסכה", "his devotion,"),
        ("מִכֹּל", "מן כל", "from everything"),
        ("אֲשֶׁר יֵעָשֶׂה", "מא יעמל", "made"),
        ("מִגֶּפֶן", "מן גפן", "from the vine of"),
        ("הַיַּיִן", "אלכ'מר", "wine —"),
        ("מֵחַרְצַנִּים", "מן אלפרצן", "from the seeds"),
        ("וְעַד-זָג", "אלי' אלזג", "to the skin surrounding it —"),
        ("לֹא יֹאכֵל", "לא יאכל", "he shall not eat."),
    ],
    5: [
        # HE: כָּל-יְמֵי נֶדֶר נִזְרוֹ תַּעַר לֹא-יַעֲבֹר עַל-רֹאשׁוֹ עַד-מְלֹאת הַיָּמִם אֲשֶׁר-יַזִּיר לַיהוָה קָדֹשׁ יִהְיֶה--גַּדֵּל פֶּרַע שְׂעַר רֹאשׁוֹ
        # JA: וטול אייאם נד'ר נסכה. לא ימר חאלק עלי' ראסה. אלי' אן תתם אלאייאם. אלתי תנסכהא לרבה יכון מקדסא. וירבי פרע שער ראסה
        # EN: And all the days of the vow of his devotion, no razor shall pass over his head, until the days he devotes to his Lord are complete; he shall be consecrated, and shall grow out the branch of the hair of his head.
        ("כָּל-יְמֵי", "וטול אייאם", "And all the days of"),
        ("נֶדֶר", "נד'ר", "the vow of"),
        ("נִזְרוֹ", "נסכה", "his devotion,"),
        ("תַּעַר", "חאלק", "no razor"),
        ("לֹא-יַעֲבֹר", "לא ימר", "shall pass"),
        ("עַל-רֹאשׁוֹ", "עלי' ראסה", "over his head,"),
        ("עַד-מְלֹאת", "אלי' אן תתם", "until"),
        ("הַיָּמִם", "אלאייאם", "the days"),
        ("אֲשֶׁר-יַזִּיר", "אלתי תנסכהא", "he devotes"),
        ("לַיהוָה", "לרבה", "to his Lord"),
        (None, "יכון", "are complete; he shall be"),
        ("קָדֹשׁ יִהְיֶה", "מקדסא", "consecrated,"),
        ("גַּדֵּל", "וירבי", "and shall grow out"),
        ("פֶּרַע", "פרע", "the branch of"),
        ("שְׂעַר", "שער", "the hair of"),
        ("רֹאשׁוֹ", "ראסה", "his head."),
    ],
    6: [
        # HE: כָּל-יְמֵי הַזִּירוֹ לַיהוָה עַל-נֶפֶשׁ מֵת לֹא יָבֹא
        # JA: כד'אך טול אייאם נסכה ללה. אלי' חצ'רה מיית לא ידכ'ל
        # EN: Likewise, all the days of his devotion to God, he shall not enter into the presence of a dead person.
        (None, "כד'אך", "Likewise,"),
        ("כָּל-יְמֵי", "טול אייאם", "all the days of"),
        ("הַזִּירוֹ", "נסכה", "his devotion"),
        ("לַיהוָה", "ללה", "to God,"),
        ("עַל-נֶפֶשׁ", "אלי' חצ'רה", "into the presence of"),
        ("מֵת", "מיית", "a dead person"),
        ("לֹא יָבֹא", "לא ידכ'ל", "he shall not enter"),
    ],
    7: [
        # HE: לְאָבִיו וּלְאִמּוֹ לְאָחִיו וּלְאַחֹתוֹ--לֹא-יִטַּמָּא לָהֶם בְּמֹתָם כִּי נֵזֶר אֱלֹהָיו עַל-רֹאשׁוֹ
        # JA: חתא באביה ואמה. ואכ'יה וא'כ'תה. לא יתנגס בהם פי חאל מותהם. לאן נסך רבה עלי'ה
        # EN: Not even for his father or his mother, his brother or his sister — he shall not defile himself through them at the time of their death, because the devotion to his Lord is upon him.
        (None, "חתא", "Not even for"),
        ("לְאָבִיו", "באביה", "his father"),
        ("וּלְאִמּוֹ", "ואמה", "or his mother,"),
        ("לְאָחִיו", "ואכ'יה", "his brother"),
        ("וּלְאַחֹתוֹ", "וא'כ'תה", "or his sister —"),
        ("לֹא-יִטַּמָּא", "לא יתנגס", "he shall not defile himself"),
        ("לָהֶם", "בהם", "through them"),
        ("בְּמֹתָם", "פי חאל מותהם", "at the time of their death,"),
        ("כִּי", "לאן", "because"),
        ("נֵזֶר", "נסך", "the devotion"),
        ("אֱלֹהָיו", "רבה", "to his Lord"),
        ("עַל-רֹאשׁוֹ", "עלי'ה", "is upon him."),
    ],
    8: [
        # HE: כֹּל יְמֵי נִזְרוֹ קָדֹשׁ הוּא לַיהוָה
        # JA: כד'אך טול אייאם נסכה. מקדס הו לרבה
        # EN: Likewise, all the days of his devotion, he is consecrated to his Lord.
        (None, "כד'אך", "Likewise,"),
        ("כֹּל", "טול", "all the days of"),
        ("יְמֵי", "אייאם", "his devotion,"),
        ("נִזְרוֹ", "נסכה", "he is"),
        ("קָדֹשׁ הוּא", "מקדס הו", "consecrated"),
        ("לַיהוָה", "לרבה", "to his Lord."),
    ],
    10: [
        # HE: וּבַיּוֹם הַשְּׁמִינִי יָבִא שְׁתֵּי תֹרִים אוֹ שְׁנֵי בְּנֵי יוֹנָה אֶל-הַכֹּהֵן--אֶל-פֶּתַח אֹהֶל מוֹעֵד
        # JA: ופי אליום אלתאמן. יאתי בשפנינין. או פרכ'י חמאם. אלי' אלאמאם. אלי' באב כ'בא אלמחצ'ר
        # EN: And on the eighth day, he shall bring two sparrows or two young pigeons to the imām, to the entrance of the tent of the assembly.
        ("וּבַיּוֹם", "ופי אליום", "And on the"),
        ("הַשְּׁמִינִי", "אלתאמן", "eighth day,"),
        ("יָבִא", "יאתי", "he shall bring"),
        ("שְׁתֵּי תֹרִים", "בשפנינין", "two sparrows"),
        ("אוֹ", "או", "or"),
        ("שְׁנֵי בְּנֵי יוֹנָה", "פרכ'י חמאם", "two young pigeons"),
        ("אֶל-הַכֹּהֵן", "אלי' אלאמאם", "to the imām,"),
        ("אֶל-פֶּתַח", "אלי' באב", "to the entrance of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly."),
    ],
    11: [
        # HE: וְעָשָׂה הַכֹּהֵן אֶחָד לְחַטָּאת וְאֶחָד לְעֹלָה וְכִפֶּר עָלָיו מֵאֲשֶׁר חָטָא עַל-הַנָּפֶשׁ וְקִדַּשׁ אֶת-רֹאשׁוֹ בַּיּוֹם הַהוּא
        # JA: ויעמל אחדהמא ד'כוה. ואלאכ'ר צעידה. ויסתג'פר ענה. במא אכ'טא פי אמר מיית. ויקדס ראסה פי ד'אלך אלוקת
        # EN: And he shall make one of them a purification-offering, and the other a burnt-offering; and he shall seek forgiveness for him for what he erred in the matter of the dead person; and his head shall be consecrated at that time.
        ("וְעָשָׂה", "ויעמל", "And he shall make"),
        ("הַכֹּהֵן אֶחָד", "אחדהמא", "one of them"),
        ("לְחַטָּאת", "ד'כוה", "a purification-offering,"),
        ("וְאֶחָד", "ואלאכ'ר", "and the other"),
        ("לְעֹלָה", "צעידה", "a burnt-offering;"),
        ("וְכִפֶּר", "ויסתג'פר", "and he shall seek forgiveness"),
        ("עָלָיו", "ענה", "for him"),
        ("מֵאֲשֶׁר חָטָא", "במא אכ'טא", "for what he erred"),
        ("עַל-הַנָּפֶשׁ", "פי אמר מיית", "in the matter of the dead person;"),
        ("וְקִדַּשׁ", "ויקדס", "and his head shall be consecrated"),
        ("אֶת-רֹאשׁוֹ", "ראסה", "at"),
        ("בַּיּוֹם הַהוּא", "פי ד'אלך אלוקת", "that time."),
    ],
    12: [
        # HE: וְהִזִּיר לַיהוָה אֶת-יְמֵי נִזְרוֹ וְהֵבִיא כֶּבֶשׂ בֶּן-שְׁנָתוֹ לְאָשָׁם וְהַיָּמִים הָרִאשֹׁנִים יִפְּלוּ כִּי טָמֵא נִזְרוֹ
        # JA: ויתנסך ללה אייאם נסכה ויאתי. בחמל אבן סנתה לקרבאן אלאתם. ואלאייאם אלמתקדמה תסקט. למא אנקטע נסכה
        # EN: And he shall practice devotion to God for the days of his devotion, and shall bring a lamb in its first year as a guilt-offering; and the preceding days shall lapse, for his devotion was interrupted.
        ("וְהִזִּיר", "ויתנסך", "And he shall practice devotion"),
        ("לַיהוָה", "ללה", "to God"),
        ("אֶת-יְמֵי", "אייאם", "for the days of"),
        ("נִזְרוֹ", "נסכה", "his devotion,"),
        ("וְהֵבִיא", "ויאתי", "and shall bring"),
        ("כֶּבֶשׂ", "בחמל", "a lamb"),
        ("בֶּן-שְׁנָתוֹ", "אבן סנתה", "in its first year"),
        ("לְאָשָׁם", "לקרבאן אלאתם", "as a guilt-offering;"),
        ("וְהַיָּמִים", "ואלאייאם", "and the preceding"),
        ("הָרִאשֹׁנִים", "אלמתקדמה", "days"),
        ("יִפְּלוּ", "תסקט", "shall lapse,"),
        ("כִּי", "למא", "for"),
        ("טָמֵא", "אנקטע", "was interrupted"),
        ("נִזְרוֹ", "נסכה", "his devotion"),
    ],
    13: [
        # HE: וְזֹאת תּוֹרַת הַנָּזִיר בְּיוֹם מְלֹאת יְמֵי נִזְרוֹ יָבִיא אֹתוֹ אֶל-פֶּתַח אֹהֶל מוֹעֵד
        # JA: והד'ה שריעה' אלנאסך. פי יום כמאל אייאם נסכה. יאתי בה. אלי' באב כ'בא אלמחצ'ר
        # EN: And this is the law of the devotee: on the day of the completion of the days of his devotion, he shall bring him to the entrance of the tent of the assembly.
        ("וְזֹאת", "והד'ה", "And this is"),
        ("תּוֹרַת", "שריעה'", "the law of"),
        ("הַנָּזִיר", "אלנאסך", "the devotee:"),
        ("בְּיוֹם", "פי יום", "on the day of"),
        ("מְלֹאת", "כמאל", "the completion of"),
        ("יְמֵי", "אייאם", "the days of"),
        ("נִזְרוֹ", "נסכה", "his devotion,"),
        ("יָבִיא", "יאתי", "he shall bring"),
        ("אֹתוֹ", "בה", "him"),
        ("אֶל-פֶּתַח", "אלי' באב", "to the entrance of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly."),
    ],
    14: [
        # HE: וְהִקְרִיב אֶת-קָרְבָּנוֹ לַיהוָה כֶּבֶשׂ בֶּן-שְׁנָתוֹ תָמִים אֶחָד לְעֹלָה וְכַבְשָׂה אַחַת בַּת-שְׁנָתָהּ תְּמִימָה לְחַטָּאת וְאַיִל-אֶחָד תָּמִים לִשְׁלָמִים
        # JA: פיקרב קרבאנה ללה. חמלא אבן סנתה צחיחא לאלצעידה. ורכ'לה אבנה' סנתהא. צחיחה לאלדכוה. וכבשא צחיחא לד'בח אלסלאמה
        # EN: And he shall present his offering to God: a lamb in its first year, unblemished, for the burnt-offering; and a ewe-lamb in its first year, unblemished, for the purification-offering; and a ram, unblemished, for the peace-offering.
        ("וְהִקְרִיב", "פיקרב", "And he shall present"),
        ("אֶת-קָרְבָּנוֹ", "קרבאנה", "his offering"),
        ("לַיהוָה", "ללה", "to God:"),
        ("כֶּבֶשׂ", "חמלא", "a lamb"),
        ("בֶּן-שְׁנָתוֹ", "אבן סנתה", "in its first year,"),
        ("תָמִים אֶחָד", "צחיחא", "unblemished,"),
        ("לְעֹלָה", "לאלצעידה", "for the burnt-offering;"),
        ("וְכַבְשָׂה", "ורכ'לה", "and a ewe-lamb"),
        ("אַחַת בַּת-שְׁנָתָהּ", "אבנה' סנתהא", "in its first year,"),
        ("תְּמִימָה", "צחיחה", "unblemished,"),
        ("לְחַטָּאת", "לאלדכוה", "for the purification-offering;"),
        ("וְאַיִל-אֶחָד", "וכבשא", "and a ram,"),
        ("תָּמִים", "צחיחא", "unblemished,"),
        ("לִשְׁלָמִים", "לד'בח אלסלאמה", "for the peace-offering."),
    ],
    15: [
        # HE: וְסַל מַצּוֹת סֹלֶת חַלֹּת בְּלוּלֹת בַּשֶּׁמֶן וּרְקִיקֵי מַצּוֹת מְשֻׁחִים בַּשָּׁמֶן וּמִנְחָתָם וְנִסְכֵּיהֶם
        # JA: וסלה' פטיר. גראדק סמד מלתותה בדהן. ורקאק פטיר ממסוחה בדהן. ואלבר ואלמזאג אלד'י מעהא
        # EN: And a basket of unleavened bread — loaves of fine flour kneaded with oil, and wafers of unleavened bread anointed with oil — and the grain-offering and the libation that goes with them.
        ("וְסַל", "וסלה'", "And a basket of"),
        ("מַצּוֹת", "פטיר", "unleavened bread —"),
        ("סֹלֶת", "גראדק סמד", "loaves of fine flour"),
        ("חַלֹּת", "מלתותה", "kneaded"),
        ("בְּלוּלֹת בַּשֶּׁמֶן", "בדהן", "with oil,"),
        ("וּרְקִיקֵי", "ורקאק", "and wafers of"),
        ("מַצּוֹת", "פטיר", "unleavened bread"),
        ("מְשֻׁחִים", "ממסוחה", "anointed"),
        ("בַּשָּׁמֶן", "בדהן", "with oil —"),
        ("וּמִנְחָתָם", "ואלבר", "and the grain-offering"),
        ("וְנִסְכֵּיהֶם", "ואלמזאג אלד'י מעהא", "and the libation that goes with them."),
    ],
    16: [
        # HE: וְהִקְרִיב הַכֹּהֵן לִפְנֵי יְהוָה וְעָשָׂה אֶת-חַטָּאתוֹ וְאֶת-עֹלָתוֹ
        # JA: ויקדמהא אלאמאם בין ידי אללה. ויצנע דכותה וצעידתה
        # EN: And the imām shall present them before God, and shall make his purification-offering and his burnt-offering.
        ("וְהִקְרִיב", "ויקדמהא", "And the imām shall present them"),
        ("הַכֹּהֵן", "אלאמאם", "before God,"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "and shall make"),
        ("וְעָשָׂה", "ויצנע", "his purification-offering"),
        ("אֶת-חַטָּאתוֹ", "דכותה", "and"),
        ("וְאֶת-עֹלָתוֹ", "וצעידתה", "his burnt-offering."),
    ],
    17: [
        # HE: וְאֶת-הָאַיִל יַעֲשֶׂה זֶבַח שְׁלָמִים לַיהוָה עַל סַל הַמַּצּוֹת וְעָשָׂה הַכֹּהֵן אֶת-מִנְחָתוֹ וְאֶת-נִסְכּוֹ
        # JA: ואלכבש. יצנעה ד'בח סלאמה ללה. מע סלה' אלפטיר. ת'ם יצנע אלבר ואלמזאג אלד'י מעה
        # EN: And the ram he shall make a peace-offering to God, together with the basket of unleavened bread; then he shall make the grain-offering and the libation that goes with it.
        ("וְאֶת-הָאַיִל", "ואלכבש", "And the ram"),
        ("יַעֲשֶׂה", "יצנעה", "he shall make"),
        ("זֶבַח שְׁלָמִים", "ד'בח סלאמה", "a peace-offering"),
        ("לַיהוָה", "ללה", "to God,"),
        ("עַל סַל", "מע סלה'", "together with the basket of"),
        ("הַמַּצּוֹת", "אלפטיר", "unleavened bread;"),
        (None, "ת'ם", "then"),
        ("וְעָשָׂה הַכֹּהֵן", "יצנע", "he shall make"),
        ("אֶת-מִנְחָתוֹ", "אלבר", "the grain-offering"),
        ("וְאֶת-נִסְכּוֹ", "ואלמזאג אלד'י מעה", "and the libation that goes with it."),
    ],
    18: [
        # HE: וְגִלַּח הַנָּזִיר פֶּתַח אֹהֶל מוֹעֵד--אֶת-רֹאשׁ נִזְרוֹ וְלָקַח אֶת-שְׂעַר רֹאשׁ נִזְרוֹ וְנָתַן עַל-הָאֵשׁ אֲשֶׁר-תַּחַת זֶבַח הַשְּׁלָמִים
        # JA: ויחלק אלנאסך. ענד באב כ'בא אלמחצ'ר שער ראסה. ויאכ'דה. וילקי עלי' אלנאר. אלד'י תחת ד'בח אלסלאמה
        # EN: And the devotee shall shave the hair of his head at the entrance of the tent of the assembly, and shall take it and cast it upon the fire that is under the peace-offering.
        ("וְגִלַּח", "ויחלק", "And the devotee shall shave"),
        ("הַנָּזִיר", "אלנאסך", "the hair of his head"),
        ("פֶּתַח", "ענד באב", "at the entrance of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly,"),
        ("אֶת-רֹאשׁ נִזְרוֹ", "שער ראסה", "and shall take it"),
        ("וְלָקַח", "ויאכ'דה", "and cast it"),
        ("וְנָתַן", "וילקי", "upon"),
        ("עַל-הָאֵשׁ", "עלי' אלנאר", "the fire"),
        ("אֲשֶׁר-תַּחַת", "אלד'י תחת", "that is under"),
        ("זֶבַח הַשְּׁלָמִים", "ד'בח אלסלאמה", "the peace-offering."),
    ],
    19: [
        # HE: וְלָקַח הַכֹּהֵן אֶת-הַזְּרֹעַ בְּשֵׁלָה מִן-הָאַיִל וְחַלַּת מַצָּה אַחַת מִן-הַסַּל וּרְקִיק מַצָּה אֶחָד וְנָתַן עַל-כַּפֵּי הַנָּזִיר אַחַר הִתְגַּלְּחוֹ אֶת-נִזְרוֹ
        # JA: ויאכ'ד אלאמאם. אלד'ראע מטבוכ'ה מן ד'אלך אלכבש. וגרדקה ואחדה מן אלפטיר. ורקאקה ואחדה. ויצ'ע ד'אלך עלי' כפי אלנאסך. בעד חלקה שער ראסה
        # EN: And the imām shall take the cooked foreleg from that ram, and one loaf from the unleavened bread, and one wafer, and shall place them upon the palms of the devotee after he has shaved the hair of his head.
        ("וְלָקַח", "ויאכ'ד", "And the imām shall take"),
        ("הַכֹּהֵן", "אלאמאם", "the cooked foreleg"),
        ("אֶת-הַזְּרֹעַ", "אלד'ראע", "from"),
        ("בְּשֵׁלָה", "מטבוכ'ה", "that ram,"),
        ("מִן-הָאַיִל", "מן ד'אלך אלכבש", "and one loaf"),
        ("וְחַלַּת מַצָּה", "וגרדקה", "from"),
        ("אַחַת מִן-הַסַּל", "ואחדה מן אלפטיר", "the unleavened bread,"),
        ("וּרְקִיק מַצָּה", "ורקאקה", "and one wafer,"),
        ("אֶחָד", "ואחדה", "and shall place them"),
        ("וְנָתַן", "ויצ'ע", "upon"),
        ("עַל-כַּפֵּי", "ד'אלך עלי' כפי", "the palms of"),
        ("הַנָּזִיר", "אלנאסך", "the devotee"),
        ("אַחַר", "בעד", "after"),
        ("הִתְגַּלְּחוֹ", "חלקה", "he has shaved"),
        ("אֶת-נִזְרוֹ", "שער ראסה", "the hair of his head."),
    ],
    20: [
        # HE: וְהֵנִיף אוֹתָם הַכֹּהֵן תְּנוּפָה לִפְנֵי יְהוָה--קֹדֶשׁ הוּא לַכֹּהֵן עַל חֲזֵה הַתְּנוּפָה וְעַל שׁוֹק הַתְּרוּמָה וְאַחַר יִשְׁתֶּה הַנָּזִיר יָיִן
        # JA: ויחרך אלגמיע תחריכא בין ידי אללה. וליכון מקדסא לאלאמאם. מע קץ אלתחריך. וסאק אלרפיעה. ובעד ד'אלך ישרב אלנאסך כ'מר
        # EN: And he shall wave all of it as a waving before God; and it shall be consecrated for the imām, together with the breast of waving and the thigh of the raised-offering; and after that the devotee may drink wine.
        ("וְהֵנִיף", "ויחרך", "And he shall wave"),
        ("אוֹתָם", "אלגמיע", "all of it"),
        ("הַכֹּהֵן", "תחריכא", "as a waving"),
        ("תְּנוּפָה", "בין ידי", "before"),
        ("לִפְנֵי יְהוָה", "אללה", "God;"),
        (None, "וליכון", "and it shall be"),
        ("קֹדֶשׁ", "מקדסא", "consecrated"),
        ("לַכֹּהֵן", "לאלאמאם", "for the imām,"),
        ("עַל חֲזֵה הַתְּנוּפָה", "מע קץ אלתחריך", "together with the breast of waving"),
        ("וְעַל שׁוֹק הַתְּרוּמָה", "וסאק אלרפיעה", "and the thigh of the raised-offering;"),
        ("וְאַחַר", "ובעד ד'אלך", "and after that"),
        ("יִשְׁתֶּה", "ישרב", "may drink"),
        ("הַנָּזִיר", "אלנאסך", "the devotee"),
        ("יָיִן", "כ'מר", "wine."),
    ],
    21: [
        # HE: זֹאת תּוֹרַת הַנָּזִיר אֲשֶׁר יִדֹּר קָרְבָּנוֹ לַיהוָה עַל-נִזְרוֹ מִלְּבַד אֲשֶׁר-תַּשִּׂיג יָדוֹ כְּפִי נִדְרוֹ אֲשֶׁר יִדֹּר--כֵּן יַעֲשֶׂה עַל תּוֹרַת נִזְרוֹ
        # JA: הד'ה שריעה' אלנאסך. קרבאנה ללה ען נסכה. סוא מא תנאל ידה. וליכון ד'אלך כמקדאר מד'ה נסכה. יצ'מה אלי' שריעה' אלנסך
        # EN: This is the law of the devotee — his offering to God on account of his devotion, apart from what his hand may obtain; and let that be in proportion to the period of his devotion, which he shall add to the law of devotion.
        ("זֹאת", "הד'ה", "This is"),
        ("תּוֹרַת", "שריעה'", "the law of"),
        ("הַנָּזִיר", "אלנאסך", "the devotee —"),
        ("קָרְבָּנוֹ", "קרבאנה", "his offering"),
        ("לַיהוָה", "ללה", "to God"),
        ("עַל-נִזְרוֹ", "ען נסכה", "on account of his devotion,"),
        ("מִלְּבַד", "סוא", "apart from"),
        ("אֲשֶׁר-תַּשִּׂיג יָדוֹ", "מא תנאל ידה", "what his hand may obtain;"),
        (None, "וליכון", "and let"),
        (None, "ד'אלך", "that be"),
        ("כְּפִי נִדְרוֹ", "כמקדאר מד'ה נסכה", "in proportion to the period of his devotion,"),
        ("אֲשֶׁר יִדֹּר", "יצ'מה", "which he shall add"),
        ("כֵּן יַעֲשֶׂה", "אלי'", "to"),
        ("עַל תּוֹרַת נִזְרוֹ", "שריעה' אלנסך", "the law of devotion."),
    ],
    22: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם מוסי' תכלימא
        # EN: Then God spoke to Moses, a speaking.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses,"),
        ("לֵּאמֹר", "תכלימא", "a speaking."),
    ],
    23: [
        # HE: דַּבֵּר אֶל-אַהֲרֹן וְאֶל-בָּנָיו לֵאמֹר כֹּה תְבָרְכוּ אֶת-בְּנֵי יִשְׂרָאֵל אָמוֹר לָהֶם
        # JA: מר הרון ובניה וקל להם. כד'י' פבארכו בני אסראיל. מקוולא להם
        # EN: Command Aaron and his sons and say to them: Thus shall you bless the sons of Israel, reciting to them:
        ("דַּבֵּר", "מר", "Command"),
        ("אֶל-אַהֲרֹן", "הרון", "Aaron"),
        ("וְאֶל-בָּנָיו", "ובניה", "and his sons"),
        ("לֵאמֹר", "וקל להם", "and say to them:"),
        ("כֹּה", "כד'י'", "Thus"),
        ("תְבָרְכוּ", "פבארכו", "shall you bless"),
        ("אֶת-בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel,"),
        ("אָמוֹר", "מקוולא", "reciting"),
        ("לָהֶם", "להם", "to them:"),
    ],
    24: [
        # HE: יְבָרֶכְךָ יְהוָה וְיִשְׁמְרֶךָ
        # JA: יבארכך אללה ויחפצ'ך
        # EN: May God bless you and keep you.
        ("יְבָרֶכְךָ יְהוָה", "יבארכך אללה", "May God bless you"),
        ("וְיִשְׁמְרֶךָ", "ויחפצ'ך", "and keep you."),
    ],
    25: [
        # HE: יָאֵר יְהוָה פָּנָיו אֵלֶיךָ וִיחֻנֶּךָּ
        # JA: ויצ'י וגהה אליך וירופך
        # EN: And may He make His face shine toward you, and show you compassion.
        ("יָאֵר", "ויצ'י", "And may He make"),
        ("פָּנָיו", "וגהה", "His face"),
        ("אֵלֶיךָ", "אליך", "shine toward you,"),
        ("וִיחֻנֶּךָּ", "וירופך", "and show you compassion."),
    ],
    26: [
        # HE: יִשָּׂא יְהוָה פָּנָיו אֵלֶיךָ וְיָשֵׂם לְךָ שָׁלוֹם
        # JA: ויקבל בקצדה אליך. ויצייר לך אלסלאם
        # EN: And may He turn with His purpose toward you, and grant you peace.
        ("יִשָּׂא", "ויקבל", "And may He turn"),
        (None, "בקצדה", "with His purpose"),
        ("פָּנָיו אֵלֶיךָ", "אליך", "toward you,"),
        ("וְיָשֵׂם", "ויצייר", "and grant"),
        ("לְךָ", "לך", "you"),
        ("שָׁלוֹם", "אלסלאם", "peace."),
    ],
    27: [
        # HE: וְשָׂמוּ אֶת-שְׁמִי עַל-בְּנֵי יִשְׂרָאֵל וַאֲנִי אֲבָרְכֵם
        # JA: פליתלו אסמי עלי' בני אסראיל. ואנא אבארך עלי'הם
        # EN: So that they recite My name over the sons of Israel — and I shall bless them.
        ("וְשָׂמוּ", "פליתלו", "So that they recite"),
        ("אֶת-שְׁמִי", "אסמי", "My name"),
        ("עַל-בְּנֵי", "עלי' בני", "over the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel —"),
        ("וַאֲנִי", "ואנא", "and I"),
        ("אֲבָרְכֵם", "אבארך עלי'הם", "shall bless them."),
    ],
}

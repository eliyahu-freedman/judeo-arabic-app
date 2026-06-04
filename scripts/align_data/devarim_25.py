"""Hand-authored alignment triples for Devarim chapter 25.

Word-level: each JA (Saadia) word or short group is mapped to the Hebrew word
it renders and its English counterpart. The runtime resolver matches each side
independently (lib/alignment.ts), so words link correctly even across
word-order crossings. Words Saadia adds with no Hebrew source (glosses,
connectives) carry he=None and link JA↔English only.

This chapter covers: the flogging law (vv. 1–3), muzzling the threshing ox
(v. 4), levirate marriage / yibbum (vv. 5–6), halitzah / sandal-removal
(vv. 7–10), the immodest intervener (vv. 11–12), honest weights and measures
(vv. 13–16), and the command to blot out Amalek (vv. 17–19).
"""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        ("כִּי-יִהְיֶה רִיב", "ואד'א וקעת כ'צומה", "And when a dispute falls"),
        ("בֵּין אֲנָשִׁים", "בין אנאס", "between people"),
        ("וְנִגְּשׁוּ", "פליתקדמו", "they shall come forward"),
        ("אֶל-הַמִּשְׁפָּט", "אלי' ד'וי אלחכם", "to those possessed of judgment"),
        ("וּשְׁפָטוּם", "ויחכמו בינהם", "and they shall judge between them"),
        ("וְהִצְדִּיקוּ אֶת-הַצַּדִּיק", "ויזכו אלזכי", "and they shall vindicate the one in the right"),
        ("וְהִרְשִׁיעוּ אֶת-הָרָשָׁע", "ויצ'למו אלצ'אלם", "and condemn the wrongdoer"),
    ],
    2: [
        ("וְהָיָה אִם-בִּן הַכּוֹת הָרָשָׁע", "ואד'א אסתחק אלצ'אלם צ'רבא", "And if the wrongdoer deserves a flogging"),
        ("וְהִפִּילוֹ הַשֹּׁפֵט", "פליבסטה אלחאכם", "the judge shall lay him down"),
        ("וְהִכָּהוּ לְפָנָיו", "ויצ'רבה בחצ'רתה", "and strike him in his presence"),
        ("כְּדֵי רִשְׁעָתוֹ", "מקדאר כ'טייתה", "according to the measure of his offense"),
        ("בְּמִסְפָּר", "באחצא", "by count"),
    ],
    3: [
        ("אַרְבָּעִים יַכֶּנּוּ", "יגלדה ארבעין", "He shall flog him forty"),
        ("לֹא יֹסִיף", "לא יזיד עליהא שייא", "he shall not add to them anything"),
        ("פֶּן-יֹסִיף לְהַכֹּתוֹ עַל-אֵלֶּה", "פאן זאד עלי' ד'אלך", "For if he adds beyond that"),
        ("מַכָּה רַבָּה", "צארת גלדה ]עט'ימה] עצ'ימה", "the flogging will become a grievous one"),
        ("וְנִקְלָה אָחִיךָ", "ויהון אכ'יך", "and your brother will be degraded"),
        ("לְעֵינֶיךָ", "בחצ'רתך", "in your presence"),
    ],
    4: [
        ("לֹא-תַחְסֹם", "לא תכ'טם", "You shall not muzzle"),
        ("שׁוֹר", "אלת'ור", "the ox"),
        ("בְּדִישׁוֹ", "פי דוסה", "in its threshing"),
    ],
    5: [
        ("כִּי-יֵשְׁבוּ אַחִים יַחְדָּו", "ואד'א אקאם אכ'ואן גמיעא", "And when brothers dwell together"),
        ("וּמֵת אַחַד מֵהֶם", "ת'ם מאת אחדהמא", "and one of them dies"),
        ("וּבֵן אֵין-לוֹ", "וליס לה ולד", "and he has no child"),
        ("לֹא-תִהְיֶה אֵשֶׁת-הַמֵּת", "פלא תכון זוגה' אלמיית", "the wife of the deceased shall not become"),
        ("לְאִישׁ זָר", "לרגל ג'ריב", "a stranger's"),
        ("הַחוּצָה", "כ'ארג ען אלאכ'וה", "outside the brotherhood"),
        ("יְבָמָהּ יָבֹא עָלֶיהָ", "בל סליפהא ידכל אליהא", "rather, her brother-in-law shall come in to her"),
        ("וּלְקָחָהּ לוֹ לְאִשָּׁה", "באן יתכ'ד'הא לה זוגה", "by taking her to himself as a wife"),
        ("וְיִבְּמָהּ", "ויבן בהא", "and building a home with her"),
    ],
    6: [
        ("וְהָיָה הַבְּכוֹר", "וליכון אלבכר", "And the firstborn"),
        ("אֲשֶׁר תֵּלֵד", "אלד'י ירגא אן תלד מנה", "whom it is hoped she will bear from him"),
        ("יָקוּם עַל-שֵׁם אָחִיו הַמֵּת", "יקום עלי' אסם אכ'יה אלמיית", "shall stand in the name of his dead brother"),
        ("וְלֹא-יִמָּחֶה שְׁמוֹ", "ללא ינדרס אסמה", "so that his name not be blotted out"),
        ("מִיִּשְׂרָאֵל", "מן אל אסראיל", "from the house of Israel"),
    ],
    7: [
        ("וְאִם-לֹא יַחְפֹּץ הָאִישׁ", "פאן לם ישא ד'אלך אלרגל", "And if that man does not wish"),
        ("לָקַחַת אֶת-יְבִמְתּוֹ", "אן יתזווג סליפתה", "to marry his sister-in-law"),
        ("וְעָלְתָה יְבִמְתּוֹ", "פלתצעד", "she shall go up"),
        ("הַשַּׁעְרָה", "אלי' באב אלחאכם", "to the gate of the judge"),
        ("אֶל-הַזְּקֵנִים", "ואלי' אלשיוך'", "and to the elders"),
        ("וְאָמְרָה", "ותקול", "and shall say"),
        ("מֵאֵן יְבָמִי", "קד אבא סליפי", "My brother-in-law has refused"),
        ("לְהָקִים לְאָחִיו שֵׁם בְּיִשְׂרָאֵל", "אן יקים לאכ'יה אסמא פי מא בין בני אסראיל", "to establish a name for his brother among the sons of Israel"),
        ("לֹא אָבָה יַבְּמִי", "ולם ישא אן יבן בי", "and he has not wished to build a home with me"),
    ],
    8: [
        ("וְקָרְאוּ-לוֹ זִקְנֵי-עִירוֹ", "פידעו בה שיוך' קריתה", "The elders of his town shall call for him"),
        ("וְדִבְּרוּ אֵלָיו", "ויכלמוה בד'אלך", "and speak with him about that"),
        ("וְעָמַד", "פאד'א וקף עלי' אלקול", "and if he stands firm in his word"),
        ("וְאָמַר", "וקאל", "and says"),
        ("לֹא חָפַצְתִּי לְקַחְתָּהּ", "אני לא אריד אלתזווג בהא", "I do not wish to marry her"),
    ],
    9: [
        ("וְנִגְּשָׁה יְבִמְתּוֹ אֵלָיו", "ותקדמת אליה", "his sister-in-law shall come forward to him"),
        ("לְעֵינֵי הַזְּקֵנִים", "בחצ'רה' אלשיוך'", "in the presence of the elders"),
        ("וְחָלְצָה נַעֲלוֹ מֵעַל רַגְלוֹ", "וכלעת נעלה ען רגלה", "and remove his sandal from his foot"),
        ("וְיָרְקָה בְּפָנָיו", "ובצקת בחצ'רתה", "and spit in his presence"),
        ("וְעָנְתָה וְאָמְרָה", "ואגאבת וקאלת", "and she shall answer and say"),
        ("כָּכָה יֵעָשֶׂה לָאִישׁ", "כד'א יצנע באלרגל", "Thus shall be done to the man"),
        ("אֲשֶׁר לֹא-יִבְנֶה אֶת-בֵּית אָחִיו", "אלד'י לא יבני בית אכ'יה", "who does not build his brother's house"),
    ],
    10: [
        ("וְנִקְרָא שְׁמוֹ", "וליסם אסמה", "And his name shall be called"),
        ("בְּיִשְׂרָאֵל", "פי אל אסראיל", "in the house of Israel"),
        ("בֵּית חֲלוּץ הַנָּעַל", "בית מכלוע אלנעל", "The house of the one whose sandal was removed"),
    ],
    11: [
        ("כִּי-יִנָּצוּ אֲנָשִׁים יַחְדָּו", "ואן תנאציאן רגלאן גמיעא", "And if two men strive together"),
        ("אִישׁ וְאָחִיו", "פג'לב אחדה'מא צאחבה", "and one of them overpowers the other"),
        ("וְקָרְבָה אֵשֶׁת הָאֶחָד לְהַצִּיל אֶת-אִישָׁהּ", "פתקדמת זוגתה לתכ'לצה", "and his wife comes forward to rescue him"),
        ("מִיַּד מַכֵּהוּ", "מן ידה", "from the other's hand"),
        ("וְשָׁלְחָה יָדָהּ", "פמדת ידהא", "and she stretches out her hand"),
        ("וְהֶחֱזִיקָה בִּמְבֻשָׁיו", "ואמסכת חיאה", "and seizes his private parts"),
    ],
    12: [
        ("וְקַצֹּתָה אֶת-כַּפָּהּ", "פאקטע ידהא", "you shall cut off her hand"),
        ("לֹא תָחוֹס עֵינֶךָ", "לתכ'לצה מנהא. ולא תשפק עליהא", "to free him from her, and you shall not show pity for her"),
    ],
    13: [
        ("לֹא-יִהְיֶה לְךָ", "ולא יכון לך", "You shall not have"),
        ("בְּכִיסְךָ", "פי כיסך", "in your pouch"),
        ("אֶבֶן וָאָבֶן", "צנגתאן", "two weights"),
        ("גְּדוֹלָה", "כברא", "a large"),
        ("וּקְטַנָּה", "וצג'רא", "and a small"),
    ],
    14: [
        ("לֹא-יִהְיֶה לְךָ", "ולא יכון לך", "And you shall not have"),
        ("בְּבֵיתְךָ", "פי ביתך", "in your house"),
        ("אֵיפָה וְאֵיפָה", "מכיאלין", "two measures"),
        ("גְּדוֹלָה", "כביר", "a large"),
        ("וּקְטַנָּה", "וצג'יר", "and a small"),
    ],
    15: [
        (None, "בל", "Rather"),
        ("אֶבֶן שְׁלֵמָה וָצֶדֶק", "צנגאת ואפיה עאדלאת", "full and just weights"),
        ("יִהְיֶה-לָּךְ", "תכון לך", "shall you have"),
        ("אֵיפָה שְׁלֵמָה וָצֶדֶק", "ואכיאל ואפיה עאדלאת", "and full and just measures"),
        ("יִהְיֶה-לָּךְ", "תכון לך", "shall you have"),
        ("לְמַעַן יַאֲרִיכוּ יָמֶיךָ", "לכי תטול מדתך", "so that your span of days may be long"),
        ("עַל הָאֲדָמָה", "פי אלבלד", "in the land"),
        ("אֲשֶׁר-יְהוָה אֱלֹהֶיךָ נֹתֵן לָךְ", "אלד'י אללה רבך מעטיך", "which the Lord your God is giving you"),
    ],
    16: [
        ("כִּי תוֹעֲבַת יְהוָה אֱלֹהֶיךָ", "לאן אללה רבך יכרה", "For the Lord your God loathes"),
        ("כָּל-עֹשֵׂה אֵלֶּה", "כל מן יעמל הד'א", "everyone who does this"),
        ("כֹּל עֹשֵׂה עָוֶל", "כל מן יעמל בג'ש", "everyone who acts with fraud"),
    ],
    17: [
        ("זָכוֹר", "ואד'כ'ר", "And remember"),
        ("אֵת אֲשֶׁר-עָשָׂה לְךָ עֲמָלֵק", "מא צנע בך עמלק", "what Amalek did to you"),
        ("בַּדֶּרֶךְ", "פי אלטריק", "on the road"),
        ("בְּצֵאתְכֶם מִמִּצְרָיִם", "פי כ'רוגכם מן מצר", "when you were coming out of Egypt"),
    ],
    18: [
        ("אֲשֶׁר קָרְךָ בַּדֶּרֶךְ", "אנה ואפאך פי אלטריק", "that he came upon you on the road"),
        ("וַיְזַנֵּב בְּךָ", "פתטרף מנך", "and cut off from you"),
        ("כָּל-הַנֶּחֱשָׁלִים אַחֲרֶיךָ", "גמיע אלמנזחפין וראך", "all the stragglers behind you"),
        ("וְאַתָּה עָיֵף", "ואנת לג'ב", "while you were weary"),
        ("וְיָגֵעַ", "ותעב", "and exhausted"),
        ("וְלֹא יָרֵא אֱלֹהִים", "ולם יכ'אף אללה", "and he did not fear God"),
    ],
    19: [
        ("וְהָיָה בְּהָנִיחַ יְהוָה אֱלֹהֶיךָ לְךָ", "פאד'א אראחך אללה רבך", "And when the Lord your God gives you rest"),
        ("מִכָּל-אֹיְבֶיךָ מִסָּבִיב", "מן גמיע אעדאך אלד'ין חואליך", "from all your enemies round about you"),
        ("בָּאָרֶץ", "פי אלבלד", "in the land"),
        ("אֲשֶׁר יְהוָה-אֱלֹהֶיךָ נֹתֵן לְךָ", "אלד'י אללה רבך", "which the Lord your God"),
        ("נַחֲלָה לְרִשְׁתָּהּ", "מעטיך נחלה לתחוזה", "is giving you as an inheritance to possess it"),
        ("תִּמְחֶה אֶת-זֵכֶר עֲמָלֵק", "פאמח ד'כר עמלק", "you shall blot out the memory of Amalek"),
        ("מִתַּחַת הַשָּׁמָיִם", "מן תחת אלסמא", "from beneath the sky"),
        ("לֹא תִּשְׁכָּח", "לא תנס ד'אלך", "Do not forget that"),
    ],
}

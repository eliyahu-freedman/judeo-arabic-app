"""Hand-authored word-level alignment triples for Bamidbar chapter 10."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses directly.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "God spoke"),
        ("יְהוָה", "אללה", "to"),
        ("אֶל-מֹשֶׁה", "מוסי'", "Moses"),
        ("לֵּאמֹר", "תכלימא", "directly."),
    ],
    2: [
        # HE: עֲשֵׂה לְךָ שְׁתֵּי חֲצוֹצְרֹת כֶּסֶף--מִקְשָׁה תַּעֲשֶׂה אֹתָם וְהָיוּ לְךָ לְמִקְרָא הָעֵדָה וּלְמַסַּע אֶת-הַמַּחֲנוֹת
        # JA: אצנע לך בוקין מן פצה מצמתה. יכונאן לך לדעוה' אלגמאעה ותרחיל אלעסאכר
        # EN: 'Make for yourself two trumpets of solid silver; they shall be for you for summoning the assembly and for setting out the camp.'
        ("עֲשֵׂה", "אצנע", "'Make"),
        ("לְךָ", "לך", "for yourself"),
        ("שְׁתֵּי חֲצוֹצְרֹת", "בוקין", "two trumpets"),
        ("כֶּסֶף", "מן פצה", "of solid"),
        ("מִקְשָׁה תַּעֲשֶׂה אֹתָם", "מצמתה", "silver;"),
        ("וְהָיוּ", "יכונאן", "they shall be"),
        ("לְךָ", "לך", "for you"),
        ("לְמִקְרָא", "לדעוה'", "for summoning"),
        ("הָעֵדָה", "אלגמאעה", "the assembly"),
        ("וּלְמַסַּע", "ותרחיל", "and for setting out"),
        ("אֶת-הַמַּחֲנוֹת", "אלעסאכר", "the camp.'"),
    ],
    3: [
        # HE: וְתָקְעוּ בָּהֵן--וְנוֹעֲדוּ אֵלֶיךָ כָּל-הָעֵדָה אֶל-פֶּתַח אֹהֶל מוֹעֵד
        # JA: פאן צרב בהמא. אגתמע אליך כל אלגמאעה. אלי' באב כ'בא אלמחצ'ר
        # EN: 'And if both are sounded, all the assembly shall gather to you, at the entrance of the tent of the assembly.'
        ("וְתָקְעוּ", "פאן צרב", "'And if"),
        ("בָּהֵן", "בהמא", "both are sounded,"),
        ("וְנוֹעֲדוּ", "אגתמע", "shall gather"),
        ("אֵלֶיךָ", "אליך", "to you,"),
        ("כָּל-הָעֵדָה", "כל אלגמאעה", "all the assembly"),
        ("אֶל-פֶּתַח", "אלי' באב", "at the entrance of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly.'"),
    ],
    4: [
        # HE: וְאִם-בְּאַחַת יִתְקָעוּ--וְנוֹעֲדוּ אֵלֶיךָ הַנְּשִׂיאִים רָאשֵׁי אַלְפֵי יִשְׂרָאֵל
        # JA: ואן צרב באחדהמא אגתמע אליך אלאשראף. רויסא אלוף בני אסראיל
        # EN: 'And if one of them is sounded, the nobles shall gather to you — the heads of the thousands of the sons of Israel.'
        ("וְאִם-בְּאַחַת", "ואן צרב", "'And if"),
        ("יִתְקָעוּ", "באחדהמא", "one of them is sounded,"),
        ("וְנוֹעֲדוּ", "אגתמע", "shall gather"),
        ("אֵלֶיךָ", "אליך", "to you —"),
        ("הַנְּשִׂיאִים", "אלאשראף", "the nobles"),
        ("רָאשֵׁי אַלְפֵי", "רויסא אלוף", "the heads of the thousands of"),
        ("יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel.'"),
    ],
    5: [
        # HE: וּתְקַעְתֶּם תְּרוּעָה--וְנָסְעוּ הַמַּחֲנוֹת הַחֹנִים קֵדְמָה
        # JA: ואנפכ'ו נפכ'א מגלבא. ירחל בהא אלעסאכר. אלנאזלין פי אלמשרק
        # EN: 'And blow a rousing blast, and the camp encamped in the east shall set out by it.'
        ("וּתְקַעְתֶּם", "ואנפכ'ו", "'And blow"),
        ("תְּרוּעָה", "נפכ'א", "a rousing"),
        (None, "מגלבא", "blast,"),
        ("וְנָסְעוּ", "ירחל", "shall set out"),
        ("הַמַּחֲנוֹת", "בהא אלעסאכר", "and the camp"),
        ("הַחֹנִים", "אלנאזלין", "encamped"),
        ("קֵדְמָה", "פי אלמשרק", "in the east"),
    ],
    6: [
        # HE: וּתְקַעְתֶּם תְּרוּעָה שֵׁנִית--וְנָסְעוּ הַמַּחֲנוֹת הַחֹנִים תֵּימָנָה תְּרוּעָה יִתְקְעוּ לְמַסְעֵיהֶם
        # JA: ואנפכ'ו נפכ'א מגלבא ת'אניא. ירחל בהא אלעסאכר. אלנאזלין פי אלגנוב. כד'אך ינפכ'ו נפכ'א לרחילהם
        # EN: 'And blow a rousing blast a second time, and the camp encamped in the south shall set out by it; thus shall they blow a blast for their setting out.'
        ("וּתְקַעְתֶּם", "ואנפכ'ו", "'And blow"),
        ("תְּרוּעָה", "נפכ'א", "a rousing"),
        (None, "מגלבא", "blast"),
        ("שֵׁנִית", "ת'אניא", "a second time,"),
        ("וְנָסְעוּ", "ירחל", "shall set out"),
        ("הַמַּחֲנוֹת", "בהא אלעסאכר", "and the camp"),
        ("הַחֹנִים", "אלנאזלין", "encamped"),
        ("תֵּימָנָה", "פי אלגנוב", "in the south"),
        (None, "כד'אך", "thus"),
        ("תְּרוּעָה יִתְקְעוּ", "ינפכ'ו נפכ'א", "shall they blow a blast"),
        ("לְמַסְעֵיהֶם", "לרחילהם", "for their setting out.'"),
    ],
    7: [
        # HE: וּבְהַקְהִיל אֶת-הַקָּהָל--תִּתְקְעוּ וְלֹא תָרִיעוּ
        # JA: ופי תגויק אלגוק. אנפכ'ו נפכ'א ולא תגלבו
        # EN: 'And when the congregation assembles, blow a steady blast and do not rouse.'
        ("וּבְהַקְהִיל", "ופי תגויק", "'And when the congregation"),
        ("אֶת-הַקָּהָל", "אלגוק", "assembles,"),
        ("תִּתְקְעוּ", "אנפכ'ו נפכ'א", "blow a steady blast"),
        ("וְלֹא תָרִיעוּ", "ולא תגלבו", "and do not rouse.'"),
    ],
    8: [
        # HE: וּבְנֵי אַהֲרֹן הַכֹּהֲנִים יִתְקְעוּ בַּחֲצֹצְרוֹת וְהָיוּ לָכֶם לְחֻקַּת עוֹלָם לְדֹרֹתֵיכֶם
        # JA: ובני הרון אלאימה. יצ'רבו באלאבואק. ויכון לכם ד'אלך. רסם אלדהר לאגיאלכם
        # EN: 'And the sons of Aaron, the imāms, shall sound the trumpets; and that shall be for you an ordinance forever throughout your generations.'
        ("וּבְנֵי", "ובני", "'And the sons of"),
        ("אַהֲרֹן", "הרון", "Aaron,"),
        ("הַכֹּהֲנִים", "אלאימה", "the imāms,"),
        ("יִתְקְעוּ", "יצ'רבו", "shall sound"),
        ("בַּחֲצֹצְרוֹת", "באלאבואק", "the trumpets;"),
        ("וְהָיוּ", "ויכון", "and that shall be"),
        ("לָכֶם", "לכם", "for you"),
        (None, "ד'אלך", "an ordinance"),
        ("לְחֻקַּת עוֹלָם", "רסם אלדהר", "forever"),
        ("לְדֹרֹתֵיכֶם", "לאגיאלכם", "throughout your generations.'"),
    ],
    9: [
        # HE: וְכִי-תָבֹאוּ מִלְחָמָה בְּאַרְצְכֶם עַל-הַצַּר הַצֹּרֵר אֶתְכֶם--וַהֲרֵעֹתֶם בַּחֲצֹצְרֹת וְנִזְכַּרְתֶּם לִפְנֵי יְהוָה אֱלֹהֵיכֶם וְנוֹשַׁעְתֶּם מֵאֹיְבֵיכֶם
        # JA: ואד'א צרתם אלי' חרב פי בלדכם. מע אלעדו אלמעאדיכם. פגלבו באלאבואק. פאד'א בווקתם בין ידי אללה רבכם. תג'אתון מן אעדאיכם
        # EN: 'And when you go to war in your land against the enemy who opposes you, sound a rousing blast on the trumpets; and when you trumpet before God your Lord, you shall be aided against your enemies.'
        ("וְכִי-תָבֹאוּ", "ואד'א צרתם", "'And when you go"),
        ("מִלְחָמָה", "אלי' חרב", "to war"),
        ("בְּאַרְצְכֶם", "פי בלדכם", "in your land"),
        ("עַל-הַצַּר הַצֹּרֵר", "מע אלעדו", "against the enemy"),
        ("אֶתְכֶם", "אלמעאדיכם", "who opposes you,"),
        ("וַהֲרֵעֹתֶם", "פגלבו", "sound a rousing blast"),
        ("בַּחֲצֹצְרֹת", "באלאבואק", "on the trumpets;"),
        ("וְנִזְכַּרְתֶּם", "פאד'א בווקתם", "and when you trumpet"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God"),
        ("אֱלֹהֵיכֶם", "רבכם", "your Lord,"),
        ("וְנוֹשַׁעְתֶּם", "תג'אתון", "you shall be aided"),
        ("מֵאֹיְבֵיכֶם", "מן אעדאיכם", "against your enemies.'"),
    ],
    10: [
        # HE: וּבְיוֹם שִׂמְחַתְכֶם וּבְמוֹעֲדֵיכֶם וּבְרָאשֵׁי חָדְשֵׁיכֶם--וּתְקַעְתֶּם בַּחֲצֹצְרֹת עַל עֹלֹתֵיכֶם וְעַל זִבְחֵי שַׁלְמֵיכֶם וְהָיוּ לָכֶם לְזִכָּרוֹן לִפְנֵי אֱלֹהֵיכֶם אֲנִי יְהוָה אֱלֹהֵיכֶם
        # JA: ופי יום פרחכם ואעיאדכם ורוס שהורכם. פאצ'רבו באלאבואק. עלי' צואעדכם. ודבאיח סלאמתכם. פתכון לכם ד'כרא בין ידי רבכם. אנא אללה רבכם אמרת בד'אלך
        # EN: 'And on the day of your rejoicing, and at your festivals, and at your new months, sound the trumpets over your ascent-offerings and your peace-offerings; and it shall be a remembrance for you before God your Lord. I am God your Lord — I have commanded this.'
        ("וּבְיוֹם", "ופי יום", "'And on the day of"),
        ("שִׂמְחַתְכֶם", "פרחכם", "your rejoicing,"),
        ("וּבְמוֹעֲדֵיכֶם", "ואעיאדכם", "and at your festivals,"),
        ("וּבְרָאשֵׁי חָדְשֵׁיכֶם", "ורוס שהורכם", "and at your new months,"),
        ("וּתְקַעְתֶּם", "פאצ'רבו", "sound"),
        ("בַּחֲצֹצְרֹת", "באלאבואק", "the trumpets"),
        ("עַל עֹלֹתֵיכֶם", "עלי' צואעדכם", "over your ascent-offerings"),
        ("וְעַל זִבְחֵי שַׁלְמֵיכֶם", "ודבאיח סלאמתכם", "and your peace-offerings;"),
        ("וְהָיוּ לָכֶם", "פתכון לכם", "and it shall be"),
        ("לְזִכָּרוֹן", "ד'כרא", "a remembrance"),
        ("לִפְנֵי אֱלֹהֵיכֶם", "בין ידי רבכם", "for you before God your Lord."),
        ("אֲנִי יְהוָה", "אנא אללה", "I am God"),
        ("אֱלֹהֵיכֶם", "רבכם", "your Lord —"),
        (None, "אמרת בד'אלך", "I have commanded this.'"),
    ],
    11: [
        # HE: וַיְהִי בַּשָּׁנָה הַשֵּׁנִית בַּחֹדֶשׁ הַשֵּׁנִי--בְּעֶשְׂרִים בַּחֹדֶשׁ נַעֲלָה הֶעָנָן מֵעַל מִשְׁכַּן הָעֵדֻת
        # JA: פלמא כאן פי אלשהר אלת'אני. מן אלסנה אלת'אניה פי עשרין מנה. ארתפע אלג'מאם. ען מסכן אלשהאדה
        # EN: And it was in the second month of the second year, on the twentieth of it, that the cloud rose from the tabernacle of the testimony.
        ("וַיְהִי", "פלמא כאן", "And it was"),
        ("בַּחֹדֶשׁ הַשֵּׁנִי", "פי אלשהר אלת'אני", "in the second month"),
        ("בַּשָּׁנָה הַשֵּׁנִית", "מן אלסנה אלת'אניה", "of the second year,"),
        ("בְּעֶשְׂרִים בַּחֹדֶשׁ", "פי עשרין מנה", "on the twentieth of it,"),
        ("נַעֲלָה", "ארתפע", "that"),
        ("הֶעָנָן", "אלג'מאם", "the cloud rose"),
        ("מֵעַל", "ען", "from"),
        ("מִשְׁכַּן הָעֵדֻת", "מסכן אלשהאדה", "the tabernacle of the testimony."),
    ],
    12: [
        # HE: וַיִּסְעוּ בְנֵי-יִשְׂרָאֵל לְמַסְעֵיהֶם מִמִּדְבַּר סִינָי וַיִּשְׁכֹּן הֶעָנָן בְּמִדְבַּר פָּארָן
        # JA: פרחל בני אסראיל עלי' מראחלהם מן ברייה' סיני. פסכן אלג'מאם פי ברייה' פארן
        # EN: And the sons of Israel set out on their journeys from the wilderness of Sinai, and the cloud settled in the wilderness of Paran.
        ("וַיִּסְעוּ", "פרחל", "And"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel set out"),
        ("לְמַסְעֵיהֶם", "עלי' מראחלהם", "on their journeys"),
        ("מִמִּדְבַּר", "מן ברייה'", "from the wilderness of"),
        ("סִינָי", "סיני", "Sinai,"),
        ("וַיִּשְׁכֹּן", "פסכן", "and"),
        ("הֶעָנָן", "אלג'מאם", "the cloud settled"),
        ("בְּמִדְבַּר", "פי ברייה'", "in the wilderness of"),
        ("פָּארָן", "פארן", "Paran."),
    ],
    13: [
        # HE: וַיִּסְעוּ בָּרִאשֹׁנָה עַל-פִּי יְהוָה בְּיַד-מֹשֶׁה
        # JA: פכאן אוול רחילהם. עלי' קול אללה ביד מוסי'
        # EN: And the first of their setting out was by the command of God, by the hand of Moses.
        ("וַיִּסְעוּ", "פכאן", "And the first"),
        ("בָּרִאשֹׁנָה", "אוול רחילהם", "of their setting out"),
        ("עַל-פִּי יְהוָה", "עלי' קול אללה", "was by the command of God,"),
        ("בְּיַד-מֹשֶׁה", "ביד מוסי'", "by the hand of Moses."),
    ],
    14: [
        # HE: וַיִּסַּע דֶּגֶל מַחֲנֵה בְנֵי-יְהוּדָה בָּרִאשֹׁנָה--לְצִבְאֹתָם וְעַל-צְבָאוֹ--נַחְשׁוֹן בֶּן-עַמִּינָדָב
        # JA: באן רחל מרכז עסכר בני יהודה. עלי' אלמקדמה לגיושהם. ועלי' גישה נחשון אבן עמינדב
        # EN: Then the division of the camp of the sons of Judah set out at the head, by their hosts; and over his host was Nahshon son of Amminadab.
        ("וַיִּסַּע", "באן רחל", "Then"),
        ("דֶּגֶל מַחֲנֵה", "מרכז עסכר", "the division of the camp of"),
        ("בְנֵי-יְהוּדָה", "בני יהודה", "the sons of Judah set out"),
        ("בָּרִאשֹׁנָה", "עלי' אלמקדמה", "at the head,"),
        ("לְצִבְאֹתָם", "לגיושהם", "by their hosts;"),
        ("וְעַל-צְבָאוֹ", "ועלי' גישה", "and over his host"),
        ("נַחְשׁוֹן", "נחשון", "was Nahshon"),
        ("בֶּן-עַמִּינָדָב", "אבן עמינדב", "son of Amminadab."),
    ],
    15: [
        # HE: וְעַל-צְבָא--מַטֵּה בְּנֵי יִשָּׂשכָר נְתַנְאֵל בֶּן-צוּעָר
        # JA: ועלי' גיש סבט יששכר. נתנאל אבן צוער
        # EN: And over the host of the tribe of Issachar was Nethanel son of Zuar.
        ("וְעַל-צְבָא", "ועלי' גיש", "And over the host of"),
        ("מַטֵּה בְּנֵי יִשָּׂשכָר", "סבט יששכר", "the tribe of Issachar"),
        ("נְתַנְאֵל", "נתנאל", "was Nethanel"),
        ("בֶּן-צוּעָר", "אבן צוער", "son of Zuar."),
    ],
    16: [
        # HE: וְעַל-צְבָא--מַטֵּה בְּנֵי זְבוּלֻן אֱלִיאָב בֶּן-חֵלֹן
        # JA: ועלי' גיש סבט זבולון. אליאב אבן חלון
        # EN: And over the host of the tribe of Zebulun was Eliab son of Helon.
        ("וְעַל-צְבָא", "ועלי' גיש", "And over the host of"),
        ("מַטֵּה בְּנֵי זְבוּלֻן", "סבט זבולון", "the tribe of Zebulun"),
        ("אֱלִיאָב", "אליאב", "was Eliab"),
        ("בֶּן-חֵלֹן", "אבן חלון", "son of Helon."),
    ],
    17: [
        # HE: וְהוּרַד הַמִּשְׁכָּן וְנָסְעוּ בְנֵי-גֵרְשׁוֹן וּבְנֵי מְרָרִי נֹשְׂאֵי הַמִּשְׁכָּן
        # JA: ת'ם פצל אלמסכן. פרחל בני גרשון ובני מררי. חאמלוה
        # EN: Then the tabernacle was taken apart, and the sons of Gershon and the sons of Merari set out, carrying it.
        (None, "ת'ם", "Then"),
        ("וְהוּרַד הַמִּשְׁכָּן", "פצל אלמסכן", "the tabernacle was taken apart,"),
        ("וְנָסְעוּ", "פרחל", "and"),
        ("בְנֵי-גֵרְשׁוֹן", "בני גרשון", "the sons of Gershon"),
        ("וּבְנֵי מְרָרִי", "ובני מררי", "and the sons of Merari set out,"),
        ("נֹשְׂאֵי הַמִּשְׁכָּן", "חאמלוה", "carrying it."),
    ],
    18: [
        # HE: וְנָסַע דֶּגֶל מַחֲנֵה רְאוּבֵן--לְצִבְאֹתָם וְעַל-צְבָאוֹ--אֱלִיצוּר בֶּן-שְׁדֵיאוּר
        # JA: ת'ם רחל מרכז עסכר ראובן לגיושהם. ועלי' גישה. אליצור אבן שדאור
        # EN: Then the division of the camp of Reuben set out by their hosts; and over his host was Elizur son of Shedeur.
        (None, "ת'ם", "Then"),
        ("וְנָסַע", "רחל", "the division"),
        ("דֶּגֶל מַחֲנֵה", "מרכז עסכר", "of the camp of"),
        ("רְאוּבֵן", "ראובן", "Reuben set out"),
        ("לְצִבְאֹתָם", "לגיושהם", "by their hosts;"),
        ("וְעַל-צְבָאוֹ", "ועלי' גישה", "and over his host"),
        ("אֱלִיצוּר", "אליצור", "was Elizur"),
        ("בֶּן-שְׁדֵיאוּר", "אבן שדאור", "son of Shedeur."),
    ],
    19: [
        # HE: וְעַל-צְבָא--מַטֵּה בְּנֵי שִׁמְעוֹן שְׁלֻמִיאֵל בֶּן-צוּרִישַׁדָּי
        # JA: ועלי' גיש סבט שמעון. שלומיאל אבן צורישדי
        # EN: And over the host of the tribe of Simeon was Shelumiel son of Zurishaddai.
        ("וְעַל-צְבָא", "ועלי' גיש", "And over the host of"),
        ("מַטֵּה בְּנֵי שִׁמְעוֹן", "סבט שמעון", "the tribe of Simeon"),
        ("שְׁלֻמִיאֵל", "שלומיאל", "was Shelumiel"),
        ("בֶּן-צוּרִישַׁדָּי", "אבן צורישדי", "son of Zurishaddai."),
    ],
    20: [
        # HE: וְעַל-צְבָא מַטֵּה בְנֵי-גָד אֶלְיָסָף בֶּן-דְּעוּאֵל
        # JA: ועלי' גיש סבט גד. אליסף אבן דעואל
        # EN: And over the host of the tribe of Gad was Eliasaph son of Deuel.
        ("וְעַל-צְבָא", "ועלי' גיש", "And over the host of"),
        ("מַטֵּה בְנֵי-גָד", "סבט גד", "the tribe of Gad"),
        ("אֶלְיָסָף", "אליסף", "was Eliasaph"),
        ("בֶּן-דְּעוּאֵל", "אבן דעואל", "son of Deuel."),
    ],
    21: [
        # HE: וְנָסְעוּ הַקְּהָתִים נֹשְׂאֵי הַמִּקְדָּשׁ וְהֵקִימוּ אֶת-הַמִּשְׁכָּן עַד-בֹּאָם
        # JA: ת'ם רחל אלקהתיין. חאמלי אלמקדס. וקד נצב אלמסכן אלי' מגייהם
        # EN: Then the Kohathites set out, carrying the sanctuary; and the tabernacle was erected before their arrival.
        (None, "ת'ם", "Then"),
        ("וְנָסְעוּ", "רחל", "set out,"),
        ("הַקְּהָתִים", "אלקהתיין", "the Kohathites"),
        ("נֹשְׂאֵי הַמִּקְדָּשׁ", "חאמלי אלמקדס", "carrying the sanctuary;"),
        ("וְהֵקִימוּ אֶת-הַמִּשְׁכָּן", "וקד נצב אלמסכן", "and the tabernacle was erected"),
        ("עַד-בֹּאָם", "אלי' מגייהם", "before their arrival."),
    ],
    22: [
        # HE: וְנָסַע דֶּגֶל מַחֲנֵה בְנֵי-אֶפְרַיִם--לְצִבְאֹתָם וְעַל-צְבָאוֹ--אֱלִישָׁמָע בֶּן-עַמִּיהוּד
        # JA: ת'ם רחל מרכז עסכר אפרים לגיושהם. ועלי' גישה. אלישמע אבן עמיהוד
        # EN: Then the division of the camp of Ephraim set out by their hosts; and over his host was Elishama son of Ammihud.
        (None, "ת'ם", "Then"),
        ("וְנָסַע", "רחל", "the division"),
        ("דֶּגֶל מַחֲנֵה", "מרכז עסכר", "of the camp of"),
        ("בְנֵי-אֶפְרַיִם", "אפרים", "Ephraim set out"),
        ("לְצִבְאֹתָם", "לגיושהם", "by their hosts;"),
        ("וְעַל-צְבָאוֹ", "ועלי' גישה", "and over his host"),
        ("אֱלִישָׁמָע", "אלישמע", "was Elishama"),
        ("בֶּן-עַמִּיהוּד", "אבן עמיהוד", "son of Ammihud."),
    ],
    23: [
        # HE: וְעַל-צְבָא--מַטֵּה בְּנֵי מְנַשֶּׁה גַּמְלִיאֵל בֶּן-פְּדָהצוּר
        # JA: ועלי' גיש סבט מנשה. גמליאל אבן פדהצור
        # EN: And over the host of the tribe of Manasseh was Gamliel son of Pedahzur.
        ("וְעַל-צְבָא", "ועלי' גיש", "And over the host of"),
        ("מַטֵּה בְּנֵי מְנַשֶּׁה", "סבט מנשה", "the tribe of Manasseh"),
        ("גַּמְלִיאֵל", "גמליאל", "was Gamliel"),
        ("בֶּן-פְּדָהצוּר", "אבן פדהצור", "son of Pedahzur."),
    ],
    24: [
        # HE: וְעַל-צְבָא--מַטֵּה בְּנֵי בִנְיָמִן אֲבִידָן בֶּן-גִּדְעוֹנִי
        # JA: ועלי' גיש סבט בנימן. אבידן אבן גדעוני
        # EN: And over the host of the tribe of Benjamin was Abidan son of Gideoni.
        ("וְעַל-צְבָא", "ועלי' גיש", "And over the host of"),
        ("מַטֵּה בְּנֵי בִנְיָמִן", "סבט בנימן", "the tribe of Benjamin"),
        ("אֲבִידָן", "אבידן", "was Abidan"),
        ("בֶּן-גִּדְעוֹנִי", "אבן גדעוני", "son of Gideoni."),
    ],
    25: [
        # HE: וְנָסַע דֶּגֶל מַחֲנֵה בְנֵי-דָן--מְאַסֵּף לְכָל-הַמַּחֲנֹת לְצִבְאֹתָם וְעַל-צְבָאוֹ--אֲחִיעֶזֶר בֶּן-עַמִּישַׁדָּי
        # JA: ת'ם רחל מרכז עסכר בני דן. עלי' סאקה' סאיר אלעסאכר לגיושהם. ועלי' גישה. אחיעזר אבן עמישדי
        # EN: Then the division of the camp of the sons of Dan set out, at the rear of all the camp, by their hosts; and over his host was Ahiezer son of Ammishaddai.
        (None, "ת'ם", "Then"),
        ("וְנָסַע", "רחל", "the division"),
        ("דֶּגֶל מַחֲנֵה", "מרכז עסכר", "of the camp of"),
        ("בְנֵי-דָן", "בני דן", "the sons of Dan set out,"),
        ("מְאַסֵּף לְכָל-הַמַּחֲנֹת", "עלי' סאקה' סאיר אלעסאכר", "at the rear of all the camp,"),
        ("לְצִבְאֹתָם", "לגיושהם", "by their hosts;"),
        ("וְעַל-צְבָאוֹ", "ועלי' גישה", "and over his host"),
        ("אֲחִיעֶזֶר", "אחיעזר", "was Ahiezer"),
        ("בֶּן-עַמִּישַׁדָּי", "אבן עמישדי", "son of Ammishaddai."),
    ],
    26: [
        # HE: וְעַל-צְבָא--מַטֵּה בְּנֵי אָשֵׁר פַּגְעִיאֵל בֶּן-עָכְרָן
        # JA: ועלי' גיש סבט אשר. פגעיאל אבן עכרן
        # EN: And over the host of the tribe of Asher was Pagiel son of Ochran.
        ("וְעַל-צְבָא", "ועלי' גיש", "And over the host of"),
        ("מַטֵּה בְּנֵי אָשֵׁר", "סבט אשר", "the tribe of Asher"),
        ("פַּגְעִיאֵל", "פגעיאל", "was Pagiel"),
        ("בֶּן-עָכְרָן", "אבן עכרן", "son of Ochran."),
    ],
    27: [
        # HE: וְעַל-צְבָא--מַטֵּה בְּנֵי נַפְתָּלִי אֲחִירַע בֶּן-עֵינָן
        # JA: ועלי' גיש סבט נפתלי. אחירע אבן עינן
        # EN: And over the host of the tribe of Naphtali was Ahira son of Enan.
        ("וְעַל-צְבָא", "ועלי' גיש", "And over the host of"),
        ("מַטֵּה בְּנֵי נַפְתָּלִי", "סבט נפתלי", "the tribe of Naphtali"),
        ("אֲחִירַע", "אחירע", "was Ahira"),
        ("בֶּן-עֵינָן", "אבן עינן", "son of Enan."),
    ],
    28: [
        # HE: אֵלֶּה מַסְעֵי בְנֵי-יִשְׂרָאֵל לְצִבְאֹתָם וַיִּסָּעוּ
        # JA: הד'ה מראחל בני אסראיל לגיושהם. פלמא רחלו
        # EN: These are the journeys of the sons of Israel by their hosts, whenever they set out.
        ("אֵלֶּה", "הד'ה", "These are"),
        ("מַסְעֵי", "מראחל", "the journeys of"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("לְצִבְאֹתָם", "לגיושהם", "by their hosts,"),
        ("וַיִּסָּעוּ", "פלמא רחלו", "whenever they set out."),
    ],
    29: [
        # HE: וַיֹּאמֶר מֹשֶׁה לְחֹבָב בֶּן-רְעוּאֵל הַמִּדְיָנִי חֹתֵן מֹשֶׁה נֹסְעִים אֲנַחְנוּ אֶל-הַמָּקוֹם אֲשֶׁר אָמַר יְהוָה אֹתוֹ אֶתֵּן לָכֶם לְכָה אִתָּנוּ וְהֵטַבְנוּ לָךְ כִּי-יְהוָה דִּבֶּר-טוֹב עַל-יִשְׂרָאֵל
        # JA: קאל מוסי'. לחובב. אבן רעואל אלמדיאני חמוה. אנא ראחלין. אלי' אלמוצ'ע אלד'י קאל אללה. אייאהא אעטיכם. תעאל מענא ונחסן אליך. לאן אללה קד ועד אל אסראיל בכ'יר
        # EN: Moses said to Hobab son of Reuel the Midianite, his father-in-law: 'We are setting out to the place which God has said — that very one I will give to you. Come with us and we will deal well with you, for God has promised the house of Israel with good.'
        ("וַיֹּאמֶר", "קאל", "Moses"),
        ("מֹשֶׁה", "מוסי'", "said to"),
        ("לְחֹבָב", "לחובב", "Hobab"),
        ("בֶּן-רְעוּאֵל", "אבן רעואל", "son of Reuel"),
        ("הַמִּדְיָנִי", "אלמדיאני", "the Midianite,"),
        ("חֹתֵן מֹשֶׁה", "חמוה", "his father-in-law:"),
        ("נֹסְעִים אֲנַחְנוּ", "אנא ראחלין", "'We are setting out"),
        ("אֶל-הַמָּקוֹם", "אלי' אלמוצ'ע", "to the place"),
        ("אֲשֶׁר אָמַר יְהוָה", "אלד'י קאל אללה", "which God has said —"),
        ("אֹתוֹ אֶתֵּן לָכֶם", "אייאהא אעטיכם", "that very one I will give to you."),
        ("לְכָה אִתָּנוּ וְהֵטַבְנוּ לָךְ", "תעאל מענא ונחסן אליך", "Come with us and we will deal well with you,"),
        ("כִּי-יְהוָה", "לאן אללה", "for God"),
        ("דִּבֶּר-טוֹב", "קד ועד", "has promised"),
        ("עַל-יִשְׂרָאֵל", "אל אסראיל בכ'יר", "the house of Israel with good.'"),
    ],
    30: [
        # HE: וַיֹּאמֶר אֵלָיו לֹא אֵלֵךְ כִּי אִם-אֶל-אַרְצִי וְאֶל-מוֹלַדְתִּי אֵלֵךְ
        # JA: קאל לא אמצ'י. אלא אלי' ארצ'י ומולדי
        # EN: He said: 'I will not go, but only to my own land and my birthplace.'
        ("וַיֹּאמֶר", "קאל", "He said:"),
        ("לֹא אֵלֵךְ", "לא אמצ'י", "'I will not go,"),
        ("כִּי אִם", "אלא", "but only"),
        ("אֶל-אַרְצִי", "אלי' ארצ'י", "to my own land"),
        ("וְאֶל-מוֹלַדְתִּי אֵלֵךְ", "ומולדי", "and my birthplace.'"),
    ],
    31: [
        # HE: וַיֹּאמֶר אַל-נָא תַּעֲזֹב אֹתָנוּ כִּי עַל-כֵּן יָדַעְתָּ חֲנֹתֵנוּ בַּמִּדְבָּר וְהָיִיתָ לָּנוּ לְעֵינָיִם
        # JA: קאל יא הד'א לא תתרכנא. פאנך תעלם. אן פי טול מקאמנא פי אלבר. כנת לנא כאבצארנא
        # EN: He said: 'O good man, do not leave us, for you know that throughout the length of our sojourn in the open country, you have been for us as our eyesight.'
        ("וַיֹּאמֶר", "קאל", "He said:"),
        (None, "יא הד'א", "'O good man,"),
        ("אַל-נָא תַּעֲזֹב אֹתָנוּ", "לא תתרכנא", "do not leave us,"),
        ("כִּי עַל-כֵּן יָדַעְתָּ", "פאנך תעלם", "for you know"),
        ("חֲנֹתֵנוּ", "אן פי טול מקאמנא", "that throughout the length of our sojourn"),
        ("בַּמִּדְבָּר", "פי אלבר", "in the open country,"),
        ("וְהָיִיתָ", "כנת", "you have been"),
        ("לָּנוּ", "לנא", "for us"),
        ("לְעֵינָיִם", "כאבצארנא", "as our eyesight.'"),
    ],
    32: [
        # HE: וְהָיָה כִּי-תֵלֵךְ עִמָּנוּ וְהָיָה הַטּוֹב הַהוּא אֲשֶׁר יֵיטִיב יְהוָה עִמָּנוּ--וְהֵטַבְנוּ לָךְ
        # JA: פאן סרת מענא. פאי כ'יר יחסן אללה בה אלינא. נחסן אליך מנה
        # EN: 'And if you journey with us, then whatever good God shall deal well to us with, we will deal well with you from it.'
        ("וְהָיָה כִּי-תֵלֵךְ", "פאן סרת", "'And if you journey"),
        ("עִמָּנוּ", "מענא", "with us,"),
        ("וְהָיָה הַטּוֹב הַהוּא", "פאי כ'יר", "then whatever good"),
        ("אֲשֶׁר יֵיטִיב יְהוָה", "יחסן אללה", "God shall deal well"),
        ("עִמָּנוּ", "בה אלינא", "to us with,"),
        ("וְהֵטַבְנוּ לָךְ", "נחסן אליך מנה", "we will deal well with you from it.'"),
    ],
    33: [
        # HE: וַיִּסְעוּ מֵהַר יְהוָה דֶּרֶךְ שְׁלֹשֶׁת יָמִים וַאֲרוֹן בְּרִית-יְהוָה נֹסֵעַ לִפְנֵיהֶם דֶּרֶךְ שְׁלֹשֶׁת יָמִים לָתוּר לָהֶם מְנוּחָה
        # JA: פרחלו מן גבל אללה. מסאפה' ת'לאת'ה אייאם. וצנדוק עהד אללה סאיר בין אידיהם. מסאפה' תלך אלת'לאת'ה' אלאייאם. לי'כתאר להם מסתקרא
        # EN: And they set out from the mountain of God a distance of three days' journey; and the ark of the covenant of God was moving before them a distance of those three days, to choose a resting-place for them.
        ("וַיִּסְעוּ", "פרחלו", "And they set out"),
        ("מֵהַר יְהוָה", "מן גבל אללה", "from the mountain of God"),
        ("דֶּרֶךְ שְׁלֹשֶׁת יָמִים", "מסאפה' ת'לאת'ה אייאם", "a distance of three days' journey;"),
        ("וַאֲרוֹן", "וצנדוק", "and the ark"),
        ("בְּרִית-יְהוָה", "עהד אללה", "of the covenant of God"),
        ("נֹסֵעַ", "סאיר", "was moving"),
        ("לִפְנֵיהֶם", "בין אידיהם", "before them"),
        ("דֶּרֶךְ שְׁלֹשֶׁת יָמִים", "מסאפה' תלך אלת'לאת'ה' אלאייאם", "a distance of those three days,"),
        ("לָתוּר לָהֶם", "לי'כתאר להם", "to choose"),
        ("מְנוּחָה", "מסתקרא", "a resting-place for them."),
    ],
    34: [
        # HE: וַעֲנַן יְהוָה עֲלֵיהֶם יוֹמָם בְּנָסְעָם מִן-הַמַּחֲנֶה
        # JA: וג'מאם אללה עליהם נהארא. אד' רחלו מן אלעסכר
        # EN: And the cloud of God was over them by day, when they set out from the camp.
        ("וַעֲנַן", "וג'מאם", "And the cloud"),
        ("יְהוָה", "אללה", "of God"),
        ("עֲלֵיהֶם", "עליהם", "was over them"),
        ("יוֹמָם", "נהארא", "by day,"),
        ("בְּנָסְעָם", "אד' רחלו", "when they set out"),
        ("מִן-הַמַּחֲנֶה", "מן אלעסכר", "from the camp."),
    ],
    36: [
        # HE: וּבְנֻחֹה יֹאמַר שׁוּבָה יְהוָה רִבְבוֹת אַלְפֵי יִשְׂרָאֵל
        # JA: וענד נזולה אן יקול. רד יא רב נורך. אלי' רבוואת אלוף אל אסראיל
        # EN: And at its coming to rest, he would say: 'Return, O Lord, Your light, to the ten-thousands of the thousands of the house of Israel.'
        ("וּבְנֻחֹה", "וענד נזולה", "And at its coming to rest,"),
        ("יֹאמַר", "אן יקול", "he would say:"),
        ("שׁוּבָה", "רד", "'Return,"),
        ("יְהוָה", "יא רב", "O Lord,"),
        (None, "נורך", "Your light,"),
        ("רִבְבוֹת", "אלי' רבוואת", "to the ten-thousands"),
        ("אַלְפֵי יִשְׂרָאֵל", "אלוף אל אסראיל", "of the thousands of the house of Israel.'"),
    ],
}

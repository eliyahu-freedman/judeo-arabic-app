"""Hand-authored alignment triples for Devarim chapter 6.

Word-level: each JA (Saadia) word is its own group, mapped to the Hebrew word
it renders and its English counterpart. The runtime resolver matches each side
independently (lib/alignment.ts), so words link correctly even across word-order
crossings — verb-subject inversions ("כלם אללה" ↔ "God spoke"), English-fronted
negations, and Hebrew construct reorderings. Words Saadia adds with no Hebrew
source (glosses, expansions) carry he=None and link JA↔English only.
"""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    # JA v1: "והזא אלוצאיא. ואלרסום ואלאחכאמ. אלזי אמרני אללה רבכם אן אעלמכמ. אן תצנעוהא פי אלבלד. אלזי אנתם גאיזין אליה לתחוזוה"
    # HE v1: "וְזֹאת הַמִּצְוָה הַחֻקִּים וְהַמִּשְׁפָּטִים אֲשֶׁר צִוָּה יְהוָה אֱלֹהֵיכֶם לְלַמֵּד אֶתְכֶם--לַעֲשׂוֹת בָּאָרֶץ אֲשֶׁר אַתֶּם עֹבְרִים שָׁמָּה לְרִשְׁתָּהּ"
    # EN v1: "And these are the commandments, and the statutes and the ordinances, which God your Lord commanded me to teach you — that you do them in the land to which you are crossing over, to take possession of it."
    1: [
        ("וְזֹאת", "והזא", "And these are"),
        ("הַמִּצְוָה", "אלוצאיא", "the commandments"),
        ("הַחֻקִּים", "ואלרסום", "and the statutes"),
        ("וְהַמִּשְׁפָּטִים", "ואלאחכאמ", "and the ordinances"),
        ("אֲשֶׁר", "אלזי", "which"),
        ("צִוָּה", "אמרני", "commanded me"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֵיכֶם", "רבכם", "your Lord"),
        ("לְלַמֵּד", "אן אעלמכמ", "to teach you"),
        ("לַעֲשׂוֹת", "אן תצנעוהא", "that you do them"),
        ("בָּאָרֶץ", "פי אלבלד", "in the land"),
        ("אֲשֶׁר", "אלזי", "to which"),
        ("אַתֶּם", "אנתם", "you are"),
        ("עֹבְרִים", "גאיזין", "crossing over"),
        ("שָׁמָּה", "אליה", "to"),
        ("לְרִשְׁתָּהּ", "לתחוזוה", "to take possession of it"),
    ],
    # JA v2: "לכי תכ'אף אללה רבך. ותחפץ' גמיע רסומה ווצאיאה אלזי אנא אמרך. אנת ואבנך ואבן אבנך. טול אייאם חיאתך. ולכי תטול מדתך"
    # HE v2: "לְמַעַן תִּירָא אֶת-יְהוָה אֱלֹהֶיךָ לִשְׁמֹר אֶת-כָּל-חֻקֹּתָיו וּמִצְו‍ֹתָיו אֲשֶׁר אָנֹכִי מְצַוֶּךָ אַתָּה וּבִנְךָ וּבֶן-בִּנְךָ כֹּל יְמֵי חַיֶּיךָ--וּלְמַעַן יַאֲרִכֻן יָמֶיךָ"
    # EN v2: "That you may fear God your Lord, and keep all His statutes and His commandments which I command you — you and your son and your son's son — all the days of your life, and that your span of days may be long."
    2: [
        ("לְמַעַן", "לכי", "That you may"),
        ("תִּירָא", "תכ'אף", "fear"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֶיךָ", "רבך", "your Lord"),
        ("לִשְׁמֹר", "ותחפץ'", "and keep"),
        ("אֶת-כָּל-חֻקֹּתָיו", "גמיע רסומה", "all His statutes"),
        ("וּמִצְו‍ֹתָיו", "ווצאיאה", "and His commandments"),
        ("אֲשֶׁר", "אלזי", "which"),
        ("אָנֹכִי", "אנא", "I"),
        ("מְצַוֶּךָ", "אמרך", "command you"),
        ("אַתָּה", "אנת", "you"),
        ("וּבִנְךָ", "ואבנך", "and your son"),
        ("וּבֶן-בִּנְךָ", "ואבן אבנך", "and your son's son"),
        ("כֹּל", "טול", "all"),
        ("יְמֵי", "אייאם", "the days of"),
        ("חַיֶּיךָ", "חיאתך", "your life"),
        ("וּלְמַעַן", "ולכי", "and that"),
        ("יַאֲרִכֻן יָמֶיךָ", "תטול מדתך", "your span of days may be long"),
    ],
    # JA v3: "פאסמע זאלך יא אסראיל ואחפצ'ה ואעמל בה. לכי יכ'אר לך. ולכי תכת'ר גדא. כמא ועדך אללה אלאה אבאיך. בלד יפיץ' לבנא ועסלא"
    # HE v3: "וְשָׁמַעְתָּ יִשְׂרָאֵל וְשָׁמַרְתָּ לַעֲשׂוֹת אֲשֶׁר יִיטַב לְךָ וַאֲשֶׁר תִּרְבּוּן מְאֹד כַּאֲשֶׁר דִּבֶּר יְהוָה אֱלֹהֵי אֲבֹתֶיךָ לָךְ--אֶרֶץ זָבַת חָלָב וּדְבָשׁ"
    # EN v3: "So hear that, O Israel, and keep it and act by it — that it may go well for you, and that you may multiply greatly — as God, the God of your fathers, promised you: a land flowing with milk and honey."
    3: [
        (None, "פאסמע", "So hear"),
        (None, "זאלך", "that"),
        ("וְשָׁמַעְתָּ", "יא אסראיל", "O Israel"),
        ("וְשָׁמַרְתָּ", "ואחפצ'ה", "and keep it"),
        ("לַעֲשׂוֹת", "ואעמל בה", "and act by it"),
        ("אֲשֶׁר יִיטַב לְךָ", "לכי יכ'אר לך", "that it may go well for you"),
        ("וַאֲשֶׁר תִּרְבּוּן", "ולכי תכת'ר", "and that you may multiply"),
        ("מְאֹד", "גדא", "greatly"),
        ("כַּאֲשֶׁר", "כמא", "as"),
        ("דִּבֶּר", "ועדך", "promised you"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֵי", "אלאה", "the God of"),
        ("אֲבֹתֶיךָ", "אבאיך", "your fathers"),
        ("אֶרֶץ", "בלד", "a land"),
        ("זָבַת", "יפיץ'", "flowing with"),
        ("חָלָב", "לבנא", "milk"),
        ("וּדְבָשׁ", "ועסלא", "and honey"),
    ],
    # JA v4: "אעלם יא אסראיל. אן אללה רבנא אללה אלואחד"
    # HE v4: "שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד"
    # EN v4: "Know, O Israel, that God is our Lord, God is the One."
    4: [
        ("שְׁמַע", "אעלם", "Know"),
        ("יִשְׂרָאֵל", "יא אסראיל", "O Israel"),
        (None, "אן", "that"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֵינוּ", "רבנא", "is our Lord"),
        ("יְהוָה", "אללה", "God"),
        ("אֶחָד", "אלואחד", "is the One"),
    ],
    # JA v5: "ואחבב אללה רבך מכ'לצא. בכל קלבך ונפסך ווגדך"
    # HE v5: "וְאָהַבְתָּ אֵת יְהוָה אֱלֹהֶיךָ בְּכָל-לְבָבְךָ וּבְכָל-נַפְשְׁךָ וּבְכָל-מְאֹדֶךָ"
    # EN v5: "And love God your Lord sincerely, with all your heart and your soul and your substance."
    5: [
        ("וְאָהַבְתָּ", "ואחבב", "And love"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֶיךָ", "רבך", "your Lord"),
        (None, "מכ'לצא", "sincerely"),
        ("בְּכָל-לְבָבְךָ", "בכל קלבך", "with all your heart"),
        ("וּבְכָל-נַפְשְׁךָ", "ונפסך", "and your soul"),
        ("וּבְכָל-מְאֹדֶךָ", "ווגדך", "and your substance"),
    ],
    # JA v6: "ותכון הזה אלכלמאת. אלתי אמרך בהא אליום פי קלבך"
    # HE v6: "וְהָיוּ הַדְּבָרִים הָאֵלֶּה אֲשֶׁר אָנֹכִי מְצַוְּךָ הַיּוֹם--עַל-לְבָבֶךָ"
    # EN v6: "And let these words, which I command you today, be in your heart."
    6: [
        ("וְהָיוּ", "ותכון", "And let"),
        ("הַדְּבָרִים", "הזה אלכלמאת", "these words"),
        ("הָאֵלֶּה", "אלתי", "which"),
        ("אָנֹכִי", "אמרך", "I command"),
        ("מְצַוְּךָ", "בהא", "you"),
        ("הַיּוֹם", "אליום", "today"),
        ("עַל-לְבָבֶךָ", "פי קלבך", "be in your heart"),
    ],
    # JA v7: "ואחכהא לבניך. ואדרסהא פי חאלגלוסך פי מנזלך ופי מסירך פי טריקך. וענד ניאמך וקיאמך"
    # HE v7: "וְשִׁנַּנְתָּם לְבָנֶיךָ וְדִבַּרְתָּ בָּם בְּשִׁבְתְּךָ בְּבֵיתֶךָ וּבְלֶכְתְּךָ בַדֶּרֶךְ וּבְשָׁכְבְּךָ וּבְקוּמֶךָ"
    # EN v7: "And recount them to your children, and study them diligently while sitting in your dwelling and while traveling on your road, and at your lying down and your rising up."
    7: [
        ("וְשִׁנַּנְתָּם", "ואחכהא", "And recount them"),
        ("לְבָנֶיךָ", "לבניך", "to your children"),
        ("וְדִבַּרְתָּ", "ואדרסהא", "and study them diligently"),
        ("בְּשִׁבְתְּךָ", "פי חאלגלוסך", "while sitting"),
        ("בְּבֵיתֶךָ", "פי מנזלך", "in your dwelling"),
        ("וּבְלֶכְתְּךָ", "ופי מסירך", "and while traveling"),
        ("בַדֶּרֶךְ", "פי טריקך", "on your road"),
        ("וּבְשָׁכְבְּךָ", "וענד ניאמך", "and at your lying down"),
        ("וּבְקוּמֶךָ", "וקיאמך", "and your rising up"),
    ],
    # JA v8: "ואעקדהא עלאמה עלי' ידך. ותכון מנשורא בין עיניך"
    # HE v8: "וּקְשַׁרְתָּם לְאוֹת עַל-יָדֶךָ וְהָיוּ לְטֹטָפֹת בֵּין עֵינֶיךָ"
    # EN v8: "And bind them as a sign upon your hand, and let them be displayed between your eyes."
    8: [
        ("וּקְשַׁרְתָּם", "ואעקדהא", "And bind them"),
        ("לְאוֹת", "עלאמה", "as a sign"),
        ("עַל-יָדֶךָ", "עלי' ידך", "upon your hand"),
        ("וְהָיוּ", "ותכון", "and let them be"),
        ("לְטֹטָפֹת", "מנשורא", "displayed"),
        ("בֵּין עֵינֶיךָ", "בין עיניך", "between your eyes"),
    ],
    # JA v9: "ואכתבהא עלי' כ'דוד פתוח מנאזלך ואבואבך"
    # HE v9: "וּכְתַבְתָּם עַל-מְזֻזוֹת בֵּיתֶךָ וּבִשְׁעָרֶיךָ"
    # EN v9: "And write them upon the cheeks of the doorposts of your dwelling and your gates."
    9: [
        ("וּכְתַבְתָּם", "ואכתבהא", "And write them"),
        (None, "עלי' כ'דוד פתוח", "upon the cheeks of the doorposts of"),
        ("עַל-מְזֻזוֹת", "מנאזלך", "your dwelling"),
        ("וּבִשְׁעָרֶיךָ", "ואבואבך", "and your gates"),
    ],
    # JA v10: "ואזא אדכ'לך אללה רבך. אלי' אלבלד אלזי קסם לאבאיך. לאברהים ליצחק ויעקוב אן יעטיכהא. תלך קרא. כבאר גיאד מא לם תבניהא"
    # HE v10: "וְהָיָה כִּי יְבִיאֲךָ יְהוָה אֱלֹהֶיךָ אֶל-הָאָרֶץ אֲשֶׁר נִשְׁבַּע לַאֲבֹתֶיךָ לְאַבְרָהָם לְיִצְחָק וּלְיַעֲקֹב--לָתֶת לָךְ עָרִים גְּדֹלֹת וְטֹבֹת אֲשֶׁר לֹא-בָנִיתָ"
    # EN v10: "And when God your Lord brings you into the land which He swore to your fathers — to Abraham, to Isaac, and to Jacob — to give to you: those towns, large and excellent, which you did not build,"
    10: [
        ("וְהָיָה כִּי", "ואזא", "And when"),
        ("יְבִיאֲךָ", "אדכ'לך", "brings you"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֶיךָ", "רבך", "your Lord"),
        ("אֶל-הָאָרֶץ", "אלי' אלבלד", "into the land"),
        ("אֲשֶׁר", "אלזי", "which"),
        ("נִשְׁבַּע", "קסם", "He swore"),
        ("לַאֲבֹתֶיךָ", "לאבאיך", "to your fathers"),
        ("לְאַבְרָהָם", "לאברהים", "to Abraham"),
        ("לְיִצְחָק", "ליצחק", "to Isaac"),
        ("וּלְיַעֲקֹב", "ויעקוב", "and to Jacob"),
        ("לָתֶת", "אן יעטיכהא", "to give to you"),
        (None, "תלך", "those"),
        ("עָרִים", "קרא", "towns"),
        ("גְּדֹלֹת", "כבאר", "large"),
        ("וְטֹבֹת", "גיאד", "and excellent"),
        ("אֲשֶׁר לֹא-בָנִיתָ", "מא לם תבניהא", "which you did not build"),
    ],
    # JA v11: "וביות ממלווה כל כ'יר לם תמלאהא. וצהאריג מנקורה לם תנקרהא. וכרום וזיאתין לם תג'רסהא. פאכלת ושבעת"
    # HE v11: "וּבָתִּים מְלֵאִים כָּל-טוּב אֲשֶׁר לֹא-מִלֵּאתָ וּבֹרֹת חֲצוּבִים אֲשֶׁר לֹא-חָצַבְתָּ כְּרָמִים וְזֵיתִים אֲשֶׁר לֹא-נָטָעְתָּ וְאָכַלְתָּ וְשָׂבָעְתָּ"
    # EN v11: "and houses filled with every good which you did not fill, and cisterns hewn in the rock which you did not hew, and vineyards and olive trees which you did not plant — and you eat and are satisfied,"
    11: [
        ("וּבָתִּים", "וביות", "and houses"),
        ("מְלֵאִים", "ממלווה", "filled"),
        ("כָּל-טוּב", "כל כ'יר", "with every good"),
        ("אֲשֶׁר לֹא-מִלֵּאתָ", "לם תמלאהא", "which you did not fill"),
        ("וּבֹרֹת", "וצהאריג", "and cisterns"),
        ("חֲצוּבִים", "מנקורה", "hewn in the rock"),
        ("אֲשֶׁר לֹא-חָצַבְתָּ", "לם תנקרהא", "which you did not hew"),
        ("כְּרָמִים", "וכרום", "and vineyards"),
        ("וְזֵיתִים", "וזיאתין", "and olive trees"),
        ("אֲשֶׁר לֹא-נָטָעְתָּ", "לם תג'רסהא", "which you did not plant"),
        ("וְאָכַלְתָּ", "פאכלת", "and you eat"),
        ("וְשָׂבָעְתָּ", "ושבעת", "and are satisfied"),
    ],
    # JA v12: "פאחזר אן תנסא אללה. אלזי אכ'רגך. מן בלד מצר מן בית אלעבודייה"
    # HE v12: "הִשָּׁמֶר לְךָ פֶּן-תִּשְׁכַּח אֶת-יְהוָה אֲשֶׁר הוֹצִיאֲךָ מֵאֶרֶץ מִצְרַיִם מִבֵּית עֲבָדִים"
    # EN v12: "then beware lest you forget God who brought you out from the land of Egypt, from the house of servitude."
    12: [
        ("הִשָּׁמֶר לְךָ", "פאחזר", "then beware"),
        ("פֶּן-תִּשְׁכַּח", "אן תנסא", "lest you forget"),
        ("אֶת-יְהוָה", "אללה", "God"),
        ("אֲשֶׁר", "אלזי", "who"),
        ("הוֹצִיאֲךָ", "אכ'רגך", "brought you out"),
        ("מֵאֶרֶץ", "מן בלד", "from the land of"),
        ("מִצְרַיִם", "מצר", "Egypt"),
        ("מִבֵּית", "מן בית", "from the house of"),
        ("עֲבָדִים", "אלעבודייה", "servitude"),
    ],
    # JA v13: "בל כ'ף אללה רבך ואעבדה. ואחלף באסמה בארא"
    # HE v13: "אֶת-יְהוָה אֱלֹהֶיךָ תִּירָא וְאֹתוֹ תַעֲבֹד וּבִשְׁמוֹ תִּשָּׁבֵעַ"
    # EN v13: "Rather, fear God your Lord and serve Him, and swear by His name uprightly."
    13: [
        (None, "בל", "Rather"),
        ("תִּירָא", "כ'ף", "fear"),
        ("אֶת-יְהוָה", "אללה", "God"),
        ("אֱלֹהֶיךָ", "רבך", "your Lord"),
        ("וְאֹתוֹ תַעֲבֹד", "ואעבדה", "and serve Him"),
        ("וּבִשְׁמוֹ", "ואחלף באסמה", "and swear by His name"),
        ("תִּשָּׁבֵעַ", "בארא", "uprightly"),
    ],
    # JA v14: "ולא תתבעו מעבודאת אכ'ר. מן מעבודאת אלאממ. אלזין חואליכמ"
    # HE v14: "לֹא תֵלְכוּן אַחֲרֵי אֱלֹהִים אֲחֵרִים--מֵאֱלֹהֵי הָעַמִּים אֲשֶׁר סְבִיבוֹתֵיכֶם"
    # EN v14: "And do not follow other objects of worship, from among the objects of worship of the nations that are round about you —"
    14: [
        ("לֹא תֵלְכוּן", "ולא תתבעו", "And do not follow"),
        ("אַחֲרֵי אֱלֹהִים אֲחֵרִים", "מעבודאת אכ'ר", "other objects of worship"),
        ("מֵאֱלֹהֵי", "מן מעבודאת", "from among the objects of worship of"),
        ("הָעַמִּים", "אלאממ", "the nations"),
        ("אֲשֶׁר", "אלזין", "that are"),
        ("סְבִיבוֹתֵיכֶם", "חואליכמ", "round about you"),
    ],
    # JA v15: "לאן אללה רבך. טאיק מעאקב פי מא בינכמ. ללא ישתד ג'צ'בה עליך. פינפזך ען וגה אלארץ'"
    # HE v15: "כִּי אֵל קַנָּא יְהוָה אֱלֹהֶיךָ בְּקִרְבֶּךָ פֶּן-יֶחֱרֶה אַף-יְהוָה אֱלֹהֶיךָ בָּךְ וְהִשְׁמִידְךָ מֵעַל פְּנֵי הָאֲדָמָה"
    # EN v15: "for God your Lord is a forceful punisher in your midst — lest His anger intensify against you and He cut you off from the face of the earth."
    15: [
        ("כִּי", "לאן", "for"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֶיךָ", "רבך", "your Lord"),
        ("אֵל קַנָּא", "טאיק מעאקב", "is a forceful punisher"),
        ("בְּקִרְבֶּךָ", "פי מא בינכמ", "in your midst"),
        ("פֶּן-יֶחֱרֶה", "ללא ישתד", "lest His anger intensify"),
        ("אַף-יְהוָה אֱלֹהֶיךָ", "ג'צ'בה", "His anger"),
        ("בָּךְ", "עליך", "against you"),
        ("וְהִשְׁמִידְךָ", "פינפזך", "and He cut you off"),
        ("מֵעַל פְּנֵי", "ען וגה", "from the face of"),
        ("הָאֲדָמָה", "אלארץ'", "the earth"),
    ],
    # JA v16: "ולא תגרבו אללה רבכמ. כמא גרבתמוה פי זאת אלמחנה"
    # HE v16: "לֹא תְנַסּוּ אֶת-יְהוָה אֱלֹהֵיכֶם כַּאֲשֶׁר נִסִּיתֶם בַּמַּסָּה"
    # EN v16: "And do not put God your Lord to the test, as you tested Him at the place of trial."
    16: [
        ("לֹא תְנַסּוּ", "ולא תגרבו", "And do not put"),
        ("אֶת-יְהוָה", "אללה", "God"),
        ("אֱלֹהֵיכֶם", "רבכמ", "your Lord"),
        (None, "כמא", "to the test, as"),
        ("כַּאֲשֶׁר נִסִּיתֶם", "גרבתמוה", "you tested Him"),
        ("בַּמַּסָּה", "פי זאת אלמחנה", "at the place of trial"),
    ],
    # JA v17: "בל אחפט'ו חפט'א. וצאיא אללה רבכמ. ושואהדה ורסומה אלזי אמרך בהא"
    # HE v17: "שָׁמוֹר תִּשְׁמְרוּן אֶת-מִצְו‍ֹת יְהוָה אֱלֹהֵיכֶם וְעֵדֹתָיו וְחֻקָּיו אֲשֶׁר צִוָּךְ"
    # EN v17: "Rather, keep diligently the commandments of God your Lord, and His testimonies and His statutes which He commanded you."
    17: [
        (None, "בל", "Rather"),
        ("שָׁמוֹר תִּשְׁמְרוּן", "אחפט'ו חפט'א", "keep diligently"),
        ("אֶת-מִצְו‍ֹת", "וצאיא", "the commandments of"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֵיכֶם", "רבכמ", "your Lord"),
        ("וְעֵדֹתָיו", "ושואהדה", "and His testimonies"),
        ("וְחֻקָּיו", "ורסומה", "and His statutes"),
        ("אֲשֶׁר", "אלזי", "which"),
        ("צִוָּךְ", "אמרך בהא", "He commanded you"),
    ],
    # JA v18: "ואצנע אלמסתקים ואלגייד בין ידי אללה. לכי יכ'אר לך. ותדכ'ל ותחוז אלבלד אלגייד. אלזי קסם אללה לאבאיך"
    # HE v18: "וְעָשִׂיתָ הַיָּשָׁר וְהַטּוֹב בְּעֵינֵי יְהוָה--לְמַעַן יִיטַב לָךְ וּבָאתָ וְיָרַשְׁתָּ אֶת-הָאָרֶץ הַטֹּבָה אֲשֶׁר-נִשְׁבַּע יְהוָה לַאֲבֹתֶיךָ"
    # EN v18: "And do what is upright and good before God — that it may go well for you, and that you may enter and take possession of the good land which God swore to your fathers."
    18: [
        ("וְעָשִׂיתָ", "ואצנע", "And do"),
        ("הַיָּשָׁר", "אלמסתקים", "what is upright"),
        ("וְהַטּוֹב", "ואלגייד", "and good"),
        ("בְּעֵינֵי", "בין ידי", "before"),
        ("יְהוָה", "אללה", "God"),
        ("לְמַעַן יִיטַב לָךְ", "לכי יכ'אר לך", "that it may go well for you"),
        ("וּבָאתָ", "ותדכ'ל", "and that you may enter"),
        ("וְיָרַשְׁתָּ", "ותחוז", "and take possession of"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the"),
        ("הַטֹּבָה", "אלגייד", "good land"),
        ("אֲשֶׁר-נִשְׁבַּע", "אלזי קסם", "which"),
        ("יְהוָה", "אללה", "God"),
        ("לַאֲבֹתֶיךָ", "לאבאיך", "swore to your fathers"),
    ],
    # JA v19: "לידפע גמיע אעדאיך מן בין ידיך. כמא ועד אללה"
    # HE v19: "לַהֲדֹף אֶת-כָּל-אֹיְבֶיךָ מִפָּנֶיךָ כַּאֲשֶׁר דִּבֶּר יְהוָה"
    # EN v19: "To drive out all your enemies from before you, as God promised you."
    19: [
        ("לַהֲדֹף", "לידפע", "To drive out"),
        ("אֶת-כָּל-אֹיְבֶיךָ", "גמיע אעדאיך", "all your enemies"),
        ("מִפָּנֶיךָ", "מן בין ידיך", "from before you"),
        ("כַּאֲשֶׁר", "כמא", "as"),
        ("דִּבֶּר", "ועד", "promised"),
        ("יְהוָה", "אללה", "God"),
    ],
    # JA v20: "ואזא סאלך אבנך גדא קאילא. מא סבב אלשואהד. ואלרסום ואלאחכאמ. אלזי אמרכם אללה רבנא"
    # HE v20: "כִּי-יִשְׁאָלְךָ בִנְךָ מָחָר לֵאמֹר מָה הָעֵדֹת וְהַחֻקִּים וְהַמִּשְׁפָּטִים אֲשֶׁר צִוָּה יְהוָה אֱלֹהֵינוּ אֶתְכֶם"
    # EN v20: "And when your son asks you tomorrow, saying: 'What is the reason for the testimonies, and the statutes and the ordinances, which God our Lord has commanded you?' —"
    20: [
        ("כִּי-יִשְׁאָלְךָ", "ואזא סאלך", "And when your son asks you"),
        ("בִנְךָ", "אבנך", "your son"),
        ("מָחָר", "גדא", "tomorrow"),
        ("לֵאמֹר", "קאילא", "saying"),
        (None, "מא סבב", "What is the reason for"),
        ("הָעֵדֹת", "אלשואהד", "the testimonies"),
        ("וְהַחֻקִּים", "ואלרסום", "and the statutes"),
        ("וְהַמִּשְׁפָּטִים", "ואלאחכאמ", "and the ordinances"),
        ("אֲשֶׁר", "אלזי", "which"),
        ("צִוָּה", "אמרכם", "has commanded you"),
        ("יְהוָה", "אללה", "God"),
        ("אֱלֹהֵינוּ", "רבנא", "our Lord"),
    ],
    # JA v21: "פקל לה. כננא עבידא לפרעון במצר. ואכ'רגנא אללה. מן ת'ם ביד שדידה"
    # HE v21: "וְאָמַרְתָּ לְבִנְךָ עֲבָדִים הָיִינוּ לְפַרְעֹה בְּמִצְרָיִם וַיֹּצִיאֵנוּ יְהוָה מִמִּצְרַיִם בְּיָד חֲזָקָה"
    # EN v21: "then say to him: 'We were slaves to Pharaoh in Egypt, and God brought us out from there with a mighty hand."
    21: [
        ("וְאָמַרְתָּ", "פקל", "then say"),
        ("לְבִנְךָ", "לה", "to him"),
        ("עֲבָדִים הָיִינוּ", "כננא עבידא", "We were slaves"),
        ("לְפַרְעֹה", "לפרעון", "to Pharaoh"),
        ("בְּמִצְרָיִם", "במצר", "in Egypt"),
        ("וַיֹּצִיאֵנוּ", "ואכ'רגנא", "and God brought us out"),
        ("יְהוָה", "אללה", "God"),
        ("מִמִּצְרַיִם", "מן ת'ם", "from there"),
        ("בְּיָד", "ביד", "with"),
        ("חֲזָקָה", "שדידה", "a mighty hand"),
    ],
    # JA v22: "פאחל אללה איאת ובראהין. ]עט'ימה] ]עט'ימה] עצ'ימה צ'ארה במצר. פי פרעון וגמיע אלה בחצ'רתנא"
    # HE v22: "וַיִּתֵּן יְהוָה אוֹתֹת וּמֹפְתִים גְּדֹלִים וְרָעִים בְּמִצְרַיִם בְּפַרְעֹה וּבְכָל-בֵּיתוֹ--לְעֵינֵינוּ"
    # EN v22: "And God brought down signs and proofs — great and harmful — upon Egypt, against Pharaoh and all his household, in our presence."
    22: [
        ("וַיִּתֵּן", "פאחל", "And God brought down"),
        ("יְהוָה", "אללה", "God"),
        ("אוֹתֹת", "איאת", "signs"),
        ("וּמֹפְתִים", "ובראהין", "and proofs"),
        ("גְּדֹלִים", "עצ'ימה", "great"),
        ("וְרָעִים", "צ'ארה", "and harmful"),
        ("בְּמִצְרַיִם", "במצר", "upon Egypt"),
        ("בְּפַרְעֹה", "פי פרעון", "against Pharaoh"),
        ("וּבְכָל-בֵּיתוֹ", "וגמיע אלה", "and all his household"),
        ("לְעֵינֵינוּ", "בחצ'רתנא", "in our presence"),
    ],
    # JA v23: "ואכ'רגנא מן ת'מ. לכי ידכ'לנא. ויעטינא אלבלד. אלזי קסם לאבאינא"
    # HE v23: "וְאוֹתָנוּ הוֹצִיא מִשָּׁם--לְמַעַן הָבִיא אֹתָנוּ לָתֶת לָנוּ אֶת-הָאָרֶץ אֲשֶׁר נִשְׁבַּע לַאֲבֹתֵינוּ"
    # EN v23: "And He brought us out from there, that He might bring us in and give us the land which He swore to our fathers."
    23: [
        ("וְאוֹתָנוּ הוֹצִיא", "ואכ'רגנא", "And He brought us out"),
        ("מִשָּׁם", "מן ת'מ", "from there"),
        ("לְמַעַן הָבִיא אֹתָנוּ", "לכי ידכ'לנא", "that He might bring us in"),
        ("לָתֶת לָנוּ", "ויעטינא", "and give us"),
        ("אֶת-הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר נִשְׁבַּע", "אלזי קסם", "which He swore"),
        ("לַאֲבֹתֵינוּ", "לאבאינא", "to our fathers"),
    ],
    # JA v24: "ת'ם אמרנא אללה. באן נצנע הזה אלרסומ . אן נכ'אף אללה רבנא. לכי יכ'אר לנא טול אלזמאן. ונחיא כיומנא הזא"
    # HE v24: "וַיְצַוֵּנוּ יְהוָה לַעֲשׂוֹת אֶת-כָּל-הַחֻקִּים הָאֵלֶּה לְיִרְאָה אֶת-יְהוָה אֱלֹהֵינוּ--לְטוֹב לָנוּ כָּל-הַיָּמִים לְחַיֹּתֵנוּ כְּהַיּוֹם הַזֶּה"
    # EN v24: "Then God commanded us to do these statutes — that we fear God our Lord — that it may go well for us all the time, and that we may live as we do this day."
    24: [
        (None, "ת'ם", "Then"),
        ("וַיְצַוֵּנוּ", "אמרנא", "commanded us"),
        ("יְהוָה", "אללה", "God"),
        ("לַעֲשׂוֹת", "באן נצנע", "to do"),
        ("אֶת-כָּל-הַחֻקִּים", "הזה אלרסומ", "these statutes"),
        ("הָאֵלֶּה", "אן", "that"),
        ("לְיִרְאָה", "נכ'אף", "we fear"),
        ("אֶת-יְהוָה", "אללה", "God"),
        ("אֱלֹהֵינוּ", "רבנא", "our Lord"),
        ("לְטוֹב לָנוּ", "לכי יכ'אר לנא", "that it may go well for us"),
        ("כָּל-הַיָּמִים", "טול אלזמאן", "all the time"),
        ("לְחַיֹּתֵנוּ", "ונחיא", "and that we may live"),
        ("כְּהַיּוֹם הַזֶּה", "כיומנא הזא", "as we do this day"),
    ],
    # JA v25: "וחסנה תכון לנא. אזחפט'נא ועמלנא גמיע הזה אלשריעה. בין ידי אללה רבנא כמא יאמרנא"
    # HE v25: "וּצְדָקָה תִּהְיֶה-לָּנוּ כִּי-נִשְׁמֹר לַעֲשׂוֹת אֶת-כָּל-הַמִּצְוָה הַזֹּאת לִפְנֵי יְהוָה אֱלֹהֵינוּ--כַּאֲשֶׁר צִוָּנוּ"
    # EN v25: "And it shall be a merit for us, when we keep and do all this law before God our Lord, as He commanded us.'"
    25: [
        ("וּצְדָקָה", "וחסנה", "And it shall be a merit"),
        ("תִּהְיֶה-לָּנוּ", "תכון לנא", "for us"),
        ("כִּי-נִשְׁמֹר", "אזחפט'נא", "when we keep"),
        ("לַעֲשׂוֹת", "ועמלנא", "and do"),
        ("אֶת-כָּל-הַמִּצְוָה", "גמיע הזה אלשריעה", "all this law"),
        ("הַזֹּאת", "בין ידי", "before"),
        ("לִפְנֵי", "אללה", "God"),
        ("יְהוָה", "רבנא", "our Lord"),
        ("אֱלֹהֵינוּ", "כמא", "as"),
        ("כַּאֲשֶׁר", "יאמרנא", "He commanded us"),
        ("צִוָּנוּ", "כמא", "as He commanded us"),
    ],
}

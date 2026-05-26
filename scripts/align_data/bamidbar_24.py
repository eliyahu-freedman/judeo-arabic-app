"""Hand-authored word-level alignment triples for Bamidbar chapter 24."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיַּרְא בִּלְעָם כִּי טוֹב בְּעֵינֵי יְהוָה לְבָרֵךְ אֶת-יִשְׂרָאֵל וְלֹא-הָלַךְ כְּפַעַם-בְּפַעַם לִקְרַאת נְחָשִׁים וַיָּשֶׁת אֶל-הַמִּדְבָּר פָּנָיו
        # JA: פלמא ראא בלעם. אן אלאצלח ענד אללה תבריך אל אסראיל . לם ימץ' כאלמרתין אלאוולתין פי טלב אלפאלאת. פאקבל בקצדה אלי' ברהם
        # EN: And when Balaam saw that it was more fitting before God to bless Israel, he did not proceed as in the first two times in seeking omens, but turned with his intent toward their wilderness.
        (None, "פלמא", "And when"),
        ("וַיַּרְא", "ראא", "saw"),
        ("בִּלְעָם", "בלעם", "Balaam"),
        ("כִּי טוֹב", "אן אלאצלח", "that it was more fitting"),
        ("בְּעֵינֵי יְהוָה", "ענד אללה", "before God"),
        ("לְבָרֵךְ", "תבריך", "to bless"),
        ("אֶת-יִשְׂרָאֵל", "אל אסראיל", "Israel,"),
        ("וְלֹא-הָלַךְ", "לם ימץ'", "he did not proceed"),
        ("כְּפַעַם-בְּפַעַם", "כאלמרתין אלאוולתין", "as in the first two times"),
        ("לִקְרַאת נְחָשִׁים", "פי טלב אלפאלאת", "in seeking omens,"),
        ("וַיָּשֶׁת", "פאקבל", "but turned"),
        (None, "בקצדה", "with his intent"),
        ("אֶל-הַמִּדְבָּר", "אלי' ברהם", "toward their wilderness."),
    ],
    2: [
        # HE: וַיִּשָּׂא בִלְעָם אֶת-עֵינָיו וַיַּרְא אֶת-יִשְׂרָאֵל שֹׁכֵן לִשְׁבָטָיו וַתְּהִי עָלָיו רוּחַ אֱלֹהִים
        # JA: פלמא מד בצרה וראהם. נאזלין עלי' נצ'אם אסבטאהם. חלת עלי'ה נבווה' אללה
        # EN: And when he extended his gaze and saw them encamped according to the order of their tribes, the prophecy of God rested upon him.
        (None, "פלמא", "And when"),
        ("וַיִּשָּׂא", "מד", "he extended"),
        ("אֶת-עֵינָיו", "בצרה", "his gaze"),
        ("וַיַּרְא", "וראהם", "and saw them"),
        ("אֶת-יִשְׂרָאֵל שֹׁכֵן", "נאזלין", "encamped"),
        ("לִשְׁבָטָיו", "עלי' נצ'אם אסבטאהם", "according to the order of their tribes,"),
        ("רוּחַ אֱלֹהִים", "נבווה' אללה", "the prophecy of God"),
        ("וַתְּהִי עָלָיו", "חלת עלי'ה", "rested upon him."),
    ],
    3: [
        # HE: וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר נְאֻם בִּלְעָם בְּנוֹ בְעֹר וּנְאֻם הַגֶּבֶר שְׁתֻם הָעָיִן
        # JA: פצ'רב מת'לה וקאל. קל יא בלעם אבן בעור. וקל יא אייהא אלרגל אלחדיד אלבצר
        # EN: And he uttered his parable and said: 'Speak, O Balaam son of Beor! And speak, O man of sharp sight!'
        ("וַיִּשָּׂא מְשָׁלוֹ", "פצ'רב מת'לה", "And he uttered his parable"),
        ("וַיֹּאמַר", "וקאל", "and said:"),
        ("נְאֻם", "קל", "'Speak,"),
        (None, "יא", "O"),
        ("בִּלְעָם", "בלעם", "Balaam"),
        ("בְּנוֹ בְעֹר", "אבן בעור", "son of Beor!"),
        ("וּנְאֻם", "וקל", "And speak,"),
        ("הַגֶּבֶר", "אלרגל", "O man of"),
        ("שְׁתֻם הָעָיִן", "אלחדיד אלבצר", "sharp sight!'"),
    ],
    4: [
        # HE: נְאֻם--שֹׁמֵעַ אִמְרֵי-אֵל אֲשֶׁר מַחֲזֵה שַׁדַּי יֶחֱזֶה נֹפֵל וּגְלוּי עֵינָיִם
        # JA: וקל יא סאמע אקואל אלטאיק. ונאצ'ר מנאצ'ר אלכאפי. והו נאים מפתוח אלעין
        # EN: 'And speak, O hearer of the words of the All-Powerful, and beholder of the visions of the All-Sufficient, who sleeps with open eyes!'
        ("נְאֻם", "וקל", "'And speak,"),
        ("שֹׁמֵעַ", "יא סאמע", "O hearer of"),
        ("אִמְרֵי-אֵל", "אקואל אלטאיק", "the words of the All-Powerful,"),
        ("מַחֲזֵה שַׁדַּי יֶחֱזֶה", "ונאצ'ר מנאצ'ר אלכאפי", "and beholder of the visions of the All-Sufficient,"),
        ("נֹפֵל", "והו נאים", "who sleeps"),
        ("וּגְלוּי עֵינָיִם", "מפתוח אלעין", "with open eyes!'"),
    ],
    5: [
        # HE: מַה-טֹּבוּ אֹהָלֶיךָ יַעֲקֹב מִשְׁכְּנֹתֶיךָ יִשְׂרָאֵל
        # JA: מא אגוד אכ'ביתך יא אל יעקוב. ומנאזלך יא אל אסראיל
        # EN: 'How goodly are your tents, O house of Jacob, and your dwellings, O house of Israel!'
        ("מַה-טֹּבוּ", "מא אגוד", "'How goodly are"),
        ("אֹהָלֶיךָ", "אכ'ביתך", "your tents,"),
        ("יַעֲקֹב", "יא אל יעקוב", "O house of Jacob,"),
        ("מִשְׁכְּנֹתֶיךָ", "ומנאזלך", "and your dwellings,"),
        ("יִשְׂרָאֵל", "יא אל אסראיל", "O house of Israel!'"),
    ],
    6: [
        # HE: כִּנְחָלִים נִטָּיוּ כְּגַנֹּת עֲלֵי נָהָר כַּאֲהָלִים נָטַע יְהוָה כַּאֲרָזִים עֲלֵי-מָיִם
        # JA: פהי כאודיה ממדודה. וכגנאן עלי' נהר. וכמצ'ארב צ'רבהא אללה. וכארוז עלי' מא
        # EN: 'For they are like valleys stretched out, and like gardens along a river, and like encampments pitched by God, and like cedars beside water.'
        (None, "פהי", "'For they are"),
        ("כִּנְחָלִים", "כאודיה", "like valleys"),
        ("נִטָּיוּ", "ממדודה", "stretched out,"),
        ("כְּגַנֹּת", "וכגנאן", "and like gardens"),
        ("עֲלֵי נָהָר", "עלי' נהר", "along a river,"),
        ("כַּאֲהָלִים", "וכמצ'ארב", "and like encampments"),
        ("נָטַע יְהוָה", "צ'רבהא אללה", "pitched by God,"),
        ("כַּאֲרָזִים", "וכארוז", "and like cedars"),
        ("עֲלֵי-מָיִם", "עלי' מא", "beside water.'"),
    ],
    7: [
        # HE: יִזַּל-מַיִם מִדָּלְיָו וְזַרְעוֹ בְּמַיִם רַבִּים וְיָרֹם מֵאֲגַג מַלְכּוֹ וְתִנַּשֵּׂא מַלְכֻתוֹ
        # JA: יהטל אלמא מן דואליה. וג'רסה פי מא ג'זיר. וירתפע מן אגג מלכה. ותתסאנא ממלכתה
        # EN: 'Water drips from his branches, and his planting is in abundant water; and his king shall rise above Agag, and his kingdom shall be exalted.'
        ("יִזַּל-מַיִם", "יהטל אלמא", "'Water drips"),
        ("מִדָּלְיָו", "מן דואליה", "from his branches,"),
        ("וְזַרְעוֹ", "וג'רסה", "and his planting is"),
        ("בְּמַיִם רַבִּים", "פי מא ג'זיר", "in abundant water;"),
        ("וְיָרֹם", "וירתפע", "and his king shall rise"),
        ("מֵאֲגַג", "מן אגג", "above Agag,"),
        ("מַלְכּוֹ", "מלכה", "and his kingdom"),
        ("וְתִנַּשֵּׂא מַלְכֻתוֹ", "ותתסאנא ממלכתה", "shall be exalted.'"),
    ],
    8: [
        # HE: אֵל מוֹצִיאוֹ מִמִּצְרַיִם כְּתוֹעֲפֹת רְאֵם לוֹ יֹאכַל גּוֹיִם צָרָיו וְעַצְמֹתֵיהֶם יְגָרֵם--וְחִצָּיו יִמְחָץ
        # JA: אלטאיק אלמכ'רגהם מן מצר. כארק אלרים מאנע ענהם. והו יאכל אעדאיה מן אלאמם. ועצ'אמהם ינהש וסהאמה תדנפהם
        # EN: 'The All-Powerful who brought them out of Egypt is like the wakefulness of the wild ox, a protection over them; and He shall consume his enemies among the nations, and their bones He shall gnaw, and His arrows shall strike them down.'
        ("אֵל", "אלטאיק", "'The All-Powerful"),
        ("מוֹצִיאוֹ מִמִּצְרַיִם", "אלמכ'רגהם מן מצר", "who brought them out of Egypt"),
        ("כְּתוֹעֲפֹת רְאֵם", "כארק אלרים", "is like the wakefulness of the wild ox,"),
        ("לוֹ", "מאנע ענהם", "a protection over them;"),
        ("יֹאכַל", "והו יאכל", "and He shall consume"),
        ("גּוֹיִם צָרָיו", "אעדאיה מן אלאמם", "his enemies among the nations,"),
        ("וְעַצְמֹתֵיהֶם יְגָרֵם", "ועצ'אמהם ינהש", "and their bones He shall gnaw,"),
        ("וְחִצָּיו יִמְחָץ", "וסהאמה תדנפהם", "and His arrows shall strike them down.'"),
    ],
    9: [
        # HE: כָּרַע שָׁכַב כַּאֲרִי וּכְלָבִיא מִי יְקִימֶנּוּ מְבָרְכֶיךָ בָרוּךְ וְאֹרְרֶיךָ אָרוּר
        # JA: ואד'י גת'א ורבץ. פהו כאסד ולבו מן ד'א יתירה. מבארכך מבארך. ולאענך מלעון
        # EN: 'When he crouches and lies down, he is like a lion and a lioness — who shall rouse him? He who blesses you is blessed, and he who curses you is accursed.'
        (None, "ואד'י", "'When"),
        ("כָּרַע", "גת'א", "he crouches"),
        ("שָׁכַב", "ורבץ", "and lies down,"),
        ("כַּאֲרִי", "פהו כאסד", "he is like a lion"),
        ("וּכְלָבִיא", "ולבו", "and a lioness —"),
        ("מִי יְקִימֶנּוּ", "מן ד'א יתירה", "who shall rouse him?"),
        ("מְבָרְכֶיךָ בָרוּךְ", "מבארכך מבארך", "He who blesses you is blessed,"),
        ("וְאֹרְרֶיךָ אָרוּר", "ולאענך מלעון", "and he who curses you is accursed.'"),
    ],
    10: [
        # HE: וַיִּחַר-אַף בָּלָק אֶל-בִּלְעָם וַיִּסְפֹּק אֶת-כַּפָּיו וַיֹּאמֶר בָּלָק אֶל-בִּלְעָם לָקֹב אֹיְבַי קְרָאתִיךָ וְהִנֵּה בֵּרַכְתָּ בָרֵךְ זֶה שָׁלֹשׁ פְּעָמִים
        # JA: פאשתד ג'צ'ב בלק עלי' בלעם וספק כפיה חרדא. וקאל לה. אנמא דעותך לתסב אעדאי. פאד'א בך תבארך פיהם. הד'ה אלמרה אלת'אלת'ה
        # EN: And Balak's anger was greatly kindled against Balaam, and he clapped his two hands in fury, and said to him: 'I summoned you only to curse my enemies — and behold, you have blessed them altogether; this is the third time!'
        ("וַיִּחַר-אַף בָּלָק", "פאשתד ג'צ'ב בלק", "And Balak's anger was greatly kindled"),
        ("אֶל-בִּלְעָם", "עלי' בלעם", "against Balaam,"),
        ("וַיִּסְפֹּק אֶת-כַּפָּיו", "וספק כפיה", "and he clapped his two hands"),
        (None, "חרדא", "in fury,"),
        ("וַיֹּאמֶר", "וקאל", "and said"),
        ("בָּלָק אֶל-בִּלְעָם", "לה", "to him:"),
        ("לָקֹב אֹיְבַי", "אנמא דעותך לתסב אעדאי", "'I summoned you only to curse my enemies —"),
        ("וְהִנֵּה בֵּרַכְתָּ בָרֵךְ", "פאד'א בך תבארך פיהם", "and behold, you have blessed them altogether;"),
        ("זֶה שָׁלֹשׁ פְּעָמִים", "הד'ה אלמרה אלת'אלת'ה", "this is the third time!'"),
    ],
    11: [
        # HE: וְעַתָּה בְּרַח-לְךָ אֶל-מְקוֹמֶךָ אָמַרְתִּי כַּבֵּד אֲכַבֶּדְךָ וְהִנֵּה מְנָעֲךָ יְהוָה מִכָּבוֹד
        # JA: ואלאן פאנצרף אלי' מוצ'עך. לקד עזמת אן אכרמך. פמנעך אללה מן אלכראמה
        # EN: 'And now, depart to your place! I had resolved to honor you greatly, but God has withheld you from honor.'
        ("וְעַתָּה", "ואלאן", "'And now,"),
        ("בְּרַח-לְךָ", "פאנצרף", "depart"),
        ("אֶל-מְקוֹמֶךָ", "אלי' מוצ'עך", "to your place!"),
        ("אָמַרְתִּי", "לקד עזמת", "I had resolved"),
        ("כַּבֵּד אֲכַבֶּדְךָ", "אן אכרמך", "to honor you greatly,"),
        ("יְהוָה", "פמנעך אללה", "but God has withheld you"),
        ("מִכָּבוֹד", "מן אלכראמה", "from honor.'"),
    ],
    12: [
        # HE: וַיֹּאמֶר בִּלְעָם אֶל-בָּלָק הֲלֹא גַּם אֶל-מַלְאָכֶיךָ אֲשֶׁר-שָׁלַחְתָּ אֵלַי--דִּבַּרְתִּי לֵאמֹר
        # JA: קאל לה בלעם. אלם אקול לרסלך. אלד'י בעת'ת בהם אלי'י קאילא
        # EN: Balaam said to him: 'Did I not already say to your messengers whom you sent to me, saying:'
        ("וַיֹּאמֶר", "קאל לה", "Balaam said to him:"),
        ("בִּלְעָם", "בלעם", "'Did I not already say"),
        ("הֲלֹא גַּם", "אלם אקול", "to your messengers"),
        ("אֶל-מַלְאָכֶיךָ", "לרסלך", "whom"),
        ("אֲשֶׁר-שָׁלַחְתָּ", "אלד'י בעת'ת בהם", "you sent"),
        ("אֵלַי", "אלי'י", "to me,"),
        ("דִּבַּרְתִּי לֵאמֹר", "קאילא", "saying:'"),
    ],
    13: [
        # HE: אִם-יִתֶּן-לִי בָלָק מְלֹא בֵיתוֹ כֶּסֶף וְזָהָב--לֹא אוּכַל לַעֲבֹר אֶת-פִּי יְהוָה לַעֲשׂוֹת טוֹבָה אוֹ רָעָה מִלִּבִּי אֲשֶׁר-יְדַבֵּר יְהוָה אֹתוֹ אֲדַבֵּר
        # JA: לו אעטאני בלק. מל ביתה פצ'ה וד'הב. לא אסתטיע. אן אתגאוז אמר אללה. פאעמל גיידה או רדייה מן ראיי. אנמא אלד'י יקולה אללה אקולה פקט
        # EN: 'Were Balak to give me his house full of silver and gold, I could not transgress the command of God, to do good or evil of my own mind — only what God says shall I say, and nothing else.'
        ("אִם-יִתֶּן-לִי בָלָק", "לו אעטאני בלק", "'Were Balak to give me"),
        ("מְלֹא בֵיתוֹ", "מל ביתה", "his house full of"),
        ("כֶּסֶף", "פצ'ה", "silver"),
        ("וְזָהָב", "וד'הב", "and gold,"),
        ("לֹא אוּכַל", "לא אסתטיע", "I could not"),
        ("לַעֲבֹר אֶת-פִּי יְהוָה", "אן אתגאוז אמר אללה", "transgress the command of God,"),
        ("לַעֲשׂוֹת טוֹבָה", "פאעמל גיידה", "to do good"),
        ("אוֹ רָעָה", "או רדייה", "or evil"),
        ("מִלִּבִּי", "מן ראיי", "of my own mind —"),
        ("אֲשֶׁר-יְדַבֵּר יְהוָה", "אנמא אלד'י יקולה אללה", "only what God says"),
        ("אֹתוֹ אֲדַבֵּר", "אקולה פקט", "shall I say, and nothing else.'"),
    ],
    14: [
        # HE: וְעַתָּה הִנְנִי הוֹלֵךְ לְעַמִּי לְכָה אִיעָצְךָ אֲשֶׁר יַעֲשֶׂה הָעָם הַזֶּה לְעַמְּךָ בְּאַחֲרִית הַיָּמִים
        # JA: ואלאן. האנא מנצרף אלי' קומי. תעאל חתי' אערפך. מא יצנע הולאי אלקום. בקומך פי אכ'ר אלאייאם
        # EN: 'And now, here I am departing to my people. Come, so that I may inform you of what this people shall do to your people at the end of days.'
        ("וְעַתָּה", "ואלאן", "'And now,"),
        ("הִנְנִי הוֹלֵךְ", "האנא מנצרף", "here I am departing"),
        ("לְעַמִּי", "אלי' קומי", "to my people."),
        ("לְכָה", "תעאל", "Come,"),
        ("אִיעָצְךָ", "חתי' אערפך", "so that I may inform you"),
        ("אֲשֶׁר יַעֲשֶׂה", "מא יצנע", "of what"),
        ("הָעָם הַזֶּה", "הולאי אלקום", "this people shall do"),
        ("לְעַמְּךָ", "בקומך", "to your people"),
        ("בְּאַחֲרִית הַיָּמִים", "פי אכ'ר אלאייאם", "at the end of days.'"),
    ],
    15: [
        # HE: וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר נְאֻם בִּלְעָם בְּנוֹ בְעֹר וּנְאֻם הַגֶּבֶר שְׁתֻם הָעָיִן
        # JA: פצ'רב מת'לה וקאל. קל יא בלעם אבן בעור. וקל יא אייהא אלרגל אלחדיד אלבצר
        # EN: And he uttered his parable and said: 'Speak, O Balaam son of Beor! And speak, O man of sharp sight!'
        ("וַיִּשָּׂא מְשָׁלוֹ", "פצ'רב מת'לה", "And he uttered his parable"),
        ("וַיֹּאמַר", "וקאל", "and said:"),
        ("נְאֻם", "קל", "'Speak,"),
        (None, "יא", "O"),
        ("בִּלְעָם", "בלעם", "Balaam"),
        ("בְּנוֹ בְעֹר", "אבן בעור", "son of Beor!"),
        ("וּנְאֻם", "וקל", "And speak,"),
        ("הַגֶּבֶר", "אלרגל", "O man of"),
        ("שְׁתֻם הָעָיִן", "אלחדיד אלבצר", "sharp sight!'"),
    ],
    16: [
        # HE: נְאֻם שֹׁמֵעַ אִמְרֵי-אֵל וְיֹדֵעַ דַּעַת עֶלְיוֹן מַחֲזֵה שַׁדַּי יֶחֱזֶה נֹפֵל וּגְלוּי עֵינָיִם
        # JA: וקל יא סאמע אקואל אלטאיק. ועארף מערפה' אלעאלי'. ונאצ'ר מנאצ'ר אלכאפי. והו נאים והו מפתוח אלעין
        # EN: 'And speak, O hearer of the words of the All-Powerful, and knower of the knowledge of the Most High, and beholder of the visions of the All-Sufficient, who sleeps with open eyes!'
        ("נְאֻם", "וקל", "'And speak,"),
        ("שֹׁמֵעַ", "יא סאמע", "O hearer of"),
        ("אִמְרֵי-אֵל", "אקואל אלטאיק", "the words of the All-Powerful,"),
        ("וְיֹדֵעַ", "ועארף", "and knower of"),
        ("דַּעַת עֶלְיוֹן", "מערפה' אלעאלי'", "the knowledge of the Most High,"),
        ("מַחֲזֵה שַׁדַּי יֶחֱזֶה", "ונאצ'ר מנאצ'ר אלכאפי", "and beholder of the visions of the All-Sufficient,"),
        ("נֹפֵל", "והו נאים", "who sleeps"),
        ("וּגְלוּי עֵינָיִם", "והו מפתוח אלעין", "with open eyes!'"),
    ],
    17: [
        # HE: אֶרְאֶנּוּ וְלֹא עַתָּה אֲשׁוּרֶנּוּ וְלֹא קָרוֹב דָּרַךְ כּוֹכָב מִיַּעֲקֹב וְקָם שֵׁבֶט מִיִּשְׂרָאֵל וּמָחַץ פַּאֲתֵי מוֹאָב וְקַרְקַר כָּל-בְּנֵי-שֵׁת
        # JA: אמר אראה וליס הו אלאן. ואלמחה והו ג'יר קריב אן יטלע כוכב מן אל יעקוב. ויקום קצ'יב מן אל אסראיל. פיוהן גהאת מואב. ויזלזל סאיר בני שת
        # EN: 'A matter I see, though it is not now; and I perceive it, though it is not near — that a star shall rise from the house of Jacob, and a scepter-bearer shall arise from the house of Israel, and shall weaken the sides of Moab, and shall shake the rest of the sons of Shet.'
        ("אֶרְאֶנּוּ", "אמר אראה", "'A matter I see,"),
        ("וְלֹא עַתָּה", "וליס הו אלאן", "though it is not now;"),
        ("אֲשׁוּרֶנּוּ", "ואלמחה", "and I perceive it,"),
        ("וְלֹא קָרוֹב", "והו ג'יר קריב", "though it is not near —"),
        ("דָּרַךְ כּוֹכָב", "אן יטלע כוכב", "that a star shall rise"),
        ("מִיַּעֲקֹב", "מן אל יעקוב", "from the house of Jacob,"),
        ("וְקָם שֵׁבֶט", "ויקום קצ'יב", "and a scepter-bearer shall arise"),
        ("מִיִּשְׂרָאֵל", "מן אל אסראיל", "from the house of Israel,"),
        ("וּמָחַץ פַּאֲתֵי מוֹאָב", "פיוהן גהאת מואב", "and shall weaken the sides of Moab,"),
        ("וְקַרְקַר כָּל-בְּנֵי-שֵׁת", "ויזלזל סאיר בני שת", "and shall shake the rest of the sons of Shet.'"),
    ],
    18: [
        # HE: וְהָיָה אֱדוֹם יְרֵשָׁה וְהָיָה יְרֵשָׁה שֵׂעִיר--אֹיְבָיו וְיִשְׂרָאֵל עֹשֶׂה חָיִל
        # JA: וסיכון אדום מנקרצ'א. וכד'אלך שעיר וסאיר אעדאיה. ואסראיל יזתאד תאיידא
        # EN: 'And Edom shall be utterly destroyed, and likewise Seir and the rest of his enemies; and Israel shall grow in strength ever more.'
        ("וְהָיָה אֱדוֹם יְרֵשָׁה", "וסיכון אדום מנקרצ'א", "'And Edom shall be utterly destroyed,"),
        ("וְהָיָה יְרֵשָׁה שֵׂעִיר", "וכד'אלך שעיר", "and likewise Seir"),
        ("אֹיְבָיו", "וסאיר אעדאיה", "and the rest of his enemies;"),
        ("וְיִשְׂרָאֵל", "ואסראיל", "and Israel"),
        ("עֹשֶׂה חָיִל", "יזתאד תאיידא", "shall grow in strength ever more.'"),
    ],
    19: [
        # HE: וְיֵרְדְּ מִיַּעֲקֹב וְהֶאֱבִיד שָׂרִיד מֵעִיר
        # JA: ואלד'י יסתולי מן אל יעקוב. יביד אלשריד מן אלקרא
        # EN: 'And he who rules from the house of Jacob shall destroy the remnant from the towns.'
        ("וְיֵרְדְּ", "ואלד'י יסתולי", "'And he who rules"),
        ("מִיַּעֲקֹב", "מן אל יעקוב", "from the house of Jacob"),
        ("וְהֶאֱבִיד", "יביד", "shall destroy"),
        ("שָׂרִיד", "אלשריד", "the remnant"),
        ("מֵעִיר", "מן אלקרא", "from the towns.'"),
    ],
    20: [
        # HE: וַיַּרְא אֶת-עֲמָלֵק וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר רֵאשִׁית גּוֹיִם עֲמָלֵק וְאַחֲרִיתוֹ עֲדֵי אֹבֵד
        # JA: ת'ם ראא אלעמלקיין. פצ'רב מת'לה וקאל. אוול חרב אלאמם עמלק. ואכ'רתה אלי' אלאבאדה
        # EN: Then he saw the Amalekites, and uttered his parable and said: 'The first to make war among the nations was Amalek, and its end is unto destruction.'
        (None, "ת'ם", "Then"),
        ("וַיַּרְא", "ראא", "he saw"),
        ("אֶת-עֲמָלֵק", "אלעמלקיין", "the Amalekites,"),
        ("וַיִּשָּׂא מְשָׁלוֹ", "פצ'רב מת'לה", "and uttered his parable"),
        ("וַיֹּאמַר", "וקאל", "and said:"),
        ("רֵאשִׁית גּוֹיִם", "אוול חרב אלאמם", "'The first to make war among the nations"),
        ("עֲמָלֵק", "עמלק", "was Amalek,"),
        ("וְאַחֲרִיתוֹ", "ואכ'רתה", "and its end is"),
        ("עֲדֵי אֹבֵד", "אלי' אלאבאדה", "unto destruction.'"),
    ],
    21: [
        # HE: וַיַּרְא אֶת-הַקֵּינִי וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר אֵיתָן מוֹשָׁבֶךָ וְשִׂים בַּסֶּלַע קִנֶּךָ
        # JA: ת'ם ראא אלקיניין. פצ'רב מת'לה וקאל. סיכון מגלסך צלבא. ותצייר פי אלצכ'ר וכרך
        # EN: Then he saw the Kenites, and uttered his parable and said: 'Your seat shall be firm and strong, and you shall set your nest in the rock.'
        (None, "ת'ם", "Then"),
        ("וַיַּרְא", "ראא", "he saw"),
        ("אֶת-הַקֵּינִי", "אלקיניין", "the Kenites,"),
        ("וַיִּשָּׂא מְשָׁלוֹ", "פצ'רב מת'לה", "and uttered his parable"),
        ("וַיֹּאמַר", "וקאל", "and said:"),
        ("אֵיתָן מוֹשָׁבֶךָ", "סיכון מגלסך צלבא", "'Your seat shall be firm and strong,"),
        ("וְשִׂים בַּסֶּלַע", "ותצייר פי אלצכ'ר", "and you shall set your nest"),
        ("קִנֶּךָ", "וכרך", "in the rock.'"),
    ],
    22: [
        # HE: כִּי אִם-יִהְיֶה לְבָעֵר קָיִן--עַד-מָה אַשּׁוּר תִּשְׁבֶּךָּ
        # JA: ואד'א יכון וקת לנפי אלקיניין. פכם יסבי מנהם אלמוצליין
        # EN: 'Yet there shall come a time for the exile of the Kenites — how many of them shall the people of Mosul (Asshur) take captive!'
        (None, "ואד'א", "'Yet"),
        ("כִּי אִם-יִהְיֶה", "יכון", "there shall come"),
        (None, "וקת", "a time"),
        ("לְבָעֵר קָיִן", "לנפי אלקיניין", "for the exile of the Kenites —"),
        ("עַד-מָה", "פכם", "how many of them"),
        ("אַשּׁוּר תִּשְׁבֶּךָּ", "יסבי מנהם אלמוצליין", "shall the people of Mosul (Asshur) take captive!'"),
    ],
    23: [
        # HE: וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר אוֹי מִי יִחְיֶה מִשֻּׂמוֹ אֵל
        # JA: פצ'רב מת'לה וקאל. אלויל למן יחיא. אד'א ציירה אלטאיק
        # EN: And he uttered his parable and said: 'Woe to him who shall be alive when the All-Powerful has brought this upon him!'
        ("וַיִּשָּׂא מְשָׁלוֹ", "פצ'רב מת'לה", "And he uttered his parable"),
        ("וַיֹּאמַר", "וקאל", "and said:"),
        ("אוֹי", "אלויל", "'Woe"),
        ("מִי יִחְיֶה", "למן יחיא", "to him who shall be alive"),
        ("מִשֻּׂמוֹ אֵל", "אד'א ציירה אלטאיק", "when the All-Powerful has brought this upon him!'"),
    ],
    24: [
        # HE: וְצִים מִיַּד כִּתִּים וְעִנּוּ אַשּׁוּר וְעִנּוּ-עֵבֶר וְגַם-הוּא עֲדֵי אֹבֵד
        # JA: ואלדראמיין מן פרצ'ה' קברס. לתעד'ב אלמוצליין ואלעבריין. והם איצ'א אלי' אבאדה
        # EN: 'And the Dramians from the harbor of Cyprus shall afflict the people of Mosul and the Hebrews — and they too shall come to destruction.'
        ("וְצִים", "ואלדראמיין", "'And the Dramians"),
        ("מִיַּד כִּתִּים", "מן פרצ'ה' קברס", "from the harbor of Cyprus"),
        ("וְעִנּוּ אַשּׁוּר", "לתעד'ב אלמוצליין", "shall afflict the people of Mosul"),
        ("וְעִנּוּ-עֵבֶר", "ואלעבריין", "and the Hebrews —"),
        ("וְגַם-הוּא", "והם איצ'א", "and they too"),
        ("עֲדֵי אֹבֵד", "אלי' אבאדה", "shall come to destruction.'"),
    ],
    25: [
        # HE: וַיָּקָם בִּלְעָם וַיֵּלֶךְ וַיָּשָׁב לִמְקֹמוֹ וְגַם-בָּלָק הָלַךְ לְדַרְכּוֹ
        # JA: ת'ם קאם בלעם ומצ'א ורגע אלי' מוצ'עה. ובלק איצ'א מצ'א אלי' סבילה
        # EN: Then Balaam arose and departed and returned to his place; and Balak too went on his way.
        (None, "ת'ם", "Then"),
        ("וַיָּקָם", "קאם", "arose"),
        ("בִּלְעָם", "בלעם", "Balaam"),
        ("וַיֵּלֶךְ", "ומצ'א", "and departed"),
        ("וַיָּשָׁב", "ורגע", "and returned"),
        ("לִמְקֹמוֹ", "אלי' מוצ'עה", "to his place;"),
        ("וְגַם-בָּלָק", "ובלק איצ'א", "and Balak too"),
        ("הָלַךְ לְדַרְכּוֹ", "מצ'א אלי' סבילה", "went on his way."),
    ],
}

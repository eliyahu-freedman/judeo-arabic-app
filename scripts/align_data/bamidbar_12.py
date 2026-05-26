"""Hand-authored word-level alignment triples for Bamidbar chapter 12."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַתְּדַבֵּר מִרְיָם וְאַהֲרֹן בְּמֹשֶׁה עַל-אֹדוֹת הָאִשָּׁה הַכֻּשִׁית אֲשֶׁר לָקָח כִּי-אִשָּׁה כֻשִׁית לָקָח
        # JA: תכלמת מרים והרון במוסי. בסבב אלאמראה אלחסנה אלתי תזווגהא. לאנה כאן קד אעתזלהא
        # EN: Miriam and Aaron spoke against Moses on account of the fair woman whom he had married, for he had kept himself apart from her.
        ("וַתְּדַבֵּר", "תכלמת", "spoke against"),
        ("מִרְיָם", "מרים", "Miriam"),
        ("וְאַהֲרֹן", "והרון", "and Aaron"),
        ("בְּמֹשֶׁה", "במוסי.", "Moses"),
        ("עַל-אֹדוֹת", "בסבב", "on account of"),
        ("הָאִשָּׁה", "אלאמראה", "the fair woman"),
        ("הַכֻּשִׁית", "אלחסנה", "whom"),
        ("אֲשֶׁר לָקָח", "אלתי תזווגהא.", "he had married,"),
        ("כִּי-אִשָּׁה כֻשִׁית לָקָח", "לאנה כאן קד אעתזלהא", "for he had kept himself apart from her."),
    ],
    2: [
        # HE: וַיֹּאמְרוּ הֲרַק אַךְ-בְּמֹשֶׁה דִּבֶּר יְהוָה--הֲלֹא גַּם-בָּנוּ דִבֵּר וַיִּשְׁמַע יְהוָה
        # JA: פקאלו. אן כאן מן אגל אלנבווה פתראה וחדה פקט כ'אטבה אללה. אליס קד כ'אטבנא אללה איצ'א. פסמע אללה ד'אלך
        # EN: And they said: 'If it be on account of prophecy — was it only he alone whom God addressed? Has God not addressed us as well?' And God heard that.
        ("וַיֹּאמְרוּ", "פקאלו.", "And they said:"),
        (None, "אן כאן", "If it be"),
        ("הֲרַק", "מן אגל", "on account of"),
        ("אַךְ-בְּמֹשֶׁה", "אלנבווה", "prophecy —"),
        ("דִּבֶּר", "פתראה", "was it only"),
        ("יְהוָה", "וחדה פקט", "he alone"),
        (None, "כ'אטבה", "whom"),
        (None, "אללה.", "God addressed?"),
        ("הֲלֹא גַּם-בָּנוּ", "אליס קד כ'אטבנא", "Has God not addressed us"),
        ("דִבֵּר", "אללה איצ'א.", "as well?'"),
        ("וַיִּשְׁמַע יְהוָה", "פסמע אללה ד'אלך", "And God heard that."),
    ],
    3: [
        # HE: וְהָאִישׁ מֹשֶׁה עָנָו מְאֹד--מִכֹּל הָאָדָם אֲשֶׁר עַל-פְּנֵי הָאֲדָמָה
        # JA: וכאן מוסי' רגלא כ'אשעא גדא. אכת'ר מן גמיע אלנאס. אלד'י עלי' וגה אלארץ'
        # EN: Now Moses was a man exceedingly humble — more than all the people who are upon the face of the earth.
        (None, "וכאן", "Now"),
        ("מֹשֶׁה", "מוסי'", "Moses"),
        ("וְהָאִישׁ", "רגלא", "was a man"),
        ("עָנָו", "כ'אשעא", "exceedingly humble"),
        ("מְאֹד", "גדא.", "—"),
        ("מִכֹּל", "אכת'ר מן", "more than"),
        ("הָאָדָם", "גמיע אלנאס.", "all the people"),
        ("אֲשֶׁר עַל-פְּנֵי", "אלד'י עלי' וגה", "who are upon the face of"),
        ("הָאֲדָמָה", "אלארץ'", "the earth."),
    ],
    4: [
        # HE: וַיֹּאמֶר יְהוָה פִּתְאֹם אֶל-מֹשֶׁה וְאֶל-אַהֲרֹן וְאֶל-מִרְיָם צְאוּ שְׁלָשְׁתְּכֶם אֶל-אֹהֶל מוֹעֵד וַיֵּצְאוּ שְׁלָשְׁתָּם
        # JA: פקאל אללה ג'פלה. למוסי והרון ומרים. אכ'רגו ת'לאת'תכם אלי' כ'בא אלמחצ'ר. פכ'רגו ת'לאת'תהם
        # EN: And God said suddenly to Moses and Aaron and Miriam: 'Come out, the three of you, to the tent of the assembly.' And the three of them came out.
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("פִּתְאֹם", "ג'פלה.", "suddenly"),
        ("אֶל-מֹשֶׁה", "למוסי", "to Moses"),
        ("וְאֶל-אַהֲרֹן", "והרון", "and Aaron"),
        ("וְאֶל-מִרְיָם", "ומרים.", "and Miriam:"),
        ("צְאוּ", "אכ'רגו", "'Come out,"),
        ("שְׁלָשְׁתְּכֶם", "ת'לאת'תכם", "the three of you,"),
        ("אֶל-אֹהֶל מוֹעֵד", "אלי' כ'בא אלמחצ'ר.", "to the tent of the assembly.'"),
        ("וַיֵּצְאוּ", "פכ'רגו", "And the three of them"),
        ("שְׁלָשְׁתָּם", "ת'לאת'תהם", "came out."),
    ],
    5: [
        # HE: וַיֵּרֶד יְהוָה בְּעַמּוּד עָנָן וַיַּעֲמֹד פֶּתַח הָאֹהֶל וַיִּקְרָא אַהֲרֹן וּמִרְיָם וַיֵּצְאוּ שְׁנֵיהֶם
        # JA: פתגלא אללה בעמוד ג'מאם. וקאם עלי' באב אלכ'בא. ונאדא יא הרון ויא מרים. פכ'רגא כליהמא
        # EN: And God appeared in a pillar of cloud, and stood at the door of the tent, and called: 'O Aaron, and O Miriam!' And the two of them came out.
        ("וַיֵּרֶד יְהוָה", "פתגלא אללה", "And God appeared"),
        ("בְּעַמּוּד", "בעמוד", "in a pillar of"),
        ("עָנָן", "ג'מאם.", "cloud,"),
        ("וַיַּעֲמֹד", "וקאם עלי'", "and stood at"),
        ("פֶּתַח הָאֹהֶל", "באב אלכ'בא.", "the door of the tent,"),
        ("וַיִּקְרָא", "ונאדא", "and called:"),
        ("אַהֲרֹן", "יא הרון", "'O Aaron,"),
        ("וּמִרְיָם", "ויא מרים.", "and O Miriam!'"),
        ("וַיֵּצְאוּ", "פכ'רגא", "And the two of them"),
        ("שְׁנֵיהֶם", "כליהמא", "came out."),
    ],
    6: [
        # HE: וַיֹּאמֶר שִׁמְעוּ-נָא דְבָרָי אִם-יִהְיֶה נְבִיאֲכֶם--יְהוָה בַּמַּרְאָה אֵלָיו אֶתְוַדָּע בַּחֲלוֹם אֲדַבֶּר-בּוֹ
        # JA: קאל אסמעו כלאמי. אן יכון נבייכמא. אנא אללה תערפת בה פי רויא . או כ'אטבתה פי חלם
        # EN: He said: 'Hear my words. If there be a prophet among you — I, God, make Myself known to him in a vision, or I speak to him in a dream.
        ("וַיֹּאמֶר", "קאל", "He said:"),
        ("שִׁמְעוּ-נָא", "אסמעו", "'Hear"),
        ("דְבָרָי", "כלאמי.", "my words."),
        ("אִם-יִהְיֶה", "אן יכון", "If there be"),
        ("נְבִיאֲכֶם", "נבייכמא.", "a prophet among you —"),
        (None, "אנא", "I,"),
        ("יְהוָה", "אללה", "God,"),
        ("אֶתְוַדָּע", "תערפת בה", "make Myself known to him"),
        ("בַּמַּרְאָה", "פי רויא .", "in a vision,"),
        ("בַּחֲלוֹם", "או כ'אטבתה פי חלם", "or I speak to him in a dream."),
    ],
    7: [
        # HE: לֹא-כֵן עַבְדִּי מֹשֶׁה בְּכָל-בֵּיתִי נֶאֱמָן הוּא
        # JA: ליס כד'אך עבדי מוסי'. בל פי גמיע אמתי מחקק הו
        # EN: Not so My servant Moses — rather, throughout all My nation he is trusted.
        ("לֹא-כֵן", "ליס כד'אך", "Not so"),
        ("עַבְדִּי", "עבדי", "My servant"),
        ("מֹשֶׁה", "מוסי'.", "Moses —"),
        (None, "בל", "rather,"),
        ("בְּכָל-בֵּיתִי", "פי גמיע אמתי", "throughout all My nation"),
        ("נֶאֱמָן הוּא", "מחקק הו", "he is trusted."),
    ],
    8: [
        # HE: פֶּה אֶל-פֶּה אֲדַבֶּר-בּוֹ וּמַרְאֶה וְלֹא בְחִידֹת וּתְמֻנַת יְהוָה יַבִּיט וּמַדּוּעַ לֹא יְרֵאתֶם לְדַבֵּר בְּעַבְדִּי בְמֹשֶׁה
        # JA: אן שפאהא אכ'אטבה. ורויא ולא באחאדית וצוור אללה אלמכ'לוקה לה יראהא. ומא באלכמא לם תכ'אפא. אן תתכלמא פי עבדי מוסי'
        # EN: Mouth to mouth I address him, and by vision and not in riddles; and the created forms of God appointed for him — he beholds them. Why then were the two of you not afraid to speak against My servant Moses?'
        ("פֶּה אֶל-פֶּה", "אן שפאהא", "Mouth to mouth"),
        ("אֲדַבֶּר-בּוֹ", "אכ'אטבה.", "I address him,"),
        ("וּמַרְאֶה", "ורויא", "and by vision"),
        ("וְלֹא בְחִידֹת", "ולא באחאדית", "and not in riddles;"),
        ("וּתְמֻנַת יְהוָה", "וצוור אללה", "and the created forms of God"),
        ("יַבִּיט", "אלמכ'לוקה לה יראהא.", "appointed for him — he beholds them."),
        ("וּמַדּוּעַ", "ומא באלכמא", "Why then"),
        ("לֹא יְרֵאתֶם", "לם תכ'אפא.", "were the two of you not afraid"),
        ("לְדַבֵּר", "אן תתכלמא", "to speak"),
        ("בְּעַבְדִּי", "פי עבדי", "against My servant"),
        ("בְמֹשֶׁה", "מוסי'", "Moses?'"),
    ],
    9: [
        # HE: וַיִּחַר-אַף יְהוָה בָּם וַיֵּלַךְ
        # JA: פאשתד ג'צ'ב אללה עליהם. וארתפע נורה
        # EN: And God's anger intensified against them, and His light ascended.
        ("וַיִּחַר-אַף יְהוָה", "פאשתד ג'צ'ב אללה", "And God's anger intensified"),
        ("בָּם", "עליהם.", "against them,"),
        ("וַיֵּלַךְ", "וארתפע נורה", "and His light ascended."),
    ],
    10: [
        # HE: וְהֶעָנָן סָר מֵעַל הָאֹהֶל וְהִנֵּה מִרְיָם מְצֹרַעַת כַּשָּׁלֶג וַיִּפֶן אַהֲרֹן אֶל-מִרְיָם וְהִנֵּה מְצֹרָעַת
        # JA: פכמא זאל אלג'מאם ען אלכ'בא. פאדא במרים ביצ'א כאלתלג. פלמא אלתפת הרון. אלי' מרים פאד'א בהא ברצא
        # EN: And as the cloud withdrew from the tent, behold — Miriam was white as snow. And when Aaron turned toward Miriam, behold, she was stricken with a skin-affliction.
        ("וְהֶעָנָן", "פכמא זאל אלג'מאם", "And as the cloud withdrew"),
        ("סָר מֵעַל הָאֹהֶל", "ען אלכ'בא.", "from the tent,"),
        ("וְהִנֵּה", "פאדא", "behold —"),
        ("מִרְיָם", "במרים", "Miriam"),
        ("מְצֹרַעַת", "ביצ'א", "was white"),
        ("כַּשָּׁלֶג", "כאלתלג.", "as snow."),
        ("וַיִּפֶן", "פלמא אלתפת", "And when"),
        ("אַהֲרֹן", "הרון.", "Aaron turned"),
        ("אֶל-מִרְיָם", "אלי' מרים", "toward Miriam,"),
        ("וְהִנֵּה מְצֹרָעַת", "פאד'א בהא ברצא", "behold, she was stricken with a skin-affliction."),
    ],
    11: [
        # HE: וַיֹּאמֶר אַהֲרֹן אֶל-מֹשֶׁה בִּי אֲדֹנִי--אַל-נָא תָשֵׁת עָלֵינוּ חַטָּאת אֲשֶׁר נוֹאַלְנוּ וַאֲשֶׁר חָטָאנוּ
        # JA: פקאל הרון למוסי'. יא סיידי. לא תגעל עלינא כ'טייה. פי מא גהלנא ואכ'טינא
        # EN: And Aaron said to Moses: 'O my lord, do not lay a sin upon us for what we did in our ignorance and in our error.
        ("וַיֹּאמֶר אַהֲרֹן", "פקאל הרון", "And Aaron said"),
        ("אֶל-מֹשֶׁה", "למוסי'.", "to Moses:"),
        ("בִּי אֲדֹנִי", "יא סיידי.", "'O my lord,"),
        ("אַל-נָא תָשֵׁת", "לא תגעל", "do not lay"),
        ("עָלֵינוּ", "עלינא", "a sin upon us"),
        ("חַטָּאת", "כ'טייה.", "for what we did"),
        ("אֲשֶׁר נוֹאַלְנוּ", "פי מא גהלנא", "in our ignorance"),
        ("וַאֲשֶׁר חָטָאנוּ", "ואכ'טינא", "and in our error."),
    ],
    12: [
        # HE: אַל-נָא תְהִי כַּמֵּת אֲשֶׁר בְּצֵאתוֹ מֵרֶחֶם אִמּוֹ וַיֵּאָכֵל חֲצִי בְשָׂרוֹ
        # JA: לא תכון הד'ה כסקט כ'רג מן בטן אמה. וקד תהרא נצף גסמה
        # EN: Let her not be like a stillborn that comes out from its mother's womb with half its body already wasted away.'
        ("אַל-נָא תְהִי", "לא תכון", "Let her not be"),
        ("כַּמֵּת", "הד'ה כסקט", "like a stillborn"),
        ("אֲשֶׁר בְּצֵאתוֹ", "כ'רג", "that comes out"),
        ("מֵרֶחֶם", "מן בטן", "from its mother's"),
        ("אִמּוֹ", "אמה.", "womb"),
        ("וַיֵּאָכֵל", "וקד תהרא", "with half its body already"),
        ("חֲצִי בְשָׂרוֹ", "נצף גסמה", "wasted away.'"),
    ],
    13: [
        # HE: וַיִּצְעַק מֹשֶׁה אֶל-יְהוָה לֵאמֹר אֵל נָא רְפָא נָא לָהּ
        # JA: פדעא מוסי'. אלי' רבה קאילא. אללהם פאשפהא
        # EN: And Moses cried out to his Lord, saying: 'O God, heal her, I pray!'
        ("וַיִּצְעַק מֹשֶׁה", "פדעא מוסי'.", "And Moses cried out"),
        ("אֶל-יְהוָה", "אלי' רבה", "to his Lord,"),
        ("לֵאמֹר", "קאילא.", "saying:"),
        ("אֵל נָא", "אללהם", "'O God, heal her,"),
        ("רְפָא נָא לָהּ", "פאשפהא", "I pray!'"),
    ],
    14: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה וְאָבִיהָ יָרֹק יָרַק בְּפָנֶיהָ--הֲלֹא תִכָּלֵם שִׁבְעַת יָמִים תִּסָּגֵר שִׁבְעַת יָמִים מִחוּץ לַמַּחֲנֶה וְאַחַר תֵּאָסֵף
        # JA: פקאל אללה למוסי . לו אן אביהא בצק פי וגההא. אלם יגב אן תסתחי מנה סבעה' אייאם. פלתקף כד'אך כ'ארג אלעסכר. ובעד ד'אלך תנצ'ם אליה
        # EN: And God said to Moses: 'Were her father to spit in her face, would she not be obliged to feel shame before him for seven days? Let her remain thus outside the camp, and after that she shall rejoin it.'
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי .", "to Moses:"),
        ("וְאָבִיהָ", "לו אן אביהא", "'Were her father"),
        ("יָרֹק יָרַק", "בצק", "to spit"),
        ("בְּפָנֶיהָ", "פי וגההא.", "in her face,"),
        ("הֲלֹא תִכָּלֵם", "אלם יגב אן תסתחי מנה", "would she not be obliged to feel shame before him"),
        ("שִׁבְעַת יָמִים", "סבעה' אייאם.", "for seven days?"),
        ("תִּסָּגֵר", "פלתקף", "Let her remain"),
        (None, "כד'אך", "thus"),
        ("מִחוּץ לַמַּחֲנֶה", "כ'ארג אלעסכר.", "outside the camp,"),
        ("וְאַחַר", "ובעד ד'אלך", "and after that"),
        ("תֵּאָסֵף", "תנצ'ם אליה", "she shall rejoin it.'"),
    ],
    15: [
        # HE: וַתִּסָּגֵר מִרְיָם מִחוּץ לַמַּחֲנֶה שִׁבְעַת יָמִים וְהָעָם לֹא נָסַע עַד-הֵאָסֵף מִרְיָם
        # JA: פוקפת מרים. כ'ארג אלעסכר סבעה' אייאם. ולם ירחל אלקום. אלי' אנצ'מאמהא
        # EN: And Miriam remained outside the camp for seven days; and the people did not set out until she had rejoined.
        ("וַתִּסָּגֵר", "פוקפת", "And Miriam remained"),
        ("מִרְיָם", "מרים.", "outside"),
        ("מִחוּץ לַמַּחֲנֶה", "כ'ארג אלעסכר", "the camp"),
        ("שִׁבְעַת יָמִים", "סבעה' אייאם.", "for seven days;"),
        ("וְהָעָם", "ולם ירחל אלקום.", "and the people did not set out"),
        ("לֹא נָסַע", "אלי'", "until"),
        ("עַד-הֵאָסֵף מִרְיָם", "אנצ'מאמהא", "she had rejoined."),
    ],
    16: [
        # HE: וְאַחַר נָסְעוּ הָעָם מֵחֲצֵרוֹת וַיַּחֲנוּ בְּמִדְבַּר פָּארָן
        # JA: ובעד ד'אלך רחלו מן חצרות. ונזלו פי ברייה' פארן
        # EN: And after that they set out from Hazeroth, and encamped in the wilderness of Paran.
        ("וְאַחַר", "ובעד ד'אלך", "And after that"),
        ("נָסְעוּ", "רחלו", "they set out"),
        ("הָעָם מֵחֲצֵרוֹת", "מן חצרות.", "from Hazeroth,"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּמִדְבַּר", "פי ברייה'", "in the wilderness of"),
        ("פָּארָן", "פארן", "Paran."),
    ],
}

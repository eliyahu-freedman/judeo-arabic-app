"""Hand-authored word-level alignment triples for Bamidbar chapter 20."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיָּבֹאוּ בְנֵי-יִשְׂרָאֵל כָּל-הָעֵדָה מִדְבַּר-צִן בַּחֹדֶשׁ הָרִאשׁוֹן וַיֵּשֶׁב הָעָם בְּקָדֵשׁ וַתָּמָת שָׁם מִרְיָם וַתִּקָּבֵר שָׁם
        # JA: ת'ם גאו בני אסראיל אגמעין. אלי' ברייה' צין פי אלשהר אלאוול. ואקאם אלקום פי רקים. ומאתת הנאך מרים. ודפנת ת'ם
        # EN: Then the sons of Israel, all of them, came to the wilderness of Zin in the first month; and the people settled in Raqim. And Miriam died there, and was buried there.
        (None, "ת'ם", "Then"),
        ("וַיָּבֹאוּ", "גאו", "came"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("כָּל-הָעֵדָה", "אגמעין", "all of them,"),
        ("מִדְבַּר-צִן", "אלי' ברייה' צין", "to the wilderness of Zin"),
        ("בַּחֹדֶשׁ הָרִאשׁוֹן", "פי אלשהר אלאוול", "in the first month;"),
        ("וַיֵּשֶׁב הָעָם", "ואקאם אלקום", "and the people settled"),
        ("בְּקָדֵשׁ", "פי רקים", "in Raqim."),
        ("וַתָּמָת", "ומאתת", "And Miriam died"),
        ("שָׁם מִרְיָם", "הנאך מרים", "there,"),
        ("וַתִּקָּבֵר שָׁם", "ודפנת ת'ם", "and was buried there."),
    ],
    2: [
        # HE: וְלֹא-הָיָה מַיִם לָעֵדָה וַיִּקָּהֲלוּ עַל-מֹשֶׁה וְעַל-אַהֲרֹן
        # JA: ולם יכון מאא לאלגמאעה. פתגווקו עלי' מוסי' והרון
        # EN: And there was no water for the congregation; and they assembled against Moses and Aaron.
        ("וְלֹא-הָיָה", "ולם יכון", "And there was no"),
        ("מַיִם", "מאא", "water"),
        ("לָעֵדָה", "לאלגמאעה", "for the congregation;"),
        ("וַיִּקָּהֲלוּ", "פתגווקו", "and they assembled"),
        ("עַל-מֹשֶׁה", "עלי' מוסי'", "against Moses"),
        ("וְעַל-אַהֲרֹן", "והרון", "and Aaron."),
    ],
    3: [
        # HE: וַיָּרֶב הָעָם עִם-מֹשֶׁה וַיֹּאמְרוּ לֵאמֹר וְלוּ גָוַעְנוּ בִּגְוַע אַחֵינוּ לִפְנֵי יְהוָה
        # JA: פלמא כ'אצם אלקום מוסי'. וקאלו. יא ליתנא תופינא. בופאה' אכ'ותנא בין ידי אללה
        # EN: And when the people quarreled with Moses, they said: 'Would that we had perished at the death of our brothers before God!'
        ("וַיָּרֶב", "פלמא כ'אצם", "And when the people quarreled"),
        ("הָעָם", "אלקום", "with"),
        ("עִם-מֹשֶׁה", "מוסי'", "Moses,"),
        ("וַיֹּאמְרוּ", "וקאלו", "they said:"),
        (None, "יא ליתנא", "'Would that"),
        ("וְלוּ גָוַעְנוּ", "תופינא", "we had perished"),
        ("בִּגְוַע", "בופאה'", "at the death of"),
        ("אַחֵינוּ", "אכ'ותנא", "our brothers"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God!'"),
    ],
    4: [
        # HE: וְלָמָה הֲבֵאתֶם אֶת-קְהַל יְהוָה אֶל-הַמִּדְבָּר הַזֶּה לָמוּת שָׁם אֲנַחְנוּ וּבְעִירֵנוּ
        # JA: ולם גיתמא בגוק אללה. אלי' הד'א אלבר. נמות פיה. נחן ובהאימנא
        # EN: 'And why have you two brought the congregation of God to this desolate wilderness, that we should die in it — we and our beasts?'
        ("וְלָמָה", "ולם", "'And why"),
        ("הֲבֵאתֶם", "גיתמא", "have you two brought"),
        ("אֶת-קְהַל יְהוָה", "בגוק אללה", "the congregation of God"),
        ("אֶל-הַמִּדְבָּר הַזֶּה", "אלי' הד'א אלבר", "to this desolate wilderness,"),
        ("לָמוּת", "נמות", "that we should die"),
        ("שָׁם", "פיה", "in it —"),
        ("אֲנַחְנוּ", "נחן", "we"),
        ("וּבְעִירֵנוּ", "ובהאימנא", "and our beasts?'"),
    ],
    5: [
        # HE: וְלָמָה הֶעֱלִיתֻנוּ מִמִּצְרַיִם לְהָבִיא אֹתָנוּ אֶל-הַמָּקוֹם הָרָע הַזֶּה לֹא מְקוֹם זֶרַע וּתְאֵנָה וְגֶפֶן וְרִמּוֹן וּמַיִם אַיִן לִשְׁתּוֹת
        # JA: ולם אצעדתמונא מן מצר פגיתם בנא. אלי' הד'א אלמוצ'ע אלרדי לא זרע ולא תין. ולא גפן ולא רמאן. חתי' מאא ליס לאלשרב
        # EN: 'And why have you two brought us up from Egypt, and led us to this wretched place — no sown crop, and no figs, and no vines, and no pomegranates; and there is not even water to drink.'
        ("וְלָמָה הֶעֱלִיתֻנוּ", "ולם אצעדתמונא", "'And why have you two brought us up"),
        ("מִמִּצְרַיִם", "מן מצר", "from Egypt,"),
        ("לְהָבִיא אֹתָנוּ", "פגיתם בנא", "and led us"),
        ("אֶל-הַמָּקוֹם הָרָע הַזֶּה", "אלי' הד'א אלמוצ'ע אלרדי", "to this wretched place —"),
        ("לֹא מְקוֹם זֶרַע", "לא זרע", "no sown crop,"),
        ("וּתְאֵנָה", "ולא תין", "and no figs,"),
        ("וְגֶפֶן", "ולא גפן", "and no vines,"),
        ("וְרִמּוֹן", "ולא רמאן", "and no pomegranates;"),
        ("וּמַיִם אַיִן", "חתי' מאא ליס", "and there is not even water"),
        ("לִשְׁתּוֹת", "לאלשרב", "to drink.'"),
    ],
    6: [
        # HE: וַיָּבֹא מֹשֶׁה וְאַהֲרֹן מִפְּנֵי הַקָּהָל אֶל-פֶּתַח אֹהֶל מוֹעֵד וַיִּפְּלוּ עַל-פְּנֵיהֶם וַיֵּרָא כְבוֹד-יְהוָה אֲלֵיהֶם
        # JA: פאקבל מוסי' והרון הארבין. מן בין ידי אלגוק. אלי' באב כ'בא אלמחצ'ר. פוקעא עלי' וגוההמא. פצ'הר נור אללה להמא
        # EN: And Moses and Aaron came fleeing from before the congregation to the entrance of the tent of the assembly; and the two of them fell upon their faces. And the light of God appeared to them.
        ("וַיָּבֹא מֹשֶׁה וְאַהֲרֹן", "פאקבל מוסי' והרון", "And Moses and Aaron came"),
        (None, "הארבין", "fleeing"),
        ("מִפְּנֵי הַקָּהָל", "מן בין ידי אלגוק", "from before the congregation"),
        ("אֶל-פֶּתַח", "אלי' באב", "to the entrance of"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of the assembly;"),
        ("וַיִּפְּלוּ", "פוקעא", "and the two of them fell"),
        ("עַל-פְּנֵיהֶם", "עלי' וגוההמא", "upon their faces."),
        ("וַיֵּרָא כְבוֹד-יְהוָה", "פצ'הר נור אללה", "And the light of God appeared"),
        ("אֲלֵיהֶם", "להמא", "to them."),
    ],
    7: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses with speech.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר", "כלם", "spoke"),
        ("יְהוָה", "אללה", "God"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "with speech."),
    ],
    8: [
        # HE: קַח אֶת-הַמַּטֶּה וְהַקְהֵל אֶת-הָעֵדָה אַתָּה וְאַהֲרֹן אָחִיךָ וְדִבַּרְתֶּם אֶל-הַסֶּלַע לְעֵינֵיהֶם וְנָתַן מֵימָיו וְהוֹצֵאתָ לָהֶם מַיִם מִן-הַסֶּלַע וְהִשְׁקִיתָ אֶת-הָעֵדָה וְאֶת-בְּעִירָם
        # JA: כ'ד' אלעצא. וגווק אלגמאעה אנת והרון אכ'יך. וקולא עלי' אלצכר בחצ'רתהם ויכ'רג מאה. פתכ'רג להם מאא מן אלצכר. אסקיהם ובהאימהם
        # EN: 'Take the staff, and assemble the congregation — you and Aaron your brother — and speak to the rock in their presence, and it will yield its water; so you shall bring forth for them water from the rock. Give them and their beasts to drink.'
        ("קַח", "כ'ד'", "'Take"),
        ("אֶת-הַמַּטֶּה", "אלעצא", "the staff,"),
        ("וְהַקְהֵל", "וגווק", "and assemble"),
        ("אֶת-הָעֵדָה", "אלגמאעה", "the congregation —"),
        ("אַתָּה", "אנת", "you"),
        ("וְאַהֲרֹן אָחִיךָ", "והרון אכ'יך", "and Aaron your brother —"),
        ("וְדִבַּרְתֶּם", "וקולא", "and speak"),
        ("אֶל-הַסֶּלַע", "עלי' אלצכר", "to the rock"),
        ("לְעֵינֵיהֶם", "בחצ'רתהם", "in their presence,"),
        ("וְנָתַן מֵימָיו", "ויכ'רג מאה", "and it will yield its water;"),
        ("וְהוֹצֵאתָ לָהֶם", "פתכ'רג להם", "so you shall bring forth for them"),
        ("מַיִם מִן-הַסֶּלַע", "מאא מן אלצכר", "water from the rock."),
        ("וְהִשְׁקִיתָ", "אסקיהם", "Give them"),
        ("אֶת-בְּעִירָם", "ובהאימהם", "and their beasts to drink.'"),
    ],
    9: [
        # HE: וַיִּקַּח מֹשֶׁה אֶת-הַמַּטֶּה מִלִּפְנֵי יְהוָה כַּאֲשֶׁר צִוָּהוּ
        # JA: פאכ'ד' מוסי'. אלעצא מן בין ידי אללה. כמא אמרה
        # EN: And Moses took the staff from before God, as He had commanded him.
        ("וַיִּקַּח מֹשֶׁה", "פאכ'ד' מוסי'", "And Moses took"),
        ("אֶת-הַמַּטֶּה", "אלעצא", "the staff"),
        ("מִלִּפְנֵי יְהוָה", "מן בין ידי אללה", "from before God,"),
        ("כַּאֲשֶׁר צִוָּהוּ", "כמא אמרה", "as He had commanded him."),
    ],
    10: [
        # HE: וַיַּקְהִלוּ מֹשֶׁה וְאַהֲרֹן אֶת-הַקָּהָל--אֶל-פְּנֵי הַסָּלַע וַיֹּאמֶר לָהֶם שִׁמְעוּ-נָא הַמֹּרִים--הֲמִן-הַסֶּלַע הַזֶּה נוֹצִיא לָכֶם מָיִם
        # JA: וגווקו מוסי' והרון. אלגוק אלי' חצ'רה' אלצכר. וקאל להם. אסמעו יא עצאה. אמן הד'א אלצכר. נכ'רג לכם מאא
        # EN: And Moses and Aaron assembled the congregation before the rock; and he said to them: 'Hear, O rebels — shall we bring out water for you from this rock?'
        ("וַיַּקְהִלוּ", "וגווקו", "And Moses and Aaron assembled"),
        ("מֹשֶׁה וְאַהֲרֹן", "מוסי' והרון", "the congregation"),
        ("אֶת-הַקָּהָל", "אלגוק", "before"),
        ("אֶל-פְּנֵי הַסָּלַע", "אלי' חצ'רה' אלצכר", "the rock;"),
        ("וַיֹּאמֶר לָהֶם", "וקאל להם", "and he said to them:"),
        ("שִׁמְעוּ-נָא", "אסמעו", "'Hear,"),
        ("הַמֹּרִים", "יא עצאה", "O rebels —"),
        ("הֲמִן-הַסֶּלַע הַזֶּה", "אמן הד'א אלצכר", "shall we bring out water for you"),
        ("נוֹצִיא לָכֶם מָיִם", "נכ'רג לכם מאא", "from this rock?'"),
    ],
    11: [
        # HE: וַיָּרֶם מֹשֶׁה אֶת-יָדוֹ וַיַּךְ אֶת-הַסֶּלַע בְּמַטֵּהוּ--פַּעֲמָיִם וַיֵּצְאוּ מַיִם רַבִּים וַתֵּשְׁתְּ הָעֵדָה וּבְעִירָם
        # JA: פרפע ידה. וצ'רב אלצכר בעצאה מרתין. פכ'רג מא כת'יר. ושרבת מנה אלגמאעה ובהאימהם
        # EN: And he raised his hand, and struck the rock with his staff twice; and much water came out, and the congregation and their beasts drank from it.
        ("וַיָּרֶם", "פרפע", "And he raised"),
        ("אֶת-יָדוֹ", "ידה", "his hand,"),
        ("וַיַּךְ", "וצ'רב", "and struck"),
        ("אֶת-הַסֶּלַע", "אלצכר", "the rock"),
        ("בְּמַטֵּהוּ", "בעצאה", "with his staff"),
        ("פַּעֲמָיִם", "מרתין", "twice;"),
        ("וַיֵּצְאוּ מַיִם רַבִּים", "פכ'רג מא כת'יר", "and much water came out,"),
        ("וַתֵּשְׁתְּ הָעֵדָה", "ושרבת מנה אלגמאעה", "and the congregation"),
        ("וּבְעִירָם", "ובהאימהם", "and their beasts drank from it."),
    ],
    12: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה וְאֶל-אַהֲרֹן יַעַן לֹא-הֶאֱמַנְתֶּם בִּי לְהַקְדִּישֵׁנִי לְעֵינֵי בְּנֵי יִשְׂרָאֵל--לָכֵן לֹא תָבִיאוּ אֶת-הַקָּהָל הַזֶּה אֶל-הָאָרֶץ אֲשֶׁר-נָתַתִּי לָהֶם
        # JA: פקאל אללה למוסי' והרון. כמא לם תומנוהם בי. ותקדסוני בחצ'רה' בני אסראיל. כד'אך לא תדכ'לא הד'א אלגוק. אלי' אלבלד אלד'י אעטיתהם
        # EN: And God said to Moses and Aaron: 'Just as you did not make them trust in Me, and sanctify Me in the presence of the sons of Israel — so shall you two not bring this congregation into the land which I have given them.'
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses"),
        ("וְאֶל-אַהֲרֹן", "והרון", "and Aaron:"),
        ("יַעַן לֹא-הֶאֱמַנְתֶּם", "כמא לם תומנוהם", "'Just as you did not make them trust"),
        ("בִּי", "בי", "in Me,"),
        ("לְהַקְדִּישֵׁנִי", "ותקדסוני", "and sanctify Me"),
        ("לְעֵינֵי בְּנֵי יִשְׂרָאֵל", "בחצ'רה' בני אסראיל", "in the presence of the sons of Israel —"),
        ("לָכֵן", "כד'אך", "so shall you two not bring"),
        ("לֹא תָבִיאוּ", "לא תדכ'לא", "this congregation"),
        ("אֶת-הַקָּהָל הַזֶּה", "הד'א אלגוק", "into the land"),
        ("אֶל-הָאָרֶץ", "אלי' אלבלד", "which I have"),
        ("אֲשֶׁר-נָתַתִּי לָהֶם", "אלד'י אעטיתהם", "given them.'"),
    ],
    13: [
        # HE: הֵמָּה מֵי מְרִיבָה אֲשֶׁר-רָבוּ בְנֵי-יִשְׂרָאֵל אֶת-יְהוָה וַיִּקָּדֵשׁ בָּם
        # JA: ד'אלך מא אלכ'צומה. אלד'י כא'צם בני אסראיל אלרסול בסבבה. פת עצ'ם פיהם
        # EN: That is the water of strife, over which the sons of Israel quarreled with the messenger, and He was magnified among them.
        ("הֵמָּה", "ד'אלך", "That is"),
        ("מֵי מְרִיבָה", "מא אלכ'צומה", "the water of strife,"),
        ("אֲשֶׁר-רָבוּ", "אלד'י כא'צם", "over which"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel quarreled"),
        ("אֶת-יְהוָה", "אלרסול בסבבה", "with the messenger,"),
        ("וַיִּקָּדֵשׁ בָּם", "פת עצ'ם פיהם", "and He was magnified among them."),
    ],
    14: [
        # HE: וַיִּשְׁלַח מֹשֶׁה מַלְאָכִים מִקָּדֵשׁ אֶל-מֶלֶךְ אֱדוֹם כֹּה אָמַר אָחִיךָ יִשְׂרָאֵל אַתָּה יָדַעְתָּ אֵת כָּל-הַתְּלָאָה אֲשֶׁר מְצָאָתְנוּ
        # JA: ת'ם בעת' מוסי' ברסל. מן רקים אלי' מלך אדום. כד'א קאל אכ'יך אסראיל. אנת עאלם. בגמיע אלמצאיב אלתי נאלתנא
        # EN: Then Moses sent messengers from Raqim to the king of Edom, saying: 'Thus says your brother Israel: You know all the calamities that have befallen us —
        (None, "ת'ם", "Then"),
        ("וַיִּשְׁלַח מֹשֶׁה", "בעת' מוסי'", "Moses sent"),
        ("מַלְאָכִים", "ברסל", "messengers"),
        ("מִקָּדֵשׁ", "מן רקים", "from Raqim"),
        ("אֶל-מֶלֶךְ אֱדוֹם", "אלי' מלך אדום", "to the king of Edom, saying:"),
        ("כֹּה אָמַר", "כד'א קאל", "'Thus says"),
        ("אָחִיךָ יִשְׂרָאֵל", "אכ'יך אסראיל", "your brother Israel:"),
        ("אַתָּה יָדַעְתָּ", "אנת עאלם", "You know"),
        ("כָּל-הַתְּלָאָה", "בגמיע אלמצאיב", "all the calamities"),
        ("אֲשֶׁר מְצָאָתְנוּ", "אלתי נאלתנא", "that have befallen us —"),
    ],
    15: [
        # HE: וַיֵּרְדוּ אֲבֹתֵינוּ מִצְרַיְמָה וַנֵּשֶׁב בְּמִצְרַיִם יָמִים רַבִּים וַיָּרֵעוּ לָנוּ מִצְרַיִם וְלַאֲבֹתֵינוּ
        # JA: אן אבאינא נזלו מצרא. פאקמנא במצר מדה טוילה. ואסא אלמצריון. בנא ובאבאינא
        # EN: that our fathers went down to Egypt, and we dwelt in Egypt a long time; and the Egyptians dealt evilly with us and with our fathers.
        (None, "אן", "that"),
        ("אֲבֹתֵינוּ", "אבאינא", "our fathers"),
        ("וַיֵּרְדוּ", "נזלו", "went down"),
        ("מִצְרַיְמָה", "מצרא", "to Egypt,"),
        ("וַנֵּשֶׁב בְּמִצְרַיִם", "פאקמנא במצר", "and we dwelt in Egypt"),
        ("יָמִים רַבִּים", "מדה טוילה", "a long time;"),
        ("וַיָּרֵעוּ", "ואסא", "and the Egyptians dealt evilly"),
        ("מִצְרַיִם", "אלמצריון", "with us"),
        ("וְלַאֲבֹתֵינוּ", "ובאבאינא", "and with our fathers."),
    ],
    16: [
        # HE: וַנִּצְעַק אֶל-יְהוָה וַיִּשְׁמַע קֹלֵנוּ וַיִּשְׁלַח מַלְאָךְ וַיֹּצִאֵנוּ מִמִּצְרָיִם וְהִנֵּה אֲנַחְנוּ בְקָדֵשׁ עִיר קְצֵה גְבוּלֶךָ
        # JA: פדעינא אלי' אללה פסמע צותנא. ובעת' ברסול. ואכ'רגנא מן מצר. והוד'א נחן פי קריה' רקים. פי טרף תכ'מך
        # EN: And we cried out to God, and He heard our voice; and He sent a messenger, and brought us out of Egypt. And behold, we are now in the town of Raqim, at the edge of your border.
        ("וַנִּצְעַק", "פדעינא", "And we cried out"),
        ("אֶל-יְהוָה", "אלי' אללה", "to God,"),
        ("וַיִּשְׁמַע", "פסמע", "and He heard"),
        ("קֹלֵנוּ", "צותנא", "our voice;"),
        ("וַיִּשְׁלַח מַלְאָךְ", "ובעת' ברסול", "and He sent a messenger,"),
        ("וַיֹּצִאֵנוּ מִמִּצְרָיִם", "ואכ'רגנא מן מצר", "and brought us out of Egypt."),
        ("וְהִנֵּה אֲנַחְנוּ", "והוד'א נחן", "And behold, we are now"),
        ("בְקָדֵשׁ עִיר", "פי קריה' רקים", "in the town of Raqim,"),
        ("קְצֵה גְבוּלֶךָ", "פי טרף תכ'מך", "at the edge of your border."),
    ],
    17: [
        # HE: נַעְבְּרָה-נָּא בְאַרְצֶךָ לֹא נַעֲבֹר בְּשָׂדֶה וּבְכֶרֶם וְלֹא נִשְׁתֶּה מֵי בְאֵר דֶּרֶךְ הַמֶּלֶךְ נֵלֵךְ לֹא נִטֶּה יָמִין וּשְׂמֹאול עַד אֲשֶׁר-נַעֲבֹר גְּבֻלֶךָ
        # JA: נריד אן נגוז פי בלדך וליסנא נמיל אלי' צ'יעה ולא כרם. ולא נשרב מא צהריג. לכנא נסיר פי אלטריק אלגאדה. לא נמיל ימנה ולא יסרה. אלי' אן נגוז תכ'מך
        # EN: We wish to pass through your land; we will not turn aside to any farmstead or vineyard, nor will we drink cistern water — but we will travel along the main road, turning neither right nor left, until we have passed through your territory.'
        ("נַעְבְּרָה-נָּא", "נריד אן נגוז", "We wish to pass"),
        ("בְאַרְצֶךָ", "פי בלדך", "through your land;"),
        ("לֹא נַעֲבֹר", "וליסנא נמיל", "we will not turn aside"),
        ("בְּשָׂדֶה", "אלי' צ'יעה", "to any farmstead"),
        ("וּבְכֶרֶם", "ולא כרם", "or vineyard,"),
        ("וְלֹא נִשְׁתֶּה", "ולא נשרב", "nor will we drink"),
        ("מֵי בְאֵר", "מא צהריג", "cistern water —"),
        ("דֶּרֶךְ הַמֶּלֶךְ נֵלֵךְ", "לכנא נסיר פי אלטריק אלגאדה", "but we will travel along the main road,"),
        ("לֹא נִטֶּה יָמִין", "לא נמיל ימנה", "turning neither right"),
        ("וּשְׂמֹאול", "ולא יסרה", "nor left,"),
        ("עַד אֲשֶׁר-נַעֲבֹר גְּבֻלֶךָ", "אלי' אן נגוז תכ'מך", "until we have passed through your territory.'"),
    ],
    18: [
        # HE: וַיֹּאמֶר אֵלָיו אֱדוֹם לֹא תַעֲבֹר בִּי--פֶּן-בַּחֶרֶב אֵצֵא לִקְרָאתֶךָ
        # JA: קאל לה אלאחמרי. לא תגוז בי. כלא באלסיף אכ'ר'ג תלקאך
        # EN: The Red One (Edom) said to him: 'You shall not pass through me — lest I come out against you with the sword.'
        ("וַיֹּאמֶר", "קאל לה", "The Red One (Edom) said to him:"),
        ("אֱדוֹם", "אלאחמרי", "'You shall not pass"),
        ("לֹא תַעֲבֹר בִּי", "לא תגוז בי", "through me —"),
        ("פֶּן-בַּחֶרֶב", "כלא באלסיף", "lest I come out"),
        ("אֵצֵא לִקְרָאתֶךָ", "אכ'ר'ג תלקאך", "against you with the sword.'"),
    ],
    19: [
        # HE: וַיֹּאמְרוּ אֵלָיו בְּנֵי-יִשְׂרָאֵל בַּמְסִלָּה נַעֲלֶה וְאִם-מֵימֶיךָ נִשְׁתֶּה אֲנִי וּמִקְנַי וְנָתַתִּי מִכְרָם רַק אֵין-דָּבָר בְּרַגְלַי אֶעֱבֹרָה
        # JA: וקאלו לה בני אסראיל נצעד פי אלמחגה. ואן שרבנא לך מא נחן ומאשיתנא. דפענא ת'מנה. וליס אמר אלא נגוז פקט
        # EN: And the sons of Israel said to him: 'We will go up by the highway; and if we or our livestock drink any of your water, we will pay its price. There is no matter at all — only let us pass through.'
        ("וַיֹּאמְרוּ", "וקאלו לה", "And the sons of Israel said to him:"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "'We will go up"),
        ("בַּמְסִלָּה נַעֲלֶה", "נצעד פי אלמחגה", "by the highway;"),
        ("וְאִם-מֵימֶיךָ נִשְׁתֶּה", "ואן שרבנא לך מא", "and if we or our livestock drink any of your water,"),
        ("אֲנִי וּמִקְנַי", "נחן ומאשיתנא", "we will pay its price."),
        ("וְנָתַתִּי מִכְרָם", "דפענא ת'מנה", "There is no matter at all —"),
        ("רַק אֵין-דָּבָר", "וליס אמר", "only let us"),
        ("בְּרַגְלַי אֶעֱבֹרָה", "אלא נגוז פקט", "pass through.'"),
    ],
    20: [
        # HE: וַיֹּאמֶר לֹא תַעֲבֹר וַיֵּצֵא אֱדוֹם לִקְרָאתוֹ בְּעַם כָּבֵד וּבְיָד חֲזָקָה
        # JA: קאל לא תגוז כד'אך. פכ'רג אדום תלקאהם. בשעב עצ'ים ויד שדידה
        # EN: He said: 'You shall not pass, not even so.' And Edom came out to meet them with a great host and a mighty hand.
        ("וַיֹּאמֶר", "קאל", "He said:"),
        ("לֹא תַעֲבֹר", "לא תגוז", "'You shall not pass,"),
        (None, "כד'אך", "not even so.'"),
        ("וַיֵּצֵא אֱדוֹם", "פכ'רג אדום", "And Edom came out"),
        ("לִקְרָאתוֹ", "תלקאהם", "to meet them"),
        ("בְּעַם כָּבֵד", "בשעב עצ'ים", "with a great host"),
        ("וּבְיָד חֲזָקָה", "ויד שדידה", "and a mighty hand."),
    ],
    21: [
        # HE: וַיְמָאֵן אֱדוֹם נְתֹן אֶת-יִשְׂרָאֵל עֲבֹר בִּגְבֻלוֹ וַיֵּט יִשְׂרָאֵל מֵעָלָיו
        # JA: פלמא אבא אדום. אן יתרך אל אסראיל. אן יגוזו פי תכ'מה. פמלו ענה
        # EN: And when Edom refused to allow the house of Israel to pass through his territory, they turned away from him.
        ("וַיְמָאֵן", "פלמא אבא", "And when Edom refused"),
        ("אֱדוֹם", "אדום", "to allow"),
        ("נְתֹן", "אן יתרך", "the house of Israel"),
        ("אֶת-יִשְׂרָאֵל", "אל אסראיל", "to pass through"),
        ("עֲבֹר בִּגְבֻלוֹ", "אן יגוזו פי תכ'מה", "his territory,"),
        ("וַיֵּט יִשְׂרָאֵל מֵעָלָיו", "פמלו ענה", "they turned away from him."),
    ],
    22: [
        # HE: וַיִּסְעוּ מִקָּדֵשׁ וַיָּבֹאוּ בְנֵי-יִשְׂרָאֵל כָּל-הָעֵדָה הֹר הָהָר
        # JA: פרחלו מן רקים. וגאת גמאעתהם. אלי' גבל הור
        # EN: And they departed from Raqim, and the whole of their congregation came to Mount Hor.
        ("וַיִּסְעוּ", "פרחלו", "And they departed"),
        ("מִקָּדֵשׁ", "מן רקים", "from Raqim,"),
        ("וַיָּבֹאוּ", "וגאת", "and the whole of their"),
        ("כָּל-הָעֵדָה", "גמאעתהם", "congregation came"),
        ("הֹר הָהָר", "אלי' גבל הור", "to Mount Hor."),
    ],
    23: [
        # HE: וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה וְאֶל-אַהֲרֹן בְּהֹר הָהָר עַל-גְּבוּל אֶרֶץ-אֱדוֹם לֵאמֹר
        # JA: פקאל אללה. למוסי' והרון פי גבל הור. ענד תכ'ם בלד אדום קאילא
        # EN: And God said to Moses and Aaron at Mount Hor, at the border of the land of Edom, saying:
        ("וַיֹּאמֶר יְהוָה", "פקאל אללה", "And God said"),
        ("אֶל-מֹשֶׁה", "למוסי'", "to Moses"),
        ("וְאֶל-אַהֲרֹן", "והרון", "and Aaron"),
        ("בְּהֹר הָהָר", "פי גבל הור", "at Mount Hor,"),
        ("עַל-גְּבוּל אֶרֶץ-אֱדוֹם", "ענד תכ'ם בלד אדום", "at the border of the land of Edom,"),
        ("לֵאמֹר", "קאילא", "saying:"),
    ],
    24: [
        # HE: יֵאָסֵף אַהֲרֹן אֶל-עַמָּיו כִּי לֹא יָבֹא אֶל-הָאָרֶץ אֲשֶׁר נָתַתִּי לִבְנֵי יִשְׂרָאֵל--עַל אֲשֶׁר-מְרִיתֶם אֶת-פִּי לְמֵי מְרִיבָה
        # JA: ינצ'ם הרון אלי' קומה. פאנה לא יד'כל אלבלד. אלד'י אעטיתה לבני אסראיל. כמא קלת חין כ'אלפתמא אמרי פי מא אלכ'צומה
        # EN: 'Aaron shall be gathered to his people; for he shall not enter the land which I have given to the sons of Israel — as I said when the two of you transgressed My command at the water of strife.'
        ("יֵאָסֵף אַהֲרֹן", "ינצ'ם הרון", "'Aaron shall be gathered"),
        ("אֶל-עַמָּיו", "אלי' קומה", "to his people;"),
        ("כִּי לֹא יָבֹא", "פאנה לא יד'כל", "for he shall not enter"),
        ("אֶל-הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר נָתַתִּי", "אלד'י אעטיתה", "which I have given"),
        ("לִבְנֵי יִשְׂרָאֵל", "לבני אסראיל", "to the sons of Israel —"),
        ("עַל אֲשֶׁר-מְרִיתֶם", "כמא קלת חין כ'אלפתמא", "as I said when the two of you transgressed"),
        ("אֶת-פִּי", "אמרי", "My command"),
        ("לְמֵי מְרִיבָה", "פי מא אלכ'צומה", "at the water of strife.'"),
    ],
    25: [
        # HE: קַח אֶת-אַהֲרֹן וְאֶת-אֶלְעָזָר בְּנוֹ וְהַעַל אֹתָם הֹר הָהָר
        # JA: כ'ד' הרון. ואלעזר אבנה. ואצעדהמא אלי' גבל הור
        # EN: 'Take Aaron and Eleazar his son, and bring the two of them up to Mount Hor.'
        ("קַח", "כ'ד'", "'Take"),
        ("אֶת-אַהֲרֹן", "הרון", "Aaron"),
        ("וְאֶת-אֶלְעָזָר", "ואלעזר", "and Eleazar"),
        ("בְּנוֹ", "אבנה", "his son,"),
        ("וְהַעַל אֹתָם", "ואצעדהמא", "and bring the two of them up"),
        ("הֹר הָהָר", "אלי' גבל הור", "to Mount Hor.'"),
    ],
    26: [
        # HE: וְהַפְשֵׁט אֶת-אַהֲרֹן אֶת-בְּגָדָיו וְהִלְבַּשְׁתָּם אֶת-אֶלְעָזָר בְּנוֹ וְאַהֲרֹן יֵאָסֵף וּמֵת שָׁם
        # JA: ואסלך' הרון ת'יאבה. ואלבסהא אלעזר אבנה. והרון ינצ'ם וימות הנאך
        # EN: 'And strip Aaron of his garments, and put them upon Eleazar his son; and Aaron shall be gathered and shall die there.'
        ("וְהַפְשֵׁט", "ואסלך'", "'And strip"),
        ("אֶת-אַהֲרֹן", "הרון", "Aaron"),
        ("אֶת-בְּגָדָיו", "ת'יאבה", "of his garments,"),
        ("וְהִלְבַּשְׁתָּם", "ואלבסהא", "and put them upon"),
        ("אֶת-אֶלְעָזָר בְּנוֹ", "אלעזר אבנה", "Eleazar his son;"),
        ("וְאַהֲרֹן יֵאָסֵף", "והרון ינצ'ם", "and Aaron shall be gathered"),
        ("וּמֵת שָׁם", "וימות הנאך", "and shall die there.'"),
    ],
    27: [
        # HE: וַיַּעַשׂ מֹשֶׁה כַּאֲשֶׁר צִוָּה יְהוָה וַיַּעֲלוּ אֶל-הֹר הָהָר לְעֵינֵי כָּל-הָעֵדָה
        # JA: פצנע מוסי'. כמא אמרה אללה. וצעדוא אלי' גבל הור. בחצ'רה' אלגמאעה
        # EN: And Moses did as God had commanded him; and they went up to Mount Hor in the presence of the congregation.
        ("וַיַּעַשׂ מֹשֶׁה", "פצנע מוסי'", "And Moses did"),
        ("כַּאֲשֶׁר צִוָּה יְהוָה", "כמא אמרה אללה", "as God had commanded him;"),
        ("וַיַּעֲלוּ אֶל-הֹר הָהָר", "וצעדוא אלי' גבל הור", "and they went up to Mount Hor"),
        ("לְעֵינֵי כָּל-הָעֵדָה", "בחצ'רה' אלגמאעה", "in the presence of the congregation."),
    ],
    28: [
        # HE: וַיַּפְשֵׁט מֹשֶׁה אֶת-אַהֲרֹן אֶת-בְּגָדָיו וַיַּלְבֵּשׁ אֹתָם אֶת-אֶלְעָזָר בְּנוֹ וַיָּמָת אַהֲרֹן שָׁם בְּרֹאשׁ הָהָר וַיֵּרֶד מֹשֶׁה וְאֶלְעָזָר מִן-הָהָר
        # JA: וסלך' מוסי' ת'יאב הרון. ואלבסהא אלעזר אבנה. ומאת הרון. הנאך פי ראס אלגבל. ונזל מוסי'. ואלעזר מן אלגבל
        # EN: And Moses stripped Aaron of his garments, and put them upon Eleazar his son; and Aaron died there at the summit of the mountain. And Moses and Eleazar came down from the mountain.
        ("וַיַּפְשֵׁט מֹשֶׁה", "וסלך' מוסי'", "And Moses stripped"),
        ("אֶת-אַהֲרֹן אֶת-בְּגָדָיו", "ת'יאב הרון", "Aaron of his garments,"),
        ("וַיַּלְבֵּשׁ אֹתָם", "ואלבסהא", "and put them upon"),
        ("אֶת-אֶלְעָזָר בְּנוֹ", "אלעזר אבנה", "Eleazar his son;"),
        ("וַיָּמָת אַהֲרֹן", "ומאת הרון", "and Aaron died"),
        ("שָׁם", "הנאך", "there"),
        ("בְּרֹאשׁ הָהָר", "פי ראס אלגבל", "at the summit of the mountain."),
        ("וַיֵּרֶד מֹשֶׁה", "ונזל מוסי'", "And Moses"),
        ("וְאֶלְעָזָר", "ואלעזר", "and Eleazar"),
        ("מִן-הָהָר", "מן אלגבל", "came down from the mountain."),
    ],
    29: [
        # HE: וַיִּרְאוּ כָּל-הָעֵדָה כִּי גָוַע אַהֲרֹן וַיִּבְכּוּ אֶת-אַהֲרֹן שְׁלֹשִׁים יוֹם כֹּל בֵּית יִשְׂרָאֵל
        # JA: פלמא ראת אלגמאעה. אן הרון קד מאת. בכא עלי'ה ת'לאתין יומא. גמיע אל אסראיל
        # EN: And when the congregation saw that Aaron had indeed died, all the house of Israel wept for him thirty days.
        ("וַיִּרְאוּ", "פלמא ראת", "And when the congregation"),
        ("כָּל-הָעֵדָה", "אלגמאעה", "saw that Aaron"),
        ("כִּי גָוַע אַהֲרֹן", "אן הרון קד מאת", "had indeed died,"),
        ("וַיִּבְכּוּ", "בכא עלי'ה", "wept for him"),
        ("שְׁלֹשִׁים יוֹם", "ת'לאתין יומא", "thirty days."),
        ("כֹּל בֵּית יִשְׂרָאֵל", "גמיע אל אסראיל", "all the house of Israel"),
    ],
}

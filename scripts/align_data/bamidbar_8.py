"""Hand-authored word-level alignment triples for Bamidbar chapter 8."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses in speech.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר יְהוָה", "כלם אללה", "God spoke"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "in speech."),
    ],
    2: [
        # HE: דַּבֵּר אֶל-אַהֲרֹן וְאָמַרְתָּ אֵלָיו בְּהַעֲלֹתְךָ אֶת-הַנֵּרֹת אֶל-מוּל פְּנֵי הַמְּנוֹרָה יָאִירוּ שִׁבְעַת הַנֵּרוֹת
        # JA: מר הרון וקל לה. אד'א אסרגת אלסרג. פאלי' מא ילי וגה אלמנארה. תצ'י סבעתהא
        # EN: 'Command Aaron and say to him: when you light the lamp, toward what faces the front of the lampstand shall its seven lamps give light.'
        ("דַּבֵּר", "מר", "'Command"),
        ("אֶל-אַהֲרֹן", "הרון", "Aaron"),
        ("וְאָמַרְתָּ", "וקל", "and say"),
        ("אֵלָיו", "לה", "to him:"),
        ("בְּהַעֲלֹתְךָ", "אד'א אסרגת", "when you light"),
        ("אֶת-הַנֵּרֹת", "אלסרג", "the lamp,"),
        ("אֶל-מוּל", "פאלי' מא ילי", "toward what faces"),
        ("פְּנֵי הַמְּנוֹרָה", "וגה אלמנארה", "the front of the lampstand"),
        ("יָאִירוּ", "תצ'י", "give light.'"),
        ("שִׁבְעַת הַנֵּרוֹת", "סבעתהא", "its seven lamps"),
    ],
    3: [
        # HE: וַיַּעַשׂ כֵּן אַהֲרֹן--אֶל-מוּל פְּנֵי הַמְּנוֹרָה הֶעֱלָה נֵרֹתֶיהָ כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה
        # JA: פצנע כד'אך הרון. ואסרג סרג אלמנארה. אלי' מא ילי וגההא. כמא אמר אללה מוסי'
        # EN: And so Aaron did — he lit the lamps of the lampstand toward what faces its front, as God had commanded Moses.
        ("וַיַּעַשׂ", "פצנע", "And so"),
        ("כֵּן", "כד'אך", "Aaron did —"),
        ("אַהֲרֹן", "הרון", "he lit"),
        ("הֶעֱלָה נֵרֹתֶיהָ", "ואסרג סרג אלמנארה", "the lamps of the lampstand"),
        ("אֶל-מוּל", "אלי' מא ילי", "toward what faces"),
        ("פְּנֵי הַמְּנוֹרָה", "וגההא", "its front,"),
        ("כַּאֲשֶׁר צִוָּה", "כמא אמר", "as"),
        ("יְהוָה", "אללה", "God had commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses."),
    ],
    4: [
        # HE: וְזֶה מַעֲשֵׂה הַמְּנֹרָה מִקְשָׁה זָהָב עַד-יְרֵכָהּ עַד-פִּרְחָהּ מִקְשָׁה הִוא כַּמַּרְאֶה אֲשֶׁר הֶרְאָה יְהוָה אֶת-מֹשֶׁה--כֵּן עָשָׂה אֶת-הַמְּנֹרָה
        # JA: והד'ה צנעה' אלמנארה מצמתה ד'הב. חתי ארגלהא ורחארחהא מצמתה. כאלמנצ'רכ. אלד'י אורא אללה מוסי'. כד'אך צנעהא
        # EN: And this is the workmanship of the lampstand: solid gold — even its base and its blossoms were solid — like the appearance which God had shown to Moses; so he made it.
        ("וְזֶה", "והד'ה", "And this is"),
        ("מַעֲשֵׂה הַמְּנֹרָה", "צנעה' אלמנארה", "the workmanship of the lampstand:"),
        ("מִקְשָׁה", "מצמתה", "solid"),
        ("זָהָב", "ד'הב", "gold —"),
        ("עַד-יְרֵכָהּ", "חתי ארגלהא", "even its base"),
        ("עַד-פִּרְחָהּ", "ורחארחהא", "and its blossoms"),
        (None, "מצמתה", "were solid —"),
        ("כַּמַּרְאֶה", "כאלמנצ'רכ", "like the appearance"),
        ("אֲשֶׁר הֶרְאָה", "אלד'י אורא", "which"),
        ("יְהוָה", "אללה", "God had shown"),
        ("אֶת-מֹשֶׁה", "מוסי'", "to Moses;"),
        ("כֵּן עָשָׂה אֶת-הַמְּנֹרָה", "כד'אך צנעהא", "so he made it."),
    ],
    5: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses in speech.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר יְהוָה", "כלם אללה", "God spoke"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "in speech."),
    ],
    6: [
        # HE: קַח אֶת-הַלְוִיִּם מִתּוֹךְ בְּנֵי יִשְׂרָאֵל וְטִהַרְתָּ אֹתָם
        # JA: קדם אלליוניין. מן בין בני אסראיל. וטהרהם
        # EN: 'Bring forward the Levites from among the sons of Israel, and purify them.'
        ("קַח", "קדם", "'Bring forward"),
        ("אֶת-הַלְוִיִּם", "אלליוניין", "the Levites"),
        ("מִתּוֹךְ", "מן בין", "from among"),
        ("בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel,"),
        ("וְטִהַרְתָּ אֹתָם", "וטהרהם", "and purify them.'"),
    ],
    7: [
        # HE: וְכֹה-תַעֲשֶׂה לָהֶם לְטַהֲרָם הַזֵּה עֲלֵיהֶם מֵי חַטָּאת וְהֶעֱבִירוּ תַעַר עַל-כָּל-בְּשָׂרָם וְכִבְּסוּ בִגְדֵיהֶם וְהִטֶּהָרוּ
        # JA: וכד'י אצנע להם פי תטהירהם. אנצ'ח עליהם מן מא אלדכוה. וימרון אלמוס עלי' גמיע בדנהם. ויג'סלון ת'יאבהם ויטהרון
        # EN: 'And thus shall you do for them in their purification: sprinkle upon them of the water of purification, and let them pass a razor over all their body, and let them wash their garments — and they shall be purified.'
        ("וְכֹה-תַעֲשֶׂה", "וכד'י אצנע", "'And thus shall you do"),
        ("לָהֶם", "להם", "for them"),
        ("לְטַהֲרָם", "פי תטהירהם", "in their purification:"),
        ("הַזֵּה", "אנצ'ח", "sprinkle"),
        ("עֲלֵיהֶם", "עליהם", "upon them"),
        ("מֵי חַטָּאת", "מן מא אלדכוה", "of the water of purification,"),
        ("וְהֶעֱבִירוּ", "וימרון", "and let them pass"),
        ("תַעַר", "אלמוס", "a razor"),
        ("עַל-כָּל-בְּשָׂרָם", "עלי' גמיע בדנהם", "over all their body,"),
        ("וְכִבְּסוּ", "ויג'סלון", "and let them wash"),
        ("בִגְדֵיהֶם", "ת'יאבהם", "their garments —"),
        ("וְהִטֶּהָרוּ", "ויטהרון", "and they shall be purified.'"),
    ],
    8: [
        # HE: וְלָקְחוּ פַּר בֶּן-בָּקָר וּמִנְחָתוֹ סֹלֶת בְּלוּלָה בַשָּׁמֶן וּפַר-שֵׁנִי בֶן-בָּקָר תִּקַּח לְחַטָּאת
        # JA: ויקרבו ת'ורא מן אלבקר. ומעה בר סמד מלתות בדהן. ות'ור אכ'ר מן אלבקר כ'דה לאלדכוה
        # EN: 'And they shall bring forward an ox from the herd, and with it wheat-flour, fine semolina mixed with oil; and a second ox from the herd — take it for the purification-offering.'
        ("וְלָקְחוּ", "ויקרבו", "'And they shall bring forward"),
        ("פַּר", "ת'ורא", "an ox"),
        ("בֶּן-בָּקָר", "מן אלבקר", "from the herd,"),
        ("וּמִנְחָתוֹ", "ומעה בר סמד", "and with it wheat-flour, fine semolina"),
        ("סֹלֶת בְּלוּלָה", "מלתות", "mixed"),
        ("בַשָּׁמֶן", "בדהן", "with oil;"),
        ("וּפַר-שֵׁנִי", "ות'ור אכ'ר", "and a second ox"),
        ("בֶן-בָּקָר", "מן אלבקר", "from the herd —"),
        ("תִּקַּח", "כ'דה", "take it"),
        ("לְחַטָּאת", "לאלדכוה", "for the purification-offering.'"),
    ],
    9: [
        # HE: וְהִקְרַבְתָּ אֶת-הַלְוִיִּם לִפְנֵי אֹהֶל מוֹעֵד וְהִקְהַלְתָּ--אֶת-כָּל-עֲדַת בְּנֵי יִשְׂרָאֵל
        # JA: וקדם אלליוניין. בין ידי כ'בא אלמחצ'ר. וגווק גמאעה' בני אסראיל
        # EN: 'And bring forward the Levites before the tent of meeting, and assemble the congregation of the sons of Israel.'
        ("וְהִקְרַבְתָּ", "וקדם", "'And bring forward"),
        ("אֶת-הַלְוִיִּם", "אלליוניין", "the Levites"),
        ("לִפְנֵי", "בין ידי", "before"),
        ("אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of meeting,"),
        ("וְהִקְהַלְתָּ", "וגווק", "and assemble"),
        ("אֶת-כָּל-עֲדַת", "גמאעה'", "the congregation of"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel.'"),
    ],
    10: [
        # HE: וְהִקְרַבְתָּ אֶת-הַלְוִיִּם לִפְנֵי יְהוָה וְסָמְכוּ בְנֵי-יִשְׂרָאֵל אֶת-יְדֵיהֶם עַל-הַלְוִיִּם
        # JA: וקדמהם בין ידי אללה. ויסנ'ד בני אסראיל אידיהם עליהם
        # EN: 'And present them before God, and the sons of Israel shall lay their hands upon them.'
        ("וְהִקְרַבְתָּ", "וקדמהם", "'And present them"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "before God,"),
        ("וְסָמְכוּ", "ויסנ'ד", "shall lay"),
        ("בְנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("אֶת-יְדֵיהֶם", "אידיהם", "their hands"),
        ("עַל-הַלְוִיִּם", "עליהם", "upon them.'"),
    ],
    11: [
        # HE: וְהֵנִיף אַהֲרֹן אֶת-הַלְוִיִּם תְּנוּפָה לִפְנֵי יְהוָה מֵאֵת בְּנֵי יִשְׂרָאֵל וְהָיוּ לַעֲבֹד אֶת-עֲבֹדַת יְהוָה
        # JA: ויזפהם הרון זפא בין ידי אללה. מן בני אסראיל. פיכונו יכ'דמון כ'דמה' אללה
        # EN: 'And Aaron shall present them as a presentation before God, from the sons of Israel — that they may be for serving the service of God.'
        ("וְהֵנִיף", "ויזפהם", "'And Aaron shall present them"),
        ("אַהֲרֹן", "הרון", "as a presentation"),
        ("תְּנוּפָה", "זפא", "before"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "God,"),
        ("מֵאֵת בְּנֵי יִשְׂרָאֵל", "מן בני אסראיל", "from the sons of Israel —"),
        ("וְהָיוּ", "פיכונו", "that they may be for"),
        ("לַעֲבֹד", "יכ'דמון", "serving"),
        ("אֶת-עֲבֹדַת יְהוָה", "כ'דמה' אללה", "the service of God.'"),
    ],
    12: [
        # HE: וְהַלְוִיִּם יִסְמְכוּ אֶת-יְדֵיהֶם עַל רֹאשׁ הַפָּרִים וַעֲשֵׂה אֶת-הָאֶחָד חַטָּאת וְאֶת-הָאֶחָד עֹלָה לַיהוָה לְכַפֵּר עַל-הַלְוִיִּם
        # JA: ואלליוניין יסנדו אידיהם. עלי' רוס אלת'יראן. ואצנע אחדהמא ד'כוה. ואלאכ'ר צעידה ללה. ואסתג'פר ענהם
        # EN: 'And the Levites shall lay their hands upon the heads of the bulls; and make one of them a purification-offering, and the other a burnt-offering to God, and seek forgiveness for them.'
        ("וְהַלְוִיִּם", "ואלליוניין", "'And the Levites"),
        ("יִסְמְכוּ", "יסנדו", "shall lay"),
        ("אֶת-יְדֵיהֶם", "אידיהם", "their hands"),
        ("עַל רֹאשׁ הַפָּרִים", "עלי' רוס אלת'יראן", "upon the heads of the bulls;"),
        ("וַעֲשֵׂה", "ואצנע", "and make"),
        ("אֶת-הָאֶחָד", "אחדהמא", "one of them"),
        ("חַטָּאת", "ד'כוה", "a purification-offering,"),
        ("וְאֶת-הָאֶחָד", "ואלאכ'ר", "and the other"),
        ("עֹלָה לַיהוָה", "צעידה ללה", "a burnt-offering to God,"),
        ("לְכַפֵּר עַל-הַלְוִיִּם", "ואסתג'פר ענהם", "and seek forgiveness for them.'"),
    ],
    13: [
        # HE: וְהַעֲמַדְתָּ אֶת-הַלְוִיִּם לִפְנֵי אַהֲרֹן וְלִפְנֵי בָנָיו וְהֵנַפְתָּ אֹתָם תְּנוּפָה לַיהוָה
        # JA: ואוקפהם בין ידי הרון ובניה. וזפהם זפא ללה
        # EN: 'And station them before Aaron and his sons, and present them as a presentation to God.'
        ("וְהַעֲמַדְתָּ", "ואוקפהם", "'And station them"),
        ("לִפְנֵי אַהֲרֹן", "בין ידי הרון", "before Aaron"),
        ("וְלִפְנֵי בָנָיו", "ובניה", "and his sons,"),
        ("וְהֵנַפְתָּ אֹתָם", "וזפהם", "and present them"),
        ("תְּנוּפָה", "זפא", "as a presentation"),
        ("לַיהוָה", "ללה", "to God.'"),
    ],
    14: [
        # HE: וְהִבְדַּלְתָּ אֶת-הַלְוִיִּם מִתּוֹךְ בְּנֵי יִשְׂרָאֵל וְהָיוּ לִי הַלְוִיִּם
        # JA: ואעזלהם מן בין בני אסראיל. פיכונו לי
        # EN: 'And separate them from among the sons of Israel, and they shall be Mine.'
        ("וְהִבְדַּלְתָּ אֶת-הַלְוִיִּם", "ואעזלהם", "'And separate them"),
        ("מִתּוֹךְ", "מן בין", "from among"),
        ("בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel,"),
        ("וְהָיוּ לִי הַלְוִיִּם", "פיכונו לי", "and they shall be Mine.'"),
    ],
    15: [
        # HE: וְאַחֲרֵי-כֵן יָבֹאוּ הַלְוִיִּם לַעֲבֹד אֶת-אֹהֶל מוֹעֵד וְטִהַרְתָּ אֹתָם וְהֵנַפְתָּ אֹתָם תְּנוּפָה
        # JA: ובעד ד'אלך ידכ'לון. ליכ'דמון כ'בא אלמחצ'ר. וקד טהרתהם. וזפיתהם זפא
        # EN: 'And after that they shall enter to serve the tent of meeting — for you will have purified them and presented them as a presentation.'
        ("וְאַחֲרֵי-כֵן", "ובעד ד'אלך", "'And after that"),
        ("יָבֹאוּ הַלְוִיִּם", "ידכ'לון", "they shall enter"),
        ("לַעֲבֹד", "ליכ'דמון", "to serve"),
        ("אֶת-אֹהֶל מוֹעֵד", "כ'בא אלמחצ'ר", "the tent of meeting —"),
        ("וְטִהַרְתָּ אֹתָם", "וקד טהרתהם", "for you will have purified them"),
        ("וְהֵנַפְתָּ אֹתָם", "וזפיתהם", "and presented them"),
        ("תְּנוּפָה", "זפא", "as a presentation.'"),
    ],
    16: [
        # HE: כִּי נְתֻנִים נְתֻנִים הֵמָּה לִי מִתּוֹךְ בְּנֵי יִשְׂרָאֵל תַּחַת פִּטְרַת כָּל-רֶחֶם בְּכוֹר כֹּל מִבְּנֵי יִשְׂרָאֵל--לָקַחְתִּי אֹתָם לִי
        # JA: לאנהם מגעולין לי. מן בין בני אסראיל. בדל כל בכר. פאתח כל בטן מן בני אסראיל. אכ'ד'תהם לי
        # EN: 'For they are appointed to Me from among the sons of Israel: in place of every firstborn, the opener of every womb among the sons of Israel — I have taken them for Myself.'
        ("כִּי", "לאנהם", "'For they are"),
        ("נְתֻנִים נְתֻנִים", "מגעולין", "appointed"),
        ("לִי", "לי", "to Me"),
        ("מִתּוֹךְ", "מן בין", "from among"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel:"),
        ("תַּחַת", "בדל", "in place of"),
        ("פִּטְרַת כָּל-רֶחֶם", "כל בכר", "every firstborn,"),
        ("בְּכוֹר כֹּל", "פאתח כל בטן", "the opener of every womb"),
        ("מִבְּנֵי יִשְׂרָאֵל", "מן בני אסראיל", "among the sons of Israel —"),
        ("לָקַחְתִּי אֹתָם לִי", "אכ'ד'תהם לי", "I have taken them for Myself.'"),
    ],
    17: [
        # HE: כִּי לִי כָל-בְּכוֹר בִּבְנֵי יִשְׂרָאֵל בָּאָדָם וּבַבְּהֵמָה בְּיוֹם הַכֹּתִי כָל-בְּכוֹר בְּאֶרֶץ מִצְרַיִם הִקְדַּשְׁתִּי אֹתָם לִי
        # JA: כמא כאן לי כל בכר. פי מא בין בני אסראיל. מן אנסאן אלי' בהימה. וד'אלך פי יום אהלכת כל בכר פי בלד מצר. אקדסתהם לי
        # EN: 'Just as every firstborn among the sons of Israel was Mine — of human and of beast — on the day I destroyed every firstborn in the land of Egypt, I consecrated them to Me.'
        (None, "כמא כאן", "'Just as"),
        ("לִי", "לי", "was Mine"),
        ("כָל-בְּכוֹר", "כל בכר", "every firstborn"),
        ("בִּבְנֵי יִשְׂרָאֵל", "פי מא בין בני אסראיל", "among the sons of Israel"),
        ("בָּאָדָם", "מן אנסאן", "of human"),
        ("וּבַבְּהֵמָה", "אלי' בהימה", "and of beast —"),
        ("בְּיוֹם הַכֹּתִי", "וד'אלך פי יום אהלכת", "on the day I destroyed"),
        ("כָל-בְּכוֹר", "כל בכר", "every firstborn"),
        ("בְּאֶרֶץ מִצְרַיִם", "פי בלד מצר", "in the land of Egypt,"),
        ("הִקְדַּשְׁתִּי אֹתָם לִי", "אקדסתהם לי", "I consecrated them to Me.'"),
    ],
    18: [
        # HE: וָאֶקַּח אֶת-הַלְוִיִּם תַּחַת כָּל-בְּכוֹר בִּבְנֵי יִשְׂרָאֵל
        # JA: כד'אלך אתכד'ת אלליוניין בדלהם
        # EN: 'Thus I took the Levites in their stead.'
        (None, "כד'אלך", "'Thus"),
        ("וָאֶקַּח", "אתכד'ת", "I took"),
        ("אֶת-הַלְוִיִּם", "אלליוניין", "the Levites"),
        ("תַּחַת כָּל-בְּכוֹר בִּבְנֵי יִשְׂרָאֵל", "בדלהם", "in their stead.'"),
    ],
    19: [
        # HE: וָאֶתְּנָה אֶת-הַלְוִיִּם נְתֻנִים לְאַהֲרֹן וּלְבָנָיו מִתּוֹךְ בְּנֵי יִשְׂרָאֵל לַעֲבֹד אֶת-עֲבֹדַת בְּנֵי-יִשְׂרָאֵל בְּאֹהֶל מוֹעֵד וּלְכַפֵּר עַל-בְּנֵי יִשְׂרָאֵל וְלֹא יִהְיֶה בִּבְנֵי יִשְׂרָאֵל נֶגֶף בְּגֶשֶׁת בְּנֵי-יִשְׂרָאֵל אֶל-הַקֹּדֶשׁ
        # JA: וגעלתהם להרון ובניה. מן בין בני אסראיל. ליכדמו כ'דמתהם פי כ'בא אלמחצ'ר. ויסתג'פרו ענהם. ולא יחל בהם ובא. אד' הם תקדמו אלי' אלקדס
        # EN: 'And I appointed them for Aaron and his sons, from among the sons of Israel, to perform their service in the tent of meeting, and to seek forgiveness for them — that no pestilence may come upon them when they approach the sanctuary.'
        ("וָאֶתְּנָה אֶת-הַלְוִיִּם", "וגעלתהם", "'And I appointed them"),
        ("לְאַהֲרֹן", "להרון", "for Aaron"),
        ("וּלְבָנָיו", "ובניה", "and his sons,"),
        ("מִתּוֹךְ", "מן בין", "from among"),
        ("בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("לַעֲבֹד אֶת-עֲבֹדַת בְּנֵי-יִשְׂרָאֵל", "ליכדמו כ'דמתהם", "to perform their service"),
        ("בְּאֹהֶל מוֹעֵד", "פי כ'בא אלמחצ'ר", "in the tent of meeting,"),
        ("וּלְכַפֵּר עַל-בְּנֵי יִשְׂרָאֵל", "ויסתג'פרו ענהם", "and to seek forgiveness for them —"),
        ("וְלֹא יִהְיֶה", "ולא יחל בהם", "that no pestilence may come upon them"),
        ("נֶגֶף", "ובא", "when they approach"),
        ("בְּגֶשֶׁת בְּנֵי-יִשְׂרָאֵל אֶל-הַקֹּדֶשׁ", "אד' הם תקדמו אלי' אלקדס", "the sanctuary.'"),
    ],
    20: [
        # HE: וַיַּעַשׂ מֹשֶׁה וְאַהֲרֹן וְכָל-עֲדַת בְּנֵי-יִשְׂרָאֵל לַלְוִיִּם כְּכֹל אֲשֶׁר-צִוָּה יְהוָה אֶת-מֹשֶׁה לַלְוִיִּם--כֵּן-עָשׂוּ לָהֶם בְּנֵי יִשְׂרָאֵל
        # JA: וצנע מוסי' והרון. וסאיר גמאעה' בני אסראיל לאלליוניין. כגמיע מא אמר אללה מוסי' פי סבבהם כד'אך צנעו להם
        # EN: And Moses and Aaron, and the rest of the congregation of the sons of Israel, did for the Levites according to all that God had commanded Moses concerning them — so they did for them.
        ("וַיַּעַשׂ", "וצנע", "And"),
        ("מֹשֶׁה", "מוסי'", "Moses"),
        ("וְאַהֲרֹן", "והרון", "and Aaron,"),
        ("וְכָל-עֲדַת", "וסאיר גמאעה'", "and the rest of the congregation of"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel,"),
        ("לַלְוִיִּם", "לאלליוניין", "did for the Levites"),
        ("כְּכֹל אֲשֶׁר-צִוָּה", "כגמיע מא אמר", "according to all that"),
        ("יְהוָה", "אללה", "God had commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses"),
        ("לַלְוִיִּם", "פי סבבהם", "concerning them —"),
        ("כֵּן-עָשׂוּ לָהֶם בְּנֵי יִשְׂרָאֵל", "כד'אך צנעו להם", "so they did for them."),
    ],
    21: [
        # HE: וַיִּתְחַטְּאוּ הַלְוִיִּם וַיְכַבְּסוּ בִּגְדֵיהֶם וַיָּנֶף אַהֲרֹן אֹתָם תְּנוּפָה לִפְנֵי יְהוָה וַיְכַפֵּר עֲלֵיהֶם אַהֲרֹן לְטַהֲרָם
        # JA: פתד'כו וג'סלו ת'יאבהם. וזפהם הרון זפא בין ידי אללה. ואסתג'פר ענהם וטהרהם
        # EN: And they were purified and washed their garments; and Aaron presented them as a presentation before God, and sought forgiveness for them and purified them.
        ("וַיִּתְחַטְּאוּ הַלְוִיִּם", "פתד'כו", "And they were purified"),
        ("וַיְכַבְּסוּ", "וג'סלו", "and washed"),
        ("בִּגְדֵיהֶם", "ת'יאבהם", "their garments;"),
        ("וַיָּנֶף", "וזפהם", "and Aaron presented them"),
        ("אַהֲרֹן", "הרון", "as a presentation"),
        ("תְּנוּפָה", "זפא", "before"),
        ("לִפְנֵי יְהוָה", "בין ידי אללה", "God,"),
        ("וַיְכַפֵּר עֲלֵיהֶם", "ואסתג'פר ענהם", "and sought forgiveness for them"),
        ("אַהֲרֹן לְטַהֲרָם", "וטהרהם", "and purified them."),
    ],
    22: [
        # HE: וְאַחֲרֵי-כֵן בָּאוּ הַלְוִיִּם לַעֲבֹד אֶת-עֲבֹדָתָם בְּאֹהֶל מוֹעֵד לִפְנֵי אַהֲרֹן וְלִפְנֵי בָנָיו כַּאֲשֶׁר צִוָּה יְהוָה אֶת-מֹשֶׁה עַל-הַלְוִיִּם כֵּן עָשׂוּ לָהֶם
        # JA: ובעד ד'אלך דכ'לו. ליכ'דמו כ'דמתהם פי כ'בא אלמחצ'ר. בין ידי הרון ובניה. כגמיע מא אמר אללה מוסי' בסבבהם. כד'אך צנעו להם
        # EN: And after that they entered to perform their service in the tent of meeting, before Aaron and his sons — according to all that God had commanded Moses concerning them, so they did for them.
        ("וְאַחֲרֵי-כֵן", "ובעד ד'אלך", "And after that"),
        ("בָּאוּ הַלְוִיִּם", "דכ'לו", "they entered"),
        ("לַעֲבֹד", "ליכ'דמו", "to perform"),
        ("אֶת-עֲבֹדָתָם", "כ'דמתהם", "their service"),
        ("בְּאֹהֶל מוֹעֵד", "פי כ'בא אלמחצ'ר", "in the tent of meeting,"),
        ("לִפְנֵי אַהֲרֹן", "בין ידי הרון", "before Aaron"),
        ("וְלִפְנֵי בָנָיו", "ובניה", "and his sons —"),
        ("כַּאֲשֶׁר צִוָּה", "כגמיע מא אמר", "according to all that"),
        ("יְהוָה", "אללה", "God had commanded"),
        ("אֶת-מֹשֶׁה", "מוסי'", "Moses"),
        ("עַל-הַלְוִיִּם", "בסבבהם", "concerning them,"),
        ("כֵּן עָשׂוּ לָהֶם", "כד'אך צנעו להם", "so they did for them."),
    ],
    23: [
        # HE: וַיְדַבֵּר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר
        # JA: ת'ם כלם אללה מוסי' תכלימא
        # EN: Then God spoke to Moses in speech.
        (None, "ת'ם", "Then"),
        ("וַיְדַבֵּר יְהוָה", "כלם אללה", "God spoke"),
        ("אֶל-מֹשֶׁה", "מוסי'", "to Moses"),
        ("לֵּאמֹר", "תכלימא", "in speech."),
    ],
    24: [
        # HE: זֹאת אֲשֶׁר לַלְוִיִּם מִבֶּן חָמֵשׁ וְעֶשְׂרִים שָׁנָה וָמַעְלָה יָבוֹא לִצְבֹא צָבָא בַּעֲבֹדַת אֹהֶל מוֹעֵד
        # JA: הד'א רסם אלליוניין. מן אבן כ'מסה ועשרין סנה פצאעדא. ידכל לאלגיש. לכ'דמה' כ'בא אלמחצ'ר
        # EN: 'This is the ordinance for the Levites: from twenty-five years of age and upward, one shall enter the host for the service of the tent of meeting.'
        ("זֹאת", "הד'א", "'This is"),
        ("אֲשֶׁר לַלְוִיִּם", "רסם אלליוניין", "the ordinance for the Levites:"),
        ("מִבֶּן", "מן אבן", "from"),
        ("חָמֵשׁ וְעֶשְׂרִים שָׁנָה", "כ'מסה ועשרין סנה", "twenty-five years of age"),
        ("וָמַעְלָה", "פצאעדא", "and upward,"),
        ("יָבוֹא", "ידכל", "one shall enter"),
        ("לִצְבֹא צָבָא", "לאלגיש", "the host"),
        ("בַּעֲבֹדַת אֹהֶל מוֹעֵד", "לכ'דמה' כ'בא אלמחצ'ר", "for the service of the tent of meeting.'"),
    ],
    25: [
        # HE: וּמִבֶּן חֲמִשִּׁים שָׁנָה יָשׁוּב מִצְּבָא הָעֲבֹדָה וְלֹא יַעֲבֹד עוֹד
        # JA: ומן אבן כ'מסין סנה. ירגע ענה. ולא יכ'דם אבדא
        # EN: 'And from fifty years of age he shall retire from it, and shall serve no more at all.'
        ("וּמִבֶּן", "ומן אבן", "'And from"),
        ("חֲמִשִּׁים שָׁנָה", "כ'מסין סנה", "fifty years of age"),
        ("יָשׁוּב", "ירגע", "he shall retire"),
        ("מִצְּבָא הָעֲבֹדָה", "ענה", "from it,"),
        ("וְלֹא יַעֲבֹד", "ולא יכ'דם", "and shall serve no more"),
        ("עוֹד", "אבדא", "at all.'"),
    ],
    26: [
        # HE: וְשֵׁרֵת אֶת-אֶחָיו בְּאֹהֶל מוֹעֵד לִשְׁמֹר מִשְׁמֶרֶת וַעֲבֹדָה לֹא יַעֲבֹד כָּכָה תַּעֲשֶׂה לַלְוִיִּם בְּמִשְׁמְרֹתָם
        # JA: לכן יכ'דם מע אכ'ותה. פי חפץ' כ'בא אלמחצ'ר. ואמא כ'דמתה אלאוולא פלא יכ'דם. כד'אך אצנע בהם פי מחפצ'הם
        # EN: 'But he may serve alongside his brothers in guarding the tent of meeting; as for his former service, he shall not serve. Thus shall you do for them in their charge.'
        (None, "לכן", "'But"),
        ("וְשֵׁרֵת", "יכ'דם", "he may serve"),
        ("אֶת-אֶחָיו", "מע אכ'ותה", "alongside his brothers"),
        ("בְּאֹהֶל מוֹעֵד", "פי חפץ' כ'בא אלמחצ'ר", "in guarding the tent of meeting;"),
        ("לִשְׁמֹר מִשְׁמֶרֶת", "ואמא כ'דמתה אלאוולא", "as for his former service,"),
        ("וַעֲבֹדָה לֹא יַעֲבֹד", "פלא יכ'דם", "he shall not serve."),
        ("כָּכָה תַּעֲשֶׂה לַלְוִיִּם", "כד'אך אצנע בהם", "Thus shall you do for them"),
        ("בְּמִשְׁמְרֹתָם", "פי מחפצ'הם", "in their charge.'"),
    ],
}

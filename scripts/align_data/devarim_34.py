"""Hand-authored alignment triples for Devarim chapter 34.

Word-level: each JA (Saadia) word or tight unit is its own group, mapped to
the Hebrew word it renders and its English counterpart. The runtime resolver
matches each side independently (lib/alignment.ts), so words link correctly
even across word-order crossings. Words Saadia adds with no Hebrew source
(glosses, expansions) carry he=None and link JA↔English only.

This is the final chapter of the Torah: Moses ascends Nebo, surveys the
Promised Land, dies "by the word of God" (עַל-פִּי יְהוָה → עלי' קול אללה),
is buried in an unknown grave, the 30-day mourning, Joshua's succession, and
the closing tribute — no prophet arose like Moses, whom God knew face-to-face.

Key Saadia moves:
 - עֶבֶד-יְהוָה → רסול אללה ("messenger of God"), his standard rendering
 - עַל-פִּי יְהוָה → עלי' קול אללה ("according to the word of God")
 - הַפִּסְגָּה → אלקלעה ("the fortress")
 - הַגִּלְעָד עַד-דָּן → מן גרש אלי' באניאס (Jerash to Banias — geographical rendering)
 - יְרֵחוֹ (first mention in v.1) → יריחא  repeated by Saadia as gloss clarification
 - לֹא-כָהֲתָה עֵינוֹ → לם תדמס עינה ("his eye had not grown dim")
 - וְלֹא-נָס לֵחֹה → ולא תזול רטובתה ("nor had his moisture departed")
 - פָּנִים אֶל-פָּנִים → שפאהא ("mouth to mouth / directly")
"""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        (None, "ת'ם", "Then"),
        ("וַיַּעַל", "צעד", "went up"),
        ("מֹשֶׁה", "מוסי'", "Moses"),
        ("מֵעַרְבֹת", "מן בידאת", "from the wilderness of"),
        ("מוֹאָב", "מואב", "Moab"),
        ("אֶל-הַר", "אלי' גבל", "to Mount"),
        ("נְבוֹ", "נבו", "Nebo"),
        ("רֹאשׁ", "ראס", "the summit of"),
        ("הַפִּסְגָּה", "אלקלעה", "the fortress"),
        ("אֲשֶׁר עַל-פְּנֵי", "אלתי בחצ'רה'", "which is opposite"),
        ("יְרֵחוֹ", "יריחא", "Jericho"),
        ("וַיַּרְאֵהוּ יְהוָה", "פאוראה אללה גמיע יריחא", "and God showed him all of Jericho"),
        (None, "פאוראה אללה", "and God showed him"),
        ("אֶת-כָּל-הָאָרֶץ", "גמיע אלבלד", "all the land"),
        ("אֶת-הַגִּלְעָד עַד-דָּן", "מן גרש אלי' באניאס", "from Jerash to Banias"),
    ],
    2: [
        ("וְאֵת כָּל-נַפְתָּלִי", "וגמיע בלד נפתלי", "And all the land of Naphtali"),
        ("וְאֶת-אֶרֶץ אֶפְרַיִם", "ואפרים", "and Ephraim"),
        ("וּמְנַשֶּׁה", "ומנשה", "and Manasseh"),
        ("וְאֵת כָּל-אֶרֶץ יְהוּדָה", "וגמיע בלד יהודה", "and all the land of Judah"),
        ("עַד הַיָּם הָאַחֲרוֹן", "אלי' אלבחר אלג'רבי", "to the Western Sea"),
    ],
    3: [
        ("וְאֶת-הַנֶּגֶב", "ואלדארום", "And the south"),
        ("וְאֶת-הַכִּכָּר", "ואלמרג", "and the meadows"),
        ("בִּקְעַת יְרֵחוֹ", "בקיע יריחא", "the valley of Jericho"),
        ("עִיר הַתְּמָרִים", "קריה' אלנכ'ל", "the town of palms"),
        ("עַד-צֹעַר", "אלי' זג'ר", "as far as Zoar"),
    ],
    4: [
        ("וַיֹּאמֶר", "פקאל", "And He said"),
        ("יְהוָה", "לה", "to him"),
        ("אֵלָיו", "הד'א", "This is"),
        ("זֹאת הָאָרֶץ", "אלבלד", "the land"),
        ("אֲשֶׁר נִשְׁבַּעְתִּי", "אלד'י אקסמת", "which I swore"),
        ("לְאַבְרָהָם", "לאברהים", "to Abraham"),
        ("לְיִצְחָק", "ויצחק", "and Isaac"),
        ("וּלְיַעֲקֹב", "ויעקוב", "and Jacob"),
        ("לֵאמֹר", "קאילא", "saying"),
        ("לְזַרְעֲךָ", "לנסלכם", "To your offspring"),
        ("אֶתְּנֶנָּה", "אעטיה", "I shall give it"),
        ("הֶרְאִיתִיךָ", "קד אוריתכהא", "I have shown it to you"),
        ("בְעֵינֶיךָ", "בעינאך", "with your own eyes"),
        ("וְשָׁמָּה", "ואלי ת'ם", "to there"),
        ("לֹא תַעֲבֹר", "לא תעבר", "but you shall not cross over"),
    ],
    5: [
        ("וַיָּמָת", "פמאת", "died"),
        ("מֹשֶׁה", "מוסי'", "And Moses"),
        ("עֶבֶד-יְהוָה", "רסול אללה", "the messenger of God"),
        (None, "פי", "in"),
        ("בְּאֶרֶץ", "בלד", "the land of"),
        ("מוֹאָב", "מואב", "Moab"),
        ("עַל-פִּי", "עלי' קול", "according to the word of"),
        ("יְהוָה", "אללה", "God"),
    ],
    6: [
        ("וַיִּקְבֹּר", "ודפנה", "And He buried him"),
        ("בַגַּי", "פי אלואד", "in the valley"),
        ("בְּאֶרֶץ מוֹאָב", "פי בלד מואב", "in the land of Moab"),
        ("מוּל בֵּית פְּעוֹר", "ממא ילי בית פעור", "in the vicinity of Beth-Peor"),
        ("וְלֹא-יָדַע אִישׁ", "ולם יעלם אחד", "and no one has known"),
        ("אֶת-קְבֻרָתוֹ", "בקברה", "the place of his grave"),
        ("עַד הַיּוֹם הַזֶּה", "אלי' יומנא הד'א", "to this day"),
    ],
    7: [
        ("וּמֹשֶׁה", "וכאן מוסי'", "And Moses was"),
        ("בֶּן-מֵאָה וְעֶשְׂרִים שָׁנָה", "אבן מאיה ועשרין סנה", "one hundred and twenty years old"),
        ("בְּמֹתוֹ", "אד' מאת", "when he died"),
        ("לֹא-כָהֲתָה עֵינוֹ", "לם תדמס עינה", "his eye had not grown dim"),
        ("וְלֹא-נָס לֵחֹה", "ולא תזול רטובתה", "nor had his moisture departed"),
    ],
    8: [
        ("וַיִּבְכּוּ", "פבכא", "wept"),
        ("בְנֵי יִשְׂרָאֵל", "בני אסראיל", "And the sons of Israel"),
        ("אֶת-מֹשֶׁה", "עלי' מוסי'", "for Moses"),
        ("בְּעַרְבֹת מוֹאָב", "פי בידאת מואב", "in the wilderness of Moab"),
        ("שְׁלֹשִׁים יוֹם", "ת'לאת'ין יומא", "thirty days"),
        ("וַיִּתְּמוּ", "אלי' אן אנקצ'ת", "until"),
        ("יְמֵי בְכִי אֵבֶל מֹשֶׁה", "אייאם חזנה", "the days of mourning for him were completed"),
    ],
    9: [
        ("וִיהוֹשֻׁעַ", "ויהושע", "And Joshua"),
        ("בִּן-נוּן", "אבן נון", "son of Nun"),
        ("מָלֵא", "אמתלי'", "was filled with"),
        ("רוּחַ חָכְמָה", "רוח אלחכמה", "the spirit of wisdom"),
        ("כִּי-סָמַךְ", "אד' סנד", "since"),
        ("מֹשֶׁה", "מוסי'", "Moses"),
        ("אֶת-יָדָיו עָלָיו", "ידיה עליה", "had laid his hands upon him"),
        ("בְּנֵי-יִשְׂרָאֵל", "בני אסראיל", "the sons of Israel"),
        ("וַיִּשְׁמְעוּ אֵלָיו", "פקבלו מנה", "accepted from him"),
        ("וַיַּעֲשׂוּ", "פעמלו", "and acted accordingly"),
        ("כַּאֲשֶׁר צִוָּה", "כמא אמר", "as"),
        ("יְהוָה", "אללה", "God"),
        ("אֶת-מֹשֶׁה", "מוסי'", "had commanded Moses"),
    ],
    10: [
        ("וְלֹא-קָם", "ולם יקום", "And there arose no"),
        ("נָבִיא", "נבי", "prophet"),
        ("עוֹד", "בעד ד'אלך", "again"),
        ("בְּיִשְׂרָאֵל", "לאל אסראיל", "in Israel"),
        ("כְּמֹשֶׁה", "מת'ל מוסי", "like Moses"),
        ("אֲשֶׁר יְדָעוֹ יְהוָה", "לאן אללה נאגאה", "for God had spoken with him"),
        ("פָּנִים אֶל-פָּנִים", "שפאהא", "directly, mouth to mouth"),
    ],
    11: [
        ("לְכָל-הָאֹתֹת", "ולסאיר אלאיאת", "And for all the signs"),
        ("וְהַמּוֹפְתִים", "ואלבראהין", "and the proofs"),
        ("אֲשֶׁר שְׁלָחוֹ יְהוָה", "אלד'י בעת' בהא אללה", "which God sent him"),
        ("לַעֲשׂוֹת", "ליצנעהא", "to perform"),
        ("בְּאֶרֶץ מִצְרָיִם", "פי בלד מצר", "in the land of Egypt"),
        ("לְפַרְעֹה", "בפרעון", "against Pharaoh"),
        ("וּלְכָל-עֲבָדָיו", "ובגמיע קואדה", "and against all his officers"),
        ("וּלְכָל-אַרְצוֹ", "ובסאיר אהל בלדה", "and against the rest of the people of his land"),
    ],
    12: [
        ("וּלְכֹל הַיָּד הַחֲזָקָה", "ולסאיר אליד אלשדידה", "and for all the mighty hand"),
        ("וּלְכֹל הַמּוֹרָא הַגָּדוֹל", "ולסאיר אלמכ'אוף אל]עט'ימה] עצ'ימה", "and for all the great terrors"),
        ("אֲשֶׁר עָשָׂה", "אלתי צנעהא", "which"),
        ("מֹשֶׁה", "מוסי'", "Moses wrought"),
        ("לְעֵינֵי כָּל-יִשְׂרָאֵל", "בחצרה' גמיע אל אסראיל", "in the presence of all the house of Israel"),
    ],
}

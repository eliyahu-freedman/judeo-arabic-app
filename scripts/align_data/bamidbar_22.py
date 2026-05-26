"""Hand-authored word-level alignment triples for Bamidbar chapter 22."""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        # HE: וַיִּסְעוּ בְּנֵי יִשְׂרָאֵל וַיַּחֲנוּ בְּעַרְבוֹת מוֹאָב מֵעֵבֶר לְיַרְדֵּן יְרֵחוֹ
        # JA: ת'ם רחלו בני אסראיל. ונזלו פי בידאת מואב. אלתי עלי' ארדן יריחא
        # EN: Then the sons of Israel journeyed, and encamped in the wilderness of Moab, which is by the Jordan of Jericho.
        (None, "ת'ם", "Then"),
        ("וַיִּסְעוּ", "רחלו", "journeyed,"),
        ("בְּנֵי", "בני", "the sons of"),
        ("יִשְׂרָאֵל", "אסראיל", "Israel"),
        ("וַיַּחֲנוּ", "ונזלו", "and encamped"),
        ("בְּעַרְבוֹת", "פי בידאת", "in the wilderness of"),
        ("מוֹאָב", "מואב", "Moab,"),
        ("מֵעֵבֶר", "אלתי עלי'", "which is by"),
        ("לְיַרְדֵּן", "ארדן", "the Jordan of"),
        ("יְרֵחוֹ", "יריחא", "Jericho."),
    ],
    2: [
        # HE: וַיַּרְא בָּלָק בֶּן-צִפּוֹר אֵת כָּל-אֲשֶׁר-עָשָׂה יִשְׂרָאֵל לָאֱמֹרִי
        # JA: ולמא ראא בלק אבן צפור. גמיע מא צנע אל אסראיל באלאמוריין
        # EN: And when Balak son of Zippor saw all that the people of Israel had done to the Amorites,
        ("וַיַּרְא", "ולמא ראא", "And when"),
        ("בָּלָק", "בלק", "Balak"),
        ("בֶּן-צִפּוֹר", "אבן צפור", "son of Zippor"),
        (None, "גמיע מא", "saw all that"),
        ("אֵת כָּל-אֲשֶׁר-עָשָׂה", "צנע", "had done"),
        ("יִשְׂרָאֵל", "אל אסראיל", "the people of Israel"),
        ("לָאֱמֹרִי", "באלאמוריין", "to the Amorites,"),
    ],
    3: [
        # HE: וַיָּגָר מוֹאָב מִפְּנֵי הָעָם מְאֹד--כִּי רַב-הוּא וַיָּקָץ מוֹאָב מִפְּנֵי בְּנֵי יִשְׂרָאֵל
        # JA: פחד'ר אלמואביין. מן קבל אלקום. גדא אד' הם כ'תירין. וצ'גרו מנהם
        # EN: the Moabites were greatly wary of the people, since they are numerous; and they were filled with dread because of them.
        ("וַיָּגָר", "פחד'ר", "the Moabites were"),
        ("מוֹאָב", "אלמואביין", "greatly wary"),
        ("מִפְּנֵי", "מן קבל", "of the people,"),
        ("הָעָם", "אלקום", "since"),
        ("מְאֹד", "גדא", "they are numerous;"),
        ("כִּי רַב-הוּא", "אד' הם כ'תירין", "and they were filled with dread"),
        ("וַיָּקָץ מוֹאָב מִפְּנֵי בְּנֵי יִשְׂרָאֵל", "וצ'גרו מנהם", "because of them."),
    ],
    4: [
        # HE: וַיֹּאמֶר מוֹאָב אֶל-זִקְנֵי מִדְיָן עַתָּה יְלַחֲכוּ הַקָּהָל אֶת-כָּל-סְבִיבֹתֵינוּ כִּלְחֹךְ הַשּׁוֹר אֵת יֶרֶק הַשָּׂדֶה וּבָלָק בֶּן-צִפּוֹר מֶלֶךְ לְמוֹאָב בָּעֵת הַהִוא
        # JA: פקאל לשיוך' מדין. אלאן סילחס הולאי אלגוק כל נאס חואלינא. כמא ילחס אלת'ור כ'צ'ר אלצחרא. וכאן בלק אבן צפור. מלכהם פי ד'אלך אלוקת
        # EN: And they said to the elders of Midian: 'Now this horde will lick up all the people around us, as the ox licks up the green of the wilderness.' And Balak son of Zippor was their king at that time.
        ("וַיֹּאמֶר מוֹאָב", "פקאל", "And they said"),
        ("אֶל-זִקְנֵי", "לשיוך'", "to the elders of"),
        ("מִדְיָן", "מדין", "Midian:"),
        ("עַתָּה", "אלאן", "'Now"),
        ("יְלַחֲכוּ", "סילחס", "will lick up"),
        ("הַקָּהָל", "הולאי אלגוק", "this horde"),
        ("אֶת-כָּל-סְבִיבֹתֵינוּ", "כל נאס חואלינא", "all the people around us,"),
        ("כִּלְחֹךְ", "כמא ילחס", "as the ox licks up"),
        ("הַשּׁוֹר", "אלת'ור", "the green of"),
        ("אֵת יֶרֶק הַשָּׂדֶה", "כ'צ'ר אלצחרא", "the wilderness.'"),
        ("וּבָלָק", "וכאן בלק", "And Balak"),
        ("בֶּן-צִפּוֹר", "אבן צפור", "son of Zippor"),
        ("מֶלֶךְ לְמוֹאָב", "מלכהם", "was their king"),
        ("בָּעֵת הַהִוא", "פי ד'אלך אלוקת", "at that time."),
    ],
    5: [
        # HE: וַיִּשְׁלַח מַלְאָכִים אֶל-בִּלְעָם בֶּן-בְּעֹר פְּתוֹרָה אֲשֶׁר עַל-הַנָּהָר אֶרֶץ בְּנֵי-עַמּוֹ--לִקְרֹא-לוֹ לֵאמֹר הִנֵּה עַם יָצָא מִמִּצְרַיִם הִנֵּה כִסָּה אֶת-עֵין הָאָרֶץ וְהוּא יֹשֵׁב מִמֻּלִי
        # JA: פבעת' ברסל אלי' בלעם אבן בעור. אלי' פאתורא. אלד'י עלי' אלפראת. בלד קומה לידעו בה. וקאל לה הוד'א קום כ'רג מן מצר קד ג'טא צ'אהר אלארץ' והו גאלס מקאבלי
        # EN: And he sent messengers to Balaam son of Beor, to Pethor which is on the Euphrates, the land of his people, to invite him; and said to him: 'Behold, a people has come out of Egypt — it has already covered the face of the land, and it sits encamped opposite me.
        ("וַיִּשְׁלַח", "פבעת'", "And he sent"),
        ("מַלְאָכִים", "ברסל", "messengers"),
        ("אֶל-בִּלְעָם", "אלי' בלעם", "to Balaam"),
        ("בֶּן-בְּעֹר", "אבן בעור", "son of Beor,"),
        ("פְּתוֹרָה", "אלי' פאתורא", "to Pethor"),
        ("אֲשֶׁר עַל-הַנָּהָר", "אלד'י עלי' אלפראת", "which is on the Euphrates,"),
        ("אֶרֶץ בְּנֵי-עַמּוֹ", "בלד קומה", "the land of his people,"),
        ("לִקְרֹא-לוֹ", "לידעו בה", "to invite him;"),
        ("לֵאמֹר", "וקאל לה", "and said to him:"),
        ("הִנֵּה עַם", "הוד'א קום", "'Behold, a people"),
        ("יָצָא", "כ'רג", "has come out"),
        ("מִמִּצְרַיִם", "מן מצר", "of Egypt —"),
        ("הִנֵּה כִסָּה", "קד ג'טא", "it has already covered"),
        ("אֶת-עֵין הָאָרֶץ", "צ'אהר אלארץ'", "the face of the land,"),
        ("וְהוּא יֹשֵׁב", "והו גאלס", "and it sits encamped"),
        ("מִמֻּלִי", "מקאבלי", "opposite me."),
    ],
    6: [
        # HE: וְעַתָּה לְכָה-נָּא אָרָה-לִּי אֶת-הָעָם הַזֶּה כִּי-עָצוּם הוּא מִמֶּנִּי--אוּלַי אוּכַל נַכֶּה-בּוֹ וַאֲגָרְשֶׁנּוּ מִן-הָאָרֶץ כִּי יָדַעְתִּי אֵת אֲשֶׁר-תְּבָרֵךְ מְבֹרָךְ וַאֲשֶׁר תָּאֹר יוּאָר
        # JA: ואלאן פתעאל אלענה לי. אד' הם א עצ'ם מני. פלעלי' אסתטיע אן אחארבה. ואטרדה מן אלבלד. לאני אעלם. אן מן תבארכה מבארך. ומן תלענה ילען
        # EN: And now, come and curse it for me, since they are stronger than I; perhaps I shall be able to fight against it and drive it out of the land — for I know that he whom you bless is blessed, and he whom you curse is cursed.'
        ("וְעַתָּה", "ואלאן", "And now,"),
        ("לְכָה-נָּא", "פתעאל", "come"),
        ("אָרָה-לִּי", "אלענה לי", "and curse it for me,"),
        ("כִּי-עָצוּם הוּא מִמֶּנִּי", "אד' הם א עצ'ם מני", "since they are stronger than I;"),
        ("אוּלַי אוּכַל", "פלעלי' אסתטיע", "perhaps I shall be able"),
        ("נַכֶּה-בּוֹ", "אן אחארבה", "to fight against it"),
        ("וַאֲגָרְשֶׁנּוּ", "ואטרדה", "and drive it out"),
        ("מִן-הָאָרֶץ", "מן אלבלד", "of the land —"),
        ("כִּי יָדַעְתִּי", "לאני אעלם", "for I know"),
        ("אֵת אֲשֶׁר-תְּבָרֵךְ", "אן מן תבארכה", "that he whom you bless"),
        ("מְבֹרָךְ", "מבארך", "is blessed,"),
        ("וַאֲשֶׁר תָּאֹר", "ומן תלענה", "and he whom you curse"),
        ("יוּאָר", "ילען", "is cursed.'"),
    ],
    7: [
        # HE: וַיֵּלְכוּ זִקְנֵי מוֹאָב וְזִקְנֵי מִדְיָן וּקְסָמִים בְּיָדָם וַיָּבֹאוּ אֶל-בִּלְעָם וַיְדַבְּרוּ אֵלָיו דִּבְרֵי בָלָק
        # JA: פמצ'ו שיוך' מואב ושיוך' מדין. ופאלאת מעהם. חתי' ואפו בלעם. פאכ'ברוה בכלאם בלק
        # EN: And the elders of Moab and the elders of Midian went, with divination-fees with them, until they reached Balaam, and told him the words of Balak.
        ("וַיֵּלְכוּ", "פמצ'ו", "And"),
        ("זִקְנֵי מוֹאָב", "שיוך' מואב", "the elders of Moab"),
        ("וְזִקְנֵי", "ושיוך'", "and the elders of"),
        ("מִדְיָן", "מדין", "Midian went,"),
        ("וּקְסָמִים בְּיָדָם", "ופאלאת מעהם", "with divination-fees with them,"),
        ("וַיָּבֹאוּ אֶל-בִּלְעָם", "חתי' ואפו בלעם", "until they reached Balaam,"),
        ("וַיְדַבְּרוּ אֵלָיו", "פאכ'ברוה", "and told him"),
        ("דִּבְרֵי בָלָק", "בכלאם בלק", "the words of Balak."),
    ],
    8: [
        # HE: וַיֹּאמֶר אֲלֵיהֶם לִינוּ פֹה הַלַּיְלָה וַהֲשִׁבֹתִי אֶתְכֶם דָּבָר כַּאֲשֶׁר יְדַבֵּר יְהוָה אֵלָי וַיֵּשְׁבוּ שָׂרֵי-מוֹאָב עִם-בִּלְעָם
        # JA: פקאל להם. ביתו ההנא אללילה. וארד עלי'כם גואבא. כמא יקול אללה לי. פאקאם רויסא מואב ענד בלעם
        # EN: And he said to them: 'Lodge here tonight, and I shall bring you back an answer, as God shall say to me.' And the officers of Moab stayed with Balaam.
        ("וַיֹּאמֶר", "פקאל", "And he said"),
        ("אֲלֵיהֶם", "להם", "to them:"),
        ("לִינוּ", "ביתו", "'Lodge"),
        ("פֹה", "ההנא", "here"),
        ("הַלַּיְלָה", "אללילה", "tonight,"),
        ("וַהֲשִׁבֹתִי אֶתְכֶם", "וארד עלי'כם", "and I shall bring you back"),
        ("דָּבָר", "גואבא", "an answer,"),
        ("כַּאֲשֶׁר יְדַבֵּר", "כמא יקול", "as"),
        ("יְהוָה", "אללה", "God"),
        ("אֵלָי", "לי", "shall say to me.'"),
        ("וַיֵּשְׁבוּ", "פאקאם", "And"),
        ("שָׂרֵי-מוֹאָב", "רויסא מואב", "the officers of Moab"),
        ("עִם-בִּלְעָם", "ענד בלעם", "stayed with Balaam."),
    ],
    9: [
        # HE: וַיָּבֹא אֱלֹהִים אֶל-בִּלְעָם וַיֹּאמֶר מִי הָאֲנָשִׁים הָאֵלֶּה עִמָּךְ
        # JA: פואפא אמר אללה בלעם. וקאל מפתתחא. מן הולאי אלקום אלד'ין מעך
        # EN: And the decree of God came to Balaam, and said, opening the speech: 'Who are these people that are with you?'
        ("וַיָּבֹא אֱלֹהִים", "פואפא אמר אללה", "And the decree of God"),
        ("אֶל-בִּלְעָם", "בלעם", "came to Balaam,"),
        ("וַיֹּאמֶר", "וקאל", "and said,"),
        (None, "מפתתחא", "opening the speech:"),
        ("מִי הָאֲנָשִׁים", "מן הולאי אלקום", "'Who are these people"),
        ("הָאֵלֶּה עִמָּךְ", "אלד'ין מעך", "that are with you?'"),
    ],
    10: [
        # HE: וַיֹּאמֶר בִּלְעָם אֶל-הָאֱלֹהִים בָּלָק בֶּן-צִפֹּר מֶלֶךְ מוֹאָב שָׁלַח אֵלָי
        # JA: קאל. אן בלק אבן צפור. מלך מואב בעת' בהם אלי'י
        # EN: He said: 'Balak son of Zippor, king of Moab, has sent them to me,
        ("וַיֹּאמֶר בִּלְעָם", "קאל", "He said:"),
        ("בָּלָק", "אן בלק", "'Balak"),
        ("בֶּן-צִפֹּר", "אבן צפור", "son of Zippor,"),
        ("מֶלֶךְ מוֹאָב", "מלך מואב", "king of Moab,"),
        ("שָׁלַח אֵלָי", "בעת' בהם אלי'י", "has sent them to me,"),
    ],
    11: [
        # HE: הִנֵּה הָעָם הַיֹּצֵא מִמִּצְרַיִם וַיְכַס אֶת-עֵין הָאָרֶץ עַתָּה לְכָה קָבָה-לִּי אֹתוֹ--אוּלַי אוּכַל לְהִלָּחֶם בּוֹ וְגֵרַשְׁתִּיו
        # JA: יקול אן אלקום אלד'י כ'רג מן מצר. קד ג'טא צ'אהר אלארץ'. אלאן תעאל סבה לי. לעלי' אסתטיע אן אחארבה ואטרדה
        # EN: saying: Behold, the people that came out of Egypt has already covered the face of the land. Now come, curse it for me; perhaps I shall be able to fight against it and drive it out.'
        (None, "יקול", "saying:"),
        ("הִנֵּה הָעָם", "אן אלקום", "Behold, the people"),
        ("הַיֹּצֵא", "אלד'י כ'רג", "that came out"),
        ("מִמִּצְרַיִם", "מן מצר", "of Egypt"),
        ("וַיְכַס אֶת-עֵין הָאָרֶץ", "קד ג'טא צ'אהר אלארץ'", "has already covered the face of the land."),
        ("עַתָּה לְכָה", "אלאן תעאל", "Now come,"),
        ("קָבָה-לִּי", "סבה לי", "curse it for me;"),
        ("אוּלַי אוּכַל", "לעלי' אסתטיע", "perhaps I shall be able"),
        ("לְהִלָּחֶם בּוֹ", "אן אחארבה", "to fight against it"),
        ("וְגֵרַשְׁתִּיו", "ואטרדה", "and drive it out.'"),
    ],
    12: [
        # HE: וַיֹּאמֶר אֱלֹהִים אֶל-בִּלְעָם לֹא תֵלֵךְ עִמָּהֶם לֹא תָאֹר אֶת-הָעָם כִּי בָרוּךְ הוּא
        # JA: קאל לה לא תמץ' מעהם. ולא תלען אלקום. פאנה מבארך
        # EN: He said to him: 'Do not go with them, and do not curse the people — for it is blessed.'
        ("וַיֹּאמֶר אֱלֹהִים", "קאל לה", "He said to him:"),
        ("לֹא תֵלֵךְ", "לא תמץ'", "'Do not go"),
        ("עִמָּהֶם", "מעהם", "with them,"),
        ("לֹא תָאֹר", "ולא תלען", "and do not curse"),
        ("אֶת-הָעָם", "אלקום", "the people —"),
        ("כִּי בָרוּךְ הוּא", "פאנה מבארך", "for it is blessed.'"),
    ],
    13: [
        # HE: וַיָּקָם בִּלְעָם בַּבֹּקֶר וַיֹּאמֶר אֶל-שָׂרֵי בָלָק לְכוּ אֶל-אַרְצְכֶם כִּי מֵאֵן יְהוָה לְתִתִּי לַהֲלֹךְ עִמָּכֶם
        # JA: פקאם באלג'דאה. פקאל לרויסא בלק. אמצ'ו אלי' בלדכם. לאן אללה נהאני. אן אמצ'י מעכם
        # EN: And he rose in the morning, and said to the officers of Balak: 'Go back to your land, for God has forbidden me to go with you.'
        ("וַיָּקָם בִּלְעָם", "פקאם", "And he rose"),
        ("בַּבֹּקֶר", "באלג'דאה", "in the morning,"),
        ("וַיֹּאמֶר", "פקאל", "and said"),
        ("אֶל-שָׂרֵי בָלָק", "לרויסא בלק", "to the officers of Balak:"),
        ("לְכוּ", "אמצ'ו", "'Go back"),
        ("אֶל-אַרְצְכֶם", "אלי' בלדכם", "to your land,"),
        ("כִּי מֵאֵן יְהוָה", "לאן אללה נהאני", "for God has forbidden me"),
        ("לְתִתִּי לַהֲלֹךְ", "אן אמצ'י", "to go"),
        ("עִמָּכֶם", "מעכם", "with you.'"),
    ],
    14: [
        # HE: וַיָּקוּמוּ שָׂרֵי מוֹאָב וַיָּבֹאוּ אֶל-בָּלָק וַיֹּאמְרוּ מֵאֵן בִּלְעָם הֲלֹךְ עִמָּנוּ
        # JA: פקאם רויסא מואב. וגאו אלי' בלק. וקאלו. קד אבא בלעם אן יגי מענא
        # EN: And the officers of Moab arose, and came to Balak, and said: 'Balaam has refused to come with us.'
        ("וַיָּקוּמוּ", "פקאם", "And"),
        ("שָׂרֵי מוֹאָב", "רויסא מואב", "the officers of Moab arose,"),
        ("וַיָּבֹאוּ", "וגאו", "and came"),
        ("אֶל-בָּלָק", "אלי' בלק", "to Balak,"),
        ("וַיֹּאמְרוּ", "וקאלו", "and said:"),
        ("מֵאֵן בִּלְעָם", "קד אבא בלעם", "'Balaam has refused"),
        ("הֲלֹךְ עִמָּנוּ", "אן יגי מענא", "to come with us.'"),
    ],
    15: [
        # HE: וַיֹּסֶף עוֹד בָּלָק שְׁלֹחַ שָׂרִים רַבִּים וְנִכְבָּדִים מֵאֵלֶּה
        # JA: פעאוד בלק איצ'א. בעת' רויסא. א עצ'ם ואגל מן אולאיך
        # EN: And Balak again sent officers — greater and more honored than those.
        ("וַיֹּסֶף עוֹד", "פעאוד", "And"),
        ("בָּלָק", "בלק איצ'א", "Balak again"),
        ("שְׁלֹחַ", "בעת'", "sent"),
        ("שָׂרִים", "רויסא", "officers —"),
        ("רַבִּים", "א עצ'ם", "greater"),
        ("וְנִכְבָּדִים", "ואגל", "and more honored"),
        ("מֵאֵלֶּה", "מן אולאיך", "than those."),
    ],
    16: [
        # HE: וַיָּבֹאוּ אֶל-בִּלְעָם וַיֹּאמְרוּ לוֹ כֹּה אָמַר בָּלָק בֶּן-צִפּוֹר אַל-נָא תִמָּנַע מֵהֲלֹךְ אֵלָי
        # JA: פגאו אלי' בלעם. וקאלו לה. כד'א קאל בלק אבן צפור. לא תמתנע מן אלמציר אלי'י
        # EN: And they came to Balaam, and said to him: 'Thus says Balak son of Zippor: Do not hold yourself back from journeying to me.
        ("וַיָּבֹאוּ", "פגאו", "And they came"),
        ("אֶל-בִּלְעָם", "אלי' בלעם", "to Balaam,"),
        ("וַיֹּאמְרוּ לוֹ", "וקאלו לה", "and said to him:"),
        ("כֹּה אָמַר", "כד'א קאל", "'Thus says"),
        ("בָּלָק", "בלק", "Balak"),
        ("בֶּן-צִפּוֹר", "אבן צפור", "son of Zippor:"),
        ("אַל-נָא תִמָּנַע", "לא תמתנע", "Do not hold yourself back"),
        ("מֵהֲלֹךְ", "מן אלמציר", "from journeying"),
        ("אֵלָי", "אלי'י", "to me."),
    ],
    17: [
        # HE: כִּי-כַבֵּד אֲכַבֶּדְךָ מְאֹד וְכֹל אֲשֶׁר-תֹּאמַר אֵלַי אֶעֱשֶׂה וּלְכָה-נָּא קָבָה-לִּי אֵת הָעָם הַזֶּה
        # JA: פאני סאכרמך גדא. וכל מא תקול לי אצנעה. ותעאל אלען לי הולאי אלקום
        # EN: For I will honor you greatly, and whatever you say to me I will do — come, curse this people for me.'
        ("כִּי-כַבֵּד אֲכַבֶּדְךָ", "פאני סאכרמך", "For I will honor you"),
        ("מְאֹד", "גדא", "greatly,"),
        ("וְכֹל אֲשֶׁר-תֹּאמַר", "וכל מא תקול", "and whatever you say"),
        ("אֵלַי", "לי", "to me"),
        ("אֶעֱשֶׂה", "אצנעה", "I will do —"),
        ("וּלְכָה-נָּא", "ותעאל", "come,"),
        ("קָבָה-לִּי", "אלען לי", "curse"),
        ("אֵת הָעָם הַזֶּה", "הולאי אלקום", "this people for me.'"),
    ],
    18: [
        # HE: וַיַּעַן בִּלְעָם וַיֹּאמֶר אֶל-עַבְדֵי בָלָק אִם-יִתֶּן-לִי בָלָק מְלֹא בֵיתוֹ כֶּסֶף וְזָהָב--לֹא אוּכַל לַעֲבֹר אֶת-פִּי יְהוָה אֱלֹהָי לַעֲשׂוֹת קְטַנָּה אוֹ גְדוֹלָה
        # JA: פאגאב בלעם קואד בלק וקאל להם. לו אעטאני בלק. מל ביתה פצ'ה וד'הב. לא אסתטיע אן אתגאוז אמר אללה רבי. פאעמל צג'ירה או כבירה
        # EN: And Balaam answered the commanders of Balak, and said to them: 'Even if Balak were to give me his houseful of silver and gold, I cannot transgress the command of God my Lord, to do a small thing or a great thing.
        ("וַיַּעַן בִּלְעָם", "פאגאב בלעם", "And Balaam answered"),
        ("אֶל-עַבְדֵי בָלָק", "קואד בלק", "the commanders of Balak,"),
        ("וַיֹּאמֶר", "וקאל להם", "and said to them:"),
        ("אִם-יִתֶּן-לִי", "לו אעטאני", "'Even if"),
        ("בָלָק", "בלק", "Balak were to give me"),
        ("מְלֹא בֵיתוֹ", "מל ביתה", "his houseful of"),
        ("כֶּסֶף", "פצ'ה", "silver"),
        ("וְזָהָב", "וד'הב", "and gold,"),
        ("לֹא אוּכַל לַעֲבֹר", "לא אסתטיע אן אתגאוז", "I cannot transgress"),
        ("אֶת-פִּי יְהוָה", "אמר אללה", "the command of God"),
        ("אֱלֹהָי", "רבי", "my Lord,"),
        ("לַעֲשׂוֹת", "פאעמל", "to do"),
        ("קְטַנָּה", "צג'ירה", "a small thing"),
        ("אוֹ גְדוֹלָה", "או כבירה", "or a great thing."),
    ],
    19: [
        # HE: וְעַתָּה שְׁבוּ נָא בָזֶה גַּם-אַתֶּם--הַלָּיְלָה וְאֵדְעָה מַה-יֹּסֵף יְהוָה דַּבֵּר עִמִּי
        # JA: ואלאן אקימו אנתם איצ'א. ההנא אללילה. חתי' אנצ'ר מא יעאוד אללה אן יכ'אטבני בה
        # EN: And now, stay here also tonight, that I may see what God will again address to me.'
        ("וְעַתָּה", "ואלאן", "And now,"),
        ("שְׁבוּ נָא", "אקימו", "stay"),
        ("גַּם-אַתֶּם", "אנתם איצ'א", "here also"),
        ("הַלָּיְלָה", "ההנא אללילה", "tonight,"),
        ("וְאֵדְעָה", "חתי' אנצ'ר", "that I may see"),
        ("מַה-יֹּסֵף", "מא יעאוד", "what"),
        ("יְהוָה", "אללה", "God"),
        ("דַּבֵּר עִמִּי", "אן יכ'אטבני בה", "will again address to me.'"),
    ],
    20: [
        # HE: וַיָּבֹא אֱלֹהִים אֶל-בִּלְעָם לַיְלָה וַיֹּאמֶר לוֹ אִם-לִקְרֹא לְךָ בָּאוּ הָאֲנָשִׁים קוּם לֵךְ אִתָּם וְאַךְ אֶת-הַדָּבָר אֲשֶׁר-אֲדַבֵּר אֵלֶיךָ--אֹתוֹ תַעֲשֶׂה
        # JA: פואפא אמר אללה בלעם לילא. וקאל. אן כאן הולאי אלקום גאו לידעוך. פקום אמץ' מעהם. לכן אלאמר. אלד'י אקולה לך אצנעה פקט
        # EN: And the decree of God came to Balaam at night, and said: 'If these people have come to invite you, arise, go with them — but only the word that I shall tell you, that alone do.'
        ("וַיָּבֹא אֱלֹהִים", "פואפא אמר אללה", "And the decree of God"),
        ("אֶל-בִּלְעָם", "בלעם", "came to Balaam"),
        ("לַיְלָה", "לילא", "at night,"),
        ("וַיֹּאמֶר לוֹ", "וקאל", "and said:"),
        ("אִם-לִקְרֹא לְךָ", "אן כאן הולאי אלקום גאו לידעוך", "'If these people have come to invite you,"),
        ("קוּם", "פקום", "arise,"),
        ("לֵךְ אִתָּם", "אמץ' מעהם", "go with them —"),
        ("וְאַךְ", "לכן", "but"),
        ("אֶת-הַדָּבָר", "אלאמר", "only the word"),
        ("אֲשֶׁר-אֲדַבֵּר אֵלֶיךָ", "אלד'י אקולה לך", "that I shall tell you,"),
        ("אֹתוֹ תַעֲשֶׂה", "אצנעה פקט", "that alone do.'"),
    ],
    21: [
        # HE: וַיָּקָם בִּלְעָם בַּבֹּקֶר וַיַּחֲבֹשׁ אֶת-אֲתֹנוֹ וַיֵּלֶךְ עִם-שָׂרֵי מוֹאָב
        # JA: פקאם באלג'דאה. ואסרג אתאנה. ומצ'א מע רויסא מואב
        # EN: And he rose in the morning, and saddled his she-donkey, and went with the officers of Moab.
        ("וַיָּקָם בִּלְעָם", "פקאם", "And he rose"),
        ("בַּבֹּקֶר", "באלג'דאה", "in the morning,"),
        ("וַיַּחֲבֹשׁ", "ואסרג", "and saddled"),
        ("אֶת-אֲתֹנוֹ", "אתאנה", "his she-donkey,"),
        ("וַיֵּלֶךְ", "ומצ'א", "and went"),
        ("עִם-שָׂרֵי", "מע רויסא", "with the officers of"),
        ("מוֹאָב", "מואב", "Moab."),
    ],
    22: [
        # HE: וַיִּחַר-אַף אֱלֹהִים כִּי-הוֹלֵךְ הוּא וַיִּתְיַצֵּב מַלְאַךְ יְהוָה בַּדֶּרֶךְ לְשָׂטָן לוֹ וְהוּא רֹכֵב עַל-אֲתֹנוֹ וּשְׁנֵי נְעָרָיו עִמּוֹ
        # JA: ת'ם אשתד ג'צ'ב אללה למצ'יה טאמעא. פוקף מלך אללה פי אלטריק ליחידה ען ד'אלך. והו ראכב עלי' אתאנה. ומעה ג'לאמיה
        # EN: Then God's anger intensified at his going in greed; and the angel of God stood in the road to turn him away from that — while he was riding on his she-donkey and his two youths were with him.
        (None, "ת'ם", "Then"),
        ("וַיִּחַר-אַף", "אשתד ג'צ'ב", "God's anger intensified"),
        ("אֱלֹהִים", "אללה", "at his going"),
        ("כִּי-הוֹלֵךְ הוּא", "למצ'יה טאמעא", "in greed;"),
        ("וַיִּתְיַצֵּב", "פוקף", "and the angel of God stood"),
        ("מַלְאַךְ יְהוָה", "מלך אללה", "in the road"),
        ("בַּדֶּרֶךְ", "פי אלטריק", "to turn him away"),
        ("לְשָׂטָן לוֹ", "ליחידה ען ד'אלך", "from that —"),
        ("וְהוּא רֹכֵב", "והו ראכב", "while he was riding"),
        ("עַל-אֲתֹנוֹ", "עלי' אתאנה", "on his she-donkey"),
        ("וּשְׁנֵי נְעָרָיו עִמּוֹ", "ומעה ג'לאמיה", "and his two youths were with him."),
    ],
    23: [
        # HE: וַתֵּרֶא הָאָתוֹן אֶת-מַלְאַךְ יְהוָה נִצָּב בַּדֶּרֶךְ וְחַרְבּוֹ שְׁלוּפָה בְּיָדוֹ וַתֵּט הָאָתוֹן מִן-הַדֶּרֶךְ וַתֵּלֶךְ בַּשָּׂדֶה וַיַּךְ בִּלְעָם אֶת-הָאָתוֹן לְהַטֹּתָהּ הַדָּרֶךְ
        # JA: פלמא ראת אלאתאן מלך אללה קאימא פי אלטריק. וסיפה מצלת פי ידה. מאלת ען אלטריק. וסארת פי אלצ'יאע. פצ'רבהא בלעם. לירדהא אלי' אלטריק
        # EN: And when the she-donkey saw the angel of God standing in the road, with his sword drawn in his hand, she turned aside from the road and went through the fields; so Balaam struck her, to turn her back to the road.
        ("וַתֵּרֶא", "פלמא ראת", "And when"),
        ("הָאָתוֹן", "אלאתאן", "the she-donkey saw"),
        ("אֶת-מַלְאַךְ יְהוָה", "מלך אללה", "the angel of God"),
        ("נִצָּב בַּדֶּרֶךְ", "קאימא פי אלטריק", "standing in the road,"),
        ("וְחַרְבּוֹ שְׁלוּפָה", "וסיפה מצלת", "with his sword drawn"),
        ("בְּיָדוֹ", "פי ידה", "in his hand,"),
        ("וַתֵּט הָאָתוֹן", "מאלת", "she turned aside"),
        ("מִן-הַדֶּרֶךְ", "ען אלטריק", "from the road"),
        ("וַתֵּלֶךְ בַּשָּׂדֶה", "וסארת פי אלצ'יאע", "and went through the fields;"),
        ("וַיַּךְ בִּלְעָם", "פצ'רבהא בלעם", "so Balaam struck her,"),
        ("לְהַטֹּתָהּ הַדָּרֶךְ", "לירדהא אלי' אלטריק", "to turn her back to the road."),
    ],
    24: [
        # HE: וַיַּעֲמֹד מַלְאַךְ יְהוָה בְּמִשְׁעוֹל הַכְּרָמִים--גָּדֵר מִזֶּה וְגָדֵר מִזֶּה
        # JA: ת'ם וקף מלך אללה. פי זקאק אלכרום. והנאך גדאר ימנה ויסרה
        # EN: Then the angel of God stood in the narrow lane of the vineyards, with a wall on the right and on the left.
        (None, "ת'ם", "Then"),
        ("וַיַּעֲמֹד", "וקף", "stood"),
        ("מַלְאַךְ יְהוָה", "מלך אללה", "the angel of God"),
        ("בְּמִשְׁעוֹל", "פי זקאק", "in the narrow lane of"),
        ("הַכְּרָמִים", "אלכרום", "the vineyards,"),
        ("גָּדֵר", "והנאך גדאר", "with a wall"),
        ("מִזֶּה", "ימנה", "on the right"),
        ("וְגָדֵר מִזֶּה", "ויסרה", "and on the left."),
    ],
    25: [
        # HE: וַתֵּרֶא הָאָתוֹן אֶת-מַלְאַךְ יְהוָה וַתִּלָּחֵץ אֶל-הַקִּיר וַתִּלְחַץ אֶת-רֶגֶל בִּלְעָם אֶל-הַקִּיר וַיֹּסֶף לְהַכֹּתָהּ
        # JA: פלמא ראתה אזדחמת מע אלחאיט. פצ'ג'טת רגל בלעם אלי' אלחאיט. פזאד פי צ'רבהא
        # EN: And when she saw him, she pressed herself against the wall and crushed Balaam's foot against the wall; so he added to his striking of her.
        ("וַתֵּרֶא הָאָתוֹן", "פלמא ראתה", "And when she saw him,"),
        ("וַתִּלָּחֵץ אֶל-הַקִּיר", "אזדחמת מע אלחאיט", "she pressed herself against the wall"),
        ("וַתִּלְחַץ אֶת-רֶגֶל בִּלְעָם", "פצ'ג'טת רגל בלעם", "and crushed Balaam's foot"),
        ("אֶל-הַקִּיר", "אלי' אלחאיט", "against the wall;"),
        ("וַיֹּסֶף", "פזאד", "so he added"),
        ("לְהַכֹּתָהּ", "פי צ'רבהא", "to his striking of her."),
    ],
    26: [
        # HE: וַיּוֹסֶף מַלְאַךְ-יְהוָה עֲבוֹר וַיַּעֲמֹד בְּמָקוֹם צָר אֲשֶׁר אֵין-דֶּרֶךְ לִנְטוֹת יָמִין וּשְׂמֹאול
        # JA: ת'ם עאוד מלך אללה פגאז. ווקף פי מוצ'ע מצ'יק. מא ליס טריק אן ימיל ענה ימנה ולא יסרה
        # EN: And the angel of God passed on again, and stood in a narrow place where there was no way to turn aside from it right or left.
        (None, "ת'ם", "And"),
        ("וַיּוֹסֶף", "עאוד", "again"),
        ("מַלְאַךְ-יְהוָה", "מלך אללה", "the angel of God"),
        ("עֲבוֹר", "פגאז", "passed on"),
        ("וַיַּעֲמֹד", "ווקף", "and stood"),
        ("בְּמָקוֹם צָר", "פי מוצ'ע מצ'יק", "in a narrow place"),
        ("אֲשֶׁר אֵין-דֶּרֶךְ", "מא ליס טריק", "where there was no way"),
        ("לִנְטוֹת", "אן ימיל ענה", "to turn aside from it"),
        ("יָמִין", "ימנה", "right"),
        ("וּשְׂמֹאול", "ולא יסרה", "or left."),
    ],
    27: [
        # HE: וַתֵּרֶא הָאָתוֹן אֶת-מַלְאַךְ יְהוָה וַתִּרְבַּץ תַּחַת בִּלְעָם וַיִּחַר-אַף בִּלְעָם וַיַּךְ אֶת-הָאָתוֹן בַּמַּקֵּל
        # JA: ולמא ראתה. רבצת תחת בלעם. פאשתד ג'צ'ב בלעם. פצ'רבהא באלעצא
        # EN: And when she saw him, she lay down beneath Balaam; and Balaam's anger intensified, and he struck her with the staff.
        ("וַתֵּרֶא הָאָתוֹן", "ולמא ראתה", "And when she saw him,"),
        ("וַתִּרְבַּץ", "רבצת", "she lay down"),
        ("תַּחַת בִּלְעָם", "תחת בלעם", "beneath Balaam;"),
        ("וַיִּחַר-אַף", "פאשתד ג'צ'ב", "and Balaam's anger intensified,"),
        ("בִּלְעָם", "בלעם", "and he struck her"),
        ("וַיַּךְ אֶת-הָאָתוֹן", "פצ'רבהא", "with"),
        ("בַּמַּקֵּל", "באלעצא", "the staff."),
    ],
    28: [
        # HE: וַיִּפְתַּח יְהוָה אֶת-פִּי הָאָתוֹן וַתֹּאמֶר לְבִלְעָם מֶה-עָשִׂיתִי לְךָ כִּי הִכִּיתַנִי זֶה שָׁלֹשׁ רְגָלִים
        # JA: פפתח אללה פאהא. פקאלת לבלעם מא ד'א צנעת בך. אד' צ'רבתני. הד'ה אלמרה אלת'אלת'ה
        # EN: And God opened her mouth, and she said to Balaam: 'What have I done to you, that you have struck me — this third time?'
        ("וַיִּפְתַּח יְהוָה", "פפתח אללה", "And God opened"),
        ("אֶת-פִּי הָאָתוֹן", "פאהא", "her mouth,"),
        ("וַתֹּאמֶר", "פקאלת", "and she said"),
        ("לְבִלְעָם", "לבלעם", "to Balaam:"),
        ("מֶה-עָשִׂיתִי לְךָ", "מא ד'א צנעת בך", "'What have I done to you,"),
        ("כִּי הִכִּיתַנִי", "אד' צ'רבתני", "that you have struck me —"),
        ("זֶה שָׁלֹשׁ רְגָלִים", "הד'ה אלמרה אלת'אלת'ה", "this third time?'"),
    ],
    29: [
        # HE: וַיֹּאמֶר בִּלְעָם לָאָתוֹן כִּי הִתְעַלַּלְתְּ בִּי לוּ יֶשׁ-חֶרֶב בְּיָדִי כִּי עַתָּה הֲרַגְתִּיךְ
        # JA: קאל. לאנך תמרדת בי. ולו אן פי ידי סיף לקתלתך
        # EN: He said: 'Because you have defied me — had I a sword in my hand, I would kill you now.'
        ("וַיֹּאמֶר בִּלְעָם לָאָתוֹן", "קאל", "He said:"),
        ("כִּי הִתְעַלַּלְתְּ בִּי", "לאנך תמרדת בי", "'Because you have defied me —"),
        ("לוּ יֶשׁ-חֶרֶב", "ולו אן פי ידי סיף", "had I a sword in my hand,"),
        ("כִּי עַתָּה הֲרַגְתִּיךְ", "לקתלתך", "I would kill you now.'"),
    ],
    30: [
        # HE: וַתֹּאמֶר הָאָתוֹן אֶל-בִּלְעָם הֲלוֹא אָנֹכִי אֲתֹנְךָ אֲשֶׁר-רָכַבְתָּ עָלַי מֵעוֹדְךָ עַד-הַיּוֹם הַזֶּה--הַהַסְכֵּן הִסְכַּנְתִּי לַעֲשׂוֹת לְךָ כֹּה וַיֹּאמֶר לֹא
        # JA: קאלת. אלי'ס אנא אתאנך אלד'י רכבתני. מנד' כנת אלי' הד'א אליום. הל עוודתך אן אצנע בך כד'א. קאל לא
        # EN: She said: 'Am I not your she-donkey on which you have ridden since I came to be until this day? Have I been accustomed to doing such a thing to you?' He said: 'No.'
        ("וַתֹּאמֶר הָאָתוֹן", "קאלת", "She said:"),
        ("הֲלוֹא אָנֹכִי", "אלי'ס אנא", "'Am I not"),
        ("אֲתֹנְךָ", "אתאנך", "your she-donkey"),
        ("אֲשֶׁר-רָכַבְתָּ עָלַי", "אלד'י רכבתני", "on which you have ridden"),
        ("מֵעוֹדְךָ", "מנד' כנת", "since I came to be"),
        ("עַד-הַיּוֹם הַזֶּה", "אלי' הד'א אליום", "until this day?"),
        ("הַהַסְכֵּן הִסְכַּנְתִּי", "הל עוודתך", "Have I been accustomed"),
        ("לַעֲשׂוֹת לְךָ כֹּה", "אן אצנע בך כד'א", "to doing such a thing to you?'"),
        ("וַיֹּאמֶר לֹא", "קאל לא", "He said: 'No.'"),
    ],
    31: [
        # HE: וַיְגַל יְהוָה אֶת-עֵינֵי בִלְעָם וַיַּרְא אֶת-מַלְאַךְ יְהוָה נִצָּב בַּדֶּרֶךְ וְחַרְבּוֹ שְׁלֻפָה בְּיָדוֹ וַיִּקֹּד וַיִּשְׁתַּחוּ לְאַפָּיו
        # JA: ת'ם כשף אללה ען בצר בלעם. פראא מלך אללה ואקפא פי אלטריק. וסיפה מצלת פי ידה. פכ'ר בין ידיה סאגדא
        # EN: Then God uncovered Balaam's sight, and he saw the angel of God standing in the road, with his sword drawn in his hand; and he fell down before him prostrating.
        (None, "ת'ם", "Then"),
        ("וַיְגַל יְהוָה", "כשף אללה", "God uncovered"),
        ("אֶת-עֵינֵי בִלְעָם", "ען בצר בלעם", "Balaam's sight,"),
        ("וַיַּרְא", "פראא", "and he saw"),
        ("אֶת-מַלְאַךְ יְהוָה", "מלך אללה", "the angel of God"),
        ("נִצָּב בַּדֶּרֶךְ", "ואקפא פי אלטריק", "standing in the road,"),
        ("וְחַרְבּוֹ שְׁלֻפָה", "וסיפה מצלת", "with his sword drawn"),
        ("בְּיָדוֹ", "פי ידה", "in his hand;"),
        ("וַיִּקֹּד וַיִּשְׁתַּחוּ", "פכ'ר בין ידיה", "and he fell down before him"),
        ("לְאַפָּיו", "סאגדא", "prostrating."),
    ],
    32: [
        # HE: וַיֹּאמֶר אֵלָיו מַלְאַךְ יְהוָה עַל-מָה הִכִּיתָ אֶת-אֲתֹנְךָ זֶה שָׁלוֹשׁ רְגָלִים הִנֵּה אָנֹכִי יָצָאתִי לְשָׂטָן כִּי-יָרַט הַדֶּרֶךְ לְנֶגְדִּי
        # JA: פקאל לה מלך אללה. לם צ'רבת אתאנך. הד'ה אלמרה אלת'אלת'ה. ואנא כ'רגת אן אחידך. אד' תורטת אלטריק חד'אי
        # EN: And the angel of God said to him: 'Why have you struck your she-donkey this third time? I have come out to turn you aside — for the road before me has become an entanglement.'
        ("וַיֹּאמֶר אֵלָיו", "פקאל לה", "And"),
        ("מַלְאַךְ יְהוָה", "מלך אללה", "the angel of God said to him:"),
        ("עַל-מָה הִכִּיתָ", "לם צ'רבת", "'Why have you struck"),
        ("אֶת-אֲתֹנְךָ", "אתאנך", "your she-donkey"),
        ("זֶה שָׁלוֹשׁ רְגָלִים", "הד'ה אלמרה אלת'אלת'ה", "this third time?"),
        ("הִנֵּה אָנֹכִי יָצָאתִי", "ואנא כ'רגת", "I have come out"),
        ("לְשָׂטָן", "אן אחידך", "to turn you aside —"),
        ("כִּי-יָרַט הַדֶּרֶךְ", "אד' תורטת אלטריק", "for the road"),
        ("לְנֶגְדִּי", "חד'אי", "before me has become an entanglement.'"),
    ],
    33: [
        # HE: וַתִּרְאַנִי הָאָתוֹן וַתֵּט לְפָנַי זֶה שָׁלֹשׁ רְגָלִים אוּלַי נָטְתָה מִפָּנַי כִּי עַתָּה גַּם-אֹתְכָה הָרַגְתִּי וְאוֹתָהּ הֶחֱיֵיתִי
        # JA: חתי' ראתני פמאלת עני. הד'ה אלמרה אלת'אלת'ה. פלו לם תמיל עני. לקתלתך אלאן ובקיתהא
        # EN: Until she saw me and turned aside from me — this third time. Had she not turned aside from me, I would have killed you now and let her live.'
        ("וַתִּרְאַנִי הָאָתוֹן", "חתי' ראתני", "Until she saw me"),
        ("וַתֵּט לְפָנַי", "פמאלת עני", "and turned aside from me —"),
        ("זֶה שָׁלֹשׁ רְגָלִים", "הד'ה אלמרה אלת'אלת'ה", "this third time."),
        ("אוּלַי נָטְתָה מִפָּנַי", "פלו לם תמיל עני", "Had she not turned aside from me,"),
        ("כִּי עַתָּה גַּם-אֹתְכָה הָרַגְתִּי", "לקתלתך אלאן", "I would have killed you now"),
        ("וְאוֹתָהּ הֶחֱיֵיתִי", "ובקיתהא", "and let her live.'"),
    ],
    34: [
        # HE: וַיֹּאמֶר בִּלְעָם אֶל-מַלְאַךְ יְהוָה חָטָאתִי--כִּי לֹא יָדַעְתִּי כִּי אַתָּה נִצָּב לִקְרָאתִי בַּדָּרֶךְ וְעַתָּה אִם-רַע בְּעֵינֶיךָ אָשׁוּבָה לִּי
        # JA: קאל לה קד אכ'טית. אד' לם אעלם. אנך ואקף תלקאי פי אלטריק ואלאן פאן סאך מצ'יי רגעת
        # EN: He said to him: 'I have erred, for I did not know that you were standing to meet me in the road. And now, if my going is displeasing to you, I shall turn back.'
        ("וַיֹּאמֶר בִּלְעָם", "קאל לה", "He said to him:"),
        ("חָטָאתִי", "קד אכ'טית", "'I have erred,"),
        ("כִּי לֹא יָדַעְתִּי", "אד' לם אעלם", "for I did not know"),
        ("כִּי אַתָּה נִצָּב", "אנך ואקף", "that you were standing"),
        ("לִקְרָאתִי", "תלקאי", "to meet me"),
        ("בַּדָּרֶךְ", "פי אלטריק", "in the road."),
        ("וְעַתָּה", "ואלאן", "And now,"),
        ("אִם-רַע בְּעֵינֶיךָ", "פאן סאך", "if my going is displeasing to you,"),
        ("אָשׁוּבָה לִּי", "מצ'יי רגעת", "I shall turn back.'"),
    ],
    35: [
        # HE: וַיֹּאמֶר מַלְאַךְ יְהוָה אֶל-בִּלְעָם לֵךְ עִם-הָאֲנָשִׁים וְאֶפֶס אֶת-הַדָּבָר אֲשֶׁר-אֲדַבֵּר אֵלֶיךָ אֹתוֹ תְדַבֵּר וַיֵּלֶךְ בִּלְעָם עִם-שָׂרֵי בָלָק
        # JA: קאל לה. אמץ' מע אלקום. ועדא אלקול. אלד'י אקולה לך קולה פקט. פמצ'א מעהם
        # EN: He said to him: 'Go with the people — but only the word that I shall tell you, speak that alone.' And he went with them.
        ("וַיֹּאמֶר מַלְאַךְ יְהוָה", "קאל לה", "He said to him:"),
        ("לֵךְ", "אמץ'", "'Go"),
        ("עִם-הָאֲנָשִׁים", "מע אלקום", "with the people —"),
        ("וְאֶפֶס", "ועדא", "but only"),
        ("אֶת-הַדָּבָר", "אלקול", "the word"),
        ("אֲשֶׁר-אֲדַבֵּר אֵלֶיךָ", "אלד'י אקולה לך", "that I shall tell you,"),
        ("אֹתוֹ תְדַבֵּר", "קולה פקט", "speak that alone.'"),
        ("וַיֵּלֶךְ בִּלְעָם", "פמצ'א", "And he went"),
        ("עִם-שָׂרֵי בָלָק", "מעהם", "with them."),
    ],
    36: [
        # HE: וַיִּשְׁמַע בָּלָק כִּי בָא בִלְעָם וַיֵּצֵא לִקְרָאתוֹ אֶל-עִיר מוֹאָב אֲשֶׁר עַל-גְּבוּל אַרְנֹן אֲשֶׁר בִּקְצֵה הַגְּבוּל
        # JA: פלמא סמע בלק במגי בלעם. כ'רג תלקאה אלי' קריה' מואב. אלד'י עלי' תכ'ם ארנון. אלד'י פי טרפה
        # EN: And when Balak heard of the coming of Balaam, he went out to meet him at the town of Moab, which is on the border of the Arnon, which is at its edge.
        ("וַיִּשְׁמַע בָּלָק", "פלמא סמע בלק", "And when Balak heard"),
        ("כִּי בָא בִלְעָם", "במגי בלעם", "of the coming of Balaam,"),
        ("וַיֵּצֵא", "כ'רג", "he went out"),
        ("לִקְרָאתוֹ", "תלקאה", "to meet him"),
        ("אֶל-עִיר מוֹאָב", "אלי' קריה' מואב", "at the town of Moab,"),
        ("אֲשֶׁר עַל-גְּבוּל", "אלד'י עלי' תכ'ם", "which is on the border of"),
        ("אַרְנֹן", "ארנון", "the Arnon,"),
        ("אֲשֶׁר בִּקְצֵה הַגְּבוּל", "אלד'י פי טרפה", "which is at its edge."),
    ],
    37: [
        # HE: וַיֹּאמֶר בָּלָק אֶל-בִּלְעָם הֲלֹא שָׁלֹחַ שָׁלַחְתִּי אֵלֶיךָ לִקְרֹא-לָךְ--לָמָּה לֹא-הָלַכְתָּ אֵלָי הַאֻמְנָם לֹא אוּכַל כַּבְּדֶךָ
        # JA: קאל בלק לבלעם. אלי'ס ארסלת אלי'ך מרה קבל הד'ה לאדעוך. לם לם תצאל אליי. אתרא. ליס אקדר אן אכרמך
        # EN: Balak said to Balaam: 'Did I not send to you once before this to invite you? Why did you not come to me? Do you suppose I am unable to honor you?'
        ("וַיֹּאמֶר בָּלָק", "קאל בלק", "Balak said"),
        ("אֶל-בִּלְעָם", "לבלעם", "to Balaam:"),
        ("הֲלֹא שָׁלֹחַ שָׁלַחְתִּי אֵלֶיךָ", "אלי'ס ארסלת אלי'ך", "'Did I not send to you"),
        ("לִקְרֹא-לָךְ", "מרה קבל הד'ה לאדעוך", "once before this to invite you?"),
        ("לָמָּה לֹא-הָלַכְתָּ אֵלָי", "לם לם תצאל אליי", "Why did you not come to me?"),
        ("הַאֻמְנָם", "אתרא", "Do you suppose"),
        ("לֹא אוּכַל כַּבְּדֶךָ", "ליס אקדר אן אכרמך", "I am unable to honor you?'"),
    ],
    38: [
        # HE: וַיֹּאמֶר בִּלְעָם אֶל-בָּלָק הִנֵּה-בָאתִי אֵלֶיךָ--עַתָּה הֲיָכֹל אוּכַל דַּבֵּר מְאוּמָה הַדָּבָר אֲשֶׁר יָשִׂים אֱלֹהִים בְּפִי--אֹתוֹ אֲדַבֵּר
        # JA: קאל. ואלאן קד צרת אלי'ך אתראני אסתטיע אן אקול שייא. אלא מא ילקנניה אללה פקט
        # EN: He said: 'And now I have indeed come to you — but do you suppose I am able to say anything, except only what God will prompt me with?'
        ("וַיֹּאמֶר בִּלְעָם", "קאל", "He said:"),
        ("הִנֵּה-בָאתִי", "ואלאן קד צרת", "'And now I have indeed come"),
        ("אֵלֶיךָ", "אלי'ך", "to you —"),
        ("עַתָּה הֲיָכֹל אוּכַל", "אתראני אסתטיע", "but do you suppose I am able"),
        ("דַּבֵּר מְאוּמָה", "אן אקול שייא", "to say anything,"),
        ("הַדָּבָר אֲשֶׁר יָשִׂים", "אלא מא ילקנניה", "except only what"),
        ("אֱלֹהִים", "אללה", "God"),
        ("בְּפִי--אֹתוֹ אֲדַבֵּר", "פקט", "will prompt me with?'"),
    ],
    39: [
        # HE: וַיֵּלֶךְ בִּלְעָם עִם-בָּלָק וַיָּבֹאוּ קִרְיַת חֻצוֹת
        # JA: ומצ'יא גמיעא. אלי' אן גאא אלי' קריה' חוצות
        # EN: And the two of them went together, until they came to the town of Hutzoth.
        ("וַיֵּלֶךְ בִּלְעָם", "ומצ'יא", "And the two of them went"),
        ("עִם-בָּלָק", "גמיעא", "together,"),
        (None, "אלי' אן גאא", "until they came"),
        ("וַיָּבֹאוּ", "אלי'", "to"),
        ("קִרְיַת חֻצוֹת", "קריה' חוצות", "the town of Hutzoth."),
    ],
    40: [
        # HE: וַיִּזְבַּח בָּלָק בָּקָר וָצֹאן וַיְשַׁלַּח לְבִלְעָם וְלַשָּׂרִים אֲשֶׁר אִתּוֹ
        # JA: פד'בח בלק בקרא וג'נמא. ובעת' בד'אלך אלי' בלעם. ואלי' אלרויסא אלד'ין מעה
        # EN: And Balak slaughtered cattle and sheep, and sent of that to Balaam and to the officers who were with him.
        ("וַיִּזְבַּח", "פד'בח", "And Balak slaughtered"),
        ("בָּלָק", "בלק", "cattle"),
        ("בָּקָר", "בקרא", "and sheep,"),
        ("וָצֹאן", "וג'נמא", "and sent"),
        ("וַיְשַׁלַּח", "ובעת'", "of that"),
        (None, "בד'אלך", "to Balaam"),
        ("לְבִלְעָם", "אלי' בלעם", "and to the officers"),
        ("וְלַשָּׂרִים", "ואלי' אלרויסא", "who were"),
        ("אֲשֶׁר אִתּוֹ", "אלד'ין מעה", "with him."),
    ],
    41: [
        # HE: וַיְהִי בַבֹּקֶר--וַיִּקַּח בָּלָק אֶת-בִּלְעָם וַיַּעֲלֵהוּ בָּמוֹת בָּעַל וַיַּרְא מִשָּׁם קְצֵה הָעָם
        # JA: פלמא כאן באלג'דאה. אכ'ד בלק בלעם. פאצעדה אלי' בעץ' ביאע מעבודה. פנצ'ר מן ת'ם בעץ' אלקום
        # EN: And it was in the morning: Balak took Balaam and brought him up to some of the high-places of his deity, and from there he saw a portion of the people.
        ("וַיְהִי בַבֹּקֶר", "פלמא כאן באלג'דאה", "And it was in the morning:"),
        ("וַיִּקַּח בָּלָק", "אכ'ד בלק", "Balak took"),
        ("אֶת-בִּלְעָם", "בלעם", "Balaam"),
        ("וַיַּעֲלֵהוּ", "פאצעדה", "and brought him up"),
        ("בָּמוֹת בָּעַל", "אלי' בעץ' ביאע מעבודה", "to some of the high-places of his deity,"),
        ("וַיַּרְא", "פנצ'ר", "and from there he saw"),
        ("מִשָּׁם", "מן ת'ם", "a portion of"),
        ("קְצֵה הָעָם", "בעץ' אלקום", "the people."),
    ],
}

"""Hand-authored alignment triples for Devarim chapter 33.

Word-level: each JA (Saadia) word is its own group, mapped to the Hebrew word
it renders and its English counterpart. The runtime resolver matches each side
independently (lib/alignment.ts), so words link correctly even across word-order
crossings. Words Saadia adds with no Hebrew source (glosses, expansions) carry
he=None and link JA↔English only.

Chapter 33 is "V'zot HaBerakhah" — Moses' tribal blessings: Reuben, Judah,
Levi, Benjamin, Joseph, Zebulun/Issachar, Gad (v.20-21), Dan, Naphtali, Asher.
Verse 20 is absent from the source data (gap in the dataset).

Alignment notes:
- v2: long poetic verse; Saadia's JA is a prayer-form reworking with expansions;
  period separates two clause-groups.
- v4: Saadia opens with "אללהם" (O God!) — a devotional gloss with no HE
  equivalent; similarly in vv.8, 11, 13.
- v5: "אלמוצוף" (the described one) = Saadia's gloss for Jeshurun.
- v16: JA has a period after "אלסנא" — split triple at that boundary.
- v17: "ושרחהא" (and the explanation thereof) is Saadia's editorial gloss.
- v21: verse 20 is absent from the dataset; v21 follows v19 in the source.
- v28: "נצ'יר מא קאל להם יעקוב אביהם" is a Saadia explanatory gloss
  (in fulfilment of what Jacob told them) with no single HE word.
"""

ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {
    1: [
        ("וְזֹאת", "והד'א", "And these are"),
        ("הַבְּרָכָה", "אלברכאת", "the blessings"),
        ("אֲשֶׁר בֵּרַךְ", "אלד'י בארך בהא", "with which"),
        ("מֹשֶׁה", "מוסי'", "Moses"),
        ("אִישׁ הָאֱלֹהִים", "רסול אללה", "the messenger of God"),
        ("אֶת-בְּנֵי יִשְׂרָאֵל", "בני אסראיל", "blessed the sons of Israel"),
        ("לִפְנֵי מוֹתוֹ", "קבל מותה", "before his death"),
    ],
    2: [
        ("וַיֹּאמַר", "וקאל", "And he said"),
        (None, "אללהם", "O God"),
        ("יְהוָה", "אלד'י תגלא לנא", "who revealed Himself to us"),
        ("מִסִּינַי", "מן טור סיני", "from Mount Sinai"),
        ("וְזָרַח", "ואשרק בנורה", "and shone with His light"),
        ("מִשֵּׂעִיר", "מן גבל שעיר", "from Mount Seir"),
        ("הוֹפִיעַ", "ולווח בה", "and flashed with it"),
        ("מֵהַר פָּארָן", "מן גבל פארן", "from Mount Paran"),
        ("וְאָתָה", "ואתא", "and came"),
        ("מֵרִבְבֹת קֹדֶשׁ", "רבואת אלקדס", "to the myriads of the holy ones"),
        ("אֵשׁ דָּת", "בשריעה' נור", "with His laws, a light"),
        ("מִימִינוֹ", "מן ימינה", "from His right hand"),
        (None, "להם", "for them"),
    ],
    3: [
        ("אַף חֹבֵב", "ואחתבא", "And He also cherished"),
        ("עַמִּים", "שעבא", "a people for Himself"),
        ("כָּל-קְדֹשָׁיו", "פגמיע כ'ואצהם", "so all their choicest ones"),
        ("בְּיָדֶךָ", "פי טאעתך", "are in obedience to You"),
        ("וְהֵם תֻּכּוּ", "והם יקפון", "and they follow"),
        ("לְרַגְלֶךָ", "את'ארך", "in Your footsteps"),
        ("יִשָּׂא מִדַּבְּרֹתֶיךָ", "ויתנאקלון כלמאתך", "and pass on Your words one to another"),
    ],
    4: [
        (None, "אללהם", "O God"),
        ("תּוֹרָה צִוָּה-לָנוּ", "אלד'י אמר לנא מוסי' באלתורייה", "who commanded us through Moses with the Torah"),
        ("מוֹרָשָׁה", "פגעלהא וראת'ה", "and made it an inheritance"),
        ("קְהִלַּת יַעֲקֹב", "לגוקה' יעקוב", "for the congregation of Jacob"),
    ],
    5: [
        ("וַיְהִי", "וכאן", "And there was"),
        ("מֶלֶךְ", "מלכא", "a king"),
        ("בִישֻׁרוּן", "פי אלמוצוף", "among the described one"),
        ("בְּהִתְאַסֵּף", "חין תגתמע אליה", "would gather to him"),
        ("רָאשֵׁי עָם", "רויסאה", "his chiefs"),
        ("יַחַד שִׁבְטֵי יִשְׂרָאֵל", "וסאיר אסבאטה", "and the rest of his tribes"),
    ],
    6: [
        (None, "אסאלך", "I ask of You"),
        ("יְחִי רְאוּבֵן", "אן יחיא אל ראובן", "that the clan of Reuben live"),
        ("וְאַל-יָמֹת", "ולא ימות", "and not die"),
        ("וִיהִי מְתָיו מִסְפָּר", "ולא יציר רהטה ד'ו אחצא", "and not become a group too few to count"),
    ],
    7: [
        ("וְזֹאת לִיהוּדָה", "והד'ה מא קאל ליהודה", "And this is what he said for Judah"),
        (None, "אללהם", "O God"),
        ("שְׁמַע", "אסמע", "hear"),
        ("יְהוָה", "צות יהודה", "the voice of Judah"),
        ("קוֹל יְהוּדָה", "ורדה", "and return him"),
        ("וְאֶל-עַמּוֹ תְּבִיאֶנּוּ", "אלי' קומה מן ג'זוה", "to his people from his campaign"),
        ("יָדָיו רָב לוֹ", "ואגעל ידאה מנתצפתאן לה", "and make his two hands prevailing for him"),
        ("וְעֵזֶר מִצָּרָיו תִּהְיֶה", "וכן לה עונא עלי' אעדאיה", "and be for him a helper against his enemies"),
    ],
    8: [
        ("וּלְלֵוִי אָמַר", "וקאל ללוי", "And he said for Levi"),
        (None, "אללהם", "O God"),
        ("תֻּמֶּיךָ וְאוּרֶיךָ", "אלד'י אנחלת צאחאיך ואנוארך", "who granted Your Thummim and Your Urim"),
        ("לְאִישׁ חֲסִידֶךָ", "לרגל אלד'י הו בארך", "to a man who is Your devoted one"),
        ("אֲשֶׁר נִסִּיתוֹ בְּמַסָּה", "וקד אמתחנתה פי ד'את אלמחנה", "and You tested him at the very trial"),
        ("תְּרִיבֵהוּ עַל-מֵי מְרִיבָה", "ואכ'תצמתה פי מת'ל מא אלכ'צומה", "and contended with him at the water of contention"),
    ],
    9: [
        ("הָאֹמֵר לְאָבִיו", "פוגדתאה אלקאיל ען אביה", "And You found him to be one who says of his father"),
        ("וּלְאִמּוֹ", "ואמה", "and his mother"),
        ("לֹא רְאִיתִיו", "כאנה לם יראהם", "as though he had not seen them"),
        ("וְאֶת-אֶחָיו לֹא הִכִּיר", "ולם ית'בת אכ'ותה", "and did not acknowledge his brothers"),
        ("וְאֶת-בָּנָו לֹא יָדָע", "ולם יעתרף בבניה", "and did not recognize his sons"),
        ("כִּי שָׁמְרוּ אִמְרָתֶךָ", "ממא חרסו מקאלתך", "because they guarded Your word"),
        ("וּבְרִיתְךָ יִנְצֹרוּ", "והם יחפצו עהדך", "and they keep Your covenant"),
    ],
    10: [
        ("יוֹרוּ מִשְׁפָּטֶיךָ לְיַעֲקֹב", "פהם יפתון פי אחכאמך לאל יעקוב", "And so they give rulings in Your laws for Jacob"),
        ("וְתוֹרָתְךָ לְיִשְׂרָאֵל", "ושראיעך לאל אסראיל", "and Your statutes for Israel"),
        ("יָשִׂימוּ קְטוֹרָה בְּאַפֶּךָ", "ויציירון אלבכור בין ידיך", "they set the incense before You"),
        ("וְכָלִיל עַל-מִזְבְּחֶךָ", "ואלכמאל עלי' מד'בחך", "and the whole-offering upon Your altar"),
    ],
    11: [
        (None, "אללהם", "O God"),
        ("בָּרֵךְ יְהוָה חֵילוֹ", "פבארך פי גנדה", "so bless his host"),
        ("וּפֹעַל יָדָיו תִּרְצֶה", "וארץ' מא תצנעה ידאה", "and be pleased with what his two hands do"),
        ("מְחַץ מָתְנַיִם קָמָיו", "ואוהן אחקא מקאומיה", "and weaken the loins of those who oppose him"),
        ("וּמְשַׂנְאָיו מִן-יְקוּמוּן", "ושאנייה מן אן יקאומונה", "and hate him, so that they cannot stand against him"),
    ],
    12: [
        ("לְבִנְיָמִן אָמַר", "וקאל לבנימין", "And he said for Benjamin"),
        ("יְדִיד יְהוָה", "אד' הו ודיד אללה", "Since he is the beloved of God"),
        ("יִשְׁכֹּן לָבֶטַח", "סיסכן ואת'קא בה", "he shall dwell in confidence in Him"),
        ("חֹפֵף עָלָיו כָּל-הַיּוֹם", "והו יטוף בה טול אלזמאן", "and He shall compass him all the length of time"),
        ("וּבֵין כְּתֵפָיו שָׁכֵן", "ובין צ'הראניה יסכן", "and between His heights He shall dwell"),
    ],
    13: [
        ("וּלְיוֹסֵף אָמַר", "וקאל ליוסף", "And he said for Joseph"),
        (None, "אללהם", "O God"),
        ("מְבֹרֶכֶת יְהוָה אַרְצוֹ", "פבארך פי בלדה", "so bless his land"),
        ("מִמֶּגֶד שָׁמַיִם מִטָּל", "מן מלאד' סמאואך וטלהא", "with the delights of Your heavens and their dew"),
        ("וּמִתְּהוֹם רֹבֶצֶת תָּחַת", "ומן אלג'מר אלג'איצ'ה אלספלא", "and with the deep waters crouching beneath"),
    ],
    14: [
        ("וּמִמֶּגֶד תְּבוּאֹת שָׁמֶשׁ", "ומן מלאד' אלג'לאת אלשמסייה", "And with the delights of the produce of the sun"),
        ("וּמִמֶּגֶד גֶּרֶשׁ יְרָחִים", "ומלאד' אלחבוב אלקמרייה", "and the delights of the grain of the moon"),
    ],
    15: [
        ("וּמֵרֹאשׁ הַרְרֵי-קֶדֶם", "ומן אצול אלגבאל אלאוולייה", "And with the ancient roots of the mountains"),
        ("וּמִמֶּגֶד גִּבְעוֹת עוֹלָם", "ומן פרוע אליפאע אלדהרייה", "and the perennial branches of the heights"),
    ],
    16: [
        ("וּמִמֶּגֶד אֶרֶץ וּמְלֹאָהּ", "ומן נעמה אלארץ' באסרהא", "And with the bounty of the earth in full"),
        ("וּרְצוֹן שֹׁכְנִי סְנֶה", "ורצ'א סאכן אלסנא", "and the favor of the One who dwells in the thornbush"),
        ("תָּבוֹאתָה לְרֹאשׁ יוֹסֵף", "יחל גמיע ד'אלך בראס יוסף", "may all this come upon the head of Joseph"),
        ("וּלְקָדְקֹד נְזִיר אֶחָיו", "והאמה' נאסך אכ'ותה", "and upon the crown of the one set apart from his brothers"),
    ],
    17: [
        ("בְּכוֹר שׁוֹרוֹ הָדָר לוֹ", "וליכון אלבהא לאלמ'מת'ל בבכר ת'ורה", "And let the glory belong to the one likened to the firstborn of his ox"),
        ("וְקַרְנֵי רְאֵם קַרְנָיו", "פתציר קרונה כקרון אלכרכדאן", "and his horns shall be as the horns of the wild ox"),
        ("בָּהֶם עַמִּים יְנַגַּח", "חתי' ינטח בהא אלאמם", "so that with them he shall gore the nations"),
        ("יַחְדָּו אַפְסֵי-אָרֶץ", "אלי' אקטאר אלארץ'", "to the ends of the earth"),
        (None, "ושרחהא", "and the explanation thereof is"),
        ("וְהֵם רִבְבוֹת אֶפְרַיִם", "אנהא רבואת אפרים", "that they are the myriads of Ephraim"),
        ("וְהֵם אַלְפֵי מְנַשֶּׁה", "ואלוף מנשה", "and the thousands of Manasseh"),
    ],
    18: [
        ("וְלִזְבוּלֻן אָמַר", "וקאל לזבולון", "And he said for Zebulun"),
        ("שְׂמַח זְבוּלֻן", "אפרח יא אל זבולון", "Rejoice, O Zebulun"),
        ("בְּצֵאתֶךָ", "פי אספארך", "in your journeys"),
        ("וְיִשָּׂשכָר בְּאֹהָלֶיךָ", "ואנת יא יששכר פי מנאזלך", "and you, O Issachar, in your dwellings"),
    ],
    19: [
        ("עַמִּים הַר-יִקְרָאוּ", "פאן אלאמם אלי' גבלכמא תחצ'ר", "For the nations shall come of their own accord to your mountain"),
        ("שָׁם יִזְבְּחוּ זִבְחֵי-צֶדֶק", "ותד'בח פיה ד'באיח עאדלה", "and shall offer righteous sacrifices there"),
        ("כִּי שֶׁפַע יַמִּים יִינָקוּ", "פהם ג'דק אלבחאר ירצ'עון", "for they shall suck the abundance of the seas"),
        ("וּשְׂפֻנֵי טְמוּנֵי חוֹל", "ודפאין אלרמל יכנזוהא", "and they shall treasure the hidden things of the sand"),
    ],
    21: [
        ("וַיַּרְא רֵאשִׁית לוֹ", "ואנה ראי' פי אוול בלדה", "And he saw, in the foremost part of his land"),
        ("כִּי-שָׁם חֶלְקַת מְחֹקֵק סָפוּן", "אן גוקה' אלראסמין הנאך מכנוזה", "that the congregation of those who traced it was stored there"),
        ("וַיֵּתֵא רָאשֵׁי עָם", "פאתא רויסא אלקום", "so he came to the chiefs of the people"),
        (None, "פתלמד'הם", "and made them disciples"),
        ("צִדְקַת יְהוָה עָשָׂה", "וצנע בעדל אללה", "and he acted according to the justice of God"),
        ("וּמִשְׁפָּטָיו עִם-יִשְׂרָאֵל", "ואחכאמה מע סאיר אל אסראיל", "and His laws, together with the rest of the clan of Israel"),
    ],
    22: [
        ("וּלְדָן אָמַר", "וקאל לדן", "And he said for Dan"),
        ("דָּן גּוּר אַרְיֵה", "כון יא דן כשבל אלאסד", "Be, O Dan, like the cub of a lion"),
        ("יְזַנֵּק", "בקווה", "in strength"),
        ("מִן-הַבָּשָׁן", "אד'א יערץ' מן אלבת'נייה", "as it springs forth from the Bashan"),
    ],
    23: [
        ("וּלְנַפְתָּלִי אָמַר", "וקאל לנפתלי", "And he said for Naphtali"),
        ("נַפְתָּלִי שְׂבַע רָצוֹן", "יא נפתלי אסתכת'ר מן אלרצ'א", "O Naphtali, gain much of favor"),
        ("וּמָלֵא בִּרְכַּת יְהוָה", "וכון ממלווא מן ברכאת אללה", "and be filled with the blessings of God"),
        ("יָם וְדָרוֹם יְרָשָׁה", "וחז מן אלארץ' ג'רבא וגנובא", "and possess from the land westward and southward"),
    ],
    24: [
        ("וּלְאָשֵׁר אָמַר", "וקאל לאשר", "And he said for Asher"),
        ("בָּרוּךְ מִבָּנִים אָשֵׁר", "כן מבארכא מן אלאוליא יא אשר", "Be blessed of the saints, O Asher"),
        ("יְהִי רְצוּי אֶחָיו", "אלד'י סיכון רצ'א אכ'ותה", "who shall be the delight of his brothers"),
        ("וְטֹבֵל בַּשֶּׁמֶן רַגְלוֹ", "וג'אמסא פי אלדהן קדמה", "and who dips his foot in oil"),
    ],
    25: [
        ("מִנְעָלֶךָ", "מג'אלקך", "Your bolts"),
        ("בַּרְזֶל וּנְחֹשֶׁת", "תכון מן אלחדיד ואלנחאס", "shall be of iron and bronze"),
        ("וּכְיָמֶיךָ דָּבְאֶךָ", "ולתכון כאיאמך הד'ה שגאעתך", "and as your days are, so shall your strength be"),
    ],
    26: [
        ("אֵין כָּאֵל יְשֻׁרוּן", "אלאה אסראיל אלד'י ליס כמת'לה", "The God of Israel, who has no likeness"),
        ("רֹכֵב שָׁמַיִם", "סאכן אלסמא", "the Dweller of the heavens"),
        ("וּבְגַאֲוָתוֹ שְׁחָקִים", "ואלשואהק בקדרתה", "and the heights, in His power"),
        ("בְּעֶזְרֶךָ", "פי עונך", "is your help"),
    ],
    27: [
        ("מְעֹנָה אֱלֹהֵי קֶדֶם", "והו אלוטן אלאלאה אלאזלי", "And He is the abode — the God eternal"),
        ("וּמִתַּחַת זְרֹעֹת עוֹלָם", "ומן דונה מלוך אלעאלם", "and beneath Him are the kings of the world"),
        ("וַיְגָרֶשׁ מִפָּנֶיךָ אוֹיֵב", "כמא טרד מן בין ידיך אלעדו", "even as He drove out the enemy from before you"),
        ("וַיֹּאמֶר הַשְׁמֵד", "וקאל לך אנפד'ה", "and said to you: Destroy him"),
    ],
    28: [
        ("וַיִּשְׁכֹּן יִשְׂרָאֵל", "חתי' סכן בעץ' אל אסראיל", "Until some of the clan of Israel settled"),
        ("בֶּטַח בָּדָד", "ואת'קא מנפרדא", "in confidence, each apart"),
        (None, "נצ'יר מא קאל להם יעקוב אביהם", "in fulfilment of what Jacob their father told them"),
        ("אֶל-אֶרֶץ דָּגָן", "פי בלד ד'י בר", "in a land of grain"),
        ("וְתִירוֹשׁ", "ועציר", "and wine-press"),
        ("אַף-שָׁמָיו יַעַרְפוּ טָל", "ואיצ'א סמאה תדר טלא", "and moreover its sky pours down dew"),
    ],
    29: [
        ("אַשְׁרֶיךָ יִשְׂרָאֵל", "פטובאך יא אל אסראיל", "So blessed are you, O clan of Israel"),
        ("מִי כָמוֹךָ", "מן מת'לך", "who is like you"),
        ("עַם נוֹשַׁע בַּיהוָה", "שעב מ'ג'את' באללה", "A people succored by God"),
        ("מָגֵן עֶזְרֶךָ", "והו תרסך ועונך", "and He is your shield and your help"),
        ("וַאֲשֶׁר-חֶרֶב גַּאֲוָתֶךָ", "וסיפך ואקתדארך", "and your sword and your might"),
        ("וְיִכָּחֲשׁוּ אֹיְבֶיךָ לָךְ", "פיכ'צ'ע לך אעדאיך", "So shall your enemies submit to you"),
        ("וְאַתָּה עַל-בָּמוֹתֵימוֹ תִדְרֹךְ", "ואנת תטא עלי קמאקמהם", "and you shall tread upon their heights"),
    ],
}

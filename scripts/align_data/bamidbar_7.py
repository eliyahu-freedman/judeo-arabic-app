"""Hand-authored alignment triples for Bamidbar chapter 7.

This is the 89-verse dedication chapter. The twelve tribal-offering blocks
(vv. 12-83) are an identical repeated formula, so they are aligned at
verse granularity (one whole-verse triple per verse) built directly from
the source strings — guaranteed verbatim. The narrative frame (vv. 1-11)
and the closing summary (vv. 84-89) are hand-authored clause-by-clause.
"""

import json
from pathlib import Path

_DATA = Path(__file__).resolve().parents[2] / "data"
_src = json.loads((_DATA / "tafsir-bamidbar-7.json").read_text(encoding="utf-8"))
_en = json.loads(
    (_DATA / "tafsir-bamidbar-7-english.json").read_text(encoding="utf-8"),
)["translations"]
_by_v = {v["v"]: v for v in _src["verses"]}

# Verse-level fallback for every verse (repeated offering blocks use this).
ALIGNMENTS: dict[int, list[tuple[str | None, str, str]]] = {}
for _n, _v in _by_v.items():
    _e = _en.get(str(_n), "")
    if _e:
        ALIGNMENTS[_n] = [(_v["hebrew"], _v["ja"], _e)]

# Clause-level overrides for the narrative frame and summary.
ALIGNMENTS.update({
    1: [
        ("וַיְהִי בְּיוֹם כַּלּוֹת מֹשֶׁה לְהָקִים אֶת-הַמִּשְׁכָּן",
         "ולמא כאן פי יום פרג' מוסי' מן נצב אלמסכן",
         "And it was on the day when Moses had finished from erecting the tabernacle"),
        ("וַיִּמְשַׁח אֹתוֹ וַיְקַדֵּשׁ אֹתוֹ וְאֶת-כָּל-כֵּלָיו",
         "ומסחה וקדסה וגמיע אניתה",
         "and had anointed it and consecrated it and all its vessels"),
        ("וְאֶת-הַמִּזְבֵּחַ וְאֶת-כָּל-כֵּלָיו", "ואלמד'בח וגמיע אניתה",
         "and the altar and all its vessels"),
        ("וַיִּמְשָׁחֵם וַיְקַדֵּשׁ אֹתָם", "מסחהם וקדסהם",
         "he anointed them and consecrated them."),
    ],
    2: [
        ("וַיַּקְרִיבוּ נְשִׂיאֵי יִשְׂרָאֵל", "פקרב אשראף בני אסראיל",
         "Then the nobles of the sons of Israel drew near"),
        ("רָאשֵׁי בֵּית אֲבֹתָם", "רויסא ביות אבאיהם",
         "heads of their fathers' houses"),
        ("הֵם נְשִׂיאֵי הַמַּטֹּת", "אלד'י הם רויסא אלאסבאט",
         "they being heads of the tribes"),
        ("הֵם הָעֹמְדִים עַל-הַפְּקֻדִים", "אלחאצ'רין עלי' עדדהם",
         "those present at their census."),
    ],
    3: [
        ("וַיָּבִיאוּ אֶת-קָרְבָּנָם לִפְנֵי יְהוָה", "פאתו בקרבאנהם ללה",
         "And they brought their offering before God"),
        ("שֵׁשׁ-עֶגְלֹת צָב וּשְׁנֵי עָשָׂר בָּקָר", "סת עגל מצ'בבה ואת'ני עשר ת'ורא",
         "six covered wagons and twelve oxen"),
        ("עֲגָלָה עַל-שְׁנֵי הַנְּשִׂאִים וְשׁוֹר לְאֶחָד",
         "עגלה לכל שריפין ות'ור לכל ואחד",
         "a wagon for every two nobles and an ox for each one"),
        ("וַיַּקְרִיבוּ אוֹתָם לִפְנֵי הַמִּשְׁכָּן", "פקדמוהא בין ידי אלמסכן",
         "and they presented them before the tabernacle."),
    ],
    4: [
        ("וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה לֵּאמֹר", "פקאל אללה למוסי' קאילא",
         "And God said to Moses, saying:"),
    ],
    5: [
        ("קַח מֵאִתָּם", "כ'ד'הא מנהם", "'Take these from them"),
        ("וְהָיוּ לַעֲבֹד אֶת-עֲבֹדַת אֹהֶל מוֹעֵד", "ותכון לכדמה' כ'בא אלמחצ'ר",
         "and they shall be for the service of the tent of meeting"),
        ("וְנָתַתָּה אוֹתָם אֶל-הַלְוִיִּם אִישׁ כְּפִי עֲבֹדָתוֹ",
         "ואדפעהא אלי' כל פריק מן אלליואניין. חסב כ'דמתהם",
         "and distribute them to every group of the Levites according to their service.'"),
    ],
    6: [
        ("וַיִּקַּח מֹשֶׁה אֶת-הָעֲגָלֹת וְאֶת-הַבָּקָר", "פאכ'ד' מוסי'. אלעגל ואלבקר",
         "And Moses took the wagons and the oxen"),
        ("וַיִּתֵּן אוֹתָם אֶל-הַלְוִיִּם", "פדפעהא אלי' אלליואניין",
         "and gave them to the Levites."),
    ],
    7: [
        ("אֵת שְׁתֵּי הָעֲגָלוֹת וְאֵת אַרְבַּעַת הַבָּקָר--נָתַן לִבְנֵי גֵרְשׁוֹן",
         "עגלתין וארבע בקראת. דפעהא לבני גרשון",
         "Two wagons and four oxen he gave to the sons of Gershon"),
        ("כְּפִי עֲבֹדָתָם", "חסב כ'דמתהם", "according to their service."),
    ],
    8: [
        ("וְאֵת אַרְבַּע הָעֲגָלֹת וְאֵת שְׁמֹנַת הַבָּקָר--נָתַן לִבְנֵי מְרָרִי",
         "וארבע עגל. ות'מאן בקראת. דפע לבני מררי",
         "And four wagons and eight oxen he gave to the sons of Merari"),
        ("כְּפִי עֲבֹדָתָם", "חסב כ'דמתהם", "according to their service"),
        ("בְּיַד אִיתָמָר בֶּן-אַהֲרֹן הַכֹּהֵן", "ואלגמיע עלי' יד איתמר. אבן הרון אלאמאם",
         "all of it under the hand of Ithamar son of Aaron the imām."),
    ],
    9: [
        ("וְלִבְנֵי קְהָת לֹא נָתָן", "ולבני קהת לם ידפע שייא",
         "But to the sons of Kohath he gave nothing"),
        ("כִּי-עֲבֹדַת הַקֹּדֶשׁ עֲלֵהֶם", "לאן כדמה' אלקדס עלי'הם",
         "because the service of the sanctuary was upon them"),
        ("בַּכָּתֵף יִשָּׂאוּ", "ואנמי' יחמלונה עלי' אכתאפהם",
         "rather they carry it upon their shoulders."),
    ],
    10: [
        ("וַיַּקְרִיבוּ הַנְּשִׂאִים אֵת חֲנֻכַּת הַמִּזְבֵּחַ בְּיוֹם הִמָּשַׁח אֹתוֹ",
         "ולמא קדם אלאשראף דשן אלמד'בח. פי יום מסח",
         "And when the nobles brought the inauguration-gift of the altar on the day of its anointing"),
        ("וַיַּקְרִיבוּ הַנְּשִׂיאִם אֶת-קָרְבָּנָם לִפְנֵי הַמִּזְבֵּחַ",
         "וקדמו קראבינהם בין ידי אלמד'בח",
         "they presented their offerings before the altar."),
    ],
    11: [
        ("וַיֹּאמֶר יְהוָה אֶל-מֹשֶׁה", "פקאל אללה למוסי'", "And God said to Moses"),
        ("נָשִׂיא אֶחָד לַיּוֹם נָשִׂיא אֶחָד לַיּוֹם", "שריף ואחד פי כל יום",
         "'One noble per day"),
        ("יַקְרִיבוּ אֶת-קָרְבָּנָם לַחֲנֻכַּת הַמִּזְבֵּחַ", "יקרב קרבאנה דשנא לאלמד'בח",
         "shall present his offering as an inauguration-gift for the altar.'"),
    ],
    84: [
        ("זֹאת חֲנֻכַּת הַמִּזְבֵּחַ בְּיוֹם הִמָּשַׁח אֹתוֹ מֵאֵת נְשִׂיאֵי יִשְׂרָאֵל",
         "הד'א גמלה' דשן אלמד'בח. פי יום מסח. מן אשראף בני אסראיל",
         "This is the total of the inauguration-gift of the altar on the day of its anointing, from the nobles of the sons of Israel"),
        ("קַעֲרֹת כֶּסֶף שְׁתֵּים עֶשְׂרֵה", "מן קצאע אלפצ'ה את'ני עשר",
         "twelve silver bowls"),
        ("מִזְרְקֵי-כֶסֶף שְׁנֵים עָשָׂר", "ומן כ'ראנב אלפצ'ה את'ני עשר",
         "twelve silver basins"),
        ("כַּפּוֹת זָהָב שְׁתֵּים עֶשְׂרֵה", "ומן ד'רוג אלדהב את'ני עשר",
         "and twelve gold caskets."),
    ],
    85: [
        ("שְׁלֹשִׁים וּמֵאָה הַקְּעָרָה הָאַחַת כֶּסֶף", "כל קצעה מן מאיה ות'לאת'ין מת'קאל פצ'ה",
         "Each bowl of a hundred and thirty shekels of silver"),
        ("וְשִׁבְעִים הַמִּזְרָק הָאֶחָד", "וכל כ'רנוב מן סבעין",
         "and each basin of seventy shekels of silver"),
        ("כֹּל כֶּסֶף הַכֵּלִים אַלְפַּיִם וְאַרְבַּע-מֵאוֹת בְּשֶׁקֶל הַקֹּדֶשׁ",
         "פד'אלך גמיע פצ'ה' אלאואני. אלפין וארבע מאיה' מת'קאל במת'קאל אלקדס",
         "so all the silver of the vessels: two thousand and four hundred shekels by the shekel of the sanctuary."),
    ],
    86: [
        ("כַּפּוֹת זָהָב שְׁתֵּים-עֶשְׂרֵה מְלֵאֹת קְטֹרֶת", "ודרוג אלדהב את'ני עשר ממלווה בכ'ורא",
         "And the gold caskets — twelve, filled with incense"),
        ("עֲשָׂרָה עֲשָׂרָה הַכַּף בְּשֶׁקֶל הַקֹּדֶשׁ", "כל דרג מן עשרה מת'אקיל במת'קאל אלקדס",
         "each casket of ten shekels by the shekel of the sanctuary"),
        ("כָּל-זְהַב הַכַּפּוֹת עֶשְׂרִים וּמֵאָה", "פד'אלך גמיע ד'הב אלדרוג מאיה ועשרין מת'קאל",
         "so all the gold of the caskets: a hundred and twenty shekels."),
    ],
    87: [
        ("כָּל-הַבָּקָר לָעֹלָה שְׁנֵים עָשָׂר פָּרִים", "וגמיע בקר אלצעידה את'ני עשר רת'",
         "And all the cattle of the ascent-offering: twelve bulls"),
        ("אֵילִם שְׁנֵים-עָשָׂר", "ואלכבאש את'ני עשר", "and the rams twelve"),
        ("כְּבָשִׂים בְּנֵי-שָׁנָה שְׁנֵים עָשָׂר--וּמִנְחָתָם",
         "ואלחמלאן בני סנה. את'ני עשר ואלבר מעהם",
         "and the yearling lambs twelve, with their grain-offering"),
        ("וּשְׂעִירֵי עִזִּים שְׁנֵים עָשָׂר לְחַטָּאת", "ואלעתדאן את'ני עשר לאלדכוה",
         "and the he-goats twelve, for the purification-offering."),
    ],
    88: [
        ("וְכֹל בְּקַר זֶבַח הַשְּׁלָמִים עֶשְׂרִים וְאַרְבָּעָה פָּרִים",
         "וגמיע בקר ד'בח אלסלאמה. ארבעה ועשרין בקראת",
         "And all the cattle of the peace-sacrifice: twenty-four heifers"),
        ("אֵילִם שִׁשִּׁים עַתֻּדִים שִׁשִּׁים כְּבָשִׂים בְּנֵי-שָׁנָה שִׁשִּׁים",
         "וסתין כבש וסתין עתוד. וסתין חמל בני סנה",
         "sixty rams, sixty he-goats, and sixty yearling lambs"),
        ("זֹאת חֲנֻכַּת הַמִּזְבֵּחַ אַחֲרֵי הִמָּשַׁח אֹתוֹ", "הד'א דשן אלמד'בח. בעד מא מסח",
         "This was the inauguration-gift of the altar after it was anointed."),
    ],
    89: [
        ("וּבְבֹא מֹשֶׁה אֶל-אֹהֶל מוֹעֵד לְדַבֵּר אִתּוֹ",
         "וכאן אד'א דכ'ל מוסי'. אלי' כ'בא אלמחצ'ר ליכלם",
         "And it was that whenever Moses entered the tent of meeting to be spoken with"),
        ("וַיִּשְׁמַע אֶת-הַקּוֹל מִדַּבֵּר אֵלָיו", "יסמע אלצות מכ'אטבה",
         "he would hear the voice addressing him"),
        ("מֵעַל הַכַּפֹּרֶת אֲשֶׁר עַל-אֲרֹן הָעֵדֻת",
         "מן פוק אלג'שא אלד'י עלי' צנדוק אלשהאדה",
         "from above the cover that was upon the ark of the testimony"),
        ("מִבֵּין שְׁנֵי הַכְּרֻבִים", "מן בין אלכרובין", "from between the two cherubim"),
        ("וַיְדַבֵּר אֵלָיו", "פיכ'אטבה הנאך", "and it would address him there."),
    ],
})

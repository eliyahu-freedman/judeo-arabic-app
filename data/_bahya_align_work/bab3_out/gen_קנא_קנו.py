#!/usr/bin/env python3
"""Generate alignment output for bab3 pages קנא–קנו."""
import json, pathlib

OUT = pathlib.Path(__file__).parent

def write(page_he, segs):
    obj = {"pages": {page_he: segs}}
    (OUT / f"{page_he}.json").write_text(
        json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"wrote {page_he}.json  ({len(segs)} segs)")

# ── קנא ────────────────────────────────────────────────────────────────────
write("קנא", [
  {
    "ja": "ענהם מן אלתנאים, והם אצחאב אלמשנה ואלבריתות עלי מא ד'כר פי מסכת אבות,",
    "en": "of the Tanna'im, who are the masters of the Mishnah and the Beraitot, as is mentioned in tractate Avot:",
    "isHeader": False,
    "pairs": [
      {"ja": "ענהם מן אלתנאים", "en": "of the Tanna'im"},
      {"ja": "והם אצחאב אלמשנה ואלבריתות", "en": "who are the masters of the Mishnah and the Beraitot"},
      {"ja": "עלי מא ד'כר פי מסכת אבות", "en": "as is mentioned in tractate Avot"}
    ]
  },
  {
    "ja": "משה קבל תורה מסיני, ומסרה ליהושע, ויהושע לזקנים, וזקנים לנביאים, ונביאים מסרוה לאנשי כנסת הגדולה, ואנשי כנסת הגדולה לשמעון הצדיק, ושמעון הצדיק לאנטיגנוס, ואנטיגנוס ליוסי בן יועזר וליוסי בן יוחנן איש ירושלם, והם מסרוה ליהושע בן פרחיה ונתאי הארבלי, והם מסרוה ליהודה בן טבאי ולשמעון בן שטח, והם מסרוה לשמעיה ואבטליון, ומהם לשמאי והלל, ומהם לרבן יוחנן בן זכאי, ורבן יוחנן בן זכאי לר' אליעזר ור' יהושע ורבן גמליאיל ור' אלעזר בן ערך ור' יוסי הכהן ור' שמעון בן נתנאל, ומהם לר' עקיבה ור' אלעזר בן עזריה ור' טרפון ורבן שמעון בן גמליאל, ומהם לר' מאיר ור' יהודה ור' יוסי ור' שמעון ורבנו יהודה הנשיא",
    "en": "\"Moses received Torah from Sinai, and transmitted it to Joshua, and Joshua to the Elders, and the Elders to the Prophets, and the Prophets transmitted it to the Men of the Great Assembly; and the Men of the Great Assembly to Simeon the Just, and Simeon the Just to Antigonus, and Antigonus to Yose ben Yoezer and Yose ben Yoḥanan of Jerusalem; they transmitted it to Yehoshua ben Peraḥyah and Nittai the Arbelite; they transmitted it to Yehudah ben Tabbai and Shimʿon ben Shataḥ; they transmitted it to Shemaiah and Avtalion; from them to Shammai and Hillel; from them to Rabban Yoḥanan ben Zakkai, and Rabban Yoḥanan ben Zakkai to Rabbi Eliʿezer and Rabbi Yehoshua and Rabban Gamliel and Rabbi Elʿazar ben ʿArakh and Rabbi Yose the Priest and Rabbi Shimʿon ben Netan'el; from them to Rabbi ʿAkiva and Rabbi Elʿazar ben ʿAzaryah and Rabbi Tarfon and Rabban Shimʿon ben Gamliel; from them to Rabbi Meir and Rabbi Yehudah and Rabbi Yose and Rabbi Shimʿon and our Rabbi Yehudah the Prince",
    "isHeader": False,
    "pairs": [
      {"ja": "משה קבל תורה מסיני", "en": "Moses received Torah from Sinai"},
      {"ja": "ומסרה ליהושע", "en": "and transmitted it to Joshua"},
      {"ja": "ויהושע לזקנים", "en": "and Joshua to the Elders"},
      {"ja": "וזקנים לנביאים", "en": "and the Elders to the Prophets"},
      {"ja": "ונביאים מסרוה לאנשי כנסת הגדולה", "en": "and the Prophets transmitted it to the Men of the Great Assembly"},
      {"ja": "ואנשי כנסת הגדולה לשמעון הצדיק", "en": "and the Men of the Great Assembly to Simeon the Just"},
      {"ja": "ושמעון הצדיק לאנטיגנוס", "en": "and Simeon the Just to Antigonus"},
      {"ja": "ואנטיגנוס ליוסי בן יועזר וליוסי בן יוחנן איש ירושלם", "en": "and Antigonus to Yose ben Yoezer and Yose ben Yoḥanan of Jerusalem"},
      {"ja": "והם מסרוה ליהושע בן פרחיה ונתאי הארבלי", "en": "they transmitted it to Yehoshua ben Peraḥyah and Nittai the Arbelite"},
      {"ja": "והם מסרוה ליהודה בן טבאי ולשמעון בן שטח", "en": "they transmitted it to Yehudah ben Tabbai and Shimʿon ben Shataḥ"},
      {"ja": "והם מסרוה לשמעיה ואבטליון", "en": "they transmitted it to Shemaiah and Avtalion"},
      {"ja": "ומהם לשמאי והלל", "en": "from them to Shammai and Hillel"},
      {"ja": "ומהם לרבן יוחנן בן זכאי", "en": "from them to Rabban Yoḥanan ben Zakkai"},
      {"ja": "ורבן יוחנן בן זכאי לר' אליעזר ור' יהושע ורבן גמליאיל ור' אלעזר בן ערך ור' יוסי הכהן ור' שמעון בן נתנאל", "en": "and Rabban Yoḥanan ben Zakkai to Rabbi Eliʿezer and Rabbi Yehoshua and Rabban Gamliel and Rabbi Elʿazar ben ʿArakh and Rabbi Yose the Priest and Rabbi Shimʿon ben Netan'el"},
      {"ja": "ומהם לר' עקיבה ור' אלעזר בן עזריה ור' טרפון ורבן שמעון בן גמליאל", "en": "from them to Rabbi ʿAkiva and Rabbi Elʿazar ben ʿAzaryah and Rabbi Tarfon and Rabban Shimʿon ben Gamliel"},
      {"ja": "ומהם לר' מאיר ור' יהודה ור' יוסי ור' שמעון ורבנו יהודה הנשיא", "en": "from them to Rabbi Meir and Rabbi Yehudah and Rabbi Yose and Rabbi Shimʿon and our Rabbi Yehudah the Prince"}
    ]
  },
  {
    "ja": "והו רבנו הקדוש אלד'י ג'מע מעאני אלמשנה ואת'בתהא ופצלהא וקיידהא, והי אצל אלנקל אלמעתמד עליה פי שריעתנא.",
    "en": "— and he is our Holy Rabbi who collected the meanings of the Mishnah, established them, parsed them, and bound them; and that is the root of the tradition relied on in our Law.",
    "isHeader": False,
    "pairs": [
      {"ja": "והו רבנו הקדוש", "en": "and he is our Holy Rabbi"},
      {"ja": "אלד'י ג'מע מעאני אלמשנה", "en": "who collected the meanings of the Mishnah"},
      {"ja": "ואת'בתהא", "en": "established them"},
      {"ja": "ופצלהא", "en": "parsed them"},
      {"ja": "וקיידהא", "en": "and bound them"},
      {"ja": "והי אצל אלנקל אלמעתמד עליה פי שריעתנא", "en": "that is the root of the tradition relied on in our Law"}
    ]
  },
  {
    "ja": "ואמא מד'אהב אהל אלשריעה פי אעתקאדהם להא ואלתזאם אלטאעה ללה בהא פעלי עשר דרג'את.",
    "en": "As for the schools of the people of the Law in their firm conviction of it and their binding themselves to obedience to God by it — they are on ten degrees.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואמא מד'אהב אהל אלשריעה", "en": "As for the schools of the people of the Law"},
      {"ja": "פי אעתקאדהם להא", "en": "in their firm conviction of it"},
      {"ja": "ואלתזאם אלטאעה ללה בהא", "en": "their binding themselves to obedience to God by it"},
      {"ja": "פעלי עשר דרג'את", "en": "they are on ten degrees"}
    ]
  },
  {
    "ja": "אולהא, קום חמלהם אלג'הל מן תמכן אלשהואת מנהם עלי רפץ' אלשריעה, וחמלוהא מחמל אלסיאסה אלתי בהא יסאס אלאמם, ואלנואמיס אלתי בהא ידבר אלג'האל, לגלבהֵ אלהוי עלי עקולהם וכ'שונהֵ טבאיעהם, פלם יתת'קפוא לזמאם אלשריעה, ולם ינקאדוא לת'קאף אלעקל טלבא ללהמל,",
    "en": "The first: a folk whom ignorance — from the establishment of appetites in them — has carried to the rejection of the Law; they take it as a polity of the sort by which the nations are governed, and laws by which the ignorant are managed, on account of the overcoming of passion upon their intellects and the coarseness of their natures. They have not lifted themselves to the bridle of the Law, nor been led by the reining-in of the intellect — seeking unrestraint.",
    "isHeader": False,
    "pairs": [
      {"ja": "אולהא", "en": "The first"},
      {"ja": "קום חמלהם אלג'הל", "en": "a folk whom ignorance"},
      {"ja": "מן תמכן אלשהואת מנהם", "en": "from the establishment of appetites in them"},
      {"ja": "עלי רפץ' אלשריעה", "en": "has carried to the rejection of the Law"},
      {"ja": "וחמלוהא מחמל אלסיאסה", "en": "they take it as a polity"},
      {"ja": "אלתי בהא יסאס אלאמם", "en": "by which the nations are governed"},
      {"ja": "ואלנואמיס אלתי בהא ידבר אלג'האל", "en": "and laws by which the ignorant are managed"},
      {"ja": "לגלבהֵ אלהוי עלי עקולהם", "en": "on account of the overcoming of passion upon their intellects"},
      {"ja": "וכ'שונהֵ טבאיעהם", "en": "and the coarseness of their natures"},
      {"ja": "פלם יתת'קפוא לזמאם אלשריעה", "en": "They have not lifted themselves to the bridle of the Law"},
      {"ja": "ולם ינקאדוא לת'קאף אלעקל", "en": "nor been led by the reining-in of the intellect"},
      {"ja": "טלבא ללהמל", "en": "seeking unrestraint"}
    ]
  },
  {
    "ja": "ופי מת'להם קאל אלחכים לא יחפוץ כסיל בתבונה כי אם בהתגלות לבו.",
    "en": "Concerning them the Wise One said: \"The fool has no delight in understanding, but only in disclosing his heart\" (Proverbs 18:2).",
    "isHeader": False,
    "pairs": [
      {"ja": "ופי מת'להם", "en": "Concerning them"},
      {"ja": "קאל אלחכים", "en": "the Wise One said"},
      {"ja": "לא יחפוץ כסיל בתבונה", "en": "The fool has no delight in understanding"},
      {"ja": "כי אם בהתגלות לבו", "en": "but only in disclosing his heart"}
    ]
  }
])

# ── קנב ────────────────────────────────────────────────────────────────────
write("קנב", [
  {
    "ja": "ואלדרג'ה אלת'אניה, קום לם יסע להם רד אלאיאת ותנכיר אלאעלאם אלתי ט'הרת עלי יד אלרסול ע\"ס לשהרתהא, אלא אנהם שכוא פי צחהֵ אלשריעה וקאלוא אקואלא קריבה מן מד'הב מן תקדם ד'כרה,",
    "en": "The second degree: a folk to whom it was not possible to refute the signs and deny the demonstrations that appeared at the hand of the Messenger (peace be upon him), on account of their fame; yet they doubted the validity of the Law and uttered sayings close to the school of the first,",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלת'אניה", "en": "The second degree"},
      {"ja": "קום לם יסע להם רד אלאיאת", "en": "a folk to whom it was not possible to refute the signs"},
      {"ja": "ותנכיר אלאעלאם אלתי ט'הרת עלי יד אלרסול ע\"ס", "en": "and deny the demonstrations that appeared at the hand of the Messenger (peace be upon him)"},
      {"ja": "לשהרתהא", "en": "on account of their fame"},
      {"ja": "אלא אנהם שכוא פי צחהֵ אלשריעה", "en": "yet they doubted the validity of the Law"},
      {"ja": "וקאלוא אקואלא קריבה מן מד'הב מן תקדם ד'כרה", "en": "and uttered sayings close to the school of the first"}
    ]
  },
  {
    "ja": "וד'לך, אן אללה אראד ארשאד כ'לקה אלי מא תנתט'ם בה אחואלהם פי אלדניא, פנבה אלנבי עלי סיאסתהם במא יואפקהם מן אלסנן, ואעטאה אללה אלאעלאם ואלאיאת ואלבראהין ליטאע אמרה וילתזם סנתה מן גיר תחקיק מנהם באלת'ואב ואלעקאב.",
    "en": "namely that God wished to guide His creatures to what their states would be ordered by in this world, so He awakened the Prophet to their governance with what would suit them of customs, and gave him the signs, demonstrations, and proofs that his command might be obeyed and his way binding upon them — without truthful verification on their part of reward and punishment.",
    "isHeader": False,
    "pairs": [
      {"ja": "אן אללה אראד ארשאד כ'לקה", "en": "that God wished to guide His creatures"},
      {"ja": "אלי מא תנתט'ם בה אחואלהם פי אלדניא", "en": "to what their states would be ordered by in this world"},
      {"ja": "פנבה אלנבי עלי סיאסתהם", "en": "so He awakened the Prophet to their governance"},
      {"ja": "במא יואפקהם מן אלסנן", "en": "with what would suit them of customs"},
      {"ja": "ואעטאה אללה אלאעלאם ואלאיאת ואלבראהין", "en": "and gave him the signs, demonstrations, and proofs"},
      {"ja": "ליטאע אמרה וילתזם סנתה", "en": "that his command might be obeyed and his way binding"},
      {"ja": "מן גיר תחקיק מנהם באלת'ואב ואלעקאב", "en": "without truthful verification on their part of reward and punishment"}
    ]
  },
  {
    "ja": "ונרי אן נביין מא עליהם מן אלרד באיג'אז עלי אלממאנעה ועלי אלמתאבעה.",
    "en": "It is fitting that we set out, in compressed form, what is upon them of refutation — both in their refusal and in their following.",
    "isHeader": False,
    "pairs": [
      {"ja": "ונרי אן נביין", "en": "It is fitting that we set out"},
      {"ja": "מא עליהם מן אלרד באיג'אז", "en": "in compressed form, what is upon them of refutation"},
      {"ja": "עלי אלממאנעה ועלי אלמתאבעה", "en": "both in their refusal and in their following"}
    ]
  },
  {
    "ja": "אמא עלי אלממאנעה, פאן אללה תעאלי אג'ל ואסני מן אן יכ'רק אלעאדה למן יכד'ב עליה ויקול ענה מא לם יקול ואן כאן מרשדא פי כד'בה עלי אללה עז וג'ל, אד' ליס נזול אלוחי מן אללה עלי אלנבי אעג'ב ואעסר מן כ'רק אלעאדה לה.",
    "en": "As for the refusal: God (exalted be He) is more splendid and more high than to break the ordinary for one who would deceive in His name and ascribe to Him what He did not say, even if [that one] were a guide despite his lying about God (mighty and exalted) — since the descent of revelation upon the prophet is not more wondrous or more difficult than the breaking of the ordinary for him.",
    "isHeader": False,
    "pairs": [
      {"ja": "אמא עלי אלממאנעה", "en": "As for the refusal"},
      {"ja": "אן אללה תעאלי אג'ל ואסני", "en": "God (exalted be He) is more splendid and more high"},
      {"ja": "מן אן יכ'רק אלעאדה", "en": "than to break the ordinary"},
      {"ja": "למן יכד'ב עליה", "en": "for one who would deceive in His name"},
      {"ja": "ויקול ענה מא לם יקול", "en": "and ascribe to Him what He did not say"},
      {"ja": "ואן כאן מרשדא פי כד'בה עלי אללה עז וג'ל", "en": "even if [that one] were a guide despite his lying about God (mighty and exalted)"},
      {"ja": "אד' ליס נזול אלוחי מן אללה עלי אלנבי", "en": "since the descent of revelation upon the prophet"},
      {"ja": "אעג'ב ואעסר מן כ'רק אלעאדה לה", "en": "is not more wondrous or more difficult than the breaking of the ordinary for him"}
    ]
  },
  {
    "ja": "ואמא עלי אלמתאבעה, לו צח באלדליל אלואצ'ח אנה כד'לך לכאן אלאנקיאד אלי קולה ואג'ב, לאן אללה תעאלי לא יכ'רק עאדה ולא יט'הר מעג'זה עלי יד ג'אהל בטריק אלהדי ואלרשאד,",
    "en": "As for the following: if it were validly established by clear evidence that it is so, compliance with his word would be obligatory — for God (exalted be He) does not break an ordinary and does not manifest a miracle at the hand of an ignorant one in the way of guidance and direction.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואמא עלי אלמתאבעה", "en": "As for the following"},
      {"ja": "לו צח באלדליל אלואצ'ח אנה כד'לך", "en": "if it were validly established by clear evidence that it is so"},
      {"ja": "לכאן אלאנקיאד אלי קולה ואג'ב", "en": "compliance with his word would be obligatory"},
      {"ja": "לאן אללה תעאלי לא יכ'רק עאדה", "en": "for God (exalted be He) does not break an ordinary"},
      {"ja": "ולא יט'הר מעג'זה עלי יד ג'אהל", "en": "and does not manifest a miracle at the hand of an ignorant one"},
      {"ja": "בטריק אלהדי ואלרשאד", "en": "in the way of guidance and direction"}
    ]
  },
  {
    "ja": "ומן אצטפאה אללה לארשאדנא ותדבירנא בעד ט'הור אלאעלאם עלי ידיה לאהל אן נקלדה סיאסתנא ותדבירנא,",
    "en": "The one whom God has chosen for our guidance and management — after the manifesting of the signs at his hand — is worthy that we follow him in our governance and management,",
    "isHeader": False,
    "pairs": [
      {"ja": "ומן אצטפאה אללה לארשאדנא ותדבירנא", "en": "The one whom God has chosen for our guidance and management"},
      {"ja": "בעד ט'הור אלאעלאם עלי ידיה", "en": "after the manifesting of the signs at his hand"},
      {"ja": "לאהל אן נקלדה סיאסתנא ותדבירנא", "en": "is worthy that we follow him in our governance and management"}
    ]
  },
  {
    "ja": "וקד ילזמנא ד'לך לראיס או סלטאן מן גיר עלם, כקולה ירא את ה' בני ומלך עם שונים אל תתערב, פכיף מן ט'הר מעג'ז עלי ידה.",
    "en": "since this is binding on us for any chief or sultan even apart from knowledge, as he said: \"Fear God, my son, and the king; do not associate with those who change\" (Proverbs 24:21) — how much more for one at whose hand a miracle is manifest.",
    "isHeader": False,
    "pairs": [
      {"ja": "וקד ילזמנא ד'לך", "en": "since this is binding on us"},
      {"ja": "לראיס או סלטאן מן גיר עלם", "en": "for any chief or sultan even apart from knowledge"},
      {"ja": "כקולה", "en": "as he said"},
      {"ja": "ירא את ה' בני ומלך עם שונים אל תתערב", "en": "Fear God, my son, and the king; do not associate with those who change"},
      {"ja": "פכיף מן ט'הר מעג'ז עלי ידה", "en": "how much more for one at whose hand a miracle is manifest"}
    ]
  },
  {
    "ja": "פעלי אלוג'הין ילזמהם אלתזאם אלשריעה, ופי",
    "en": "On both grounds, then, the binding force of the Law is incumbent upon them — and concerning",
    "isHeader": False,
    "pairs": [
      {"ja": "פעלי אלוג'הין", "en": "On both grounds"},
      {"ja": "ילזמהם אלתזאם אלשריעה", "en": "the binding force of the Law is incumbent upon them"}
    ]
  }
])

# ── קנג ────────────────────────────────────────────────────────────────────
write("קנג", [
  {
    "ja": "מת'להם קאל אלחכים הבינו פתאים ערמה וכסילים הבינו לב.",
    "en": "their like the Wise One said: \"Understand prudence, O simple ones, and you fools, understand the heart\" (Proverbs 8:5).",
    "isHeader": False,
    "pairs": [
      {"ja": "מת'להם קאל אלחכים", "en": "their like the Wise One said"},
      {"ja": "הבינו פתאים ערמה", "en": "Understand prudence, O simple ones"},
      {"ja": "וכסילים הבינו לב", "en": "and you fools, understand the heart"}
    ]
  },
  {
    "ja": "ואלדרג'ה אלת'אלת'ה, קום צח ענדהם חקיקהֵ אלשריעה, וזעמוא אנהא פצ'ל מן אללה תעאלי לארשאד כ'לקה בהא פי הד'ה אלדאר וסיאסתהם פי הד'א אלעאלם פקט, לא לת'ואב פי אלאכ'רה ולא לעקאב.",
    "en": "The third degree: a folk for whom the true reality of the Law has been validly established, but who claim that it is a bounty from God (exalted be He) for the guidance of His creatures by it in this house only, and for their governance in this world only — not for reward in the next world, nor for punishment.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלת'אלת'ה", "en": "The third degree"},
      {"ja": "קום צח ענדהם חקיקהֵ אלשריעה", "en": "a folk for whom the true reality of the Law has been validly established"},
      {"ja": "וזעמוא אנהא פצ'ל מן אללה תעאלי", "en": "but who claim that it is a bounty from God (exalted be He)"},
      {"ja": "לארשאד כ'לקה בהא פי הד'ה אלדאר", "en": "for the guidance of His creatures by it in this house only"},
      {"ja": "וסיאסתהם פי הד'א אלעאלם פקט", "en": "and for their governance in this world only"},
      {"ja": "לא לת'ואב פי אלאכ'רה ולא לעקאב", "en": "not for reward in the next world, nor for punishment"}
    ]
  },
  {
    "ja": "וגלטהם פי ד'לך מא תרדד פי כתב אלאנביא מן אלת'ואב ואלעקאב פי אלדניא דון אלאכ'רה,",
    "en": "Their mistake in this is from what is repeated in the books of the prophets of reward and punishment in this world without the next.",
    "isHeader": False,
    "pairs": [
      {"ja": "וגלטהם פי ד'לך", "en": "Their mistake in this"},
      {"ja": "מא תרדד פי כתב אלאנביא", "en": "is from what is repeated in the books of the prophets"},
      {"ja": "מן אלת'ואב ואלעקאב פי אלדניא דון אלאכ'רה", "en": "of reward and punishment in this world without the next"}
    ]
  },
  {
    "ja": "וקד אחתפל רבנו סעדיה רצ'י אללה ענה פי שרח אם בחקותי תלכו בד'כר מא יתביין פיה פסאד מד'הב האולא אלקום,",
    "en": "Our Rabbi Saadia (may God be pleased with him) attended carefully in his commentary on If you walk in My statutes (Leviticus 26:3) to the mention of what makes manifest the corruption of the school of this folk.",
    "isHeader": False,
    "pairs": [
      {"ja": "וקד אחתפל רבנו סעדיה רצ'י אללה ענה", "en": "Our Rabbi Saadia (may God be pleased with him) attended carefully"},
      {"ja": "פי שרח אם בחקותי תלכו", "en": "in his commentary on If you walk in My statutes"},
      {"ja": "בד'כר מא יתביין פיה פסאד מד'הב האולא אלקום", "en": "to the mention of what makes manifest the corruption of the school of this folk"}
    ]
  },
  {
    "ja": "ופי כתב אלאנביא את'אר קויה מן אמר אלת'ואב ואלעקאב פי אלאכ'רה, מנהא קול אלולי ע\"ס כי את כל מעשה האלהים יביא במשפט על כל נעלם אם טוב ואם רע, ומנהא קולה ועסותם רשעים כי יהיו אפר תחת כפות רגליכם, וקאל ושבתם וראיתם בין צדיק לרשע בין עובד אלהים לאשר לא עבדו, וקאל ויצאו וראו בפגרי האנשים הפושעים בי כי תולעתם לא תמות ואשם לא תכבה והיו דראון לכל בשר, וקאל מה רב טובך אשר צפנת ליראיך פעלת לחוסים בך נגד בני אדם, וקאל ונתתי לך מהלכים בין העומדים האלה, וקאל עין לא ראתה אלהים זולתך יעשה למחכה לו, וקאל ורבים מישני אדמת עפר יקיצו אלה לחיי עולם ואלה לחרפות ולדראון עולם, ומנהא קולה והלך לפניך צדקך כבוד ה' יאספך, וכת'יר מת'ל ד'לך ממא יטול וצפה.",
    "en": "In the books of the prophets are strong traces of the matter of reward and punishment in the next world — among them the saying of the Friend (peace be upon him): \"For God shall bring every work into judgment over every hidden thing, whether it be good or evil\" (Ecclesiastes 12:14), and: \"And you shall tread down the wicked, for they shall be ash under the soles of your feet\" (Malachi 3:21), and: \"Then you shall return and see between the righteous and the wicked, between him that serves God and him that does not serve Him\" (Malachi 3:18), and: \"And they shall go forth and look upon the carcasses of the men who have transgressed against Me; for their worm shall not die, neither shall their fire be quenched; and they shall be a horror to all flesh\" (Isaiah 66:24), and: \"How great is Your goodness which You have stored up for those who fear You; You have wrought for those who take refuge in You, in the presence of the sons of men\" (Psalms 31:20), and: \"And I will give you free access among these who stand\" (Zechariah 3:7), and: \"Eye has not seen a God beside You who works for him that waits for Him\" (Isaiah 64:3), and: \"And many of those that sleep in the dust of the earth shall awake, some to everlasting life and some to reproaches and everlasting horror\" (Daniel 12:2), and among them: \"And your righteousness shall go before you, the glory of the Lord shall gather you in\" (Isaiah 58:8), and many like this whose description would take long.",
    "isHeader": False,
    "pairs": [
      {"ja": "ופי כתב אלאנביא את'אר קויה", "en": "In the books of the prophets are strong traces"},
      {"ja": "מן אמר אלת'ואב ואלעקאב פי אלאכ'רה", "en": "of the matter of reward and punishment in the next world"},
      {"ja": "מנהא קול אלולי ע\"ס", "en": "among them the saying of the Friend (peace be upon him)"},
      {"ja": "כי את כל מעשה האלהים יביא במשפט על כל נעלם אם טוב ואם רע", "en": "For God shall bring every work into judgment over every hidden thing, whether it be good or evil"},
      {"ja": "ועסותם רשעים כי יהיו אפר תחת כפות רגליכם", "en": "And you shall tread down the wicked, for they shall be ash under the soles of your feet"},
      {"ja": "ושבתם וראיתם בין צדיק לרשע בין עובד אלהים לאשר לא עבדו", "en": "Then you shall return and see between the righteous and the wicked, between him that serves God and him that does not serve Him"},
      {"ja": "ויצאו וראו בפגרי האנשים הפושעים בי כי תולעתם לא תמות ואשם לא תכבה והיו דראון לכל בשר", "en": "And they shall go forth and look upon the carcasses of the men who have transgressed against Me; for their worm shall not die, neither shall their fire be quenched; and they shall be a horror to all flesh"},
      {"ja": "מה רב טובך אשר צפנת ליראיך פעלת לחוסים בך נגד בני אדם", "en": "How great is Your goodness which You have stored up for those who fear You; You have wrought for those who take refuge in You, in the presence of the sons of men"},
      {"ja": "ונתתי לך מהלכים בין העומדים האלה", "en": "And I will give you free access among these who stand"},
      {"ja": "עין לא ראתה אלהים זולתך יעשה למחכה לו", "en": "Eye has not seen a God beside You who works for him that waits for Him"},
      {"ja": "ורבים מישני אדמת עפר יקיצו אלה לחיי עולם ואלה לחרפות ולדראון עולם", "en": "And many of those that sleep in the dust of the earth shall awake, some to everlasting life and some to reproaches and everlasting horror"},
      {"ja": "והלך לפניך צדקך כבוד ה' יאספך", "en": "And your righteousness shall go before you, the glory of the Lord shall gather you in"},
      {"ja": "וכת'יר מת'ל ד'לך ממא יטול וצפה", "en": "and many like this whose description would take long"}
    ]
  },
  {
    "ja": "ואלדרג'ה אלראבעה, קום ת'בת פי נפוסהם צחהֵ אלשריעה וחקיקהֵ אלת'ואב ואלעקאב פי אלאכ'רה, אלא אנהם מאלת בהם נפוסהם אלי חב אלדניא ושהואתהא, פאתכ'ד'וא אעמאל",
    "en": "The fourth degree: a folk in whose souls the validity of the Law and the true reality of reward and punishment in the next world are firmly fixed — yet their souls have inclined them toward love of this world and its appetites, so they have taken the acts of",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלראבעה", "en": "The fourth degree"},
      {"ja": "קום ת'בת פי נפוסהם צחהֵ אלשריעה", "en": "a folk in whose souls the validity of the Law"},
      {"ja": "וחקיקהֵ אלת'ואב ואלעקאב פי אלאכ'רה", "en": "and the true reality of reward and punishment in the next world are firmly fixed"},
      {"ja": "אלא אנהם מאלת בהם נפוסהם אלי חב אלדניא ושהואתהא", "en": "yet their souls have inclined them toward love of this world and its appetites"},
      {"ja": "פאתכ'ד'וא אעמאל", "en": "so they have taken the acts of"}
    ]
  }
])

# ── קנד ────────────────────────────────────────────────────────────────────
write("קנד", [
  {
    "ja": "אלטאעה מצאיד יצידון בהא אלדניא, ואלתזמוא אלשריעה בט'אהרהם לא בבאטנהם, ובאלסנתהם לא בקלובהם, ופי מת'להם קיל בפיו שלום את רעהו ידבר ובקרבו ישים ארבו.",
    "en": "obedience as snares with which they hunt for this world; they bind themselves to the Law in their outward but not in their inward, in their tongues but not in their hearts. Concerning their like it is said: \"He speaks peace with his neighbor with his mouth, but in his interior he sets his ambush\" (Jeremiah 9:7).",
    "isHeader": False,
    "pairs": [
      {"ja": "אלטאעה מצאיד יצידון בהא אלדניא", "en": "obedience as snares with which they hunt for this world"},
      {"ja": "ואלתזמוא אלשריעה בט'אהרהם לא בבאטנהם", "en": "they bind themselves to the Law in their outward but not in their inward"},
      {"ja": "ובאלסנתהם לא בקלובהם", "en": "in their tongues but not in their hearts"},
      {"ja": "ופי מת'להם קיל", "en": "Concerning their like it is said"},
      {"ja": "בפיו שלום את רעהו ידבר ובקרבו ישים ארבו", "en": "He speaks peace with his neighbor with his mouth, but in his interior he sets his ambush"}
    ]
  },
  {
    "ja": "ואלדרג'ה אלכ'אמסה, קום צח להם ג'מיע מא תקדם מן אמר אלשריעה וחקיקהֵ אלת'ואב ואלעקאב פי אלאכ'רה, אלא אנהם מאלת בהם נפוסהם אלי חב אלדניא, ואלתזמוא אלשריעה וקצדוא אלתזאמהא לינאלוא אלת'ואב מן אללה ואלת'נא מן אלנאס וכראמתהם פי אלדניא עליהא, והו באב מן אבואב אלריא, והו אלשרך אלכ'פי.",
    "en": "The fifth degree: a folk for whom the whole of what has gone before of the matter of the Law and the true reality of reward and punishment in the next world has been validly established, except that their souls have inclined them toward love of this world; they have bound themselves to the Law, and intended in binding themselves to it to attain the reward from God and people's praise and honor in this world by it — and that is one of the gates of ostentation, namely the hidden associationism.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלכ'אמסה", "en": "The fifth degree"},
      {"ja": "קום צח להם ג'מיע מא תקדם מן אמר אלשריעה", "en": "a folk for whom the whole of what has gone before of the matter of the Law"},
      {"ja": "וחקיקהֵ אלת'ואב ואלעקאב פי אלאכ'רה", "en": "and the true reality of reward and punishment in the next world has been validly established"},
      {"ja": "אלא אנהם מאלת בהם נפוסהם אלי חב אלדניא", "en": "except that their souls have inclined them toward love of this world"},
      {"ja": "ואלתזמוא אלשריעה", "en": "they have bound themselves to the Law"},
      {"ja": "וקצדוא אלתזאמהא לינאלוא אלת'ואב מן אללה", "en": "and intended in binding themselves to it to attain the reward from God"},
      {"ja": "ואלת'נא מן אלנאס וכראמתהם פי אלדניא עליהא", "en": "and people's praise and honor in this world by it"},
      {"ja": "והו באב מן אבואב אלריא", "en": "and that is one of the gates of ostentation"},
      {"ja": "והו אלשרך אלכ'פי", "en": "namely the hidden associationism"}
    ]
  },
  {
    "ja": "ואלדרג'ה אלסאדסה, קום קצדוא באעמאלהם ת'ואב אללה פי אלדניא פקט, חבא להא ואית'ארהם ללד'אתהא, מע ג'הלהם בצחהֵ ת'ואב אלאכ'רה ונעימהא.",
    "en": "The sixth degree: a folk who have intended by their acts only the reward of God in this world, out of love for it and preference for its pleasures, along with their ignorance of the validity of the reward and bliss of the next world.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלסאדסה", "en": "The sixth degree"},
      {"ja": "קום קצדוא באעמאלהם ת'ואב אללה פי אלדניא פקט", "en": "a folk who have intended by their acts only the reward of God in this world"},
      {"ja": "חבא להא ואית'ארהם ללד'אתהא", "en": "out of love for it and preference for its pleasures"},
      {"ja": "מע ג'הלהם בצחהֵ ת'ואב אלאכ'רה ונעימהא", "en": "along with their ignorance of the validity of the reward and bliss of the next world"}
    ]
  },
  {
    "ja": "ואלדרג'ה אלסאבעה, קום צח להם ג'מיע מא תקדם ד'כרה, אלא אנהם קצדוא פי טאעתהם ללה רג'א ת'ואב אללה פי אלדניא ואלאכ'רה, וג'הלוא וג'ה אלטאעה ללה לד'אתה, אעני בד'לך אג'לאלא ואכראמא ללה ואעט'אמא למא הו אהלה פקט, וענהם קאלוא אואילנא ע\"ס אל תהיו כעבדים המשמשים את הרב על מנת לקבל פרס אלא היו כעבדים המשמשים את הרב על מנת שלא לקבל פרס, ויהי מורא שמים עליכם.",
    "en": "The seventh degree: a folk for whom the whole of what has gone before has been validly established, except that they intended in their obedience to God the hope of God's reward in this world and the next, and were ignorant of the aspect of obedience to God for His own sake — I mean by that, only awe and reverence for God and magnification of the One who is its rightful object. About them our early ones (peace be upon them) said: \"Do not be like the servants who serve the master on condition of receiving a gift, but be like the servants who serve the master on condition of not receiving a gift; and let the fear of Heaven be upon you\" (m. Avot 1:3).",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלסאבעה", "en": "The seventh degree"},
      {"ja": "קום צח להם ג'מיע מא תקדם ד'כרה", "en": "a folk for whom the whole of what has gone before has been validly established"},
      {"ja": "אלא אנהם קצדוא פי טאעתהם ללה רג'א ת'ואב אללה פי אלדניא ואלאכ'רה", "en": "except that they intended in their obedience to God the hope of God's reward in this world and the next"},
      {"ja": "וג'הלוא וג'ה אלטאעה ללה לד'אתה", "en": "and were ignorant of the aspect of obedience to God for His own sake"},
      {"ja": "אעני בד'לך אג'לאלא ואכראמא ללה", "en": "I mean by that, only awe and reverence for God"},
      {"ja": "ואעט'אמא למא הו אהלה פקט", "en": "and magnification of the One who is its rightful object"},
      {"ja": "וענהם קאלוא אואילנא ע\"ס", "en": "About them our early ones (peace be upon them) said"},
      {"ja": "אל תהיו כעבדים המשמשים את הרב על מנת לקבל פרס", "en": "Do not be like the servants who serve the master on condition of receiving a gift"},
      {"ja": "אלא היו כעבדים המשמשים את הרב על מנת שלא לקבל פרס", "en": "but be like the servants who serve the master on condition of not receiving a gift"},
      {"ja": "ויהי מורא שמים עליכם", "en": "and let the fear of Heaven be upon you"}
    ]
  },
  {
    "ja": "ואלדרג'ה אלת'אמנה, קום צח פי נפוסהם ג'מיע מא תקדם ד'כרה, אלא אנהם אלתזמוא טאעהֵ אללה כ'ופא מן עקאבה פי אלדניא ואלאכ'רה, וקד ביינא קבח הד'ין אלמד'הבין פי מא ד'כרנא.",
    "en": "The eighth degree: a folk in whose souls the whole of what has gone before has been validly established — except that they bound themselves to obedience to God out of fear of His punishment in this world and the next. We have already made clear the ugliness of these two schools in what we have set out.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלת'אמנה", "en": "The eighth degree"},
      {"ja": "קום צח פי נפוסהם ג'מיע מא תקדם ד'כרה", "en": "a folk in whose souls the whole of what has gone before has been validly established"},
      {"ja": "אלא אנהם אלתזמוא טאעהֵ אללה כ'ופא מן עקאבה פי אלדניא ואלאכ'רה", "en": "except that they bound themselves to obedience to God out of fear of His punishment in this world and the next"},
      {"ja": "וקד ביינא קבח הד'ין אלמד'הבין פי מא ד'כרנא", "en": "We have already made clear the ugliness of these two schools in what we have set out"}
    ]
  },
  {
    "ja": "ואלדרג'ה אלתאסעה, קום חקקוא אלשריעה ואיקנוא באלת'ואב ואלעקאב עליהם פי אלדארין",
    "en": "The ninth degree: a folk who verified the Law and were certain of the reward and punishment for them in both houses;",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלתאסעה", "en": "The ninth degree"},
      {"ja": "קום חקקוא אלשריעה", "en": "a folk who verified the Law"},
      {"ja": "ואיקנוא באלת'ואב ואלעקאב עליהם פי אלדארין", "en": "and were certain of the reward and punishment for them in both houses"}
    ]
  }
])

# ── קנה ────────────────────────────────────────────────────────────────────
write("קנה", [
  {
    "ja": "ג'מיעא, וקצדוא טאעהֵ אללה לוג'הה ולמא הו אהלה, גיר אנהם לם יתחפט'וא מן מפסדאת אלטאעאת, פדכ'להם אלפסאד מן חית' לם ישערוא,",
    "en": "they intended obedience to God for His own sake and for the One who is its rightful object — yet they did not guard themselves from the corrupters of obediences, so corruption entered them from where they did not perceive,",
    "isHeader": False,
    "pairs": [
      {"ja": "וקצדוא טאעהֵ אללה לוג'הה", "en": "they intended obedience to God for His own sake"},
      {"ja": "ולמא הו אהלה", "en": "and for the One who is its rightful object"},
      {"ja": "גיר אנהם לם יתחפט'וא מן מפסדאת אלטאעאת", "en": "yet they did not guard themselves from the corrupters of obediences"},
      {"ja": "פדכ'להם אלפסאד מן חית' לם ישערוא", "en": "so corruption entered them from where they did not perceive"}
    ]
  },
  {
    "ja": "נט'יר מא קאל אלחכים זבובי מות יבאיש יביע שמן רוקח, וקאל וחוטא אחד יאבד טובה הרבה,",
    "en": "like the Wise One's saying: \"Dead flies cause the perfumer's ointment to stink and ferment\" (Ecclesiastes 10:1), and his saying: \"But one sinner destroys much good\" (Ecclesiastes 9:18),",
    "isHeader": False,
    "pairs": [
      {"ja": "נט'יר מא קאל אלחכים", "en": "like the Wise One's saying"},
      {"ja": "זבובי מות יבאיש יביע שמן רוקח", "en": "Dead flies cause the perfumer's ointment to stink and ferment"},
      {"ja": "וחוטא אחד יאבד טובה הרבה", "en": "But one sinner destroys much good"}
    ]
  },
  {
    "ja": "וקאל בעץ' אלאפאצ'ל לתלאמיד'ה לי לם יכון לכם ד'נוב לכ'פת עליכם מא הו אשד מן אלד'נוב, פקיל לה ומא הו אשד מן אלד'נוב, קאל אלכבריא ואלעג'ב, כקול אלכתאב תועבת ה' כל גבה לב.",
    "en": "Some of the men of excellence said to his disciples: \"Why are you without sins, that I might fear for you what is harsher than sins?\" It was said to him: \"And what is harsher than sins?\" He said: \"Pride and self-satisfaction\" — as the Book said: \"Every one proud of heart is an abomination to the Lord\" (Proverbs 16:5).",
    "isHeader": False,
    "pairs": [
      {"ja": "וקאל בעץ' אלאפאצ'ל לתלאמיד'ה", "en": "Some of the men of excellence said to his disciples"},
      {"ja": "לי לם יכון לכם ד'נוב", "en": "Why are you without sins"},
      {"ja": "לכ'פת עליכם מא הו אשד מן אלד'נוב", "en": "that I might fear for you what is harsher than sins"},
      {"ja": "פקיל לה ומא הו אשד מן אלד'נוב", "en": "It was said to him: And what is harsher than sins"},
      {"ja": "קאל אלכבריא ואלעג'ב", "en": "He said: Pride and self-satisfaction"},
      {"ja": "כקול אלכתאב", "en": "as the Book said"},
      {"ja": "תועבת ה' כל גבה לב", "en": "Every one proud of heart is an abomination to the Lord"}
    ]
  },
  {
    "ja": "ואלדרג'ה אלעאשרה, קום תחקקוא אלשריעה וג'מיע מא ילזמהם מן אלת'ואב ואלעקאב פי אלדארין, פאנתבהוא מן גפלתהם, פאבצרת קלובהם ואג'באת אללה עליהם לעט'ים נעמתה עליהם ואחסאנה אליהם, פלם יחפלוא לא בת'ואב ולא בעקאב,",
    "en": "The tenth degree: a folk who verified the Law and the whole of what is incumbent on them of reward and punishment in both houses; they awakened from their heedlessness, and their hearts saw what is obligatory for God upon them by reason of the magnitude of His blessing upon them and His beneficence to them. They paid no regard to reward or punishment,",
    "isHeader": False,
    "pairs": [
      {"ja": "ואלדרג'ה אלעאשרה", "en": "The tenth degree"},
      {"ja": "קום תחקקוא אלשריעה", "en": "a folk who verified the Law"},
      {"ja": "וג'מיע מא ילזמהם מן אלת'ואב ואלעקאב פי אלדארין", "en": "and the whole of what is incumbent on them of reward and punishment in both houses"},
      {"ja": "פאנתבהוא מן גפלתהם", "en": "they awakened from their heedlessness"},
      {"ja": "פאבצרת קלובהם", "en": "and their hearts saw"},
      {"ja": "ואג'באת אללה עליהם לעט'ים נעמתה עליהם ואחסאנה אליהם", "en": "what is obligatory for God upon them by reason of the magnitude of His blessing upon them and His beneficence to them"},
      {"ja": "פלם יחפלוא לא בת'ואב ולא בעקאב", "en": "They paid no regard to reward or punishment"}
    ]
  },
  {
    "ja": "בל סארעוא אלי טאעהֵ אללה רבהם אג'לאלא ואעט'אמא ושוקא ואכ'לאצא למערפתהם בה ותמייזהם ענה,",
    "en": "but hastened to the obedience to God their Lord out of awe, reverence, longing, and the purification toward Him of their knowledge of Him and their discrimination from Him,",
    "isHeader": False,
    "pairs": [
      {"ja": "בל סארעוא אלי טאעהֵ אללה רבהם", "en": "but hastened to the obedience to God their Lord"},
      {"ja": "אג'לאלא ואעט'אמא ושוקא", "en": "out of awe, reverence, longing"},
      {"ja": "ואכ'לאצא למערפתהם בה ותמייזהם ענה", "en": "and the purification toward Him of their knowledge of Him and their discrimination from Him"}
    ]
  },
  {
    "ja": "ותלך ארפע דרג'את אהל אלשריעה, והד'ה מרתבהֵ אלאנביא ואלאוליא אלד'ין תבאיעוא ללה ועאהדוה ותאג'רוה ועאקדוה, ווהבוה אנפסהם ואולאדהם ואמואלהם ולד'אתהם,",
    "en": "This is the highest of the degrees of the people of the Law — the rank of the prophets and of the friends of God, those who pledged themselves to God, made covenant with Him, did business with Him, contracted with Him, gave Him their souls, their children, their property, and their pleasures,",
    "isHeader": False,
    "pairs": [
      {"ja": "ותלך ארפע דרג'את אהל אלשריעה", "en": "This is the highest of the degrees of the people of the Law"},
      {"ja": "והד'ה מרתבהֵ אלאנביא ואלאוליא", "en": "the rank of the prophets and of the friends of God"},
      {"ja": "אלד'ין תבאיעוא ללה ועאהדוה ותאג'רוה ועאקדוה", "en": "those who pledged themselves to God, made covenant with Him, did business with Him, contracted with Him"},
      {"ja": "ווהבוה אנפסהם ואולאדהם ואמואלהם ולד'אתהם", "en": "gave Him their souls, their children, their property, and their pleasures"}
    ]
  },
  {
    "ja": "פצדקוא ענד אלאנג'אז למא צ'מנוא לה ען אנפסהם, וענהם יקול אלכתאב אספו לי חסידי כורתי בריתי עלי זבח.",
    "en": "and were found truthful at the time of accomplishing of what they had warranted of themselves to Him. Concerning them the Book says: \"Gather to Me My pious ones, those who have made a covenant with Me by sacrifice\" (Psalms 50:5).",
    "isHeader": False,
    "pairs": [
      {"ja": "פצדקוא ענד אלאנג'אז", "en": "and were found truthful at the time of accomplishing"},
      {"ja": "למא צ'מנוא לה ען אנפסהם", "en": "of what they had warranted of themselves to Him"},
      {"ja": "וענהם יקול אלכתאב", "en": "Concerning them the Book says"},
      {"ja": "אספו לי חסידי כורתי בריתי עלי זבח", "en": "Gather to Me My pious ones, those who have made a covenant with Me by sacrifice"}
    ]
  }
])

# ── קנו ────────────────────────────────────────────────────────────────────
write("קנו", [
  {
    "ja": "ד'כרנא אלמוג'וד עליה אכת'ר ג'מהור אלאמה, ופי ד'כרנא לה מנפעה לנא, וועט' למן אסתרשד,",
    "en": "we have mentioned what is found in most of the people of the community. There is benefit for us in our mentioning it, and a sermon to whoever seeks guidance;",
    "isHeader": False,
    "pairs": [
      {"ja": "ד'כרנא אלמוג'וד עליה אכת'ר ג'מהור אלאמה", "en": "we have mentioned what is found in most of the people of the community"},
      {"ja": "ופי ד'כרנא לה מנפעה לנא", "en": "There is benefit for us in our mentioning it"},
      {"ja": "וועט' למן אסתרשד", "en": "and a sermon to whoever seeks guidance"}
    ]
  },
  {
    "ja": "וד'לך אנה אד'א וג'ד פיהא מנזלה יקרב חט'ה מנהא ערף מא יליהא מן אלמראתב וראם אלארתקא אליהא, ויתביין לה מא בינה ובין אלמרתבה אלעליא מן אלמראתב, פירום אלצעוד אליהא באלתדריג' פיכון ד'לך אסהל עליה.",
    "en": "when one finds among them a station near to his own portion, he comes to know what is adjacent to it of the levels, and aspires to ascend to it; and what is between him and the highest of the levels becomes clear to him, and he aspires to climb to it by gradation, so that this becomes easier for him.",
    "isHeader": False,
    "pairs": [
      {"ja": "אד'א וג'ד פיהא מנזלה יקרב חט'ה מנהא", "en": "when one finds among them a station near to his own portion"},
      {"ja": "ערף מא יליהא מן אלמראתב", "en": "he comes to know what is adjacent to it of the levels"},
      {"ja": "וראם אלארתקא אליהא", "en": "and aspires to ascend to it"},
      {"ja": "ויתביין לה מא בינה ובין אלמרתבה אלעליא", "en": "and what is between him and the highest of the levels becomes clear to him"},
      {"ja": "פירום אלצעוד אליהא באלתדריג'", "en": "and he aspires to climb to it by gradation"},
      {"ja": "פיכון ד'לך אסהל עליה", "en": "so that this becomes easier for him"}
    ]
  },
  {
    "ja": "פצל. ה.",
    "en": "Faṣl 5.",
    "isHeader": True,
    "pairs": []
  },
  {
    "ja": "וקד ינבגי לנא אן נביין וג'ה אלתנביה אלעקלי עלי טריק אלסואל ואלג'ואב אלי אכ'ר אלבאב, למא פי ד'לך מן אלביאן ואלוצ'וח למטלובנא.",
    "en": "It is fitting that we set out the manner of the rational awakening, by the way of question and answer, to the end of the gate — for the sake of explanation and clarity in what we seek.",
    "isHeader": False,
    "pairs": [
      {"ja": "וקד ינבגי לנא אן נביין", "en": "It is fitting that we set out"},
      {"ja": "וג'ה אלתנביה אלעקלי", "en": "the manner of the rational awakening"},
      {"ja": "עלי טריק אלסואל ואלג'ואב אלי אכ'ר אלבאב", "en": "by the way of question and answer, to the end of the gate"},
      {"ja": "למא פי ד'לך מן אלביאן ואלוצ'וח למטלובנא", "en": "for the sake of explanation and clarity in what we seek"}
    ]
  },
  {
    "ja": "פנקול, אן אלתנביה אלעקלי הו אלהאם אללה ללאנסאן בתוסט עקלה אלי מערפתה ואלתמייז ען את'אר חכמתה,",
    "en": "We say: the rational awakening is the inspiration of God to the human being, by means of his intellect, toward the knowledge of Him and discrimination from the traces of His wisdom,",
    "isHeader": False,
    "pairs": [
      {"ja": "אן אלתנביה אלעקלי", "en": "the rational awakening"},
      {"ja": "הו אלהאם אללה ללאנסאן", "en": "is the inspiration of God to the human being"},
      {"ja": "בתוסט עקלה", "en": "by means of his intellect"},
      {"ja": "אלי מערפתה ואלתמייז ען את'אר חכמתה", "en": "toward the knowledge of Him and discrimination from the traces of His wisdom"}
    ]
  },
  {
    "ja": "וד'לך יכון מן אללה תעאלי למן אהתדי בהד'ה אלשריעה ענד אלאנתהא אלי גאיהֵ קוהֵ עקלה וצחהֵ תמייזה, פכאן מתשווקא פי אלוצול אלי רצ'א אללה ואלארתקא פי דרג'את אלפצ'איל אליה, ואפרג קלבה מן המום אלדניא ושואגלהא.",
    "en": "and this comes from God (exalted be He) to the one who has been guided by this Law when he reaches the utmost limit of the strength of his intellect and the validity of his discrimination, such that he longs in attaining to the pleasure of God and ascending in the degrees of the virtues toward Him, and has emptied his heart of the cares of this world and its distractions.",
    "isHeader": False,
    "pairs": [
      {"ja": "וד'לך יכון מן אללה תעאלי", "en": "and this comes from God (exalted be He)"},
      {"ja": "למן אהתדי בהד'ה אלשריעה", "en": "to the one who has been guided by this Law"},
      {"ja": "ענד אלאנתהא אלי גאיהֵ קוהֵ עקלה וצחהֵ תמייזה", "en": "when he reaches the utmost limit of the strength of his intellect and the validity of his discrimination"},
      {"ja": "פכאן מתשווקא פי אלוצול אלי רצ'א אללה", "en": "such that he longs in attaining to the pleasure of God"},
      {"ja": "ואלארתקא פי דרג'את אלפצ'איל אליה", "en": "and ascending in the degrees of the virtues toward Him"},
      {"ja": "ואפרג קלבה מן המום אלדניא ושואגלהא", "en": "and has emptied his heart of the cares of this world and its distractions"}
    ]
  },
  {
    "ja": "ואמא אלאמור אלתי בהא יצל אלאנסאן אלי גרץ' אלתנביה אלעקלי פהי אלתחקק במא גרס אללה פי עקול אלנאטקין, מת'ל אסתחסאן אלצדק ואסתקבאח אלכד'ב, ואית'אר אלעדל, ואלנפור מן אלג'ור, ומכאפאהֵ אהל אלאחסאן באלאחסאן ואלשכר להם, ומכאפאהֵ אהל אלאסאסה באלאסאה ואלד'ם להם, ומסאלמהֵ אלנאס ואלאפצ'אל עליהם, ומואזנהֵ אלנעם באלחמד, ואלחסנאת באלת'ואב, ואלסיאת באלעקאב, ותפאצ'ל ת'ואב עלי ת'ואב, ועקאב עלי עקאב, ואלצפח ען אלמד'נבין ענד צדק תובתהם.",
    "en": "As for the things by which the human being attains to the goal of the rational awakening, they are the realization of what God has planted in the intellects of the speaking beings — such as the appreciation of truthfulness and the abhorring of falsehood, the preference for justice, the repulsion from injustice, the requiting of the beneficent with beneficence and thankfulness to them, the requiting of the maleficent with harm and blame toward them, making peace with people and the bestowal of good upon them, the balancing of blessings with praise, of good deeds with reward, of evil deeds with punishment, of one reward over another, of one punishment over another, and the pardoning of sinners upon the truthfulness of their repentance.",
    "isHeader": False,
    "pairs": [
      {"ja": "ואמא אלאמור אלתי בהא יצל אלאנסאן אלי גרץ' אלתנביה אלעקלי", "en": "As for the things by which the human being attains to the goal of the rational awakening"},
      {"ja": "פהי אלתחקק במא גרס אללה פי עקול אלנאטקין", "en": "they are the realization of what God has planted in the intellects of the speaking beings"},
      {"ja": "מת'ל אסתחסאן אלצדק ואסתקבאח אלכד'ב", "en": "such as the appreciation of truthfulness and the abhorring of falsehood"},
      {"ja": "ואית'אר אלעדל", "en": "the preference for justice"},
      {"ja": "ואלנפור מן אלג'ור", "en": "the repulsion from injustice"},
      {"ja": "ומכאפאהֵ אהל אלאחסאן באלאחסאן ואלשכר להם", "en": "the requiting of the beneficent with beneficence and thankfulness to them"},
      {"ja": "ומכאפאהֵ אהל אלאסאסה באלאסאה ואלד'ם להם", "en": "the requiting of the maleficent with harm and blame toward them"},
      {"ja": "ומסאלמהֵ אלנאס ואלאפצ'אל עליהם", "en": "making peace with people and the bestowal of good upon them"},
      {"ja": "ומואזנהֵ אלנעם באלחמד", "en": "the balancing of blessings with praise"},
      {"ja": "ואלחסנאת באלת'ואב", "en": "of good deeds with reward"},
      {"ja": "ואלסיאת באלעקאב", "en": "of evil deeds with punishment"},
      {"ja": "ותפאצ'ל ת'ואב עלי ת'ואב, ועקאב עלי עקאב", "en": "of one reward over another, of one punishment over another"},
      {"ja": "ואלצפח ען אלמד'נבין ענד צדק תובתהם", "en": "and the pardoning of sinners upon the truthfulness of their repentance"}
    ]
  },
  {
    "ja": "פאד'א צחת הד'ה אלמעארף פי נפס",
    "en": "When these forms of knowledge become valid in the soul of",
    "isHeader": False,
    "pairs": [
      {"ja": "פאד'א צחת הד'ה אלמעארף פי נפס", "en": "When these forms of knowledge become valid in the soul of"}
    ]
  }
])

print("done.")

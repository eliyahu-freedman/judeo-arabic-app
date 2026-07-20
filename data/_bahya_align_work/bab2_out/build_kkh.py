# -*- coding: utf-8 -*-
import json, re, os

segs = [
  {
    "ja": "ענד קראיתך למא נבהתך אליה פי הד'א אלבאב, אנה קליל מן כת'יר ממא תצל אליה בפהמך מן אסראר אלחכמה אד'א אסתכשפת ענהא בנקא לבך וצפא קלבך,",
    "en": "When you read what I have alerted you to in this gate, [know] that it is little out of much that you may attain by your understanding of the secrets of the wisdom, if you uncover them through the purity of your mind and the clarity of your heart.",
    "pairs": [
      {"ja": "ענד קראיתך", "en": "When you read"},
      {"ja": "למא נבהתך אליה", "en": "what I have alerted you to"},
      {"ja": "פי הד'א אלבאב", "en": "in this gate"},
      {"ja": "אנה קליל מן כת'יר", "en": "that it is little out of much"},
      {"ja": "ממא תצל אליה בפהמך", "en": "that you may attain by your understanding"},
      {"ja": "מן אסראר אלחכמה", "en": "of the secrets of the wisdom"},
      {"ja": "אד'א אסתכשפת ענהא", "en": "if you uncover them"},
      {"ja": "בנקא לבך", "en": "through the purity of your mind"},
      {"ja": "וצפא קלבך", "en": "and the clarity of your heart"}
    ]
  },
  {
    "ja": "פאד'א וצלת מן ד'לך אלי אלגאיה אלתי פי טאקתך, פינבגי לך אן תעלם אן ג'מיע מא וקפת עליה מן חכמהֵ אלכ'אלק תעאלי וקדרתה פי הד'א אלעאלם ליס יתג'זא מן קדרתה וחכמתה בשי,",
    "en": "And when you reach of that the utmost extent that is within your capacity, it behooves you to know that all you have apprehended of the wisdom of the Creator (exalted) and His power in this world is no portion at all of His power and His wisdom —",
    "pairs": [
      {"ja": "פאד'א וצלת מן ד'לך", "en": "And when you reach of that"},
      {"ja": "אלי אלגאיה", "en": "the utmost extent"},
      {"ja": "אלתי פי טאקתך", "en": "that is within your capacity"},
      {"ja": "פינבגי לך אן תעלם", "en": "it behooves you to know"},
      {"ja": "אן ג'מיע מא וקפת עליה", "en": "that all you have apprehended"},
      {"ja": "מן חכמהֵ אלכ'אלק תעאלי", "en": "of the wisdom of the Creator (exalted)"},
      {"ja": "וקדרתה פי הד'א אלעאלם", "en": "and His power in this world"},
      {"ja": "ליס יתג'זא מן קדרתה וחכמתה בשי", "en": "is no portion at all of His power and His wisdom"}
    ]
  },
  {
    "ja": "אד' ליס יט'הר אלא מא דעת אליה אלצ'רורה מן אג'ל אלאנסאן פקט, לא חסב אמכאן קדרתה, אד' לא נהאיה להא.",
    "en": "for there appears only what necessity has called for, for the sake of man alone — not according to the scope of His power, since it has no limit.",
    "pairs": [
      {"ja": "אד' ליס יט'הר", "en": "for there appears"},
      {"ja": "אלא מא דעת אליה אלצ'רורה", "en": "only what necessity has called for"},
      {"ja": "מן אג'ל אלאנסאן פקט", "en": "for the sake of man alone"},
      {"ja": "לא חסב אמכאן קדרתה", "en": "not according to the scope of His power"},
      {"ja": "אד' לא נהאיה להא", "en": "since it has no limit"}
    ]
  },
  {
    "ja": "פינבגי אן יכון פי נפסך מן ג'לאלה וכ'ופה ועט'ים קדרתה בחסב ד'לך, לא בקדר מא תפהם מנה פקט,",
    "en": "So let there be in your soul, of His majesty and the fear of Him and the magnitude of His power, according to this — not according to what you understand of Him alone.",
    "pairs": [
      {"ja": "פינבגי אן יכון פי נפסך", "en": "So let there be in your soul"},
      {"ja": "מן ג'לאלה וכ'ופה", "en": "of His majesty and the fear of Him"},
      {"ja": "ועט'ים קדרתה", "en": "and the magnitude of His power"},
      {"ja": "בחסב ד'לך", "en": "according to this"},
      {"ja": "לא בקדר מא תפהם מנה פקט", "en": "not according to what you understand of Him alone"}
    ]
  },
  {
    "ja": "בל מת'ל נפסך פי אלעאלם מת'ל טפל ולד פי מטבק אלמלך, פעני באמרה ואמר לה אלמלך בג'מיע מצאלחה, ולטף בה חתי כבר ועקל, ולא עלם לה בשי אלא באלמטבק ומא פיה,",
    "en": "Rather, your own example in the world is like a child born in the king's dungeon: the king attended to his matter, and commanded for him all of his welfares, and dealt subtly with him until he grew up and reasoned. He has no knowledge of anything but the dungeon and what is in it.",
    "pairs": [
      {"ja": "בל מת'ל נפסך פי אלעאלם", "en": "Rather, your own example in the world"},
      {"ja": "מת'ל טפל ולד פי מטבק אלמלך", "en": "is like a child born in the king's dungeon"},
      {"ja": "פעני באמרה", "en": "the king attended to his matter"},
      {"ja": "ואמר לה אלמלך בג'מיע מצאלחה", "en": "and commanded for him all of his welfares"},
      {"ja": "ולטף בה", "en": "and dealt subtly with him"},
      {"ja": "חתי כבר ועקל", "en": "until he grew up and reasoned"},
      {"ja": "ולא עלם לה בשי", "en": "He has no knowledge of anything"},
      {"ja": "אלא באלמטבק ומא פיה", "en": "but the dungeon and what is in it"}
    ]
  },
  {
    "ja": "וכאן יכ'תלף אליה רסול אלמלך בג'מיע מא יחתאג' אליה מן סראג' וטעאם ושראב ולבאס, וערפה אנה עבד אלמלך, ואן אלמטבק בג'מיע מא יחויה ומא יג'לבה אליה מן אלקות פהו ללמלך,",
    "en": "The king's messenger used to come back and forth to him with all that he needed of lamp and food and drink and clothing; and he made known to him that he is the king's servant, and that the dungeon, with all it contains and with all the food the messenger brings to it, belongs to the king.",
    "pairs": [
      {"ja": "וכאן יכ'תלף אליה רסול אלמלך", "en": "The king's messenger used to come back and forth to him"},
      {"ja": "בג'מיע מא יחתאג' אליה", "en": "with all that he needed"},
      {"ja": "מן סראג' וטעאם ושראב ולבאס", "en": "of lamp and food and drink and clothing"},
      {"ja": "וערפה אנה עבד אלמלך", "en": "and he made known to him that he is the king's servant"},
      {"ja": "ואן אלמטבק", "en": "and that the dungeon"},
      {"ja": "בג'מיע מא יחויה", "en": "with all it contains"},
      {"ja": "ומא יג'לבה אליה מן אלקות", "en": "and with all the food the messenger brings to it"},
      {"ja": "פהו ללמלך", "en": "belongs to the king"}
    ]
  },
  {
    "ja": "ת'ם אלזמה שכרה וחמדה, פקאל סבחאן צאחב הד'א אלמטבק אלד'י ציירני לה עבדא וכ'צני בג'מלהֵ נעמה וג'עלני המה ושגלה.",
    "en": "Then [the messenger] bound him to thanking and praising him; so he said: \"Glory be to the master of this dungeon, who has made me his servant, and singled me out by the whole of his blessings, and made me his concern and his occupation.\"",
    "pairs": [
      {"ja": "ת'ם אלזמה שכרה וחמדה", "en": "Then [the messenger] bound him to thanking and praising him"},
      {"ja": "פקאל סבחאן צאחב הד'א אלמטבק", "en": "so he said: \"Glory be to the master of this dungeon"},
      {"ja": "אלד'י ציירני לה עבדא", "en": "who has made me his servant"},
      {"ja": "וכ'צני בג'מלהֵ נעמה", "en": "and singled me out by the whole of his blessings"},
      {"ja": "וג'עלני המה ושגלה", "en": "and made me his concern and his occupation"}
    ]
  },
  {
    "ja": "פקאל לה אלרסול, למא תקול הכד'א פאנך תכ'טי, אד' ליס הד'א אלמטבק פקט הו מלך אלמלך, פאן פי סעהֵ בלאדה מן אמת'אל הד'א אלמטבק מא לא יחצי כת'רה,",
    "en": "The messenger said to him: \"Why do you speak so? You err! For this dungeon alone is not the kingdom of the king. In the breadth of his lands are dungeons like this — innumerable in multitude.",
    "pairs": [
      {"ja": "פקאל לה אלרסול", "en": "The messenger said to him"},
      {"ja": "למא תקול הכד'א", "en": "Why do you speak so"},
      {"ja": "פאנך תכ'טי", "en": "You err"},
      {"ja": "אד' ליס הד'א אלמטבק פקט הו מלך אלמלך", "en": "For this dungeon alone is not the kingdom of the king"},
      {"ja": "פאן פי סעהֵ בלאדה", "en": "In the breadth of his lands"},
      {"ja": "מן אמת'אל הד'א אלמטבק", "en": "are dungeons like this"},
      {"ja": "מא לא יחצי כת'רה", "en": "innumerable in multitude"}
    ]
  },
  {
    "ja": "וכד'לך ליסת בעבדה אנת וחדך, אד' עבידה אכת'ר מן אן יחוט בהם עדדא.",
    "en": "So too, you are not his servant alone — for his servants are more than can be numbered.",
    "pairs": [
      {"ja": "וכד'לך ליסת בעבדה אנת וחדך", "en": "So too, you are not his servant alone"},
      {"ja": "אד' עבידה אכת'ר", "en": "for his servants are more"},
      {"ja": "מן אן יחוט בהם עדדא", "en": "than can be numbered"}
    ]
  },
  {
    "ja": "וכד'לך מא באשרתה מן נעמתה ופצ'לה לא קדר לה מן נעמתה לגירך, וכד'לך שגלה באמרך לא קדר לה ענד שגלה בסואך.",
    "en": "And likewise: what you have experienced of his blessing and his bounty has no measure compared to his blessing upon others; and likewise his occupation with your matter has no measure compared to his occupation with what is besides you.\"",
    "pairs": [
      {"ja": "וכד'לך מא באשרתה", "en": "And likewise: what you have experienced"},
      {"ja": "מן נעמתה ופצ'לה", "en": "of his blessing and his bounty"},
      {"ja": "לא קדר לה מן נעמתה לגירך", "en": "has no measure compared to his blessing upon others"},
      {"ja": "וכד'לך שגלה באמרך", "en": "and likewise his occupation with your matter"},
      {"ja": "לא קדר לה ענד שגלה בסואך", "en": "has no measure compared to his occupation with what is besides you"}
    ]
  },
  {
    "ja": "פקאל אלצבי אני לא עלם לי במא ד'כרת, אנמא פהמת מן אמר אלמלך חסב מא באשרתה מן מלכה ונעמתה פקט.",
    "en": "The child said: \"I have no knowledge of what you have mentioned. I have understood the matter of the king only according to what I have experienced of his kingship and his blessing — only that.\"",
    "pairs": [
      {"ja": "פקאל אלצבי", "en": "The child said"},
      {"ja": "אני לא עלם לי במא ד'כרת", "en": "I have no knowledge of what you have mentioned"},
      {"ja": "אנמא פהמת מן אמר אלמלך", "en": "I have understood the matter of the king"},
      {"ja": "חסב מא באשרתה", "en": "only according to what I have experienced"},
      {"ja": "מן מלכה ונעמתה פקט", "en": "of his kingship and his blessing"}
    ]
  },
  {
    "ja": "פקאל לה אלרסול, קל סבחאן אלמלך אלעאלי אלד'י לא נהאיה למלכה, ולא גאיה",
    "en": "The messenger said to him: \"Say: Glory be to the exalted King, whose kingdom has no end, and no limit—",
    "pairs": [
      {"ja": "פקאל לה אלרסול", "en": "The messenger said to him"},
      {"ja": "קל סבחאן אלמלך אלעאלי", "en": "Say: Glory be to the exalted King"},
      {"ja": "אלד'י לא נהאיה למלכה", "en": "whose kingdom has no end"},
      {"ja": "ולא גאיה", "en": "and no limit"}
    ]
  }
]

out = {"pages": {"קכה": segs}}
os.makedirs('data/_bahya_align_work/bab2_out', exist_ok=True)
json.dump(out, open('data/_bahya_align_work/bab2_out/קכה.json','w'), ensure_ascii=False, indent=1)
print("wrote", sum(len(s['pairs']) for s in segs), "pairs in", len(segs), "segs")

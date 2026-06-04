import type { Metadata } from "next";
import { ComingSoon } from "../_coming-soon";

export const metadata: Metadata = {
  title: "Yefet ben Eli — coming soon",
  description:
    "The 10th-century Karaite biblical commentaries of Yefet ben Eli, in Judeo-Arabic. Coming soon to the Judeo-Arabic library.",
  alternates: { canonical: "/advanced/yefet-ben-eli" },
};

export default function YefetPage() {
  return (
    <ComingSoon
      author="Yefet ben Eli al-Baṣrī (10th c.)"
      work="Karaite commentaries on the Bible"
      oneLiner="The most prolific Karaite exegete of the 10th century, in his lucid Judeo-Arabic prose. Selections from his commentaries on the Pentateuch, Prophets, and Writings."
      sample="תפסיר יפת בן עלי"
    />
  );
}

import { redirect } from "next/navigation";
import { avotHref } from "../chapters";

// /advanced/rambam-mishnah/avot → redirect to the intro (Eight Chapters)
export default function AvotRoot() {
  redirect(avotHref("intro"));
}

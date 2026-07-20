import { redirect } from "next/navigation";
import { sanhedrinHref } from "../chapters";

export default function SanhedrinRoot() {
  redirect(sanhedrinHref("ch1"));
}

import data from "@/data/cognates.json";
import { CognateCards, type CognateEntry } from "./cards";

type CognateData = {
  _total: number;
  entries: CognateEntry[];
};

export default function CognatesPage() {
  const payload = data as CognateData;
  return <CognateCards entries={payload.entries} />;
}

import data from "@/data/aramaic-cognates.json";
import { AramaicCognateCards, type AramaicCognateEntry } from "./cards";

type AramaicCognateData = {
  _total: number;
  entries: AramaicCognateEntry[];
};

export default function AramaicCognatesPage() {
  const payload = data as AramaicCognateData;
  return <AramaicCognateCards entries={payload.entries} />;
}

import data from "@/data/first-50-ja-words.json";
import { First50Cards, type FirstFiftyEntry } from "./cards";

type FirstFiftyData = {
  _total: number;
  entries: FirstFiftyEntry[];
};

export default function First50Page() {
  const payload = data as FirstFiftyData;
  return <First50Cards entries={payload.entries} />;
}

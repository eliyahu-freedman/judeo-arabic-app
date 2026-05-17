import data from "@/data/alphabet.json";
import { AlphabetUI, type AlphabetData } from "./alphabet";

export default function AlphabetPage() {
  return <AlphabetUI data={data as AlphabetData} />;
}

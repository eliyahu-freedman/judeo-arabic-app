import data from "@/data/tafsir-bereshit-1.json";
import { TafsirReader, type TafsirData } from "./reader";

export default function TafsirPage() {
  return <TafsirReader data={data as TafsirData} />;
}

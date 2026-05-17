import data from "@/data/bahya-hakdamah.json";
import { BahyaReader, type BahyaData } from "./reader";

export default function AdvancedPage() {
  return <BahyaReader data={data as BahyaData} />;
}

import { CharacterAnalysis } from "../../../lib/types/analysis";

interface CharacterResultsProps {
  data: CharacterAnalysis;
}

export function CharacterResults({ data }: CharacterResultsProps) {
  return (
    <div className="space-y-2">
      <h4 className="font-semibold">Key Characters</h4>
      <ul className="list-disc pl-4">
        {data.characters.map((char, i) => (
          <li key={i}>{char.name}: {char.description}</li>
        ))}
      </ul>
    </div>
  );
}

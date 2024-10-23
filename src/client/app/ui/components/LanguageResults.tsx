import { LanguageAnalysis } from "../../../lib/types/analysis";

interface LanguageResultsProps {
  data: LanguageAnalysis;
}

export function LanguageResults({ data }: LanguageResultsProps) {
  return (
    <div className="space-y-2">
      <h4 className="font-semibold">Language Analysis</h4>
      <p>Language Code: {data.language_code}</p>
      <p>Confidence: {data.confidence.toFixed(2)}%</p>
    </div>
  );
}

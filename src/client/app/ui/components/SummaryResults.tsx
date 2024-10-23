import { SummaryAnalysis } from "../../../lib/types/analysis";

interface SummaryResultsProps {
  data: SummaryAnalysis;
}

export function SummaryResults({ data }: SummaryResultsProps) {
  return (
    <div className="space-y-2">
      <h4 className="font-semibold">Summary Analysis</h4>
      <p>Summary: {data.summary}</p>
      <p>Word Count: {data.word_count}</p>
    </div>
  );
}

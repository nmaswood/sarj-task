import { SentimentAnalysis } from "../../../lib/types/analysis";

interface SentimentResultsProps {
  data: SentimentAnalysis;
}

export function SentimentResults({ data }: SentimentResultsProps) {
  return (
    <div className="space-y-2">
      <h4 className="font-semibold">Sentiment Analysis</h4>
      <p>Sentiment Score: {data.sentiment}</p>
      <p>Classification: {data.classification}</p>
    </div>
  );
}

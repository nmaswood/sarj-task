interface AnalysisErrorProps {
  message: string;
}

export function AnalysisError({ message }: AnalysisErrorProps) {
  return (
    <div className="p-4 bg-red-50 border border-red-200 rounded text-red-700">
      {message}
    </div>
  );
}

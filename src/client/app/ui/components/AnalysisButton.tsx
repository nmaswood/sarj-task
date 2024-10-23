interface AnalysisButtonProps {
  onClick: () => void;
  loading: boolean;
  disabled?: boolean;
  children: React.ReactNode;
}

export function AnalysisButton({ onClick, loading, disabled, children }: AnalysisButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={loading || disabled}
      className="w-full sm:w-auto px-4 py-2 bg-blue-500 text-white rounded
        hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed
        flex items-center justify-center gap-2"
    >
      {loading && (
        <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
          <circle 
            className="opacity-25" 
            cx="12" 
            cy="12" 
            r="10" 
            stroke="currentColor" 
            strokeWidth="4"
            fill="none"
          />
          <path 
            className="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
          />
        </svg>
      )}
      {children}
    </button>
  );
}

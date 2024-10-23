export interface AnalysisResponse {
  success: boolean;
  data?: { [key: string]: string };
}

export interface CharacterAnalysis {
  characters: Array<{
    name: string;
    description: string;
  }>;
}

export interface LanguageAnalysis {
  language_code: string;
  confidence: number;
}

export interface SentimentAnalysis {
  sentiment: number;
  classification: string;
}

export interface SummaryAnalysis {
  summary: string;
  word_count: number;
}

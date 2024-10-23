import { AnalysisResponse, CharacterAnalysis, LanguageAnalysis, SentimentAnalysis, SummaryAnalysis } from '../lib/types/analysis';
import { ApiError } from '@/lib/types/error';

const baseUrl = process.env.BASE_URL?.replace(/\/$/, '/api/v1');

async function handleApiError(response: Response) {
  if (!response.ok) {
    const error: ApiError = await response.json();
    throw new Error(error.detail);
  }
}

async function fetchApi<T>(endpoint: string, book_id: string): Promise<AnalysisResponse <T>> {
  try {
    const response = await fetch(`${baseUrl}/${endpoint}?book_id=${book_id}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    });

    await handleApiError(response);

    const data = await response.json();
    return { success: true, ...data };
  } catch {
    throw new Error(`${endpoint} analysis failed`);
  }
}

export const analysisApi = {
  analyzeCharacters: async (book_id: string): Promise<AnalysisResponse<CharacterAnalysis>> => {
    return fetchApi<CharacterAnalysis>('characters', book_id);
  },
  analyzeLanguage: async (book_id: string): Promise<AnalysisResponse<LanguageAnalysis>> => {
    return fetchApi<LanguageAnalysis>('language', book_id);
  },
  analyzeSentiment: async (book_id: string): Promise<AnalysisResponse<SentimentAnalysis>> => {
    console.log("book id", book_id);
    const result = await fetchApi<SentimentAnalysis>('sentiment', book_id);
    console.log("response", result);
    return result;
  },
  analyzeSummary: async (book_id: string): Promise<AnalysisResponse<SummaryAnalysis>> => {
    return fetchApi<SummaryAnalysis>('summary', book_id);
  }
};


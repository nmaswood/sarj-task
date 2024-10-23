import { AnalysisResponse } from '@/lib/types/analysis';
import { ApiError } from '@/lib/types/error';

const baseUrl = process.env.NEXT_PUBLIC_BASE_URL?.replace(/\/$/, '');

async function handleApiError(response: Response) {
  if (!response.ok) {
    const error: ApiError = await response.json();
    throw new Error(error.detail);
  }
}

async function fetchApi(endpoint: string, book_id: string): Promise<AnalysisResponse> {
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
  analyzeCharacters: async (book_id: string): Promise<AnalysisResponse> => {
    return fetchApi('characters', book_id);
  },
  analyzeLanguage: async (book_id: string): Promise<AnalysisResponse> => {
    return fetchApi('language', book_id);
  },
  analyzeSentiment: async (book_id: string): Promise<AnalysisResponse> => {
    console.log("book id", book_id);
    const result = await fetchApi('sentiment', book_id);
    console.log("response", result);
    return result;
  },
  analyzeSummary: async (book_id: string): Promise<AnalysisResponse> => {
    return fetchApi('summary', book_id);
  }
};

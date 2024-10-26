import { Book, SuccessResponse } from '@/lib/types/book';
import { ApiError } from '@/lib/types/error';

const baseUrl = process.env.BASE_URL?.replace(/\/$/, '/api/v1') ||  'https://sarj-task.onrender.com/api/v1';

async function handleApiError(response: Response) {
  if (!response.ok) {
    const error: ApiError = await response.json();
    throw new Error(error.detail);
  }
}

export const bookApi = {
  getBook: async (id: string): Promise<Book> => {
    try {
      console.log("bassss", baseUrl);

      const response = await fetch(`${baseUrl}/book/${id}`);
      await handleApiError(response);
      return await response.json();
    } catch (error) {
      throw new Error(`Failed to fetch book: ${error}`);
    }
  },

  saveBook: async (book: Book): Promise<SuccessResponse> => {
    try {
      const response = await fetch(`${baseUrl}/book`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(book),
      });
      await handleApiError(response);
      return await response.json();
    } catch (error) {
      throw new Error(`Failed to save book: ${error}`);
    }
  },

  getSavedBooks: async (): Promise<Book[]> => {
    try {
      const response = await fetch(`${baseUrl}/books`);
      await handleApiError(response);
      return await response.json();
    } catch (error) {
      throw new Error(`Failed to fetch saved books: ${error}`);
    }
  },
};

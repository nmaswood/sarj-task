// store/useBookStore.ts
import { create } from 'zustand';
import { Book } from '@/lib/types/book';

interface BookStore {
  selectedBook: Book | null;
  setSelectedBook: (book: Book | null) => void;
}

export const useBookStore = create<BookStore>((set) => ({
  selectedBook: null,
  setSelectedBook: (book) => set({ selectedBook: book }),
}));

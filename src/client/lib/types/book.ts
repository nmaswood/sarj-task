export interface Book {
  id: number;
  title: string;
  description: string;
  type: string;
  image: string;
  url: string;
  site_name: string;
  content: string;
}

export interface SuccessResponse {
  message: string;
  status: string;
}

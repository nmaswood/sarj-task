interface ErrorMessageProps {
  message: string;
}

export const ErrorMessage = ({ message }: ErrorMessageProps) => (
  <div className="text-center text-sm text-red-700 bg-gray-400 rounded-lg" role="alert">
    {message}
  </div>
);

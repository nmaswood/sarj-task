# SARJ Task

A web application for fetching, analyzing, and managing Project Gutenberg books with advanced text analysis capabilities.

## 🚀 Features

### Core Functionality
- Search and fetch books using Project Gutenberg IDs
- View book text and metadata
- Save books for future reference
- Browse previously accessed books

### Text Analysis Tools
- Character identification
- Language detection
- Sentiment analysis
- Plot summarization

## 🛠️ Technology Stack

### Frontend
- Next.js 
- Node.js 20.15.0
- Runs on port 3000

### Backend
- FastAPI (Python 3.10)
- Runs on port 8000

## 🏗️ Project Structure

```
src/
├── client/
│   └── NextJS App
└── server/
    └── FastAPI App
```

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/book/{book_id}` | GET | Fetch book by ID |
| `/book` | POST | Save a book |
| `/books` | GET | Get all saved books |
| `/characters` | POST | Analyze book characters |
| `/language` | POST | Detect book language |
| `/sentiment` | POST | Analyze book sentiment |
| `/summary` | POST | Generate book summary |

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js 20.15.0+ (for local development)
- Python 3.10+ (for local development)

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Database Configuration
DB_HOST=
DB_NAME=
DB_USERNAME=
DB_PASSWORD=

# Project Gutenberg URLs
GUTENBERG_CONTENT_URL=
GUTENBERG_METADATA_URL=

# Application Settings
ENV=development
SECRET_KEY=qwerty
HOST=localhost
PORT=8000

# Client Settings
NEXT_PUBLIC_BASE_URL=http://localhost:8000/api/v1
```

### Running with Docker

1. Build and start the containers:
```bash
docker-compose up --build
```

2. Access the applications:
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000

### Local Development

#### Frontend
```bash
cd src/client
npm install
npm run dev
```

#### Backend
```bash
cd src/server
python -m venv venv  "or" python3 -m venv venv
virtualenv venv
source venv/bin/activate "or" source venv/scripts/activate
pip install -r requirements.txt
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

## 📦 Docker Configuration

The project includes three Docker configurations:

1. `src/client/Dockerfile` - Frontend container configuration
2. `src/server/Dockerfile` - Backend container configuration
3. `src/docker-compose.yml` - Container orchestration

## 🔍 Usage

1. Access the web interface at `http://localhost:3000`
2. Enter a Project Gutenberg book ID in the search field
3. View the book's content and metadata
4. Use the analysis tools to:
   - Identify key characters
   - Detect the book's language
   - Analyze sentiment
   - Generate plot summaries
5. Access your saved books through the library view

## 🤝 Contributing

1. Fork the repository (`git clone https://github.com/driiisdev/sarj-task.git`)
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details

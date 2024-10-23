FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install necessary system dependencies and clean up afterwards to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy and install Python dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.__init__:app"]

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

# Expose port 8080 (Cloud Run expects this)
EXPOSE 8080

# Start the app using Uvicorn on the correct port (8080)
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8080"]

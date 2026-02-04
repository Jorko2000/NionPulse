FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy worker code
COPY services/worker /app

RUN pip install --no-cache-dir \
    boto3 \
    redis \
    opentelemetry-api \
    opentelemetry-sdk \
    prometheus-client

CMD ["python", "consumer.py"]

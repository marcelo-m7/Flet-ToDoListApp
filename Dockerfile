FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080 \
    HOST=0.0.0.0

WORKDIR /app

# Install system dependencies needed for building Python packages like cryptography
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir flet==0.27.1 python-dotenv==1.0.1 cryptography==42.0.8

# Copy application source
COPY src ./src

EXPOSE 8080

CMD ["python", "src/main.py"]

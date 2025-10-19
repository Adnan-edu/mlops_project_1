# Use Python 3.12 for prebuilt wheels on amd64
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy project
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -e . \
    && pip install gunicorn

# Expose the Cloud Run port
EXPOSE 8080

# Start the app with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "application:app"]

FROM python:3.11-slim

# Setup environment
ENV POETRY_VERSION=1.7.1 \
    PATH="/root/.local/bin:$PATH" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies & Poetry
RUN apt-get update && apt-get install -y curl build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy poetry config files and install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Copy the rest of your app
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Run app using installed uvicorn
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

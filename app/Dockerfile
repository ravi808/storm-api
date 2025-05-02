# Stage 1: Builder
FROM python:3.11-slim AS builder

# Set environment variables
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set working directory
WORKDIR /app

# Copy only the dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root --only main

# Copy the rest of the application
COPY . .

# Stage 2: Final
FROM python:3.11-slim

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app /app

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

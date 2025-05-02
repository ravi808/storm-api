# # Use an official Python runtime as a base image
# FROM python:3.11-slim as builder

# ENV PYTHONUNBUFFERED 1

# RUN apt-get update &&  \
#     apt-get install -y libpq-dev gcc

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY ./requirements.txt /app

# # Create virtual env
# RUN python -m venv /opt/venv
# # Enable venv
# ENV PATH="/opt/venv/bin:$PATH"

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Run multistage as best practice
# FROM python:3.11-slim as runner
# WORKDIR /app/
# COPY --from=builder /opt/venv /opt/venv

# # Enable venv
# ENV PATH="/opt/venv/bin:$PATH"
# COPY ./ /app/

# ENV PYTHONUNBUFFERED=0
# # Run app.py when the container launches
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]


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

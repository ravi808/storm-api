# 🧠 STORM API — FastAPI Wrapper for Stanford STORM

This project exposes Stanford's **Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking (STORM)** as a clean, modular, production-ready **FastAPI web service**.

It enables querying a topic and getting structured output: outlines, perspectives, and article content — powered by LLMs like GPT-3.5/4 via OpenAI or Litellm.

---

## 🚀 Features

- ✅ RESTful API via FastAPI
- ✅ Versioned endpoint structure (`/api/v1/...`)
- ✅ Modular architecture (pipeline, LM config, routes, utils)
- ✅ No disk I/O — all results are returned in-memory as JSON
- ✅ Dockerized for easy deployment
- ✅ Dependency management via Poetry
- ✅ Logging, exception handling, and clean async design
- ✅ Tested with GPT-3.5 and GPT-4 via `knowledge_storm` package

---

## 📦 Project Structure

```
storm-api/
├── api/v1/           # FastAPI routes and schemas
├── core/             # STORM pipeline orchestration logic
├── config/           # App settings and env management
├── utils/            # Logger, exception handlers
├── tests/            # Pytest unit/integration tests
├── main.py           # App entrypoint
├── Dockerfile        # For container builds
├── pyproject.toml    # Poetry dependency file
├── poetry.lock       # Locked dependencies
└── README.md
```

---

## 🧰 Setup

### 📌 Requirements

- Python 3.11+
- Poetry
- Docker (optional)

---

### 🔧 Local Setup (with Poetry)

1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Clone the repo

```bash
git clone https://github.com/yourname/storm-api.git
cd storm-api
poetry install
```

3. Add your OpenAI/YDC credentials in a `.env` file:

```env
OPENAI_API_KEY=your-openai-api-key
YDC_API_KEY=your-you-com-api-key
```

4. Run the app:

```bash
poetry run uvicorn main:app --reload
```

---

### 🐳 Docker Setup

```bash
docker build -t storm-api .
docker run -p 8000:8000 --env-file .env storm-api
```

---

## 🌐 API Usage

### 🔍 POST `/api/v1/generate-outline`

**Request Body**:

```json
{
  "topic": "Artificial Intelligence"
}
```

**Response**:

```json
{
  "topic": "Artificial Intelligence",
  "outline": {
    "questions": [...],
    "passages": [...],
    "article": "...",
    ...
  }
}
```

### ✅ Health Check

```bash
curl http://localhost:8000/api/v1/healthcheck
```

---

## 🧪 Testing

Run tests with:

```bash
poetry run pytest
```

---

## 🛡 Environment Variables

You can use `.env` or set them directly:

| Variable         | Description                    |
|------------------|--------------------------------|
| `OPENAI_API_KEY` | Required for GPT access        |
| `YDC_API_KEY`    | Required for You.com retrieval |
| `SEARCH_TOP_K`   | Optional, defaults to `5`      |
| `MAX_PERSPECTIVE`| Optional, defaults to `3`      |

---

## 📚 Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Poetry](https://python-poetry.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Knowledge STORM](https://pypi.org/project/knowledge-storm/)
- [OpenAI / Litellm](https://github.com/BerriAI/litellm)

---
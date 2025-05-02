from fastapi import FastAPI
from api.v1.endpoints import router as v1_router

app = FastAPI(
    title="Stanford STORM API",
    version="1.0.0",
    description="Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking"
)

app.include_router(v1_router, prefix="/api")
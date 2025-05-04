from fastapi import FastAPI
from api.v1.endpoints import router as v1_router  # Import the versioned API router

# Initialize FastAPI app with metadata for documentation
app = FastAPI(
    title="Stanford STORM API",  
    version="1.0.0",             # API version
    description="Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking"  # Description shown in docs
)

# Include the version 1 router under the /api path prefix
app.include_router(v1_router, prefix="/api")

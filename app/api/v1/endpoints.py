from fastapi import APIRouter, HTTPException
from models.v1.schemas import TopicInput, TopicResponse
from core.pipeline_manager import storm_pipeline_manager
from utils.logger import setup_logger

router = APIRouter(prefix="/v1", tags=["STORM"])

logger = setup_logger(__name__)


@router.post("/generate-outline", response_model=TopicResponse)
async def generate_outline(payload: TopicInput):
    """
    Generate a structured article outline and synthesized perspective from a topic.

    Args:
        payload (TopicInput): Input topic data from user.

    Returns:
        TopicResponse: JSON result with structured synthesis.
    """
    topic = payload.topic.strip()
    if not topic:
        raise HTTPException(status_code=422, detail="Topic cannot be empty.")
    
    try:
        logger.info(f"Generating outline for topic: {topic}")
        result = storm_pipeline_manager.run_pipeline(topic)
        return {"topic": topic, "outline": result}
    except Exception as e:
        logger.error(f"Pipeline error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

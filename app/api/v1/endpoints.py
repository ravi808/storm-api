from fastapi import APIRouter, HTTPException
from models.v1.schemas import TopicInput, TopicResponse
from core.pipeline_manager import storm_pipeline_manager
from utils.logger import setup_logger

# Create an API router with versioned prefix and tag
router = APIRouter(prefix="/v1", tags=["STORM"])

# Initialize a logger for this module
logger = setup_logger(__name__)


@router.post("/generate-outline", response_model=TopicResponse)
async def generate_outline(payload: TopicInput):
    """
    Endpoint to generate a structured article outline using the STORM pipeline.

    This route processes the provided topic, runs it through the STORM synthesis engine,
    and returns the generated outline and synthesized perspectives.

    Args:
        payload (TopicInput): Input schema containing the topic string.

    Returns:
        TopicResponse: JSON response containing the topic and the generated outline.
    """

    # Clean and validate input topic
    topic = payload.topic.strip()
    if not topic:
        raise HTTPException(
            status_code=422,
            detail="Topic cannot be empty."
        )

    try:
        # Log the received request
        logger.info(f"Generating outline for topic: {topic}")

        # Run the topic through the STORM pipeline
        result = storm_pipeline_manager.run_pipeline(topic)

        return {"topic": topic, "outline": result}

    except Exception as e:
        # Log unexpected errors
        logger.error(f"Pipeline error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while generating the outline. Please try again later."
        )

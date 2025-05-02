from pydantic import BaseModel, Field


class TopicInput(BaseModel):
    """
    Request schema for STORM API input.

    Attributes:
        topic (str): The main subject for which a structured outline/article will be generated.
    """
    topic: str = Field(..., example="Artificial Intelligence", min_length=3, max_length=100)


class TopicResponse(BaseModel):
    """
    Response schema returned after processing a topic through the STORM pipeline.

    Attributes:
        topic (str): The original input topic.
        outline (dict): The generated outline, questions, and possibly the article summary.
    """
    topic: str
    outline: dict

from fastapi import APIRouter
from models.schema import TopicInput
from app.core.pipeline_manager import create_article
from fastapi.responses import JSONResponse

router = APIRouter()

# @router.post("/storm", response_model=OutlineResponse)
# async def synthesize_outline(request: QueryRequest):
#     outline = generate_outline(request.query)
#     return {"query": request.query, "outline": outline}
@router.post("/create-wiki-article/chatgpt35")
def create_wiki_article(topic_input: TopicInput):
    json_contents = create_article.create_article_chatgpt35(topic=topic_input.topic)
    return JSONResponse(content=json_contents)

# @router.post("/create-wiki-article/chatgpt35")
# def create_wiki_article():
#     # topic = input('Topic: ')
#     topic: str = "Narender Modi"
#     json_contents = create_article(topic=topic)
#     print("JSON: ", json_contents)
#     return JSONResponse(content=json_contents)
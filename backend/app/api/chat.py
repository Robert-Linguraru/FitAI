from fastapi import APIRouter
from app.services.rag_service import RagService
from app.models.chat import ChatRequest, ChatResponse

rag_service = RagService()
router = APIRouter(
    prefix="/api",
    tags=["chat"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
) -> ChatResponse:

    response = rag_service.chat(
        request.message,
    )

    return ChatResponse(
        answer=response.answer,
        sources=response.sources,
    )
from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse

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

    return ChatResponse(
        answer=f"You said: {request.message}"
    )
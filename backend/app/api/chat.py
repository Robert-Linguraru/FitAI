from fastapi import APIRouter
from time import perf_counter
from uuid import uuid4
from app.dependencies import rag_service
from app.models.chat import ChatRequest, ChatResponse
from app.services.timing import ChatTiming

router = APIRouter(
    prefix="/api",
    tags=["chat"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
)

def chat(
    request: ChatRequest,
) -> ChatResponse:
    timing = ChatTiming(request_id=str(uuid4()))
    started_at = perf_counter()

    try:
        response = rag_service.chat(
            request.message,
            timing=timing,
        )

        return ChatResponse(
            answer=response.answer,
            sources=response.sources,
        )
    finally:
        timing.log_summary(
            total_duration_ms=(perf_counter() - started_at) * 1000,
        )
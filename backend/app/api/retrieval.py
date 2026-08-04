from fastapi import APIRouter, HTTPException

from app.models.retrieval import (
    RetrievalRequest,
    RetrievalResponse,
)
from app.rag.retriever import WorkoutRetriever


router = APIRouter(
    prefix="/api",
    tags=["retrieval"],
)


@router.post(
    "/retrieve",
    response_model=RetrievalResponse,
)
async def retrieve_workouts(
    request: RetrievalRequest,
) -> RetrievalResponse:
    """Return workouts found through semantic search."""

    try:
        retriever = WorkoutRetriever()

        results = retriever.retrieve(
            query=request.query,
            limit=request.limit,
        )

        return RetrievalResponse(
            query=request.query,
            results=results,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error
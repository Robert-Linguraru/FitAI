from pydantic import BaseModel, Field


class RetrievalResult(BaseModel):
    """A workout returned by semantic search."""

    workout_id: str
    name: str
    goal: str
    difficulty: str
    training_style: str
    document: str
    distance: float


class RetrievalRequest(BaseModel):
    """Request body for testing semantic workout retrieval."""

    query: str = Field(min_length=1)
    limit: int = Field(default=3, ge=1, le=10)


class RetrievalResponse(BaseModel):
    """Response returned by the temporary retrieval endpoint."""

    query: str
    results: list[RetrievalResult]
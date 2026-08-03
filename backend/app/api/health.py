from fastapi import APIRouter


router = APIRouter(
    prefix="/api",
    tags=["health"],
)


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Return the current health status of the FitAI backend."""
    return {
        "status": "ok",
        "service": "fitai-backend",
    }
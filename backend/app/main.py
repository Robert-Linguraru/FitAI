from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import rag_service
from app.api.chat import router as chat_router
from app.api.retrieval import router as retrieval_router
from app.api.health import router as health_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Warm retrieval dependencies before accepting application requests."""

    logger.info("Warming FitAI retrieval service.")
    rag_service.warm_up()
    logger.info("FitAI retrieval service ready.")
    yield


app = FastAPI(
    title="FitAI API",
    description="Backend API for the FitAI AI Personal Fitness Coach.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(retrieval_router)

@app.get("/", tags=["root"])
async def root() -> dict[str, str]:
    """Return basic information about the FitAI backend."""
    return {
        "message": "FitAI API is running.",
        "documentation": "/docs",
    }
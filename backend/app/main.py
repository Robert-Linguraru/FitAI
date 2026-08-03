from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router

from app.api.health import router as health_router



app = FastAPI(
    title="FitAI API",
    description="Backend API for the FitAI AI Personal Fitness Coach.",
    version="0.1.0",
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

@app.get("/", tags=["root"])
async def root() -> dict[str, str]:
    """Return basic information about the FitAI backend."""
    return {
        "message": "FitAI API is running.",
        "documentation": "/docs",
    }
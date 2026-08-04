from __future__ import annotations

import os

import chromadb
from chromadb.api.models.Collection import Collection


DEFAULT_CHROMA_PATH = "/app/chroma_db"
DEFAULT_COLLECTION_NAME = "fitai-workouts"


class ChromaService:
    """Manage the FitAI ChromaDB collection."""

    def __init__(self) -> None:
        chroma_path = os.getenv(
            "CHROMA_PATH",
            DEFAULT_CHROMA_PATH,
        )

        self._client = chromadb.PersistentClient(
            path=chroma_path,
        )

        self._collection = self._client.get_or_create_collection(
            name=DEFAULT_COLLECTION_NAME,
            metadata={
                "description": "Workout plans used by FitAI."
            },
        )
        
    def query(
        self,
        query_embedding: list[float],
        limit: int = 3,
    ) -> dict:
        """Return the closest documents to a query embedding."""

        if not query_embedding:
            raise ValueError(
                "Query embedding cannot be empty."
            )

        if limit < 1:
            raise ValueError(
                "Result limit must be at least 1."
            )

        available_documents = self.count()

        if available_documents == 0:
            raise ValueError(
                "The ChromaDB collection is empty. "
                "Run the ingestion pipeline first."
            )

        result_limit = min(
            limit,
            available_documents,
        )

        return self._collection.query(
            query_embeddings=[query_embedding],
            n_results=result_limit,
            include=[
                "documents",
                "metadatas",
                "distances",
            ],
        )

    @property
    def collection(self) -> Collection:
        """Return the underlying Chroma collection."""

        return self._collection

    def count(self) -> int:
        """Return the number of stored workout documents."""

        return self._collection.count()

    def reset(self) -> None:
        """Delete every document in the collection."""

        existing = self._collection.get()

        ids = existing.get("ids", [])

        if ids:
            self._collection.delete(ids=ids)
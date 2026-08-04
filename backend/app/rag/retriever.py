from app.models.retrieval import RetrievalResult
from app.rag.chroma_service import ChromaService
from app.services.embedding_service import EmbeddingService


class WorkoutRetriever:
    """Retrieve workouts from ChromaDB using semantic similarity."""

    def __init__(
        self,
        embedding_service: EmbeddingService | None = None,
        chroma_service: ChromaService | None = None,
    ) -> None:
        self._embedding_service = (
            embedding_service
            or EmbeddingService()
        )

        self._chroma_service = (
            chroma_service
            or ChromaService()
        )

    def retrieve(
        self,
        query: str,
        limit: int = 3,
    ) -> list[RetrievalResult]:
        """Return the most semantically relevant workout plans."""

        cleaned_query = query.strip()

        if not cleaned_query:
            raise ValueError(
                "Retrieval query cannot be empty."
            )

        query_embedding = (
            self._embedding_service.create_embedding(
                cleaned_query
            )
        )

        raw_results = self._chroma_service.query(
            query_embedding=query_embedding,
            limit=limit,
        )

        ids = raw_results.get("ids", [[]])[0]
        documents = raw_results.get("documents", [[]])[0]
        metadatas = raw_results.get("metadatas", [[]])[0]
        distances = raw_results.get("distances", [[]])[0]

        results: list[RetrievalResult] = []

        for workout_id, document, metadata, distance in zip(
            ids,
            documents,
            metadatas,
            distances,
            strict=True,
        ):
            results.append(
                RetrievalResult(
                    workout_id=workout_id,
                    name=str(metadata["name"]),
                    goal=str(metadata["goal"]),
                    difficulty=str(
                        metadata["difficulty"]
                    ),
                    training_style=str(
                        metadata["training_style"]
                    ),
                    document=document,
                    distance=float(distance),
                )
            )

        return results
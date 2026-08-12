from app.models.retrieval import RetrievalResult
from app.rag.chroma_service import ChromaService
from app.services.embedding_service import EmbeddingService
from app.services.timing import ChatTiming


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

    def warm_up(self) -> None:
        """Warm retrieval dependencies."""

        self._chroma_service.warm_up()

    def retrieve(
        self,
        query: str,
        limit: int = 3,
        timing: ChatTiming | None = None,
    ) -> list[RetrievalResult]:
        """Return the most semantically relevant workout plans."""

        cleaned_query = query.strip()

        if not cleaned_query:
            raise ValueError(
                "Retrieval query cannot be empty."
            )

        if timing is None:
            query_embedding = self._embedding_service.create_embedding(
                cleaned_query
            )
        else:
            with timing.measure("embeddings"):
                query_embedding = self._embedding_service.create_embedding(
                    cleaned_query
                )

        if timing is None:
            raw_results = self._chroma_service.query(
                query_embedding=query_embedding,
                limit=limit,
            )
        else:
            with timing.measure("retrieval"):
                raw_results = self._chroma_service.query(
                    query_embedding=query_embedding,
                    limit=limit,
                )

        ids = raw_results.get("ids", [[]])[0]
        documents = raw_results.get("documents", [[]])[0]
        metadatas = raw_results.get("metadatas", [[]])[0]
        distances = raw_results.get("distances", [[]])[0]

        results: list[RetrievalResult] = []

        if timing is not None:
            timing.retrieved_document_count = len(documents)

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
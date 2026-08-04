import os

from openai import OpenAI


DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"


class EmbeddingService:
    """Generate OpenAI embeddings for text used by FitAI retrieval."""

    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is not configured."
            )

        self._model = os.getenv(
            "OPENAI_EMBEDDING_MODEL",
            DEFAULT_EMBEDDING_MODEL,
        )

        self._client = OpenAI(api_key=api_key)

    def create_embedding(
        self,
        text: str,
    ) -> list[float]:
        """Create one embedding vector for the supplied text."""

        cleaned_text = text.strip()

        if not cleaned_text:
            raise ValueError(
                "Cannot create an embedding for empty text."
            )

        response = self._client.embeddings.create(
            model=self._model,
            input=cleaned_text,
        )

        return response.data[0].embedding

    def create_embeddings(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """Create embedding vectors for several pieces of text."""

        cleaned_texts = [
            text.strip()
            for text in texts
            if text.strip()
        ]

        if not cleaned_texts:
            raise ValueError(
                "At least one non-empty text is required."
            )

        response = self._client.embeddings.create(
            model=self._model,
            input=cleaned_texts,
        )

        ordered_results = sorted(
            response.data,
            key=lambda item: item.index,
        )

        return [
            item.embedding
            for item in ordered_results
        ]
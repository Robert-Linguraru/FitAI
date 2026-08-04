from app.rag.prompt_builder import RagPromptBuilder
from app.rag.retriever import WorkoutRetriever
from app.services.gpt_service import GPTGenerationService


class RagService:
    """Coordinates the complete Retrieval-Augmented Generation pipeline."""

    def __init__(self) -> None:
        self._retriever = WorkoutRetriever()
        self._prompt_builder = RagPromptBuilder()
        self._gpt_service = GPTGenerationService()

    def chat(
        self,
        user_message: str,
    ) -> str:
        """
        Generate a grounded AI response using semantic retrieval.
        """

        retrieved_workouts = self._retriever.retrieve(
            query=user_message,
            limit=3,
        )

        prompt = self._prompt_builder.build(
            user_message=user_message,
            retrieved_workouts=retrieved_workouts,
        )

        return self._gpt_service.generate(prompt)
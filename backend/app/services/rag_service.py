from app.rag.prompt_builder import RagPromptBuilder
from app.rag.retriever import WorkoutRetriever
from app.services.gpt_service import GPTGenerationService
import logging

logger = logging.getLogger(__name__)

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
        if not retrieved_workouts:
            logger.warning(
                "No workouts found for query: %s",
                user_message,
            )

            return (
                "I couldn't find a suitable workout in the current "
                "knowledge base. Try describing your goal, equipment, "
                "or experience level differently."
            )        

        prompt = self._prompt_builder.build(
            user_message=user_message,
            retrieved_workouts=retrieved_workouts,
        )

        try:
            return self._gpt_service.generate(prompt)

        except Exception:
            logger.exception(
                "OpenAI generation failed."
            )

            return (
                "I'm having trouble generating a recommendation right now. "
                "Please try again in a moment."
            )
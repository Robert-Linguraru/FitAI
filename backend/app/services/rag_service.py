from app.rag.prompt_builder import RagPromptBuilder
from app.rag.retriever import WorkoutRetriever
from app.services.gpt_service import GPTGenerationService
from app.services.timing import ChatTiming
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ChatResult:
    """Answer and structured workout provenance for one chat request."""

    answer: str
    sources: list[str]


class RagService:
    """Coordinates the complete Retrieval-Augmented Generation pipeline."""

    def __init__(self) -> None:
        self._retriever = WorkoutRetriever()
        self._prompt_builder = RagPromptBuilder()
        self._gpt_service = GPTGenerationService()

    def chat(
        self,
        user_message: str,
        timing: ChatTiming | None = None,
    ) -> ChatResult:
        """
        Generate a grounded AI response using semantic retrieval.
        """

        
        retrieved_workouts = self._retriever.retrieve(
            query=user_message,
            limit=3,
            timing=timing,
        )
        if not retrieved_workouts:
            logger.warning(
                "No workouts found for query: %s",
                user_message,
            )

            return ChatResult(
                answer=(
                    "I couldn't find a suitable workout in the current "
                    "knowledge base. Try describing your goal, equipment, "
                    "or experience level differently."
                ),
                sources=[],
            )        

        if timing is None:
            prompt = self._prompt_builder.build(
                user_message=user_message,
                retrieved_workouts=retrieved_workouts,
            )
        else:
            with timing.measure("prompt_building"):
                prompt = self._prompt_builder.build(
                    user_message=user_message,
                    retrieved_workouts=retrieved_workouts,
                    timing=timing,
                )

        try:
            if timing is None:
                generation = self._gpt_service.generate(prompt)
            else:
                with timing.measure("generation"):
                    generation = self._gpt_service.generate(
                        prompt,
                        timing=timing,
                    )

            return ChatResult(
                answer=generation.answer,
                sources=generation.sources,
            )

        except Exception:
            logger.exception(
                "OpenAI generation failed."
            )

            return ChatResult(
                answer=(
                    "I'm having trouble generating a recommendation right now. "
                    "Please try again in a moment."
                ),
                sources=[],
            )

    def warm_up(self) -> None:
        """Warm RAG dependencies before serving requests."""

        self._retriever.warm_up()

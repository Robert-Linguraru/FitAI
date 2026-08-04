from openai import OpenAI
import logging

from app.rag.prompt_builder import RagPrompt
logger = logging.getLogger(__name__)

class GPTGenerationService:
    """Generates grounded responses using the OpenAI Responses API."""

    def __init__(self) -> None:
        self._client = OpenAI()

    def generate(
        self,
        prompt: RagPrompt,
    ) -> str:
        """
        Generate a response from a prepared RAG prompt.
        """
        logger.info(
            "Sending request to OpenAI Responses API."
        )
        response = self._client.responses.create(
            model="gpt-5",
            instructions=prompt.instructions,
            input=prompt.model_input,
        )
        logger.info(
            "Received response from OpenAI."
        )

        return response.output_text.strip()
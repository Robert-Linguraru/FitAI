from openai import OpenAI

from app.rag.prompt_builder import RagPrompt


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

        response = self._client.responses.create(
            model="gpt-5",
            instructions=prompt.instructions,
            input=prompt.model_input,
        )

        return response.output_text.strip()
import logging
import json

from openai import OpenAI

from app.tools.workout_tool import WorkoutTool
from app.rag.prompt_builder import RagPrompt

logger = logging.getLogger(__name__)

WORKOUT_TOOL = {
    "type": "function",
    "name": "get_workout_by_name",
    "description":          
        "Retrieve the complete workout plan, including the weekly "
        "schedule, exercises, sets, repetitions, rest times, and "
        "recommendations, using the exact workout name.",
    "parameters": {
        "type": "object",
        "properties": {
            "workout_name": {
                "type": "string",
                "description": "The exact workout name."
            }
        },
        "required": ["workout_name"],
    },
}

class GPTGenerationService:
    """Generates grounded responses using the OpenAI Responses API."""

    def __init__(self) -> None:
        self._client = OpenAI()
        self._workout_tool = WorkoutTool()

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
            tools=[WORKOUT_TOOL],
        )

        logger.info(
            "Received response from OpenAI."
        )

        # Check if GPT requested a tool
        for item in response.output:

            if item.type != "function_call":
                continue

            if item.name != "get_workout_by_name":
                logger.warning(
                    "Unknown tool requested: %s",
                    item.name,
                )

                tool_output = {
                    "error": f"Unknown tool '{item.name}'."
                }

                response = self._client.responses.create(
                    model="gpt-5",
                    previous_response_id=response.id,
                    input=[
                        {
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": json.dumps(tool_output),
                        }
                    ],
                )

                break            

            logger.info(
                "Executing tool: %s",
                item.name,
            )

            try:
                arguments = json.loads(item.arguments)
            except json.JSONDecodeError:
                logger.exception(
                    "Invalid tool arguments."
                )

                tool_output = {
                    "error": "Invalid tool arguments."
                }

                response = self._client.responses.create(
                    model="gpt-5",
                    previous_response_id=response.id,
                    input=[
                        {
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": json.dumps(tool_output),
                        }
                    ],
                )

                break

            workout = self._workout_tool.get_workout_by_name(
                arguments["workout_name"],
            )

            if workout is None:
                tool_output = {
                    "error": (
                        "The requested workout could not be found "
                        "in the FitAI knowledge base."
                    )
                }
            else:
                tool_output = workout.model_dump()

                logger.info(
                    "Tool '%s' executed successfully.",
                    item.name,
                )            

            logger.info(
                "Submitting tool output back to OpenAI."
            )

            response = self._client.responses.create(
                model="gpt-5",
                previous_response_id=response.id,
                input=[
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": json.dumps(tool_output),
                    }
                ],
            )

            break

        logger.info(
            "Returning final AI response."
        )

        return response.output_text.strip()
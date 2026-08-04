from app.models.workout import WorkoutPlan
from app.repositories.workout_repository import WorkoutRepository


class WorkoutTool:
    """Exposes workout operations that may be invoked by the AI."""

    def __init__(self) -> None:
        self._repository = WorkoutRepository()

    def get_workout_by_name(
        self,
        workout_name: str,
    ) -> WorkoutPlan | None:
        """
        Return the complete workout plan for the given name.
        """

        return self._repository.get_by_name(
            workout_name,
        )
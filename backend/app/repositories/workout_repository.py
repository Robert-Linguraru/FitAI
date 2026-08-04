from app.models.workout import WorkoutPlan
from app.services.workout_loader import load_workouts


class WorkoutRepository:
    """Provides query operations over the workout knowledge base."""

    def __init__(self) -> None:
        self._workouts = load_workouts()

    def get_by_name(
        self,
        workout_name: str,
    ) -> WorkoutPlan | None:

        normalized_name = workout_name.casefold()

        for workout in self._workouts:
            if workout.name.casefold() == normalized_name:
                return workout

        return None 
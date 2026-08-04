import json
from pathlib import Path

from pydantic import TypeAdapter, ValidationError

from app.models.workout import WorkoutPlan


WORKOUT_DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "workouts.json"
)

workout_list_adapter = TypeAdapter(list[WorkoutPlan])


def load_workouts(
    data_path: Path = WORKOUT_DATA_PATH,
) -> list[WorkoutPlan]:
    """Load and validate all workout plans from the JSON knowledge base."""

    if not data_path.exists():
        raise FileNotFoundError(
            f"Workout data file was not found: {data_path}"
        )

    try:
        with data_path.open(
            mode="r",
            encoding="utf-8",
        ) as data_file:
            raw_data = json.load(data_file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Workout data contains invalid JSON: {error}"
        ) from error

    try:
        workouts = workout_list_adapter.validate_python(raw_data)
    except ValidationError as error:
        raise ValueError(
            f"Workout data failed validation: {error}"
        ) from error

    workout_ids = [workout.id for workout in workouts]

    if len(workout_ids) != len(set(workout_ids)):
        raise ValueError(
            "Workout data contains duplicate workout IDs."
        )

    workout_names = [
        workout.name.casefold()
        for workout in workouts
    ]

    if len(workout_names) != len(set(workout_names)):
        raise ValueError(
            "Workout data contains duplicate workout names."
        )

    return workouts
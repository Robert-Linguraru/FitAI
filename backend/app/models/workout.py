from pydantic import BaseModel, Field


class Exercise(BaseModel):
    """A single exercise included in a workout session."""

    name: str = Field(min_length=1)
    sets: int = Field(ge=1)
    repetitions: str = Field(min_length=1)
    rest_seconds: int = Field(ge=0)
    notes: str = ""


class WorkoutDay(BaseModel):
    """One scheduled training day containing a group of exercises."""

    day: str = Field(min_length=1)
    focus: str = Field(min_length=1)
    exercises: list[Exercise] = Field(min_length=1)


class WorkoutPlan(BaseModel):
    """A complete workout plan stored in the FitAI knowledge base."""

    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    goal: str = Field(min_length=1)
    difficulty: str = Field(min_length=1)
    equipment: list[str] = Field(min_length=1)
    duration_minutes: int = Field(gt=0)
    training_style: str = Field(min_length=1)
    themes: list[str] = Field(min_length=1)
    weekly_schedule: list[WorkoutDay] = Field(min_length=1)
    recommendations: list[str] = Field(min_length=1)

    def to_searchable_text(self) -> str:
        """Build the text that will later be embedded for semantic search."""

        equipment_text = ", ".join(self.equipment)
        themes_text = ", ".join(self.themes)

        return (
            f"Workout name: {self.name}. "
            f"Summary: {self.summary} "
            f"Goal: {self.goal}. "
            f"Difficulty: {self.difficulty}. "
            f"Equipment: {equipment_text}. "
            f"Duration: {self.duration_minutes} minutes. "
            f"Training style: {self.training_style}. "
            f"Themes: {themes_text}."
        )
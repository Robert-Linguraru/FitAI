import type { Workout } from "../types/workout";

interface WorkoutCardProps {
  workout: Workout;
}

function WorkoutCard({ workout }: WorkoutCardProps) {
  const difficultyClassName = `workout-card--${workout.difficulty.toLowerCase()}`;

  return (
    <section
      className={`workout-card workout-card--enter ${difficultyClassName}`}
      aria-label={workout.name}
    >
      <div className="workout-card-header">
        <div>
          <p className="workout-card-eyebrow">Recommended workout</p>
          <h3>{workout.name}</h3>
        </div>

        <span className="workout-difficulty">
          {workout.difficulty}
        </span>
      </div>

      <div className="workout-details">
        <div className="workout-detail">
          <span className="workout-detail-label">Goal</span>
          <strong>{workout.goal}</strong>
        </div>

        <div className="workout-detail">
          <span className="workout-detail-label">Duration</span>
          <strong>{workout.duration}</strong>
        </div>
      </div>

      <div className="workout-equipment">
        <span className="workout-detail-label">Equipment</span>
        <ul>
          {workout.equipment.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
    </section>
  );
}

export default WorkoutCard;

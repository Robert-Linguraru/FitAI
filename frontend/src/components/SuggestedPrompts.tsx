interface SuggestedPrompt {
  icon: string;
  title: string;
  prompt: string;
}

interface SuggestedPromptsProps {
  onSelectPrompt: (prompt: string) => void;
}

const suggestedPrompts: SuggestedPrompt[] = [
  {
    icon: "🏠",
    title: "Home Workout",
    prompt: "Create a beginner home workout using only bodyweight.",
  },
  {
    icon: "🔥",
    title: "Fat Loss",
    prompt: "Recommend a fat loss workout for someone with 45 minutes.",
  },
  {
    icon: "💪",
    title: "Build Muscle",
    prompt: "Create a muscle-building workout for the gym.",
  },
  {
    icon: "🏃",
    title: "Improve Endurance",
    prompt: "Suggest an endurance-focused workout.",
  },
  {
    icon: "⏱",
    title: "20 Minute Workout",
    prompt: "I only have 20 minutes. What workout do you recommend?",
  },
  {
    icon: "🧘",
    title: "Beginner Routine",
    prompt: "I'm completely new to fitness. Where should I start?",
  },
];

function SuggestedPrompts({
  onSelectPrompt,
}: SuggestedPromptsProps) {
  return (
    <div className="suggested-prompts" aria-label="Suggested prompts">
      {suggestedPrompts.map((suggestedPrompt) => (
        <button
          className="suggested-prompt"
          key={suggestedPrompt.title}
          type="button"
          aria-label={`Use prompt: ${suggestedPrompt.prompt}`}
          onClick={() => onSelectPrompt(suggestedPrompt.prompt)}
        >
          <span className="suggested-prompt-icon" aria-hidden="true">
            {suggestedPrompt.icon}
          </span>

          <span className="suggested-prompt-copy">
            <strong>{suggestedPrompt.title}</strong>
            <span>{suggestedPrompt.prompt}</span>
          </span>
        </button>
      ))}
    </div>
  );
}

export default SuggestedPrompts;

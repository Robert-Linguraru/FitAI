import {
  Activity,
  Clock3,
  Dumbbell,
  Flame,
  Home,
  PersonStanding,
  type LucideIcon,
} from "lucide-react";

type SuggestedPromptIconKey =
  | "home"
  | "fatLoss"
  | "muscle"
  | "endurance"
  | "time"
  | "beginner";

interface SuggestedPrompt {
  icon: SuggestedPromptIconKey;
  title: string;
  prompt: string;
}

const suggestedPromptIcons: Record<
  SuggestedPromptIconKey,
  LucideIcon
> = {
  home: Home,
  fatLoss: Flame,
  muscle: Dumbbell,
  endurance: Activity,
  time: Clock3,
  beginner: PersonStanding,
};

interface SuggestedPromptsProps {
  onSelectPrompt: (prompt: string) => void;
}

const suggestedPrompts: SuggestedPrompt[] = [
  {
    icon: "home",
    title: "Home Workout",
    prompt: "Create a beginner home workout using only bodyweight.",
  },
  {
    icon: "fatLoss",
    title: "Fat Loss",
    prompt: "Recommend a fat loss workout for someone with 45 minutes.",
  },
  {
    icon: "muscle",
    title: "Build Muscle",
    prompt: "Create a muscle-building workout for the gym.",
  },
  {
    icon: "endurance",
    title: "Improve Endurance",
    prompt: "Suggest an endurance-focused workout.",
  },
  {
    icon: "time",
    title: "20 Minute Workout",
    prompt: "I only have 20 minutes. What workout do you recommend?",
  },
  {
    icon: "beginner",
    title: "Beginner Routine",
    prompt: "I'm completely new to fitness. Where should I start?",
  },
];

function SuggestedPrompts({
  onSelectPrompt,
}: SuggestedPromptsProps) {
  return (
    <div className="suggested-prompts" aria-label="Suggested prompts">
      {suggestedPrompts.map((suggestedPrompt) => {
        const PromptIcon = suggestedPromptIcons[
          suggestedPrompt.icon
        ];

        return (
          <button
            className="suggested-prompt"
            key={suggestedPrompt.title}
            type="button"
            aria-label={`Use prompt: ${suggestedPrompt.prompt}`}
            onClick={() => onSelectPrompt(suggestedPrompt.prompt)}
          >
            <span className="suggested-prompt-icon" aria-hidden="true">
              <PromptIcon size={19} strokeWidth={2} />
            </span>

            <span className="suggested-prompt-copy">
              <strong>{suggestedPrompt.title}</strong>
              <span>{suggestedPrompt.prompt}</span>
            </span>
          </button>
        );
      })}
    </div>
  );
}

export default SuggestedPrompts;

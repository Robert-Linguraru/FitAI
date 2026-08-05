import type { ChatMessage as ChatMessageData } from "../types/chatMessage";
import { workouts } from "../data/workouts";
import WorkoutCard from "./WorkoutCard";

interface ChatMessageProps {
  message: ChatMessageData;
}

function ChatMessage({ message }: ChatMessageProps) {
  const isAssistant = message.role === "assistant";
  const recommendedWorkout = isAssistant
    ? workouts.find((workout) =>
        message.content
          .toLocaleLowerCase()
          .includes(workout.name.toLocaleLowerCase()),
      )
    : undefined;

  return (
    <article
      className={`chat-message chat-message--${message.role}`}
    >
      <div className="message-avatar" aria-hidden="true">
        {isAssistant ? "AI" : "You"}
      </div>

      <div className="message-content">
        <p className="message-author">
          {isAssistant ? "FitAI" : "You"}
        </p>

        {recommendedWorkout && (
          <WorkoutCard workout={recommendedWorkout} />
        )}

        <p className="message-text">{message.content}</p>
      </div>
    </article>
  );
}

export default ChatMessage;

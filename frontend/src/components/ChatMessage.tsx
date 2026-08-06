import { useEffect, useState } from "react";
import type { ChatMessage as ChatMessageData } from "../types/chatMessage";
import { workouts } from "../data/workouts";
import WorkoutCard from "./WorkoutCard";

interface ChatMessageProps {
  message: ChatMessageData;
}

function ChatMessage({ message }: ChatMessageProps) {
  const isAssistant = message.role === "assistant";
  const [isEntered, setIsEntered] = useState(!isAssistant);

  useEffect(() => {
    if (!isAssistant) {
      return;
    }

    const animationFrameId = window.requestAnimationFrame(
      () => {
        setIsEntered(true);
      },
    );

    return () => {
      window.cancelAnimationFrame(animationFrameId);
    };
  }, [isAssistant]);

  const recommendedWorkouts = isAssistant
    ? (message.sources ?? [])
        .flatMap((source) => {
          const workout = workouts.find(
            (candidate) =>
              candidate.name.toLocaleLowerCase() ===
              source.toLocaleLowerCase(),
          );

          return workout ? [workout] : [];
        })
        .filter(
          (workout, index, matches) =>
            matches.findIndex(
              (match) => match.id === workout.id,
            ) === index,
        )
    : [];

  return (
    <article
      className={`chat-message chat-message--${message.role}${
        isAssistant && !isEntered
          ? " chat-message--enter"
          : ""
      }`}
    >
      <div className="message-avatar" aria-hidden="true">
        {isAssistant ? "AI" : "You"}
      </div>

      <div className="message-content">
        <p className="message-author">
          {isAssistant ? "FitAI" : "You"}
        </p>

        {recommendedWorkouts.map((workout) => (
          <WorkoutCard key={workout.id} workout={workout} />
        ))}

        <p className="message-text">{message.content}</p>
      </div>
    </article>
  );
}

export default ChatMessage;

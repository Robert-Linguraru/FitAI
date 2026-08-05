import type { ChatMessage as ChatMessageData } from "../types/chatMessage";

interface ChatMessageProps {
  message: ChatMessageData;
}

function ChatMessage({ message }: ChatMessageProps) {
  const isAssistant = message.role === "assistant";

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

        <p className="message-text">{message.content}</p>
      </div>
    </article>
  );
}

export default ChatMessage;

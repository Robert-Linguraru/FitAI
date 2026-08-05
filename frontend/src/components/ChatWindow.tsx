import type { RefObject } from "react";
import type { ChatMessage as ChatMessageData } from "../types/chatMessage";
import ChatMessage from "./ChatMessage";
import LoadingIndicator from "./LoadingIndicator";

interface ChatWindowProps {
  messages: ChatMessageData[];
  isLoading: boolean;
  bottomAnchorRef: RefObject<HTMLDivElement | null>;
}

function ChatWindow({
  messages,
  isLoading,
  bottomAnchorRef,
}: ChatWindowProps) {
  return (
    <div
      className="chat-history"
      role="log"
      aria-live="polite"
      aria-relevant="additions"
    >
      {messages.map((message) => (
        <ChatMessage key={message.id} message={message} />
      ))}

      {isLoading && <LoadingIndicator />}
      <div ref={bottomAnchorRef} aria-hidden="true" />
    </div>
  );
}

export default ChatWindow;

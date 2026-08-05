import {
  useEffect,
  useRef,
  useState,
  type ChangeEvent,
  type FormEvent,
} from "react";
import { sendChat } from "./api/client";
import ChatInput from "./components/ChatInput";
import ChatWindow from "./components/ChatWindow";
import "./App.css";
import type { ChatMessage, ChatRole } from "./types/chatMessage";

function createMessage(
  role: ChatRole,
  content: string,
): ChatMessage {
  return {
    id: `${role}-${Date.now()}-${Math.random()
      .toString(36)
      .slice(2)}`,
    role,
    content,
  };
}

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<ChatMessage[]>(
    [],
  );
  const [isLoading, setIsLoading] = useState(false);
  const isLoadingRef = useRef(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const bottomAnchorRef = useRef<HTMLDivElement>(null);

  const hasConversationStarted = messages.length > 0;

  useEffect(() => {
    bottomAnchorRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "end",
    });
  }, [messages, isLoading]);

  useEffect(() => {
    if (!isLoading && hasConversationStarted) {
      inputRef.current?.focus();
    }
  }, [hasConversationStarted, isLoading]);

  const handleSubmit = async (
    event: FormEvent<HTMLFormElement>,
  ) => {
    event.preventDefault();

    if (isLoadingRef.current) {
      return;
    }

    const trimmedMessage = message.trim();

    if (!trimmedMessage) {
      return;
    }

    isLoadingRef.current = true;
    setIsLoading(true);

    setMessages((currentMessages) => [
      ...currentMessages,
      createMessage("user", trimmedMessage),
    ]);

    setMessage("");

    try {
      const response = await sendChat({
        message: trimmedMessage,
      });

      setMessages((currentMessages) => [
        ...currentMessages,
        createMessage("assistant", response.answer),
      ]);
    } catch (error) {
      console.error(
        "Unable to contact the FitAI backend.",
        error,
      );

      setMessages((currentMessages) => [
        ...currentMessages,
        createMessage(
          "assistant",
          "I couldn't reach the FitAI service.\nPlease make sure the backend is running, then try again.",
        ),
      ]);
    } finally {
      isLoadingRef.current = false;
      setIsLoading(false);
    }
  };

  return (
    <main
      className={
        hasConversationStarted
          ? "app app--chat"
          : "app app--welcome"
      }
    >
      <section className="fitai-card">
        <header className="fitai-header">
          <div className="brand">
            <div className="logo" aria-hidden="true">
              🏋️
            </div>

            <div className="brand-copy">
              <h1>FitAI</h1>
              <p>AI Personal Fitness Coach</p>
            </div>
          </div>

          <div className="status">
            <span
              className="status-dot"
              aria-hidden="true"
            />

            <span>Backend</span>
            <span className="ready">Ready</span>
          </div>
        </header>

        <div
          className="welcome-region"
          aria-hidden={hasConversationStarted}
        >
          <div className="welcome-content">
            <p className="eyebrow">
              Personalized training
            </p>

            <h2>
              Build a workout around your life.
            </h2>

            <p>
              Describe your fitness goals in natural
              language and receive personalized workout
              recommendations powered by FitAI.
            </p>
          </div>
        </div>

        <div
          className="conversation-region"
          aria-hidden={!hasConversationStarted}
        >
          <ChatWindow
            messages={messages}
            isLoading={isLoading}
            bottomAnchorRef={bottomAnchorRef}
          />
        </div>

        <ChatInput
          value={message}
          isLoading={isLoading}
          inputRef={inputRef}
          placeholder={
            hasConversationStarted
              ? "Ask FitAI a follow-up question..."
              : "Tell FitAI about your goals..."
          }
          onChange={(event: ChangeEvent<HTMLInputElement>) =>
            setMessage(event.target.value)
          }
          onSubmit={(event: FormEvent<HTMLFormElement>) =>
            void handleSubmit(event)
          }
        />
      </section>
    </main>
  );
}

export default App;
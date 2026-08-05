import { useState, type FormEvent } from "react";
import { sendChat } from "./api/client";
import "./App.css";

type ChatRole = "user" | "assistant";

interface ChatMessage {
  id: string;
  role: ChatRole;
  content: string;
}

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

  const hasConversationStarted = messages.length > 0;

  const handleSubmit = async (
    event: FormEvent<HTMLFormElement>,
  ) => {
    event.preventDefault();

    const trimmedMessage = message.trim();

    if (!trimmedMessage) {
      return;
    }

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
          "I couldn’t reach the FitAI service. Check that the backend is running, then try again.",
        ),
      ]);
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
          <div
            className="chat-history"
            role="log"
            aria-live="polite"
            aria-relevant="additions"
          >
            {messages.map((chatMessage) => {
              const isAssistant =
                chatMessage.role === "assistant";

              return (
                <article
                  className={
                    `chat-message chat-message--${chatMessage.role}`
                  }
                  key={chatMessage.id}
                >
                  <div
                    className="message-avatar"
                    aria-hidden="true"
                  >
                    {isAssistant ? "AI" : "You"}
                  </div>

                  <div className="message-content">
                    <p className="message-author">
                      {isAssistant ? "FitAI" : "You"}
                    </p>

                    <p className="message-text">
                      {chatMessage.content}
                    </p>
                  </div>
                </article>
              );
            })}
          </div>
        </div>

        <form
          className="chat-form"
          onSubmit={handleSubmit}
        >
          <label
            className="sr-only"
            htmlFor="chat-message"
          >
            Message FitAI
          </label>

          <div className="chat-control">
            <input
              id="chat-message"
              name="message"
              type="text"
              placeholder={
                hasConversationStarted
                  ? "Ask FitAI a follow-up question..."
                  : "Tell FitAI about your goals..."
              }
              value={message}
              onChange={(event) =>
                setMessage(event.target.value)
              }
              autoComplete="off"
            />

            <button type="submit">
              Send
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </form>
      </section>
    </main>
  );
}

export default App;
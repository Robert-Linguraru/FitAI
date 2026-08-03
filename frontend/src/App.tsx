import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    console.log("Message:", message);

    setMessage("");
  };

  return (
    <main className="app">
      <section className="hero-card">

        <div className="logo">
          🏋️
        </div>

        <h1>FitAI</h1>

        <h2>AI Personal Fitness Coach</h2>

        <p>
          Describe your fitness goals in natural language and receive
          personalized workout recommendations powered by
          Retrieval Augmented Generation and OpenAI.
        </p>

        <form
          className="chat-form"
          onSubmit={handleSubmit}
        >
          <input
            type="text"
            placeholder="Tell FitAI about your goals..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />

          <button type="submit">
            Send
          </button>
        </form>

        <div className="status">
          <span className="status-dot"></span>

          Backend Status

          <span className="ready">
            Ready
          </span>
        </div>

      </section>
    </main>
  );
}

export default App;
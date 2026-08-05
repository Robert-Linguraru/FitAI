function LoadingIndicator() {
  return (
    <div
      className="chat-message chat-message--assistant"
      role="status"
      aria-label="FitAI is thinking"
    >
      <div className="message-avatar" aria-hidden="true">
        AI
      </div>

      <div className="message-content">
        <p className="message-author">FitAI</p>
        <p className="message-text">Thinking...</p>
      </div>
    </div>
  );
}

export default LoadingIndicator;

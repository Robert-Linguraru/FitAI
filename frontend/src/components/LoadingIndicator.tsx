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
        <div className="message-skeleton" aria-hidden="true">
          <span className="skeleton-line skeleton-line--title" />
          <span className="skeleton-line skeleton-line--body" />
          <span className="skeleton-line skeleton-line--body" />
          <span className="skeleton-line skeleton-line--body-short" />
        </div>

        <span className="sr-only">FitAI is thinking</span>
      </div>
    </div>
  );
}

export default LoadingIndicator;

import type {
  ChangeEvent,
  FormEvent,
  RefObject,
} from "react";

interface ChatInputProps {
  value: string;
  placeholder: string;
  isLoading: boolean;
  inputRef: RefObject<HTMLInputElement | null>;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  onSubmit: (event: FormEvent<HTMLFormElement>) => void;
}

function ChatInput({
  value,
  placeholder,
  isLoading,
  inputRef,
  onChange,
  onSubmit,
}: ChatInputProps) {
  return (
    <form className="chat-form" onSubmit={onSubmit}>
      <label className="sr-only" htmlFor="chat-message">
        Message FitAI
      </label>

      <div className="chat-control">
        <input
          id="chat-message"
          name="message"
          type="text"
          ref={inputRef}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
          disabled={isLoading}
          autoComplete="off"
        />

        <button type="submit" disabled={isLoading}>
          {isLoading ? "Thinking..." : "Send"}
          <span aria-hidden="true">→</span>
        </button>
      </div>
    </form>
  );
}

export default ChatInput;

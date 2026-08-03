import type {
    ChatRequest,
    ChatResponse,
} from "../types/chat";

const API_URL =
    import.meta.env.VITE_API_URL ??
    "http://localhost:8000";

export async function sendChat(
    request: ChatRequest
): Promise<ChatResponse> {

    const response = await fetch(
        `${API_URL}/api/chat`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify(request),
        }
    );

    if (!response.ok) {
        throw new Error("Failed to contact backend.");
    }

    return response.json();
}
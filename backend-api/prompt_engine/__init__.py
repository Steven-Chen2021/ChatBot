"""Simple prompt construction utilities."""

SYSTEM_PROMPT = "You are a helpful assistant."


def build_prompt(user_input: str) -> str:
    """Combine the system prompt with user input."""
    return f"{SYSTEM_PROMPT}\nUser: {user_input}"

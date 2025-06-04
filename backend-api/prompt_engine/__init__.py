"""Prompt construction utilities used for Gemini requests."""

from __future__ import annotations

from typing import Optional


SYSTEM_PROMPT = "You are a helpful assistant."


def set_system_prompt(text: str) -> None:
    """Override the global system prompt."""
    global SYSTEM_PROMPT
    SYSTEM_PROMPT = text


def build_prompt(user_input: str, *, context: Optional[str] = None) -> str:
    """Combine the system prompt, optional context and user input."""
    sections = [SYSTEM_PROMPT]
    if context:
        sections.append(f"Context:\n{context.strip()}")
    sections.append(f"User: {user_input}")
    return "\n".join(sections)

"""Utilities for processing uploaded files."""

from fastapi import UploadFile


def extract_text(file: UploadFile) -> str:
    """Read file contents as text."""
    content = file.file.read().decode("utf-8", errors="ignore")
    file.file.seek(0)
    return content

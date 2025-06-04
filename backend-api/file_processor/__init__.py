"""Utilities for processing uploaded files.

This module currently supports extracting text from plain text, Markdown and
PDF files. PDF parsing is optional and will gracefully fail if the required
dependency is not installed. All other files are read as UTF-8 text.
"""

from pathlib import Path
from typing import Optional

from fastapi import UploadFile


def _read_as_text(file: UploadFile, encoding: str = "utf-8") -> str:
    """Return file contents decoded as text."""
    content = file.file.read().decode(encoding, errors="ignore")
    file.file.seek(0)
    return content


def _read_pdf(file: UploadFile) -> Optional[str]:
    """Attempt to read a PDF file using PyPDF2 if available."""
    try:
        from PyPDF2 import PdfReader  # type: ignore
    except Exception:
        return None

    try:
        reader = PdfReader(file.file)
        text = "".join(page.extract_text() or "" for page in reader.pages)
    finally:
        file.file.seek(0)
    return text


def extract_text(file: UploadFile) -> str:
    """Extract textual content from an uploaded file."""
    suffix = Path(file.filename or "").suffix.lower()
    if suffix == ".pdf":
        text = _read_pdf(file)
        if text is not None:
            return text
        # fall back to returning an empty string if parsing failed
        return ""

    return _read_as_text(file)

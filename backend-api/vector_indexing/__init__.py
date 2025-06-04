"""Naïve in-memory text index.

This module implements a very small text search facility used by the demo API.
Documents are stored on disk in a JSON file and tokenised using whitespace.  A
trivial scoring algorithm based on word overlap is provided for searching.
"""

from __future__ import annotations

from pathlib import Path
from collections import defaultdict
from typing import Dict, Iterable, List, Tuple

import json

INDEX_FILE = Path(__file__).resolve().parent / "index.json"

if INDEX_FILE.exists():
    data = json.loads(INDEX_FILE.read_text())
    _DOCUMENTS: Dict[str, str] = data.get("docs", {})
    _TOKENS: Dict[str, List[str]] = {
        token: list(names) for token, names in data.get("tokens", {}).items()
    }
else:
    _DOCUMENTS = {}
    _TOKENS = {}


def _tokenise(text: str) -> Iterable[str]:
    for token in text.lower().split():
        cleaned = "".join(c for c in token if c.isalnum())
        if cleaned:
            yield cleaned


def _persist() -> None:
    INDEX_FILE.write_text(
        json.dumps({"docs": _DOCUMENTS, "tokens": _TOKENS}, indent=2)
    )


def add_document(name: str, content: str) -> None:
    """Add a document to the index."""
    _DOCUMENTS[name] = content

    for token in set(_tokenise(content)):
        _TOKENS.setdefault(token, []).append(name)

    _persist()


def search(query: str, *, top_k: int = 5) -> List[Tuple[str, int]]:
    """Return document names ranked by naive token overlap."""
    counts: Dict[str, int] = defaultdict(int)
    query_tokens = list(_tokenise(query))

    for token in query_tokens:
        for name in _TOKENS.get(token, []):
            counts[name] += 1

    ranked = sorted(counts.items(), key=lambda i: i[1], reverse=True)
    return ranked[:top_k]


def get_document(name: str) -> str:
    """Retrieve the raw text of a document."""
    return _DOCUMENTS.get(name, "")

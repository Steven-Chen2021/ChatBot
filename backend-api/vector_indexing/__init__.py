"""Basic in-memory vector index placeholder."""

from pathlib import Path
import json

INDEX_FILE = Path(__file__).resolve().parent / "index.json"

if INDEX_FILE.exists():
    _INDEX = json.loads(INDEX_FILE.read_text())
else:
    _INDEX = {}


def add_document(name: str, content: str) -> None:
    """Store document text in a simple JSON index."""
    _INDEX[name] = content
    INDEX_FILE.write_text(json.dumps(_INDEX, indent=2))

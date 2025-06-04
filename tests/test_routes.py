import importlib
from pathlib import Path
from io import BytesIO
from fastapi import UploadFile

import backend_api.gemini_connector as gc
import backend_api.vector_indexing as vi
import backend_api.routers.admin as admin
import backend_api.routers.chat as chat
import backend_api.routers.status as status


def setup_patches(monkeypatch):
    monkeypatch.setattr(gc, 'query_gemini', lambda p: f'ECHO:{p}')
    monkeypatch.setattr(chat, 'query_gemini', lambda p: f'ECHO:{p}')
    monkeypatch.setattr(vi, 'INDEX_FILE', Path('/tmp/index.json'))
    monkeypatch.setattr(vi, '_DOCUMENTS', {})
    monkeypatch.setattr(vi, '_TOKENS', {})
    monkeypatch.setattr(vi, '_persist', lambda: None)
    monkeypatch.setattr(admin, 'extract_text', lambda f: 'txt')
    monkeypatch.setattr(admin, 'add_document', lambda n, c: None)


def test_status(monkeypatch):
    setup_patches(monkeypatch)
    assert status.status() == {'status': 'ok'}


def test_chat(monkeypatch):
    setup_patches(monkeypatch)
    response = chat.chat(chat.ChatRequest(message='hi'))
    assert response.response.startswith('ECHO:')


def test_upload(monkeypatch):
    setup_patches(monkeypatch)
    file = UploadFile(filename='t.txt', file=BytesIO(b'data'))
    result = admin.upload_file(file)
    assert result['status'] == 'uploaded'
    assert result['filename'] == 't.txt'

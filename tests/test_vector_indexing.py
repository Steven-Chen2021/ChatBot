import importlib

vi = importlib.import_module('backend_api.vector_indexing')


def test_add_search(tmp_path, monkeypatch):
    monkeypatch.setattr(vi, 'INDEX_FILE', tmp_path / 'index.json')
    monkeypatch.setattr(vi, '_DOCUMENTS', {})
    monkeypatch.setattr(vi, '_TOKENS', {})
    monkeypatch.setattr(vi, '_persist', lambda: None)

    vi.add_document('doc1', 'hello world')
    assert vi.get_document('doc1') == 'hello world'

    results = vi.search('hello')
    assert ('doc1', 1) in results

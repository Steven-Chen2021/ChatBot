import importlib
from fastapi import UploadFile
from io import BytesIO

fp = importlib.import_module('backend_api.file_processor')


def make_upload(name: str, data: bytes) -> UploadFile:
    return UploadFile(filename=name, file=BytesIO(data))


def test_extract_text_plain():
    f = make_upload('sample.txt', b'hello')
    assert fp.extract_text(f) == 'hello'


def test_extract_text_pdf_without_pypdf():
    f = make_upload('sample.pdf', b'%PDF-1.4')
    assert fp.extract_text(f) == ''

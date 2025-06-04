from fastapi import APIRouter, UploadFile, File

from ..file_processor import extract_text
from ..vector_indexing import add_document

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    """Upload a text file and index its contents."""
    content = extract_text(file)
    add_document(file.filename, content)
    return {"status": "uploaded", "filename": file.filename}

from fastapi import APIRouter

router = APIRouter(prefix='/admin')

@router.post('/upload')
def upload_file():
    return {"status": "uploaded"}
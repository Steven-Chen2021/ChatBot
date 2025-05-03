from fastapi import APIRouter

router = APIRouter(prefix='/status')

@router.get('/')
def status():
    return {"status": "ok"}
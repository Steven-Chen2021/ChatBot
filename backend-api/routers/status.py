from fastapi import APIRouter

router = APIRouter(prefix="/status", tags=["status"])


@router.get("/")
def status():
    """Return service status."""
    return {"status": "ok"}

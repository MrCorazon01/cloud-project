from fastapi import APIRouter

router = APIRouter()

@router.get("/health/ready")
def readiness():
    return {"status": "ready"}

@router.get("/health/live")
def liveness():
    return {"status": "alive"}
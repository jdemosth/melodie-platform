from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "ok"}


@router.get("/ping")
def ping_call():
    return {"Message": "pong!"}

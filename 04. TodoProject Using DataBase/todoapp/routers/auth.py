from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_user():
    return {"user": "authenticated"}
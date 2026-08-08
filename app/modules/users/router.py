from fastapi import APIRouter, HTTPException
from app.modules.users.schemas import UserCreate, UserResponse
from app.modules.users.service import user_service

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    return user_service.create_user(user)


        
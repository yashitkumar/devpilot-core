from fastapi import APIRouter
from app.modules.auth.schemas import LoginRequest, LoginResponse
from app.modules.auth.service import auth_service

router = APIRouter()

@router.post("/auth/login", response_model = LoginResponse)
async def login(user: LoginRequest):
    return auth_service.login(user)


        
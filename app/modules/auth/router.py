from fastapi import APIRouter, Depends
from app.modules.auth.schemas import LoginRequest, LoginResponse
from app.modules.auth.service import AuthService
from app.modules.auth.dependencies import get_auth_service

router = APIRouter()

@router.post("/auth/login", response_model = LoginResponse)
async def login(
    user: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    return auth_service.login(user)


        
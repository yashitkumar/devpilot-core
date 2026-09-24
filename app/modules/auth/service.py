from app.modules.users.repository import UserRepository
from app.modules.auth.schemas import LoginRequest
from app.core.security import verify_password
from app.modules.users.models import User
from app.modules.auth.exceptions import InvalidCredentialsError
from app.core.security import create_access_token

class AuthService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def login(self, login_request: LoginRequest) -> dict[str, str]:
        existing_user = self._repository.get_by_email(login_request.email)
        if not existing_user:
            raise InvalidCredentialsError("Invalid email or password")

        if not verify_password(login_request.password, existing_user.password_hash):
            raise InvalidCredentialsError("Invalid email or password")

        access_token = create_access_token(str(existing_user.id))

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

# auth_service = AuthService(user_repository)        
    

from app.core.security import hash_password
from app.modules.users.exceptions import UserAlreadyExistsError
from app.modules.users.repository import UserRepository
from app.modules.users.models import User
from uuid import uuid4
from datetime import UTC, datetime
from app.modules.users.schemas import UserCreate

class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def create_user(self, user_create: UserCreate) -> User:
        existing_user = self._repository.get_by_email(user_create.email)

        if existing_user:
            raise UserAlreadyExistsError("User already exists")

        user_id = uuid4()  # Generate a new UUID
        now = datetime.now(UTC)
        user = User(
            id=user_id,
            name=user_create.name,
            email=user_create.email,
            password_hash=hash_password(user_create.password),
            created_at=now,
            updated_at=now,
        )
        return self._repository.create(user)

# user_service = UserService(user_repository)        


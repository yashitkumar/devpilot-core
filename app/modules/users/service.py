
import bcrypt
from app.modules.users.exceptions import UserAlreadyExistsError
from app.modules.users.repository import UserRepository, user_repository
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
            password_hash=self.hash_password(user_create.password),
            created_at=now,
            updated_at=now,
        )
        return self._repository.create(user)

    def hash_password(self, password: str) -> str:
            bcrypt_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            return bcrypt_hash.decode('utf-8')

user_service = UserService(user_repository)        


from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.users.repository import UserRepository
from app.modules.users.service import UserService
from app.modules.auth.service import AuthService


def get_user_repository(
        db: Session = Depends(get_db)
) -> UserRepository:
    return UserRepository(db)

def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repository)
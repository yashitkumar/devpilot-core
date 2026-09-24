from fastapi.security import OAuth2PasswordBearer
from uuid import UUID
from fastapi import Depends
from app.core.security import decode_access_token
from app.modules.users.repository import UserRepository
from app.modules.users.models import User
from app.modules.auth.exceptions import InvalidTokenError
from sqlalchemy.orm import Session
from app.core.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login") 

def get_current_user(
    token: str = Depends(oauth2_scheme), #depends on the oauth2_scheme to extract the token from the request
    db: Session = Depends(get_db),
) -> User:
    user_id = decode_access_token(token) #returns user_id as string
    repository = UserRepository(db)

    user = repository.get_by_id(UUID(user_id))

    if not user:
        raise InvalidTokenError("User not found")

    return user
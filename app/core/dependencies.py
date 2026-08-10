from fastapi.security import OAuth2PasswordBearer
from uuid import UUID
from fastapi import Depends
from app.core.security import decode_access_token
from app.modules.users.repository import user_repository
from app.modules.users.models import User
from app.modules.auth.exceptions import InvalidTokenError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login") 

def get_current_user(token: str = Depends(oauth2_scheme),) -> User: #depends on the oauth2_scheme to extract the token from the request
    user_id = decode_access_token(token) #returns user_id as string

    user = user_repository.get_by_id(UUID(user_id))

    if not user:
        raise InvalidTokenError("User not found")

    return user

from datetime import UTC, datetime, timedelta
import jwt
from app.core.config import settings
import bcrypt
from app.modules.auth.exceptions import InvalidTokenError
from jwt.exceptions import InvalidTokenError as JWTInvalidTokenError

def hash_password(password: str) -> str:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(user_id: str) -> str:
        expires_at = datetime.now(UTC) + timedelta(minutes=30) 

        payload = {
                "sub": user_id,
                "exp": expires_at
        }

        return jwt.encode(
                payload,
                settings.jwt_secret_key,
                algorithm="HS256"
        )

def decode_access_token(token: str) -> str:
        # If the token is expired, jwt.decode() will raise ExpiredSignatureError
        try:
            decoded_token = jwt.decode( 
                    token, 
                    settings.jwt_secret_key, 
                    algorithms=["HS256"])
            
            user_id = decoded_token.get("sub")

            if not user_id:
                    raise InvalidTokenError("Token is invalid")
            return user_id
        
        except JWTInvalidTokenError:
            raise InvalidTokenError("Token is invalid")
                

        
        
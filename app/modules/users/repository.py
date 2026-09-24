from uuid import UUID
from app.modules.users.models import User
from sqlalchemy.orm import Session
from sqlalchemy import select


class UserRepository:

    def __init__(self, db: Session):
        # self._users: dict[UUID, User] = {}
        self._db = db    

    def create(self, user: User) -> User:
        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)
        return user

    def get_by_id(self, user_id: UUID) -> User | None:
        return self._db.get(User, user_id)

    def get_by_email(self, email: str) -> User | None:  
        statement = select(User).where(User.email == email)
        return self._db.scalars(statement).first()

    def get_all(self) -> list[User]:
       statement = select(User)
       return list(self._db.scalars(statement).all())

    def delete(self, user_id: UUID) -> bool:
        user = self._db.get(User, user_id)

        if not user:
            return False

        self._db.delete(user)
        self._db.commit()

        return True 

# user_repository = UserRepository()      

 
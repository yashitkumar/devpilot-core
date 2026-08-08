from uuid import UUID
from app.modules.users.models import User


class UserRepository:

    def __init__(self):
        self._users: dict[UUID, User] = {}

    def create(self, user: User) -> User:
        self._users[user.id] = user
        return user

    def get_by_id(self, user_id: UUID) -> User | None:
        return self._users.get(user_id)

    def get_by_email(self, email: str) -> User | None:  
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def get_all(self) -> list[User]:
       return list(self._users.values())

    def delete(self, user_id: UUID) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False    

user_repository = UserRepository()      

 
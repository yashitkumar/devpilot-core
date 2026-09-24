from uuid import UUID

import pytest

from app.modules.users.exceptions import UserAlreadyExistsError
from app.modules.users.schemas import UserCreate
from app.modules.users.service import UserService


class FakeUserRepository:
    def __init__(self):
        self.users = {}

    def get_by_email(self, email: str):
        return next(
            (user for user in self.users.values() if user.email == email),
            None,
        )

    def create(self, user):
        self.users[user.id] = user
        return user
        
 
def test_create_user():
    repository = FakeUserRepository()
    service = UserService(repository)

    request = UserCreate(
        name="Yashit",
        email="yashit@example.com",
        password="Password123",
    )

    user = service.create_user(request)

    assert user.name == "Yashit"
    assert user.email == "yashit@example.com"
    assert user.password_hash != "Password123"
    assert len(repository.users) == 1        



def test_create_user_with_existing_email_raises_error():
    repository = FakeUserRepository()
    service = UserService(repository)

    request = UserCreate(
        name="Yashit",
        email="yashit@example.com",
        password="Password123",
    )

    service.create_user(request)

    with pytest.raises(UserAlreadyExistsError):
        service.create_user(request)    
from app.core.database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.core.config import settings
import pytest
from app.modules.users.models import User

test_engine = create_engine(settings.test_database_url)

TestSessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    autocommit=False,
)

Base.metadata.create_all(bind=test_engine)


@pytest.fixture
def db():
    session = TestSessionLocal()

    try:
        yield session
    finally:
        session.rollback()
        session.close()
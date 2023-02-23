import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from app.models import Base
from app.main import get_db


TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///test_simple_twitter.sqlite3"
test_engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="function", autouse=True)
def db() -> Session:
    try:
        db_session = TestingSessionLocal()
        Base.metadata.create_all(bind=test_engine)
        yield db_session
    finally:
        db_session.close()
        # Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function", autouse=True)
def client(db: Session):
    from app.main import app
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as client:
        yield client

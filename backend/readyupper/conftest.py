import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .database import DATABASE_SETTINGS, database_url, Base
from .main import app, get_db


@pytest.fixture(scope="session")
def engine():
    # Create the test engine.
    TEST_DATABASE_SETTINGS = DATABASE_SETTINGS.copy()
    TEST_DATABASE_SETTINGS["NAME"] = "test_" + DATABASE_SETTINGS["NAME"]
    TEST_DATABASE_URL = database_url(**TEST_DATABASE_SETTINGS)

    test_engine = create_engine(TEST_DATABASE_URL)

    # Create tables.
    Base.metadata.create_all(test_engine)

    yield test_engine

    # Drop tables.
    Base.metadata.drop_all(test_engine)


@pytest.fixture(scope="session")
def TestSession(engine):
    return sessionmaker(bind=engine)


@pytest.fixture
def db(TestSession):
    session = TestSession()
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def test_client(db, mocker):
    def get_test_db():
        yield db

    app.dependency_overrides[get_db] = get_test_db

    return TestClient(app)

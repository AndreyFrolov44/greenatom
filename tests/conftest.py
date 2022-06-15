import pytest
import os

from sqlalchemy_utils import drop_database, database_exists, create_database
from alembic.config import Config, command
from fastapi.testclient import TestClient


os.environ["TESTING"] = 'True'

from db.base import TEST_SQLALCHEMY_DATABASE_URL
from main import app


@pytest.fixture(autouse=True, scope="session")
def test_app():
    if not database_exists(TEST_SQLALCHEMY_DATABASE_URL):
        create_database(TEST_SQLALCHEMY_DATABASE_URL)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))
    command.upgrade(alembic_cfg, "head")

    try:
        yield TEST_SQLALCHEMY_DATABASE_URL
    finally:
        drop_database(TEST_SQLALCHEMY_DATABASE_URL)


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

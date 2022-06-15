import os

import databases
import sqlalchemy

from sqlalchemy import create_engine

from core.config import settings

TESTING = os.environ.get("TESTING")

if TESTING:
    TEST_SQLALCHEMY_DATABASE_URL = (
        f'postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/test_database'
    )
    database = databases.Database(TEST_SQLALCHEMY_DATABASE_URL)
    engine = create_engine(
        TEST_SQLALCHEMY_DATABASE_URL
    )
else:
    SQLALCHEMY_DATABASE_URL = (
        f'postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}'
    )
    database = databases.Database(SQLALCHEMY_DATABASE_URL)
    engine = create_engine(
        f'postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}'
    )

metadata = sqlalchemy.MetaData()

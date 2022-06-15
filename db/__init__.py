from sqlalchemy_utils import database_exists, create_database

from .inbox import inbox
from .request import request
from .user import user
from .base import engine, metadata, database

if not database_exists(str(database.url)):
    create_database(str(database.url))

metadata.create_all(bind=engine)

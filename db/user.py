from sqlalchemy import Table, Column, Integer, String

from .base import metadata


user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String, unique=True, nullable=False),
    Column("password_hash", String, nullable=False),
)
from sqlalchemy import Table, Column, Integer

from .base import metadata


request = Table(
    "requests",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
)
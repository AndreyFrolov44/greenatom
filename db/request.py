from sqlalchemy import Table, Column, Integer, ForeignKey

from .base import metadata


request = Table(
    "requests",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, ForeignKey('users.id', ondelete="CASCADE"), index=True, nullable=False)
)

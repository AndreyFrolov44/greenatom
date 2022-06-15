from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from .base import metadata


inbox = Table(
    "inboxes",
    metadata,
    Column("request_code", Integer, ForeignKey('requests.id', ondelete="CASCADE"), index=True, nullable=False),
    Column("file_name", String, unique=True, nullable=False),
    Column("datetime", DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column("id", Integer, primary_key=True, index=True),
)



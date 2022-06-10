from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .base import metadata


inbox = Table(
    "inboxes",
    metadata,
    Column("request_code", Integer, primary_key=True, index=True),
    Column("file_name", String, unique=True),
    Column("datetime", DateTime(timezone=True), server_default=func.now())
)

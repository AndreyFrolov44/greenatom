from fastapi import Depends

from services.inbox import InboxService
from services.request import RequestService
from db.base import database


def get_inbox_service() -> InboxService:
    return InboxService(database=database)


def get_request_service() -> RequestService:
    return RequestService(database=database)
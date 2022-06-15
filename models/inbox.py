import datetime

from typing import Optional
from pydantic import BaseModel


class Inbox(BaseModel):
    request_code: int
    file_name: str
    datetime: datetime.datetime
    id: Optional[int]

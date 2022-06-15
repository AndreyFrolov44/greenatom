from typing import Optional

from pydantic import BaseModel


class Request(BaseModel):
    id: Optional[int]

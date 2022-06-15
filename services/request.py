from typing import List, Optional

from .base import BaseService
from db.request import request
from models.request import Request
from models.user import User


class RequestService(BaseService):

    async def create(self, user: User) -> Request:
        req = Request(
            user_id=user.id
        )

        values = {**req.dict()}
        values.pop("id", None)
        query = request.insert().values(**values)
        req.id = await self.database.execute(query)

        return req

    async def get_by_id(self, code_id: int) -> Optional[Request]:
        query = request.select().where(request.c.id == code_id)
        req = await self.database.fetch_one(query)
        if not req:
            return None
        return Request.parse_obj(req)

    async def delete(self, code_id: int):
        query = request.delete().where(request.c.id == code_id)
        await self.database.execute(query)

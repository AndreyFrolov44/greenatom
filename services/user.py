from typing import Optional
from fastapi import HTTPException, status

from models.user import User, UserIn, UserCreate
from db.user import user
from .base import BaseService
from core.security import get_password_hash


class UserService(BaseService):
    async def get_by_username(self, username: str) -> Optional[UserCreate]:
        query = user.select().where(user.c.username == username)
        usr = await self.database.fetch_one(query)
        if usr is None:
            return None
        return UserCreate.parse_obj(usr)

    async def create(self, usr: UserIn) -> Optional[User]:
        username_exist = await self.get_by_username(usr.username)
        if username_exist:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Данный username уже используется")
        if usr.password != usr.password2:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пароли не совпадают")
        create_user = UserCreate(
            username=usr.username,
            password_hash=get_password_hash(usr.password)
        )
        values = {**create_user.dict()}
        values.pop("id", None)
        query = user.insert().values(**values)
        create_user.id = await self.database.execute(query)
        return User(**create_user.dict())

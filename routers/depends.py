from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from services.inbox import InboxService
from services.request import RequestService
from services.user import UserService
from db.base import database
from core.config import settings
from models.user import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/")


def get_user_service() -> UserService:
    return UserService(database=database)


def get_inbox_service() -> InboxService:
    return InboxService(database=database)


def get_request_service() -> RequestService:
    return RequestService(database=database)


async def get_current_user(
        users: UserService = Depends(get_user_service),
        token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверные данные авторизации",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await users.get_by_username(username=username)
    if user is None:
        raise credentials_exception
    return user

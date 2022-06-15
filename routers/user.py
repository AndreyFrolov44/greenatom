from fastapi import APIRouter, Depends

from models.user import UserIn, User
from services.user import UserService
from .depends import get_user_service

router = APIRouter(tags=['user'])


@router.post("/", response_model=User)
async def register(
        userIn: UserIn,
        users: UserService = Depends(get_user_service)
):
    return await users.create(userIn)

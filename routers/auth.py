from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.token import Token, Login
from services.user import UserService
from core.security import verify_password, create_access_token
from .depends import get_user_service

router = APIRouter(tags=['auth'])


@router.post("/", response_model=Token)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        users: UserService = Depends(get_user_service)
):
    user = await users.get_by_username(form_data.username)
    if user is None or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный email или пароль")
    return Token(
        access_token=create_access_token({"sub": user.username}),
        token_type="Bearer"
    )
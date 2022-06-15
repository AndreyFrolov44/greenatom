from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class UserCreate(BaseModel):
    id: Optional[int]
    username: str
    password_hash: str


class UserIn(BaseModel):
    username: str
    password: str
    password2: str

from fastapi import APIRouter

from . import inbox, user, auth

router = APIRouter()
router.include_router(inbox.router, prefix='/frames')
router.include_router(user.router, prefix='/user')
router.include_router(auth.router, prefix='/login')

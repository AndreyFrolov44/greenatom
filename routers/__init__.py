from fastapi import APIRouter

from . import inbox

router = APIRouter()
router.include_router(inbox.router, prefix='/frames')

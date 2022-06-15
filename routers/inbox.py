from typing import List
from fastapi import APIRouter, File, UploadFile, Depends

from services.inbox import InboxService
from services.request import RequestService
from .depends import get_inbox_service, get_request_service
from models.inbox import Inbox


router = APIRouter(tags=['inbox'])


@router.post("/", response_model=List[Inbox])
async def create_file(
        inboxes: InboxService = Depends(get_inbox_service),
        requests: RequestService = Depends(get_request_service),
        files_list: List[UploadFile] = File(...)
):
    return await inboxes.create(files_list, requests)


@router.get("/{request_code}", response_model=List[Inbox])
async def get_file(
        request_code: int,
        inboxes: InboxService = Depends(get_inbox_service),
):
    return await inboxes.get_by_request_code(request_code)


@router.delete("/{request_code}")
async def delete_file(
        request_code: int,
        inboxes: InboxService = Depends(get_inbox_service),
        requests: RequestService = Depends(get_request_service),
):
    return await inboxes.delete(request_code, requests)

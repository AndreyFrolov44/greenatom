import datetime
import uuid

from typing import List
from fastapi import UploadFile, HTTPException, status, Response
from minio import Minio

from db.inbox import inbox
from models.inbox import Inbox
from models.user import User
from core.config import settings
from .request import RequestService
from .base import BaseService


class InboxService(BaseService):

    async def create(self, files: List[UploadFile], requests: RequestService, user: User) -> List[Inbox]:
        if not 1 <= len(files) <= 15:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Вы можете загрузить от 1 до 15 файлов"
            )

        req = None

        client = Minio(
            "minio:9000",
            access_key=settings.MINIO_ROOT_USER,
            secret_key=settings.MINIO_ROOT_PASSWORD,
            secure=False
        )
        res = []

        today = datetime.datetime.now()

        bucket_name = today.strftime('%Y%m%d')
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)

        for file in files:
            if not file.content_type == "image/jpeg":
                continue
            if not req:
                req = await requests.create(user)

            file_name = f'{uuid.uuid4()}.jpg'
            bytes_file = await file.read()
            await file.seek(0)
            client.put_object(bucket_name, file_name, file.file, len(bytes_file))
            cur = Inbox(
                request_code=req.id,
                file_name=file_name,
                datetime=datetime.datetime.utcnow(),
            )

            values = {**cur.dict()}
            values.pop("id", None)

            query = inbox.insert().values(**values)
            cur.id = await self.database.execute(query)
            res.append(cur)
        return res

    async def get_file(self, request_code: int, requests: RequestService, user: User) -> List[Inbox]:
        req = await requests.get_by_id(request_code)
        if not req:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Неверный код запроса")
        if req.user_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="У вас нет доступа к данному запросу")
        return await self.get_by_request_code(request_code)

    async def get_by_request_code(self, request_code: int) -> List[Inbox]:
        query = inbox.select().where(inbox.c.request_code == request_code)
        inbox_list = await self.database.fetch_all(query)
        return list(map(lambda val: Inbox.parse_obj(val), inbox_list))

    async def delete(self, request_code: int, requests: RequestService, user: User) -> Response:
        req = await requests.get_by_id(request_code)
        if not req:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Неверный код запроса")
        if req.user_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="У вас нет доступа к данному запросу")

        inboxes = await self.get_by_request_code(request_code)

        client = Minio(
            "minio:9000",
            access_key=settings.MINIO_ROOT_USER,
            secret_key=settings.MINIO_ROOT_PASSWORD,
            secure=False
        )

        bucket_name = inboxes[0].datetime.strftime('%Y%m%d')

        for item in inboxes:
            client.remove_object(bucket_name=bucket_name, object_name=item.file_name)

        await requests.delete(request_code)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

from uuid import UUID

from fastapi import APIRouter, status, Body, Response

from app.dependencies import channels_service
# from app.services.channels.service import ChannelService
from app.telegram.registration import update_handlers
from app.dependencies import settings_service

router = APIRouter(
    prefix="/channels",
    tags=["channels"]
)
# модульность (не нужно все в одном файле), переиспользование настроек (префиксы и т.д.)
# проверка токена авторизации через dependencies. middleware
# общие описания ответов responses
# если устарел - deprecated

# channels_service = ChannelService()

#

@router.get("")
async def get_channels():
    channels = await channels_service.get_active_channels()

    return channels

@router.post("", status_code=status.HTTP_201_CREATED)
async def post_channel(channel_id: int):
    # await update_handlers()
    return await channels_service.create_channel(
        channel_id=channel_id
    )


# @router.get("/update/{channel_id}/{is_active}")
# async def update_channel(channel_id: int, is_active, response:Response):
#     response.headers[str(channel_id)] = is_active
#     return "Success"

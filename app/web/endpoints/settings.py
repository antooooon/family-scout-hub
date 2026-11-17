from uuid import UUID

from fastapi import APIRouter, status

from app.dependencies import settings_service
from app.db.models.settings import SettingsCreate
from app.telegram.registration import update_handlers

router = APIRouter(prefix="/settings",
                   tags=["settings"])


# @router.post("/")
# async def post_settings(name:str, telegram_id: int):
#     return await settings_service.register_settings(
#         name=name,
#         telegram_id=telegram_id
#     )
@router.post("", status_code=status.HTTP_201_CREATED)
async def post_settings(payload: SettingsCreate):
    return await settings_service.register_settings(
        name=payload.name,
        telegram_id=payload.telegram_id
    )

@router.post("/{settings_id}/channels", status_code=status.HTTP_201_CREATED)
async def post_channel_settings(
        settings_id: UUID,
        channel_id: int,
        telegram_id: int
):
    result = await settings_service.add_channel_with_settings(
        settings_id=settings_id,
        channel_id=channel_id,
        telegram_id=telegram_id,
    )

    await update_handlers()

    return result


# settings_id — path-параметр,
# channel_id и telegram_id — query-параметры.


@router.post("/{settings_id}/keywords", status_code=status.HTTP_201_CREATED)
async def post_keyword_settings(
        settings_id: UUID,
        keyword: str
):
    return await settings_service.add_keyword_with_settings(
        settings_id=settings_id,
        word=keyword
    )

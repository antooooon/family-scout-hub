import datetime

from telethon.utils import get_display_name

from app.db.repositories.channels import ChannelRepository
from app.schemas.channels import ChannelCreateDTO
from app.telegram.client import client


class ChannelService:
    def __init__(self):
        self.repository = ChannelRepository()

    async def create_channel(self, channel_id):

        channel = await client.get_entity(channel_id)

        title = get_display_name(channel)

        dto = ChannelCreateDTO(
            telegram_id=channel_id,
            username=channel.username or "",
            title=title,
            is_active=True,
            created_at=datetime.datetime.now()
        )

        return await self.repository.create(dto=dto)


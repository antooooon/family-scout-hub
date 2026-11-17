from telethon import TelegramClient
from telethon.utils import get_display_name

from app.schemas.channels import ChannelCreateDTO


class TelegramChannelProvider:
    def __init__(self, client: TelegramClient):
        self.client = client

    async def get_channel_info(self, channel_id: int):
        channel = await self.client.get_entity(channel_id)

        return ChannelCreateDTO(
            telegram_id=channel.id,
            username=getattr(channel, "username", ""),
            title=get_display_name(channel)
        )

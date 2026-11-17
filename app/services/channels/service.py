import datetime
from uuid import UUID

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from telethon.utils import get_display_name

from app.db.repositories.channels import ChannelRepository
from app.schemas.channels import ChannelCreateDTO
from app.telegram.client import client


class ChannelService:

    def __init__(
            self,
            session_factory: async_sessionmaker[AsyncSession],
            repository: ChannelRepository
    ):
        self.repository = repository
        self.session_factory = session_factory

    async def create_channel(self, channel_id):

        channel = await client.get_entity(channel_id)

        title = get_display_name(channel)

        dto = ChannelCreateDTO(
            telegram_id=channel_id,
            username=channel.username or "",
            title=title,
            # is_active=True,
            # created_at=datetime.datetime.now()
        )

        return await self.repository.create(dto=dto)

    async def create_channel_with_settings(
            self,
            channel_id: int,
            settings_id: UUID,
            telegram_id: int
    ):
        async with self.session_factory() as session:
            async with session.begin():
                ...
        # сначала проверяем права на тек насстройки
        # проверяемм есть ли канал в таблице каналы, еслин ет -создаем
        # создаем канал-настройка
        ...


    async def get_active_channels_ids(self) -> list:
        return await self.repository.get_active_channels_ids()

    async def get_active_channels(self) -> list[dict]:
        return await self.repository.get_active_channels()

    async def get_channels(self) -> list:
        return await self.repository.get_channels()

    async def get_active_channels_ids_for_user(self, telegram_id: int) -> list[int]:
        return await self.repository.get_active_channels_ids_for_user(telegram_id=telegram_id)

from uuid import UUID

from dotenv.main import with_warn_for_invalid_lines
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from telethon import TelegramClient

from app.db.session import async_session

from app.db.models.channels import Channel
from app.db.models.channels_settings import ChannelSettings
from app.db.models.settings import Settings
from app.db.models.users_settings import UserSettings
from app.db.models.users import User

from app.schemas.channels import ChannelCreateDTO


class ChannelRepository:

    async def create(self, dto) -> Channel:
        async with async_session() as session:
            channel = Channel(
                telegram_id=dto.telegram_id,
                username=dto.username,
                title=dto.title,
                is_active=dto.is_active,
                created_at=dto.created_at
            )

            session.add(channel)
            await session.commit()
            await session.refresh(channel)

            return channel

    async def get_active_channels_ids(self) -> list:
        async with async_session() as session:
            stmt = (
                select(Channel.telegram_id)
                .where(Channel.is_active.is_(True))
            )

            result = await session.execute(stmt)

            return list(result.scalars().all())

    async def get_active_channels(self) -> list[dict]:
        async with async_session() as session:
            stmt = (
                select(Channel.telegram_id,
                       Channel.title)
                .where(Channel.is_active.is_(True))
            )

            result = await session.execute(stmt)

            return [dict(row) for row in result.mappings().all()]

    async def get_channels(self) -> list:
        async with async_session() as session:
            stmt = (
                select(Channel.telegram_id,
                       Channel.title)
            )

            result = await session.execute(stmt)

            return list(result.scalars().all())

    async def get_active_channels_ids_for_user(
            self,
            telegram_id: int
    ) -> list[int]:
        async with async_session() as session:
            stmt = (
                select(Channel.telegram_id)
                .join(ChannelSettings,  ChannelSettings.channel_id == Channel.id)
                .join(Settings,         Settings.id == ChannelSettings.settings_id)
                .join(UserSettings,     UserSettings.settings_id == Settings.id)
                .join(User,             User.id == UserSettings.user_id)
                .where(
                    User.telegram_id == telegram_id,
                    Channel.is_active.is_(True),
                    Settings.is_active.is_(True),
                )
                .distinct()
            )

            result = await session.execute(stmt)

            return list(result.scalars().all())


    async def update_channel(
            self,
            telegram_id: int,
            dto: ChannelCreateDTO
    ) -> Channel | None:

        update_data = dto.model_dump(exclude_unset=True)

        if not update_data:
            return None

        async with async_session() as session:
            stmt = (
                update(Channel)
                .where(Channel.telegram_id == telegram_id)
                .values(**update_data)
                .returning(Channel)
            )

            result = await session.execute(stmt)

            channel = result.scalar_one_or_none()

            await session.commit()

            return channel


    async def create_or_get_channel(
            self,
            session: AsyncSession,
            channel_id: int,
            channel_username: str,
            channel_title: str
    ):
        stmt = (
            select(Channel)
            .where(Channel.telegram_id == channel_id)
        )

        result = await session.execute(stmt)
        channel = result.scalar_one_or_none()

        if channel is None:
            channel = Channel(
                telegram_id=channel_id,
                username=channel_username,
                title=channel_title
            )
            session.add(channel)
            await session.flush()

            return channel

        return channel

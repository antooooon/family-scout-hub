from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.channels_settings import ChannelSettings


class ChannelSettingsRepository:

    async def create_channel_settings(
            self,
            session: AsyncSession,
            settings_id: UUID,
            channel_id: int
    ):
        channel_settings = ChannelSettings(
            settings_id=settings_id,
            channel_id=channel_id
        )

        session.add(channel_settings)

        await session.flush()

        return channel_settings

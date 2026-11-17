from sqlalchemy import select

from app.db.models.channels_settings import ChannelSettings
from app.db.models.channels import Channel
from app.db.models.keywords import Keyword
from app.db.models.settings import Settings
from app.db.session import async_session


class MonitoringRepository:

    async def get_monitoring_data(
            self,
            channels_ids: list
    ) -> list:
        async with async_session() as session:
            stmt = (
                select(
                    Channel.telegram_id,
                    Settings.id.label("settings_id"),
                    Settings.name.label("settings_name"),
                    Keyword.word
                )
                .join(
                    ChannelSettings,
                    ChannelSettings.channel_id == Channel.id
                )
                .join(
                    Settings,
                    Settings.id == ChannelSettings.settings_id
                )
                .join(
                    Keyword,
                    Keyword.settings_id == Settings.id
                )
                .where(
                    Channel.telegram_id.in_(channels_ids),
                    Keyword.is_active.is_(True),
                    Settings.is_active.is_(True)
                )
                .distinct()
            )

            result = await session.execute(stmt)

            return result.mappings().all()

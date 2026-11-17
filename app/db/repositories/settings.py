from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from app.db.models import Settings


class SettingsRepository:

    async def register_settings(
            self,
            session: AsyncSession,
            name: str
    ) -> Settings:

        settings = Settings(
            id=uuid4(),
            name=name
        )

        session.add(settings)
        await session.flush()

        return settings

    async def get_settings(
            self,
            session: AsyncSession,
            settings_id: UUID
    ):
        stmt = (
            select(Settings)
            .where(Settings.id==settings_id)
        )

        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    async def delete_settings(
            self,
            session: AsyncSession,
            settings_id: UUID
    ):
        stmt = (
            delete(Settings)
            .where(Settings.id==settings_id)
        )

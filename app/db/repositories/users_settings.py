from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.user_roles import UserRole
from app.db.models.users_settings import UserSettings


class UserSettingsRepository:

    async def create_user_settings(
            self,
            session: AsyncSession,
            settings_id: UUID,
            user_id: int,
            role: UserRole
    ) -> UserSettings:

        user_settings = UserSettings(
            settings_id=settings_id,
            user_id=user_id,
            role=role
        )

        session.add(user_settings)
        await session.flush()

        return user_settings

    async def get_user_settings(
            self
    ):
        ...


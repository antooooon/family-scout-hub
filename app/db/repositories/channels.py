from sqlalchemy import select, update

from app.db.session import async_session
from app.db.models.channels import Channel
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

    async def get_active_channels(self) -> list:
        async with async_session() as session:
            stmt = (
                select(Channel.telegram_id,
                       Channel.title)
                .where(Channel.is_active.is_(True))
            )

            result = await session.execute(stmt)

            return list(result.mappings().all())

    async def get_channels(self) -> list:
        async with async_session() as session:
            stmt = (
                select(Channel.telegram_id,
                       Channel.title)
            )

            result = await session.execute(stmt)

            return list(result.mappings().all())

    async def update_channel(
            self,
            telegram_id:int,
            dto:ChannelCreateDTO
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

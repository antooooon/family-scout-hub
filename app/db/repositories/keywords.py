from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.keywords import Keyword
from app.db.session import async_session


class KeywordRepository:

    async def create(
            self,
            dto
    ) -> Keyword:
        async with async_session() as session:
            keyword = Keyword(
                word=dto.word,
                is_active=dto.is_active,
                # created_at=dto.created_at
            )

            session.add(keyword)
            await session.commit()
            await session.refresh(keyword)

            return keyword

    async def get_active_keywords(self) -> list[str]:
        async with async_session() as session:
            stmt = (
                select(Keyword.word)
                .where(Keyword.is_active.is_(True))
            )

            result = await session.execute(stmt) # statement

            return list(result.scalars().all())

    async def create_with_settings(
            self,
            session: AsyncSession,
            settings_id: UUID,
            word: str
    ) -> Keyword:
        keyword = Keyword(
            settings_id=settings_id,
            word=word
        )

        session.add(keyword)
        await session.flush()

        return keyword

    async def delete(
            self,
            word: str
    ):
        ...
# Repository не должен знать:
#
# Telegram это или FastAPI;
# зачем нам keyword;
# что делать при совпадении;
# отправлять ли уведомление.
#
# Он просто работает с данными
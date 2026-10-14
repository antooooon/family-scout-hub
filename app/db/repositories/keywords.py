from sqlalchemy import select

from app.db.models.keywords import Keyword
from app.db.session import async_session


class KeywordRepository:

    async def create(self, dto) -> Keyword:
        async with async_session() as session:
            keyword = Keyword(
                word=dto.word,
                is_active=dto.is_active,
                created_at=dto.created_at
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

    async def delete(self, word: str):
        ...


# Repository не должен знать:
#
# Telegram это или FastAPI;
# зачем нам keyword;
# что делать при совпадении;
# отправлять ли уведомление.
#
# Он просто работает с данными
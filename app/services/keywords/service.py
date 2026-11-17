from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.db.repositories.keywords import KeywordRepository
from app.services.keywords.matcher import find_keywords


class KeywordService:

    def __init__(
            self,
            session_factory: async_sessionmaker[AsyncSession],
            repository: KeywordRepository
    ):
        self.session_factory = session_factory
        self.repository = repository

    async def find_matches(self, text: str) -> list[str]:
        keywords = await self.repository.get_active_keywords()

        return find_keywords(text, keywords)

    async def find_matches_for_channel(
            self,
            text: str,
            keywords: list
    ) -> list[str]:
        # keywords = await self.repository.get_active_keywords()

        return find_keywords(text, keywords)

    async def create_keyword(self, dto):
        # if dto.created_at is None:
        #     dto.created_at = datetime.now()

        return await self.repository.create(dto=dto)

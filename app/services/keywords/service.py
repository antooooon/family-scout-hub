from datetime import datetime

from app.db.repositories.keywords import KeywordRepository
from app.services.keywords.matcher import find_keywords


class KeywordService:

    def __init__(self):
        self.repository = KeywordRepository()

    async def find_matches(self, text: str) -> list[str]:
        keywords = await self.repository.get_active_keywords()

        return find_keywords(text, keywords)

    async def create_keyword(self, dto):
        if dto.created_at is None:
            dto.created_at = datetime.now()

        return await self.repository.create(dto=dto)

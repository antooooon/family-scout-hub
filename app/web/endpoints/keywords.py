import datetime

from fastapi import APIRouter

from app.services.keywords.service import KeywordService
from app.schemas.keywords import KeywordCreatedDTO


router = APIRouter(prefix="/keywords")

keyword_service = KeywordService()


@router.get("/")
async def get_keywords(status_code=200):
    keywords = await keyword_service.repository.get_active_keywords()

    return keywords


@router.post("/{word}")
async def post_keywords(word):

    dto = KeywordCreatedDTO(
        word=word,
        is_active=True,
        created_at=datetime.datetime.now()
    )

    return await keyword_service.create_keyword(dto=dto)

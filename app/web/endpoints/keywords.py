import datetime

from fastapi import APIRouter, status

# from app.services.keywords.service import KeywordService
from app.dependencies import keyword_service
from app.schemas.keywords import KeywordCreatedDTO


router = APIRouter(
    prefix="/keywords",
    tags=["keywords"]
)

# keyword_service = KeywordService()


@router.get("")
async def get_keywords(status_code=status.HTTP_200_OK):
    keywords = await keyword_service.repository.get_active_keywords()

    return keywords


@router.post("")
async def post_keywords(word: str, status_code=status.HTTP_201_CREATED):

    dto = KeywordCreatedDTO(
        word=word
    )

    return await keyword_service.create_keyword(dto=dto)

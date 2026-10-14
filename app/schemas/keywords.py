from datetime import datetime

from pydantic import BaseModel


class KeywordCreatedDTO(BaseModel):
    word: str
    is_active: bool
    created_at: datetime


class KeywordDeleteDTO(BaseModel):
    ...
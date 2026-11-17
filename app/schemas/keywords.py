from datetime import datetime, timezone

from pydantic import BaseModel
from pydantic.v1 import Field


class KeywordCreatedDTO(BaseModel):
    word: str
    is_active: bool = True
    # created_at: datetime = Field(
    #     default_factory=lambda: datetime.now(timezone.utc)
    # )


class KeywordDeleteDTO(BaseModel):
    ...
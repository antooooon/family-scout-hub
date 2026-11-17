from datetime import datetime, timezone

from pydantic import BaseModel, Field


class ChannelCreateDTO(BaseModel):

    telegram_id: int
    username: str | None = None
    title: str | None = None

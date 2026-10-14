from datetime import datetime

from pydantic import BaseModel


class ChannelCreateDTO(BaseModel):

    telegram_id: int
    username: str
    title: str
    is_active: bool
    created_at: datetime
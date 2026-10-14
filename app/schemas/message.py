from datetime import datetime

from pydantic import BaseModel


class CreateMessageDTO(BaseModel):
    id: int
    channel_id: int
    keyword_id: int
    text: str
    publisher_id: int
    created_at: datetime

class DeleteMessageDTO(BaseModel):
    ...

class UpdateMessageDTO(BaseModel):
    id: int
    created_at: datetime
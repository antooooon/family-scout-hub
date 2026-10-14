from datetime import datetime

from sqlalchemy import Integer, String, DateTime, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base import DataBase


class Message(DataBase):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    channel_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    keyword_id: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(String)
    publisher_id: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime)
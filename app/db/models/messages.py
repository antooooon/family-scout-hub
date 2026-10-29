from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, DateTime, BigInteger, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import DataBase
if TYPE_CHECKING:
    from app.db.models.matches import Match


class Message(DataBase):
    __tablename__ = "messages"

    __table_args__ = (
        UniqueConstraint(
            "message_id",
            "channel_id",
            name="uq_message_channel",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    message_id: Mapped[int] = mapped_column(BigInteger)
    channel_id: Mapped[int] = mapped_column(BigInteger)
    # keyword_id: Mapped[int] = mapped_column(Integer, default=-1)
    text: Mapped[str] = mapped_column(String)
    publisher_id: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    # --- relationships ---
    match: Mapped[list["Match"]] = relationship(
        back_populates="message",
    )

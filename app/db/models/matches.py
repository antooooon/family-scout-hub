from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Integer, DateTime, Uuid, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models.base import DataBase
if TYPE_CHECKING:
    from app.db.models.messages import Message
    from app.db.models.settings import Settings


class Match(DataBase):
    __tablename__ = "matches"

    __table_args__ = (
        PrimaryKeyConstraint(
            "message_id",
            # "channel_id",
            "settings_id",
            name="pk_matches",
        ),
    )

    message_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("messages.id", ondelete="CASCADE"),
    )

    settings_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("settings.id", ondelete="CASCADE"),
    )

    created_at: Mapped[datetime] = mapped_column(DateTime)

    # --- relationships ---
    message: Mapped["Message"] = relationship(
        back_populates="match",
    )

    settings: Mapped["Settings"] = relationship(
        back_populates="match",
    )

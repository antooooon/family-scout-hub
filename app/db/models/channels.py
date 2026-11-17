from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import DataBase
if TYPE_CHECKING:
    from app.db.models.channels_settings import ChannelSettings


class Channel(DataBase):
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    telegram_id: Mapped[int] = mapped_column(
        Integer,
        # ForeignKey("channel.channel_id"),
        unique=True
    )

    username: Mapped[str] = mapped_column(String)

    title: Mapped[str] = mapped_column(String)

    is_active: Mapped[bool] = mapped_column(Boolean, default=1)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    # --- relationships ---
    channel_settings: Mapped[list["ChannelSettings"]] = relationship(
        back_populates="channel",
        cascade="all, delete-orphan",
    )

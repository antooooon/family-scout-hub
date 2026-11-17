from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Integer, Uuid, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import DataBase
if TYPE_CHECKING:
    from app.db.models.channels import Channel
    from app.db.models.settings import Settings


# Many-to-Many.
class ChannelSettings(DataBase):
    __tablename__ = "channels_settings"

    __table_args__ = (
        UniqueConstraint("channel_id", "settings_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    channel_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("channels.id", ondelete="CASCADE"),
        # unique=True
    )

    settings_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("settings.id", ondelete="CASCADE")
    )

    # --- relationships ---
    channel: Mapped["Channel"] = relationship(
        back_populates="channel_settings"
    )

    settings: Mapped["Settings"] = relationship(
        back_populates="channel_settings"
    )


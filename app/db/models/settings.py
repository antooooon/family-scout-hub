from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, Field
from sqlalchemy import Integer, String, Boolean, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import DataBase

if TYPE_CHECKING:
    from app.db.models.channels_settings import ChannelSettings
    from app.db.models.keywords import Keyword
    from app.db.models.users_settings import UserSettings
    from app.db.models.matches import Match


class Settings(DataBase):
    __tablename__ = "settings"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)  # Foreign Key (FK) для users, user_groups
    name: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # --- relationships ---
    channel_settings: Mapped[list["ChannelSettings"]] = relationship(
        back_populates="settings",
        cascade = "all, delete-orphan",
    )

    keyword: Mapped[list["Keyword"]] = relationship(
        back_populates="settings",
        cascade="all, delete-orphan",
    )

    settings_associations: Mapped[list["UserSettings"]] = relationship(     # Один Settings → много записей связей
        back_populates="settings",
        cascade="all",
    )

    # --- relationships ---
    match: Mapped[list["Match"]] = relationship(
        back_populates="settings"
    )


class SettingsCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
        description="name of the settings",
        examples=["Python jobs"]
    )
    telegram_id: int = Field(
        description="user Telegram ID",
        examples=[817775867]
    )

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Integer, String, Boolean, DateTime, Uuid
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import DataBase
if TYPE_CHECKING:
    from app.db.models.settings import Settings


# One-to-Many
class Keyword(DataBase):
    __tablename__ = "keywords"

    __table_args__ = (
        UniqueConstraint(
            "settings_id",
            "word",
            name="uq_keyword_settings_word"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    settings_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("settings.id", ondelete="CASCADE"),
        nullable=False
    )
    word: Mapped[str] = mapped_column(String, nullable=False)
    # created_at: Mapped[datetime] = mapped_column(DateTime)

    # --- relationships ---
    settings: Mapped["Settings"] = relationship(
        back_populates="keyword",
    )

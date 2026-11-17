from datetime import datetime, timezone
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    Integer,
    DateTime,
    Enum,
    ForeignKey,
    Uuid
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import DataBase
from app.db.models.user_roles import UserRole
if TYPE_CHECKING:
    from app.db.models.settings import Settings
    from app.db.models.users import User


class UserSettings(DataBase):
    __tablename__ = "user_settings"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    settings_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("settings.id", ondelete="CASCADE"),
        primary_key=True
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(
            UserRole,
            values_callable=lambda enum_cls: [
                member.value for member in enum_cls
            ]
        ),
        nullable=False,
        default=UserRole.VIEWER,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    # --- relationships ---
    user: Mapped["User"] = relationship(            # Одна запись связи → один User
        # foreign_keys=[user_id],
        back_populates="user_associations",
    )
    # У модели UsersSettings есть отношение к модели User
    # Чтобы понять, как связывать записи, используй колонку user_id(если она используется еще где-то)

    settings: Mapped["Settings"] = relationship(        # Одна запись связи → один Settings
        # foreign_keys=[settings_id],
        back_populates="settings_associations",
    )
    # "Settings" - строковая аннотация(Forward Reference)

    # back_populates - Это механизм, который связывает два отношения
    # между моделями и синхронизирует их на уровне Python - объектов.





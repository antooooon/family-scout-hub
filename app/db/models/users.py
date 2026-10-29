from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import DataBase
if TYPE_CHECKING:
    from app.db.models.users_settings import UserSettings


class User(DataBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(String)
    telegram_id: Mapped[int] = mapped_column(Integer,
                                             unique=True,
                                             nullable=False)

    user_associations: Mapped[list["UserSettings"]] = relationship(     # Один User → много записей связей
        back_populates="user",
        cascade="all"
    )
    # ORM cascade Указывается в relationship()

    # есть еще Каскад на уровне БД: ondelete - mapped_column(ForeignKey("settings.id", ondelete="CASCADE")
    # Если физически удалить запись Settings, база данных автоматически удалит записи, которые ссылаются на неё через этот FK.

# Каскад	            Что означает
# save-update	    Добавление родителя в Session распространяется на связанные объекты
# merge	            Передача состояния связанных объектов при merge()
# delete	        Удаление родителя приводит к удалению связанных объектов
# delete-orphan	    Удаление объекта из родительской коллекции приводит к его удалению из БД
# all	            Набор основных каскадов: save-update, merge, refresh-expire, expunge, delete
#
# all не включает delete-orphan — его добавляют отдельно.

# составное ограничение:
# UNIQUE(user_id, settings_id)
# Это называется Composite Unique Constraint.
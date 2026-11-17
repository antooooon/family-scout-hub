from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.db.repositories.users import UsersRepository
from app.db.models.users import User
# from app.db.session import async_session


# вводим атомарность: либо вся бизнес операция, либо ничего. поэтому тут session, а не в репо
class UsersService:

    def __init__(
            self,
            session_factory: async_sessionmaker[AsyncSession],
            repository: UsersRepository
    ):
        self.session_factory = session_factory
        self.repository = repository

    async def register_or_get(self,
                              telegram_id:int,
                              username:str | None
                              ) -> User:

        async with self.session_factory() as session:
            async with session.begin():
                user = await self.repository.get_user(
                    telegram_id=telegram_id,
                    session=session
                )

                if user is None:
                    return await self.repository.register_user(
                        session=session,
                        telegram_id=telegram_id,
                        username=username
                    )

                return user

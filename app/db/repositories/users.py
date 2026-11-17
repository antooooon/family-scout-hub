from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# from app.db.session import async_session
from app.db.models.users import User


class UsersRepository:

    # flush() для отправки изменений, пока транзакция еще не закончена
    async def get_user(self,
                       session: AsyncSession,
                       telegram_id: int
                       ) -> User | None:
        stmt = (
            select(User)
            .where(User.telegram_id == telegram_id)
        )

        result = await session.execute(stmt)

        print(result)

        return result.scalar_one_or_none()


    async def register_user(self,
                            session: AsyncSession,
                            telegram_id:int,
                            username:str | None) -> User:
        user = User(
            telegram_id=telegram_id,
            user_name=username
        )

        session.add(user)
        await session.flush()

        return user

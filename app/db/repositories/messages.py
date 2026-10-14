from sqlalchemy import select

from app.db.session import async_session
from app.db.models.messages import Message

_ = select()

class MessageRepository:

    async def create(self, dto):
        async with async_session() as session:
            message = Message(
                id=dto.id,
                channel_id=dto.channel_id,
                keyword_id=dto.keyword_id,
                text=dto.text,
                publisher_id=dto.publisher_id,
                created_at=dto.created_at
            )

            session.add(message)
            await session.commit()
            await session.refresh(message)

            return message

    async def get_message(self, keyword_id) -> list:
        ...
        # async with async_session() as session:
        #     stmt = (
        #         select(Message.text)
        #         .where(Message.keyword_id.is_(keyword_id))
        #     )
        #
        #     result = await session.execute(stmt)
        #
        #     return list(result.scalars().all())

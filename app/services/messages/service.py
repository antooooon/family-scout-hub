# 1. СОЗДАНИЕ. создавать сообщения, которые были найдены
# 2. ПОИСК. искать сообщения по отправителю и содержанию и ключ. слову, если одинаково, то пропускать
# 3. АПДЕЙТ. если найдены сообщения, но отличаются, ценой, например, то обновлять в БД
# 4. УДАЛЕНИЕ. удаление сообщения по id или дате и id_публициста
#               удлаение всех сообщений по ключ слову
#               удаление всех сообщений по юзеру
#               удаление всех сообщений за период
# 5. QUERY метод. получение списка упорядоченных сообщений по дате, ключ словам, юзеру, каналу

from datetime import datetime

from app.db.repositories.messages import MessageRepository
# from app.services.keywords.matcher import find_keywords


class MessageService:

    def __init__(self):
        self.repository = MessageRepository()

    async def find_matches(self, text: str) -> list[str]:
       ...

    async def create_message(self, dto):
        if dto.created_at is None:
            dto.created_at = datetime.now()

        return await self.repository.create(dto=dto)

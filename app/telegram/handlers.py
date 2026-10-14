import datetime

from telethon import events

from app.config.settings import BASE_DIR
from app.schemas.message import CreateMessageDTO
from app.services.channels.service import ChannelService
from app.services.keywords.service import KeywordService
from app.services.messages.service import MessageService
from app.telegram.client import client


# channels_service = ChannelService().repository
#
# async def get_channels() -> list:
#     return await channels_service.get_active_channels()
#
# CHANNELS = get_channels()
# #
CHANNELS = [
    -1001537731683,     # Батуми Барахолка
    -1001869681010,      # Детская Барахолка
    8580535538
]


@client.on(events.NewMessage(chats=CHANNELS))
async def new_message_handler(event):
    message = event.message

    if not message.text:
        return

    keyword_service = KeywordService()
    keywords = await keyword_service.find_matches(text=message.text)

    if keywords:
    # if any(word in message.text for word in keywords):
        await client.send_message("me", message)
        # message._text - атрибут, message.text - то же, только функция text() через @property, следует использовать его
        await client.send_message("@anastasiakotiki", message)

        dto = CreateMessageDTO(
            id=event.id,
            channel_id=event.chat_id,
            keyword_id=0,
            text=message.text,
            publisher_id=event.sender_id,
            created_at=datetime.datetime.now()
        )
        await MessageService().create_message(dto=dto)

        with open(BASE_DIR / "log.txt", "a", encoding="utf-8") as log:
            log.write("\n" + "=" * 50)
            log.write(f"\nКанал ID: {event.chat_id}")
            log.write(f"\nТекст: {message.text}")
            log.write("\n" + "=" * 50)




# @client.on — это не какой-то отдельный механизм прослушивания Telegram.
#   Это просто удобный способ зарегистрировать функцию в клиенте.

# словарь для хранения настроек каналов для парсинга в разрезе пользователей
# test_settings_dict = {
#     "me": [["job for python", "anoter_chat", ...]],
#     "@anastasiakotiki": [["discounts_batumi", ...]],
#     "everyone": [[CHANNELS], ...]
# }

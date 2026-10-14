from telethon import events

from app.telegram.client import client
from app.telegram.handlers import new_message_handler
from app.services.channels.service import ChannelService


async def register_handlers():
    channel_service = ChannelService()

    channels = await channel_service.repository.get_active_channels_ids()

    if not channels:
        print("Нет активных каналов для мониторинга")
        return

    client.add_event_handler(
        new_message_handler,
        events.NewMessage(chats=channels)
    )

    print(f"Обработчик зарегистрирован для {len(channels)} каналов")


async def update_handlers():
    # Удаляем старую регистрацию
    client.remove_event_handler(new_message_handler)

    # Получаем актуальные каналы
    channel_service = ChannelService()
    channels = await channel_service.repository.get_active_channels_ids()

    if not channels:
        print("Нет активных каналов")
        return

    # Регистрируем обработчик заново
    client.add_event_handler(
        new_message_handler,
        events.NewMessage(chats=channels)
    )

    print(f"Мониторинг каналов обновлён: {len(channels)}")

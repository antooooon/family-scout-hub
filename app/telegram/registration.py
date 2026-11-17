from telethon import events

from app.telegram.client import client
# from app.telegram.handlers import new_message_handler
from app.telegram.handlers import create_handler
# from app.services.channels.service import ChannelService
from app.dependencies import channels_service, monitoring_service


async def register_handlers(telegram_id: int):

    # channels = await channels_service.get_active_channels_ids()
    channels_ids = await channels_service.get_active_channels_ids_for_user(
        telegram_id=telegram_id
    )

    if not channels_ids:
        print("Нет активных каналов для мониторинга")
        return

    channels_map = await monitoring_service.get_monitoring_config(channels_ids=channels_ids)

    handler = create_handler(channels_map=channels_map)

    client.add_event_handler(
        handler,
        # new_message_handler,
        events.NewMessage(chats=list(channels_map.keys()))
    )

    print(f"Обработчик зарегистрирован для {len(channels_map)} каналов")


async def update_handlers():
    pass
    # Удаляем старую регистрацию
    # client.remove_event_handler(new_message_handler)

    # Получаем актуальные каналы
    channels = []
    # channels = await channels_service.get_active_channels_ids_for_user(
    #     telegram_id=telegram_id
    # )

    if not channels:
        print("Нет активных каналов для мониторинга")
        return

    # Регистрируем обработчик заново
    client.add_event_handler(
        # new_message_handler,
        events.NewMessage(chats=channels)   # Создаём новую конфигурацию события.
    )                                       # Здесь хранит именно объект фильтра NewMessage, с которым была выполнена регистрация.

    print(f"Мониторинг каналов обновлён: {len(channels)}")

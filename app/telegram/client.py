import logging

from telethon import TelegramClient

from app.config.settings import settings


logger = logging.getLogger(__name__)

def create_telegram_client() -> TelegramClient:
    return TelegramClient(
        session="telegram_monitor",
        api_id=settings.telegram_api_id,
        api_hash=settings.telegram_api_hash,
        connection_retries=10,
        retry_delay=5,
        auto_reconnect=True,
        timeout=10
    )

client = create_telegram_client()


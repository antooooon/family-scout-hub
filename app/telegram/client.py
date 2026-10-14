from telethon import TelegramClient

from app.config.settings import settings


client = TelegramClient(
    "telegram_monitor",
    settings.telegram_api_id,
    settings.telegram_api_hash,
)
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_PATH = BASE_DIR.parent / ".env"
DB_PATH = f"sqlite+aiosqlite:///{BASE_DIR / 'tg_monitor.db'}"


class Settings(BaseSettings):
    telegram_api_id: int
    telegram_api_hash: str

    database_url: str

    # notification_bot_token: str
    # notification_chat_id: int

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
    )


try:
    settings = Settings(database_url=DB_PATH)
except Exception as err:
    print(f"Ошибка загрузки: {err}")


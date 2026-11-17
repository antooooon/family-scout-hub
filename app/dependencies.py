from app.db.repositories.channels import ChannelRepository
from app.db.repositories.channel_settings import ChannelSettingsRepository
from app.db.repositories.keywords import KeywordRepository
from app.db.repositories.monitoring import MonitoringRepository
from app.db.repositories.settings import SettingsRepository
from app.db.repositories.users import UsersRepository
from app.db.repositories.users_settings import UserSettingsRepository

from app.db.session import async_session

from app.schemas.telegram import TelegramChannelProvider

from app.services.channels.service import ChannelService
from app.services.keywords.service import KeywordService
from app.services.settings.service import SettingsService
from app.services.users.service import UsersService
from app.services.monitoring import MonitoringService
from app.telegram.client import client


users_repository = UsersRepository()
settings_repository = SettingsRepository()
users_settings_repository = UserSettingsRepository()
channel_repository = ChannelRepository()
channel_settings_repository = ChannelSettingsRepository()
keyword_repository = KeywordRepository()
monitoring_repository = MonitoringRepository()


telegram_channel_provider=TelegramChannelProvider(client=client)

users_service = UsersService(
    session_factory=async_session,
    repository=users_repository,
)

settings_service = SettingsService(
    session_factory=async_session,
    repository=settings_repository,
    users_repository=users_repository,
    users_settings_repository=users_settings_repository,
    channel_repository=channel_repository,
    channel_settings_repository=channel_settings_repository,
    channel_provider=telegram_channel_provider,
    keyword_repository=keyword_repository,
)

channels_service = ChannelService(
    session_factory=async_session,
    repository=channel_repository
)

keyword_service = KeywordService(
    session_factory=async_session,
    repository=keyword_repository
)

monitoring_service = MonitoringService(
    repository = monitoring_repository
)

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from telethon import TelegramClient

from app.db.repositories.channel_settings import ChannelSettingsRepository
from app.db.repositories.channels import ChannelRepository
from app.db.repositories.keywords import KeywordRepository
from app.schemas.telegram import TelegramChannelProvider
from app.services.exceptions import UserNotFoundError
from app.db.models import Channel, Keyword, Settings
from app.db.models.user_roles import UserRole
from app.db.repositories.users import UsersRepository
from app.db.repositories.users_settings import UserSettingsRepository
from app.db.repositories.settings import SettingsRepository


class SettingsService:

    def __init__(
            self,
            session_factory: async_sessionmaker[AsyncSession],
            repository: SettingsRepository,
            users_repository: UsersRepository,
            users_settings_repository: UserSettingsRepository,
            channel_repository: ChannelRepository,
            channel_settings_repository: ChannelSettingsRepository,
            channel_provider: TelegramChannelProvider,
            keyword_repository: KeywordRepository,
    ):
        self.session_factory = session_factory
        self.repository = repository
        self.users_repository = users_repository
        self.users_settings_repository = users_settings_repository
        self.channel_repository = channel_repository
        self.channel_settings_repository = channel_settings_repository
        self.channel_provider = channel_provider
        self.keyword_repository = keyword_repository

    async def register_settings(
            self,
            name: str,
            telegram_id: int,
    ) -> Settings:
        async with self.session_factory() as session:
            async with session.begin():

                user = await self.users_repository.get_user(
                    session=session,
                    telegram_id=telegram_id
                )

                if user is None:
                    raise UserNotFoundError(telegram_id)

                settings = await self.repository.register_settings(
                    session=session,
                    name=name
                )

                await self.users_settings_repository.create_user_settings(
                    session=session,
                    settings_id=settings.id,
                    user_id=user.id,
                    role=UserRole.OWNER
                )

                return settings


    async def get_settings(
            self,
            settings_id: UUID,
            # user_id: int
    ):
        async with self.session_factory() as session:
            async with session.begin():
                await self.repository.get_settings(
                    session=session,
                    settings_id=settings_id
                )

    async def add_channel_with_settings(
            self,
            settings_id: UUID,
            channel_id: int,
            telegram_id: int,
    ):
        channel_info = await self.channel_provider.get_channel_info(channel_id)

        channel_username = channel_info.username
        channel_title = channel_info.title

        async with self.session_factory() as session:
            async with session.begin():

                # тут будут определяться настройки авторизованного пользователя

                if not telegram_id == 817775867:
                    raise UserNotFoundError(telegram_id=telegram_id)

                channel = await self.channel_repository.create_or_get_channel(
                    session=session,
                    # settings_id=settings_id,
                    channel_id=channel_id,
                    channel_username=channel_username,
                    channel_title=channel_title
                )

                channel_settings = await self.channel_settings_repository.create_channel_settings(
                    session=session,
                    settings_id=settings_id,
                    channel_id=channel.id
                )

                return channel_settings

    async def add_keyword_with_settings(
            self,
            settings_id: UUID,
            word: str
    ):
        async with self.session_factory() as session:
            async with session.begin():

                # тут будут определяться настройки авторизованного пользователя

                keyword = await self.keyword_repository.create_with_settings(
                    session=session,
                    settings_id=settings_id,
                    word=word
                )

                return keyword





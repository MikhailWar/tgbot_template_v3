from typing import AsyncIterable, AsyncIterator

from aiogram.types import TelegramObject, User
from dishka import Provider, from_context, Scope, provide
from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

from app.bootstrap.config import Config
from app.bootstrap.logging import logger
from app.infrastructure.database.transaction_manager import TransactionManager


class ConfigProvider(Provider):
    config: Config = from_context(
        Config, scope=Scope.APP
    )


class DbProvider(Provider):

    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    async def engine(
            self, config: Config
    ) -> AsyncIterator[AsyncEngine]:
        engine = create_async_engine(config.db.construct_sqlalchemy_url())
        yield engine
        await engine.dispose()

    @provide(scope=Scope.APP)
    def get_sessionmaker(
            self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        factory = async_sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush=False,
        )
        logger.debug("Session provider was initialized")
        return factory

    @provide
    async def get_session(
            self, factory: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with factory() as session:
            yield session


class ApplicationProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_transaction_manager(self, session: AsyncSession) -> TransactionManager:
        return TransactionManager(session)

    @provide(scope=Scope.REQUEST)
    async def get_user(self, event: TelegramObject) -> User:
        return event.chat









from typing import AsyncIterable

from dishka import Provider, from_context, Scope, provide
from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.bootstrap.config import Config
from app.infrastructure.database.transaction_manager import TransactionManager


class ConfigProvider(Provider):
    config: Config = from_context(
        Config, scope=Scope.APP
    )


class DbProvider(Provider):

    @provide(scope=Scope.APP)
    def get_engine(self, config: Config) -> Engine:
        engine = create_async_engine(
            config.db.construct_sqlalchemy_url(),
            query_cache_size=1200,
            pool_size=20,
            max_overflow=200,
            future=True,
        )
        return engine

    @provide(scope=Scope.APP)
    def get_session_pool(self, engine: Engine) -> async_sessionmaker[AsyncSession]:
        session_pool = async_sessionmaker(bind=engine, expire_on_commit=False)
        print(session_pool)
        return session_pool

    @provide(scope=Scope.REQUEST)
    async def get_session(self, session_pool: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with session_pool() as session:
            yield session


class ApplicationProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_transaction_manager(self, session: AsyncSession) -> TransactionManager:
        return TransactionManager(session)
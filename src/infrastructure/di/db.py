from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.infrastructure.database.config import DatabaseConfig
from src.infrastructure.database.factory import create_async_engine, create_sessionmaker


class DatabaseProvider(Provider):
    scope = Scope.APP

    @provide
    def get_async_engine(self, db_config: DatabaseConfig) -> AsyncEngine:
        return create_async_engine(db_config)

    @provide
    def get_sessionmaker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return create_sessionmaker(engine)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, sessionmaker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session

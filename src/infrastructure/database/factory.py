from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from .config import DatabaseConfig


def create_async_engine(db_config: DatabaseConfig, **kwargs) -> AsyncEngine:
    return _create_async_engine(url=db_config.get_database_url(), **kwargs)


def create_sessionmaker(engine: AsyncEngine, **kwargs) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, **kwargs)

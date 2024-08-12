from typing import TypeVar, Generic

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.models.base import Base

Model = TypeVar('Model', bound=Base, covariant=True, contravariant=False)


class BaseRepo(Generic[Model]):
    """
    A class representing a base repository for handling database operations.

    Attributes:
        session (AsyncSession): The database session used by the repository.
        model (Model): The database table model.
    """

    def __init__(self, session: AsyncSession, model: type[Model]) -> None:
        self.session = session
        self.model = model

    async def _get_by_id(self, id_: int) -> Model:
        stmt = (
            select(self.model)
            .where(self.model.id == id_)
        )
        data = await self.session.execute(stmt)
        return data.scalar_one()

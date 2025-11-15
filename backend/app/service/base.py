from sqlalchemy import select, insert, update
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession

from typing import TypeVar,Generic, Type

from app.service.database import async_session_maker

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)

class BaseService(Generic[ModelType]):
    model: Type[ModelType]

    def __init__(self, session: AsyncSession):
        self._session = session
        if self.model is None:
            raise ValueError("Model not found")

    @classmethod
    async def find_by_id(self, model_id: int):
        query = select(self.model).filter_by(id=model_id)
        result = await self._session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self._session.execute(query)
        return result.scalar_one_or_none()


    @classmethod
    async def find_all(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self._session.execute(query)
        return result.scalars().all()
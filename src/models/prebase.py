# Добавляем импорт классов для определения столбца ID.
from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from src.config import DATABASE_URL


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(DATABASE_URL)

AsyncSessionFactory = sessionmaker(engine, class_=AsyncSession)

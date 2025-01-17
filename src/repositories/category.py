from sqlalchemy.future import select

from src.models.category import Category
from src.models.prebase import AsyncSessionFactory
from src.repositories.repository import Repository
from src.schemas.category import Category as Category_schema


async def get_all() -> list[Category]:
    async with AsyncSessionFactory() as session:
        result = await session.execute(select(Category))
        categories = result.scalars().all()
        return categories


async def add(name: str, description: str) -> Category:
    async with AsyncSessionFactory() as session:
        category = Category(name=name, description=description)
        session.add(category)
        await session.commit()
        return category


class CategoryRepository(Repository[Category_schema]):
    async def get_all(self) -> list[Category_schema]:
        pass

    async def add(self, **kwargs: object) -> None:
        pass

    async def update(self, id: int, **kwargs: object) -> None:
        pass

    async def delete(self, id: int) -> None:
        pass


def get_categories_names(categories: list[Category]):
    return [category.name for category in categories]

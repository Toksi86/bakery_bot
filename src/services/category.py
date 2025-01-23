from sqlalchemy.future import select

from src.core.db import AsyncSessionFactory
from src.models.category import Category


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


def get_categories_names(categories: list[Category]) -> list[Category.name]:
    return [category.name for category in categories]

from sqlalchemy.future import select

from src.core.db import AsyncSessionFactory
from src.models.product import Product


async def get_all() -> list[Product]:
    async with AsyncSessionFactory() as session:
        result = await session.execute(select(Product))
        products = result.scalars().all()
        return products


async def add(name: str, description: str, category_id: int) -> Product:
    async with AsyncSessionFactory() as session:
        product = Product(name=name, description=description, category_id=category_id)
        session.add(product)
        await session.commit()
        return product

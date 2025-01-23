import asyncio

from src.services.category import get_all as get_all_categories
from src.services.product import add as add_product
from src.services.product import get_all as get_all_products


async def main():
    categories = await get_all_categories()
    # await add_product('Пирог с картошкой', 'Пирог запечённый в печи с картошкой и луком', 1)
    products = await get_all_products()
    print(categories)
    print(products)


if __name__ == '__main__':
    asyncio.run(main())

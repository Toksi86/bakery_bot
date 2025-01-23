from vkbottle.bot import BotLabeler
from vkbottle.bot import Message

from src.services.product import get_products_by_category

labeler = BotLabeler()


@labeler.message(payload={'cmd': 'product_list'})
async def product_list(message: Message, **kwargs):
    category_name = kwargs['category_name']
    products = await get_products_by_category(category_name)

    if products:
        product_list_text = '\n'.join(products)
        await message.answer(f'Продукты в категории "{category_name}":\n{product_list_text}')
    else:
        await message.answer(f'В категории "{category_name}" нет продуктов.')

from vkbottle.bot import BotLabeler, Message

from src.repositories.category import get_all as get_categories
from src.repositories.category import get_categories_names

labeler = BotLabeler()


@labeler.message(text='Категории')
async def category(message: Message):
    try:
        categories = await get_categories()
        categories_name = get_categories_names(categories)
        await message.answer(f'{categories_name}')
    except Exception as e:
        print(f"Ошибка при получении категорий: {e}")
        await message.answer("Произошла ошибка при получении категорий.")

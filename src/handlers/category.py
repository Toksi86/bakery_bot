import json

from vkbottle import Keyboard, Text
from vkbottle.bot import BotLabeler, Message

from src.services.category import get_all as get_categories
from src.services.category import get_categories_names

labeler = BotLabeler()


@labeler.message(text='Категории')
async def category(message: Message):
    try:
        categories = await get_categories()
        categories_name = get_categories_names(categories)

        keyboard = Keyboard(one_time=True)
        for category_name in categories_name:
            keyboard.add(
                Text(category_name, payload={"cmd": "selected_category_cmd", "selected_category": category_name}))

        await message.answer('Выберите категорию:', keyboard=keyboard)
    except Exception as e:
        print(f"Ошибка при получении категорий: {e}")
        await message.answer("Произошла ошибка при получении категорий.")


@labeler.message(payload_contains={"cmd": "selected_category_cmd"})
async def additional_message_handler(message: Message, **kwargs):
    try:
        payload_dict = json.loads(message.payload)
        selected_category = payload_dict.get("selected_category")
        if selected_category:
            await message.answer(f"Выбрана категория: {selected_category}")
        else:
            await message.answer("Не удалось получить выбранную категорию из payload.")

    except json.JSONDecodeError as e:
        print(f"Ошибка при декодировании payload: {e}")
        await message.answer("Произошла ошибка при обработке payload.")

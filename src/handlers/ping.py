from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()


@labeler.message(text="ping")
async def ping_handler(message: Message):
    await message.answer("pong")

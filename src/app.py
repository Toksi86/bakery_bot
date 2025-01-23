from vkbottle import LoopWrapper
from vkbottle.bot import Bot

from src.core.config import TOKEN
from src.handlers import labelers


def init_bot():
    """Фабрика для бота.
    """
    bot_ = Bot(token=TOKEN,
               loop_wrapper=LoopWrapper())
    for labeler in labelers:
        bot_.labeler.load(labeler)

    return bot_


bot = init_bot()

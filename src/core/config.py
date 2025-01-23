import os

from dotenv import load_dotenv
from vkbottle import BuiltinStateDispenser
from vkbottle.bot import BotLabeler

load_dotenv()
TOKEN = os.getenv('TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()

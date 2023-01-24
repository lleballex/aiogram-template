from aiogram import Bot, Dispatcher

from os import getenv


BOT_TOKEN = getenv('BOT_TOKEN')
assert BOT_TOKEN is not None


dp = Dispatcher()
bot = Bot(BOT_TOKEN, parse_mode="HTML")

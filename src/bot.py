from handlers import register_handlers

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

from pathlib import Path
from loguru import logger
from dotenv import load_dotenv


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent

    load_dotenv(base_dir / '.env')
    logger.add(base_dir / 'logs.log', level="INFO")

    import config

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.BOT_TOKEN, parse_mode='HTML')

    register_handlers(dp)

    logger.info('Bot started')
    dp.run_polling(bot)
    logger.info('Bot stopped')


if __name__ == '__main__':
    main()

import asyncio
import logging.config

from aiogram import Bot, Dispatcher

from config import bot_config
from config import logging_config


logging.config.dictConfig(logging_config.logging_config)


async def main():
    BOT = Bot(bot_config.main_config.tg_bot.token)
    dp = Dispatcher()

    await dp.start_polling(BOT)


if __name__ == '__main__':
    asyncio.run(main())
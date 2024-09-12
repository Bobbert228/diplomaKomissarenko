import asyncio
import logging
import sys
from os import getenv
import config

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """ Реакция бота на команду /start """
    await message.answer(f"Приветствую, {message.from_user.full_name}. Приятного пользования ботом. Выберите функцию.")



async def main() -> None:
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

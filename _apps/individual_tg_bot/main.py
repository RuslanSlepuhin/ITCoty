import asyncio
import logging

from _apps.individual_tg_bot.commands import set_default_commands
from _apps.individual_tg_bot.handlers.main_handler import Handlers
from _apps.individual_tg_bot.settings import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ParseMode
from aiogram.utils import executor

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
Handlers(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()

    dp.filters_factory.bind(Command)
    loop.create_task(set_default_commands(bot))
    loop.create_task(bot.delete_webhook(drop_pending_updates=True))
    executor.start_polling(dp, skip_updates=True)

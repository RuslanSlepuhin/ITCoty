import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types.message import ParseMode
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from _apps.individual_tg_bot.commands import set_default_commands
from _apps.individual_tg_bot.settings import TOKEN
from aiogram.dispatcher.filters import Command



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    loop = asyncio.new_event_loop()
    dp = Dispatcher(bot, storage=MemoryStorage())
    dp.message_handlers()
    dp.middleware.setup()
    dp.filters_factory.bind(Command)
    loop.create_task(set_default_commands(bot))
    loop.create_task(bot.delete_webhook(drop_pending_updates=True))
    executor.start_polling(dp, skip_updates=True)


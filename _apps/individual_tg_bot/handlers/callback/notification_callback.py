
from aiogram.types import CallbackQuery
from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.keyboards.inline.main_menu import get_inline_menu
from _apps.individual_tg_bot.service import db


async def get_per_day_notification(query: CallbackQuery) -> None:
    """Обработка per_day_notification callback"""
    pass


async def get_on_getting_notification(query: CallbackQuery) -> None:
    """Обработка on_getting_notification callback"""
    pass


async def cancel_notification(query: CallbackQuery) -> None:
    """Обработка cancel_notification callback"""
    await db.delete_user_request(query.from_user.id)
    await query.message.answer(text=text.menu, reply_markup=get_inline_menu())

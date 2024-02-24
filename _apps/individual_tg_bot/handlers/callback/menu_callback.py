from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.keyboards.inline.direction_buton import (
    get_direction_button,
)
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot.keyboards.inline.notifications import notification_button
from _apps.individual_tg_bot.keyboards.inline.new_request import new_request_button
from _apps.individual_tg_bot.service import db


async def get_vacancy_filter(query: CallbackQuery) -> None:
    """Обработка vacancy_filter callback"""
    result = await db.get_user_request()
    users = [user.get('user_id') for user in result]
    if query.from_user.id in users:
        await query.message.answer(text.new_request, reply_markup=new_request_button())
    else:
        await query.message.answer(text=text.direction, reply_markup=get_direction_button())


async def get_notification_callback(query: CallbackQuery) -> None:
    """Обработка notification callback"""
    await query.message.answer(text=text.get_notification, reply_markup=notification_button())


async def get_restart(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка restart callback"""
    pass
    # await query.message.answer(text=text.direction, reply_markup=get_direction_button())
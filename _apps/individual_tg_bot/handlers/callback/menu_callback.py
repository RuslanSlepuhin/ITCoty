from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.keyboards.inline.direction_buton import (
    get_direction_button,
)
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


async def get_vacancy_filter(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка start_survey callback"""
    await query.message.answer(text=text.direction, reply_markup=get_direction_button())

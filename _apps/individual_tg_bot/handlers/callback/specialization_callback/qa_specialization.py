from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot .keyboards.inline.level_button import level_button


async def qa_manual_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Product manager"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.manual}",
        reply_markup=level_button(),
    )

async def qa_auto_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Product manager"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.auto}",
        reply_markup=level_button(),
    )

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot .keyboards.inline.level_button import level_button




#@router.callback_query(F.data == text.system_analyst)
async def system_analyst_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback System Analyst"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.system_analyst}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.ba)
async def ba_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback BA"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.ba}",
        reply_markup=level_button(),
    )

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot .keyboards.inline.level_button import level_button



#@router.callback_query(F.data == text.project_manager)
async def project_manager_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Project manager"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.project_manager}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.product_manager)
async def product_manager_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Product manager"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.product_manager}",
        reply_markup=level_button(),
    )

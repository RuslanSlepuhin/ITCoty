from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text

from _apps.individual_tg_bot.keyboards.inline.level_button import level_button




#@router.callback_query(F.data == text.unity)
async def unity_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Unity"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.unity}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.game_designer)
async def game_designer_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Game designer"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.game_designer}",
        reply_markup=level_button(),
    )

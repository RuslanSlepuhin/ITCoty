from aiogram.dispatcher import FSMContext

from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.keyboards.inline.level_button import level_button




#@router.callback_query(F.data == text.react)
async def react_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback React"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.react}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.angular)
async def angular_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Angular"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.angular}",
        reply_markup=level_button(),
    )


@router.callback_query(F.data == text.vue)
async def vue_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Vue"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.vue}",
        reply_markup=level_button(),
    )

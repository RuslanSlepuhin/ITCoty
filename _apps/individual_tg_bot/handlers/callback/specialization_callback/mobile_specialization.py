from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot .keyboards.inline.level_button import level_button



#@router.callback_query(F.data == text.ios)
async def ios_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback IOS"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.ios}",
        reply_markup=level_button(),
    )


@router.callback_query(F.data == text.android)
async def android_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Android"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.android}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.flutter)
async def flutter_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Flutter"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.flutter}",
        reply_markup=level_button(),
    )

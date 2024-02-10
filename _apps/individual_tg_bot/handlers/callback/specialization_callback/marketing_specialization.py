from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot .keyboards.inline.level_button import level_button




#@router.callback_query(F.data == text.seo)
async def seo_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback SEO"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.seo}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.copywriter)
async def copywriter_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Copywriter"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.copywriter}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.marketer)
async def marketer_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Marketer"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.marketer}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.content_manager)
async def content_manager_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Content manager"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.content_manager}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.media_buyer)
async def media_buyer_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Media buyer"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.media_buyer}",
        reply_markup=level_button(),
    )


from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot .keyboards.inline.level_button import level_button




#@router.callback_query(F.data == text.motion)
async def motion_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Motion"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.motion}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.three_d)
async def three_d_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback 3D"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.three_d}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.ux_ui)
async def ux_ui_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback UX/UI"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.ux_ui}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.illustrator)
async def illustrator_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Illustrator"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.illustrator}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.graphic)
async def graphic_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Graphic"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.graphic}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.design)
async def design_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Designer"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.design}",
        reply_markup=level_button(),
    )

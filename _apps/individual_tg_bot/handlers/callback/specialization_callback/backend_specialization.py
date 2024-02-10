
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot .keyboards.inline.level_button import level_button




#@router.callback_query(F.data == text.one_c)
async def one_c_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback 1C"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.one_c}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.java)
async def java_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Java"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.java}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.python)
async def python_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Python"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.python}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.php)
async def php_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback PHP"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.php}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.c_plus_plus)
async def c_plus_plus_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback C++"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.c_plus_plus}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.c_sharp)
async def c_sharp_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback C#"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.c_sharp}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.dot_net)
async def dot_net_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback .Net"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.dot_net}",
        reply_markup=level_button(),
    )


#@router.callback_query(F.data == text.golang)
async def golang_callback(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка callback Golang"""
    await query.message.answer(
        text=f"Необходимо выбрать уровень владения {text.golang}",
        reply_markup=level_button(),
    )

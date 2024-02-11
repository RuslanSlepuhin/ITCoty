from aiogram.dispatcher import FSMContext
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup)

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.keyboards.inline.level_button import level_button
from _apps.individual_tg_bot.keyboards.inline.specializations.buttons import \
    buttons_sales


async def sales_specialization_callback(
    query: CallbackQuery, state: FSMContext
) -> None:
    """Обработка callback для sales направления"""
    data = await state.get_data()

    selected_specializations = data.get("selected_specializations", set())

    if text.accept in query.data:
        await query.message.answer(
            text=f"Выбранные специализации: {', '.join(selected_specializations)}\nНеобходимо выбрать уровень владения",
            reply_markup=level_button(),
        )
        return

    if query.data in buttons_sales:
        selected_specializations.add(query.data)

    await state.update_data(selected_specializations=selected_specializations)

    updated_keyboard = InlineKeyboardMarkup()
    for button_text, button_callback in buttons_sales.items():
        if button_callback not in selected_specializations:
            updated_keyboard.add(
                InlineKeyboardButton(text=button_text, callback_data=button_callback)
            )

    if query.data in selected_specializations:
        await query.message.answer(
            text=f"Выбранные специализации: {', '.join(selected_specializations)}",
            reply_markup=updated_keyboard,
        )
        return

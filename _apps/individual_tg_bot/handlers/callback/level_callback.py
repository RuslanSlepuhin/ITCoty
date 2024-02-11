from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import _apps.individual_tg_bot.keyboards.inline.specializations.keyboards as kb

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.keyboards.inline.level_button import level_button_dict
from _apps.individual_tg_bot.keyboards.inline.location_button import location_button


async def level_callback_handler(
    query: CallbackQuery, state: FSMContext
) -> None:
    """Обработка callback для уровня владения """
    data = await state.get_data()

    selected_specializations = data.get("selected_specializations", set())

    if text.accept_level in query.data:
        await query.message.answer(
            text=f"{text.chosen_level} {', '.join(selected_specializations)}\n{text.location}",
            reply_markup=location_button(),
        )
        return

    if query.data in level_button_dict:
        selected_specializations.add(query.data)

    await state.update_data(selected_specializations=selected_specializations)

    updated_keyboard = InlineKeyboardMarkup()
    for button_text, button_callback in level_button_dict.items():
        if button_callback not in selected_specializations:
            updated_keyboard.add(
                InlineKeyboardButton(text=button_text, callback_data=button_callback)
            )

    if query.data in selected_specializations:
        await query.message.answer(
            text=f"{text.chosen_level} {', '.join(selected_specializations)}",
            reply_markup=updated_keyboard,
        )
        return
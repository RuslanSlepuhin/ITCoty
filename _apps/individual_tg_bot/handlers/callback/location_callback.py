from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.keyboards.inline.location_button import location_button_dict
from _apps.individual_tg_bot.keyboards.inline.work_format import work_format_button


async def location_callback_handler(
    query: CallbackQuery, state: FSMContext
) -> None:
    """Обработка callback для локации """
    data = await state.get_data()

    selected_specializations = data.get("selected_specializations", set())

    if text.accept_location in query.data:
        await query.message.answer(
            text=f"{text.chosen_location} {', '.join(selected_specializations)}\n{text.work_format}",
            reply_markup=work_format_button(),
        )
        return

    if query.data in location_button_dict:
        selected_specializations.add(query.data)

    await state.update_data(selected_specializations=selected_specializations)

    updated_keyboard = InlineKeyboardMarkup()
    for button_text, button_callback in location_button_dict.items():
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
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from _apps.individual_tg_bot import text


def work_format_button():
    """Inline клавиатура для формата работы"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text=text.remote, callback_data=text.remote))
    inline_keyboard.add(InlineKeyboardButton(text=text.office, callback_data=text.office))
    inline_keyboard.add(InlineKeyboardButton(text=text.hybrid, callback_data=text.hybrid))
    inline_keyboard.add(InlineKeyboardButton(text=text.part_time, callback_data=text.part_time))
    inline_keyboard.add(InlineKeyboardButton(text=text.full_time, callback_data=text.full_time))
    inline_keyboard.add(InlineKeyboardButton(text=text.any_format, callback_data=text.any_format))
    inline_keyboard.add(InlineKeyboardButton(text=text.skip_continue, callback_data=text.skip_continue))
    return inline_keyboard

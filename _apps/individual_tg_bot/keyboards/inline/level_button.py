from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from _apps.individual_tg_bot import text


def level_button():
    """Уровень владения профессией"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text=text.trainee, callback_data=text.trainee))
    inline_keyboard.add(InlineKeyboardButton(text=text.junior, callback_data=text.junior))
    inline_keyboard.add(InlineKeyboardButton(text=text.middle, callback_data=text.middle))
    inline_keyboard.add(InlineKeyboardButton(text=text.senior, callback_data=text.senior))
    inline_keyboard.add(InlineKeyboardButton(text=text.tech_lead, callback_data=text.tech_lead))
    return inline_keyboard

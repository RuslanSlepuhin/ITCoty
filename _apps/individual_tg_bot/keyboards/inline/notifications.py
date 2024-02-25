from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from _apps.individual_tg_bot import text

notification_dict = {
    text.per_day_notification: text.per_day_notification,
    text.on_getting_notification: text.on_getting_notification,
    text.cancel_notification: text.cancel_notification,
}

def notification_button():
    """Клавиатура для уведомлений"""

    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    for button_text, button_callback in notification_dict.items():
        inline_keyboard.add(
            InlineKeyboardButton(text=button_text, callback_data=button_callback)
        )
    return inline_keyboard

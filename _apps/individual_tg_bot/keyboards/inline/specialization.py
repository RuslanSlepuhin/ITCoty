from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from _apps.individual_tg_bot import text


def design_button():
    """Кнопки специализации Design"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text=text.motion, callback_data=text.motion))
    inline_keyboard.add(InlineKeyboardButton(text=text.three_d, callback_data=text.three_d))
    inline_keyboard.add(InlineKeyboardButton(text=text.ux_ui, callback_data=text.ux_ui))
    inline_keyboard.add(InlineKeyboardButton(text=text.illustrator, callback_data=text.illustrator))
    inline_keyboard.add(InlineKeyboardButton(text=text.graphic, callback_data=text.graphic))
    inline_keyboard.add(InlineKeyboardButton(text=text.design, callback_data=text.design))

    return inline_keyboard


def backend_button():
    """Кнопки специализации backend"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text=text.one_c, callback_data=text.one_c))
    inline_keyboard.add(InlineKeyboardButton(text=text.java, callback_data=text.java))
    inline_keyboard.add(InlineKeyboardButton(text=text.python, callback_data=text.python))
    inline_keyboard.add(InlineKeyboardButton(text=text.php, callback_data=text.php))
    inline_keyboard.add(InlineKeyboardButton(text=text.c_plus_plus, callback_data=text.c_plus_plus))
    inline_keyboard.add(InlineKeyboardButton(text=text.c_sharp, callback_data=text.c_sharp))
    inline_keyboard.add(InlineKeyboardButton(text=text.dot_net, callback_data=text.dot_net))
    inline_keyboard.add(InlineKeyboardButton(text=text.golang, callback_data=text.golang))

    return inline_keyboard


def analyst_button():
    """Кнопки специализации analyst"""
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(InlineKeyboardButton(text=text.system_analyst, callback_data=text.system_analyst))
    inline_keyboard.add(InlineKeyboardButton(text=text.ba, callback_data=text.ba))

    return inline_keyboard


def mobile_button():
    """Кнопки специализации mobile"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text=text.ios, callback_data=text.ios))
    inline_keyboard.add(InlineKeyboardButton(text=text.android, callback_data=text.android))
    inline_keyboard.add(InlineKeyboardButton(text=text.flutter, callback_data=text.flutter))

    return inline_keyboard


def marketing_button():
    """Кнопки специализации marketing"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text=text.seo, callback_data=text.seo))
    inline_keyboard.add(InlineKeyboardButton(text=text.copywriter, callback_data=text.copywriter))
    inline_keyboard.add(InlineKeyboardButton(text=text.marketer, callback_data=text.marketer))
    inline_keyboard.add(InlineKeyboardButton(
        text=text.content_manager, callback_data=text.content_manager
    ))
    inline_keyboard.add(InlineKeyboardButton(text=text.media_buyer, callback_data=text.media_buyer))
    return inline_keyboard


def product_project_manager_button():
    """Кнопки специализации Product & Project manager"""
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_keyboard.add(InlineKeyboardButton(
        text=text.project_manager, callback_data=text.project_manager
    ))
    inline_keyboard.add(InlineKeyboardButton(
        text=text.product_manager, callback_data=text.product_manager
    ))
    return inline_keyboard


def sales_button():
    """Кнопки специализации Sales"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    return inline_keyboard


def dev_ops_button():
    """Кнопки специализации DevOps"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    return inline_keyboard


def frontend_button():
    """Кнопки специализации Frontend"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text=text.react, callback_data=text.react))
    inline_keyboard.add(InlineKeyboardButton(text=text.angular, callback_data=text.angular))
    inline_keyboard.add(InlineKeyboardButton(text=text.vue, callback_data=text.vue))
    return inline_keyboard


def support_button():
    """Кнопки специализации Support"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    return inline_keyboard


def fullstack_button():
    """Кнопки специализации Fullstack"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    return inline_keyboard


def hr_button():
    """Кнопки специализации HR"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    return inline_keyboard


def game_dev_button():
    """Кнопки специализации GameDev"""
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_keyboard.add(InlineKeyboardButton(text=text.unity, callback_data=text.unity))
    inline_keyboard.add(InlineKeyboardButton(text=text.game_designer, callback_data=text.game_designer))
    return inline_keyboard


def qa_button():
    """Кнопки специализации QA"""
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text=text.manual, callback_data=text.manual))
    inline_keyboard.add(InlineKeyboardButton(text=text.auto, callback_data=text.auto))
    return inline_keyboard

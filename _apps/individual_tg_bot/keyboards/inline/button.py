# from aiogram.utils.keyboard import InlineKeyboardBuilder
#
# # def get_inline_menu():
# #     """Inline клавиатура для главного меню"""
# #     inline_keyboard = InlineKeyboardMarkup(row_width=3)
# #     inline_keyboard.add(InlineKeyboardButton(text="Фильтр вакансий", callback_data="vacancy_filter")
# #     inline_keyboard.add(InlineKeyboardButton(text="Пройти опрос", callback_data="start_survey")
# #     inline_keyboard.add(
# #         text="Периодичность уведомлений", callback_data="notification"
# #     )
# #     inline_keyboard.add(InlineKeyboardButton(text="Профиль на сайте", url="https://itcoty.ru/")
# #     inline_keyboard(1, 1, 1)
# #     return inline_keyboard
#
#
# def get_inline_notification():
#     """Inline клавиатура для меню уведомлений"""
#     inline_keyboard = InlineKeyboardMarkup()
#     inline_keyboard.add(
#         text="По поступлению вакансий", callback_data="notification_on_receipt"
#     )
#     inline_keyboard.add(
#         text="Дайджестом за день", callback_data="notification_digest"
#     )
#     inline_keyboard.add(
#         text="Отменить получение уведомлений", callback_data="cancel_notification"
#     )
#     inline_keyboard(1, 1, 1)
#     return inline_keyboard

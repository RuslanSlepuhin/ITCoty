from aiogram import Bot
from aiogram.types import CallbackQuery


# @router.callback_query(F.data == "notification_on_receipt")
async def get_notification_on_receipt(query: CallbackQuery, bot: Bot) -> None:
    """Обработка notification_on_receipt callback"""
    pass


# @router.callback_query(F.data == "notification_digest")
async def get_notification_digest(query: CallbackQuery, bot: Bot) -> None:
    """Обработка notification_digest callback"""
    pass


# @router.callback_query(F.data == "cancel_notification")
async def get_cancel_notification(query: CallbackQuery, bot: Bot) -> None:
    """Обработка cancel_notification callback"""
    pass

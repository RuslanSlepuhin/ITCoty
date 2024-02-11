from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.keyboards.inline.main_menu import get_inline_menu


async def start_handler(msg: Message) -> None:
    """Обработка команды start"""

    await msg.answer(
        text.greet.format(name=msg.from_user.full_name), reply_markup=get_inline_menu()
    )


async def get_menu(msg: Message) -> None:
    """Обработка команды menu"""
    await msg.answer(text.menu, reply_markup=get_inline_menu())


async def cancel_handler(state: FSMContext) -> None:
    """Обработка команды cancel"""
    current_state = await state.get_state()
    if current_state is None:
        return


async def bot_info(message: Message):
    """Обработка команды info"""
    await message.answer(text=text.info)
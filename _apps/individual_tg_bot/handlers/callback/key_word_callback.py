from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from _apps.individual_tg_bot import text
from _apps.individual_tg_bot.service import show_summary


async def key_word_handler(message: Message, state:FSMContext, ) -> None:
    """Обработка ключевого слова"""

    await state.update_data(keyword=message.text)
    await message.answer(text=text.thanks_text, reply_markup=ReplyKeyboardRemove())
    data = await state.get_data()
    await show_summary(message=message, data=data)
from aiogram import Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from _apps.individual_tg_bot import text
#from _apps.individual_tg_bot.keyboards.inline.button import get_inline_notification
from _apps.individual_tg_bot.keyboards.inline.direction_buton import get_direction_button
from _apps.individual_tg_bot.states.states import User

#router = Router()


#@router.callback_query(F.data == text.vacancy_filter)
async def get_vacancy_filter(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка start_survey callback"""
    await state.set_state(User.name)
    await query.message.answer(text=text.direction, reply_markup=get_direction_button())


#@router.callback_query(F.data == text.start_survey)
async def get_start_survey(query: CallbackQuery, state: FSMContext) -> None:
    """Обработка start_survey callback"""
    await state.set_state(User.name)
    await query.message.answer(
        text=text.sent_first_question, reply_markup=ReplyKeyboardRemove()
    )


#@router.callback_query(F.data == text.notification)
# async def get_notification(query: CallbackQuery) -> None:
#     """Обработка notification callback"""
#     await query.message.answer(
#         text=text.get_notification, reply_markup=get_inline_notification()
#     )

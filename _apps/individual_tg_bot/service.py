import asyncio
from typing import Dict

from _apps.individual_tg_bot.db import AsyncPGDatabase
from _apps.individual_tg_bot.settings import DB_URL
from _apps.individual_tg_bot.text import suit_vacancies
from aiogram import Bot
from aiogram.types import Message

db = AsyncPGDatabase(DB_URL)


async def show_summary(message: Message, data: Dict) -> None:
    result = {
        "user_id": message.from_user.id,
        "direction": str(data.get("selected_direction", [])),
        "specialization": ", ".join(data.get("selected_specializations", [])),
        "level": ", ".join(data.get("selected_level", [])),
        "location": ", ".join(data.get("selected_location", [])),
        "work_format": ", ".join(data.get("selected_work_format", [])),
        "keyword": str(data.get("keyword", [])),
    }
    await db.create_table()
    await db.insert_into_data(**result)


async def period_get_vacancy_task_wrapper(bot: Bot):
    while True:
        result = await db.get_user_request()
        for rq in result:
            vacancies = await db.get_periodical_task_vacancies(
                direction=rq.get("direction"),
                specialization=rq.get("specialization"),
                level=rq.get("level"),
                location=rq.get("location"),
                work_format=rq.get("work_format"),
                keyword=rq.get("keyword"),
            )

            if vacancies:
                for vacancy in vacancies:
                    message = (suit_vacancies + f"{vacancy.get('title')} {vacancy.get('vacancy_url')}\n")
                    await bot.send_message(chat_id=rq.get("user_id"), text=message)
        await asyncio.sleep(1800)

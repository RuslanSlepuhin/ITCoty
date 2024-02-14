from typing import Any, Dict
import asyncio
from _apps.individual_tg_bot.db import AsyncPGDatabase
from _apps.individual_tg_bot.settings import DB_URL
from aiogram.types import Message

db = AsyncPGDatabase(DB_URL)
""" Колонки в таблице vacancies profession:direction, tags:specialization, level:level, job_type:work_format, keyword:body"""
async def main():
    result = await db.vacancy()
    print(result)
asyncio.run(main())

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
    await message.answer(text=str(result))
    await db.create_table()
    await db.insert_data(**result)

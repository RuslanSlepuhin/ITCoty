from aiogram.dispatcher.filters.state import State, StatesGroup


class User(StatesGroup):
    email = State()
    direction = State()
    specialization = State()
    location = State()
    salary_rate = State()
    work_format = State()
    keywords = State()
    CV_url = State()


# 1) направление, 2) специализация 3) локация 4) ур-нь зп 5) формат работы 6) ключевые слова 7) ссылкa на CV

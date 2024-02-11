
from aiogram import Dispatcher

from _apps.individual_tg_bot.handlers.callback.direction_callback import direction_design_callback, \
    direction_backend_callback, direction_analyst_callback, direction_mobile_callback, direction_marketing_callback, \
    direction_product_project_manager_callback, direction_sales_callback, direction_dev_ops_callback, \
    direction_frontend_callback, direction_support_callback, direction_fullstack_callback, direction_hr_callback, \
    direction_game_dev_callback, direction_qa_callback
from _apps.individual_tg_bot.handlers.callback.menu_callback import get_vacancy_filter

from _apps.individual_tg_bot.handlers.callback.specialization_callback.analyst_specialization import analyst_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.dev_ops_specialization import \
    dev_ops_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.fullstack_specialization import \
    fullstack_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.hr_specialization import \
    hr_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.mobile_specialization import \
    mobile_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.product_project_manager_specialization import \
    product_project_manager_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.qa_specialization import \
    qa_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.sales_specialization import \
    sales_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.support_specialization import \
    support_specialization_callback

from _apps.individual_tg_bot.handlers.routers.command_router import start_handler, cancel_handler, get_menu, bot_info

from _apps.individual_tg_bot.handlers.callback.specialization_callback.backend_specialization import backend_specialization_callback


from _apps.individual_tg_bot.handlers.callback.specialization_callback.frontend_specialization import  frontend_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.game_dev_specialization import game_dev_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.marketing_specialization import marketing_specialization_callback
from _apps.individual_tg_bot.handlers.callback.specialization_callback.design_specialization import design_specialization_callback
from _apps.individual_tg_bot.keyboards.inline.specializations.buttons import *


class Handlers:
    def __init__(self, dp:Dispatcher) -> None:
        self.dp = dp


    def register_message_handlers(self):
        """Регистрация message handlers"""
        self.dp.register_message_handler(start_handler, commands=['start'])
        self.dp.register_message_handler(cancel_handler, commands=['cancel'])
        self.dp.register_message_handler(get_menu, commands=['menu'])
        self.dp.register_message_handler(bot_info, commands=['info'])

    def register_direction_handlers(self):
        """Регистрация callback  direction handlers"""
        self.dp.register_callback_query_handler(get_vacancy_filter, text=text.vacancy_filter)
        self.dp.register_callback_query_handler(direction_design_callback, text=text.design)
        self.dp.register_callback_query_handler(direction_backend_callback, text=text.backend)
        self.dp.register_callback_query_handler(direction_analyst_callback, text=text.analyst)
        self.dp.register_callback_query_handler(direction_mobile_callback, text=text.mobile)
        self.dp.register_callback_query_handler(direction_marketing_callback, text=text.marketing)
        self.dp.register_callback_query_handler(direction_product_project_manager_callback,
                                           text=text.product_project_manager)
        self.dp.register_callback_query_handler(direction_sales_callback, text=text.sales)
        self.dp.register_callback_query_handler(direction_dev_ops_callback, text=text.dev_ops)
        self.dp.register_callback_query_handler(direction_frontend_callback, text=text.frontend)
        self.dp.register_callback_query_handler(direction_support_callback, text=text.support)
        self.dp.register_callback_query_handler(direction_fullstack_callback, text=text.fullstack)
        self.dp.register_callback_query_handler(direction_hr_callback, text=text.hr)
        self.dp.register_callback_query_handler(direction_game_dev_callback, text=text.game_dev)
        self.dp.register_callback_query_handler(direction_qa_callback, text=text.qa)

    def register_specializations_handlers(self):
        self.dp.register_callback_query_handler(design_specialization_callback,
                                                text=buttons_design)
        self.dp.register_callback_query_handler(analyst_specialization_callback,
                                                text=buttons_analyst)
        self.dp.register_callback_query_handler(backend_specialization_callback,
                                                text=buttons_backend)
        self.dp.register_callback_query_handler(dev_ops_specialization_callback,
                                                text=buttons_dev_ops)
        self.dp.register_callback_query_handler(frontend_specialization_callback,
                                                text=buttons_frontend)
        self.dp.register_callback_query_handler(fullstack_specialization_callback,
                                                text=buttons_fullstack)
        self.dp.register_callback_query_handler(game_dev_specialization_callback,
                                                text=buttons_game_dev)
        self.dp.register_callback_query_handler(hr_specialization_callback,
                                                text=buttons_hr)
        self.dp.register_callback_query_handler(marketing_specialization_callback,
                                                text=buttons_marketing)
        self.dp.register_callback_query_handler(mobile_specialization_callback,
                                                text=buttons_mobile)
        self.dp.register_callback_query_handler(product_project_manager_specialization_callback,
                                                text=buttons_product_project_manager)
        self.dp.register_callback_query_handler(qa_specialization_callback,
                                                text=buttons_qa)
        self.dp.register_callback_query_handler(sales_specialization_callback,
                                                text=buttons_sales)
        self.dp.register_callback_query_handler(support_specialization_callback,
                                                text=buttons_support)

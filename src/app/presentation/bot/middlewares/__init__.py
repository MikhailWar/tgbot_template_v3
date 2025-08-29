from aiogram import Dispatcher



def setup_middlewares(dp: Dispatcher):
    middleware_types = [

    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)
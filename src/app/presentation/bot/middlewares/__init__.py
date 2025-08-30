from aiogram import Dispatcher

from app.presentation.bot.middlewares.database import UserMiddleware


def setup_middlewares(dp: Dispatcher):
    middleware_types = [
        UserMiddleware()
    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)
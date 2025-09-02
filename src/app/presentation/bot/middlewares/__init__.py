from aiogram import Dispatcher
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore

from app.bootstrap.config import PROJECT_DIRECTORY
from app.infrastructure.managers.users import UserManager
from app.presentation.bot.middlewares.users import UserMiddleware


def setup_middlewares(dp: Dispatcher):
    i18n = I18nMiddleware(
        core=FluentRuntimeCore(
            path=PROJECT_DIRECTORY / "bootstrap/locales/{locale}/LC_MESSAGES",
        ),
        manager=UserManager(),
    )

    middleware_types = [
        UserMiddleware(
            i18n=i18n
        )
    ]

    for middleware_type in middleware_types:
        dp.update.outer_middleware(middleware_type)

    i18n.setup(dp)
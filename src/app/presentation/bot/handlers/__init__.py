"""Import all routers and add them to routers_list."""
from aiogram import Dispatcher

from .admin import admin_router
from .user import user_router

routers_list = [
    admin_router,
    user_router,
]




def setup_bot_controllers(dp: Dispatcher):
    dp.include_routers(
        admin_router,
        user_router,
    )



__all__ = [
    "routers_list",
]

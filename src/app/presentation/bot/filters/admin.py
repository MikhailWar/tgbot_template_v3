from aiogram.filters import BaseFilter
from aiogram.types import Message
from dishka import AsyncContainer
from dishka.integrations.aiogram import FromDishka
from sqlalchemy.ext.asyncio import AsyncSession

from app.bootstrap.config import Config


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message, dishka_container: AsyncContainer) -> bool:

        config = await dishka_container.get(Config)
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin

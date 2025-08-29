from aiogram.filters import BaseFilter
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka
from sqlalchemy.ext.asyncio import AsyncSession

from app.bootstrap.config import Config


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message, session: FromDishka[AsyncSession]) -> bool:

        print(session)


        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin

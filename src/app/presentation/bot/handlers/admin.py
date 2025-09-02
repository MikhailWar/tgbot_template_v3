from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_i18n import I18nContext

from src.app.presentation.bot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(m: Message, i18n: I18nContext):
    await m.answer(
        i18n.get('hello-admin')
    )

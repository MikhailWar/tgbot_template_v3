from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from app.application.usecases.bot_start import BotStartInteractor

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, interactor: FromDishka[BotStartInteractor]):
    response = await interactor()
    await message.reply(response)

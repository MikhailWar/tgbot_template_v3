from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext

from app.presentation.bot.keyboards.lang import get_lang_menu, LangCallback

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, i18n: I18nContext):
    await message.answer(
        text=i18n.get('hello', user=message.from_user.full_name),
    )


@user_router.message(Command('lang'))
async def cmd_lang(
        m: Message,
        i18n: I18nContext,
):
    await m.answer(
        text=i18n.get('cur-lang', language=i18n.locale),
        reply_markup=get_lang_menu(i18=i18n)
    )


@user_router.callback_query(
    LangCallback.filter()
)
async def set_lang_handler(
        c: CallbackQuery,
        i18n: I18nContext,
        callback_data: LangCallback
):
    if callback_data.locale != i18n.locale:
        await i18n.set_locale(locale=callback_data.locale)
        await c.message.edit_text(
            text=i18n.get('cur-lang', language=i18n.locale),
            reply_markup=get_lang_menu(i18=i18n)
        )

    await c.answer()

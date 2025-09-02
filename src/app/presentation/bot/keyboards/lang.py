from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext


class LangCallback(CallbackData, prefix="lang"):
    locale: str


def get_lang_menu(i18: I18nContext):

    markup = InlineKeyboardBuilder()
    markup.max_width = 1
    for locale in i18.core.available_locales:

        markup.add(
            InlineKeyboardButton(
                text=i18.core.get('lang_button', locale),
                callback_data=LangCallback(locale=locale).pack()
            )
        )

    return markup.as_markup()

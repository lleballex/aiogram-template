from aiogram.utils.i18n import gettext as _
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder 


def get_menu_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=_('/start'))
    return builder.as_markup(resize_keyboard=True)

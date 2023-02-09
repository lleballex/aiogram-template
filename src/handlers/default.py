from keyboards.main import get_menu_kb

from aiogram import Router
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _


default_router = Router()


@default_router.message()
async def default_handler(message: Message) -> None:
    await message.answer(_('What are you talking about?'),
                         reply_markup=get_menu_kb()) 

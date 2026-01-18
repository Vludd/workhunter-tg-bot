from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup

from app.templates.main_menu import show_main_menu
from app.api.user import get_user_data


async def start(msg: Message):
    user = msg.from_user
    if not user or not user.username:
        return
    
    username = user.username
    
    user = get_user_data()
    
    if not user.username:
        user.username = username
    
    card = show_main_menu(user)
    await msg.answer(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )

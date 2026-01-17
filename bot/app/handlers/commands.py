from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup

from app.templates.profile import profile_card


async def start(msg: Message):
    user = msg.from_user
    if not user or not user.username:
        return
    
    username = user.username
    
    card = profile_card(False, username)
    await msg.answer(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )

from aiogram.types import Message

from app.bot.services.commands import start_command


async def start(msg: Message):
    if msg.from_user is None:
        return
    
    text = start_command(msg.from_user.id)
    await msg.answer(text)

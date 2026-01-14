from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup

from app.bot.services.commands import start_command
from app.bot.services.messages import render_setup_profile, render_test_message
from app.bot.dto.template import CardTemplateDTO

async def start(msg: Message):
    if msg.from_user is None:
        return
    
    text = start_command(msg.from_user.id)
    await msg.answer(text)


async def render_template(msg: Message):
    if msg.from_user is None:
        return
    
    msg_template: CardTemplateDTO = render_test_message(msg.from_user.id)
    
    await msg.answer(
        text=msg_template.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=msg_template.buttons) if msg_template.buttons else None
    )
    
    for template in render_setup_profile():
        await msg.answer(
            text=template.text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=template.buttons) if template.buttons else None
        )
        

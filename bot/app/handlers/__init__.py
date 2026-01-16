from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import F

from app.handlers.commands import start
from app.handlers.messages import render_template

    
def register_handlers(dp: Dispatcher):
    dp.message.register(start, F.text == "/start")
    dp.message.register(render_template, F.text == "/test_render")

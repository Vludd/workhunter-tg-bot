from app.dependencies import bot, dp
from app.handlers import register_handlers

register_handlers(dp)


async def main():
    await dp.start_polling(bot)

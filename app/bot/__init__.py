from app.bot.dependencies import bot, dp
from app.bot.handlers import register_handlers

register_handlers(dp)


async def main():
    await dp.start_polling(bot)

from datetime import datetime

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup

from app.dto.template import CardTemplateDTO
from app.dto.vacancy import VacancyDTO
from app.templates.favorites import favorites_card
from app.api.vacancies import get_vacancies


async def render_favorites(msg: Message):
    card: CardTemplateDTO = favorites_card(get_vacancies())
    await msg.answer(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )

async def render_favorites_callback(cq: CallbackQuery):
    await cq.answer()
    
    if not isinstance(cq.message, Message):
        return
    
    card: CardTemplateDTO = favorites_card(get_vacancies())
    await cq.message.edit_text(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )

from datetime import datetime

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup

from app.dto.template import CardTemplateDTO
from app.dto.vacancy import VacancyDTO
from app.templates.favorites import favorites_card


def test_favorites_card() -> CardTemplateDTO:
    post_time_str = "2025-01-14 23:38:56+00:00"
    post_dt = datetime.fromisoformat(post_time_str)
    
    test_vacancies: VacancyDTO = VacancyDTO(
        id=1,
        title="Senior Python Developer (TEST CARD)",
        company="Tech Corp",
        salary="$120,000 - $150,000",
        location="Remote",
        skills=["Python", "Django", "REST", "Docker"],
        nuosances=[],
        source="LinkedIn",
        url="https://www.linkedin.com/jobs/view/1234567890/",
        posted_at=post_dt,
        score=95
    )
    
    msg_template: CardTemplateDTO = favorites_card([test_vacancies])
    return msg_template

async def render_favorites(msg: Message):
    card = test_favorites_card()
    await msg.answer(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )

async def render_favorites_callback(cq: CallbackQuery):
    await cq.answer()
    
    if not isinstance(cq.message, Message):
        return
    
    template: CardTemplateDTO = test_favorites_card()
    await cq.message.edit_text(
        text=template.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=template.buttons) if template.buttons else None
    )

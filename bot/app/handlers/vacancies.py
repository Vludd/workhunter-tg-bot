from datetime import datetime
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup

from app.dto.template import CardTemplateDTO
from app.dto.vacancy import VacancyDTO
from app.templates.profile import profile_card, get_setup_template
from app.templates.vacancy import vacancy_card


def test_vacancy_card() -> CardTemplateDTO:
    post_time_str = "2025-01-14 23:38:56+00:00"
    post_dt = datetime.fromisoformat(post_time_str)
    
    test_vacancy: VacancyDTO = VacancyDTO(
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
    
    msg_template: CardTemplateDTO = vacancy_card(test_vacancy)
    return msg_template

async def show_vacancies(msg: Message):
    card = test_vacancy_card()
    await msg.answer(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )


import asyncio
from datetime import datetime
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup

from app.api.user import get_user_data
from app.dto.template import CardTemplateDTO
from app.dto.vacancy import VacancyDTO
from app.templates.vacancy import searching_vacancies_card, vacancy_card


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

async def render_vacancies(msg: Message):
    user_data = get_user_data()
    
    card = searching_vacancies_card(user_data)
    sent_msg = await msg.answer(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )
    
    await asyncio.sleep(1.5) # test mock delay
    
    card = test_vacancy_card()
    await sent_msg.edit_text(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )

async def render_vacancies_callback(cq: CallbackQuery):
    await cq.answer()
    
    if not isinstance(cq.message, Message):
        return
    
    user_data = get_user_data()
    
    card = searching_vacancies_card(user_data)
    sent_msg = await cq.message.edit_text(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )
    
    await asyncio.sleep(1.5) # test mock delay
    
    card = test_vacancy_card()
    if isinstance(sent_msg, Message):
        await sent_msg.edit_text(
            text=card.text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
        )

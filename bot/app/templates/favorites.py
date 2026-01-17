from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.dto.vacancy import VacancyDTO
from app.dto.template import CardTemplateDTO
from datetime import datetime, timezone
from typing import Optional


def favorites_card(vacancies: list) -> CardTemplateDTO:
    count = len(vacancies)
    
    top_vacancies = []
    normal_vacancies = []
    nounces_vacancies = []
    
    text = f"⭐ Избранные вакансии — {count}:\n\n"
    
    text += f"🔥 Топ вакансии — {len(top_vacancies)}:\n"
    for v in top_vacancies:
        text += f"{v.title} — {v.hits or ''}%\n"
        
    text += f"👍 Подходят — {len(normal_vacancies)}:\n"
    for v in normal_vacancies:
        text += f"{v.title} — {v.hits or ''}%\n"
        
    text += f"👍 Подходят — {len(nounces_vacancies)}:\n"
    for v in nounces_vacancies:
        text += f"{v.title} — {v.hits or ''}%\n"
        
    buttons = [
        [InlineKeyboardButton(text="👀 Просмотреть", callback_data=f"favorites:check")],
        [InlineKeyboardButton(text="↩️ Назад", callback_data=f"favorites:back")],
    ]

    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template

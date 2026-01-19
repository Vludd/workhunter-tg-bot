from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.dto.profile import ProfileDTO
from app.dto.vacancy import VacancyDTO
from app.dto.template import CardTemplateDTO
from datetime import datetime, timezone
from typing import Optional


# post_time_str = "2026-01-13 02:14:56+00:00"

def posted_time_ago(posted_at: datetime) -> str:
    now = datetime.now(timezone.utc)
    
    delta = now - posted_at
    seconds = int(delta.total_seconds())

    minutes = seconds // 60
    hours = minutes // 60
    days =  hours // 24
    weeks = days // 14
    month = days // 30
    years = month // 12
    
    if years > 0:
        posted_at_text = f"{years} г. назад"
    elif month > 0:
        posted_at_text = f"{month} мес. назад"
    elif weeks > 0:
        posted_at_text = f"{weeks} нед. назад"
    elif days > 0:
        posted_at_text = f"{days} дн. назад"
    elif hours > 0:
        posted_at_text = f"{hours} ч. назад"
    elif minutes > 0:
        posted_at_text = f"{minutes} мин. назад"
    else:
        posted_at_text = f"{seconds} сек. назад"
    
    return posted_at_text
    

def vacancy_card(vacancy: VacancyDTO) -> CardTemplateDTO:
    posted_ago = posted_time_ago(vacancy.posted_at) if vacancy.posted_at else None
    
    text = f"🧑‍💻 *{vacancy.title}*\n"
    text += f"🏢 {vacancy.company}\n\n"
    text += f"💰 {vacancy.salary}\n"
    text += f"🌍 {vacancy.location}\n"
    text += f"🧠 Совпадение: {vacancy.score}%{'🔥' if vacancy.score >= 80 else '👍' if vacancy.score >= 60 else '⚠️'}\n\n"
    text += f"📌 Совпало: \n{', '.join(vacancy.skills)}\n\n"
    text += f"⚠️ Нюансы: \n{', '.join(vacancy.nuosances)}\n\n" if vacancy.nuosances else ""
    text += f"🕒 Опубликовано: {posted_ago}\n" if vacancy.posted_at and posted_ago else ""
    text += f"🔗 Источник: {vacancy.source}\n" if vacancy.source else ""
    
    buttons = [
        [
            InlineKeyboardButton(text="💾 Сохранить", callback_data=f"fav:{vacancy.id}"),
            InlineKeyboardButton(text="❌ Пропустить", callback_data=f"skip:{vacancy.id}")
        ]
    ]
    
    if vacancy.url:
        buttons.append([InlineKeyboardButton(text="🔗 Подробнее", url=vacancy.url)])
        
    buttons.append([InlineKeyboardButton(text="↩️ Назад", callback_data=f"vacancy_item:back")])
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template


def searching_vacancies_card(user_data: ProfileDTO) -> CardTemplateDTO:
    text = (
        "🔍 Ищу подходящие вакансии под твой профиль...\n\n"

        f"🧠 Навыки: {', '.join(map(str, user_data.skills)) if user_data.skills else '—'}\n"
        f"💼 Уровень: {user_data.experience or '—'}\n"
        f"🌍 Локация: {user_data.location or '—'}\n\n"

        "⏳ _Это занимает 2–5 секунд_"
    )
    
    template = CardTemplateDTO(
        text=text,
        buttons=[]
    )
    
    return template

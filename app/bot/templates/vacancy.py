from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.bot.dto.vacancy import VacancyDTO
from app.bot.dto.template import CardTemplateDTO
from datetime import datetime, timezone
from typing import Optional


# post_time_str = "2026-01-13 02:14:56+00:00"

def posted_time_ago(posted_at: datetime) -> str:
    now = datetime.now(timezone.utc)
    
    delta = now - posted_at
    seconds = int(delta.total_seconds())

    minutes = seconds // 60
    hours = seconds // 3600
    
    if hours > 0:
        posted_at_text = f"{hours} час(-ов) назад"
    elif minutes > 0:
        posted_at_text = f"{minutes} минут(-ы) назад"
    else:
        posted_at_text = f"{seconds} секунд(-ы) назад"
    
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
        [InlineKeyboardButton(text="⭐ В избранное", callback_data=f"fav:{vacancy.id}"),
         InlineKeyboardButton(text="❌ Пропустить", callback_data=f"skip:{vacancy.id}")],
    ]
    
    if vacancy.url:
        buttons.append([InlineKeyboardButton(text="🔗 Подробнее", url=vacancy.url)])
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template

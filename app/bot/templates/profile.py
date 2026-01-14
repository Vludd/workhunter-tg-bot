from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.bot.dto.vacancy import VacancyDTO
from app.bot.dto.template import CardTemplateDTO
from datetime import datetime, timezone
from typing import Optional



def setup_profile_start(username: str, stats: dict) -> CardTemplateDTO:
    vacancies_count: int = stats.get("vacancies_count", 0)
    favorites_count: int = stats.get("favorites_count", 0)
    is_following: bool = stats.get("is_following", False)
    vacancy_series: bool = stats.get("vacancy_series", 0)
    
    text = f"С возвращением, {username} 👋\n\n"
    text += f"🔍 Новых вакансий сегодня: {vacancies_count}\n"
    text += f"⭐ В избранном: {favorites_count}\n"
    text += f"📣 Авто-отслеживание: {'Включено ✅' if is_following else 'Отключено ❌'}\n\n"
    text += f"🔥 _{vacancy_series} вакансий подряд: Ты сегодня в ударе!_\n\n" if vacancy_series >= 5 else ""
    text += f"Выберите действие:\n\n"
    
    buttons = [
        [InlineKeyboardButton(text="🚀 Начать настройку", callback_data=f"setup:start"),
         InlineKeyboardButton(text="⏭ Пропустить (позже)", callback_data=f"setup:skip")],
    ]

    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.dto.vacancy import VacancyDTO
from app.dto.template import CardTemplateDTO
from datetime import datetime, timezone
from typing import Optional


def setup_profile_start() -> CardTemplateDTO:
    text = f"👋 Привет!\n"
    text += f"Я помогаю находить *подходящие вакансии в Telegram* и отслеживать новые в реальном времени.\n\n"
    text += f"Чтобы рекомендации были точными, давай быстро настроим профиль.\nЭто займёт *2–3 минуты*.\n\n"
    
    buttons = [
        [InlineKeyboardButton(text="🚀 Начать настройку", callback_data=f"setup:start"),
         InlineKeyboardButton(text="⏭ Пропустить (позже)", callback_data=f"setup:skip")],
    ]

    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template

def setup_profile_1() -> CardTemplateDTO:
    text = "⚙️ Настройка профиля (1/4)\n\n"
    text += "🧠 Укажи свои ключевые навыки через запятую. Например: `python, fastapi, redis`."
    
    buttons = []
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template

def setup_profile_2() -> CardTemplateDTO:
    text = "⚙️ Настройка профиля (2/4)\n\n"
    text += "💼 Укажи уровень опыта"
    
    buttons = [
        [
            InlineKeyboardButton(text="🟢 Junior (0–1)", callback_data=f"level:junior"),
            InlineKeyboardButton(text="🔵 Middle (1–3)", callback_data=f"level:middle"),
            InlineKeyboardButton(text="🟣 Senior (3+)", callback_data=f"level:senior"),
        ],
        [InlineKeyboardButton(text="⚪ Не важно", callback_data=f"level:any")],
    ]
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template

def setup_profile_3() -> CardTemplateDTO:
    text = "⚙️ Настройка профиля (3/4)\n\n"
    text += "🌍 Где ты ищешь работу?"
    
    buttons = [
        [
            InlineKeyboardButton(text="🇰🇿 Казахстан", callback_data=f"contry:kz"),
            InlineKeyboardButton(text="🇷🇺 Россия", callback_data=f"country:ru"),
        ],
        [InlineKeyboardButton(text="🌐 Весь мир", callback_data=f"country:world")]
    ]
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template

def setup_profile_4() -> CardTemplateDTO:
    wallet_course = "1$ = 78,07 руб = 510,17 тг"
    
    text = "⚙️ Настройка профиля (4/4)\n\n"
    text += "💰 Укажи желаемую зарплату."
    text += 'Можно текстом: `"от 2500$"`.'
    text += f'Текущий курс: `{wallet_course}`.'
    
    buttons = [
        [
            InlineKeyboardButton(text="До 2000$", callback_data=f"payment:2k"),
            InlineKeyboardButton(text="2000–3000$", callback_data=f"payment:2_3k"),
            InlineKeyboardButton(text="3000–5000$", callback_data=f"payment:3_5k"),
            InlineKeyboardButton(text="5000$+", callback_data=f"payment:5k"),
        ],
        [InlineKeyboardButton(text="⚪ Не важно", callback_data=f"payment:none")]
    ]
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template

def setup_profile_ready() -> CardTemplateDTO:
    text = "✅ Профиль готов!\n\n"
    text += "Я буду присылать тебе *подходящие вакансии* и отслеживать новые в реальном времени."
    
    buttons = [
        [
            InlineKeyboardButton(text="🔍 Показать вакансии", callback_data=f"ready_profile:vacancies"),
            InlineKeyboardButton(text="⚙️ Изменить профиль", callback_data=f"ready_profile:change_profile"),
        ],
        [InlineKeyboardButton(text="📣 Включить авто-отслеживание", callback_data=f"ready_profile:following"),]
    ]
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons
    )
    
    return template
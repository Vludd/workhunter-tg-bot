from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.dto.profile import ProfileStep
from app.dto.vacancy import VacancyDTO
from app.dto.template import CardTemplateDTO
from datetime import datetime, timezone
from typing import Optional
from app.fsm.profile import ProfileSetup
from aiogram.fsm.context import FSMContext


def profile_card(profile_completed: bool, username: Optional[str], stats: dict = {}) -> CardTemplateDTO:
    if profile_completed:
        return completed_profile_template(username, stats)
    
    return uncompleted_profile_template()

def completed_profile_template(username: Optional[str], stats: dict = {}) -> CardTemplateDTO:
    vacancies_count: int = stats.get("vacancies_count", 0)
    favorites_count: int = stats.get("favorites_count", 0)
    is_following: bool = stats.get("is_following", False)
    vacancy_series: bool = stats.get("vacancy_series", 0)
    
    text = f"С возвращением, {username} 👋\n\n" if username else "С возвращением 👋\n\n"
    
    text += f"🔍 Новых вакансий сегодня: {vacancies_count}\n"
    text += f"⭐ В избранном: {favorites_count}\n"
    text += f"📣 Авто-отслеживание: {'Включено ✅' if is_following else 'Отключено ❌'}\n\n"
    
    text += f"🔥 _{vacancy_series} вакансий подряд: Ты сегодня в ударе!_\n\n" if vacancy_series >= 5 else ""
    
    text += f"Выберите действие:\n\n"
    
    buttons = [
        [InlineKeyboardButton(text="🔍 Показать вакансии", callback_data=f"profile:vacancies")],
        [
            InlineKeyboardButton(text="⭐ Избранное", callback_data=f"profile:favorites"),
            InlineKeyboardButton(text="📊 Срез рынка", callback_data=f"profile:market"),
        ],
        [
            InlineKeyboardButton(text="🏆 Достижения", callback_data=f"profile:achievements"),
            InlineKeyboardButton(text="⚙️ Настройка профиля", callback_data=f"profile:settings"),
        ]
    ]

    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template
    
def uncompleted_profile_template() -> CardTemplateDTO:
    text = f"👋 Привет!\n"
    text += f"Я помогаю находить *подходящие вакансии в Telegram* и отслеживать новые в реальном времени.\n\n"
    text += f"Чтобы рекомендации были точными, давай быстро настроим профиль.\nЭто займёт *2–3 минуты*.\n\n"
    
    buttons = [
        [InlineKeyboardButton(text="🚀 Начать настройку", callback_data=f"profile_setup:start"),
         InlineKeyboardButton(text="⏭ Пропустить (позже)", callback_data=f"profile_setup:skip")],
    ]

    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template

def setup_profile_1() -> CardTemplateDTO:
    text = "⚙️ Настройка профиля (1/4)\n\n"
    text += "🧠 Укажи свои ключевые навыки через запятую. Например: `python, fastapi, redis`."
    
    buttons = []
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
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
        buttons=buttons if buttons else None
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
        buttons=buttons if buttons else None
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
        buttons=buttons if buttons else None
    )
    
    return template

def finished_profile_template() -> CardTemplateDTO:
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
        buttons=buttons if buttons else None
    )
    
    return template

PROFILE_SETUP_FLOW = [
    ProfileStep(ProfileSetup.skills, setup_profile_1),
    ProfileStep(ProfileSetup.experience, setup_profile_2),
    ProfileStep(ProfileSetup.location, setup_profile_3),
    ProfileStep(ProfileSetup.salary, setup_profile_4),
]

async def get_setup_template(state: FSMContext) -> CardTemplateDTO:
    current = await state.get_state()

    for step in PROFILE_SETUP_FLOW:
        if step.state == current:
            return step.template()

    return uncompleted_profile_template()

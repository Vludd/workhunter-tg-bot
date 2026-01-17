from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.dto.profile import ProfileSetupStep
from app.dto.vacancy import VacancyDTO
from app.dto.template import CardTemplateDTO
from datetime import datetime, timezone
from typing import Optional
from app.fsm.profile import ProfileSetup
from aiogram.fsm.context import FSMContext


def show_main_menu(profile_completed: bool, username: Optional[str], stats: dict = {}) -> CardTemplateDTO:
    if profile_completed:
        return main_menu(username, stats)
    
    return welcome_card()

def main_menu(username: Optional[str], stats: dict = {}) -> CardTemplateDTO:
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
        [InlineKeyboardButton(text="🔍 К вакансиям", callback_data=f"main_menu:vacancies")],
        [InlineKeyboardButton(text="📊 Срез рынка", callback_data=f"main_menu:market")],
        [
            InlineKeyboardButton(text="⭐ Избранное", callback_data=f"main_menu:favorites"),
            InlineKeyboardButton(text="🏆 Достижения", callback_data=f"main_menu:achievements")
        ],
        [InlineKeyboardButton(text="⚙️ Настройки", callback_data=f"main_menu:settings")]
    ]

    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template
    
def welcome_card() -> CardTemplateDTO:
    text = f"👋 Привет!\n"
    text += f"Я помогаю находить *подходящие вакансии в Telegram* и отслеживать новые в реальном времени.\n\n"
    text += f"Чтобы рекомендации были точными, давай быстро настроим профиль.\nЭто займёт *2–3 минуты*.\n\n"
    
    buttons = [
        [InlineKeyboardButton(text="🚀 Начать настройку", callback_data=f"profile_setup:start")],
        [InlineKeyboardButton(text="⏩ Пропустить", callback_data=f"profile_setup:skip")],
    ]

    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template

def setup_skills_card() -> CardTemplateDTO:
    text = "⚙️ Настройка профиля (1/4)\n\n"
    text += "🧠 Укажи свои ключевые навыки через запятую. Например: `python, fastapi, redis`:"
    
    buttons = []
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template

def setup_experience_card() -> CardTemplateDTO:
    text = (
        "⚙️ Настройка профиля (2/4)\n\n"
        "💼 Укажи свой уровень опыта\n"
        "_Сколько лет коммерческой разработки?_ \n\n"
        "Под опытом имеется в виду:\n"
        "• работа над коммерческими проектами\n"
        "• аутсорс / фриланс\n"
        "• участие в стартапах\n\n"
        "Pet-проекты не учитываются.\n"
        "Если опыта немного, но есть собственные проекты в проде — выбирай уровень, который считаешь честным."
    )
    
    buttons = [
        [InlineKeyboardButton(text="🟢 Junior (0–1)", callback_data=f"profile_experience:junior")],
        [InlineKeyboardButton(text="🔵 Middle (1–3)", callback_data=f"profile_experience:middle")],
        [InlineKeyboardButton(text="🟣 Senior (3+)", callback_data=f"profile_experience:senior")],
        [InlineKeyboardButton(text="⚪ Не важно", callback_data=f"profile_experience:any")],
    ]
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template

def setup_location_card() -> CardTemplateDTO:
    text = "⚙️ Настройка профиля (3/4)\n\n"
    text += "🌍 Где ты ищешь работу?"
    
    buttons = [
        [InlineKeyboardButton(text="🇰🇿 Казахстан", callback_data=f"profile_location:kz")],
        [InlineKeyboardButton(text="🇷🇺 Россия", callback_data=f"profile_location:ru")],
        [InlineKeyboardButton(text="🌎 Весь мир", callback_data=f"profile_location:any")],
        [InlineKeyboardButton(text="🌐 Remote", callback_data=f"profile_location:remote")],
    ]
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template

def setup_salary_card() -> CardTemplateDTO:
    wallet_course = "1$ = 78,07 руб = 510,17 тг"
    
    text = "⚙️ Настройка профиля (4/4)\n\n"
    text += "💰 Укажи желаемую зарплату."
    text += 'Можно указать текстом, например: `"от 2500$"`.'
    text += f'Текущий курс: `{wallet_course}`.'
    
    buttons = [
        [InlineKeyboardButton(text="💼 До 2000$", callback_data=f"profile_salary:2k")],
        [InlineKeyboardButton(text="💵 2000–3000$", callback_data=f"profile_salary:2_3k")],
        [InlineKeyboardButton(text="💰 3000–5000$", callback_data=f"profile_salary:3_5k")],
        [InlineKeyboardButton(text="🏆 5000$+", callback_data=f"profile_salary:5k")],
        [InlineKeyboardButton(text="— Не важно", callback_data=f"profile_salary:none")]
    ]
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template

def finished_profile_card() -> CardTemplateDTO:
    text = "✅ Профиль готов!\n\n"
    text += "Я буду присылать тебе *подходящие вакансии* и отслеживать новые в реальном времени. Не забудь включить авто-отслеживание!"
    
    buttons = [
        [InlineKeyboardButton(text="🔍 К вакансиям", callback_data=f"finished_profile:vacancies")],
        [InlineKeyboardButton(text="⚙️ Изменить профиль", callback_data=f"finished_profile:change_profile")],
        [InlineKeyboardButton(text="📣 Включить авто-отслеживание", callback_data=f"finished_profile:following"),]
    ]
    
    template = CardTemplateDTO(
        text=text,
        buttons=buttons if buttons else None
    )
    
    return template

PROFILE_SETUP_FLOW = [
    ProfileSetupStep(ProfileSetup.skills, setup_skills_card),
    ProfileSetupStep(ProfileSetup.experience, setup_experience_card),
    ProfileSetupStep(ProfileSetup.location, setup_location_card),
    ProfileSetupStep(ProfileSetup.salary, setup_salary_card),
]

async def get_setup_template(state: FSMContext) -> CardTemplateDTO:
    current = await state.get_state()

    for step in PROFILE_SETUP_FLOW:
        if step.state == current:
            return step.template()

    return welcome_card()

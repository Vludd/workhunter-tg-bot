from aiogram import Dispatcher, F

from app.fsm.profile import ProfileSetup
from app.handlers.commands import start
from app.handlers.profile import set_skills, show_profile, show_vacancies_callback, start_callback
from app.handlers.vacancies import show_vacancies

    
def register_handlers(dp: Dispatcher):
    dp.message.register(start, F.text == "/start")
    dp.message.register(show_profile, F.text == "/profile")
    dp.message.register(show_vacancies, F.text == "/vacancies")
    
    dp.message.register(set_skills, ProfileSetup.skills, F.text.len() > 1)
    dp.callback_query.register(start_callback, F.data == "profile_setup:start")
    dp.callback_query.register(show_vacancies_callback, F.data == "profile:vacancies")

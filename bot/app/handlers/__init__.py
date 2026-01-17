from aiogram import Dispatcher, F

from app.fsm.profile import ProfileSetup
from app.handlers.commands import start
from app.handlers.main_menu import (
    set_skills, render_main_menu, 
    render_vacancies_callback, start_callback, render_main_menu_callback
)

from app.handlers.vacancies import render_vacancies
from app.handlers.favorites import render_favorites, render_favorites_callback

    
def register_handlers(dp: Dispatcher):
    dp.message.register(start, F.text == "/start")
    dp.message.register(render_main_menu, F.text == "/menu")
    dp.message.register(render_vacancies, F.text == "/vacancies")
    dp.message.register(render_favorites, F.text == "/favorites")
    
    dp.message.register(set_skills, ProfileSetup.skills, F.text.len() > 1)
    dp.callback_query.register(start_callback, F.data == "profile_setup:start")
    
    dp.callback_query.register(render_vacancies_callback, F.data == "main_menu:vacancies")
    dp.callback_query.register(render_favorites_callback, F.data == "main_menu:favorites")
    
    dp.callback_query.register(render_main_menu_callback, F.data == "favorites:back")
    dp.callback_query.register(render_main_menu_callback, F.data == "vacancy_item:back")
    dp.callback_query.register(render_main_menu_callback, F.data == "profile_setup:skip")
    

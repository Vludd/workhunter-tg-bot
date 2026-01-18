from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup

from app.api.user import get_user_data
from app.dto.template import CardTemplateDTO
from app.fsm.profile import ProfileSetup
from app.handlers.vacancies import test_vacancy_card
from app.templates.main_menu import show_main_menu, get_setup_template


async def render_main_menu(msg: Message):
    user = msg.from_user
    if not user or not user.username:
        return
    
    username = user.username
    
    user = get_user_data()
    
    if not user.username:
        user.username = username
    
    card = show_main_menu(user)
    await msg.answer(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )
    
async def set_skills(msg: Message, state: FSMContext):
    skills = msg.text
    print(f"Got skills: {skills}")
    
    await state.set_state(ProfileSetup.experience)
    
    msg_template: CardTemplateDTO = await get_setup_template(state)
    await msg.reply(
        text=msg_template.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=msg_template.buttons) if msg_template.buttons else None
    )
    
async def render_main_menu_callback(cq: CallbackQuery):
    await cq.answer()
    
    if not isinstance(cq.message, Message):
        return
    
    user = cq.message.from_user
    if not user or not user.username:
        return
    
    user = get_user_data()
    
    card = show_main_menu(user)
    await cq.message.edit_text(
        text=card.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=card.buttons) if card.buttons else None
    )

async def start_callback(cq: CallbackQuery, state: FSMContext):
    await cq.answer()
    
    if not isinstance(cq.message, Message):
        return
    
    await state.set_state(ProfileSetup.skills)
    
    template: CardTemplateDTO = await get_setup_template(state)
    await cq.message.edit_text(
        text=template.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=template.buttons) if template.buttons else None
    )

async def render_vacancies_callback(cq: CallbackQuery):
    await cq.answer()
    
    if not isinstance(cq.message, Message):
        return
    
    template: CardTemplateDTO = test_vacancy_card()
    await cq.message.edit_text(
        text=template.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=template.buttons) if template.buttons else None
    )
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup

from app.dto.template import CardTemplateDTO
from app.fsm.profile import ProfileSetup
from app.handlers.vacancies import test_vacancy_card
from app.templates.profile import profile_card, get_setup_template


async def show_profile(msg: Message):
    user = msg.from_user
    if not user or not user.username:
        return
    
    username = user.username
    
    card = profile_card(True, username)
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

async def show_vacancies_callback(cq: CallbackQuery):
    await cq.answer()
    
    if not isinstance(cq.message, Message):
        return
    
    template: CardTemplateDTO = test_vacancy_card()
    await cq.message.edit_text(
        text=template.text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=template.buttons) if template.buttons else None
    )
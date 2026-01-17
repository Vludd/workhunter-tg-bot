from aiogram.fsm.state import StatesGroup, State


class ProfileSetup(StatesGroup):
    skills = State()
    experience = State()
    location = State()
    salary = State()

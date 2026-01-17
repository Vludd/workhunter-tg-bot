from dataclasses import dataclass
from aiogram.fsm.state import State
from typing import List, Optional
from typing import Callable

from app.dto.template import CardTemplateDTO

@dataclass
class ProfileFilterDTO:
    skills: List[Optional[str]]
    level: Optional[str]
    location: Optional[str]
    payment: int

@dataclass
class ProfileInfoDTO:
    new_vacancies: int
    favorite_count: int
    following: bool

@dataclass(frozen=True)
class ProfileSetupStep:
    state: State
    template: Callable[[], CardTemplateDTO]

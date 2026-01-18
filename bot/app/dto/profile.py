from dataclasses import dataclass
from aiogram.fsm.state import State
from typing import List, Optional
from typing import Callable

from app.dto.template import CardTemplateDTO

@dataclass
class ProfileDTO:
    id: Optional[int]
    username: Optional[str]
    
    skills: List[Optional[str]]
    experience: Optional[str]
    location: Optional[str]
    salary: Optional[str]
    
    completed: bool = False

@dataclass
class ProfileInfoDTO:
    new_vacancies: int
    favorite_count: int
    following: bool

@dataclass(frozen=True)
class ProfileSetupStep:
    state: State
    template: Callable[[], CardTemplateDTO]

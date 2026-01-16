from dataclasses import dataclass
from typing import List, Optional


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

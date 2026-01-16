from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class VacancyDTO:
    id: int
    title: str
    company: str
    salary: str  # можно позже сделать int / диапазон, если нужно
    location: str
    score: float  # совпадение с профилем в процентах
    skills: List[str]
    nuosances: List[str]
    description: Optional[str] = None
    contact: Optional[str] = None  # ссылка или контакт HR
    source: Optional[str] = None  # канал/сайт
    url: Optional[str] = None  # ссылка на сообщение вакансии
    posted_at: Optional[datetime] = None  # дата публикации вакансии "2026-01-13 02:14:56+00:00"

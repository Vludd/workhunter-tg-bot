from app.utils import get_vacancies
from app.templates.vacancy import vacancy_card
from app.templates.start import setup_profile_start, setup_profile_1, setup_profile_2, setup_profile_3, setup_profile_ready
from app.dto.vacancy import VacancyDTO
from app.dto.template import CardTemplateDTO
from datetime import datetime, timezone, timedelta


def render_test_message(user_id: int) -> CardTemplateDTO:
    post_time_str = "2026-01-12 21:14:56+00:00"
    post_dt = datetime.fromisoformat(post_time_str)
    
    test_vacancy: VacancyDTO = VacancyDTO(
        id=1,
        title="Senior Python Developer",
        company="Tech Corp",
        salary="$120,000 - $150,000",
        location="Remote",
        skills=["Python", "Django", "REST", "Docker"],
        nuosances=[],
        source="LinkedIn",
        url="https://www.linkedin.com/jobs/view/1234567890/",
        posted_at=post_dt,
        score=95
    )
    
    msg_template: CardTemplateDTO = vacancy_card(test_vacancy)
    return msg_template

def render_setup_profile() -> list[CardTemplateDTO]:
    templates = []
    
    templates.append(setup_profile_start())
    templates.append(setup_profile_1())
    templates.append(setup_profile_2())
    templates.append(setup_profile_3())
    templates.append(setup_profile_ready())
    
    return templates
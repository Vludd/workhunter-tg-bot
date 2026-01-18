from datetime import datetime
from app.dto.vacancy import VacancyDTO


def get_mock_vacancy() -> VacancyDTO:
    post_time_str = "2025-01-14 23:38:56+00:00"
    post_dt = datetime.fromisoformat(post_time_str)
    
    vacancy_data: VacancyDTO = VacancyDTO(
        id=1,
        title="Senior Python Developer (TEST CARD)",
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
    
    return vacancy_data

def get_vacancies() -> list[VacancyDTO]:
    vacancies: list[VacancyDTO] = []
    
    vacancies.append(get_mock_vacancy())
    
    return vacancies

from app.utils import get_vacancies


def start_command(user_id: int) -> str:
    vacancies = get_vacancies(user_id)
    text = "\n\n".join([f"{v['title']} @ {v['company']}\n{v['url']}" for v in vacancies])
    return text

from datetime import datetime
from app.dto.profile import ProfileDTO


def get_mock_profile() -> ProfileDTO:
    profile_data: ProfileDTO = ProfileDTO(
        id=1,
        username=None,
        skills=["Python", "FastAPI", "Redis", "Docker"],
        experience="middle",
        location="Remote",
        salary="2000+",
        completed=True
    )
    
    return profile_data

def get_user_data() -> ProfileDTO:
    return get_mock_profile()

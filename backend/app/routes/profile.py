from fastapi import APIRouter
from typing import Optional


router = APIRouter()

profile = {
    "skills": [], 
    "experience": None, 
    "location": None,
    "salary": None
}

setup_step = 0

@router.get("")
async def get_profile(user_id: int):
    return {"profile": profile, "step": setup_step}

@router.post("/setup/start")
async def start_profile_setup(user_id: int):
    global setup_step
    setup_step = 1
    return {"status": "setup started"}
    
@router.post("/setup/skills")
async def set_profile_skills(user_id: int, skills: list[str]):
    global setup_step
    setup_step = 2
    profile["skills"] = skills
    return {"status": "skills updated"}

@router.post("/setup/experience")
async def set_profile_experience(user_id: int, experience: str):
    global setup_step
    setup_step = 3
    profile["experience"] = experience
    return {"status": "experience level updated"}

@router.post("/setup/location")
async def set_profile_location(user_id: int, location: str):
    global setup_step
    setup_step = 4
    profile["location"] = location
    return {"status": "location updated"}

@router.post("/setup/salary")
async def set_profile_salary(user_id: int, salary: str):
    global setup_step
    setup_step = 0
    profile["salary"] = salary
    return {"status": "profile setup finished"}

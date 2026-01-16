from fastapi import APIRouter
from typing import Optional


router = APIRouter()

# @router.post("/refresh")
# async def refresh_data():
#     return {"status": "Data refreshed successfully"}

# @router.post("/send")
# async def send_data():
#     return {"status": "Data sent successfully"}

# @router.post("/filter")
# def set_filter(from_date: str, to_date: str):
#     filter_config["from_date"] = from_date
#     filter_config["to_date"] = to_date
#     return {"status": "filter updated", "filter": filter_config}

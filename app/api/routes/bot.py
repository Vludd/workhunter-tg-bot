from fastapi import APIRouter
from typing import Optional


router = APIRouter()

# filter_config: dict[str, Optional[str]] = {
#     "from_date": None,
#     "to_date": None,
# }

# @router.post("/refresh")
# async def refresh_data():
#     return {"status": "Data refreshed successfully"}

# @router.post("/filter")
# def set_filter(from_date: str, to_date: str):
#     filter_config["from_date"] = from_date
#     filter_config["to_date"] = to_date
#     return {"status": "filter updated", "filter": filter_config}

# @router.post("/follow")
# def toggle_follow(enable: bool):
#     filter_config["real_time"] = enable
#     return {"status": "real-time tracking", "enabled": enable}

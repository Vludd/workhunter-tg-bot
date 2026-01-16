from fastapi import APIRouter
from app.routes.bot import router as bot_router
from app.routes.mtproto import router as mtproto_router


router = APIRouter()
router.include_router(mtproto_router, prefix="/mtproto", tags=["MTProto"])
router.include_router(bot_router, prefix="/bot", tags=["Bot"])

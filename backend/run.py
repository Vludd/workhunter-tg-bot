import uvicorn
import logging

from app.config import APP_HOST, APP_PORT, APP_DEBUG
from app.core.logger import setup_logger


if __name__ == "__main__":
    setup_logger(logging.DEBUG if APP_DEBUG else logging.INFO)
    uvicorn.run("app.main:app", host=APP_HOST, port=APP_PORT, reload=APP_DEBUG)

from os import getenv
from dotenv import load_dotenv

load_dotenv()

APP_HOST: str = getenv("APP_HOST", "localhost")
APP_PORT: int = int(getenv('APP_PORT', "8000"))
APP_DEBUG: bool = getenv('APP_DEBUG', "False").lower() == "true"

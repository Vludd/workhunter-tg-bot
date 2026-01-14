from os import getenv
from dotenv import load_dotenv

BOT_TOKEN: str = getenv('BOT_TOKEN', "")
OWNER_ID: int = int(getenv('OWNER_ID', "0"))

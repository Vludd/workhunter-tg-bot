from dataclasses import dataclass
from typing import List, Optional
from aiogram.types import InlineKeyboardButton

@dataclass
class CardTemplateDTO:
    text: str
    buttons: Optional[list[list[InlineKeyboardButton]]] = None

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class FavoritesDTO:
    pass


@dataclass
class FavoriteInfoDTO:
    favorite_vacancies: list
    favorite_count: int
    following: bool

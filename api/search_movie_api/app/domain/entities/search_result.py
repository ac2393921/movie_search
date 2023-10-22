from typing import List

from app.domain.entities.entity import Entity
from app.domain.entities.movie import Movie


class SearchResult(Entity):
    id: str
    movies: List[Movie]
    total_hits: int

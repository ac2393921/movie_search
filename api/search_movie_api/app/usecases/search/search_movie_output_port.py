from typing import List

from app.domain.entities.movie import Movie
from pydantic import BaseModel


class SearchMovieOutputPort(BaseModel):
    movies: List[Movie] = []
    total_hits: int = 0

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy_utils import UUIDType

from be.models.base import Base


class GenreMovie(Base):
    __tablename__ = "genres_movies"
    movie_id = Column(
        UUIDType(binary=False),
        ForeignKey("movies.id", ondelete="CASCADE"),
        primary_key=True,
    )
    genre_id = Column(
        Integer, ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True
    )

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy_utils import UUIDType

from be.models.base import Base


class CastMovie(Base):
    __tablename__ = "casts_movies"
    movie_id = Column(
        UUIDType(binary=False),
        ForeignKey("movies.id", ondelete="CASCADE"),
        primary_key=True,
    )
    cast_id = Column(
        Integer, ForeignKey("casts.id", ondelete="CASCADE"), primary_key=True
    )

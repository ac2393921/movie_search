import uuid

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from be.models.base import Base
from be.models.cast_movie import CastMovie
from be.models.genre_movie import GenreMovie
from be.models.movie_porduction_country import MovieProductionCountry


class Movie(Base):
    # テーブル名
    __tablename__ = "movies"
    # カラムの定義
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    director_id = Column(
        Integer, ForeignKey("directors.id", ondelete="CASCADE"), nullable=True
    )
    content_type_id = Column(
        Integer, ForeignKey("content_types.id", ondelete="CASCADE"), nullable=True
    )
    title = Column(String(255), unique=False)
    description = Column(Text, unique=False)
    release_date = Column(DateTime, unique=False, nullable=True)
    score = Column(Float, nullable=True)

    genres = relationship(
        "Genre",
        secondary=GenreMovie.__tablename__,
        back_populates="movies",
    )

    casts = relationship(
        "Cast",
        secondary=CastMovie.__tablename__,
        back_populates="movies",
    )

    productin_countries = relationship(
        "ProductionCountry",
        secondary=MovieProductionCountry.__tablename__,
        back_populates="movies",
    )

    director = relationship(
        "Director",
        back_populates="movies",
    )

    content_type = relationship(
        "ContentType",
        back_populates="movies",
    )

    def __init__(
        self,
        id=None,
        director_id=None,
        content_type_id=None,
        title=None,
        description=None,
        release_date=None,
        score=None,
    ):
        self.id = id
        self.director_id = director_id
        self.content_type_id = content_type_id
        self.title = title
        self.description = description
        self.release_date = release_date
        self.score = score

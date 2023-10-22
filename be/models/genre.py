from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from be.models.base import Base
from be.models.genre_movie import GenreMovie


class Genre(Base):
    # テーブル名
    __tablename__ = "genres"
    # カラムの定義
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)

    movies = relationship(
        "Movie",
        secondary=GenreMovie.__tablename__,
        back_populates="genres",
    )

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

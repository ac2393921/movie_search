from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from be.models.base import Base
from be.models.cast_movie import CastMovie


class Cast(Base):
    # テーブル名
    __tablename__ = "casts"
    # カラムの定義
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    movies = relationship(
        "Movie", secondary=CastMovie.__tablename__, back_populates="casts"
    )

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

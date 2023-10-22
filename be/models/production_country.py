from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from be.models.base import Base
from be.models.movie_porduction_country import MovieProductionCountry


class ProductionCountry(Base):
    # テーブル名
    __tablename__ = "production_countries"
    # カラムの定義
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=False)

    movies = relationship(
        "Movie",
        secondary=MovieProductionCountry.__tablename__,
        back_populates="productin_countries",
    )

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

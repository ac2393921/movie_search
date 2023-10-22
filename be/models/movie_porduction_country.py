from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy_utils import UUIDType

from be.models.base import Base


class MovieProductionCountry(Base):
    __tablename__ = "movies_production_countries"
    movie_id = Column(
        UUIDType(binary=False),
        ForeignKey("movies.id", ondelete="CASCADE"),
        primary_key=True,
    )
    production_country_id = Column(
        Integer,
        ForeignKey("production_countries.id", ondelete="CASCADE"),
        primary_key=True,
    )

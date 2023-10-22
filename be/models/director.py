from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from be.models.base import Base


class Director(Base):
    # テーブル名
    __tablename__ = "directors"
    # カラムの定義
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)

    movies = relationship("Movie", back_populates="director")

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

import uuid

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        Text)
from sqlalchemy_utils import UUIDType

from api.models.base import Base


class Movie(Base):
  # テーブル名
  __tablename__ = 'movies'
  # カラムの定義
  id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
  director_id = Column(Integer, ForeignKey('directors.id', ondelete="CASCADE"), nullable=True)
  content_type_id = Column(Integer, ForeignKey('content_types.id', ondelete="CASCADE"), nullable=True)
  title = Column(String(255), unique=False)
  description = Column(Text, unique=False)
  release_date = Column(DateTime, unique=False, nullable=True)
  score = Column(Float, nullable=True)
  
  def __init__(self, id=None, director_id=None, content_type_id=None, title=None, description=None, release_date=None, score=None):
    self.id = id
    self.director_id = director_id
    self.content_type_id = content_type_id
    self.title = title
    self.description = description
    self.release_date = release_date
    self.score = score

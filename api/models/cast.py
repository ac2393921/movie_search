from sqlalchemy import Column, Integer, String

from api.models.base import Base


class Cast(Base):
  # テーブル名
  __tablename__ = 'casts'
  # カラムの定義
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255))
  
  def __init__(self, id=None, name=None):
    self.id = id
    self.name = name
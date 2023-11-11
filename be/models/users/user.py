import uuid

from sqlalchemy import Column, String
from sqlalchemy_utils import UUIDType

from be.models.users.base import Base


class User(Base):
    # テーブル名
    __tablename__ = "users"
    # カラムの定義
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def __init__(
        self,
        id=None,
        username=None,
        email=None,
        password=None,
    ):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

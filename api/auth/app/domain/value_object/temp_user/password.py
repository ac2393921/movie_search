from typing import Any

import bcrypt

from app.domain.value_object.value_object import ValueObject


class Password(ValueObject):
    value: bytes

    # パスワードのハッシュ化
    @classmethod
    def hash(cls, password: str) -> bytes:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password

    # パスワードの検証
    def verify(self, input_password: str):
        return bcrypt.checkpw(self.value, input_password)

    @classmethod
    def generate(cls, password: str) -> "Password":
        hashed_password = cls.hash(password)
        return cls(value=hashed_password)

    def __str__(self) -> str:
        return str(self.value, "utf-8")

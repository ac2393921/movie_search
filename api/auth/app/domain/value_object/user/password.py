import bcrypt

from app.domain.value_object.value_object import ValueObject


class Password(ValueObject):
    value: str

    # パスワードのハッシュ化
    def hash(self) -> bytes:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.value.encode("utf-8"), salt)
        return hashed_password

    # パスワードの検証
    def verify(self, input_password: str):
        return bcrypt.checkpw(self.value.encode("utf-8"), input_password)

    def __str__(self) -> str:
        return str(self.hash())

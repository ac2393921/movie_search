import secrets

from pydantic import constr

from app.domain.value_object.value_object import ValueObject


class Code(ValueObject):
    value: constr(min_length=6, max_length=6)

    @classmethod
    def generate(cls) -> "Code":
        # ランダムな6桁の確認コードを生成
        random_code = secrets.token_hex(3).upper()[:6]
        return cls(value=random_code)

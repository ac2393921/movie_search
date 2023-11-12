from uuid import uuid4

from app.domain.value_object.value_object import ValueObject


class TempUserId(ValueObject):
    value: str

    @classmethod
    def generate(cls):
        return cls(value=str(uuid4()))

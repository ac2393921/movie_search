from pydantic import EmailStr

from app.domain.value_object.value_object import ValueObject


class Email(ValueObject):
    value: EmailStr

    def __str__(self):
        return str(self.value)

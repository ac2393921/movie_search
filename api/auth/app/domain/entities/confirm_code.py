from app.domain.entities.entity import Entity
from app.domain.value_object.confirm_code.code import Code
from app.domain.value_object.confirm_code.confirm_code_id import ConfirmCodeId


class ConfirmCode(Entity):
    confirm_code_id: ConfirmCodeId
    code: Code

    @classmethod
    def generate(cls):
        return cls(
            confirm_code_id=ConfirmCodeId.generate(),
            code=Code.generate(),
        )

    @property
    def key(self):
        return str(self.code) + str(self.confirm_code_id)

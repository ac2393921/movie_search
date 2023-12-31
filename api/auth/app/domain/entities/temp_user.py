from typing import Optional

from app.domain.entities.entity import Entity
from app.domain.value_object.temp_user.confirm_code import ConfirmCode
from app.domain.value_object.temp_user.email import Email
from app.domain.value_object.temp_user.password import Password
from app.domain.value_object.temp_user.temp_user_id import TempUserId
from app.domain.value_object.temp_user.username import UserName


class ConfirmCodeMismatchError(Exception):
    """確認コードが一致しない場合に発生する例外"""


class StoredConfirmCodeIsNoneError(Exception):
    """作成された確認コードがNoneの場合に発生する例外"""


class InputConfirmCodeIsNoneError(Exception):
    """入力された確認コードがNoneの場合に発生する例外"""


class TempUser(Entity):
    temp_user_id: TempUserId
    username: UserName
    email: Email
    password: Password
    confirm_code: Optional[ConfirmCode]

    def __str__(self) -> str:
        return f"{self.temp_user_id.value} {self.username.value} {self.email.value} {self.password.decode()} {self.confirm_code.value}"

    @classmethod
    def generate(cls, username: str, email: str, password: str) -> "TempUser":
        return cls(
            temp_user_id=TempUserId.generate(),
            username=UserName(value=username),
            email=Email(value=email),
            password=Password.generate(password),
            confirm_code=None,
        )

    @classmethod
    def regenarate(cls, temp_user_id, username, email, password, confirm_code) -> "TempUser":
        return cls(
            temp_user_id=TempUserId(value=temp_user_id),
            username=UserName(value=username),
            email=Email(value=email),
            password=Password(value=password),
            confirm_code=ConfirmCode(value=confirm_code),
        )

    def generate_confirm_code(self) -> None:
        self.confirm_code = ConfirmCode.generate()

    def confirm(self, confirm_code: ConfirmCode) -> None:
        print(self.confirm_code)
        if confirm_code is None or confirm_code.value is None:
            raise InputConfirmCodeIsNoneError("confirm code is None")

        if self.confirm_code is None or self.confirm_code.value is None:
            raise StoredConfirmCodeIsNoneError("confirm code is None")

        if not self.confirm_code == confirm_code:
            raise ConfirmCodeMismatchError("confirm code is not match")

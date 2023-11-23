from app.domain.entities.entity import Entity
from app.domain.value_object.user.email import Email
from app.domain.value_object.user.password import Password
from app.domain.value_object.user.user_id import UserId
from app.domain.value_object.user.username import UserName


class PasswordMismatchError(Exception):
    """パスワードが一致しない場合に発生する例外"""


class User(Entity):
    user_id: UserId
    username: UserName
    email: Email
    password: Password

    @classmethod
    def generate(cls, username: str, email: str, password: str):
        return cls(
            user_id=UserId.generate(),
            username=UserName(value=username),
            email=Email(value=email),
            password=Password(value=password),
        )

    @classmethod
    def regenerate(cls, user_id: str, username: str, email: str, password: str):
        return cls(
            user_id=UserId(value=user_id),
            username=UserName(value=username),
            email=Email(value=email),
            password=Password(value=password),
        )

    def verify_password(self, password: str) -> None:
        if not self.password.verify(password):
            raise PasswordMismatchError("パスワードが一致しません。")

    def __str__(self) -> str:
        return f"{self.user_id} {self.username} {self.email} {self.password.decode()}"

from app.domain.entities.entity import Entity
from app.domain.value_object.user.email import Email
from app.domain.value_object.user.password import Password
from app.domain.value_object.user.user_id import UserId
from app.domain.value_object.user.username import UserName


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

    def __str__(self) -> str:
        return f"{self.user_id} {self.username} {self.email} {self.password.decode()}"

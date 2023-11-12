from app.domain.entities.entity import Entity
from app.domain.value_object.temp_user.confirm_code import ConfirmCode
from app.domain.value_object.temp_user.email import Email
from app.domain.value_object.temp_user.password import Password
from app.domain.value_object.temp_user.temp_user_id import TempUserId
from app.domain.value_object.temp_user.username import UserName


class TempUser(Entity):
    temp_user_id: TempUserId
    username: UserName
    email: Email
    password: Password
    confirm_code: ConfirmCode

    @classmethod
    def generate(cls, username, email, password):
        return cls(
            temp_user_id=TempUserId.generate(),
            username=UserName(value=username),
            email=Email(value=email),
            password=Password.generate(password),
            confirm_code=ConfirmCode.generate(),
        )

    def __str__(self) -> str:
        return f"{self.temp_user_id} {self.username} {self.email} {str(self.password)} {self.confirm_code}"

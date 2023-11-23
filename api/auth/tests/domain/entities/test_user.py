import pytest

from app.domain.entities.user import PasswordMismatchError, User
from app.domain.value_object.user.password import Password


class TestUser:

    # パスワードが一致する場合に例外が発生しないこと
    def test__can_verify_password(self):
        # arrange
        input_password = "password"
        hashed_password = Password.hash(input_password)
        user = User.generate(username="username", email="email@email.com", password=hashed_password,)

        # act
        user.verify_password("password")

    # パスワードが異なる場合に例外が発生すること
    def test__raise_when_password_is_invalid(self):
        # arrange
        input_password = "password"
        hashed_password = Password.hash(input_password)
        user = User.generate(username="username", email="email@email.com", password=hashed_password,)

        # act & assert
        with pytest.raises(PasswordMismatchError):
            user.verify_password("invalid_password")
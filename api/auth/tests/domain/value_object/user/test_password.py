from app.domain.value_object.user.password import Password


class TestUserPassword:
    # パスワードがハッシュ化されていること
    def test__can_hash_password(self):
        # arrange
        input = "password"

        # act
        actual = Password.hash(input)

        # assert
        assert actual != input
        assert isinstance(actual, bytes)

    # ハッシュ化したパスワードと値が一致した場合にTrueを返すこと
    def test__can_verify_password(self):
        # arrange
        input = "password"
        value_object = Password.generate(input)

        # act
        actual = value_object.verify(input)

        # assert
        assert actual is True

    # ハッシュ化したパスワードと値が一致しない場合にFalseを返すこと
    def test__can_verify_password__when_invalid(self):
        # arrange
        expect = "password"
        value_object = Password.generate(expect)
        invalid_password = "invalid_password"

        # act
        actual = value_object.verify(invalid_password)

        # assert
        assert actual is False

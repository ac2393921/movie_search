from app.domain.value_object.user.password import Password


class TestHashPassword:
    # パスワードがハッシュ化されていること
    def test__can_hash_password(self):
        # arrange
        input = "password"
        value_object = Password(value=input)

        # act
        actual = value_object.hash()

        # assert
        assert actual != input

    # ハッシュ化したパスワードと値が一致した場合にTrueを返すこと
    def test__can_verify_password(self):
        # arrange
        expect = "password"
        value_object = Password(value=expect)
        hashed_password = value_object.hash()

        # act
        actual = value_object.verify(hashed_password)

        # assert
        assert actual is True

    # ハッシュ化したパスワードと値が一致しない場合にFalseを返すこと
    def test__can_verify_password__when_invalid(self):
        # arrange
        expect = "password"
        value_object = Password(value=expect)
        invalid_hashed_password = Password(value="invalid").hash()

        # act
        actual = value_object.verify(invalid_hashed_password)

        # assert
        assert actual is False

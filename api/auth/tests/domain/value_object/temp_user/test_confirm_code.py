from app.domain.value_object.temp_user.confirm_code import ConfirmCode


class TestConfirmCode:
    def test__can_generate_random_confirm_code(self):
        # Arrange
        # Act
        code = ConfirmCode.generate()
        # Assert
        assert isinstance(code, ConfirmCode)

    def test__can_generate_random_confirm_code__with_6_digits(self):
        # Arrange
        # Act
        code = ConfirmCode.generate()
        # Assert
        assert len(code.value) == 6
        assert isinstance(code.value, str)

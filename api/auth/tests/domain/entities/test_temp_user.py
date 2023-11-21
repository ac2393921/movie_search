import pytest

from app.domain.entities.temp_user import (ConfirmCodeMismatchError,
                                           InputConfirmCodeIsNoneError,
                                           StoredConfirmCodeIsNoneError,
                                           TempUser)
from app.domain.value_object.temp_user.confirm_code import ConfirmCode


class TestTempUser:
    # 確認コードが一致する場合に例外が発生しないこと
    def test__can_confirm(self):
        # arrange
        temp_user = TempUser.generate("username", "email@email.com", "password",)
        temp_user.generate_confirm_code()
        confirm_code = temp_user.confirm_code

        # act
        temp_user.confirm(confirm_code)

    # 確認コードが異なる場合にConfirmCodeMismatchErrorが発生すること
    def test__when_confirm_code_is_invalid(self):
        # arrange
        temp_user = TempUser.generate("username", "email@email.com", "password",)
        temp_user.generate_confirm_code()
        invalid_confirm_code = ConfirmCode.generate()

        # act & assert
        with pytest.raises(ConfirmCodeMismatchError):
            temp_user.confirm(invalid_confirm_code)

    # 入力された確認コードがNoneの場合にInputConfirmCodeIsNoneErrorが発生すること
    def test__when_input_confirm_code_is_none(self):
        # arrange
        temp_user = TempUser.generate("username", "email@email.com", "password",)
        temp_user.generate_confirm_code()

        # act & assert
        with pytest.raises(InputConfirmCodeIsNoneError):
            temp_user.confirm(None)

    # 生成された確認コードがNoneの場合にStoredConfirmCodeIsNoneErrorが発生すること
    def test__when_confirm_code_is_noen(self):
        # arrange
        temp_user = TempUser.generate("username", "email@email.com", "password",)
        correct_confirm_code = ConfirmCode.generate()

        # act & assert
        with pytest.raises(StoredConfirmCodeIsNoneError):
            temp_user.confirm(correct_confirm_code)

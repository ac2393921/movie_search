import pytest

from app.domain.domain_service.user_existence_checker import (
    DuplicateError,
    UserExistenceChecker,
)
from app.domain.entities.user import User


class TestUserExistenceChecker:
    # ユーザーが存在した場合にDuplicateErrorが発生させること
    def test_user_exists(self, mocker):
        # arrange
        email = "test@test.mail"
        # UserRepositoryのモックを作成
        user_repository_mock = mocker.Mock()
        # fetch_by_emailメソッドが呼ばれた時に、モックの返り値を設定
        user_repository_mock.fetch_by_email.return_value = User.generate(
            username="test",
            email=email,
            password="test",
        )
        user_checker = UserExistenceChecker(user_repository_mock)

        # act
        # assert
        with pytest.raises(DuplicateError):
            user_checker.check_by_email(email)

    # ユーザーが存在しない場合にDuplicateErrorが発生しないこと
    def test_user_does_not_exist(self, mocker):
        # arrange
        email = "test@test.mail"
        # UserRepositoryのモックを作成
        user_repository_mock = mocker.Mock()
        # fetch_by_emailメソッドが呼ばれた時に、モックの返り値を設定
        user_repository_mock.fetch_by_email.return_value = None
        user_checker = UserExistenceChecker(user_repository_mock)

        # act
        user_checker.check_by_email(email)

        # assert
        # user_repository_mock.fetch_by_emailが1回呼ばれたことを確認
        user_repository_mock.fetch_by_email.assert_called_once_with(email=email)

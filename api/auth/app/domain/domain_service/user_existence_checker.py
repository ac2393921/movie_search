from app.domain.repositories.user.user_repository import UserRepository


class DuplicateError(Exception):
    """Userが既に存在している場合に発生するエラー"""


class NotFoundUserError(Exception):
    """Userが存在しない場合に発生するエラー"""


class UserExistenceChecker:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def check_exist_by_email(self, email: str):
        user = self._user_repository.fetch_by_email(email=email)

        if user is None:
            raise NotFoundUserError("ユーザーが存在しません")

    def check_not_exist_by_email(self, email: str):
        user = self._user_repository.fetch_by_email(email=email)

        if user is not None:
            raise DuplicateError("ユーザーが既に存在しています")

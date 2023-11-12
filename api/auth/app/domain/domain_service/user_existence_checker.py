from app.domain.repositories.user.user_repository import UserRepository


class DuplicateError(Exception):
    def __init__(self, message="Duplicate value found."):
        self.message = message
        super().__init__(self.message)


class UserExistenceChecker:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def check_by_email(self, email: str):
        user = self._user_repository.fetch_by_email(email=email)

        if user is not None:
            raise DuplicateError("ユーザーが既に存在しています")

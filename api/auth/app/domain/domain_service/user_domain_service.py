from app.domain.repositories.user.user_repository import UserRepository


class UserDomainService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def exist_by_email(self, email: str):
        user = self._user_repository.fetch_by_email(email=email)

        if user is not None:
            raise Exception("ユーザーが既に存在しています")

from logging import getLogger

from app.domain.domain_service.token_generator import TokenGenerator
from app.domain.domain_service.user_existence_checker import \
    UserExistenceChecker
from app.domain.repositories.user.user_repository import UserRepository
from app.usecases.auth.sign_in.input_port import SingInInputPort
from app.usecases.auth.sign_in.output_port import SingInOutputPort

logger = getLogger("uvicorn.app")


class SingInInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
    ) -> None:
        self._user_repository = user_repository

    def handle(self, input: SingInInputPort) -> SingInOutputPort:
        # ユーザーが存在するか確認
        user_existence_checker = UserExistenceChecker(
            user_repository=self._user_repository,
        )
        user_existence_checker.check_exist_by_email(email=input.email)

        # ユーザーが存在していたらemailよりユーザ情報を取得
        user = self._user_repository.fetch_by_email(input.email)

        # ユーザーのパスワードが一致するか確認
        user.verify_password(input.password)

        # ユーザー情報からJWTを作成
        token = TokenGenerator.generate_token(user)
        logger.info(f"token: {token}")

        return SingInOutputPort(token=token)

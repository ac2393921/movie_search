from logging import getLogger

from app.domain.domain_service.user_existence_checker import \
    UserExistenceChecker
from app.domain.entities.temp_user import TempUser
from app.domain.repositories.temp_user.temp_user_repository import \
    TempUserRepository
from app.domain.repositories.user.user_repository import UserRepository
from app.domain.value_object.temp_user.email import Email
from app.usecases.auth.temporary_register.input_port import \
    TemporaryRegisterInputPort
from app.usecases.auth.temporary_register.output_port import \
    TemporaryRegisterOutputPort

logger = getLogger("uvicorn.app")


class TemporaryRegisterInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
        temp_user_repository: TempUserRepository,
    ) -> None:
        self._user_repository = user_repository
        self._temp_user_repository = temp_user_repository

    def handle(self, input: TemporaryRegisterInputPort):
        # 登録可能なメールか確認
        user_existence_checker = UserExistenceChecker(
            user_repository=self._user_repository,
        )
        user_existence_checker.check_not_exist_by_email(input.email)
        logger.info(f"登録可能なメールです。email: {input.email}")

        # 一時的なユーザー情報を生成
        # 確認コードも作成される
        temp_user = TempUser.generate(
            username=input.username,
            email=input.email,
            password=input.password,
        )
        temp_user.generate_confirm_code()
        logger.info("確認コードを生成しました。")

        self._temp_user_repository.save(temp_user)
        logger.info(
            f"一時的なユーザー情報をキャッシュサーバーに保存しました。temp_user_id: {temp_user.temp_user_id}"
        )

        # メール送信
        # TODO: メール送信処理を実装する

        return TemporaryRegisterOutputPort(
            temp_user_id=str(temp_user.temp_user_id),
        )

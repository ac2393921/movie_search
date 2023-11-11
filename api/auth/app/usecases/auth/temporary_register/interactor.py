from app.domain.domain_service.user_domain_service import UserDomainService
from app.domain.repositories.user.user_repository import UserRepository
from app.domain.value_object.password import Password
from app.usecases.auth.temporary_register.input_port import TemporaryRegisterInputPort
from app.usecases.auth.temporary_register.output_port import TemporaryRegisterOutputPort


class TemporaryRegisterInteractor:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def handle(self, input: TemporaryRegisterInputPort):
        # 登録可能なメールか確認
        user_domain_service = UserDomainService(
            user_repository=self._user_repository,
        )
        user_domain_service.exist_by_email(input.email)

        # パスワードハッシュ化
        password = Password(value=input.password)
        hash_password = password.hash()

        # ユーザ情報をキャッシュに保存

        # キャッシュサーバーに保存するkeyの作成

        # キャッシュのサーバーに保存するvalueを作成

        # 保存

        # メール送信

        return TemporaryRegisterOutputPort(
            username=input.username,
            email=input.email,
            password=input.password,
        )
